# 1. Seconds to Hours, Minutes, Seconds
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# 2. Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 2)


# 3. Split Evenly
def split_evenly(total, people):
    each = total // people
    remainder = total % people

    return each, remainder


# 4. Initials
def initials(full_name):
    words = full_name.split()

    result = ""
    i = 0

    while i < len(words):
        result += words[i][0]
        i += 1

    return result.upper()


# 5. Palindrome
def is_palindrome_word(word):
    word = word.strip().lower()

    return word == word[::-1]


# 6. Mask Email
def mask_email(email):
    at = email.index("@")

    name = email[:at]
    domain = email[at:]

    if len(name) <= 1:
        return "*" + domain

    return name[0] + "*" * (len(name) - 1) + domain


# 7. Middle
def middle(values):
    length = len(values)

    if length % 2 == 1:
        return values[length // 2]

    return values[length // 2 - 1:length // 2 + 1]


# 8. Rotate Left
def rotate_left(values, k):
    if len(values) == 0:
        return []

    k = k % len(values)

    return values[k:] + values[:k]


# 9. Fibonacci
def fib_list(n):
    result = []

    a = 0
    b = 1
    i = 0

    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1

    return result


# 10. Collatz
def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps


# =========================
# User Input
# =========================

print("===== Python Lab 01 =====")


# 1
seconds = int(input("Enter seconds: "))
print("Time:", seconds_to_hms(seconds))


# 2
celsius = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(celsius))


# 3
total = int(input("Enter total: "))
people = int(input("Enter number of people: "))

each, remainder = split_evenly(total, people)

print("Each person gets:", each)
print("Remainder:", remainder)


# 4
full_name = input("Enter your full name: ")
print("Initials:", initials(full_name))


# 5
word = input("Enter a word: ")
print("Palindrome:", is_palindrome_word(word))


# 6
email = input("Enter your email: ")
print("Masked email:", mask_email(email))


# 7
values = input("Enter numbers separated by spaces: ").split()

numbers = []
i = 0

while i < len(values):
    numbers.append(int(values[i]))
    i += 1

print("Middle:", middle(numbers))


# 8
values = input("Enter numbers separated by spaces: ").split()

numbers = []
i = 0

while i < len(values):
    numbers.append(int(values[i]))
    i += 1

k = int(input("Enter rotation amount: "))

print("Rotated list:", rotate_left(numbers, k))


# 9
n = int(input("Enter n for Fibonacci: "))
print("Fibonacci:", fib_list(n))


# 10
n = int(input("Enter number for Collatz: "))
print("Collatz steps:", collatz_steps(n))
