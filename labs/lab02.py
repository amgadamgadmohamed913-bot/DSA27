
import math



def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("not a valid triangle")
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"



def course_result(coursework, final, attendance):
    for v in (coursework, final, attendance):
        if not 0 <= v <= 100:
            raise ValueError("values must be between 0 and 100")
    if attendance < 75:
        return "Fail"
    if final < 40:
        return "Fail"
    total = coursework * 0.4 + final * 0.6
    if total >= 85:
        return "Distinction"
    elif total >= 50:
        return "Pass"
    else:
        return "Fail"



def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True



def primes_below(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result



def first_repeated(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return values[i]
    return None



def count_pairs(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2


def count_pairs_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count



def calculator(command):
    match command:
        case ["add", a, b]:
            return a + b
        case ["sub", a, b]:
            return a - b
        case ["mul", a, b]:
            return a * b
        case ["div", a, b]:
            if b == 0:
                raise ValueError("division by zero")
            return a / b
        case ["neg", a]:
            return -a
        case ["sum", *nums]:
            return sum(nums)
        case _:
            raise ValueError(f"unknown command: {command}")



def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default



def stats(*numbers):
    if not numbers:
        raise ValueError("stats() needs at least one number")
    lo = hi = numbers[0]
    for x in numbers[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi



def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target



def make_multiplier(k):
    def multiply(x):
        return x * k
    return multiply



def apply_n(f, x, n):
    for _ in range(n):
        x = f(x)
    return x


def main():
    while True:
        print("\n1 triangle  2 course  3 fizzbuzz  4 is_prime  5 primes_below")
        print("6 first_repeated  7 count_pairs  8 calculator  9 parse_int")
        print("10 stats  11 append_to  12 multiplier  13 apply_n  0 exit")
        choice = parse_int(input("Choose: "))

        if choice == 0:
            break
        elif choice == 1:
            a, b, c = (float(input(f"Side {n}: ")) for n in "abc")
            try:
                print(classify_triangle(a, b, c))
            except ValueError as e:
                print("Error:", e)
        elif choice == 2:
            cw = float(input("Coursework: "))
            fin = float(input("Final: "))
            att = float(input("Attendance %: "))
            try:
                print(course_result(cw, fin, att))
            except ValueError as e:
                print("Error:", e)
        elif choice == 3:
            print(fizzbuzz(int(input("n: "))))
        elif choice == 4:
            print(is_prime(int(input("n: "))))
        elif choice == 5:
            print(primes_below(int(input("n: "))))
        elif choice == 6:
            print(first_repeated(input("Values (spaces): ").split()))
        elif choice == 7:
            n = int(input("n: "))
            print(count_pairs(n), count_pairs_loop(n))
        elif choice == 8:
            parts = input("e.g. add 2 3: ").split()
            cmd = [parts[0]] + [float(p) for p in parts[1:]]
            try:
                print(calculator(cmd))
            except ValueError as e:
                print("Error:", e)
        elif choice == 9:
            print(parse_int(input("Text: "), default="not a number"))
        elif choice == 10:
            nums = [float(x) for x in input("Numbers (spaces): ").split()]
            try:
                print(stats(*nums))
            except ValueError as e:
                print("Error:", e)
        elif choice == 11:
            lst = []
            while True:
                item = input("Item (empty to stop): ")
                if item == "":
                    break
                lst = append_to(item, lst)
                print(lst)
        elif choice == 12:
            k = float(input("k: "))
            x = float(input("x: "))
            print(make_multiplier(k)(x))
        elif choice == 13:
            x = float(input("x: "))
            n = int(input("n: "))
            print(apply_n(lambda v: v * 2, x, n))
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
