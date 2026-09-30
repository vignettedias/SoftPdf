Testing is intended to show that a program does what it is intended to do and to discover program defects before it is put into use. Software testing is the process of evaluating a software application to ensure that it meets its specified requirements. It involves executing a program with the intent of finding errors, verifying its functionality, and ensuring that it performs as expected. The phrase *with the intent of finding errors* is essential: a good test case is one with a high probability of finding an as-yet-undiscovered error, and a test that finds nothing is not thereby a success. Testing can show the presence of errors, but not their absence.

Testing has five objectives: to detect defects before users do; to validate that the software does what its requirements specify; to improve quality (reliability, performance, and usability); to ensure user satisfaction; and to show compliance with the standards and regulations of the application domain.

It is useful to distinguish three terms. An *error* (mistake) is a human action that produces an incorrect result; it leads to a *fault* (defect, bug) in the code; executing the fault may cause a *failure*, an observable deviation from the expected behavior. Testing observes failures in order to locate faults; debugging removes them.

Testing proceeds from the small to the large ([[fig:test-strategy]]). Development moves inward from system engineering through requirements and design to code; testing moves outward. *Unit testing* verifies individual components as coded; *integration testing* verifies the assembled components against the design; *validation testing* confirms the software against its requirements; and *system testing* verifies the software together with the other elements of the system (hardware, people, and databases). Other testing strategies include requirement-based, functional, performance, security, usability, regression, user acceptance, and maintenance testing.

@fig test-strategy

Testing may be classified in three independent ways: by how it is executed (*manual* or *automated*), by what is tested (*functional* testing of what the system does, or *non-functional* testing of how well it does it), and by what the tester knows (*white-box* testing from the code, or *black-box* testing from the specification). A further distinction is between *static* techniques, which examine work products without executing them (reviews, walkthroughs, inspections, and static analysis), and *dynamic* techniques, which execute the software.

## 8.1 Reviews and inspections

Software inspections and reviews analyze and check the system requirements, design models, program source code, and even proposed system tests. These are static verification techniques: you do not need to execute the software to verify it. Reviews and inspections are complementary to testing and have three advantages over it:

1. During testing, errors can mask (hide) other errors. When an error leads to unexpected outputs, you can never be sure whether later output anomalies are due to a new error or are side effects of the original error. Inspection is a static process, so errors do not interact, and a single inspection session can discover many errors.
2. Incomplete versions of a system can be inspected without additional costs. To test an incomplete program you have to develop specialized test harnesses.
3. As well as searching for program defects, an inspection can consider broader quality attributes of a program, such as compliance with standards, portability, and maintainability. It can look for inefficiencies, inappropriate algorithms, and poor programming style that make the system difficult to maintain and update.

Inspections cannot, however, check non-functional characteristics such as performance and usability, or show that the software behaves correctly when running with real data. Both inspection and testing are therefore needed.

The review process ([[fig:review-process]]) has three phases. In *pre-review activities*, the review is planned, a team is chosen, and each reviewer prepares individually, reading the work product and the relevant standards. The *review meeting* is short (two hours at most); the author 'walks through' the document with the team, and a chair records the problems found. In *post-review activities*, the problems raised are addressed: defects are corrected, the software may be refactored, and follow-up checks confirm that every comment has been dealt with.

@fig review-process

Program inspections are peer reviews in which team members collaborate to find bugs in the program being developed. The inspection process is driven by a *checklist* of common programming errors ([[fig:inspection-checklist]]). The checklist should be established by discussion with experienced staff and regularly updated as more experience is gained, and it varies from one programming language to another. Different organizations may develop their own checklists based on local standards and practices.

@fig inspection-checklist

::: example ex-inspect | Manual inspections when code is generated by tools
A food-delivery company's development team now generates much of its code with AI assistants and automated testing tools, and proposes to stop holding manual code inspections. (a) Give two benefits of manual inspections and four kinds of error that inspections find. (b) State the advantages and disadvantages of removing manual inspections. (c) Recommend the most suitable tool for keeping inspections effective.
--- solution
(a) *Benefits.* Inspections improve code quality, because people can detect design flaws, poor readability, and logic that is technically correct but inappropriate, which automated tests do not look for. They also spread understanding of the system: the team learns how the code works, which reduces the risk that only its author (or no one, for generated code) understands it. *Errors found by inspection* include logical design errors; violations of coding standards; poor readability and incorrect or misleading variable names; missing or incorrect comments and incomplete documentation; and, from the checklist, data faults such as uninitialized variables and interface faults such as parameters in the wrong order.

