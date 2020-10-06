from random import choice

# simple hotdog a sandwich? bot
def get_bot_response(user_response):

  # list of bot responses
  bot_response_yes = ["If you say so", "A hot dog is definitely not a sandwich ", "Whats next? You're going to tell me tacos are sandwiches too?"]
  bot_response_no = ["If you say so", "A hot dog is definitely a sandwich", "Finally, someone who gets it"]
  
  # return random response from list of bot responses
  if user_response == "yes":
    return choice(bot_response_yes)
  elif user_response == "no":
    return choice(bot_response_no)
  else:
    return "You must pick a side..."





print("Welcome to the \'Is a Hot Dog a Sandwich?\' Bot")
print("There are arguments to be made for both sides")

user_response = ""
# prompt user to answer question
while True:
  user_response = input("So, is a hot dog a sandwich?: ")
  
  # break out when user types done
  if user_response == 'done':
    break

  
  bot_response = get_bot_response(user_response)
  print(bot_response)