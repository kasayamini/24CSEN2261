name = "Alice"
age = 25

print("Hello, " + name + "! You are " + str(age) + " years old.")

if age >= 18:
    print(name + " is an adult.")
else:
    print(name + " is a minor.")

for i in range(1, 6):
    print(i)

while age > 0:
    print(age)
    age -= 1  # Decrease age by 1 each time

def greet(person):
    print("Hi, " + person + "!")

greet(name)
