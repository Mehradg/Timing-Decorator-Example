import time

def calc_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        timer = end - start
        return f"{result} \n{timer}"
    return wrapper

@calc_time
def show_nums(n):
    result = []
    for i in range(1,n+1):
        result.append(i)
    return (result)

number = int(input("Enter a number: "))

print(show_nums(number))