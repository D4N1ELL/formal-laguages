import random

def generateString(rule):
    string = ""
    i = 0
    while i < len(rule):

        # cover case when 1 occurrence from options
        if (rule[i] == "(" and rule.index(")", i) == len(rule) - 1) or (
                rule[i] == "(" and rule[rule.index(")", i) + 1] not in ["*", "+", "?", "{"]):
            char = choice(options(rule[i + 1:rule.index(")", i)]))
            string += char
            i = rule.index(")", i)
            print(f"Just one occurrence from options: Adding {char} to string => {string}")

        # cover case when 1 or more occurrences from options
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "+":
            times = random.randint(1, 5)
            for _ in range(times):
                char = choice(options(rule[i + 1:rule.index(")", i)]))
                string += char
                print(f"One or more occurrences from options: Adding {char} to string => {string}")
            i = rule.index(")", i) + 1

        # cover case when 0 or more occurrences from options
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "*":
            for _ in range(random.randint(0, 5)):
                char = choice(options(rule[i + 1:rule.index(")", i)]))
                string += char
                print(f"Zero or more occurrences from options: Adding {char} to string => {string}")
            i = rule.index(")", i) + 1

        # cover case when fixed occurrences from options
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "{":
            for _ in range(int(rule[rule.index("{", i) + 1])):
                char = choice(options(rule[i + 1:rule.index(")", i)]))
                string += char
                print(f"Fixed occurrences from options: Adding {char} to string => {string}")
            i = rule.index("}", i) + 1

        # cover case when 0 or 1 occurrence from options
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "?":
            if random.randint(0, 1):
                char = choice(options(rule[i + 1:rule.index(")", i)]))
                string += char
                print(f"Zero or one occurrence from options: Adding {char} to string => {string}")
            i = rule.index(")", i) + 1

        elif i < len(rule) - 2 and rule[i + 1] == "?":
            if random.randint(0, 1):
                string += rule[i]
                print(f"Zero or one occurrence: Adding {rule[i]} to string => {string}")
            i += 2



        elif rule[i] in '(){|+*?' + '}':
            i += 1
            pass

        else:
            string += rule[i]
            print(f"Adding {rule[i]} to string => {string}")
            i += 1

    return string


def choice(options):
    return random.choice(options)


def options(sequence):
    return sequence.split("|")


rule1 = "(S|T)(U|V)W*Y+2U"
print('Final string: ', generateString(rule1))
print('-' * 70)

rule2 = "L(M|N)O{" + "3}" + "P*Q(2|3)"
print('Final string: ', generateString(rule2))
print('-' * 70)

rule3 = "R*S(T|U|V)W(Z|Y|Z){" + "2}"
print('Final string: ', generateString(rule3))





