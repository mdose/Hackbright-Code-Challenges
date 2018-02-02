# Complete the function below.

def eval(exp):
    """
    Look for operators '*' or '/' first, Take int before and after these operators, Calucate result, Save result.
    Do again for '+' or '-'. Save final result and return.
    """

    parsed = parse(exp)

    while len(parsed) > 1:
        if "*" in parsed:
            i = parsed.index("*")
            l = i - 1
            r = i + 1
            result = parsed[l] * parsed[r]
            parsed[l:r+1] = [result]

        if "/" in parsed:
            i = parsed.index("/")
            l = i - 1
            r = i + 1
            result = parsed[l] / parsed[r]
            parsed[l:r+1] = [result]

        if "+" in parsed:
            i = parsed.index("+")
            l = i - 1
            r = i + 1
            result = parsed[l] + parsed[r]
            parsed[l:r+1] = [result]

        if "-" in parsed:
            i = parsed.index("-")
            l = i - 1
            r = i + 1
            result = parsed[l] - parsed[r]
            parsed[l:r+1] = [result]

    return parsed[0]

def parse(exp):
    lst = exp.split(" ")
    return [int(x) if x.lstrip("-").isdigit() else x for x in lst]
