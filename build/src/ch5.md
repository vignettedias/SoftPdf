System modeling is the process of creating abstract, visual representations of a system to understand, define, and communicate its requirements before implementation. Each model presents a different view or perspective of that system, and the models act as a bridge between vague user needs and precise technical specifications. They ensure that stakeholders and developers share a common understanding of what is to be built.

Models make structure, behavior, and interactions easier to understand than text alone; they clarify vague requirements and reduce miscommunication; they give developers, clients, and testers a common visual language; they support traceability and the generation of test cases and documentation; and they expose missing requirements and design flaws early, when they are cheap to fix. Above all, a model is an abstraction: it deliberately leaves out detail so that the engineer can concentrate on one perspective at a time.

A system may be modeled from five perspectives:

1. A *context* perspective, which models the environment of the system and its interactions with external entities.
2. An *interaction* perspective, which models how the system interacts with its users and how its components communicate.
3. A *structural* perspective, which models the organization of the system's components and their relationships.
4. A *behavioral* perspective, which models how the system behaves in response to inputs and events.
5. A *data* perspective, which models the structure and organization of the data within the system.

Three families of notation are used. Data-flow diagrams (DFDs) model context and the flow of data; entity–relationship (ER) diagrams model the structure of data (entities, their attributes, and the relationships between them); and the Unified Modeling Language (UML) covers all five perspectives. The UML is a standardized, general-purpose modeling language used to visualize, specify, construct, and document the artifacts of a software-intensive system. It is essentially a blueprint language for software. A UML model is more than a drawing: it is a collection of diagrams and model elements that together form a formal representation of the system's architecture, structure, and behavior, so that developers, technical writers, and business analysts can each understand the system at the level of detail relevant to them.

UML diagrams fall into two categories ([[fig:uml-types]]). *Structural diagrams* show the static elements of a system and their relationships, irrespective of time. They represent the 'nouns' of the system (classes, objects, components) and are used for planning and documenting architecture. *Behavioral diagrams* show the dynamic behavior of the system and its interactions over time. They represent the 'verbs' (actions and events) and are used to analyze user interactions and run-time behavior.

@fig uml-types

The structural diagrams are: the *class diagram*, which shows classes, their attributes and operations, and their relationships; the *object diagram*, a snapshot of instances and their links at one point in time; the *component diagram*, which shows how the system is divided into modular components and their dependencies; the *deployment diagram*, which shows hardware nodes and the software artifacts deployed on them; the *package diagram*, which organizes model elements into logical groups to manage complexity; and the *composite structure diagram*, which shows the internal parts and ports of a class or component.

The behavioral diagrams are: the *use case diagram*, which captures high-level functional requirements as interactions between actors and use cases; the *activity diagram*, a flowchart of the steps of a business process or operation; the *state machine diagram*, which models the life cycle of a single object as states and the events that cause transitions between them; and four *interaction diagrams*. Of these, the *sequence diagram* shows how objects interact in chronological order; the *communication diagram* (called a collaboration diagram in earlier versions of the UML) shows the same information but emphasizes the links between objects rather than timing; the *interaction overview diagram* combines activity and sequence diagrams to give a high-level view of the flow of control; and the *timing diagram* shows the precise timing of state changes along a linear time axis.

## 5.1 Context models

At an early stage in the specification of a system, you should decide on the system boundaries. This involves working with system stakeholders to decide what functionality should be included in the system and what is provided by the system's environment. A context model is a visual representation that models the system as a single process interacting with external entities. It defines the system boundary, its scope, and its major inputs and outputs, without showing any internal detail.

The usual form of context model is the *context diagram*, which is the top level (level 0) of a set of data-flow diagrams. A DFD visually represents the flow of data through a system, using standardized symbols for processes, data stores, external entities, and data flows to show inputs, outputs, transformations, and storage without describing implementation. The four elements are shown in [[fig:dfd-symbols]]:

