x = float(input('first number: '))
y = float(input('Second number: '))
operation = input('Operation: ')

result =  None

if opreration == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Unsupported operation')

if result is not None:
    print('Result:', result)