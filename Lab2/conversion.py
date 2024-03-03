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


def FiniteAutomaton(Q, Sigma, delta, q0, F):
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F


def main():
    Q = ['q0', 'q1', 'q2', 'q3']
    sigma = ['a', 'b']
    F = ['q3']
    delta = {
        'q0': {'a': ['q1'], 'b': ['q0']},
        'q1': {'b': ['q1', 'q2']},
        'q2': {'a': ['q2'], 'b': ['q3']},
    }


if __name__ == "__main__":
    main()



