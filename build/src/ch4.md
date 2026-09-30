The requirements for a system are the descriptions of the services that a software system should provide and the constraints under which it must operate. They define *what* the software should do to meet the needs of its users and other stakeholders, and they say nothing, or as little as possible, about *how* it will do it. The process of discovering, analyzing, documenting, and checking these services and constraints is called requirements engineering (RE).

Requirements engineering matters because every later activity depends on it. A design can be no better than the requirements it implements, and tests can only check what the requirements state. Errors in requirements are also the most expensive errors to correct. If a missing or wrong requirement is discovered after the system has been delivered, the design, the code, the tests, and the documentation may all have to change. The same error found while the requirements are being written costs only a revision of a few sentences. This is the reason for the attention that this chapter gives to validating requirements and managing requirements change.

It helps to separate two levels of description:

1. *User requirements* are statements, in natural language plus diagrams, of what services the system is expected to provide to its users and the constraints under which it must operate. They are written for customers and managers who are not interested in the details of the implementation.

2. *System requirements* are more detailed descriptions of the software system's functions, services, and operational constraints. The system requirements document (sometimes called a functional specification) defines exactly what is to be implemented, and it may be part of the contract between the buyer of the system and its developers.

Different levels of requirement are needed because they are read by different people. A client manager wants to check that the system will support the business; a software developer needs to know precisely what each function must do with each input.

## 4.1 Functional and non-functional requirements

Software requirements can be divided into two groups ([[fig:req-kinds]]). The first group states what the software should do: it should process user inputs, store and retrieve data, generate reports, or control external devices. The second group states the constraints under which it does these things: how fast it must respond, how secure it must be, how easy it must be to use, and which other systems it must work with.

@fig req-kinds

Both groups sit inside a third, higher-level kind of requirement. *Business requirements* are the high-level goals and objectives that a system must achieve to support an organization's strategic business needs. They explain *why* the system is being built and what impact it should have on the business, for example 'reduce the time taken to settle an insurance claim from ten days to two'. Business requirements are not implemented directly; they are refined into the functional and non-functional requirements that together achieve them ([[fig:req-nesting]]). Every functional requirement should therefore be traceable to a business requirement. A function that supports no business goal is a candidate for removal.

@fig req-nesting

The two main categories of software requirement are:

1. *Functional requirements* These are statements of services the system should provide, how the system should react to particular inputs, and how the system should behave in particular situations. In some cases, the functional requirements may also explicitly state what the system should not do.

2. *Non-functional requirements* These are constraints on the services or functions offered by the system. They include timing constraints, constraints on the development process, and constraints imposed by standards. Non-functional requirements often apply to the system as a whole rather than to individual system features or services.

In reality, the distinction between the two is not as clear-cut as these definitions suggest. A user requirement concerned with security, such as a statement limiting access to authorized users, looks like a non-functional requirement. When it is developed in more detail, however, it generates requirements that are clearly functional, such as the need to provide a login facility and to record who accessed each record. Requirements are not independent, and one requirement often generates or constrains others.

### 4.1.1 Functional requirements

The functional requirements for a system describe what the system should do. They depend on the type of software being developed, the expected users of the software, and the general approach taken by the organization when writing requirements. Functional requirements focus on user tasks, data processing, and system features such as calculations and data manipulation. They are derived directly from user needs and business objectives. Examples are:

1. The system shall generate a monthly sales report for each branch.

2. A user shall be able to search for a customer by customer ID.

3. The system shall send an e-mail confirmation to the customer when an order is dispatched.

Functional requirements are essential. Without them the system does not do its basic job, and a system that is missing a required function has failed, however well it performs the functions it does have. They are checked by functional testing (unit, system, and acceptance testing) that shows each feature working as intended.

In principle, the functional requirements specification of a system should be both complete and consistent. *Completeness* means that all services required by the user should be defined. *Consistency* means that requirements should not have contradictory definitions. In practice, for large, complex systems, it is practically impossible to achieve both, partly because of the size of the system and partly because stakeholders have different, and often inconsistent, needs. Inconsistencies may not be obvious when the requirements are first specified; they are discovered during validation (Section 4.6) or even after the system has been delivered.

### 4.1.2 Non-functional requirements

Non-functional requirements, as the name suggests, are requirements that are not directly concerned with the specific services delivered by the system to its users. They define *how* the system must perform: its quality attributes and operational limits, such as reliability, response time, security, storage, and scalability. They are derived from technical constraints, budgets, regulations, or the need to work with other systems. Examples are:

1. The system shall display any report within 3 seconds of the request.

2. The database shall support 10,000 concurrent users.

3. All payment data shall be encrypted when stored and when transmitted.

