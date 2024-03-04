# Given that:
# AF = (Q,∑,δ,q0,F)
#
# Variant 16
# Q = {q0,q1,q2,q3},
# ∑ = {a,b},
# F = {q3},
# δ(q0,a) = q1,
# δ(q1,b) = q1,
# δ(q1,b) = q2,
# δ(q2,a) = q2,
# δ(q2,b) = q3,
# δ(q0,b) = q0.

from graphviz import Digraph


class StateMachine:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def to_grammar(self):
        grammar_rules = {}
        for state in self.Q:
            grammar_rules[state] = set()
            for symbol in self.sigma:
                if (state, symbol) in self.delta:
                    destination = self.delta[(state, symbol)]
                    grammar_rules[state].add(symbol + destination)
            if state in self.F:
                grammar_rules[state].add('ε')  # ε represents an empty string (epsilon)
        return grammar_rules

    def draw(self):
        graph = Digraph()
        graph.attr(rankdir='LR', size='8,5')

        # Non-final states
        for state in set(self.Q) - set(self.F):
            graph.node(state, shape='circle')
        # Final states
        for state in set(self.F):
            graph.node(state, shape='doublecircle')

        # Invisible start node
        graph.node('', shape='none')
        graph.edge('', self.q0)

        # Edges for delta
        for (source, symbol), destination in self.delta.items():
            graph.edge(source, destination, label=symbol)

        return graph


Q = ['q0', 'q1', 'q2', 'q3']
sigma = ['a', 'b']
F = ['q3']
initial = 'q0'
delta = {
    ('q0', 'a'): 'q1',
    ('q1', 'b'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q3',
    ('q0', 'b'): 'q0'

}


def check_determinism(machine):
    for state in machine.Q:
        observed_sigma = set()
        for symbol in machine.sigma:
            if (state, symbol) in machine.delta:
                if symbol in observed_sigma:
                    return False  # Duplicate transition for a state and symbol
                observed_sigma.add(symbol)
            else:
                return False  # Missing transition for a state and symbol
    return True


def ndfa_to_dfa(ndfa):
    dfa_states = set(['q0'])  # Start with the initial state
    dfa_F = set()
    dfa_delta = {}
    pending_states = [{'q0'}]  # States to process

    while pending_states:
        current_state = pending_states.pop()
        for symbol in ndfa.sigma:
            new_Q = set()
            for state in current_state:
                if (state, symbol) in ndfa.delta:
                    new_Q.add(ndfa.delta[(state, symbol)])
            if new_Q:
                new_state_id = ''.join(sorted(new_Q))
                dfa_delta[(''.join(sorted(current_state)), symbol)] = new_state_id
                if new_state_id not in dfa_states:
                    dfa_states.add(new_state_id)
                    pending_states.append(new_Q)
                if new_Q & set(ndfa.F):
                    dfa_F.add(new_state_id)

    return StateMachine(dfa_states, ndfa.sigma, dfa_delta, 'q0', dfa_F)



sm = StateMachine(Q, sigma, delta, initial, F)
grammar = sm.to_grammar()
print("Regular Grammar:")
for left_side, production_set in grammar.items():
    for production in production_set:
        print(f"{left_side} -> {production}")

determinism_check = "deterministic" if check_determinism(sm) else "non-deterministic"
print("is", determinism_check)

converted_dfa = ndfa_to_dfa(sm)
# Display the converted DFA
print("Converted DFA:")
for state in converted_dfa.Q:
    print(f"State: {state}")
    for symbol in converted_dfa.sigma:
        if (state, symbol) in converted_dfa.delta:
            print(f" δ({state}, {symbol}) = {converted_dfa.delta[(state, symbol)]}")

sm_graph = sm.draw()

# Render the graph to a file and view it
output_path = 'state_machine_variant_16'
sm_graph.render(output_path, view=True, format='png')