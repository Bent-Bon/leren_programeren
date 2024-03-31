line = input("Enter Input: ").split()
#print(line)

def process_input():
    if len(line) == 1 and line[0] in ['+', '-']: # unary operator
        return [float(line[0])], []
    
    operands, operators = [], []
    for token in line:
        try:
            val = float(token)
            operands.append(val)
        except ValueError:
            operators.append(token)
            
    while len(operators) > 0:
        op = operators.pop()
        
        if op == '*':
            right = operands.pop()
            left = operands.pop()
            operands.append(left * right)
        elif op == '/':
            right = operands.pop()