Non-functional requirements are often more critical than individual functional requirements. Users can usually find ways to work around a system function that does not quite meet their needs, but failing to meet a non-functional requirement can make the whole system unusable. If an aircraft system does not meet its reliability requirements, it will not be certified as safe; if a web store takes a minute to load each page, customers will leave. The system may work, but it is effectively useless. Non-functional requirements are checked by performance testing, security audits, and by measuring the delivered system against benchmarks, for example 'load time < 2 s'. This is why they should be stated quantitatively wherever possible: 'the system should be fast' cannot be tested, whereas 'the system shall respond within 2 seconds for 95% of requests' can.

[[fig:nfr-types]] is a classification of non-functional requirements. You can see from this diagram that non-functional requirements may come from required characteristics of the software (product requirements), from the organization developing the software (organizational requirements), or from external sources:

1. *Product requirements* These requirements specify or constrain the behavior of the software. Examples include performance requirements on how fast the system must execute and how much memory it requires (efficiency), reliability requirements that set out the acceptable failure rate (dependability), security requirements, and usability requirements.

2. *Organizational requirements* These are broad system requirements derived from policies and procedures in the customer's and developer's organizations. Examples include operational process requirements that define how the system will be used, development process requirements that specify the programming language, the development environment, or process standards to be used, and environmental requirements that specify the operating environment of the system.

3. *External requirements* This broad heading covers all requirements that are derived from factors external to the system and its development process. These may include regulatory requirements that set out what must be done for the system to be approved for use by a regulator, such as a central bank; legislative requirements that must be followed to ensure that the system operates within the law; and ethical requirements that ensure that the system will be acceptable to its users and the general public.

@fig nfr-types

The difference between the two kinds of requirement can be summarized by asking what each one describes. A functional requirement names a behavior: it can be demonstrated by giving the system an input and observing the output. A non-functional requirement names a property: it is observed by measuring the system over many inputs, many users, or a long period of time.

::: example ex-antivirus-req | Classifying the requirements for an antivirus product
A company has asked for antivirus software with the following requirements: (1) core detection capabilities, using signature-based, heuristic, and machine-learning detection; (2) real-time monitoring and protection of both the file system and web traffic; (3) automatic malware removal; (4) low resource consumption; (5) daily updates from the vendor's server; (6) an attractive user interface; (7) code security; (8) compliance with legal requirements. Classify each requirement.
--- solution
A requirement is functional if it names a service that the product performs on an input, and non-functional if it names a property or constraint of the product as a whole.

1. *Detection* (signature, heuristic, and machine-learning) is functional. Each technique is a distinct service: given a file, it reports whether the file is malicious.
2. *Real-time monitoring and protection* is functional: the product must intercept file and web events and scan them. It carries a performance constraint (scanning must not noticeably delay the user), which should be stated separately.
3. *Automatic malware removal* is functional: quarantine or delete an infected file and repair what it changed.
4. *Low resource consumption* is a non-functional product requirement of the efficiency type (performance and space). It must be made measurable, for example 'CPU use below 5% and memory below 150 MB during background scanning'.
5. *Daily updates from the server* is functional (download and install signature and model updates) with a dependability constraint on the update service.
6. *An attractive user interface* is a non-functional product requirement of the usability type. As written it cannot be tested and should be restated, for example 'a first-time user can start a full scan within 30 seconds without help'.
7. *Code security* is a non-functional product requirement of the security type: the product itself must resist tampering, for example by signing its update packages and protecting its own processes.
8. *Legal considerations* is a non-functional external requirement of the legislative type: data protection law on the handling of scanned user files, and licensing of any third-party detection engines.
--- answer
Requirements 1, 2, 3, and 5 are functional. Requirements 4 (efficiency), 6 (usability), and 7 (security) are non-functional product requirements, and requirement 8 is a non-functional external (legislative) requirement. Requirements 4 and 6 must be rewritten in measurable form before they can be verified.
:::

## 4.2 The software requirements document

The software requirements document, usually called the software requirements specification or SRS, is an official statement of what the system developers should implement. It should include both the user requirements for a system and a detailed specification of the system requirements. The process of requirements specification produces this structured document. It defines the data, functional, and behavioral elements of the system unambiguously, using models where necessary to show information flow, events, states, and constraints.

Requirements documents are essential when an outside contractor is developing the software, and they are useful whenever a system is large, long-lived, or critical. Agile methods argue that requirements change so rapidly that a detailed document is out of date as soon as it is written, and they use lighter-weight approaches (Section 4.7.3). Even then, a short document that sets out the business and dependability requirements is valuable, because requirements that apply to the system as a whole are easily forgotten when attention is on the next increment.

A requirements document has a diverse set of readers, from the senior managers of the customer organization who pay for the system to the engineers who develop, test, and maintain it. For this reason it should cover a broad range of topics. The subjects that an SRS must address are:

