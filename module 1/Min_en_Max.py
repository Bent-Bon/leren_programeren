A = int(input("(a)wat is je eerste cijfer?: "))
B = int(input("(b)wat is je tweede cijfer?: "))

if A > B:
    y = min(A, B)
    x = max(A, B)
    print(f"a is het grootste nummer: {x}")
elif A < B:
    y = min(A, B)
    x = max(A, B)
    print(f"a is het kleinste nummer: {y}")
else:
    y = min(A, B)
    x = max(A, B)
    print("a en b zijn even groot")
print(f"het minnimum is {y}")
print(f"het maximum is {x}")