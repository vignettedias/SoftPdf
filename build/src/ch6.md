Architectural design is concerned with understanding how a software system should be organized and designing the overall structure of that system. It is the critical link between design and requirements engineering, as it identifies the main structural components in a system and the relationships between them. The output of the architectural design process is an architectural model that describes how the system is organized as a set of communicating components.

Software architecture is the overall structure of the software: its components and the manner in which those components interact. It provides the framework within which detailed design is carried out. An architectural design must specify three kinds of property:

1. *Structural properties* The components of the system (modules, objects, filters) and the ways in which they are packaged and interact.
2. *Extra-functional properties* How the architecture achieves the requirements for performance, security, reliability, adaptability, and other non-functional characteristics. The architecture is the main place where these are decided, because they depend on how the whole system is organized rather than on any single component.
3. *Families of related systems* The architecture should draw on repeatable patterns that are common to families of similar systems, so that proven designs are reused rather than reinvented.

## 6.1 Architectural design decisions

Architectural design is a creative process, and the decisions made depend on the type of system being developed, the background and experience of the architect, and the specific requirements. A small number of structural concepts, however, recur in every architecture: the control hierarchy of the program, the way it is partitioned, and the way its data is logically organized.

### 6.1.1 Control hierarchy

Control hierarchy, also called program structure, is the organization of program components (modules) that shows how control flows from one module to another. Higher-level components manage and delegate tasks to lower-level components. The hierarchy is drawn as a tree-like structure chart. It does not show the sequence of processing, the order of decisions, or the repetition of operations; it shows only which module invokes which.

The following terms describe a control hierarchy:

1. *Depth* The number of levels of control.
2. *Width* The overall span of control: the largest number of modules at any one level.
3. *Fan-out* The number of modules directly controlled by a given module.
4. *Fan-in* The number of modules that directly control a given module.
5. *Superordinate module* A module that controls another module.
6. *Subordinate module* A module that is controlled by another module.

[[fig:lms-hierarchy]] is the control hierarchy of a library management system. When a user borrows a book, the main application calls the transaction management module, which in turn uses the book inventory to check availability.

@fig lms-hierarchy

Fan-in and fan-out are easily reversed. Fan-out is outgoing control (whom a module calls); fan-in is incoming control (who calls it). A useful check follows from the fact that both count the same arrows: the sum of all fan-outs in a structure chart equals the sum of all fan-ins. As design heuristics, fan-out should be kept moderate, since a module with very high fan-out makes too many decisions and should be factored with an intermediate control level, while fan-in should increase towards the bottom of the hierarchy, because a module with high fan-in is being reused.

::: example ex-fan | Measuring a control hierarchy
For the structure chart in [[fig:fan-chart]], find the depth and width of the hierarchy and the fan-in and fan-out of every module.

@fig fan-chart
--- solution
The levels are {A}, {B, C, D}, and {E, F, G}, so the depth is 3 and the width is max(1, 3, 3) = 3. Counting arrows leaving and entering each module:

1. Fan-out: A = 3, B = 2, C = 2, D = 1, and E = F = G = 0.
2. Fan-in: A = 0, B = C = D = E = 1, and F = G = 2.

Check: the sum of the fan-outs is 3 + 2 + 2 + 1 = 8 and the sum of the fan-ins is 1 + 1 + 1 + 1 + 2 + 2 = 8.
--- answer
Depth 3, width 3. F and G have fan-in 2: they are shared utilities, which is desirable provided they are functionally cohesive. A is superordinate to B, C, and D; B and C are superordinate to F.
:::

For the library system of [[fig:lms-hierarchy]], the same measures give depth 3 and width 8; the main application has fan-out 3, user management and book inventory 3 each, transaction management 2, and every module except the main application has fan-in 1.

### 6.1.2 Structural partitioning

If the architectural style of a system is hierarchical, the program structure can be partitioned both horizontally and vertically.

*Horizontal partitioning* splits the software into separate branches of the hierarchy for each major function. In its simplest form there are three partitions: input (data collection and preprocessing), process (core computation), and output (presentation of results). Equivalently, the system is divided into layers or tiers by functionality, such as presentation, business logic, and data storage ([[fig:lms-horizontal]]). The user interface can then be changed without affecting business logic or storage. Horizontal partitioning makes the software easier to test and maintain, gives fewer side effects because errors do not spread easily, and makes new functions easy to add. Its disadvantages are that more data must be passed across module interfaces and that the control of program flow becomes more complex.

