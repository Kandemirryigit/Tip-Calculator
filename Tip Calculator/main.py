#Tip Calculator

from art import logo  #To import our logo to our .py file we are using this method

#to show our logo and text
print(logo)
print("Welcome to the tip calculator.\n")

#we are using this to take input so we are gonna take information from user
#we should use int before input because input's default data type is str but we are gonna make operation with numbers
total_bill=int(input("How much total bill? $"))
total_tip=int(input("how much tip do you wanna give? $"))
number_of_people=int(input("how many people to split the bill? "))
 
total_price=total_bill+total_tip  #I used this formul to find total price


#I used this formul to find how much money each person will pay
#If you wanna see float numbers you can change int to float
each_person_gotta_pay=int(total_price/number_of_people)


#to show final output 
print(f"each person gotta pay: {each_person_gotta_pay}$")
 