1. *External entities* are sources or sinks of data outside the system: people, organizations, or other systems. They are drawn as rectangles.
2. *Processes* transform incoming data into outgoing data. They are drawn as circles (bubbles), numbered, and named with a verb phrase such as 'Validate order'.
3. *Data flows* show the movement of data and are drawn as labeled arrows.
4. *Data stores* are repositories where data is held between processes. They are drawn as open-ended rectangles.

@fig dfd-symbols

In the context diagram the whole system is a single process. [[fig:sales-context]] is the context diagram of a sales order system. It shows at once who uses the system (managers, employees, and customers) and what data crosses the boundary in each direction. In requirements engineering this gives a broad, stakeholder-friendly view that is used to clarify requirements, identify the interfaces that must be specified, and prevent scope creep: any proposed function that does not correspond to one of the flows on the context diagram is outside the agreed scope.

A context diagram says nothing about how the system works internally; its processes are revealed by decomposing it into lower-level DFDs (Section 5.4.1).

@fig sales-context

## 5.2 Interaction models

Interaction models show how users interact with the system, how the system interacts with other systems, and how its components interact. Modeling user interaction helps to identify user requirements; modeling component interaction shows whether a proposed structure can deliver the required performance and dependability.

### 5.2.1 Use case modeling

A use case diagram illustrates how users (actors) interact with a system to achieve specific goals. It captures:

1. *Actors*, the roles that interact with the system, such as users or external systems, drawn as stick figures.
2. *Use cases*, the functions or actions that the system performs for an actor, such as 'Borrow book', drawn as ellipses.
3. *Relationships*, which show how actors and use cases are connected: associations, includes, and extends.

A use case diagram focuses on user goals, the system boundary, and high-level functionality without technical detail, and so it is used early to clarify requirements. Two relationships between use cases are important:

1. *«include»* is a mandatory dependency: the base use case cannot complete without executing the included use case, which is always performed as part of the base use case's workflow. It is drawn as a dashed arrow labeled «include» pointing from the base use case to the included use case.
2. *«extend»* is a conditional dependency: the extending use case executes only if a particular condition is met during the base use case, and the base use case can complete successfully without it. It is drawn as a dashed arrow labeled «extend» pointing from the extending use case to the base use case, and the condition is documented.

[[fig:lib-usecase]] shows the use cases of a library system. A member searches for, borrows, and returns books and views their account; a librarian adds books and manages members. Borrowing a book always includes checking that the book is available and that the member's account is in good standing, so these are «include» relationships. A fine is generated only when a book is returned late, so 'Generate fine' extends 'Return book'.

@fig lib-usecase

Each use case should also be documented in more detail, as a text description (actors, preconditions, main and alternative flows, postconditions) or as a sequence diagram.

### 5.2.2 Sequence diagrams

A sequence diagram is an interaction diagram that shows how objects interact with each other over time. It emphasizes the chronological order of the messages exchanged between objects to achieve a specific behavior, and it is used to model workflows, processes, and interactions between components. Its elements are:

1. *Lifelines*, which represent the objects or participants in the interaction. Each is drawn as a named box with a vertical dashed line below it.
2. *Messages*, drawn as arrows from one lifeline to another, labeled with the operation or signal and usually numbered.
3. *Activation bars*, narrow rectangles on a lifeline showing when an object is actively processing a message.
4. *Return messages*, optional dashed arrows that show a response or return value.
5. *Combined fragments*, boxes that represent conditional logic, loops, or parallel execution. The operator in the top-left corner is, for example, *alt* (alternatives, each with a guard), *opt* (an optional part executed only if its guard is true), or *loop*.
6. *Actors*, the external entities that take part in the interaction.

Time runs from top to bottom. [[fig:lib-sequence]] shows a student member borrowing a book. The member searches, the library checks availability with the book object, and the result is displayed. If the book is available, the *opt* fragment is executed: the member confirms, the book is reserved, a loan is created, and the book's status is updated.