1. *Functionality* What is the software supposed to do?
2. *External interfaces* How does the software interact with people, the system's hardware, other hardware, and other software?
3. *Performance* What is the speed, availability, response time, and recovery time of the software functions?
4. *Quality attributes* What are the reliability, maintainability, portability, and security considerations?
5. *Constraints* Are there required standards, policies, implementation languages, database integrity rules, resource limits, or operating environments?
6. *Safety* Are there hazards that the software must avoid or control?

[[fig:srs-structure]] shows one widely used organization of a requirements document, based on the IEEE standard for requirements documents. The standard is generic, and each organization adapts it to its own needs. The specific requirements in part 4 are normally the largest and most important part of the document, and they may be organized in different ways: by feature, by class of user, or by mode of operation.

@fig srs-structure

### 4.2.1 Properties of a good specification

A requirements document is used as the basis for design, for testing, and often for a contract. It can only serve these purposes if its requirements have certain properties. A good SRS is:

1. *Correct* Every requirement stated is one that the software shall meet; nothing in it contradicts the real needs of the stakeholders.
2. *Unambiguous* Every requirement has only one interpretation. Natural language is inherently ambiguous, so terms are defined in a glossary and vague words such as 'fast', 'user-friendly', and 'flexible' are avoided.
3. *Complete* All significant requirements are included, together with the responses of the software to all realizable classes of input, both valid and invalid.
4. *Consistent* No subset of the requirements conflicts with another, for example one requirement that a report is printed daily and another that it is printed weekly.
5. *Ranked for importance and stability* Each requirement is marked as essential, desirable, or optional, and as stable or likely to change, so that effort and change control can be planned.
6. *Verifiable* For every requirement there is a finite, cost-effective process by which a person or a machine can check that the software meets it.
7. *Modifiable* Its structure and style allow changes to be made easily, completely, and consistently; each requirement is stated once and not repeated.
8. *Traceable* The origin of each requirement is clear, and each requirement can be referenced by later documents such as designs and test cases.

Requirements that fail these tests cause predictable problems. Requirements that are inconsistent, incomplete, not aligned with the business goals, not implementable, or incomprehensible lead to rework during development or to a delivered system that does not meet its users' needs. Good requirements, by contrast, are clear, necessary, complete, comprehensible, testable, and trackable from their source through to the code and tests that implement them.

## 4.3 Requirements specification

Requirements specification is the process of writing down the user and system requirements in a requirements document. Ideally, the user and system requirements should be clear, unambiguous, easy to understand, complete, and consistent. In practice this is difficult to achieve, because stakeholders interpret requirements in different ways and there are often inherent conflicts and inconsistencies in the requirements.

User requirements are almost always written in natural language, supplemented by simple diagrams and tables. System requirements may also be written in natural language, but other notations based on forms, graphical system models, or mathematical models can be used. Graphical models, which are described in Chapter 5, are most useful when you need to show how a state changes or when you need to describe a sequence of actions.

### 4.3.1 Natural language specification

Natural language is expressive, intuitive, and universal. It is also potentially vague and ambiguous, and its interpretation depends on the background of the reader. To minimize misunderstandings, the following simple guidelines are useful:

1. Invent a standard format and ensure that all requirement definitions adhere to it. Standardizing the format makes omissions less likely and requirements easier to check. Each requirement should be stated in a single sentence where possible.
2. Use language consistently to distinguish between mandatory and desirable requirements. Mandatory requirements use 'shall'; desirable requirements use 'should'.
3. Use text highlighting (bold or italic) to pick out key parts of the requirement.
4. Do not assume that readers understand technical software engineering language. Avoid jargon, abbreviations, and acronyms.
5. Whenever possible, associate a rationale with each requirement. The rationale explains why the requirement has been included, and it is particularly useful when requirements are changed, because it helps to decide what changes would be undesirable.

::: example ex-rewrite | Rewriting requirements so that they can be verified
The following statements were collected for an online store. Explain what is wrong with each and rewrite it. (a) 'The system should be easy to use.' (b) 'The site must be fast and must be available at all times.' (c) 'The system shall store customer details and should allow them to be changed.'
--- solution
(a) is not verifiable: 'easy to use' cannot be measured. A usability requirement must name a user group, a task, and a measure.

(b) combines two requirements in one sentence, and neither is measurable. 'Available at all times' is also unrealistic, since no system can promise 100% availability.

(c) is compound and mixes a mandatory verb with a desirable one, so it is unclear whether changing details is required.
--- answer
(a) *Usability* A first-time customer shall be able to find a product and complete a purchase in under 4 minutes without help, in at least 90% of trials.

(b) *Performance* Product pages shall load within 2 seconds for 95% of requests at a load of 2,000 concurrent users. *Availability* The store shall be available for at least 99.5% of each calendar month.

(c) R1: The system shall store the name, address, e-mail, and phone number of each registered customer. R2: A registered customer shall be able to change their stored details after logging in.
:::

## 4.4 Requirements engineering processes

