# #Even Odd

num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Even")

else:
    print("Odd")


#Prime Number

n = int(input("Enter n: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")


#Vowel in a String

string = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


#Merge two dictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]

print(result)


#Student record to a file

# Taking input
name = input("Enter name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

# Writing to file
with open("students.txt", "a") as file:
    file.write(f"{name}, {roll}, {marks}\n")

print("Record saved successfully.")


#Grade Students

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
elif marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"

print("Grade:", grade)


#Area of a Cirle

def f(x):
    return x**2   # Example function

def area(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2

    for i in range(1, n):
        result += f(a + i * h)

    return result * h

# Example usage
a = 0
b = 2
n = 1000

print("Area:", area(a, b, n))