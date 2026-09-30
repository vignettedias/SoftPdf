Testing is intended to show that a program does what it is intended to do and to discover program defects before it is put into use. Software testing is the process of evaluating a software application to ensure that it meets its specified requirements. It involves executing a program with the intent of finding errors, verifying its functionality, and ensuring that it performs as expected. The phrase *with the intent of finding errors* is essential: a good test case is one with a high probability of finding an as-yet-undiscovered error, and a test that finds nothing is not thereby a success. Testing can show the presence of errors, but not their absence.

Testing has five objectives: to detect defects before users do; to validate that the software does what its requirements specify; to improve quality (reliability, performance, and usability); to ensure user satisfaction; and to show compliance with the standards and regulations of the application domain.

It is useful to distinguish three terms. An *error* (mistake) is a human action that produces an incorrect result; it leads to a *fault* (defect, bug) in the code; executing the fault may cause a *failure*, an observable deviation from the expected behavior. Testing observes failures in order to locate faults; debugging removes them.

Testing proceeds from the small to the large ([[fig:test-strategy]]). Development moves inward from system engineering through requirements and design to code; testing moves outward. *Unit testing* verifies individual components as coded; *integration testing* verifies the assembled components against the design; *validation testing* confirms the software against its requirements; and *system testing* verifies the software together with the other elements of the system (hardware, people, and databases). Other testing strategies include requirement-based, functional, performance, security, usability, regression, user acceptance, and maintenance testing.

@fig test-strategy

Testing may be classified in three independent ways: by how it is executed (*manual* or *automated*), by what is tested (*functional* testing of what the system does, or *non-functional* testing of how well it does it), and by what the tester knows (*white-box* testing from the code, or *black-box* testing from the specification). A further distinction is between *static* techniques, which examine work products without executing them (reviews, walkthroughs, inspections, and static analysis), and *dynamic* techniques, which execute the software.

## 8.1 The testing process

Testing is the process of verifying that a system works as intended and validating that it meets its users' actual needs. It is an investigative process that gives stakeholders information about the quality of the product, and its primary goal is to deliver a reliable and secure product by uncovering defects before the software reaches its users. The fundamental test process has five groups of activities ([[fig:test-process]]):

1. *Test planning and control* defines the approach and monitors progress: objectives, scope, strategy, resources, and entry and exit criteria are set, and metrics are monitored so that corrective action can be taken.
2. *Test analysis* identifies *what* to test: the test basis (requirements, design, code) is analyzed to identify testable features and to derive *test conditions*.
3. *Test design* defines *how* to test: test conditions are elaborated into test cases with inputs, expected results, and preconditions.
4. *Test implementation and execution* prepares the environment and runs the tests: testware and the test environment are built, test cases are prioritized and organized into suites, the tests are executed, and the results are logged.
5. *Test completion* closes testing: the exit criteria are evaluated, testware is archived, deliverables are handed over, and lessons learned are recorded.

@fig test-process

### 8.1.1 Test strategy and test plan

A *test strategy* is a description of how testing is to be performed to reach the test objectives under given circumstances. It provides the high-level framework for testing across an organization or program, and it is documented and implemented through *test plans*. A test plan is 'a document describing the scope, approach, resources, and schedule of intended test activities'; it is the primary output of test planning. Its components are:

1. *Test objectives* The quality aspects that will be verified, aligned with business goals and the risk analysis.
2. *Test scope* The features in scope (to be tested) and out of scope (excluded), justified by risk assessment.
3. *Test strategy and approach* The test levels to be performed (component, integration, system, acceptance); the test types (functional, non-functional, structural); the test techniques (black-box, white-box, experience-based); the *entry criteria*, conditions that must be met before testing begins; and the *exit criteria*, measurable conditions that determine when testing is complete.
4. *Resource planning* The skills of the people needed, the specification of the test environment, and the tools.
5. *Schedule and milestones* A timeline aligned with the development milestones, with the dependencies identified.
6. *Risk management approach* How product risks (defects in the software) and project risks (constraints on testing, such as a late build) will be addressed.
7. *Metrics and reporting* What will be measured (defect density, test coverage, progress) and how often it is reported.
8. *Test deliverables* The documents and artifacts to be produced: test cases, test reports, and defect logs.

### 8.1.2 Test design and test cases

*Test design* is the process of defining the scenarios and conditions required to verify that a system meets its requirements. It is the bridge between the high-level test plan and the detailed test cases. Its objective is maximum test coverage with minimum effort; its activities are analyzing the requirements, identifying *test scenarios* (the high-level 'what to test'), and selecting techniques. The techniques are *black-box* (without knowledge of the code: equivalence partitioning and boundary value analysis, Section 8.8), *white-box* (from the internal structure of the code: statement, branch, and path coverage, Sections 8.6 and 8.7), and *experience-based* (intuition and past knowledge: error guessing and exploratory testing).

A *test case* is a detailed, step-by-step specification of the inputs, execution conditions, and expected outcomes for one test scenario; it is the most granular level of test documentation. Its components are shown in [[fig:test-case-tbl]]: a unique identifier, the preconditions that must be true before the test starts, the steps, the test data, the expected result, and the actual result and status, which are filled in during execution.

@fig test-case-tbl

::: example ex-testplan | A test plan for a hospital appointment and billing system
A hospital is building a patient appointment and billing system: patients book, reschedule, and cancel appointments; reception staff register patients; the system generates bills and accepts payment through a payment gateway; and doctors view their schedules. Prepare the main components of a test plan and write one complete test case.
--- solution
*Objectives* Verify that appointments are never double-booked, that bills are computed correctly, that payments are recorded exactly once, and that patient data is accessible only to authorized staff.

*Scope* In scope: registration, appointment booking, rescheduling and cancellation, billing, payment, and doctor schedules. Out of scope: the payment gateway's internal processing (a third-party service) and the hospital's existing laboratory system, which is unchanged.

*Approach* Levels: component tests by developers, component and system integration tests (with the payment gateway virtualized), system tests, and user acceptance tests with reception staff. Types: functional; performance (200 concurrent bookings); security (role-based access). Techniques: equivalence partitioning and boundary values for dates and amounts, a state-transition model of an appointment (booked, rescheduled, cancelled, completed), and branch coverage of the billing rules. *Entry criteria*: the build is deployed to the test environment and smoke tests pass. *Exit criteria*: all planned tests executed; no open critical or high-severity defects; branch coverage of billing at least 90%.

*Resources* Two testers, one automation engineer, a test environment with anonymized patient data, and Selenium, JUnit, and a load-testing tool. *Schedule* System testing in weeks 9 and 10, acceptance testing in week 11, aligned with the development milestones. *Risks* Late delivery of the billing module (mitigated by testing booking first); unavailability of the gateway sandbox (mitigated by service virtualization). *Metrics and reporting* Tests executed and passed, defects by severity, defect density, and coverage, reported daily during system testing. *Deliverables* The test plan, test cases, defect log, and test summary report.
--- answer
Test case TC-APPT-03. *Objective*: a slot that is already booked cannot be booked again. *Preconditions*: Dr Rao's 10:00 slot on 5 May is booked by patient P1; receptionist R is logged in. *Steps*: 1. Search Dr Rao's slots for 5 May. 2. Select 10:00. 3. Try to book it for patient P2. *Test data*: doctor Rao, date 5 May, time 10:00, patient P2. *Expected result*: the 10:00 slot is shown as unavailable and the booking is refused with the message 'Slot already booked'; P1's booking is unchanged. *Actual result and status*: recorded during execution.
:::

## 8.2 Verification and validation: the V model

*Verification* asks 'Are we building the product right?': does each work product conform to its specification? *Validation* asks 'Are we building the right product?': does the software meet the needs of its users? The V&V model, usually called the *V model*, arranges development and testing so that every development activity has a corresponding testing activity ([[fig:v-model]]). The left side of the V descends from requirements to code; the right side ascends from unit testing to acceptance testing; the tests at each level are *designed* when the corresponding development work product is produced, but *executed* after coding, on the way up.

The levels correspond as follows:

1. *Requirements analysis ↔ acceptance testing* The user requirements are the basis of the acceptance tests, which are designed as soon as the requirements are agreed and executed by or with the users on the finished system.
2. *System design ↔ system testing* The system requirements and system design are the basis of the system tests, which check the complete, integrated system, functional and non-functional, against its specification.
3. *Architecture design ↔ integration testing* The architecture (the components and their interfaces) is the basis of the integration tests, which check that the components work together.
4. *Module design ↔ unit testing* The detailed design of each module is the basis of its unit tests, which check each component in isolation.
5. *Coding* sits at the bottom of the V; it is verified by code reviews, inspections, and static analysis before unit testing begins.

