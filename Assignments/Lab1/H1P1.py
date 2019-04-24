first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your age?: "))
confidence=int(input("How confident are you in programming between 1-100%? "))
dog_age= age * 7
print("hello, " + first_name+ " " + last_name + " , nice to meet you! You might be " + str(age) + " in human years, but in dog year you are " +str(dog_age)+"." )
if confidence < 50: 
    print("I agree, programmers can't be trusted!") 
else:
    print("Writing good code takes hard work!")


