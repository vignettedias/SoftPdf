Software design is the activity in which the *what* of a system, captured in the requirements model, is converted into the *how* of a buildable solution. It is an iterative process that translates requirements into a blueprint for constructing the software. It begins with a high-level, abstract representation and becomes progressively more detailed, while every refinement remains traceable to the requirements.

Design is a core part of software engineering and is applied whatever software process is used: waterfall, incremental, spiral, or agile. It begins after the requirements have been analyzed and modeled, and it is the last modeling step before construction (code generation and testing). Design matters for several reasons. It determines how easily the software can be built and later changed; it is the place where quality is established, since quality cannot be added after coding; it produces representations that can be assessed before any code exists; and it is the foundation for coding, testing, deployment, and maintenance. Without design, the result is a system that is unstable, difficult to test, and impossible to assess.

This chapter describes the design model and the principles and concepts of good design, the measures of module quality called cohesion and coupling, and the design of user interfaces.

## 7.1 The design model and design principles

The requirements model of Chapter 5 contains scenario-based, class-based, flow-oriented, and behavioral elements. Design uses these elements to produce four design models ([[fig:design-pyramid]]):

1. *Data/class design* converts analysis classes into design classes and defines the data structures required for implementation. It forms the base of the pyramid, because every other design decision depends on the data the system manipulates.
2. *Architectural design* defines the relationships between the major structural elements of the software, using architectural styles and patterns (Chapter 6).
3. *Interface design* specifies how the software communicates with other systems and with the people who use it: the flow of information across the system boundary and the associated behavior (Section 7.4).
4. *Component-level design* converts the structural elements of the architecture into procedural descriptions of each component: its internal algorithms and data.

The correspondence is not one-to-one. Every design model draws on several analysis elements; component-level design, for example, uses class-based, flow, and behavioral models together.

@fig design-pyramid

### 7.1.1 Quality and principles of design

A design is evaluated through technical reviews. A good design must implement all the explicit requirements of the requirements model and accommodate the implicit requirements expected by stakeholders; it must be a readable, understandable guide for those who code, test, and support the software; and it must give a complete picture of the software, addressing the data, functional, and behavioral domains from an implementation perspective.

Ten principles guide both the design process and the design product:

1. *Avoid tunnel vision* Consider all requirements and alternative approaches, not a single aspect such as performance.
2. *Be traceable to the analysis model* Every design element should have a justification in the requirements, so that nothing is omitted and nothing unnecessary is added.
3. *Do not reinvent the wheel* Reuse libraries, components, and proven patterns.
4. *Minimize intellectual distance* Structure the software as the real-world problem is structured; a library system whose modules are members, books, and loans is easier to understand than one organized around arbitrary technical divisions.
5. *Exhibit uniformity and integration* Keep structure, style, and logic consistent across components developed by different teams.
6. *Accommodate change* Use modular, scalable structures that absorb new requirements.
7. *Degrade gracefully* Bad data or errors must not crash the whole system; error handling and fallbacks keep it running with reduced function.
8. *Design is not coding, and coding is not design* Design plans structure at a higher level of abstraction than code, even when it includes pseudocode for complex algorithms.
9. *Assess quality during design* Evaluate efficiency, scalability, and correctness while designing, not at the end.
10. *Review to minimize conceptual errors* Peer reviews catch logical flaws before they reach the code.

The design process itself proceeds top-down in three iterative stages ([[fig:design-process]]). The system interface, the architecture, and the detailed design are each generated, documented, and evaluated in turn; after each evaluation the designer may return and improve the document, and the process ends with a formal review of the complete design.

@fig design-process

## 7.2 Design concepts

Design concepts help designers answer three questions: how the software should be divided into smaller components; how the details of functions and data structures can be separated from the overall conceptual representation of the software; and what criteria define the quality of a design. Abstraction and refinement answer the second question; modularity, separation of concerns, and architecture the first; cohesion, coupling, and the design principles the third.

### 7.2.1 Abstraction

Abstraction is the process of hiding implementation details and showing only the essential features of a system. At the highest level of abstraction a solution is stated in the language of the problem domain; at lower levels it is described more and more procedurally, until at the lowest level it can be implemented directly. Abstraction reduces complexity because, at any moment, the designer deals only with the details relevant at the current level. There are three types:

1. *Procedural abstraction* A process is broken into named procedures that perform specific tasks without exposing their implementation. A function calculateInterest(principal, rate, time) computes interest without revealing the formula.
2. *Data abstraction* A data structure is defined so that its implementation is hidden and only the necessary operations are exposed. A Calculator class whose result attribute is private and read only through getResult() can later store the result differently without affecting its callers.
3. *Control abstraction* The details of control flow are hidden so that the programmer thinks about the task rather than the mechanism. A for-each loop or an iterator replaces manual management of loop counters; a menu-driven runCalculator() function hides the loop, the switch statement, and the termination logic.

Abstraction is related to, but not the same as, encapsulation. Abstraction is a design concept concerned with *what* is exposed; encapsulation (information hiding) is the mechanism, such as the private keyword, that prevents access to what is not exposed.

### 7.2.2 Design patterns and separation of concerns

A *design pattern* is a proven solution to a recurring design problem, recorded with its context and the essential structure of the solution so that it can be reused. A pattern helps a designer decide whether it applies to the current problem, whether it can be reused to save effort, and whether it can guide the development of a similar pattern. Model–view–controller, singleton, and observer are familiar examples.

*Separation of concerns* is the principle that a complex problem is easier to solve when it is broken into pieces that can each be solved and optimized independently. A *concern* is a feature or behavior specified in the requirements. The justification is divide and conquer: solving one large problem is harder than solving several small ones. Separation of concerns is the principle; modularity, abstraction, functional independence, and refinement are the techniques that realize it.

### 7.2.3 Modularity

Modularity is the practice of dividing a system into smaller, manageable, and independent components called modules, which can be combined to form the complete system. A monolithic program cannot easily be understood by one reader, because the number of control paths, variables, and interactions is too large. Dividing it into modules makes each part intellectually manageable. Modularity makes software easier to understand, improves reuse, simplifies debugging and maintenance, allows new features to be added as new modules, and allows teams to work in parallel.

Five criteria are used to evaluate how well a design method supports effective modularity:

1. *Modular decomposability* The problem can be divided systematically into subproblems, such as a banking system divided into account management, loan processing, and transactions.
2. *Modular composability* Existing modules can be assembled into new systems, such as a payment-gateway module reused across e-commerce platforms.
3. *Modular understandability* Each module can be understood as a standalone unit.
4. *Modular continuity* Small changes in requirements affect individual modules only; a change in tax rules affects only the tax module.
5. *Modular protection* An error inside one module does not propagate to others.

More modules are not always better. As the number of modules increases, the cost of developing each module falls, but the cost of integrating them (interfaces, calls, communication) rises ([[fig:modularity-cost]]). Too few modules give *undermodularity*, with large, complex modules approaching a monolith; too many give *overmodularity*, with high integration cost. The total cost is lowest in a region around some number M of modules, which cannot be predicted exactly but which a designer should aim for.

@fig modularity-cost

### 7.2.4 Refinement and refactoring

*Refinement* (stepwise refinement) is a top-down strategy in which a function is elaborated level by level, from an abstract statement to detailed procedural steps that can be coded directly ([[fig:login-refine]]). Abstraction and refinement are complementary: abstraction lets a designer state a procedure while suppressing detail, and refinement reveals the detail as design proceeds. Refinement in design corresponds to partitioning in requirements analysis.

@fig login-refine

*Refactoring* is a reorganization technique that improves the internal structure of a design or its code without changing its external behavior. Its purposes are to eliminate redundancy and unused elements, to improve efficiency, and to enhance readability, maintainability, and scalability. A designer looks for poorly constructed elements, low-cohesion components that perform unrelated functions, and unnecessary complexity. For example, a ReportManager that fetches sales records, computes statistics, and e-mails a PDF can be split into SalesRepository, SalesStatistics, and ReportMailer; managers receive the same report, but each component now has one responsibility. Refactoring does not fix defects, because it does not change behavior; debugging does.

## 7.3 Cohesion and coupling