::: example ex-pay-seq | A sequence model for payment processing
A food-delivery service lets customers order from restaurants through a mobile app. Draw a sequence model for the payment step, from placing the order to confirming payment, including the case in which the bank rejects the payment.
--- solution
The participants are the Customer (an actor), the App, the Order System, the Payment Gateway, the Bank Server, and the Order Database. The order is saved first with status PENDING so that a failed payment does not lose the customer's cart. The gateway asks the bank to authorize the amount and returns the result to the order system. The two outcomes are alternatives, so they are placed in an *alt* fragment with the guards [approved] and [rejected] ([[fig:swiggy-seq]]).

@fig swiggy-seq
--- answer
The message sequence is: 1 placeOrder (Customer→App); 2 createOrder (App→Order System); 3 save order as PENDING (Order System→Order DB); 4 requestPayment (Order System→Payment Gateway); 5 authorize (Gateway→Bank); 6 approved or rejected (Bank→Gateway); 7 payment status (Gateway→Order System); then, in the *alt* fragment, either 8 update status to PAID and 9 confirm to the app, or 10 update status to FAILED and 11 report failure so that the customer can retry; finally 12 the app shows the result to the customer.
:::

::: example ex-ticket | Use cases and a booking sequence for a ticket reservation system
A ticket reservation system for a public transport network integrates real-time seat availability, fare calculation, passenger details, and payment. The fare depends on the distance, the ticket type (adult, child, senior), and peak-hour pricing. (a) Model the interaction between users and the system. (b) Model the ticket booking scenario.
--- solution
(a) The interaction between users and the system is modeled by a use case diagram ([[fig:ticket-usecase]]). The actors are the Passenger, the Admin who maintains the fare rules, and the external Payment gateway. Booking always includes calculating the fare and making the payment. Concessions and peak-hour surcharges apply only under a condition, so they extend 'Calculate fare'.

@fig ticket-usecase

(b) A scenario, which is an ordered set of interactions, is modeled by a sequence diagram ([[fig:ticket-seq]]). Every fare parameter appears as an argument of the fare message (distance, ticket type, and time of travel), and the peak-hour surcharge is placed in an *opt* fragment. The seat is held while the fare is calculated and paid for, and is confirmed only after payment succeeds.

@fig ticket-seq
--- answer
(a) A use case diagram with actors Passenger, Admin, and Payment gateway, and use cases Search seats, Book ticket («include» Calculate fare and Make payment), Cancel ticket, View booking, and Manage fares, with 'Apply concession / peak pricing' «extend» 'Calculate fare'. (b) A sequence diagram whose messages run: search, find seats, check availability, select seat and enter passenger details, hold seat, fare(distance, type, time) with an optional peak-hour surcharge, pay, confirm seat, and issue the ticket.
:::

### 5.2.3 Communication diagrams

A communication diagram (also known as a collaboration diagram) is another type of interaction diagram. It emphasizes the relationships between objects and shows how messages are exchanged within a particular context. Unlike a sequence diagram, it does not show time as a separate dimension; instead it shows the structural organization of the objects and their connections. Its elements are:

1. *Objects and links* Objects are rectangles labeled with their class names, and links are lines connecting objects that show associations between them.
2. *Messages* Each message is written beside a link with an arrow and a sequence number that gives the order of the interactions, for example '1: searchBook', '2: checkAvailability'. The label describes the action taking place.

@fig lib-sequence

[[fig:lib-comm]] is the communication diagram for the same borrowing interaction as [[fig:lib-sequence]]. The two diagrams contain the same information, and tools can generate one from the other. A sequence diagram is better when the order of messages is what matters; a communication diagram is better when you want to see which objects must be linked.

@fig lib-comm

## 5.3 Structural models

Structural models show the organization of a system in terms of its components and their relationships.

### 5.3.1 Class diagrams

A class diagram is a structural diagram that visualizes the static design of a system. It shows classes with their attributes and operations, the relationships between classes, and the constraints and multiplicities of those relationships (for example, one-to-many). It serves as a blueprint for an object-oriented system and clarifies how its parts relate before implementation.

A class is drawn as a rectangle with three compartments: the name, the attributes, and the operations. Visibility is shown by a prefix: + for public and − for private. Six kinds of relationship are used ([[fig:class-rels]]):