@fig v-model

The left side is the *verification phase*. Its activities are static: each work product is checked by reviews, walkthroughs, inspections, and audits (Section 8.3) before the next one is built on it. The right side is the *validation phase*. Its activities are dynamic: the software is executed at five levels, component (unit) testing, component integration testing, system integration testing, system testing, and acceptance testing ([[fig:val-levels]]), described in Sections 8.4 and 8.5.

@fig val-levels

The V model has important advantages. Testing is planned from the start, and test design begins with the requirements, so ambiguous or untestable requirements are found early, when they are cheapest to correct. Every requirement and design element has a matching test level, which gives clear traceability and clear responsibilities. Each phase has defined deliverables and review points, which makes progress easy to monitor. Its disadvantages are those of the waterfall model on which it is based: it is rigid; requirements must be stable, because a change late in the process means revising the work products and test designs of several levels; no working software is available until late; and it is poorly suited to projects whose requirements are uncertain. The V model is therefore used for systems whose requirements are well understood and fixed, and above all for safety-critical and regulated systems (medical, avionics, automotive, banking), in which verification at every stage and traceable evidence of testing are required.

::: example ex-vmodel | Applying the V model to an insulin dose system
A hospital commissions software that calculates and records insulin doses. A main controller reads the patient's data from the patient database, CalculateDose computes the dose from the patient's weight and blood glucose, and the dose is displayed to a nurse for confirmation. The software must be certified by a medical regulator. (a) Justify the choice of the V model. (b) For each level of the V, state the work product on the left, the tests designed from it, and one example test executed on the right.
--- solution
(a) The requirements are fixed by clinical protocol and regulation, a wrong dose is dangerous, and the regulator requires documented evidence that every requirement has been verified and tested. The V model provides exactly this: every development work product is reviewed (verification), and every one has a test level designed from it (validation), with traceability between them. Its rigidity matters little, because the requirements are stable.

(b) The four levels and coding are:

1. *Requirements analysis → acceptance test design → acceptance testing* User requirement: 'the nurse must confirm every dose before it is recorded'. Acceptance test, executed with nurses on the ward system: a calculated dose is never recorded without an explicit confirmation.
2. *System design → system test design → system testing* System requirement: 'a dose is displayed within 2 seconds; doses above 20 units require a second nurse'. System tests check the time limit under load and the second-nurse rule for 20 and 21 units (boundary values).
3. *Architecture design → integration test design → integration testing* Architecture: controller, CalculateDose, and the patient database, with the interface getPatientData() returning age and weight. Integration tests check that the units of weight passed across the interface are kilograms and that a missing record is reported, not treated as zero.
4. *Module design → unit test design → unit testing* Module design of CalculateDose: 0.5 units per kilogram, reduced by 10% for patients over 70. Unit tests for weight 70 kg at ages 70 and 71 (35.0 and 31.5 units), with a stub replacing the database (Section 8.4).
5. *Coding* The code is inspected against a checklist (Section 8.3) and statically analyzed before unit testing.
--- answer
The V model suits the system because its requirements are stable and safety-critical and the regulator requires traceable verification. Each left-side work product (user requirements, system design, architecture, module design) is reviewed when produced and has its tests designed at once; the tests are executed on the right at the matching level (acceptance, system, integration, unit).
:::

## 8.3 Reviews, inspections, and audits

Software inspections and reviews analyze and check the system requirements, design models, program source code, and even proposed system tests. These are static verification techniques: you do not need to execute the software to verify it. Reviews and inspections are complementary to testing and have three advantages over it:

1. During testing, errors can mask (hide) other errors. When an error leads to unexpected outputs, you can never be sure whether later output anomalies are due to a new error or are side effects of the original error. Inspection is a static process, so errors do not interact, and a single inspection session can discover many errors.
2. Incomplete versions of a system can be inspected without additional costs. To test an incomplete program you have to develop specialized test harnesses.
3. As well as searching for program defects, an inspection can consider broader quality attributes of a program, such as compliance with standards, portability, and maintainability. It can look for inefficiencies, inappropriate algorithms, and poor programming style that make the system difficult to maintain and update.

Inspections cannot, however, check non-functional characteristics such as performance and usability, or show that the software behaves correctly when running with real data. Both inspection and testing are therefore needed.

The review process ([[fig:review-process]]) has three phases. In *pre-review activities*, the review is planned, a team is chosen, and each reviewer prepares individually, reading the work product and the relevant standards. The *review meeting* is short (two hours at most); the author 'walks through' the document with the team, and a chair records the problems found. In *post-review activities*, the problems raised are addressed: defects are corrected, the software may be refactored, and follow-up checks confirm that every comment has been dealt with.

@fig review-process

An *audit* is an independent, objective examination of a work product or process, carried out by people external to the development team (often an internal audit department or a third-party organization). Instead of looking for technical defects, auditors check for compliance with standards (such as ISO 9001 or CMMI), legal regulations, and internal policies. The scope is broad: management records, security protocols, and licensing agreements are examined as well as the code. The outcome is a formal *audit report* that lists the non-compliances and recommends corrective actions. Where a review asks whether the product is correct, an audit also asks whether it was produced properly: whether it complies with legal and licensing requirements, is traceable to its requirements, is documented well enough to be maintained, and respects ethical constraints such as privacy and fairness.

A *review* is the broadest category: a systematic meeting or process in which a work product (requirements, design, or code) is examined by project personnel, managers, or users to find defects and to provide feedback. *Peer reviews* are conducted by colleagues, as in code reviews and walkthroughs; *management reviews* are conducted by managers to monitor progress and make decisions. *Formal* reviews follow a strict agenda and a documented process; *informal* reviews, such as a 'buddy check', are less structured.

An *inspection* is the most formal and rigorous type of peer review. Defined by Michael Fagan at IBM, it follows six steps ([[fig:fagan]]): *planning*, in which the moderator checks that the work product meets the entry criteria, chooses the team, and schedules the meeting; *overview*, in which the author explains the work product to the team; *preparation*, in which each inspector studies it individually against the checklist; the *inspection meeting*, in which the reader paraphrases the work product and the defects found are logged; *rework*, in which the author corrects every logged defect; and *follow-up*, in which the moderator verifies the corrections and checks the exit criteria. The roles are the *moderator*, who leads the meeting and ensures that the process is followed; the *reader*, who paraphrases the document for the group (the author may take this role in lighter-weight reviews); the *recorder* or scribe, who documents every defect; the *author*; and the *inspectors*. What distinguishes an inspection from other reviews is that it is data-driven: checklists, entry and exit criteria, and defect measurements are used to improve the development process itself, not just the code.

@fig fagan

Program inspections are peer reviews in which team members collaborate to find bugs in the program being developed. The inspection process is driven by a *checklist* of common programming errors ([[fig:inspection-checklist]]). The checklist should be established by discussion with experienced staff and regularly updated as more experience is gained, and it varies from one programming language to another. Different organizations may develop their own checklists based on local standards and practices.

@fig inspection-checklist

::: example ex-inspect | Manual inspections when code is generated by tools
A financial company that used to hold structured peer reviews now generates much of its code with AI tools. The generated code lacks comments, readability, and clear structure, although it works, and the company proposes to cancel all manual inspections and rely only on automated testing. (a) Give two benefits of manual inspections and four kinds of error that inspections find. (b) State the advantages and disadvantages of this decision in terms of reliability, maintainability, and long-term risk. (c) Recommend the most suitable tool for keeping inspections effective.
--- solution
(a) *Benefits.* Inspections improve code quality, because people can detect design flaws, poor readability, and logic that is technically correct but inappropriate, which automated tests do not look for. They also spread understanding of the system: the team learns how the code works, which reduces the risk that only its author (or no one, for generated code) understands it. *Errors found by inspection* include logical design errors; violations of coding standards; poor readability and incorrect or misleading variable names; missing or incorrect comments and incomplete documentation; and, from the checklist, data faults such as uninitialized variables and interface faults such as parameters in the wrong order.

(b) Removing inspections has advantages: development is faster, review time is saved, and automated checks run quickly and consistently on every change. Its disadvantages are more serious. Logical errors that tests do not happen to exercise remain unnoticed; readability and structure degrade, so maintainability falls; technical debt accumulates, which raises the long-term risk; and human insight into whether the code is the right solution is lost. Generated code is particularly likely to be plausible but subtly wrong, so the loss matters more, not less.
--- answer
(c) A *structured inspection checklist* is the most suitable tool. It makes reviewers check systematically for coding-standard compliance, documentation, design consistency, and the classes of fault in [[fig:inspection-checklist]], so that quality is maintained even for generated code and even when inspections are made shorter and lighter-weight rather than removed.
:::