Component-level design defines the internal structure of each module identified by the architecture. Its quality is judged by two complementary measures. *Cohesion* looks inside a module and asks how strongly its elements belong together. *Coupling* looks between modules and asks how strongly they depend on one another. Together they express *functional independence*: a module is functionally independent when it has a single, well-defined purpose (high cohesion) and a minimal, simple interface to other modules (low coupling). The rule *high cohesion, low coupling* is the most important principle of modular design.

### 7.3.1 Cohesion

Cohesion is the degree to which the elements inside a module (its functions, data, and statements) are related to each other and belong together. A highly cohesive module performs a single, well-defined task. A module with low cohesion groups loosely related or unrelated functionality, which makes it harder to understand, test, and change. Seven levels of cohesion are distinguished, from lowest to highest ([[fig:cohesion-scale]]). Some texts omit procedural and sequential cohesion and use a five-level scale; this book uses the full seven-level scale.

@fig cohesion-scale

1. *Coincidental cohesion* (lowest) Unrelated functions are grouped together for no reason, usually through lack of planning; for example, a module that prints a report, clears the screen, and plays music. A change to one task risks disturbing the others that happen to live beside it.
2. *Logical cohesion* Functions that perform logically similar operations, or that belong to the same category, are grouped together, and the one executed is selected by an external control such as a flag. An output_handler(output_type, data) that prints to screen, printer, or file according to output_type is logically cohesive. Every value of the flag must be tested, and a new output type requires changing the shared module.
3. *Temporal cohesion* Functions are grouped because they are executed at the same time or in response to the same event, not because they are related: for example, a start-up module that initializes variables, opens files, and clears the screen, or a set of actions all triggered when an order is updated.
4. *Procedural cohesion* Elements are grouped because they must be executed in a fixed order, although they do not operate on the same data; for example, check permissions, then open the file, then log the access.
5. *Communicational cohesion* Elements are grouped because they operate on the same data: get a temperature, log it, and display it. The functions share an input or output, which ties them together.
6. *Sequential cohesion* Elements are grouped because the output of one is the input of the next, like a chain: read the order, validate it, and compute its total.
7. *Functional cohesion* (highest) Every element contributes to a single, well-defined task; for example, calculate_average(numbers).

A practical test is to describe the module in one sentence. If the sentence has a single verb and object ('computes the average'), the module is functionally cohesive. If it needs 'and' joining unrelated activities, cohesion is lower; 'at start-up' or 'when … happens' suggests temporal cohesion; 'first … then …' suggests procedural cohesion; 'depending on the flag' or 'of this kind' suggests logical cohesion.

Higher cohesion is desirable because a module that focuses on one task is easier to understand and modify, has clear expected results and is therefore easier to test, and is self-contained and therefore easier to reuse and extend.

::: example ex-coh-code | Classifying the cohesion of two code fragments
These fragments illustrate a measure within a module that influences maintainability and reuse. Identify the type of cohesion (the bonding within the module) in each and state whether it is high or low.

```
(i)  def calculate_average(numbers):
         """Calculates the average of a list of numbers."""
         if not numbers:
             return 0
         return sum(numbers) / len(numbers)

(ii) class Utility:
         def print_message(self, message):
             print(message)
         def calculate_square(self, number):
             return number * number
         def read_file(self, filename):
             with open(filename, 'r') as file:
                 return file.read()
```
--- solution
The measure within a module is cohesion (the measure between modules is coupling). Apply the one-sentence test to each module.

(i) 'calculate_average computes the average of a list of numbers.' One verb, one object: every statement, including the empty-list guard, contributes to that result.

(ii) 'Utility prints a message *and* squares a number *and* reads a file.' The three methods share no data, no order of execution, and no purpose; they have been placed together only because each is a 'utility'.
--- answer
(i) Functional cohesion, which is high and desirable: all elements contribute to a single, well-defined task. (ii) Coincidental cohesion, which is low and undesirable: the elements are grouped arbitrarily with no logical relationship. Utility should be split, for example into a messaging module, a math module, and a file module.
:::

::: example ex-coh-fd | Cohesion in the modules of a food-delivery system
Classify the cohesion of each of the following modules of a food-delivery order system.

