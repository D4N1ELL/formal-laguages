# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Istrati Daniel

----
## Theory

&ensp;&ensp;&ensp; A finite automaton is a mechanism used to represent processes of different kinds. It can be compared to a state machine as they both have similar structures and purpose as well. The word finite signifies the fact that an automaton comes with a starting and a set of final states. In other words, for process modeled by an automaton has a beginning and an ending.

&ensp;&ensp;&ensp; Based on the structure of an automaton, there are cases in which with one transition multiple states can be reached which causes non determinism to appear. In general, when talking about systems theory the word determinism characterizes how predictable a system is. If there are random variables involved, the system becomes stochastic or non deterministic.

&ensp;&ensp;&ensp; That being said, the automata can be classified as non-/deterministic, and there is in fact a possibility to reach determinism by following algorithms which modify the structure of the automaton.

## Objectives:

1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:

   a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

   b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

   a. Implement conversion of a finite automaton to a regular grammar.

   b. Determine whether your FA is deterministic or non-deterministic.

   c. Implement some functionality that would convert an NDFA to a DFA.

   d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):

    - You can use external libraries, tools or APIs to generate the figures/diagrams.

    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

Please consider that all elements of the task 3 can be done manually, writing a detailed report about how you've done the 
conversion and what changes have you introduced. In case if you'll be able to write a complete program that will take some finite automata and then convert it to the regular grammar - this will be **a good bonus point**.


## Implementation description
We can resolve this problem by trying to see the graph on paper. First i tried to make a table where we can see clearly 
which node connects with another and in what case.
![nfa_blank](https://github.com/D4N1ELL/formal-languages/blob/main/nfa_bank?raw=true)
For a clearer image I also recreated it on the computer:
![nfa](https://github.com/D4N1ELL/formal-languages/blob/main/nfa?raw=true)
Then we reconstruct the table using the new states that we created in the first one, such as q1q2 for example. Then we 
analyze where it repeats and just iterate the same thing over and over until no more new states appear.
![dfa_blank](https://github.com/D4N1ELL/formal-languages/blob/main/dfa_bank?raw=true)
![dfa](https://github.com/D4N1ELL/formal-languages/blob/main/dfa?raw=true)

## Code
First i define a Python class named `StateMachine`, which represents a finite state machine or
automaton, including its states, symbols (alphabet), transition functions, initial state, and final (accepting)
states. The `__init__` method initializes a new instance of the `StateMachine` class with these components.
The `to_grammar` method converts the finite state machine into a regular grammar. For each state in the
machine, it creates a set of production rules based on the transition function; for transitions that lead to
another state on input of a symbol, it adds a production rule combining the symbol and the target state. If a
state is an accepting state, it also adds an epsilon (ε) production, representing an empty string, to signify
that the string can end at this state.

Then the function, `check_determinism`, checks whether a given finite state machine (FSM) is deterministic. It
iterates through each state in the FSM, tracking the symbols it encounters for transitions originating from
that state. If a symbol appears more than once for transitions from the same state, indicating multiple
transitions for the same input (a characteristic of non-deterministic FSMs), the function returns `False`. It
also checks for any missing transitions for a symbol from any state; if a transition is missing, it returns
`False`, implying the FSM is not fully deterministic. If none of these conditions are met for any state, the
FSM is considered deterministic, and the function returns `True`.

The function, `ndfa_to_dfa`, converts a non-deterministic finite automaton (NDFA) into a deterministic
finite automaton (DFA). It starts by initializing the DFA with a single state (assumed to be 'q0' for the
initial state) and prepares to process this and potentially other states. As it iterates through pending states
(initially containing just the start state), it checks each symbol in the NDFA's alphabet to determine the set
of states that can be reached from the current state using that symbol. This set of states forms a new state in
the DFA. The function ensures that each new state is unique by checking if it has already been added to the
DFA's state set; if not, it adds the new state and schedules it for processing. The function also checks if any
of the new states include final states of the NDFA; if so, these new states are marked as final states in the
DFA. The process repeats until there are no more pending states, at which point the function returns the
constructed DFA as a `StateMachine` object, including its states, alphabet, transitions, initial state, and
final states

The `draw` method is part of a finite state machine (FSM) class, designed to visually represent the FSM as
a directed graph. It utilizes the Graphviz library through the `Digraph` class to create and manipulate the
graph. The method sets the graph's orientation as left-to-right and specifies its size. It distinguishes between
non-final and final states by representing them with circles and double circles, respectively. An invisible
start node is created to represent the initial state, with an edge pointing to it, emphasizing the FSM's entry
point. For each transition defined in the FSM, the method draws an edge from the source state to the
destination state, labeling it with the symbol that triggers the transition. This graphical representation aids
in understanding the FSM's structure and behavior visually.
----

## Results:

```commandline
Regular Grammar:
q0 -> aq1
q0 -> bq0
q1 -> bq2
q2 -> bq3
q2 -> aq2
q3 -> ε
is non-deterministic
Converted DFA:
State: q1
 δ(q1, b) = q2
State: q2
 δ(q2, a) = q2
 δ(q2, b) = q3
State: q3
State: q0
 δ(q0, a) = q1
 δ(q0, b) = q0
```
The output consists of two main parts: the conversion of a finite automaton (FA) into a regular grammar
and the conversion of a non-deterministic finite automaton (NDFA) into a deterministic finite automaton
(DFA).
1. **Regular Grammar Conversion:**
- It lists the conversion results of the FA's states into regular grammar rules. Each state is shown to
produce a set of productions, where each production consists of an input symbol followed by a state (or an
empty string, ε, for accept states). For example, `q0 -> aq0` means that from state `q0`, on input `a`, the
automaton transitions back to `q0`. The state `q3` produces `ε`, indicating it's an accept state that can mark
the end of a valid input string.
2. **Determinism Check and DFA Conversion:**
- The FA is identified as non-deterministic, which prompts its conversion into a deterministic finite
automaton (DFA) for simplification and easier analysis.
- The converted DFA's states and their transitions are listed, showing how each state transitions to
another state upon reading an input symbol. For instance, `δ(q0, a) = q0` indicates that in the DFA, from
state `q0`, on input `a`, it remains in `q0`. The DFA simplifies the state transitions to ensure that for every
state and input symbol, there is exactly one possible next state, hence making the automaton deterministic.
- Notably, the state `q3` in the DFA does not have any outgoing transitions listed, which typically
indicates it's an accept state; however, the absence of transitions also means it could be considered a sink
state for certain inputs in the context of DFA

----
## Conclusions
The provided code successfully models and manipulates finite automata (FAs), demonstrating key concepts
in computational theory, such as state machines, determinism, and the conversion between non-deterministic finite automata (NDFAs) and deterministic finite automata (DFAs). 

In conclusion, the work done demonstrates the practical application of theoretical computer science
concepts, offering tools to represent, manipulate, and understand finite automata. It bridges the gap
between abstract theoretical concepts and their practical implementation, facilitating a deeper
understanding of how computational models are constructed and analyzed.