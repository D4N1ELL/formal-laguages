# Topic: Regular expressions

### Course: Formal Languages & Finite Automata
### Author: Istrati Daniel

----
## Theory

&ensp;&ensp;&ensp; Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized 
programming language embedded inside Python and made available through the re module. Using this little language, you specify 
the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, 
or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a 
match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.

&ensp;&ensp;&ensp; Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C. 
For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a 
certain way in order to produce bytecode that runs faster.

&ensp;&ensp;&ensp; The regular expression language is relatively small and restricted, so not all possible string processing tasks can be done 
using regular expressions. There are also tasks that can be done with regular expressions, but the expressions turn out to 
be very complicated. In these cases, you may be better off writing Python code to do the processing; while Python code will 
be slower than an elaborate regular expression, it will also probably be more understandable.


----
## Objectives:


1. Write and cover what regular expressions are, what they are used for;

2. Below you will find 3 complex regular expressions per each variant. Take a variant depending on your number in the list of students and do the following:

    a. Write a code that will generate valid combinations of symbols conform given regular expressions (examples will be shown).

    b. In case you have an example, where symbol may be written undefined number of times, take a limit of 5 times (to evade generation of extremely long combinations);

    c. **Bonus point**: write a function that will show sequence of processing regular expression (like, what you do first, second and so on)

## Variant 4:

![Variant 4](/variant_4_task.png)

Examples of what must be generated:

{SUWWY24, SVWY24, ...}
{LMOOOPPPQ2, LNOOOPQ3, ...}
{RSTWXX, RRRSUWYY, ...}

----
## Code
The implementtation consists of a function which takes the given rule and travers it symbol by symbol and checking if it is a special one or no. In this function are covered some base cases, like 1 or more occurrences or a fixed number. Also in each case is printed the step, like how the string which is generated is modified.

Some examples of covered cases in code are:

1 or more occurrences from options
```
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "+":
            times = random.randint(1, 5)
            for _ in range(times):
                char =  choice(options(rule[i + 1:rule.index(")", i)]))
                string +=  char
                print(f"One or more occurrences from options: Adding {char} to string => {string}")
            i = rule.index(")", i) + 1
```

Fixed occurrences from options

```
        elif rule[i] == "(" and rule[rule.index(")", i) + 1] == "{":
            for _ in range(int(rule[rule.index("{", i) + 1])):
                char = choice(options(rule[i+1:rule.index(")", i)]))
                string += char
                print(f"Fixed occurrences from options: Adding {char} to string => {string}")
            i = rule.index("}", i) + 1
```

Similarly works for other cases such as 0 or more occurrences, 0 or 1 occurrence or just one.


----
## Results:

```commandline
Just one occurrence from options: Adding S to string => S
Just one occurrence from options: Adding U to string => SU
Adding W to string => SUW
Adding Y to string => SUWY
Adding 2 to string => SUWY2
Adding U to string => SUWY2U
Final string:  SUWY2U
----------------------------------------------------------------------
Adding L to string => L
Just one occurrence from options: Adding M to string => LM
Adding O to string => LMO
Adding 3 to string => LMO3
Adding P to string => LMO3P
Adding Q to string => LMO3PQ
Just one occurrence from options: Adding 2 to string => LMO3PQ2
Final string:  LMO3PQ2
----------------------------------------------------------------------
Adding R to string => R
Adding S to string => RS
Just one occurrence from options: Adding V to string => RSV
Adding W to string => RSVW
Fixed occurrences from options: Adding Y to string => RSVWY
Fixed occurrences from options: Adding Z to string => RSVWYZ
Final string:  RSVWYZ

```

----
## Conclusions

In conclusion, this lab demonstrates a practical approach to understanding and implementing basic elements of regular expressions through Python code. By defining rules and applying logic for generating strings based on those rules, it provides insight into how regular expressions can be utilized for text generation and manipulation tasks.

While this implementation provides a simplified version of regular expression functionality, it offers a hands-on way to comprehend the concepts behind regular expressions and their practical applications in text processing and manipulation. Further enhancements could include expanding the functionality to cover more complex regular expression features and optimizing the code for efficiency and readability.