1. The Order Validation module performs a single purpose: checking that an order is valid.
2. An order-placement module whose steps form a chain: it validates the order, passes the validated order to its pricing step, and passes the priced order to its submission step.
3. A module processes the order ID, the items, and the restaurant ID, all using the same order record.
4. A module performs its tasks in a fixed order: check the restaurant is open, then lock the cart, then start the payment.
5. GPS updates and ETA calculation are grouped together because they belong to the same category of 'location functions', and a parameter selects which is performed.
6. Notifications to the customer, the restaurant, and the delivery partner are grouped because they are all triggered at the same moment, when the order status is updated.
7. Database operations are grouped because they all work on the same shared order data.
8. Unrelated tasks (applying a coupon, rotating log files, and refreshing the banner images) are placed together.
9. The Payment Gateway module has one responsibility: obtaining payment authorization.
10. Start-up tasks (loading configuration, connecting to the database, warming the menu cache) are executed at the same time.
--- solution
Ask for each module why its elements are together: one task (functional), a data chain (sequential), shared data (communicational), fixed order (procedural), same time or event (temporal), same category chosen by a flag (logical), or no reason (coincidental).
--- answer
1. Functional. 2. Sequential. 3. Communicational. 4. Procedural. 5. Logical. 6. Temporal. 7. Communicational. 8. Coincidental. 9. Functional. 10. Temporal.
:::

### 7.3.2 Coupling

Coupling is the degree of interdependence between modules: how closely one module is connected to another. Low coupling is desirable because it makes the system more modular and easier to maintain, test, and extend; high coupling increases complexity and makes change ripple from module to module. Six types are distinguished, from strongest (worst) to weakest (best) ([[fig:coupling-scale]]):

@fig coupling-scale

1. *Content coupling* One module directly modifies, or relies on, the internal data or logic of another, for example by setting module_b.internal_data = 42. It violates information hiding: if B changes its internals, A breaks.
2. *Common coupling* Several modules share global data, such as a global configuration dictionary. A fault seen in one module may be caused by any other module that writes the global data.
3. *External coupling* Modules depend on an externally imposed format, protocol, device, or service, such as a third-party authentication API. The system is exposed to changes or failures outside its control.
4. *Control coupling* One module controls the behavior of another by passing a control flag, as in function_b('start'). The caller must know about the callee's internal decisions; the callee in control coupling usually has logical cohesion.
5. *Stamp coupling* A whole data structure is passed when only part of it is needed, as when process_student(student) uses only student.id. Changes to the structure ripple to the callee unnecessarily.
6. *Data coupling* (weakest) Modules share only the elementary data they need, as parameters, as in greet_user(name, age).

::: example ex-coupling | Classifying cohesion and coupling together
Classify each fragment. (1) end_of_day() closes the database, backs up the logs, and sends a summary e-mail. (2) shipping_cost(order) uses only order.weight from an Order record with twenty fields. (3) render(report, fmt), with fmt in {"pdf", "csv", "html"} and a separate branch for each. (4) Two modules both read and write a global variable current_user. (5) greet_user(name, age) is called with just the two values it prints.
--- answer
(1) Temporal cohesion: the tasks are grouped only because they run at the end of the day. (2) Stamp coupling: a whole record is passed where one field is needed; passing order.weight would give data coupling. (3) Inside render, logical cohesion; between the caller and render, control coupling, since fmt selects the behavior. (4) Common coupling through shared global data. (5) Data coupling, the weakest and best form.
:::

The two properties reinforce each other. When related elements are placed together (high cohesion), fewer connections are needed to other modules (low coupling); when modules communicate through a few simple parameters, each can be understood in isolation. The results are concrete: a requirement change affects one module (modular continuity); a fault is unlikely to propagate (modular protection); each module can be unit-tested with simple stubs and drivers; functionally cohesive, data-coupled modules can be reused elsewhere; and teams can work in parallel. Note the difference between communicational cohesion (functions *inside one module* sharing data, which is acceptable) and common coupling (*different modules* sharing global data, which is not).

## 7.4 User interface design

The user interface (UI) is the part of the software that people see, hear, and touch. However sound the architecture and components, a system whose interface confuses or frustrates its users will be judged a failure. User interface design is the activity of creating an effective communication medium between a human and a computer: identifying interface objects and actions and producing screen layouts and interaction mechanisms that let users perform their tasks efficiently, intuitively, and with satisfaction.