1. *Association* A general relationship between classes, meaning that objects of one class are linked to objects of the other; drawn as a solid line. Example: Student enrolls in Course.
2. *Aggregation* A whole–part relationship in which the parts can exist independently of the whole; drawn with a hollow diamond at the whole. Example: a Department has Professors, who continue to exist if the department is closed.
3. *Composition* A strong whole–part relationship in which the parts cannot exist without the whole; drawn with a filled diamond at the whole. Example: a House has Rooms; if the house is destroyed, so are its rooms.
4. *Generalization* An 'is-a' relationship in which a subclass inherits from a superclass; drawn as a solid line with a hollow triangle pointing to the superclass. Example: ElectricCar is a Car.
5. *Dependency* A temporary 'uses' relationship in which one class uses another, for example as a parameter; drawn as a dashed arrow. Example: ReportGenerator uses Data.
6. *Realization* A class implements an interface; drawn as a dashed line with a hollow triangle pointing to the interface.

Generalization and realization are easily confused because both use a hollow triangle. The difference is the line: a *solid* line means that the subclass inherits the structure and behavior of a superclass; a *dashed* line means that a class promises to implement the operations declared by an interface.

*Multiplicity* (cardinality) is written at each end of an association to say how many objects take part: 1 (exactly one), 0..1 (zero or one), \* or 0..\* (any number), 1..\* (at least one), or a range such as 1..4.

[[fig:lib-class]] is a class diagram of a library system. A Library is composed of Books and Loans: if the library is deleted, its books and loan records are deleted too. Members and Librarians are aggregated by the library, because a person can exist independently of it (a student might graduate but still exist as a person). Each Loan links exactly one Book to exactly one Member, while a book or a member may have many loans over time. Faculty and Student are types of Member that have different borrowing rules, so they are subclasses connected by generalization, each overriding getMaxBooks().

@fig class-rels

@fig lib-class

::: example ex-crc | Principal and collaborating classes of a food-delivery system
A food-delivery system processes orders placed with restaurants, takes payments, assigns delivery partners, and tracks deliveries in real time. Identify the principal classes of the system and the classes each one collaborates with.
--- solution
A class is identified by its responsibilities: what it knows and what it does. Its *collaborators* are the other classes whose services it must use to meet those responsibilities. This is the basis of Class–Responsibility–Collaborator (CRC) modeling.

Some of these classes are also *active classes* in the strict UML sense: an active class is one whose objects own their own thread of control and so can initiate activity, rather than only responding to calls. The Delivery Partner Allocator (continuously matching orders to free partners), the Real-Time Tracker (continuously receiving GPS updates), and the Notification Service (sending messages asynchronously) are active; they are drawn with double vertical borders in a class diagram. Customer, by contrast, is best modeled as an actor that uses the system, together with a passive Customer class that holds the customer's data. A tempting wrong answer is to call every class that 'does something' an active class.
--- answer
The principal classes, their responsibilities, and their collaborators are listed in [[fig:fd-crc]]. Of these, the Delivery Partner Allocator, the Real-Time Tracker, and the Notification Service are active classes.

@fig fd-crc
:::

::: example ex-card | Implications of multiplicity in a class model
For the food-delivery system, draw a class diagram showing the multiplicities of the main associations and explain how the multiplicities affect implementation.
--- solution
[[fig:fd-class]] shows the model. A Customer places zero or more Orders; each Order belongs to one Customer and one Restaurant, has exactly one Payment, is composed of one or more OrderItems, and is assigned to zero or one DeliveryPartner (none until a partner accepts it).

@fig fd-class
--- answer
Multiplicity determines three things in the implementation:

1. *Database design* A one-to-many association (Customer 1 — 0..\* Order) becomes a foreign key in the 'many' table (Order.customerId); a many-to-many association needs a separate link table; a composition (Order ◆— OrderItem) means that item rows are deleted with their order.
2. *Object and memory structure* An end with multiplicity 1 or 0..1 becomes a single reference (order.payment); an end with \* becomes a collection (customer.orders). A lower bound of 0 means that the reference may be null and the code must handle that case.
3. *Constraint enforcement* Bounds are business rules that the code must check: exactly one payment per order, at least one item per order, and at most one delivery partner per order.
:::

