import calculator
value=0.0

op=input("What operation would you like, +,-,*,/,memory_store,memory_return,memory_clear,invert,power,exit:")

num_1=float(input("Enter your first number: "))
num_2=input("Enter your second number (leave blank for 'invert' or 'ms'): ")

if op== '+':
    value=calculator.add(float(num_1), float(num_2))
    print(num_1, "+", num_2, "=", value)
elif op== '-':
    value=calculator.sub(float(num_1), float(num_2))
    print(num_1, "-", num_2, "=", value)
elif op== '*':
    value=calculator.multi(float(num_1), float(num_2))
    print(num_1, "*", num_2, "=", value)
elif op== '/':
    value=calculator.divide(float(num_1), float(num_2))
    print(num_1, "/", num_2, "=", value)

elif op== 'memory_store':
    calculator.memory_store(value)

elif op== 'memory_return':
    value=calculator.memory_return()
    print=(value)

elif op== 'memory_clear':
     calculator.memory_clear

elif op=='invert':
    value=calculator.invert(num_1)
    print(value)

elif op=='power':
    value=calculator.power(float(num_1),float(num_2))
    print(value)






















