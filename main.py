from datetime import date

#question name
name = input(" Enter your name : ").title()

#question number age
byear = int(input(" Enter your birth year: "))
bmonth = int(input(" Enter your birth month: "))

#today variable
current_year = date.today().year
current_month = date.today().month

#classic age calcule
age = (current_year - byear)

#modify age by month
if bmonth < current_month:
    age - 1

#add month
moth_decal = current_month - bmonth
if moth_decal < -1:
    moth_decal = 0

#result
print("Hello ", name,", you have ", age, " year old and ", moth_decal, " mothn.")

# made by KodHeur 👑
# go on : https://github.com/KodHeur for more project