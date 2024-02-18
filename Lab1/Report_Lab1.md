# Regular Grammars & Finite Automata

### Course: Formal Languages & Finite Automata
### Author: Istrati Daniel
----
## Theory

&ensp;&ensp;&ensp; A formal language can be considered to be the media or the format used to convey information from a sender entity to the one that receives it. The usual components of a language are:
- The alphabet: Set of valid characters;
- The vocabulary: Set of valid words;
- The grammar: Set of rules/constraints over the lang.

## Objectives:

1. Discover what a language is and what it needs to have in order to be considered a formal one;

2. Provide the initial setup for the evolving project that you will work on during this semester. You can deal with each laboratory work as a separate task or project to demonstrate your understanding of the given themes, but you also can deal with labs as stages of making your own big solution, your own project. Do the following:
    a. Create GitHub repository to deal with storing and updating your project;
    b. Choose a programming language. Pick one that will be easiest for dealing with your tasks, you need to learn how to solve the problem itself, not everything around the problem (like setting up the project, launching it correctly and etc.);
    c. Store reports separately in a way to make verification of your work simpler (duh)

3. According to your variant number, get the grammar definition and do the following:
    a. Implement a type/class for your grammar;
    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;
    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description


1. Firslty i created 2 classes which contain the methods and attributes of the grammar. First one is `Grammar` and it contains:
    - 2 sets : non-terminal and terminal symbols, and a dictionary containing the production rules of the grammar;

```
class Grammar:
    def __init__(self):
        self.Non_Terminal = {'S', 'A', 'B'}
        self.Terminal = {'a', 'b', 'c', 'd'}
        self.Production = {
            'S': ['bS', 'dA'],
            'A': ['aA', 'dB', 'b'],
            'B': ['cB', 'a']
        }
```

2. The `generate_string` function generates correct strings from the language expressed by the given grammar. The function works by starting from the start symbol and then randomly choosing a production rule from the ones allowed by the grammar for this symbol and adding the symbols to the string. If the symbol is a terminal symbol the function stops, otherwise it continues with the next symbol in the production rule.

```
 def generate_string(self):
        string = ''
        current_symbol = 'S'
        while current_symbol in self.VN:
            production = random.choice(self.P[current_symbol])
            for symbol in production:
                if symbol in self.VT:
                    string += symbol
                    current_symbol = ''
                else:
                    current_symbol = symbol
                    break
        return string
```

3. The `to_finite_automaton` method is used to convert the grammar to a finite automaton. The method creates a finite automaton and initiates a FiniteAutomaton object with the following attributes:
    - `Q` - a set of states;
    - `Sigma` - a set of input symbols;
    - `delta` - a dictionary containing the state transitions;
    - `q0` - the initial state;
    - `F` - a set of final states;

    The method works by iterating through the production rules and adding the state transitions to the delta dictionary. If the production rule is of the form `A -> a` then the state `A` is added to the dictionary with the input symbol `a` and the value `[a]`. If the production rule is of the form `A -> aB` then the state `A` is added to the dictionary with the input symbol `a` and the value `[B]`.

```
   def to_finite_automaton(self):
        Q = self.VN
        Sigma = self.VT
        delta = {}
        for state, productions in self.P.items():
            for production in productions:
                if len(production) == 1:
                    if production.islower():
                        delta.setdefault(state, {}).setdefault(production, [production])
                else:
                    delta.setdefault(state, {}).setdefault(production[0], []).append(production[1:])
        q0 = 'S'
        F = [t for production in self.P for t in self.P[production] if len(t) == 1 and t.islower()]
        return FiniteAutomaton(Q, Sigma, delta, q0, F)
```

4. The `string_belongs_to_language` method is used to check if an input string can be obtained via the state transition from the finite automaton. The method works by iterating through the input string and checking if character and the state transition is valid. If the state transition is not valid the method returns False, otherwise it returns True. Also, if the explicit parameter is set to True the method will print the reason why the string is not valid.

```
   def string_belongs_to_language(self, input_string, explicit=False):
        current_state = self.q0
        for symbol in input_string:
            if symbol not in self.Sigma:
                if explicit:
                    print("Invalid symbol in input string")
                return False
            if symbol in self.delta.get(current_state, {}):
                current_state = self.delta[current_state][symbol][0]
            else:
                if explicit:
                    print("Invalid transition")
                return False
        return current_state in self.F
```

----

## Results:

### The obtained finite automaton:

```
Q: {'B', 'A', 'S'}
Sigma: {'c', 'a', 'b', 'd'}
delta: {'S': {'b': ['S'], 'd': ['A']}, 'A': {'a': ['A'], 'd': ['B'], 'b': ['b']}, 'B': {'c': ['B'], 'a': ['a']}}
q0: S
F: ['b', 'a']
```

### Loops to generate random strings and check if belong to language:

1. First with valid strings, generated by the grammar and as expected all the strings belong to the language.

```
=======================================
Generated string: db
String belongs to language: True

=======================================
Generated string: db
String belongs to language: True

=======================================
Generated string: bdab
String belongs to language: True

=======================================
Generated string: db
String belongs to language: True

=======================================
Generated string: bdab
String belongs to language: True

=======================================
Generated string: db
String belongs to language: True

=======================================
Generated string: dda
String belongs to language: True

=======================================
Generated string: bbddcca
String belongs to language: True

=======================================
Generated string: bbbbdb
String belongs to language: True

=======================================
Generated string: bbbdb
String belongs to language: True

2. Then with invalid strings, generated by the grammar and then modified by adding an invalid character and as expected all the strings did not belong to the language.
```
=======================================
Generated string: dbx
Invalid symbol in input string
String belongs to language: False

=======================================
Generated string: bdaabx
Invalid symbol in input string
String belongs to language: False

=======================================
Generated string: ddxa
Invalid symbol in input string
String belongs to language: False
```

3. Then with invalid strings, generated randomly and as expected all the strings did not belong to the language.

```
=======================================
Generated string: addcccbaba
Invalid transition
String belongs to language: False

=======================================
Generated string: ddaccbbcdc
Invalid transition
String belongs to language: False

=======================================
Generated string: dcaacacbaa
Invalid transition
String belongs to language: False

=======================================
Generated string: cccbccbdad
Invalid transition
String belongs to language: False

=======================================
Generated string: ababcdbcba
Invalid transition
String belongs to language: False

=======================================
Generated string: dadcddddbc
Invalid transition
String belongs to language: False

=======================================
Generated string: bacaaddbcd
Invalid transition
String belongs to language: False

=======================================
Generated string: ccdddccaad
Invalid transition
String belongs to language: False

=======================================
Generated string: dcdbadbada
Invalid transition
String belongs to language: False

=======================================
Generated string: dbcbbadcdb
Invalid transition
String belongs to language: False
```

4. And finally with invalid strings, generated by the grammar and then modified by removing a character and as expected there were some strings that did belong to the language and some that did not. This is because the grammar has some repetitive production rules and removing a character can result in a valid string.
```
=======================================
Generated string: dada
Removing symbol at index 3
Modified string: dad
String belongs to language: False

=======================================
Generated string: bbbdb
Removing symbol at index 0
Modified string: bbdb
String belongs to language: True

=======================================
Generated string: ddcca
Removing symbol at index 1
Modified string: dcca
Invalid transition
String belongs to language: False
```

----
## Conclusions
During this laboratory work i learned how to implemet grammar rules and finite automation in code and also strengthened my understandings about this course. 
