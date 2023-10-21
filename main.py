import random

input_string  = "begin I := 1 ; R := 3 ; while X > I do begin R := R * 3 ; I := I + 1 ; end end"

#region SemanticTerm

def parse_string(input_string: str):
    words = input_string.split()

    for i in range(0, len(words)):
        if words[i] == ";":
            words[i] = " dot "
        elif words[i] == "begin":
            words[i] = ""
        elif words[i] == "end":
            words[i] = ")"

    words = parse_OP(words)

    words = parse_AS(words)

    words = parse_IF(words)

    words = parse_WH(words)

    words.pop()
    words.pop(0)
    if words[-2] == " dot ":
        words.pop(-2)
    return "".join(words)

def parse_IF(words: list) -> list:
    for i in range(0, len(words) - 4):
        if words[i] == "if":
            words[i] = "IF("
            words.pop(i+2)
            words.pop(i+4)
            # words.insert(i+4, ")")
            return parse_IF(words)
    return words

def parse_WH(words: list) -> list:
    for i in range(0, len(words) - 3):
        if words[i] == "while":
            words[i] = "WH("
            words.pop(i+2)
            words.insert(i+2, ", ")
            return parse_WH(words)
    return words

def parse_AS(words) -> list:
    for i in range(1, len(words) - 1):
        if words[i] == ":=":
            words[i] = "AS_" + words[i-1] + f"({words[i+1]})"
            words.pop(i+1)
            words.pop(i-1)
            return parse_AS(words)
    return words

def parse_OP(words) -> list:
    for i in range(1, len(words) - 1):
        if words[i] == ">":
            words[i] = "S2(gr, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
        elif words[i] == "=":
            words[i] = "S2(eq, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
        elif words[i] == "or": #I don't have a correct symbol
            words[i] = "S2(or, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
        elif words[i] == "*":
            words[i] = "S2(mult, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
        elif words[i] == "+":
            words[i] = "S2(add, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
        elif words[i] == "-":
            words[i] = "S2(sub, " + (f"{words[i-1]}_hat," if words[i-1].isnumeric() else f"{words[i-1]} =>, ") + (f"{words[i+1]}_hat)" if words[i+1].isnumeric() else f"{words[i+1]} =>)")
            words.pop(i+1)
            words.pop(i-1)
            return parse_OP(words)
    return words
#endregion


#region TermTesting
X = 3 #Input data
I = random.randint(0, 1000) #Define variables
R = random.randint(0, 1000) #Define variables

def AS_I(num):
    print(f" AS_I -> {num} ", end=" ")
    global I
    I = num

def AS_R(num):
    print(f" AS_R -> {num} ", end=" ")
    global R
    R = num

def WH(cond, do):
    print(" WH ", end=" ")
    loop_num = 1
    while cond():
        print(f"while condition, loop number: {loop_num}", end=" ")
        loop_num += 1
        do()

def S2(op, var1, var2):
    print(f" S2({op}, {var1}, {var2}) ", end=" ")
    if (op == "gr"):
        return var1 > var2
    elif (op == "eq"):
        return var1 == var2
    elif (op == "or"):
        return var1 or var2
    elif (op == "add"):
        return var1 + var2
    elif (op == "sub"):
        return var1 - var2
    elif (op == "mult"):
        return var1 * var2

def SUPERP(do1, do2):
    do2
    do1

def func1():
    return SUPERP(AS_R(S2("mult", R, 3)), AS_I(S2("add", I, 1)))

def cond1():
    return S2("gr", X, I)

def term(input_data):
    AS_I(1)
    AS_R(3)
    WH(cond1, func1)

def exec(input_data):
    term(X)
    print(R)

exec(X)

print(parse_string(input_string))

#endregion