::: example ex-audit | Audits for AI-generated code
Teams now generate much of their code with AI-assisted tools, yet structured audits are still used for verification. (a) List the benefits of audits for compliance gaps, ethical concerns, and maintainability, with an example use case for each. (b) A cybersecurity company develops mostly AI-generated code that is functional but poorly documented and difficult to interpret. Management cancels all audits and relies solely on test design. Propose a test design. (c) Give two reasons why testing cannot fully replace audits.
--- solution
(a) *Compliance gaps.* Audits check the code against regulations, security standards, and licences, which a working program may still violate. Use case: generated code that logs full card numbers breaches PCI DSS; generated code copied from a GPL-licensed source creates a licensing obligation.

*Ethical concerns.* Audits check how data is collected and used and whether decisions are fair and explainable. Use case: a generated loan-scoring function uses postcode as an input, which acts as a proxy for a protected attribute; generated analytics code keeps personal data longer than the privacy policy allows.

*Maintainability.* Audits check readability, structure, documentation, and technical debt, which no functional test measures. Use case: generated code duplicates the same validation logic in ten places with no comments, so a later change to the rule is missed in some of them.

(b) Because the code is hard to read, the test design must be driven by the requirements and threats rather than by the code:

1. *Requirements-based black-box tests* with equivalence partitioning and boundary value analysis for every input.
2. *White-box coverage* measured by a tool, with a minimum of branch coverage and basis paths for the critical functions, so that untested generated logic is visible.
3. *Security tests*: static analysis (SAST), dependency and secret scanning, fuzzing of every input parser, and penetration tests against the OWASP Top 10.
4. *Negative and abuse-case tests*: malformed, oversized, and malicious inputs, and authentication and authorization bypass attempts.
5. *Regression and mutation tests*: an automated regression suite run on every change, with mutation testing to show that the tests actually detect faults.
--- answer
(c) Testing cannot replace audits because (1) testing shows only that the software behaves correctly for the cases tested, while an audit examines whether it *should* behave that way and whether it meets regulations, licences, and ethical standards, which no test oracle states; and (2) testing does not assess the qualities that audits examine without executing the code, such as documentation, readability, design structure, and traceability, so poorly understood generated code would pass its tests and still be unmaintainable and insecure.
:::

## 8.4 Component testing