(b) Removing inspections has advantages: development is faster, review time is saved, and automated checks run quickly and consistently on every change. Its disadvantages are more serious. Logical errors that tests do not happen to exercise remain unnoticed; readability and structure degrade, so maintainability falls; technical debt accumulates, which raises the long-term risk; and human insight into whether the code is the right solution is lost. Generated code is particularly likely to be plausible but subtly wrong, so the loss matters more, not less.
--- answer
(c) A *structured inspection checklist* is the most suitable tool. It makes reviewers check systematically for coding-standard compliance, documentation, design consistency, and the classes of fault in [[fig:inspection-checklist]], so that quality is maintained even for generated code and even when inspections are made shorter and lighter-weight rather than removed.
:::

## 8.2 White-box testing

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

## 8.3 Basis path testing

Basis path testing is a white-box method that identifies a set of *independent paths* through a program's control flow graph and designs a test case for each, so that every independent path, and therefore every statement and every branch, is executed at least once.

### 8.3.1 Flow graphs

A control flow graph (flow graph) represents the logic of a program. *Nodes* (circles) represent one or more statements; a sequence of statements with no branching can be collapsed into one node. *Edges* (arrows) represent the transfer of control. A *predicate node* contains a condition and has two or more outgoing edges. A *region* is an area bounded by edges and nodes; the area outside the graph counts as one region. An *independent path* is one that introduces at least one new edge not traversed by any previously listed path. Structured constructs have the standard subgraphs of [[fig:cfg-notation]].

@fig cfg-notation

To draw a flow graph, number the executable statements; give each decision (if, loop test, switch) its own node; merge purely sequential statements if desired (this removes one node and one edge together, so it does not change the result); draw a join node where branches meet; draw the back edge of each loop from the end of the body to the loop test; and split a compound condition such as a AND b into one predicate node per simple condition.

### 8.3.2 Cyclomatic complexity

Cyclomatic complexity, V(G), is a software metric that gives the number of linearly independent paths in a program's flow graph. It is therefore the number of test cases needed to execute every basis path, and an upper bound on the number needed to cover every edge. It can be computed in three ways, which must agree:

1. V(G) = E − N + 2, where E is the number of edges and N the number of nodes (for a single program; in general E − N + 2P for P connected components).
2. V(G) = D + 1, where D is the number of predicate (decision) nodes; a multi-way decision with k outgoing edges counts as k − 1.
3. V(G) = R, the number of regions of the planar flow graph, including the outer region.

The basis path testing procedure is: draw the flow graph; compute V(G); list V(G) independent paths, each adding at least one new edge; design a test case, with inputs and expected output, for each path; and execute the tests. Modules with V(G) above about 10 are hard to test and are candidates for refactoring.

::: example ex-larger | Basis paths of a two-way decision
Find the cyclomatic complexity and the basis path tests for: 1 Read A; 2 Read B; 3 IF A > B THEN; 4 Print "A is greater"; 5 ELSE; 6 Print "B is greater"; 7 ENDIF.
--- solution
The flow graph is [[fig:cfg-larger]]. Its edges are 1→2, 2→3, 3→4, 3→5, 5→6, 4→7, 6→7, so E = 7 and N = 7.

@fig cfg-larger

V(G) = E − N + 2 = 7 − 7 + 2 = 2. Check: one predicate node (3), so V(G) = 1 + 1 = 2; two regions, R1 and the outer region.
--- answer
V(G) = 2. Path 1: 1–2–3–4–7 with A = 10, B = 5, expected 'A is greater'. Path 2: 1–2–3–5–6–7 with A = 3, B = 8, expected 'B is greater'. Note that A = B also takes path 2 and prints 'B is greater', which is wrong for equal values; a boundary test (Section 8.4) is needed to find this defect.
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