@fig lms-horizontal

*Vertical partitioning*, also called *factoring*, organizes the program top-down so that control and decision-making reside in the upper-level modules, while the lower-level modules are workers that perform input, computation, and output ([[fig:lms-vertical]]). The reason for doing this is the effect of change. A change in a control module affects all its subordinates, whereas a change in a worker module has minimal impact on other modules. Because most requirement changes affect input, computation, or output, which are done by workers, a factored structure is easier to maintain.

@fig lms-vertical

### 6.1.3 Logical data representation

Logical data representation defines how data elements relate to each other: how the data is structured and organized in terms of logical relationships between entities, independently of physical storage. It specifies the data organization, the methods of access, the associations between data items, and the processing alternatives. [[fig:lms-logical]] shows the library system. A transaction links a user to a book, recording that the user has borrowed it. The logical view is the same whether the data is kept in a relational database, a NoSQL store, or flat files.

@fig lms-logical

## 6.2 Architectural views

It is impossible to represent all relevant information about a system's architecture in a single model. An architectural design can be represented by five kinds of model:

1. *Structural model* The architecture as an organized collection of program components and their interactions. Example: a layered web application with presentation, business-logic, and data-access layers.
2. *Framework model* Raises the level of abstraction by identifying repeatable architectural frameworks found in similar applications. Example: the model–view–controller (MVC) framework, in which the model manages data, the view handles the user interface, and the controller processes input.
3. *Dynamic model* The behavioral aspects of the architecture: how the structure or configuration changes in response to external events. Example: a traffic-monitoring system that adjusts signals from live traffic data.
4. *Process model* The business or technical processes that the system must accommodate, focusing on how tasks are executed. Example: order placement → payment → inventory check → shipping.
5. *Functional model* The functional hierarchy of the system: how functions are decomposed and depend on one another. Example: 'Manage accounts' decomposed into 'Create account', 'Deposit money', and 'Withdraw money'.

For the library system, the structural view divides the system into user management, book inventory, and transaction management ([[fig:lms-structural]]). The framework view might use a web framework such as Django or Spring Boot, which supplies authentication, object–relational mapping for the inventory, URL routing for borrow and return requests, and templates for the pages. The dynamic view is expressed as behavior over time ([[fig:lms-dynamic]]), and the functional view simply lists what the system does: register user, log in, search books, borrow book, and return book.

@fig lms-structural

@fig lms-dynamic

## 6.3 Architectural patterns

An architectural pattern (or style) is a stylized description of good design practice, which has been tried and tested in different environments. Patterns include information about when they are and when they are not useful, and a pattern gives a designer a starting point with known strengths and weaknesses. Three patterns are described here.

### 6.3.1 Layered architecture

The layered architecture pattern organizes the system into layers, each of which provides services to the layer above it ([[fig:layered-pattern]]). The lowest layers represent core services, such as the operating system and database, that are used throughout the system; the top layer provides the user interface. [[fig:layered-generic]] is a generic four-layer architecture.

@fig layered-pattern

@fig layered-generic

The layered approach supports the incremental development of systems. As a layer is developed, some of the services provided by that layer may be made available to users. The architecture is also changeable and portable: as long as its interface is unchanged, a layer can be replaced by another, equivalent layer, and when layer interfaces change only the adjacent layer is affected.

### 6.3.2 Client–server architecture

In a client–server architecture, the functionality of the system is organized into services, with each service delivered from a separate server, and clients use the services by making requests to the servers ([[fig:cs-pattern]]). The major components are a set of servers that offer services, a set of clients that call on those services, and a network that allows the clients to access the services. [[fig:cs-film]] shows a film library in which separate servers manage the catalogue, videos, pictures, and web pages.

@fig cs-pattern

@fig cs-film

Clients have to know the names of the available servers and the services they provide, but servers do not need to know the identity of the clients or how many clients are accessing them. The principal advantage of the pattern is that servers can be distributed across a network and replicated when load is high.

### 6.3.3 Call-and-return architecture

A call-and-return architecture decomposes the system into a hierarchy of procedures or components in which control passes downward by calls and results pass back upward by returns. In its classic form, the *main program/subprogram* architecture, a main program invokes controller subprograms, which in turn invoke worker components ([[fig:call-return]]). A *remote procedure call* architecture has the same structure, but the components are distributed across computers on a network. Call-and-return architectures are easy to understand and to scale: new functionality is added as new subprograms. Their weakness is that each caller waits for its callee, so a slow component delays everything above it.

