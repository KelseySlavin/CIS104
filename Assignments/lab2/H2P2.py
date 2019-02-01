book_title = input("What is the title of the book?: ")
book_author = input ("Who is the author of the book?: ")
publish_year= int(input("What is the publish year of the book?: "))
book_pages = int(input("How many pages are in the book?: "))
CURRENT_YEAR = 2019
book_age = (CURRENT_YEAR-publish_year)
print ("Your book is " + str(book_age)+" years old.")
if(book_age<10):
    print ("This book is younger than 10 years old.")
else: 
    print("This book is at least 10 years old.")
if(int(book_pages)<100):
    print ("This book is a short book.")
elif(float(book_pages)<=300):
    print("This book is an average book.")
else:
    print("This book is a long book.")