::: example ex-uni | A class model and a sequence diagram for university accounts
Each student has a University Account with an account id and a student name. Based on this account the student has a Link Account with an e-mail address and a password; the password can be reset, but the e-mail address cannot be changed. The link account is used to access Blackboard and Zoom. Blackboard holds a list of courses and supports adding courses and downloading and uploading homework. Zoom holds a list of meetings and can create and delete meetings. Each Course has a course id and name and has at least one meeting and one homework. A Meeting has a unique meeting id and an invitation link, and joining it by id requires the password. Each Homework has a course id, a homework number, and a list of questions. (a) Draw the class diagram. (b) Model the interaction among the objects when a student joins the online lecture of a course.
--- solution
(a) The nouns give the classes, their properties give the attributes, and the verbs give the operations ([[fig:uni-class]]). A Link Account cannot exist without its University Account, so the relationship is a composition. Blackboard and Zoom own their lists of courses and meetings, which are also compositions. Blackboard and Zoom *use* the link account for access, which is a dependency. The multiplicity 1..\* records that each course has at least one meeting and at least one homework, and {readOnly} records that the e-mail address cannot be changed.

@fig uni-class

(b) The interaction involves the Student, the Zoom application, the University account server, and the Zoom server ([[fig:zoom-seq]]). The link account is authenticated first; the meeting password is then checked by the Zoom server, and the two outcomes are shown in an *alt* fragment.

@fig zoom-seq
--- answer
(a) Classes UniversityAccount, LinkAccount, Blackboard, Zoom, Course, Meeting, and Homework with the attributes and operations shown, composition from UniversityAccount to LinkAccount, from Blackboard to Course, and from Zoom to Meeting, and Course associated with 1..\* Homework and 1..\* Meeting. (b) Messages: join(meetingId); authenticate(email, password); token; joinMeeting(id, password, token); then either admit and stream, or an error message.
:::

### 5.3.2 Component and deployment diagrams