The requirements engineering process is the systematic process of discovering, analyzing, documenting, and checking the services that a system should provide and the constraints under which it must operate. [[fig:re-process]] shows its main activities and the documents they produce. A feasibility study produces a feasibility report; elicitation and analysis produce system models; specification produces the user and system requirements; and validation checks them before they are collected into the requirements document. Management of requirements runs through all of these stages, because requirements change throughout.

@fig re-process

The stages, their purposes, and the techniques used in each are as follows:

1. *Feasibility study* The purpose is to assess the technical, economic, and operational feasibility of the proposed system: can it be built with available technology, will its benefits outweigh its costs, and will it fit the way the organization works? Activities include market analysis, technology assessment, risk analysis, and cost–benefit analysis. The result is a recommendation on whether to continue.

2. *Requirements elicitation* The purpose is to gather information about the needs and expectations of stakeholders: users, customers, and domain experts. Techniques include interviews, surveys, observation, focus groups, workshops, and prototyping (Section 4.5).

3. *Requirements analysis* The purpose is to analyze the elicited information, identify conflicts, and prioritize requirements. Techniques include use case analysis (describing the interactions between users and the system), data-flow diagrams (visualizing the flow of data through the system), requirement decomposition (breaking complex requirements into smaller, manageable ones), and risk analysis (identifying potential risks and developing mitigation strategies).

4. *Requirements specification* The purpose is to document the requirements in a clear, concise, and unambiguous manner. The deliverable is the software requirements specification, which must include the functional requirements (what the system should do), the non-functional requirements (quality attributes such as performance, usability, and security), the user requirements (from the perspective of end-users), and the system requirements (from the perspective of the system developers).

5. *Requirements validation* The purpose is to ensure that the requirements are correct, complete, consistent, and feasible. Techniques include reviews and inspections, prototyping, and testing (Section 4.6).

6. *Requirements management* Throughout stages 1 to 5, requirements management tracks changes to requirements, manages conflicts, and ensures that the system remains aligned with the evolving needs of stakeholders. Its techniques are change control, version control, and traceability (Section 4.7).

The same work is sometimes described as seven overlapping tasks: *inception* (establishing a basic understanding of the problem, the stakeholders, and the nature of the solution), *elicitation*, *elaboration* (refining the information into an analysis model), *negotiation* (reconciling conflicting requirements), *specification*, *validation*, and *management*. The list is different, but the idea is the same: the requirements move from vague business needs to a precise, checked, and controlled description.

@fig re-spiral

These activities are not carried out once in strict sequence. In practice, requirements engineering is an iterative process in which the activities are interleaved. [[fig:re-spiral]] shows this as a spiral. The amount of time and effort devoted to each activity in each iteration depends on the stage of the overall process and on the type of system being developed. Early in the process, most effort is spent on understanding high-level business and non-functional requirements and the user requirements for the system. Later, in the outer rings of the spiral, more effort is devoted to eliciting and understanding the detailed system requirements.

## 4.5 Requirements elicitation and analysis

After an initial feasibility study, the next stage of the requirements engineering process is requirements elicitation and analysis. Software engineers work with customers and system end-users to find out about the application domain, what services the system should provide, the required performance of the system, hardware constraints, and so on. Elicitation has four objectives:

1. to understand user expectations;
2. to identify the functional and non-functional requirements;
3. to prevent miscommunication between the stakeholders and the development team; and
4. to ensure that the project deliverables align with business goals.

A process model of elicitation and analysis is shown in [[fig:elicit-process]]. The activities are:

@fig elicit-process

1. *Requirements discovery* This is the process of interacting with stakeholders of the system to discover their requirements. Domain requirements from stakeholders and documentation are also discovered during this activity.
2. *Requirements classification and organization* This activity takes the unstructured collection of requirements, groups related requirements, and organizes them into coherent clusters.
3. *Requirements prioritization and negotiation* Inevitably, when multiple stakeholders are involved, requirements will conflict. This activity is concerned with prioritizing requirements and finding and resolving requirements conflicts through negotiation.
4. *Requirements specification* The requirements are documented and input into the next round of the spiral.

Elicitation is difficult. Stakeholders often do not know what they want from a computer system except in the most general terms; they express requirements in their own terms and with implicit knowledge of their own work; different stakeholders have different requirements, which they may express in different ways; and the business environment may change during the analysis process.

### 4.5.1 Elicitation techniques

No single technique is sufficient for every system. The following techniques are commonly combined:

1. *Interviews* One-to-one or group discussions with stakeholders. *Closed* interviews use a predetermined list of questions; *open* interviews explore issues without a fixed agenda. Interviews are good for getting an overall understanding of what stakeholders do and how they might interact with the system, but they are less effective for understanding domain requirements, which stakeholders find hard to articulate.
2. *Questionnaires and surveys* Written questions sent to many stakeholders. They reach large, dispersed user groups cheaply but give little opportunity to follow up an unexpected answer.
3. *Workshops and brainstorming* Collaborative sessions in which stakeholders and developers generate and refine requirements together. They are effective at surfacing conflicts early and building agreement.
4. *Prototyping* An early, partial version of the system, or a mock-up of its interface, is shown to users to obtain feedback. Users who cannot describe what they want can often say at once what is wrong with a prototype.
5. *Observation and ethnography* An analyst immerses themselves in the working environment and observes the day-to-day work. Observation reveals how people actually work, which is often different from how formal procedures say they work, and it uncovers requirements that derive from cooperation between people.
6. *Document analysis* Existing forms, reports, manuals, regulations, and the documentation of current systems are studied to extract requirements, particularly domain requirements.
7. *Introspection* The analyst imagines what they would want if they were the user. It is quick but reliable only when the analyst has deep domain knowledge, and its results must be checked with real users.
8. *Use cases and scenarios* Real-life examples of how the system will be used are written down or modeled. People find it easier to relate to concrete examples than to abstract descriptions, so scenarios are an effective way of discovering the details of interactions (Chapter 5).
9. *Storyboarding and walkthroughs* Sequences of sketches of the user interface are walked through with stakeholders to check the flow of a task.
10. *Facilitated application specification technique (FAST)* A structured meeting of customers and developers, run by a neutral facilitator with agreed rules and an agenda. Before the meeting each participant lists objects, services, constraints, and performance criteria; the lists are combined, conflicts are discussed, and a joint specification is drafted.

The choice depends on the stakeholders and the system. Interviews and document analysis are nearly always used; observation is valuable where work practices are complex or tacit; prototyping and storyboarding are most useful for interactive systems whose users have difficulty describing what they need.

## 4.6 Requirements validation

Requirements validation is the process of checking that requirements actually define the system that the customer really wants. It overlaps with analysis, since it is concerned with finding problems with the requirements. Validation verifies that the software requirements are complete, consistent, and accurately reflect stakeholder needs, and it detects errors early in order to reduce costly rework. During validation, stakeholders systematically check the requirements model for proper reflection of information, function, and behavior. The specification is examined to ensure that:

1. all software requirements have been stated unambiguously;
2. inconsistencies, omissions, and errors have been detected and corrected; and
3. the work products conform to the standards established for the process, the project, and the product.

Requirements validation is important because errors in a requirements document can lead to extensive rework costs when these problems are discovered during development or after the system is in service. The cost of fixing a requirements problem by making a system change is usually much greater than repairing design or coding errors, because a change to the requirements usually means that the system design and implementation must also be changed, and the system must then be tested again.

### 4.6.1 Validation checks

During the requirements validation process, different types of checks should be carried out on the requirements in the requirements document:

1. *Validity checks* A user may think that a system is needed to perform certain functions. However, further thought and analysis may identify additional or different functions that are required. Validity checks ensure that the system performs the functions needed across the user community.
2. *Consistency checks* Requirements in the document should not conflict. That is, there should not be contradictory constraints or different descriptions of the same system function.
3. *Completeness checks* The requirements document should include requirements that define all intended functions and the constraints on them.
4. *Realism checks* Using knowledge of existing technology, the requirements should be checked to ensure that they can actually be implemented within the proposed budget and schedule.
5. *Verifiability* To reduce the potential for dispute between customer and contractor, system requirements should always be written so that they are verifiable. This means that you should be able to write a set of tests that can demonstrate that the delivered system meets each specified requirement.

### 4.6.2 Validation techniques

There are a number of requirements validation techniques that can be used individually or in conjunction with one another:

1. *Requirements reviews* A group of people from the contractor and the client carefully review the SRS document to identify errors, ambiguities, and inconsistencies. The systematic analysis ensures that the requirements are verifiable and traceable. Estimates of defect density guide how thorough a review must be: if earlier reviews of similar documents found around 0.6 errors per page, a review of a 50-page SRS that finds only three errors has probably not been thorough enough.
2. *Prototyping* An executable model of the system is demonstrated to end-users and customers. They can experiment with this model to see if it meets their real needs. The technique is particularly effective for collecting user feedback and for validating assumptions early.
3. *Test-case generation* Requirements must be testable. If the tests for the requirements are devised as part of the validation process, this often reveals requirements problems: if a test is difficult or impossible to design, the requirement will be difficult to implement and should be reconsidered. Requirements-based testing also shows that the system performs as the customer expects and supports risk management.
4. *Automated consistency analysis* If the requirements are expressed as a system model in a structured or formal notation, tools can check the model automatically for conflicts, contradictions, and inconsistencies. This improves both the accuracy and the efficiency of validation.
5. *Walkthroughs* An informal review without a formally defined procedure. Walkthroughs are used early to check feasibility, to obtain opinions, and to reach agreement among stakeholders.
6. *Simulation* The behavior of the system is replicated in a realistic setting to check that the requirements meet their goals. Simulation is especially effective for complex and real-time systems whose behavior is hard to imagine from a document.