### 7.4.1 The golden rules

Three golden rules form the basis of interface design principles:

1. *Place the user in control* The interface should respond to the user's needs, so that users feel in charge of the system rather than controlled by it. Interaction modes should not force users into unnecessary actions and should be easy to enter and leave (for example, turning spell-checking on and off); interaction should be flexible (keyboard, mouse, touch, voice); actions should be interruptible and undoable; skilled users should be able to streamline repetitive tasks, for example with macros; technical internals should be hidden from casual users; and users should be able to manipulate on-screen objects directly.
2. *Reduce the user's memory load* The more a user must remember, the more error-prone the interaction. Visual cues let users recognize rather than recall; defaults should be meaningful, with a way to reset them; shortcuts should be intuitive (Alt+P for print); layouts should use real-world metaphors, such as a chequebook for bill payment; and information should be disclosed progressively, overview first and detail on demand.
3. *Make the interface consistent* Consistency lets users transfer what they have learned in one part of the system to every other part. Visual information should be organized by the same rules on all screens; input mechanisms and navigation should be standardized; indicators such as titles, icons, and colors should show users where they are; applications in a family should follow the same conventions; and widely accepted interaction patterns should not be changed without a compelling reason.

### 7.4.2 Interface design models and users

Four models come into play when a user interface is analyzed and designed ([[fig:ui-models]]). The *user model* is a profile of the end users (their demographics, abilities, and goals), established by the software engineer. The *design model* is created by the engineer to fit the user model. The *mental model* is the user's own perception of how the system works. The *implementation model* is the system's look and feel together with its supporting documentation. The goal of interface design is to make the implementation model coincide with the users' mental model, so that the system behaves as its users expect. The key rule is 'know the user, know the tasks': designers must not substitute their own view for the user's.

@fig ui-models

Users are classified in the user model as *novices*, who have no syntactic knowledge of the system and little semantic knowledge of the application; *knowledgeable, intermittent users*, who understand the application but have low recall of the interface details; and *knowledgeable, frequent users*, who have good semantic and syntactic knowledge and look for shortcuts and abbreviated modes of interaction. A good interface serves all three: guided workflows and visible menus for novices, consistent layout and recognizable icons for intermittent users, and keyboard shortcuts and macros for frequent users.

### 7.4.3 The interface design process

The UI design process is iterative and is represented by a spiral with four activities ([[fig:ui-spiral]]):

1. *Interface analysis and modeling* Understand user profiles, skill levels, and environment; define user categories and elicit their requirements; analyze the tasks users perform; and analyze the physical work environment (location, lighting, noise). This corresponds to *user research* and to organizing the content and navigation (*information architecture*).
2. *Interface design* Define interface objects, actions, and their screen representations. Low-fidelity *wireframes* sketch the layout of each screen, and *visual design* applies typography, color, and iconography.
3. *Interface construction* Begin with a *prototype*, an interactive mock-up used to evaluate usage scenarios, then use UI toolkits to complete the interface.
4. *Interface validation* Confirm that the interface supports all user tasks and their variations, and assess ease of use, ease of learning, and user acceptance by *usability testing* with real users.

@fig ui-spiral

Several passes through the spiral elaborate the interface incrementally, so not every detail need be specified in the first iteration.

The following issues arise in almost every interface design. *System response time* has two characteristics, its length and its *variability*; consistent response times are preferable to highly variable ones, even if slightly longer. *Help facilities* must decide whether help is available for all functions, how it is accessed, how it is represented and structured, and how the user returns to work. *Error messages* should use language the user understands, give constructive advice for recovery, indicate any negative consequences, be accompanied by a visual or audible cue, and never blame the user: 'The date must be in DD/MM/YYYY format; your other entries have been kept' is better than 'Error 0x80070057'. *Menu and command labels* should be consistent, learnable, and customizable. *Accessibility* must allow people with visual, hearing, or mobility impairments to use the system, and *internationalization* designs a locale-independent core, supported by Unicode, that can be *localized* for particular languages and regions.

### 7.4.4 Principles and elements of interface design