@fig call-return

The program structures produced by architectural mapping (Section 6.4) are call-and-return architectures.

::: example ex-arch-fd | Architectural styles for a food-delivery system
A food-delivery company runs apps for customers, restaurants, and delivery partners. Customers browse menus and place orders; restaurants accept and prepare them; delivery partners are assigned and tracked in real time; payments are processed through a payment gateway. Explain how the client–server, layered, and call-and-return architectures apply to this system, and draw the layered architecture.
--- solution
The three styles describe different aspects of the same system, so they are used together.

1. *Client–server* The three mobile apps are clients. They send requests (browse menus, place an order, update location) to servers that provide the services: order processing, restaurant management, delivery allocation, payment processing, and tracking. The client–server style is chosen because many clients in many places must share the same data, and because servers can be replicated to handle peak loads at meal times.
2. *Layered* Within the servers the software is organized into layers: a presentation layer (the interfaces of the three apps), an application layer (order processing, restaurant management, delivery allocation, tracking), a business-logic layer (payment processing, validation rules, the notification service), and a data layer (order, customer, restaurant, payment, and tracking databases). Each layer uses only the services of the layer below. A change of database or payment provider is confined to one layer.
3. *Call-and-return* The flow of control for a request follows call-and-return. When a customer places an order, the client app calls the order service; the order service calls the payment service; the payment service calls the database and the payment gateway; each returns its result to its caller. Each call waits for its response before the caller continues.
--- answer
The system is a client–server system whose server side is layered and whose request handling is call-and-return ([[fig:fd-layered]]). The client–server style gives scalability and shared data; layering gives separation of concerns and replaceable layers; call-and-return gives a simple, predictable flow of control. For this system the client–server style has four advantages: order, payment, and tracking data are managed centrally; server capacity can be increased for meal-time peaks; sensitive payment data stays on secure servers; and updates are made once, on the server. Its disadvantages are that a server failure stops every client, that all three apps need a stable network connection, that heavy traffic can make the servers a bottleneck, and that the server infrastructure is costly.

@fig fd-layered
:::

## 6.4 Architectural mapping using data flow

Requirements models for many systems include data-flow diagrams. Architectural mapping is the method that converts a DFD into a program structure with a call-and-return architecture. It has six steps:

1. Identify the type of information flow: transform flow or transaction flow.
2. Define the flow boundaries: where data enters and leaves the processing core.
3. Map the DFD into the program structure.
4. Define the control hierarchy by factoring.
5. Refine the design using design heuristics, to improve functional independence (high cohesion and low coupling, Chapter 7).
6. Elaborate and document the architectural description.

Two kinds of information flow determine the detailed procedure ([[fig:flow-types]]). In *transform flow*, data enters the system along incoming paths, is converted from an external form to an internal representation, is processed at a *transform centre*, and leaves along outgoing paths after conversion back to an external form. The overall flow is linear. In *transaction flow*, a single data item, the transaction, triggers one of several alternative flows of processing. A *transaction centre* evaluates the transaction and routes it to the appropriate action path.

@fig flow-types

### 6.4.1 Transform mapping

Transform mapping is the set of design steps that converts a DFD exhibiting transform flow into a program structure with separate input, transform, and output branches under a main controller. The steps are:

1. Confirm that the DFD exhibits transform flow.
2. Define the flow boundaries. The *incoming boundary* is drawn where external data has become internal, valid data; the *outgoing boundary* where internal results begin to be converted to external form.
3. Identify the transform centre: the processes between the two boundaries.
4. Perform *first-level factoring*: a main controller at the top, with an input controller, a transform controller, and an output controller beneath it.
5. Perform *second-level factoring*: map each DFD process into a module beneath the controller of its domain.
6. Refine the structure to improve cohesion and reduce coupling.

::: example ex-payroll | Transform mapping of a payroll system
A payroll system receives working hours from employees, fetches employee details from a data store, validates the data, calculates pay, generates payslips, and updates the payroll records ([[fig:payroll-dfd]]). Map the DFD into a program structure.

@fig payroll-dfd
--- solution
*Step 1.* There is one input stream and one path through the system, so the flow is transform flow.

