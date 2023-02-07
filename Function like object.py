# 1
def numbering_progression(start, amount):
    def operating(oper, n):
        nonlocal start
        if oper == "+":
            start += n
        if oper == "-":
            start -= n
        if oper == "*":
            start *= n
        if oper == "//":
            start //= n
        return start

    for i in range(amount):
        yield operating

# 2
def my_function():
    my_lis = [0,1]
    def fibonacci(n):
        if n <= len(my_lis):
            return my_lis[n - 1]
        else:
            curr = my_lis[-1] + my_lis[-2]
            my_lis.append(curr)
            if n >= len(my_lis):
                return fibonacci(n)
            else:
                return my_lis[n - 1]
    return fibonacci


def fibonacci_2(n, prev = 0, curr = 1):
    if n > 0:
        return fibonacci_2(prev = curr, curr = prev + curr, n = n - 1)
    else:
        return curr


# 3
def summa_elements(lis,func):
    return sum(func(lis))


def sort_element(lis):
    for el in lis:
        if el % 2 and el != 5:
            continue
        else:
            lis.remove(el)
    return lis