You should not underestimate the problems involved in requirements validation. It is difficult to show that a set of requirements does in fact meet a user's needs, because users must picture the system in operation and imagine how it would fit into their work. As a result, you rarely find all requirements problems during validation, and further changes to correct omissions and misunderstandings will be needed after the requirements document has been agreed upon.

::: example ex-validate | Validating the requirements for an online fashion store
StyleSphere is a start-up e-commerce platform selling sustainable and ethically sourced fashion to environmentally conscious young customers. Its application is struggling with customer acquisition, building trust, and managing its supply chain, and a new version is planned with many changed requirements (see [[ex:ex-stylesphere]]). Is it necessary to apply requirements validation techniques before the new version is built? Justify your answer with a suitable example.
--- solution
Validation is necessary. The new requirements come from several sources at once (marketing, supply-chain partners, legal advisers, and customer feedback), so they are especially likely to conflict, to be incomplete, or to be unrealistic. Requirements are finalized only after validation: the specification must be examined to ensure that every requirement is stated unambiguously, that inconsistencies, omissions, and errors have been found and corrected, and that the document conforms to the project's standards.

Consider two proposed requirements: 'Every product page shall show live stock levels from all partner suppliers' and 'Every product page shall load within 2 seconds'. A consistency and realism check shows that they may conflict, since querying several supplier systems on every page view could make pages slow. A third requirement, 'Every product shall display a verified sustainability certificate', fails a realism check if some small suppliers have no certification.

The validation techniques apply as follows:

1. A *requirements review* by marketing, supply-chain, and legal staff finds the stock/performance conflict and the certification gap. It is resolved by caching supplier stock every 15 minutes and by labelling uncertified items differently.
2. A *prototype* of the new product page, shown to a sample of target customers, checks whether the trust features (impact score, reviews, supplier story) actually increase confidence before they are built.
3. *Test-case generation* for 'the impact score shall be accurate' shows that the requirement cannot be tested until the formula and its data sources are defined, so the requirement is rewritten.
4. *Automated consistency analysis* of the structured requirements checks that every changed requirement is traced to its source and does not contradict another requirement.
--- answer
Yes. Because the changed requirements come from many stakeholders, validation is needed to find conflicts (live supplier stock versus a 2-second page load), unrealistic requirements (certification for every product), and untestable requirements (an undefined 'accurate' impact score) before they are designed and coded. Reviews, prototyping, test-case generation, and automated consistency analysis are the techniques to use; errors removed at this stage are far cheaper than errors found after release.
:::

## 4.7 Requirements management

The requirements for large software systems are always changing. One reason for this is that these systems are usually developed to address 'wicked' problems, that is, problems that cannot be completely defined. Because the problem cannot be fully defined, the software requirements are bound to be incomplete. During the software process, the stakeholders' understanding of the problem is constantly changing ([[fig:req-evolution]]). The system requirements must then also evolve to reflect this changed problem view.

@fig req-evolution

Once a system has been installed and is regularly used, new requirements inevitably emerge. It is hard for users and system customers to anticipate what effects the new system will have on their business processes and the way that work is done. Once end-users have experience of a system, they will discover new needs and priorities.

### 4.7.1 Why requirements change

Requirements change for many reasons. The main *sources* of change, and the *factors* that drive each one, are:

1. *The business and technical environment* After installation the hardware may change, the system may have to interface with other systems, business priorities may change, and new legislation and regulations may be introduced. Competition, new markets, and pressure on revenue are the usual factors.
2. *Customers who are not the users* The people who pay for a system and the people who use it are often different. Customers impose requirements because of organizational and budgetary constraints, and these may conflict with end-user requirements; after delivery, new features may have to be added for user support if the system is to meet its goals.
3. *Diverse stakeholders* Large systems have many stakeholders with different, and often contradictory, requirements. The final requirements are inevitably a compromise, and the balance of support given to different users may have to change as experience grows.
4. *Improved understanding* As development proceeds, developers and stakeholders understand the problem better. Feedback from prototypes and from early releases reveals requirements that nobody had thought of.
5. *Other systems and processes* Requirements that depend on external systems, devices, or organizational processes change when those systems and processes change.

From an evolution perspective, requirements fall into two classes. *Enduring requirements* are relatively stable requirements that derive from the core activity of the organization; a hospital will always have doctors, nurses, and patients. *Volatile requirements* are likely to change during the development process or after the system has been put into operation. There are four types of volatile requirement:

