# # Day 14
# ######################### Project: Higher Lower

# ## Tasks to do

# # import from art
# # import Random
# # import from game_data
# import random
# from art import logo, vs
# from game_data import data
# from replit import clear

# def play():
#   # # function to generate A, B from data dictionary
#   def random_generator():
#     person = random.choice(data)
#     return person

#   A = random_generator()
#   B = random_generator()
#   #print logo 'Higher'
#   print(logo)
#   # Compare A: random choice (name, description, location)
#   #Condition to make sure we don't get the same person in both
#   while A == B:
#     A = random_generator()

#   print('Compare A: ' + A['name'] + ', a ' + A['description'] + ', from ' +
#         A['country'])
#   # print logo 'lower'
#   print(vs)
#   # Against B  random choice (name, description, location)
#   print('Compare B: ' + B['name'] + ', a ' + B['description'] + ', from ' +
#         B['country'])

#   A_followers = A['follower_count']
#   B_followers = B['follower_count']
#   print(f"pss, A's followers are {A_followers}")
#   print(f"pss, B's followers are {B_followers}")

#   # # Function to compare follower_count of A and B

#   correct_answer = ''

#   def compare_followers(A, B):
#     if A_followers > B_followers:
#       correct_answer = 'a'
#     elif B_followers > A_followers:
#       correct_answer = 'b'
#     elif A_followers == B_followers:
#       correct_answer = 'a' or 'b'
#     return correct_answer

#   correct_answer = compare_followers(A, B)
#   new_A = correct_answer

#   # input(Who has more followers? Type 'A' or 'B')
#   guess_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

#   # Score counter function
#   score = 0

#   # def score_count(guess_answer, correct_answer, score):
#   def score_counter(guess_answer, correct_answer, score):
#     if guess_answer == correct_answer:
#       new_score = score + 1
#       print(f"You're right! Current score: {new_score}")

#     else:
#       new_score = score
#       print(f"You're wrong! Final score: {new_score}")
#       return

#   score_counter(guess_answer, correct_answer, score)
#   while guess_answer == correct_answer:
#     play()

# play()

# # # Then B becomes A
# # # New B: random choice(name, deciption, location)

############################## Angela's code
from art import logo
from art import vs
from game_data import data
import random
from replit import clear


def format_data(account):
  """Takes the account data and returns the printable format."""
  # Format account data into printable format
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """Take the user guess and followers counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == 'a'
    #Means if it is correct, it'll return True
  else:
    return guess == 'b'
    #Means if b has more followers than 'a' and user guess was also b, then return True
  #else it'll return false


# Display code
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make game repeatable
while game_should_continue:
  # Generate random account from game data

  # Making account as position B become the next account at position A
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct
  ## Get follower count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen betweeen rounds
  clear()
  print(logo)

  # Give user feedback on their guess
  # Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score} ")
  else:
    game_should_continue = False
    print(f"Oops, that's wrong!. Final score:{score}")
