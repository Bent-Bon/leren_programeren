A = int(input("(a)wat is je eerste cijfer?: "))
B = int(input("(b)wat is je tweede cijfer?: "))

if A > B:
    min_val = B
    max_val = A
    print(f"a is het grootste nummer: {max_val}")
elif A < B:
    min_val = A
    max_val = B
    print(f"a is het kleinste nummer: {min_val}")
else:
    min_val = A
    max_val = B
    print("a en b zijn even groot")
print(f"het minnimum is {min_val}")
print(f"het maximum is {max_val}")