A *component diagram* shows how a system is divided into modular, replaceable components and how they depend on one another. A component is an encapsulated unit with provided and required interfaces; it may represent a physical artifact (a JAR file, a DLL, a container) or a logical service. It is drawn as a rectangle with the component icon. An *interface* is a contract that defines the operations a component offers (a *provided* interface, drawn as a 'lollipop') or needs (a *required* interface). A *frame* may enclose related components to show a subsystem. The relationships are *dependency* (a dashed arrow: a change in the target may affect the source), *interface realization* (the component implements an interface's operations), and *component realization* (the component is physically built from other artifacts, marked «build»). [[fig:lib-component]] is a component diagram of the library system.

@fig lib-component

A *deployment diagram* shows the physical hardware on which software is deployed. A *node* is a physical or virtual computational resource, drawn as a three-dimensional box: a *device node* is hardware such as a server or a phone, and an *execution environment node* is a software container such as a JVM, a Docker container, or an operating system. An *artifact* is a file or deliverable deployed on a node, such as library-core.jar. A *communication path*, a solid line between nodes, is labeled with the protocol used, such as HTTPS or JDBC. A *deployment specification*, a note attached to a deployment, gives configuration parameters such as memory limits. Nodes may be nested, for example a container inside a virtual machine. [[fig:lib-deploy]] shows the library system deployed on four nodes.

@fig lib-deploy

## 5.4 Behavioral models

Behavioral models are models of the dynamic behavior of a system as it is executing. They show what happens or what is supposed to happen when a system responds to a stimulus from its environment. Stimuli are of two types: *data*, where some data arrives that has to be processed, and *events*, which trigger system processing. Many business systems are data-processing systems that are primarily driven by data; real-time systems are often event-driven.

### 5.4.1 Data-driven modeling

Data-driven models show the sequence of actions involved in processing input data and generating an associated output. DFDs are the classic notation. They are simple and intuitive, and it is usually possible to explain them to potential system users who can then participate in validating the model.

DFDs are drawn as a hierarchy of levels. This book uses the convention that the context diagram is *level 0*:

1. *Level 0 (context diagram)* The system is a single process, numbered 0.0, interacting with external entities (Section 5.1).
2. *Level 1* The single process is decomposed into its main sub-processes, typically three to seven, numbered 1.0, 2.0, and so on. Data stores and detailed data flows are added, while the inputs and outputs of the context diagram are preserved. For example, a payment system might be broken into processing, invoicing, and confirmation.
3. *Level 2* Each level-1 process is refined into more detailed steps, numbered 1.1, 1.2, and so on, with its own flows and stores; for example, payment processing is refined into payment verification and funds deduction.
4. *Level 3 and below* Further detail is added for complex systems, until every input–process–output needed for implementation has been mapped.

Some texts call the context diagram the 'context level' and the first decomposition 'level 0'. The diagrams are the same; only the labels differ. Whichever convention is used, it should be stated and applied consistently.

A DFD is created top-down. Start with level 0 by identifying the external entities and the high-level data exchanged with them. Then decompose iteratively: select a process, expand it in the next level, add sub-processes and data stores, and verify that the new diagram is balanced. Stop at primitive processes that need no further breakdown. The following rules keep a set of DFDs correct:

1. *Balancing rule* The inputs and outputs of a parent process must match exactly those of its child diagram, so that data flow is continuous across levels without additions or omissions.
2. *No data flow between entities* External entities interact only with processes, never directly with each other or with data stores. Entities represent the system boundary, not internal components.
3. *Process naming* Processes are named with verb–noun phrases, such as 'Validate order', that describe a data transformation; vague labels such as 'Process data' are avoided.
4. *Data-flow constraints* Flows carry data only, never control signals. They are labeled and directional, and they connect entities or processes to stores but never entity to entity. A flow out of a store is a read; a flow into a store is a write.
5. *Validity rules* Every process must have at least one input and one output. A process with inputs but no outputs is a *black hole*; a process with outputs but no inputs is a *miracle*. Data stores need flows in both directions if they are updated and read.

The lemonade stand is a simple example. The system has four activities: a customer places an order for lemonade; the stand owner makes the lemonade; the customer pays; and the owner serves the lemonade. [[fig:lemon-l0]] is its context diagram. The customer, the employee, and the vendor who supplies the ingredients are the external entities.

@fig lemon-l0

At level 1 ([[fig:lemon-l1]]), the single process is decomposed into four processes: 1.0 Sale, 2.0 Production, 3.0 Procurement, and 4.0 Payroll. Every flow on the context diagram appears again, now connected to the process that handles it: the customer's order and payment go to Sale, the served product comes from Production, and so on. New internal flows, such as the product ordered passing from Sale to Production, appear for the first time.

@fig lemon-l1

At level 2, each process is decomposed again. [[fig:lemon-l2]] shows process 1.0, Sale, as three processes that record the order, receive the payment, and produce the sales forecast from the stored orders and payments. Its external flows (customer order and payment in; product ordered and sales forecast out) are exactly those of process 1.0 at level 1, so the diagrams balance. [[fig:lemon-tree]] summarizes the whole decomposition.

@fig lemon-l2

@fig lemon-tree

::: example ex-records | Data and data-flow models of an academic record system
In an academic record system, courses are created with a course number, credits, and a syllabus. Students (roll number, address, semester) are admitted and register for courses. The marks for each subject are keyed in, the semester weighted average (SWA) is calculated from the credits, the marks are combined with previous marks into a cumulative weighted average, and the marks and SWA are formatted and printed. A student with an SWA of 85 or higher is placed on the Vice-Chancellor's list; a student with an SWA below 50 is placed on conditional standing. (a) Draw an entity–relationship diagram. (b) Draw the context diagram and the level-1 DFD.
--- solution
(a) An entity–relationship (ER) diagram models the data perspective: entities (things about which data is kept), their attributes, and the relationships between them with their cardinalities. A student registers for many courses and a course has many students, so the many-to-many relationship is resolved by an Enrollment entity that also holds the marks. A student has one transcript *per semester*, so Student to Transcript is one-to-many ([[fig:rec-er]]).

(b) The context diagram shows the whole system as one process and the four external entities that exchange data with it ([[fig:rec-context]]). A context diagram has exactly one process; a list of the system's functions belongs to level 1, not level 0.

@fig rec-er

@fig rec-context

At level 1 the process is decomposed into six processes with four data stores ([[fig:rec-l1]]). Every flow on the context diagram appears on the level-1 diagram, so the two diagrams balance.

@fig rec-l1
--- answer
(a) Entities Student, Course, Enrollment (RollNo, CourseNo, Semester, Marks), and Transcript (RollNo, Semester, SWA), with Student 1–N Enrollment N–1 Course and Student 1–N Transcript. (b) Context: Registrar, Faculty, Student, and Academic office around process 0.0. Level 1: 1.0 Maintain courses, 2.0 Admit and register, 3.0 Record marks, 4.0 Compute SWA, 5.0 Print grade report, and 6.0 Determine standing (SWA ≥ 85 → Vice-Chancellor's list; SWA < 50 → conditional standing), with stores D1 Courses, D2 Students, D3 Enrollments, and D4 Transcripts.
:::

Activity diagrams are the UML's notation for data-driven and workflow models. An activity diagram represents the flow of activities or actions within a system. It is used to model workflows, business processes, algorithms, and the steps of use cases, showing how tasks are performed sequentially or concurrently. Its notation is:

1. *Start node*, a solid circle marking the beginning of the activity; *end node*, a solid circle with a border marking its termination.
2. *Action*, a rounded rectangle representing one task or step.
3. *Decision node*, a diamond at which the flow branches according to guard conditions written in brackets; *merge node*, also a diamond, which combines alternative flows.
4. *Fork* and *join*, thick bars. A fork splits one flow into several concurrent flows; a join waits for all of them and merges them into one.
5. *Flow*, an arrow showing the direction of control between actions and decisions.
6. *Swimlanes*, vertical or horizontal partitions that group actions by the actor or system responsible for them.

[[fig:lib-activity]] shows borrowing a book with swimlanes for the member, the library system, and the librarian. If the book is available it is reserved and borrowing is confirmed; the book status, the member profile, and the notifications are then updated in parallel, and the join waits for all three before the book is issued. Each action is placed in the lane of whoever performs it, which is the main value of swimlanes: they show responsibilities.

@fig lib-activity

### 5.4.2 Event-driven modeling

Event-driven modeling shows how a system responds to external and internal events. It is based on the assumption that a system has a finite number of states and that events (stimuli) may cause a transition from one state to another. A state represents a condition or situation during the lifetime of an object, and transitions represent changes from one state to another. The UML supports event-based modeling using state machine diagrams (state charts). The notation is:

1. *States*, rounded rectangles, each a specific condition of the object; the *initial state*, a solid circle; and the *final state*, a solid circle with a border.
2. *Transitions*, arrows between states, showing how the object moves from one state to another.
3. *Events*, written on transitions to name the trigger, for example *reserve* or *return*.
4. *Guard conditions*, Boolean conditions in square brackets that must be true for the transition to fire, for example [member eligible].
5. *Actions*, written after a slash, performed during a transition or within a state, for example /updateStatus or /generateFine.
6. *Composite states*, states that contain substates and so group related states; and the *history state*, a circle containing H, which returns the machine to the last active substate when a composite state is re-entered.

[[fig:lib-state]] models the life of a book. A new book is Available; it may be Reserved and then issued, or issued directly; while On loan it becomes Overdue if the due date passes. A returned book becomes Available again, and a fine is generated if it was overdue. Only a damaged book that is Withdrawn leaves the machine. Note that returning a book does not end its life: a state diagram whose final state follows 'Returned' would model a single loan, not the book.

@fig lib-state

## 5.5 Building a requirements model

The models of this chapter are complementary, and a complete requirements model uses several of them. It is useful to group them into four kinds of element:

1. *Scenario-based elements* describe the system from the user's point of view: use cases and their text descriptions, use case diagrams, and activity and swimlane diagrams. They are usually the first part of the model to be developed, and they drive the others.
2. *Class-based elements* describe the objects that the system manipulates, their attributes and operations, and their relationships: class diagrams, CRC models, and collaboration diagrams.
3. *Behavioral elements* describe how the system responds to external events: state diagrams and sequence diagrams.
4. *Flow-oriented elements* describe how data is transformed as it moves through the system: data-flow diagrams, control-flow diagrams, and processing narratives.

The elements are not alternatives. Each answers a different question (who uses the system and for what, what it knows, how it reacts, and how data moves through it), and a reviewer can check them against each other: every use case should be supported by classes and operations, and every data flow should be produced and consumed by some process.

::: example ex-antivirus-model | A requirements model for an antivirus product
A client requires antivirus software with: signature-based, heuristic, and machine-learning detection; real-time monitoring and protection of the system and web traffic; automatic malware removal; low resource consumption; daily updates from the vendor's server; an attractive user interface; code security; and compliance with legal requirements. Build the requirements model using the elements of the requirements model.
--- solution
The requirements are first classified (see [[ex:ex-antivirus-req]] in Chapter 4): the detection, monitoring, removal, and update requirements are functional and are modeled below, while the efficiency, usability, security, and legal requirements are non-functional and are recorded as constraints on the model.

*Scenario-based element.* The actors are the User and the vendor's Update Server. The use cases are Run scan, Configure real-time protection, Quarantine or remove malware, View threat report, and Update definitions. Removal happens only when a threat is found, so it extends scanning ([[fig:av-usecase]]).

*Class-based element.* A ScanEngine uses one or more Detectors. Detector is an interface, realized by SignatureDetector, HeuristicDetector, and MLDetector, so that a new detection technique can be added without changing the engine. Infected files are passed to the Quarantine ([[fig:av-class]]).

@fig av-usecase

@fig av-class

*Behavioral element.* The engine monitors file and web events, scans each one, and returns to monitoring or, if the file is malicious, quarantines it and notifies the user; updates are installed in a separate state, so scans never use half-installed definitions ([[fig:av-state]]).

*Flow-oriented element.* Scanning is decomposed into intercepting the file, analyzing it against the signature store, and taking action, which quarantines infected files and reports to the user ([[fig:av-dfd]]).

@fig av-state

@fig av-dfd
--- answer
The model consists of the use case diagram (scenario-based), the class diagram (class-based), the state diagram of the engine (behavioral), and the level-1 DFD of scanning (flow-oriented), with the measurable non-functional constraints of [[ex:ex-antivirus-req]].
:::

::: keypoints
- A model is an abstract view of a system that ignores some details. Complementary models show the system's context, interactions, structure, behavior, and data.
- The UML has structural diagrams (class, object, component, deployment, package, composite structure) and behavioral diagrams (use case, activity, state machine, and the interaction diagrams: sequence, communication, timing, and interaction overview).
- Context models show the system boundary and the external entities that exchange data with the system. The context diagram is the level-0 DFD.
- DFDs are decomposed level by level; each child diagram must balance with its parent, and entities, processes, flows, and stores must obey the DFD rules.
- Use case diagrams show actors and their goals, with «include» for mandatory and «extend» for conditional behavior. Sequence and communication diagrams show the messages exchanged between objects.
- Class diagrams show classes, their attributes and operations, and association, aggregation, composition, generalization, dependency, and realization relationships, with multiplicities that determine keys, collections, and constraints in the implementation.
- Activity diagrams show workflows with decisions, forks, joins, and swimlanes; state diagrams show how an object's state changes in response to events, guarded by conditions and accompanied by actions.
- A requirements model combines scenario-based, class-based, behavioral, and flow-oriented elements.
:::
