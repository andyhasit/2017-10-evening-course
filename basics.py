
a = 2
print(a)
pint(a





"""
# Python file (aka module)
# Print statement (only for learning and debugging)
# Runs in sequence and exits
# Comments & triple quotes

a = 2
b = 3
c = 5
print(a)
print(c)

# Operators + - * > ==

print(c + a)

d = c + a
print(d)
print(d == 9)
print(d == a + b)

# Brackets

print(d == a + b - 8 * 2)

# Errors - syntax vs import vs non syntax
# Explain compile vs run

pint(a)
NameError, SyntaxError

# if else elif

if d == 9:
    print("yes")
print("next")

if d > 10:
    print("big")
    if d > 100:
        print("really big")
    elif d > 50:
        print("quite big")
else:
    print("small")
print("next")

# indentation rules, tabs vs spaces

# while loops

x = 0
while x < 5:
    print(x)
    x = x + 1

x = 0
while True:
    print(x)
    x = x + 1
    if x > 5:
        break

while x < 5:
    x = x + 1
    if x % 2 == 0:
        print(x)
    
while x < 5:
    x = x + 1
    if x % 2 == 0:
        continue
    print(x)

# For loops
numbers = [3, 5, 6, 4, 2, -2, 6, 3]

for i in numbers:
    print(i)

# Don't confuse with 'in' operator

4 in numbers

# Functions

max, min, abs

# Types

int(), str(), type()

immutable: string, int, bool, float, double, tuple
mutable: list, dict

divmod
len
range
all
any



"""