A compound condition is split into one predicate node per simple condition. For if (x > 0 AND y > 0) the graph has two predicate nodes and V(G) = 3, and the tests (x = −1, y = 7), (x = 2, y = −3), and (x = 2, y = 3) exercise both simple conditions as false. Treating the compound condition as one node would give V(G) = 2 and would miss an error such as OR written for AND. Similarly, a switch with four outgoing edges counts as 4 − 1 = 3 decisions, so a switch with three cases and a default has V(G) = 4.

### 8.3.3 Graph matrices

A graph matrix is a square matrix whose rows and columns correspond to the nodes of a flow graph; the entry in row i and column j records a direct link from node i to node j. Direction matters, so the matrix is generally not symmetric. Links are usually named with letters and nodes with digits. A *connection matrix* replaces each link by a weight, in the simplest case 1 for a connection. It gives a mechanical way of computing V(G): for each row, count the 1s and subtract 1; ignore empty rows; add the results; and add 1. A row with k entries is a k-way decision and contributes k − 1, so the procedure computes D + 1.

For a graph with links a: 1→1, b: 1→2, c: 1→3, d: 2→4, and e: 3→4, row 1 has three entries (3 − 1 = 2), rows 2 and 3 have one each (0), and row 4 is empty. So V(G) = 2 + 0 + 0 + 1 = 3, which agrees with E − N + 2 = 5 − 4 + 2 = 3.

## 8.4 Black-box testing

Black-box (behavioral) testing checks the functionality of a system without knowledge of its internal structure, by comparing the outputs produced for given inputs with the expected outputs. It is used to test the functional validity of the software, to look for interface errors, and to test behavior and performance. It finds missing or incorrect functions, which white-box testing cannot, while white-box testing finds untested internal paths, which black-box testing cannot. The two approaches are complementary.

### 8.4.1 Equivalence partitioning

Equivalence class partitioning divides the input data into classes such that all members of a class are expected to behave in the same way. One representative from each class is tested, on the assumption that if it works, all the others will too. A *valid* class contains inputs the system should accept; an *invalid* class contains inputs that it should reject gracefully. An input range gives one valid and two invalid classes; a specific value gives one valid and two invalid classes; a member of a set or a Boolean gives one valid and one invalid class. Valid classes may be combined in one test, but each invalid class should be tested on its own, so that the cause of a rejection is unambiguous.

A login system, for example, accepts a password only if its length L is 6 to 12 characters ([[fig:ecp-line]]). The classes are V1 (6 ≤ L ≤ 12), I1 (L < 6), and I2 (L > 12), and representatives such as lengths 9, 3, and 16 test them.

@fig ecp-line

### 8.4.2 Boundary value analysis

Boundary value analysis (BVA) tests the edges of the input domain, selecting values just below, exactly on, and just above each boundary, because errors cluster at boundaries. Programmers often write < where ≤ was intended, and such off-by-one errors leave typical values unaffected. For a range [a, b] the values are min−, min, min+, a nominal value, max−, max, and max+ ([[fig:bva-line]]). For the password rule the boundary tests are lengths 5, 6, 7, 11, 12, and 13; if the code were written len > 6 and len < 12, the tests at 6 and 12 would fail, whereas a mid-range value such as 9 would detect nothing. With n independent inputs, single-fault BVA needs 4n + 1 tests and robustness testing, which adds min− and max+, needs 6n + 1.

@fig bva-line

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

### 8.4.3 Decision tables and state transitions

*Decision table testing* is used for systems with complex business logic. A decision table lists the *conditions* (inputs that affect behavior), the *actions* (outputs), and the *rules*, each a unique combination of conditions with its actions. A complete table of n Boolean conditions has 2ⁿ rules, and each rule gives a test case. For a login with the conditions 'username correct' and 'password correct', there are four rules; only T, T shows the home page, and the other three show an error message. Rules with the same actions that differ only in one condition may be merged with a 'don't care' entry.

