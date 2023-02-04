def geometric_progression(num, end_num):
    i = 1
    while i < end_num:
        try:
            yield i
            i *= num
        except Exception as err:
            print(err)
            return

def my_range(start,stop,step = 1):
    if step > 0:
        while start < stop:
            yield start
            start += step
        return
    if step < 0:
        while stop < start:
            yield start
            start += step
        return


def prime_numbers(end):
    for num in range(1,end):
        for i in range(2,num):
            if not num % i:
                break
        else:
            yield num


print([i ** 3 for i in range(2,20)])