*Component testing* (also called unit, module, or program testing) is the testing of individual software components in isolation, to detect defects and to verify the functioning of modules, classes, or functions before they are integrated. Its *test basis* is the program specifications (low-level design documents), the component design specifications, the source code itself (for white-box testing), the component requirements derived from the system requirements, and the interface specifications of the component. The process follows the general test process ([[fig:unit-process]]): test conditions are identified from the specifications and code; test cases are designed with white-box techniques (statement, decision, and condition coverage) and black-box techniques (equivalence partitions and boundary values on the component's inputs); the tests are implemented in a framework such as JUnit, NUnit, or pytest; they are executed automatically on every build in a continuous integration (CI/CD) pipeline; and the results are evaluated with code-coverage measures.

@fig unit-process

A component seldom works alone: it calls other components and is called by others. To test it in isolation, the missing neighbors are replaced by *test doubles* ([[fig:stub-driver]], [[fig:stub-driver-tbl]]):

1. A *stub* replaces a *called* (lower-level) component that is not yet developed or must be excluded. It returns predefined responses, so the tester can check that the component under test handles them correctly. Stubs are used in top-down integration.
2. A *driver* replaces a *calling* (higher-level) component. It invokes the component under test with test data and checks its outputs. Drivers are used in bottom-up integration.
3. A *test harness* is the whole test environment of stubs, drivers, and other utilities that executes the tests and records the results.

The stub and the driver are compared in [[fig:stub-driver-tbl]]. A stub answers the question 'does my component handle the responses it receives correctly?'; a driver answers the question 'does my component produce the correct outputs for its inputs?'.

@fig stub-driver

@fig stub-driver-tbl

::: example ex-stubdriver | A stub and a driver for a dose calculation
In the insulin dose system of [[ex:ex-vmodel]], Main_Controller (module A) calls CalculateDose (module B), which calls Database.getPatientData (module C). The dose is 0.5 units per kilogram of body weight. Write (a) a stub that allows B to be tested before C exists, and (b) a driver that allows B to be tested before A exists.
--- solution
(a) The stub takes the place of the database and returns fixed test data; the test calls B, which calls the stub.

```
def getPatientData_stub():                # replaces module C
    return {"age": 65, "weight": 70}      # fixed test data

def test_calculate_dose():
    patient = getPatientData_stub()        # stub called here
    dose = calculate_dose(patient["age"], patient["weight"])
    assert dose == 35                      # 0.5 x 70
```

(b) The driver takes the place of the main controller: it supplies the inputs directly, calls B, and checks the output.

```
def driver_test_calculate_dose():         # replaces module A
    dose = calculate_dose(age=65, weight=70)
    print(f"Driver result: {dose} units")
    assert dose == 35

driver_test_calculate_dose()
```
--- answer
The stub sits *below* the unit and supplies the data the unit asks for; the driver sits *above* the unit and supplies the call and its arguments. Both form part of the test harness, and both are discarded when the real modules A and C are integrated.
:::

## 8.5 Integration and system testing

*Integration testing* verifies the interaction between modules. Its goal is to detect interface defects, data-flow errors, and interaction failures that component tests, which test each part alone, cannot reveal. There are two levels. *Component integration testing* tests the interactions between the components of one system; *system integration testing* tests the interactions between whole systems or subsystems. The inputs to integration testing are the interface specifications (API contracts and message formats), the architectural design showing how components are related, the database schema definitions, the communication protocols (REST, SOAP, message queues), and the system and subsystem design specifications.

### 8.5.1 Integration strategies

In *big bang* integration, all components are combined at once and then tested. It needs no stubs or drivers, but when a test fails the fault may be anywhere, so it is practical only for very small systems. *Incremental* integration adds modules step by step, so that each failure can be traced to the module just added. There are three incremental approaches ([[fig:integ-orders]], [[fig:integ-strategies]]):

1. *Top-down* integration starts with the top-level (main) module and integrates downward, replacing lower modules that are not ready by stubs. Modules may be added *depth-first* (one complete branch at a time) or *breadth-first* (one level at a time). Its advantage is that a skeleton of the whole system, with its major control and decision logic, is working early; its disadvantage is that many stubs are needed and lower-level processing is tested late.
2. *Bottom-up* integration starts with the lowest-level modules and integrates upward, replacing higher modules that are not ready by drivers. Low-level modules are often combined into *clusters* (builds) that perform a sub-function, each tested with a driver. Its advantage is that the foundation services are tested thoroughly and early, and no stubs are needed; its disadvantage is that the program does not exist as a whole until the last module is added.
3. *Sandwich* (hybrid) integration combines the two: top-down for the upper levels and bottom-up for the lower levels, meeting at a middle layer. It uses both stubs and drivers and suits medium and large systems.

@fig integ-orders

With the modules of [[ex:ex-stubdriver]], top-down integration first tests A with a stub for B, then replaces the stub by B and tests A with B, using a stub for C, and finally adds C. Bottom-up integration first tests C with a driver, then adds B and tests B with C through a driver that replaces A, and finally adds A.

@fig integ-strategies

::: example ex-integ-order | Integration orders, stubs, and drivers
A program has the module hierarchy of [[fig:integ-orders]]: M1 calls M2, M3, and M4; M2 calls M5 and M6; M4 calls M7. Give the order of integration for top-down (depth-first and breadth-first) and bottom-up integration, and state the stubs and drivers needed. How would sandwich integration proceed?
--- solution
*Top-down, depth-first*: M1, M2, M5, M6, M3, M4, M7. *Top-down, breadth-first*: M1, M2, M3, M4, M5, M6, M7. In either order each module except M1 is represented by a stub until it is integrated, so six stubs are needed (for M2 to M7). Testing M1 first requires stubs for M2, M3, and M4; when M2 replaces its stub, stubs for M5 and M6 are needed; and so on.

*Bottom-up*: the leaves are tested first: M5 and M6 as a cluster with a driver standing in for M2, M7 with a driver for M4, and M3 with a driver for M1. Then M2 (with M5 and M6) and M4 (with M7) replace their drivers and are tested with a driver for M1. Finally M1 is added. The drivers replace the calling modules M1, M2, and M4, so three drivers are needed, and no stubs.

*Sandwich*: the middle layer M2, M3, M4 is chosen as the target. M1 is tested top-down with stubs for the middle layer, while the clusters {M5, M6} and {M7} are tested bottom-up with drivers; the two parts meet when the real M2, M3, and M4 are integrated.
--- answer
Top-down depth-first M1, M2, M5, M6, M3, M4, M7; breadth-first M1, M2, M3, M4, M5, M6, M7; six stubs. Bottom-up M5, M6, M7, M3, then M2, M4, then M1; three drivers (for M1, M2, and M4). Sandwich: top-down to the middle layer and bottom-up to it at the same time.
:::

### 8.5.2 Interface and data-flow testing

*Interface testing* checks the correctness of what passes between modules: function parameters, data types, data formats, and return values. *Data-flow testing* checks that the correct data flows between modules: that each module receives the value the specification intends, not merely a value of the right type.

::: example ex-interface | Finding interface and data-flow defects
Each pair of modules below passes its own component tests. Find the defect that integration testing reveals in each.

```
# (a) Module A
def get_age():
    return "25"                 # string
# Module B
def calculate_birth_year(age):
    return 2025 - age
# Integration
year = calculate_birth_year(get_age())

# (b)
def get_price():
    return 100
def apply_discount(price):
    return price * 0.9
def final_price():
    price = get_price()
    return apply_discount(50)   # wrong variable used
```
--- answer
(a) An *interface* defect: A returns the age as a string and B expects a number, so the subtraction fails ('cannot subtract a string from an integer'). Each module is correct by itself; the defect is in the agreement between them, and the interface specification must state the type. (b) A *data-flow* defect: final_price passes the constant 50 instead of the price obtained from get_price, so it returns 45.0 instead of 90.0. The types are correct, so only a test that checks the value flowing between the modules finds it.
:::

### 8.5.3 System integration testing

System integration testing (SIT) tests the interaction between different systems and subsystems as a whole, including external third-party systems (payment gateways, SMS providers), databases and middleware, hardware devices (scanners, IoT sensors), and legacy systems reached through adapters. It is performed after component integration testing and before system testing, usually by integration testers or the QA team. Its inputs are the system interface specifications, the API documentation (OpenAPI or Swagger), the message formats (JSON or XML schemas), the network protocols (REST, SOAP, MQTT), and the service level agreements (SLAs) of the external systems. Its techniques are listed in [[fig:sit-techniques]]. Two deserve emphasis. In *contract testing*, the provider of a service publishes a contract describing its API, and each consumer is tested against the contract before the two are integrated, so that an incompatible change is found at once. In *service virtualization*, an external system that is unavailable, slow, or costly to call is simulated; it plays the part that a stub plays in component testing, but for a complex dependency. The differences between the two levels of integration testing are summarized in [[fig:cit-vs-sit]].

@fig sit-techniques

@fig cit-vs-sit

### 8.5.4 System testing

*System testing* is the testing of an integrated system to evaluate its compliance with the specified requirements. It validates the complete system in an environment that mirrors production, testing both what the system does (*functional* testing) and how well it does it (*non-functional* testing) ([[fig:sys-test-types]]). Before it begins, the system requirements specification, the functional requirements (use cases or user stories), the non-functional requirements (performance and security specifications), the interface specifications, and the business rules must exist.

@fig sys-test-types

Functional system tests are designed with the black-box techniques of Section 8.8: *equivalence partitioning* for input fields with valid and invalid ranges (a password of 8 to 64 characters: 'Pass1234' is valid, 'short' is rejected); *boundary value analysis* for numeric and text limits (an age of 18 to 120: test 17, 18, 19, 119, 120, and 121); *decision tables* for complex business rules (premium and standard customers, orders above and below a limit: all four combinations); and *state transitions* for workflows (an order that is CREATED, PAID, SHIPPED, and DELIVERED must not go from PAID to DELIVERED without being SHIPPED). Non-functional system tests include *performance* testing (response times under normal load), *load* testing (behavior at the expected peak), *stress* testing (behavior beyond the peak, and recovery from it), *security*, *usability*, *compatibility* (browsers, devices, and operating systems), and *recovery* testing (the system is made to fail and its recovery is checked). System testing is followed by *acceptance testing*, in which users check the system against their requirements in their own environment: *alpha* testing by users at the developer's site, *beta* testing by users at their own sites, and formal *user acceptance testing* before the system is accepted.

::: example ex-sit | Integration and system tests for a hospital information system
A hospital's patient registration system sends lab orders to a separate laboratory system, which returns results to a results-delivery portal. Registration also charges fees through an external payment gateway that charges for every call. (a) Design the system integration tests. (b) Give two functional and three non-functional system tests.
--- solution
(a) *End-to-end flow*: register a patient, order a blood test, record the result in the laboratory system, and check that the result appears on the portal for that patient, with the same patient identifier in all three systems. *Contract testing*: the laboratory system publishes the contract of its order API (fields, types, and error codes), and registration is tested against it, so a renamed field is found before deployment. *Service virtualization*: the payment gateway is replaced by a virtual service that returns success, decline, and timeout responses, so that all three are tested without charges. *Message testing*: if results are sent as events, check that a result event is consumed exactly once and in order. *Database integration*: a patient created in registration appears with the same data in the laboratory database.
--- answer
(b) Functional: a patient cannot be registered twice with the same national ID (equivalence partitions: new ID, existing ID); an appointment moves only through valid states (booked → checked in → completed). Non-functional: *performance*, a result appears on the portal within 5 seconds of being recorded; *load*, 500 concurrent registrations complete without errors; *security*, a patient can see only their own results.
:::

## 8.6 White-box testing

White-box testing (also called clear-box, open-box, or glass-box testing) examines the internal structure, logic, and code of an application. Tests are designed from knowledge of the implementation, and the tester has access to the source code. Its objectives are to ensure that all internal operations work as the design specifies and to identify hidden errors, security vulnerabilities, and inefficiencies. It finds logical errors, broken or badly structured paths, typographical errors, and unreachable or redundant code. It is needed in addition to black-box testing because logic errors tend to hide on paths that are rarely executed, which tests derived from the specification may never reach.

*Code coverage* measures how much of the code is executed by a test suite. *Statement coverage* is the percentage of executable statements executed at least once; *branch coverage* is the percentage of decision outcomes (branches) taken at least once, so an if statement needs one test for its true branch and one for its false branch; and *path coverage* is the percentage of feasible paths executed. Each is computed as (number executed ÷ total number) × 100%. Full path coverage implies full branch coverage, which implies full statement coverage, but not the reverse.

::: example ex-coverage | Statement, branch, and path coverage
The function below has six statements (S1–S6) and two decisions with two outcomes each. Find the coverage achieved by the test sets {m = 80}, {m = 30}, and {m = 80, m = 30}.

```
def classify(m):
    result = "Fail"             # S1
    if m >= 40:                 # S2  (decision D1)
        result = "Pass"         # S3
    if m >= 75:                 # S4  (decision D2)
        result = "Distinction"  # S5
    return result               # S6
```
--- solution
m = 80 executes S1–S6 and takes D1-true and D2-true: statement coverage 6/6 = 100%, branch coverage 2/4 = 50%. m = 30 executes S1, S2, S4, S6 and takes both false branches: statement coverage 4/6 = 66.67%, branch coverage 50%. Together they execute all six statements and all four branches.

For paths, the four combinations of outcomes are TT, TF, FT, and FF. FT (m < 40 and m ≥ 75) is infeasible, so there are three feasible paths, needing m = 80, m = 50, and m = 30.
--- answer
{80}: 100% statement, 50% branch. {30}: 66.67% statement, 50% branch. {80, 30}: 100% statement, 100% branch, but path coverage 2/3 = 66.67%; adding m = 50 gives 100% path coverage.
:::

*Control-structure testing* supplements coverage by concentrating on the conditions inside decisions, where five kinds of error are common: Boolean operator errors (AND written for OR), Boolean variable errors (the wrong variable), parenthesis errors, relational operator errors (> written for ≥), and arithmetic expression errors (such as division by zero inside a condition). For a relational expression such as age > 18, testing values just above, equal to, and just below the constant (19, 18, 17) detects most relational operator errors.

## 8.7 Basis path testing

Basis path testing is a white-box method that identifies a set of *independent paths* through a program's control flow graph and designs a test case for each, so that every independent path, and therefore every statement and every branch, is executed at least once.

### 8.7.1 Flow graphs

A control flow graph (flow graph) represents the logic of a program. *Nodes* (circles) represent one or more statements; a sequence of statements with no branching can be collapsed into one node. *Edges* (arrows) represent the transfer of control. A *predicate node* contains a condition and has two or more outgoing edges. A *region* is an area bounded by edges and nodes; the area outside the graph counts as one region. An *independent path* is one that introduces at least one new edge not traversed by any previously listed path. Structured constructs have the standard subgraphs of [[fig:cfg-notation]].

To draw a flow graph, number the executable statements; give each decision (if, loop test, switch) its own node; merge purely sequential statements if desired (this removes one node and one edge together, so it does not change the result); draw a join node where branches meet; draw the back edge of each loop from the end of the body to the loop test; and split a compound condition such as a AND b into one predicate node per simple condition.

@fig cfg-notation

### 8.7.2 Cyclomatic complexity

Cyclomatic complexity, V(G), is a software metric that gives the number of linearly independent paths in a program's flow graph. It is therefore the number of test cases needed to execute every basis path, and an upper bound on the number needed to cover every edge. It can be computed in three ways, which must agree:

1. V(G) = E − N + 2, where E is the number of edges and N the number of nodes (for a single program; in general E − N + 2P for P connected components).
2. V(G) = D + 1, where D is the number of predicate (decision) nodes; a multi-way decision with k outgoing edges counts as k − 1.
3. V(G) = R, the number of regions of the planar flow graph, including the outer region.

Some texts write the second formula as V(G) = P + 1, using P for the number of predicate nodes; this is the same formula, and P here must not be confused with the number of connected components in E − N + 2P.

The basis path testing procedure is: draw the flow graph; compute V(G); list V(G) independent paths, each adding at least one new edge; design a test case, with inputs and expected output, for each path; and execute the tests. Modules with V(G) above about 10 are hard to test and are candidates for refactoring.

::: example ex-larger | Basis paths of a two-way decision
Find the cyclomatic complexity and the basis path tests for: 1 Read A; 2 Read B; 3 IF A > B THEN; 4 Print "A is greater"; 5 ELSE; 6 Print "B is greater"; 7 ENDIF.
--- solution
The flow graph is [[fig:cfg-larger]]. Its edges are 1→2, 2→3, 3→4, 3→5, 5→6, 4→7, 6→7, so E = 7 and N = 7.

@fig cfg-larger

V(G) = E − N + 2 = 7 − 7 + 2 = 2. Check: one predicate node (3), so V(G) = 1 + 1 = 2; two regions, R1 and the outer region.
--- answer
V(G) = 2. Path 1: 1–2–3–4–7 with A = 10, B = 5, expected 'A is greater'. Path 2: 1–2–3–5–6–7 with A = 3, B = 8, expected 'B is greater'. Note that A = B also takes path 2 and prints 'B is greater', which is wrong for equal values; a boundary test (Section 8.8) is needed to find this defect.
:::

::: example ex-nested | A nested decision
Find V(G) and the basis path tests for: 1 if (a < b) 2 F1(); 3 else if (a < c) 4 F2(); 5 else F3(); 6 end.
--- solution
From [[fig:cfg-nested]], the edges are 1→2, 1→3, 3→4, 3→5, 2→6, 4→6, 5→6: E = 7, N = 6, so V(G) = 7 − 6 + 2 = 3. There are two predicate nodes (1 and 3), so D + 1 = 3, and three regions.

@fig cfg-nested
--- answer
V(G) = 3. Path 1–2–6 (a = 1, b = 5, c = 0): F1 executed. Path 1–3–4–6 (a = 5, b = 2, c = 9): F2 executed. Path 1–3–5–6 (a = 5, b = 2, c = 3): F3 executed.
:::

::: example ex-fact | Cyclomatic complexity of a factorial function
Compute the cyclomatic complexity of the following code using a flow graph.

```
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```
--- solution
Number the nodes: 1 the test n == 0; 2 return 1; 3 result = 1 (with the loop initialization i = 1); 4 the loop test i ≤ n; 5 result *= i (with the increment of i); 6 return result; 7 exit. The flow graph is [[fig:cfg-fact]].

@fig cfg-fact

The edges are 1→2, 1→3, 3→4, 4→5, 5→4 (the back edge of the loop), 4→6, 2→7, and 6→7, so E = 8 and N = 7.

V(G) = E − N + 2 = 8 − 7 + 2 = 3.

Check by decisions: the predicate nodes are the if statement (node 1) and the for-loop test (node 4), so D = 2 and V(G) = 2 + 1 = 3. Check by regions: the loop encloses R1, the two branches of the if enclose R2, and R3 is the outer region, so R = 3.

A flowchart that draws only the loop, without the test n == 0, is a flowchart of a different program. It has one decision and gives V(G) = 2; the if statement must appear in the graph.
--- answer
V(G) = 3. The basis paths are 1–2–7 (n = 0, returns 1), 1–3–4–6–7 (loop not entered), and 1–3–4–5–4–6–7 (loop entered, for example n = 3, returns 6). The second path is taken only if the loop test is false at once, which for n ≠ 0 happens only when n is negative; for n = −1 the function returns 1.
:::

::: example ex-countpos | A loop containing a decision
The following code counts the positive elements of an array a of length n: 1 count = 0; 2 i = 0; 3 while i < n; 4 if a[i] > 0; 5 count = count + 1; 6 i = i + 1; 7 print(count). Find V(G) and the basis path tests.
--- solution
The edges in [[fig:cfg-countpos]] are 1→2, 2→3, 3→4, 3→7, 4→5, 4→6, 5→6, and 6→3: E = 8 and N = 7, so V(G) = 8 − 7 + 2 = 3. The predicate nodes are 3 and 4, giving 2 + 1 = 3. Merging the sequential nodes 1 and 2 gives E = 7 and N = 6, and V(G) is still 3.

@fig cfg-countpos
--- answer
V(G) = 3. Path 1–2–3–7 (n = 0): output 0. Path 1–2–3–4–6–3–7 (n = 1, a = [−2]): output 0. Path 1–2–3–4–5–6–3–7 (n = 1, a = [5]): output 1.
:::

::: example ex-leap | Basis paths and equivalence classes for a leap-year function
For the following pseudocode, (a) design test cases for basis path testing and (b) apply equivalence class partitioning.

```
function isLeapYear(year):
    if (year is not divisible by 4) then return False
    else if (year is not divisible by 100) then return True
    else if (year is divisible by 400) then return True
    else return False
```
--- solution
(a) The flow graph has three predicate nodes (1, 3, and 5), one per condition ([[fig:cfg-leap]]). Its edges are 1→2, 1→3, 3→4, 3→5, 5→6, 5→7, and the four returns into the exit node 8, so E = 10 and N = 8: V(G) = 10 − 8 + 2 = 4 = 3 + 1.

@fig cfg-leap

Each independent path is described by the outcome of every condition it passes through. A path cannot be 'divisible by 4, not divisible by 100, and divisible by 400', because a year that is not divisible by 100 returns True before the third condition is tested.

(b) Equivalence classes are formed from the *input domain*. A non-leap year is a valid input with the expected output False, so it is a valid class, not an invalid one. The valid classes follow the rules: V1 not divisible by 4; V2 divisible by 4 but not by 100; V3 divisible by 400; V4 divisible by 100 but not by 400. The invalid classes are inputs outside the specification: I1 a year ≤ 0 (if years must be positive) and I2 a non-integer value.
--- answer
(a) V(G) = 4. Path 1–2–8 (year 2023): False. Path 1–3–4–8 (2024): True. Path 1–3–5–6–8 (2000): True. Path 1–3–5–7–8 (1900): False. (b) Valid classes V1 (2023 → False), V2 (2024 → True), V3 (2000 → True), V4 (1900 → False); invalid classes I1 (−4 → rejected) and I2 ('abc' or 2020.5 → rejected).
:::

::: example ex-sort | Cyclomatic complexity and path tests for a selection sort
Draw the flow graph of the following selection sort, find its cyclomatic complexity, and design a test suite that exercises its paths.

```
void selectionSort(int a[]) {
    int size = a.length;
    for (int i = 0; i < size; i++) {
        int minIndex = i;
        for (int j = i + 1; j < size; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }
        int temp = a[minIndex]; a[minIndex] = a[i]; a[i] = temp;
    }
}
```
--- solution
Number the nodes: 1 size = a.length and i = 0; 2 the outer test i < size; 3 minIndex = i and j = i + 1; 4 the inner test j < size; 5 the test a[j] < a[minIndex]; 6 minIndex = j; 7 j++; 8 the swap and i++; 9 exit ([[fig:cfg-sort]]).

@fig cfg-sort

The edges are 1→2, 2→3, 2→9, 3→4, 4→5, 4→8, 5→6, 5→7, 6→7, 7→4, and 8→2, so E = 11 and N = 9: V(G) = 11 − 9 + 2 = 4. The predicate nodes are 2, 4, and 5, giving 3 + 1 = 4.

Because of the loops, the number of complete paths is unbounded, so path coverage is achieved in practice by the basis paths together with loop tests (zero, one, and several iterations of each loop).
--- answer
V(G) = 4. Basis tests: P1 1–2–9 with a = [] (no change); P2 1–2–3–4–8–2–9 with a = [5] (outer loop once, inner loop zero times); P3 …4–5–7–4… with a = [1, 2] (comparison false, already sorted); P4 …4–5–6–7–4… with a = [2, 1] (comparison true, result [1, 2]). Adding a = [3, 1, 2] (result [1, 2, 3]) exercises several iterations of both loops.
:::

::: example ex-discount-cfg | Basis paths of a discount function
For the following function, (a) calculate the cyclomatic complexity, (b) identify the independent paths, and (c) write test cases that cover them.

```
float calculate_discount(float total_amount, int is_member,
                         char coupon_code[]) {
    if (total_amount <= 0) { return 0; }
    float discount = 0;
    if (is_member) { discount += total_amount * 0.1; }
    if (strcmp(coupon_code, "SAVE20") == 0)
        { discount += total_amount * 0.2; }
    else if (strcmp(coupon_code, "SAVE10") == 0)
        { discount += total_amount * 0.1; }
    float max_discount = total_amount * 0.3;
    if (discount > max_discount) { discount = max_discount; }
    float final_amount = total_amount - discount;
    return final_amount;
}
```
--- solution
Number the nodes: 1 total_amount <= 0?; 2 return 0; 3 discount = 0 and is_member?; 4 member discount; 5 SAVE20?; 6 add 20%; 7 SAVE10?; 8 add 10%; 9 max_discount = 30% and discount > max_discount?; 10 cap the discount; 11 compute and return final_amount; 12 exit ([[fig:cfg-discount]]).

(a) The edges are 1→2, 1→3, 3→4, 3→5, 4→5, 5→6, 5→7, 6→9, 7→8, 7→9, 8→9, 9→10, 9→11, 10→11, 2→12, and 11→12, so E = 16 and N = 12: V(G) = 16 − 12 + 2 = 6. The predicate nodes are 1, 3, 5, 7, and 9 (the else-if is a separate decision), so V(G) = 5 + 1 = 6.

(b) Six independent paths, each adding at least one new edge:

- P1 1–2–12
- P2 1–3–5–7–9–11–12
- P3 1–3–4–5–7–9–11–12
- P4 1–3–4–5–6–9–11–12
- P5 1–3–4–5–7–8–9–11–12
- P6 1–3–…–9–10–11–12

(c) Path P6 requires discount > 0.3 × total_amount, but the largest possible discount is 10% + 20% = 30%, which equals the cap and never exceeds it. P6 is therefore an *infeasible path* in exact arithmetic, and the cap is dead code. The test (200, 1, "SAVE20") gives a discount of 60 and a cap of 60, so it follows P4, not P6, and returns 140. In floating-point arithmetic, rounding can occasionally make the sum of the two discounts exceed the computed cap (for total_amount = 3 the cap is taken and the result is 2.1), so the path is reachable only by accident. The infeasibility is recorded, and the designer is asked whether the cap was intended for a combination that the code does not yet allow.
--- answer
V(G) = 6. Tests: P1 (0, 0, "NONE") → 0; P2 (100, 0, "NONE") → 100; P3 (100, 1, "NONE") → 90; P4 (100, 1, "SAVE20") → 70; P5 (100, 1, "SAVE10") → 80; P6 infeasible, since the combined discount can never exceed the 30% cap (the test (200, 1, "SAVE20") → 140 follows P4).
:::

@fig cfg-discount

::: example ex-flowchart | A flowchart with two decisions
In the following flowchart, b and c are inputs: Start; a = 10; if a > b then a = b; otherwise, if a > c then b = c, else c = a; then print a, b, c; Stop. Compute V(G) by all three methods and design the basis path tests.
--- solution
Number the boxes: 1 Start; 2 a = 10; 3 a > b?; 4 a = b; 5 a > c?; 6 b = c; 7 c = a; 8 print a, b, c; 9 Stop ([[fig:cfg-flowchart]]).

*Method 1.* The edges are 1→2, 2→3, 3→4, 3→5, 5→6, 5→7, 4→8, 6→8, 7→8, 8→9, so E = 10 and N = 9: V(G) = 10 − 9 + 2 = 3.

*Method 2.* The predicate nodes are 3 and 5, so V(G) = 2 + 1 = 3.

*Method 3.* The regions are R1 (3–4–8–6–5–3), R2 (5–6–8–7–5), and the outer region R3, so V(G) = 3.
--- answer
V(G) = 3. Path 1–2–3–4–8–9 (b = 5, c = 3): prints 5, 5, 3. Path 1–2–3–5–6–8–9 (b = 20, c = 4): prints 10, 4, 4. Path 1–2–3–5–7–8–9 (b = 20, c = 30): prints 10, 20, 10.
:::

@fig cfg-flowchart

::: example ex-sumloop | A loop with constant bounds
Find V(G) and the basis path tests for: 1 sum = 0; 2 i = 1; 3 while (i <= 5); 4 sum = sum + i; 5 i++; 6 printf("The sum is: %d", sum); 7 return 0.
--- solution
From [[fig:cfg-sumloop]], the edges are 1→2, 2→3, 3→4, 4→5, 5→3, 3→6, 6→7: E = 7 and N = 7, so V(G) = 7 − 7 + 2 = 2, and the single predicate node (3) gives 1 + 1 = 2.

The basis paths are P1: 1–2–3–6–7 (loop not entered) and P2: 1–2–3–4–5–3–6–7 (loop entered). Because the bounds are constants, the test i ≤ 5 is always true the first time, so no input can make P1 happen: it is an *infeasible path*. An infeasible path is recorded as such and not forced.
--- answer
V(G) = 2. P2 is tested by running the program: it iterates five times and prints 'The sum is: 15'; this single run also traverses the exit edge 3→6, so all seven edges are covered. P1 is infeasible. If the bound were an input n, P1 would be tested with n = 0 (expected output 'The sum is: 0').
:::

A compound condition is split into one predicate node per simple condition. For if (x > 0 AND y > 0) the graph has two predicate nodes and V(G) = 3, and the tests (x = −1, y = 7), (x = 2, y = −3), and (x = 2, y = 3) exercise both simple conditions as false. Treating the compound condition as one node would give V(G) = 2 and would miss an error such as OR written for AND. Similarly, a switch with four outgoing edges counts as 4 − 1 = 3 decisions, so a switch with three cases and a default has V(G) = 4.

@fig cfg-sumloop

### 8.7.3 Graph matrices

A graph matrix is a square matrix whose rows and columns correspond to the nodes of a flow graph; the entry in row i and column j records a direct link from node i to node j. Direction matters, so the matrix is generally not symmetric. Links are usually named with letters and nodes with digits. A *connection matrix* replaces each link by a weight, in the simplest case 1 for a connection. It gives a mechanical way of computing V(G): for each row, count the 1s and subtract 1; ignore empty rows; add the results; and add 1. A row with k entries is a k-way decision and contributes k − 1, so the procedure computes D + 1.

::: example ex-matrix | Cyclomatic complexity from a connection matrix
A flow graph has the links a: 1→1 (a self-loop), b: 1→2, c: 1→3, d: 2→4, and e: 3→4. Draw its graph matrix and connection matrix, find V(G), and list the paths.
--- solution
Each link is entered in the row of the node it leaves and the column of the node it enters ([[fig:gm-graph]]). In the connection matrix, row 1 has three connections (3 − 1 = 2), rows 2 and 3 have one each (1 − 1 = 0), and row 4, the exit node, is empty and is ignored.

V(G) = (2 + 0 + 0) + 1 = 3. Check: E = 5 links and N = 4 nodes, so E − N + 2 = 3. The number of 1s in the matrix (5) equals E, and the number of rows (4) equals N; both are useful checks.
--- answer
V(G) = 3. Following the rows from node 1 to the empty row gives the paths 1–2–4 (links b, d) and 1–3–4 (links c, e); the third independent path uses the self-loop first, 1–1–2–4 (links a, b, d).
:::

@fig gm-graph

When two parallel links join the same pair of nodes, the graph matrix records both in one cell (written a + b). This book follows the common convention of treating such a cell as a single connection when the connection matrix is built, so the cell holds 1; a graph with parallel links a + b from 1 to 2, c from 1 to 3, and d from 3 to 4 therefore has V(G) = (2 − 1) + (1 − 1) + 1 = 2, with the paths 1–2 and 1–3–4. If each link is to be weighted separately, the cell holds 2 and the extra path via b is counted; the convention used should be stated.

## 8.8 Black-box testing

Black-box (behavioral) testing checks the functionality of a system without knowledge of its internal structure, by comparing the outputs produced for given inputs with the expected outputs. It is used to test the functional validity of the software, to look for interface errors, and to test behavior and performance. It finds missing or incorrect functions, which white-box testing cannot, while white-box testing finds untested internal paths, which black-box testing cannot. The two approaches are complementary.

### 8.8.1 Equivalence partitioning

Equivalence class partitioning divides the input data into classes such that all members of a class are expected to behave in the same way. One representative from each class is tested, on the assumption that if it works, all the others will too. A *valid* class contains inputs the system should accept; an *invalid* class contains inputs that it should reject gracefully. An input range gives one valid and two invalid classes; a specific value gives one valid and two invalid classes; a member of a set or a Boolean gives one valid and one invalid class. Valid classes may be combined in one test, but each invalid class should be tested on its own, so that the cause of a rejection is unambiguous.

A login system, for example, accepts a password only if its length L is 6 to 12 characters ([[fig:ecp-line]]). The classes are V1 (6 ≤ L ≤ 12), I1 (L < 6), and I2 (L > 12), and representatives such as lengths 9, 3, and 16 test them.

@fig ecp-line

### 8.8.2 Boundary value analysis

Boundary value analysis (BVA) tests the edges of the input domain, selecting values just below, exactly on, and just above each boundary, because errors cluster at boundaries. Programmers often write < where ≤ was intended, and such off-by-one errors leave typical values unaffected. For a range [a, b] the values are min−, min, min+, a nominal value, max−, max, and max+ ([[fig:bva-line]]). For the password rule the boundary tests are lengths 5, 6, 7, 11, 12, and 13; if the code were written len > 6 and len < 12, the tests at 6 and 12 would fail, whereas a mid-range value such as 9 would detect nothing. With n independent inputs, single-fault BVA needs 4n + 1 tests and robustness testing, which adds min− and max+, needs 6n + 1.

@fig bva-line

::: example ex-age | Equivalence classes and boundary values for two inputs
An insurance form accepts an age from 18 to 60 and a policy type from {Gold, Silver}. Derive the equivalence classes, a minimal equivalence-partitioning test set, and the boundary value tests for age.
--- solution
*Classes.* Age: V1 (18 ≤ age ≤ 60), I1 (age < 18), I2 (age > 60). Policy: V2 (Gold or Silver), I3 (any other value).

*ECP tests.* The valid classes are combined in one test; each invalid class is tested alone with every other input valid: TC1 (35, Gold) → accepted; TC2 (12, Gold) → rejected, age; TC3 (70, Silver) → rejected, age; TC4 (35, Platinum) → rejected, policy.

*BVA tests for age.* Lower boundary 18: 17, 18, 19. Upper boundary 60: 59, 60, 61. With the nominal value 35, single-fault BVA uses 18, 19, 35, 59, 60 (4n + 1 = 5), and robustness testing adds 17 and 61 (6n + 1 = 7).
--- answer
Four ECP tests (one valid, three invalid) and seven boundary tests {17, 18, 19, 35, 59, 60, 61}. The values 17 and 61 also represent the invalid age classes, so the combined suite needs no separate values such as 12 and 70 for age.
:::

::: example ex-bva-fact | Boundary value tests for the factorial function
Identify the boundaries of the input domain of the factorial function of [[ex:ex-fact]] and generate boundary value test cases for it.
--- solution
The specification is that the input is a non-negative integer, so the lower boundary is 0 and negative values are invalid. There is also an upper boundary, because the result must fit in the integer type used by the rest of the system. With 32-bit signed integers (maximum 2,147,483,647), 12! = 479,001,600 fits but 13! = 6,227,020,800 does not, so the valid domain is 0 ≤ n ≤ 12 and 13 is the first invalid value above it. BVA therefore tests −1, 0, 1, a nominal value, 11, 12, and 13.

It is tempting to take an arbitrary 'reasonable' maximum such as 10 and then also test 12 as a valid 'large number'. That is inconsistent: once the maximum is fixed, a value above it is an invalid input, not a valid one. The boundary must come from the specification (here the integer range).
--- answer
1. n = −1 (just below the minimum): expected, the input is rejected with an error. *The given code returns 1*, because range(1, 0) is empty, so this test fails and reveals a defect: the function needs a guard such as if n < 0: raise ValueError.
2. n = 0 (minimum): expected 1.
3. n = 1 (just above the minimum): expected 1.
4. n = 6 (nominal): expected 720.
5. n = 11 (just below the maximum): expected 39,916,800.
6. n = 12 (maximum): expected 479,001,600.
7. n = 13 (just above the maximum): expected, rejected as out of range (13! exceeds the 32-bit range).
:::

::: example ex-subscription | Test cases for a subscription-cost function
A function calculates a yearly subscription cost. The 'basic' plan costs $100 per user and the 'premium' plan $150 per user; for more than 100 users there is a 10% discount on basic and a 15% discount on premium.

```
function calculateYearlySubscriptionCost(numberOfUsers, planType) {
    let costPerUser = planType === 'basic' ? 100 : 150;
    let discount = numberOfUsers > 100 ? (planType === 'basic' ? 0.1 : 0.15) : 0;
    return numberOfUsers * costPerUser * (1 - discount);
}
```

Write test cases covering both plans, the discount boundary, and invalid inputs, with expected outputs and rationale.
--- solution
The inputs are partitioned by plan (basic, premium, invalid) and by user count (invalid ≤ 0, 1 to 100 without discount, above 100 with discount); the boundary is at 100/101. Every expected output is computed from the *specification*, not by running the code.
--- answer
1. (50, 'basic') → 5,000: basic plan, no discount.
2. (100, 'basic') → 10,000: on the boundary; 100 users do not receive the discount.
3. (101, 'basic') → 101 × 100 × 0.9 = 9,090: just above the boundary.
4. (100, 'premium') → 15,000: premium plan on the boundary.
5. (101, 'premium') → 101 × 150 × 0.85 = 12,877.50: premium discount just above the boundary (a tempting wrong answer is 12,835).
6. (1, 'basic') → 100: minimum valid user count.
7. (0, 'basic') and (−1, 'premium') → rejected: invalid user counts. The code returns 0 and −150, so the second test fails and reveals that negative counts are not checked.
8. (50, 'gold') or (50, null) → rejected: invalid plan. The code returns 7,500, because every plan that is not 'basic' is charged as premium; this test also fails and reveals a defect.
:::

::: example ex-transfer | Black-box tests for a fund transfer
A banking application transfers funds between a user's own accounts and to other accounts in the same bank. The user enters the recipient's account number, the amount, and an optional message. Design black-box tests, stating your assumptions.
--- solution
*Assumptions.* Transfers are only within the bank; the amount must be from ₹1 to ₹1,00,000 per transfer; the amount cannot exceed the sender's balance; account numbers have exactly 12 digits; the message is at most 100 characters.

*Equivalence classes.* Valid: V1 own-account transfer; V2 transfer to another customer's account; V3 amount within limits and ≤ balance; V4 12-digit existing account. Invalid: I1 amount < 1; I2 amount > 1,00,000; I3 amount > balance; I4 account number of wrong length; I5 non-existent account; I6 transfer to the same account as the sender; I7 message longer than 100 characters.

*Boundary values for the amount.* 0, 1, 2, a nominal value, 99,999, 1,00,000, and 1,00,001; and, with a balance of 5,000, amounts of 5,000 and 5,001. For the account number, lengths 11, 12, and 13.
--- answer
Representative tests: own-account transfer of ₹500 → success, both balances updated; transfer of ₹1 and ₹1,00,000 to a valid account → success; ₹0 and ₹1,00,001 → rejected; ₹5,001 with a balance of ₹5,000 → rejected, 'insufficient funds', and no balance changes; an 11- or 13-digit account number → rejected; a valid-format number that does not exist → rejected; a transfer to the sender's own source account → rejected; a 101-character message → rejected or truncated as specified.
:::

### 8.8.3 Decision tables and state transitions

*Decision table testing* is used for systems with complex business logic. A decision table lists the *conditions* (inputs that affect behavior), the *actions* (outputs), and the *rules*, each a unique combination of conditions with its actions. A complete table of n Boolean conditions has 2ⁿ rules, and each rule gives a test case. For a login with the conditions 'username correct' and 'password correct', there are four rules; only T, T shows the home page, and the other three show an error message. Rules with the same actions that differ only in one condition may be merged with a 'don't care' entry.

::: example ex-discount | A decision table for a checkout discount
At checkout, a logged-in customer whose cart total exceeds ₹1,000 receives a 10% discount; a logged-in customer with a smaller total pays full price; a customer who is not logged in is redirected to the login page, whatever the total. Build the decision table and derive the test cases.
--- solution
There are two Boolean conditions, C1 (logged in?) and C2 (total > ₹1,000?), so the table has 2² = 4 rules ([[fig:discount-table]]).

@fig discount-table
--- answer
R1: logged in, total ₹1,500 → pays ₹1,350. R2: logged in, total ₹800 → pays ₹800. R3: not logged in, ₹1,500 → login page. R4: not logged in, ₹800 → login page. R3 and R4 have the same action and differ only in C2, so they may be merged into one rule with C2 = '–' (don't care), giving three tests. Boundary values for C2 should be added: a total of exactly ₹1,000 must pay full price, and ₹1,000.01 must receive the discount.
:::

*State transition testing* is used for systems whose behavior depends on their current state and so on the sequence of earlier inputs. The system is modeled by states, transitions, the events that cause them, and the outputs produced. A test is designed for each transition or sequence of events, and invalid events in each state are also tested, where the expected result is that the state does not change. [[fig:pin-state]] models PIN entry at an ATM: the tests are a correct PIN first time; one wrong then correct; two wrong then correct; and three wrong, which blocks the account and is the most important negative test. [[fig:login-state]] models a login system, whose transition table gives five tests: enter username; valid password; invalid password; retry after an error; and logout.

@fig pin-state

@fig login-state

## 8.9 Regression and mutation testing

*Regression testing* is testing performed to ensure that recent changes (bug fixes, new features, or refactoring) have not adversely affected existing functionality. Modules are coupled, so a change in one can break a feature that was never touched; such an unintended side effect is a *regression*. Regression testing re-runs previously passed tests after every fix, after new features are added, after refactoring, and before each release. Its steps are to identify the areas affected by a change, select the relevant test cases, execute them, and analyze the results ([[fig:regression-cycle]]). Because the tests are repeated often, they are usually automated. Regression testing differs from *retesting*, which re-runs the specific test that failed in order to confirm that a reported defect has been fixed.

@fig regression-cycle

*Mutation testing* evaluates the quality of a test suite. Small, deliberate changes (mutations) are made to the source code, such as replacing + with −, > with ≥, or deleting a statement, and the test suite is run against each mutant. If some test fails, the mutant is *killed*; if all tests pass, it *survives*, which reveals a weakness in the tests. An *equivalent mutant* behaves identically to the original for every input and is excluded. The mutation score is

<p class="eq">Mutation score = killed mutants ÷ (total mutants − equivalent mutants) × 100%.</p>

For example, if a suite kills 90 of 120 mutants and none is equivalent, the score is 90 ÷ 120 × 100 = 75%. If 35 of 50 mutants are killed and 5 are equivalent, the score is 35 ÷ 45 × 100 = 77.78%; if improved tests kill 7 more, it becomes 42 ÷ 45 × 100 = 93.33%.

::: example ex-mutation | Killing relational and arithmetic mutants
(a) The code if (x > 5) return "High"; else return "Low"; is tested with x = 10 and x = 2. The mutants are M1: x >= 5, M2: x < 5, and M3: x > 6. Find the mutation score and improve the tests. (b) The code return a + b; with mutants a − b, a * b, and a / b is tested with (a, b) = (2, 2). Find the score and improve the test.
--- solution
(a) For x = 10 the original and M1 and M3 return High, but M2 returns Low, so M2 is killed. For x = 2 the original, M1, and M3 return Low. M1 and M3 survive: score 1 ÷ 3 × 100 = 33.33%. The test x = 5 makes the original return Low and M1 return High, killing M1; the test x = 6 makes the original return High and M3 return Low, killing M3.

(b) The expected result is 4. a − b gives 0 and a / b gives 1, so both are killed, but a * b gives 4 and survives, because 2 + 2 = 2 × 2: score 2 ÷ 3 × 100 = 66.67%. The test (3, 1), expected 4, gives 3 for a * b and kills it.
--- answer
(a) 33.33%, rising to 100% with the tests {10, 2, 5, 6}: boundary values kill relational mutants. (b) 66.67%, rising to 100% with (3, 1): test data should avoid values for which different operators give the same result.
:::

## 8.10 Testing object-oriented and web systems

Object-oriented software needs a different approach because the natural unit of testing is the class, not the function: an operation's result depends on the object's state, operations may be inherited or overridden, and the code executed for a call may be chosen only at run time. *Class testing* exercises sequences of operations on one object, observing its state through public operations because its attributes are encapsulated. *Integration testing* checks that collaborating objects exchange messages correctly. *Inheritance testing* re-runs a base class's tests in the context of each subclass, because an overridden method works under new rules. *Polymorphism testing* supplies a test for each possible binding of a polymorphic call. *Scenario-based testing* follows a use case across several objects. The difficulties are encapsulation, inheritance (a change in a base class can affect every subclass), polymorphism, and state dependencies. The main techniques are *random testing* (random inputs and operation sequences), *fault-based testing* (planting faults, as in mutation testing), *scenario-based testing*, and *use-case testing*. For example, an Account class is class-tested with sequences such as deposit(100), withdraw(40), and getBalance() → 60, and withdraw(10) on a new account → rejected; if SavingsAccount overrides withdraw to keep a minimum balance of 500, the inherited tests are re-run for SavingsAccount, and with a balance of 1,000 it must allow withdraw(500) but reject withdraw(501).

A web-based system runs in a browser and interacts with its users over the Internet, so it must work across many devices, browsers, and network conditions. Its testing includes functional, cross-browser, cross-platform, performance (load and stress), security (such as SQL injection and session hijacking), usability, compatibility, database, API, accessibility, localization and internationalization, and regression testing.

::: example ex-checkout | Testing the checkout of an online store
A clothing store's website lets users browse and buy items online. Describe how you would test the checkout process to ensure a smooth and efficient user experience.
--- answer
1. *Functional testing* of the whole flow: add to cart, enter shipping and billing details, choose a payment method, review, and confirm; check that the order is recorded and a confirmation e-mail is sent.
2. *Form validation and error handling*: invalid e-mail addresses, postal codes, and card numbers must give clear messages without losing the other entries.
3. *Payment testing* for every method (cards, UPI, wallets), including declined and timed-out payments.
4. *Cross-browser and cross-platform testing* on desktop, tablet, and phone.
5. *Performance and load testing* with many simultaneous users, as during a sale.
6. *Security testing*: HTTPS on every page, no storage of card data, and protection against injection and session hijacking.
7. *Usability testing* with real users, who should complete a purchase quickly without help.
8. *Regression testing* of checkout after every change to the cart, pricing, or payment code.
:::

::: keypoints
- Testing executes software with the intent of finding errors. It proceeds from unit to integration, validation, and system testing, and may be manual or automated, functional or non-functional, white-box or black-box.
- The test process is planning and control, analysis, design, implementation and execution, and completion. A test plan states objectives, scope, approach (levels, types, techniques, entry and exit criteria), resources, schedule, risks, metrics, and deliverables; a test case has an ID, preconditions, steps, data, expected result, and actual result.
- The V model pairs each development phase with a test level: requirements with acceptance testing, system design with system testing, architecture with integration testing, and module design with unit testing. The left side is verified by static reviews; the right side is validated by execution.
- A Fagan inspection has six steps (planning, overview, preparation, meeting, rework, follow-up) and the roles of moderator, reader, recorder, author, and inspectors. An audit is an independent check of compliance.
- Stubs replace called modules (top-down integration); drivers replace calling modules (bottom-up). Integration may be big bang, top-down, bottom-up, or sandwich; system integration testing uses end-to-end, contract, and service virtualization techniques.
- Reviews and inspections are static techniques. Errors do not mask one another, incomplete systems can be inspected, and broader quality attributes can be checked. Inspections are driven by checklists of common errors. Audits add independent checks of compliance, ethics, and maintainability that testing cannot provide.
- Statement, branch, and path coverage measure how much of the code is exercised; path coverage implies branch coverage, which implies statement coverage.
- Basis path testing draws a flow graph, computes V(G) = E − N + 2 = D + 1 = R, and designs one test for each independent path. Every decision, including loop tests and each simple part of a compound condition, is a predicate node.
- Equivalence partitioning tests one value from each valid and invalid class; boundary value analysis tests just below, on, and just above each boundary, which must be derived from the specification.
- Decision tables test combinations of conditions; state transition testing tests sequences of events.
- Regression testing checks that changes have not broken existing behavior; mutation testing measures how many deliberately planted faults a test suite detects.
:::
