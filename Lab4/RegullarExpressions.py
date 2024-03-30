import re
import itertools

def generate_combinations(regex):
    def process(regex):
        parts = []
        while regex:
            if regex.startswith("{"):
                end_idx = regex.index("}") + 1
                parts.append(regex[:end_idx])
                regex = regex[end_idx:]
            else:
                parts.append(regex[0])
                regex = regex[1:]
        return parts

    def expand_part(part):
        if part.startswith("{") and part.endswith("}"):
            return part[1:-1].split(",")
        elif part.endswith("*"):
            return [part[:-1], ""]
        elif part.endswith("+"):
            return [part[:-1]] + [part[:-1]] * 4
        else:
            return [part]

    def generate_combinations_util(parts):
        expanded_parts = [expand_part(part) for part in parts]
        for combination in itertools.product(*expanded_parts):
            yield "".join(combination)

    processed_regex = process(regex)
    combinations = generate_combinations_util(processed_regex)
    return combinations

def show_processing_sequence(regex):
    def process(regex):
        sequence = []
        while regex:
            if regex.startswith("{"):
                end_idx = regex.index("}") + 1
                sequence.append(regex[:end_idx])
                regex = regex[end_idx:]
            else:
                sequence.append(regex[0])
                regex = regex[1:]
        return sequence

    return process(regex)

# Example regular expressions
regex1 = "{SU*,WY}24"
regex2 = "{LMO*,OPQ}3"
regex3 = "{ABC+}5"

print("Processing Sequence for regex1:", show_processing_sequence(regex1))
print("Generated Combinations for regex1:", list(generate_combinations(regex1)))

print("Processing Sequence for regex2:", show_processing_sequence(regex2))
print("Generated Combinations for regex2:", list(generate_combinations(regex2)))

print("Processing Sequence for regex3:", show_processing_sequence(regex3))
print("Generated Combinations for regex3:", list(generate_combinations(regex3)))


# regex1 = "{S,T}{U,V}W*Y*24"
#
# (S|T)(U|V)W*Y+2U
# L(M|N)O^3P*Q(2|3)
# R*S(T|U|V)W(Z|Y|Z)^2

