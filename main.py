from datetime import date

#question name
name = input(" Enter your name : ").title()

#question number age
byear = int(input(" Enter your birth year: "))
bmonth = int(input(" Enter your birth month: "))
#bdate = int(input(" Enter your birth day: "))

#today variable
current_year = date.today().year
current_month = date.today().month

#classic age calcule
age = (current_year - byear)

#modify age by month
if bmonth > current_month:
    age + 1

#add month
if current_month > bmonth :
    moth_decal = 0
else:moth_decal = current_month - bmonth


#result
print("Hello ", name,", you have ", age, " year old and ", moth_decal, " mothn.")
