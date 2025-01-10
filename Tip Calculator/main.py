#Tip Calculator



#to import our logo to our .py file we are using this method
from art import logo



#to show our logo and text
print(logo)
print("Welcome to the tip calculator.\n")



#we are using this to take input so we are gonna take information from user
#we should use int before input because input's default data type is str but we are gonna make operation with numbers
total_bill=int(input("what was the total bill? $"))
percent_of_bill=int(input("how much tip would you like to give? %10,%12,%15 ? %"))
number_of_people=int(input("how many people to split the bill? "))
 


#for determine conditions
if percent_of_bill==10:
    price=total_bill+(percent_of_bill*1.10)    # %10= x*1.10   
elif percent_of_bill==12:
    price=total_bill+(percent_of_bill*1.12)    # %12= x*1.12
elif percent_of_bill==15:
    price=total_bill+(percent_of_bill*1.15)    # %15= x*1.15



# we used this formule to find how much money each person will pay
#if you wanna see float numbers you can change int to float
each_person_gotta_pay=int(price/number_of_people)


#to show final output 
print(f"each person gotta pay: {each_person_gotta_pay}$")
 
