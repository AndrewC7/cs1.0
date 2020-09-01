# this is a simple conversion calculator. It can handle seconds/minutes/hours 

print("Welcome to my simple conversion calculator! Simply:\n")
print("1) Input the number of seconds/minutes/hours\n")
print("2) Specify seconds/minutes/hours\n")
print("3) Input your desired conversion\n")
number = input("\nNumber of seconds/minutes/hours to convert:\n")

# check to make sure user input is an int. If not, ask them to enter one
while True:
     try:
         number = float(number)
         break
     except ValueError:
         print("Error: Please enter a valid number :)")
         break

# if input is int, move on to next questions. if not, ask for a number before moving on to next questions
if(isinstance(number, float)):
    convert = input("\nValue to convert:\n")
    desired = input("\nValue desired:\n")
else:
    number = input("Number of seconds/minutes/hours to convert:\n")
    convert = input("\nValue to convert:\n")
    desired = input("\nValue desired:\n")





# the next 2 if statements handle conversions into seconds. The 1st one checks if the user input minutes and the second
# checks if the user input hours. Both convert number into a float, perform the required math, and print the result
if((desired == 'Seconds' or desired =='seconds') and (convert == 'Minutes' or convert == 'minutes')):
    number = float(number)
    result = number * 60 
    print("\nThere are", result, "seconds in", number, "minutes.\n")

if((desired == 'Seconds' or desired == 'seconds') and (convert == 'Hours' or convert == 'hours')):
    number = float(number)
    result = number * 3600
    print("\nThere are", result, "seconds in", number, "Hours.\n")



# the next 2 if statements handle conversions into minutes. The 1st one checks if the user input seconds and the second
# checks if the user input hours. Both convert number into a float, perform the required math, and print the result
if((desired == 'Minutes' or desired =='minutes') and (convert == 'Seconds' or convert == 'seconds')):
    number = float(number)
    result = number / 60 
    print("\nThere are", result, "minutes in", number, "seconds.\n")

if((desired == 'Minutes' or desired == 'minutes') and (convert == 'Hours' or convert == 'hours')):
    number = float(number)
    result = number * 60
    print("\nThere are", result, "minutes in", number, "Hours.\n")



# the next 2 if statements handle conversions into hours. The 1st one checks if the user input seconds and the second
# checks if the user input minutes. Both convert number into a float, perform the required math, and print the result
if((desired == 'Hours' or desired =='hours') and (convert == 'Seconds' or convert == 'seconds')):
    number = float(number)
    result = number / 3600 
    print("\nThere are", result, "hours in", number, "seconds.\n")

if((desired == 'Hours' or desired == 'hours') and (convert == 'Minutes' or convert == 'minutes')):
    number = float(number)
    result = number / 60
    print("\nThere are", result, "hours in", number, "minutes.\n")