1. *Mutable requirements* These are requirements that change because of changes to the environment in which the organization is operating. For example, in hospital systems, the funding of patient care may change and so require different treatment information to be collected.
2. *Emergent requirements* These are requirements that emerge as the customer's understanding of the system develops during the system development. The design process may reveal new emergent requirements.
3. *Consequential requirements* These are requirements that result from the introduction of the computer system. Introducing the computer system may change the organization's processes and open up new ways of working that generate new system requirements.
4. *Compatibility requirements* These are requirements that depend on the particular systems or business processes within an organization. As these change, the compatibility requirements on the commissioned or delivered system may also have to evolve.

::: example ex-stylesphere | Changing requirements for an online fashion store
StyleSphere is a start-up e-commerce platform focused on sustainable and ethically sourced fashion, aimed at environmentally conscious customers looking for unique, high-quality clothing. The company runs its own e-commerce application but is struggling with customer acquisition, building trust, and its supply chain. Identify the sources of changing requirements and the factors behind them, explain the types of volatile requirement, and state the modified requirements for the new version of the application.
--- solution
*Sources of change and their factors.* Each problem the business faces becomes a source of new or changed requirements:

1. *Business environment (customer acquisition).* Factors: competition from larger fashion platforms, falling revenue, and marketing costs. The niche (sustainable fashion) must be made visible, so content, referral, and social-sharing features are needed.
2. *Customers' understanding and priorities (trust).* Factors: customer feedback, abandoned carts, and poor reviews. Customers doubt sustainability claims, so the product pages must show evidence.
3. *Other systems and processes (supply chain).* Factors: new partner suppliers and couriers with their own systems; stock-outs and late deliveries.
4. *Legislation and regulation.* Factors: consumer-protection rules on environmental claims ('green claims'), data-protection law, and changes in tax rules for online sales.
5. *Data and experience from the running system.* Factors: analytics showing where visitors leave the site; requests from users of the current version.

*Types of volatile requirement in this system:*

1. *Mutable:* rules on what may be claimed as 'sustainable' and on tax for online sales change with the regulatory environment, so the product-information and checkout requirements must change with them.
2. *Emergent:* analysis of why visitors do not buy shows that they need proof of ethical sourcing; a requirement for a verified impact score and supplier story emerges only as this understanding develops.
3. *Consequential:* once the new version introduces a take-back and resale scheme for used clothing, customers need a way to request collection and track credit for returned items, requirements that exist only because the new system exists.
4. *Compatibility:* stock and shipment requirements depend on the partner suppliers' inventory systems and the couriers' tracking services; when those change their interfaces, StyleSphere's requirements must change too.

The core catalogue, cart, and checkout requirements are enduring and are not expected to change.
--- answer
Modified requirements for the new version:

1. *(Acquisition)* The system shall provide editorial content pages and a referral scheme giving the referrer and the new customer store credit on the first order.
2. *(Trust)* Each product page shall show the supplier, the materials, a sustainability certificate where one exists, and verified-buyer reviews.
3. *(Trust)* The system shall calculate and display an impact score for each product from a published formula.
4. *(Supply chain)* The system shall import stock levels from each partner supplier's system at least every 15 minutes and shall show 'dispatches in n days' based on that stock.
5. *(Supply chain)* The system shall display courier tracking for every dispatched order.
6. *(Regulation)* Environmental claims shall be displayed only where supported by a stored certificate.
7. *(Consequential)* Customers shall be able to request collection of used StyleSphere items and track the resulting store credit.

Requirement 1 addresses acquisition; 2 and 3 address trust; 4 and 5 address the supply chain; 6 addresses regulation and also supports trust; 7 introduces a new service. By type, 6 is mutable, 3 is emergent, 7 is consequential, and 4 and 5 are compatibility requirements.
:::

### 4.7.2 Requirements management planning and change management

Requirements management is the process of understanding and controlling changes to system requirements. You need to keep track of individual requirements and maintain links between dependent requirements so that you can assess the impact of requirements changes. Its three main techniques are:

1. *Change control* A defined process through which every proposed change is submitted, analyzed, approved or rejected, and implemented.
2. *Version control* Different versions of the requirements document are maintained, so that it is always clear which version is current and what changed between versions.
3. *Traceability* Links are maintained between each requirement and its source, other requirements, and later artifacts such as design documents and test cases. Traceability lets you see how a change ripples through the system.

Planning is an essential first stage in the requirements management process. During planning you decide on how requirements are uniquely identified so that they can be cross-referenced; on the change management process; on the traceability policies that define the relationships to be recorded; and on the tool support to be used, which may range from specialist requirements management systems to spreadsheets and simple databases.

Requirements change management ([[fig:change-mgmt]]) should be applied to all proposed changes to a system's requirements after the requirements document has been approved. The advantage of using a formal process is that all change proposals are treated consistently and changes to the requirements document are made in a controlled way. There are three principal stages:

@fig change-mgmt