A good interface is visually apparent and forgiving, hides system internals, and minimizes the input the user must supply. The following principles make these characteristics concrete:

1. *Clarity* The interface is easy to understand and navigate; every element has an obvious purpose.
2. *Consistency* Colors, fonts, icons, terms, and controls are used in the same way throughout.
3. *Familiarity* Familiar patterns and conventions, and real-world metaphors, reduce the learning curve.
4. *Efficiency* Users accomplish their tasks quickly and easily; the user's efficiency, not the developer's convenience, is optimized.
5. *Responsiveness and visibility of status* The interface responds quickly and always shows what the system is doing: progress, location, and the result of each action.
6. *Aesthetics* The interface is visually appealing, readable for all age groups, and uncluttered.
7. *Forgiveness* Users can recover easily from errors, with undo and clear paths back; work is saved automatically.
8. *Accessibility* The interface is usable by people with disabilities.

Other principles often listed for web and mobile applications are *anticipation* (offer what the user will need next), *controlled autonomy*, *focus* on the primary task, *Fitts's law* (the time to select a target grows with its distance and shrinks with its size, so frequent targets should be large and close), *latency reduction* (acknowledge and occupy delays), *learnability*, *work-product integrity*, *tracking state*, and *visible navigation*.

The *elements* of an interface are its layout (the arrangement of elements on the screen), typography, color, icons, buttons, forms (input fields for collecting data), and navigation (the system for moving between parts of the interface). A layout is usually designed first as a wireframe that places these elements, and the principles are then checked against it.

::: example ex-ui-fd | Screen layouts for an order processing and delivery system
For a food-delivery company's order processing and delivery management system: (a) design user interface layouts for (i) the restaurant order management screen, (ii) the delivery partner assignment screen, and (iii) the real-time order tracking screen; (b) show in a table how key user interface design principles are applied and satisfied in these screens.
--- solution
Each screen is designed for the user who will use it and the task they perform most often.

(i) *Restaurant order management* ([[fig:scr-restaurant]]) is used by busy kitchen staff on a tablet. Tabs separate New, Preparing, Ready, and Completed orders and show counts. Each new-order card shows only the items, time, and payment, with one-tap Accept and Reject and a preparation-time selector. Selecting an order opens its detail panel with Mark ready and Call rider. An out-of-stock toggle prevents orders that cannot be met, and a sound alert announces new orders.

@fig scr-restaurant

(ii) *Delivery partner assignment* ([[fig:scr-assign]]) is used by a dispatcher. A live map shows the restaurant and nearby partners; beside it, suggested partners are ranked nearest first with distance, time, rating, and status. A partner who is still on a delivery can only be queued. Automatic assignment counts down visibly and can be overridden or undone.

@fig scr-assign

(iii) *Real-time order tracking* ([[fig:scr-track]]) is used by the customer on a phone. The estimated arrival time is the most prominent element, above a five-step progress bar and a map with the rider's location, updated every ten seconds. The rider's name and rating are shown with a Call button, and delays are explained in plain language.

@fig scr-track
--- answer
(b) The principles and their application are summarized in [[fig:ui-principles-table]].

@fig ui-principles-table
:::

::: keypoints
- Design translates the requirements model into data/class, architectural, interface, and component-level designs. Ten principles, from avoiding tunnel vision to reviewing for conceptual errors, guide it.
- Abstraction may be procedural, data, or control abstraction. Separation of concerns divides a problem into independently solvable concerns and is realized by modularity.
- Modularity is judged by decomposability, composability, understandability, continuity, and protection; the total cost of a design is lowest between undermodularity and overmodularity.
- Refinement elaborates a design top-down; refactoring improves internal structure without changing external behavior.
- Cohesion, from lowest to highest, is coincidental, logical, temporal, procedural, communicational, sequential, and functional.
- Coupling, from strongest to weakest, is content, common, external, control, stamp, and data coupling. The goal is high cohesion and low coupling, which is functional independence.
- The golden rules of interface design are to place the user in control, reduce the user's memory load, and make the interface consistent. The user, design, mental, and implementation models should be aligned.
- The interface design process is a spiral of analysis and modeling, design, construction, and validation. Response time, help, error handling, labeling, accessibility, and internationalization must always be considered.
:::
