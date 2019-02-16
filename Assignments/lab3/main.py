import calculator
value=0.0

op=input("What operation would you like, +,-,*,/,ms,mr,mc,invert,power:")

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

elif op== 'ms':
    calculator.ms(value)

elif op== 'mr':
    value=calculator.mr()
    print=(value)

elif op== 'mc':

    calculator.mc

elif op=='invert':
    value=calculator.invert(num_1)
    print(value)

elif op=='power':
    value=calculator.power(float(num_1),float(num_2))
    print(value)

