1. *Problem analysis and change specification* The process starts with an identified requirements problem or, sometimes, with a specific change proposal. The problem or proposal is analyzed to check that it is valid, and the result is fed back to the person who asked for the change.
2. *Change analysis and costing* The effect of the proposed change is assessed using traceability information and general knowledge of the system requirements. The cost of making the change is estimated in terms of modifications to the requirements document and, if appropriate, to the system design and implementation. A decision is then made whether or not to proceed.
3. *Change implementation* The requirements document and, where necessary, the system design and implementation are modified. The document should be organized so that changes can be made without extensive rewriting.

If a new requirement has to be urgently implemented, there is always a temptation to change the system and then retrospectively modify the requirements document. You should try to avoid this, as it almost inevitably leads to the requirements specification and the system implementation getting out of step.

### 4.7.3 Requirements in agile development

Agile processes take a different approach. Requirements are managed as small, negotiable items, often user stories, in a prioritized backlog that is continuously refined, implemented in short iterations, and validated through frequent stakeholder feedback. Instead of a single fixed SRS, agile development treats requirements as evolving assets that are detailed 'just in time' for implementation. [[fig:agile-re]] shows the cycle.

@fig agile-re

1. *Product backlog* The backlog is the master list containing all requests, features, and fixes. The rule is simple: if it is not on the list, it does not get built. The most important items (high value or high risk) are moved to the top; the bottom of the list remains vague and can change at any time.
2. *User stories* Requirements are written on small cards in the form 'As a ⟨user role⟩, I want ⟨feature⟩ so that ⟨benefit⟩'. This keeps the focus on who needs a feature and why, rather than on how to code it. Each story is given acceptance criteria that say when it is done.
3. *Sprints* The whole list is not built at once; it is sliced into short, fixed time periods. In sprint planning, the team picks the top items from the backlog that they can finish in one sprint. Once a sprint starts, new items are generally not added to it (the sprint is *frozen*), which lets the team concentrate.
4. *Feedback loop* At the end of each sprint the team shows the working software to the customer. The customer may say 'this button is too small' or 'I don't actually need this feature any more'. The backlog is immediately updated with this feedback: new ideas are added and unwanted items removed before the next sprint begins.

Large requirements are first recorded as *epics*. An epic is a high-level goal or large feature that spans several sprints; it is broad and deliberately vague, and it is refined later into a number of user stories. A user story is small enough to be completed in a single sprint, is detailed (with acceptance criteria), and belongs to an epic. In this way the epic is the parent and its stories are the children.

When a user proposes a requirements change in an agile process, the change does not go through a formal change management process. Rather, the user adds it to the backlog and prioritizes it, and it is scheduled into a later sprint if its priority is high enough.

::: example ex-epic | Splitting an epic into user stories
A library wants its members to be able to reserve books online. Write this as an epic and split it into user stories with acceptance criteria.
--- solution
The epic states the goal: 'As a library member, I want to reserve books online so that I do not have to visit the library to check availability.' It is too large for one sprint, because it involves searching, reserving, notification, and cancellation, so it is split into stories that can each be finished and demonstrated in a sprint.
--- answer
1. As a member, I want to search the catalogue by title or author so that I can find a book. *Accepted when* results appear within 2 seconds and show availability.
2. As a member, I want to reserve a book that is on loan so that I get it when it is returned. *Accepted when* a reservation is recorded and shown in 'My reservations'.
3. As a member, I want to be notified when a reserved book is ready so that I can collect it. *Accepted when* an e-mail is sent within 10 minutes of the book being returned.
4. As a member, I want to cancel a reservation so that the book goes to the next person. *Accepted when* the reservation disappears and the next member in the queue is promoted.
:::

::: keypoints
- Requirements for a software system set out what the system should do and define constraints on its operation. Business requirements state why the system is needed; functional requirements state what it must do; non-functional requirements state how well it must do it.
- Non-functional requirements may be product, organizational, or external requirements. They often apply to the system as a whole and should be stated in measurable terms.
- The software requirements document is an agreed statement of the system requirements. A good specification is correct, unambiguous, complete, consistent, ranked, verifiable, modifiable, and traceable.
- The requirements engineering process includes a feasibility study, requirements elicitation and analysis, requirements specification, requirements validation, and requirements management. In practice these activities are interleaved in a spiral.
- Elicitation techniques include interviews, surveys, workshops, prototyping, observation, document analysis, introspection, scenarios, storyboarding, and FAST.
- Requirements validation checks requirements for validity, consistency, completeness, realism, and verifiability, using reviews, prototyping, test-case generation, automated consistency analysis, walkthroughs, and simulation.
- Requirements change because of changes in the business environment, conflicts between stakeholders, and improved understanding. Volatile requirements may be mutable, emergent, consequential, or compatibility requirements.
- Requirements management uses change control, version control, and traceability. Agile processes manage requirements as a prioritized backlog of user stories grouped into epics.
:::
