def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def devide(a,b):
    print(f"DEVIDING {a} / {b}")
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(91.5, 2)
iq = devide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
