pennies= int(input("How many pennies do you have?:"))
value=pennies*.01
print("You have "+ str(pennies) + " pennies.")
nickels= int(input("How many nickels do you have?:"))
value=nickels*.05+value
print("You have "+str(nickels) + " nickels.")
dimes= int(input("How many dimes do you have?:"))
value=dimes*.10+value
print("You have "+str(dimes)+ " dimes.")
quarters=int(input("How many dimes do you have?:"))
value=quarters*0.25+value
print("You have "+str(quarters)+ " quarters.")
half_dollars=int(input("How many half dollars do you have?:"))
value=half_dollars*0.50+value
print("You have "+str(half_dollars)+" half dollars.")
dollars=int(input("How many dollars do you have?:"))
value=dollars*1.00+value
print("You have "+str(dollars)+" dollars.")

print("the value of your coins is " +str(value))