*State transition testing* is used for systems whose behavior depends on their current state and so on the sequence of earlier inputs. The system is modeled by states, transitions, the events that cause them, and the outputs produced. A test is designed for each transition or sequence of events, and invalid events in each state are also tested, where the expected result is that the state does not change. [[fig:pin-state]] models PIN entry at an ATM: the tests are a correct PIN first time; one wrong then correct; two wrong then correct; and three wrong, which blocks the account and is the most important negative test. [[fig:login-state]] models a login system, whose transition table gives five tests: enter username; valid password; invalid password; retry after an error; and logout.

@fig pin-state

@fig login-state

## 8.5 Regression and mutation testing

*Regression testing* is testing performed to ensure that recent changes (bug fixes, new features, or refactoring) have not adversely affected existing functionality. Modules are coupled, so a change in one can break a feature that was never touched; such an unintended side effect is a *regression*. Regression testing re-runs previously passed tests after every fix, after new features are added, after refactoring, and before each release. Its steps are to identify the areas affected by a change, select the relevant test cases, execute them, and analyze the results ([[fig:regression-cycle]]). Because the tests are repeated often, they are usually automated. Regression testing differs from *retesting*, which re-runs the specific test that failed in order to confirm that a reported defect has been fixed.

@fig regression-cycle

*Mutation testing* evaluates the quality of a test suite. Small, deliberate changes (mutations) are made to the source code, such as replacing + with −, > with ≥, or deleting a statement, and the test suite is run against each mutant. If some test fails, the mutant is *killed*; if all tests pass, it *survives*, which reveals a weakness in the tests. An *equivalent mutant* behaves identically to the original for every input and is excluded. The mutation score is

<p class="eq">Mutation score = killed mutants ÷ (total mutants − equivalent mutants) × 100%.</p>

For example, if 35 of 50 mutants are killed and 5 are equivalent, the score is 35 ÷ 45 × 100 = 77.78%; if improved tests kill 7 more, it becomes 42 ÷ 45 × 100 = 93.33%. For the code if (x > 5) return "High" with the tests x = 10 and x = 2, the mutant x ≥ 5 survives until the boundary test x = 5 is added, and the mutant x > 6 survives until x = 6 is added: boundary values kill relational mutants.

## 8.6 Testing object-oriented and web systems

Object-oriented software needs a different approach because the natural unit of testing is the class, not the function: an operation's result depends on the object's state, operations may be inherited or overridden, and the code executed for a call may be chosen only at run time. *Class testing* exercises sequences of operations on one object, observing its state through public operations because its attributes are encapsulated. *Integration testing* checks that collaborating objects exchange messages correctly. *Inheritance testing* re-runs a base class's tests in the context of each subclass, because an overridden method works under new rules. *Polymorphism testing* supplies a test for each possible binding of a polymorphic call. *Scenario-based testing* follows a use case across several objects. The difficulties are encapsulation, inheritance (a change in a base class can affect every subclass), polymorphism, and state dependencies.

A web-based system runs in a browser and interacts with its users over the Internet, so it must work across many devices, browsers, and network conditions. Its testing includes functional, cross-browser, cross-platform, performance (load and stress), security (such as SQL injection and session hijacking), usability, compatibility, database, API, accessibility, localization and internationalization, and regression testing.

::: keypoints
- Testing executes software with the intent of finding errors. It proceeds from unit to integration, validation, and system testing, and may be manual or automated, functional or non-functional, white-box or black-box.
- Reviews and inspections are static techniques. Errors do not mask one another, incomplete systems can be inspected, and broader quality attributes can be checked. Inspections are driven by checklists of common errors.
- Statement, branch, and path coverage measure how much of the code is exercised; path coverage implies branch coverage, which implies statement coverage.
- Basis path testing draws a flow graph, computes V(G) = E − N + 2 = D + 1 = R, and designs one test for each independent path. Every decision, including loop tests and each simple part of a compound condition, is a predicate node.
- Equivalence partitioning tests one value from each valid and invalid class; boundary value analysis tests just below, on, and just above each boundary, which must be derived from the specification.
- Decision tables test combinations of conditions; state transition testing tests sequences of events.
- Regression testing checks that changes have not broken existing behavior; mutation testing measures how many deliberately planted faults a test suite detects.
:::