*Steps 2–3.* Before Validate data completes, the hours are still raw external data; afterwards they are trusted internal data, so the incoming boundary is drawn after process 1.2. Generate payslip begins converting results into an external document, so the outgoing boundary is drawn before process 1.4. The input domain is therefore {Collect work hours, Validate data}, the transform centre is {Calculate pay}, and the output domain is {Generate payslip, Update records}.

*Step 4.* First-level factoring places a main controller, Payroll system, over three controllers ([[fig:payroll-l1]]).

@fig payroll-l1

*Step 5.* Second-level factoring places each process beneath the controller of its domain ([[fig:payroll-l2]]).

*Step 6.* Each worker module performs one task and receives only the data it needs; Calculate pay, for example, receives validated hours and the rate. If Collect work hours and Validate data are always used together and are small, they may be merged into a single 'Get valid hours' module; if Calculate pay is complex, it may be factored further into gross pay, deductions, and net pay. Controllers make decisions and workers do not call controllers, so control passes downward only.
--- answer
The program structure is: Payroll system → {Input controller → (Collect work hours, Validate data); Transform controller → (Calculate pay); Output controller → (Generate payslip, Update records)}. Drawing the DFD processes themselves as the final architecture, without the controllers, would not be a transform mapping.
:::

@fig payroll-l2

### 6.4.2 Transaction mapping

Transaction mapping converts a DFD exhibiting transaction flow into a program structure with an incoming (reception) branch and a dispatch branch in which a transaction dispatcher controls one subordinate module per action path. The steps are:

1. Identify the transaction centre: the process that controls branching, such as a request handler or menu process.
2. Identify the input transactions: the external triggers that activate the different paths.
3. Establish the processing path (action path) for each transaction type.
4. Map the DFD to a program structure: a dispatcher module with one module per transaction type.
5. Refine the architecture, factoring each action path further where needed.

::: example ex-atm | Transaction mapping of an ATM
At an ATM, a user's menu choice is sent to a menu selection process, which passes control to Withdraw, Deposit, or Balance enquiry ([[fig:atm-dfd]]). Map the DFD into a program structure.

@fig atm-dfd
--- solution
One input triggers one of several mutually exclusive paths, so the flow is transaction flow and Menu selection is the transaction centre. The centre becomes a transaction dispatcher, each action path becomes a subordinate module, and a reception branch obtains the menu choice ([[fig:atm-structure]]).

@fig atm-structure

Each transaction module is then factored into its own action path. Withdraw controls Get amount, Check balance, Dispense cash, and Update account; Deposit controls Accept cash, Verify amount, and Update account. The shared module Update account then has fan-in 2, which is good reuse. An action path may itself have transform flow (Withdraw reads an amount, computes a new balance, and dispenses cash), in which case it is mapped by transform mapping beneath the dispatcher.
--- answer
ATM system → {Read menu selection (reception); Menu selection process (dispatcher) → Withdraw, Deposit, Balance enquiry}. A new transaction such as Transfer funds is added as one more subordinate of the dispatcher, without changing the existing modules.
:::

The two mappings differ in their key element (a transform centre or a transaction centre), in their top structure (input, transform, and output controllers, or a reception branch and a dispatcher), and in the way a feature is added (usually a new module in one domain, or a new module under the dispatcher). A student-records processor that reads scores, validates them, computes grades, and prints grade reports has transform flow; a library kiosk that offers Issue, Return, Renew, and Search has transaction flow.

::: keypoints
- A software architecture describes the components of a system and how they interact. An architectural design must specify structural properties, extra-functional properties, and families of related systems.
- A control hierarchy is described by its depth, width, fan-in, and fan-out and by superordinate and subordinate modules. The sum of fan-outs equals the sum of fan-ins.
- Horizontal partitioning divides the program into branches or layers by major function; vertical partitioning (factoring) puts control at the top and workers at the bottom, so that most changes affect only workers.
- An architecture can be described by structural, framework, dynamic, process, and functional models.
- The layered, client–server, and call-and-return patterns are frequently combined: clients request services from servers whose software is layered and whose requests are handled by calls and returns.
- Architectural mapping converts a DFD into a program structure. Transform mapping identifies incoming and outgoing boundaries and a transform centre and factors the structure into input, transform, and output branches; transaction mapping identifies a transaction centre and builds a dispatcher with one module per action path.
:::
