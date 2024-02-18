#
# # Variant 16:
# VN={S, A, B},
# VT={a, b, c, d},
# P={
#     S → bS
#     S → dA
#     A → aA
#     A → dB
#     B → cB
#     A → b
#     B → a
# }
# Get the grammar definition and do the following:
#
#     a. Implement a type/class for your grammar;
#     b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;
#     c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
#     d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


class Grammar:
    def __init__(self, VN, VT, P):
        self.VN = VN
        self.VT = VT
        self.P = P

    def generate_valid_strings(self, start_symbol, num_strings):
        def generate_string(current_string, remaining_length):
            if remaining_length == 0:
                return [current_string]

            valid_strings = []
            for production in self.P:
                if production[0] == current_string[-1]:
                    for symbol in production[1:]:
                        valid_strings.extend(generate_string(current_string + symbol, remaining_length - 1))
            return valid_strings

        valid_strings = []
        for production in self.P:
            if production[0] == start_symbol:
                for symbol in production[1:]:
                    valid_strings.extend(generate_string(symbol, num_strings - 1))
        return valid_strings[:num_strings]

    def to_finite_automaton(self):
        states = set()
        alphabet = self.VT
        transitions = {}
        start_state = 'S'
        accepting_states = set()

        for production in self.P:
            from_state = production[0]
            to_state = production[1]
            states.add(from_state)
            states.add(to_state)
            if from_state not in transitions:
                transitions[from_state] = {}
            transitions[from_state][to_state] = None

            if len(production) == 2 and production[1] in self.VT:
                accepting_states.add(to_state)

        return FiniteAutomaton(states, alphabet, transitions, start_state, accepting_states)


class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    def is_valid_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.accepting_states


# Define the grammar
VN = {'S', 'A', 'B'}
VT = {'a', 'b', 'c', 'd'}
P = [
    'S → bS',
    'S → dA',
    'A → aA',
    'A → dB',
    'B → cB',
    'A → b',
    'B → a'
]

# Create a grammar object
grammar = Grammar(VN, VT, P)

# Generate 5 valid strings
valid_strings = grammar.generate_valid_strings('S', 5)
print("5 Valid Strings:")
for string in valid_strings:
    print(string)

# Convert grammar to finite automaton
finite_automaton = grammar.to_finite_automaton()

# Test if a string is valid in the generated finite automaton
test_string = 'abdc'
print(f"Is '{test_string}' a valid string in the finite automaton? {finite_automaton.is_valid_string(test_string)}")

