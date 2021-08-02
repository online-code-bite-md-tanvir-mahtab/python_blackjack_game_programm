import random
from art import logo
from replit import clear


def deal_card(cards):
  # nwo i am going to find the the 11 in the list and delete and add 1
  if 11 in cards:
    cards.remove(11)
    cards.append(1)
  return cards
  pass
def result_of_game(user_score,computer_score):
    if user_score ==0 or computer_score ==0:
        return "Win with black jack"
    elif user_score == computer_score:
        return "Draw"
    elif user_score > computer_score:
        return "You win 😎"
    elif computer_score > user_score:
        return "You lose"


choose = True
while choose:
  choose = input("Do you want to play the blackjack? Type 'y' or 'n':").lower()
  if choose == "y":
    clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # creating new list for the user
    deal_card(cards)
    user_list = []
    computer_list = []
    # print(len(cards))
    # creating two new variable that will hold the value of the random number
    number1 =0
    computer_number = 0
    for _ in range(2):
      number1 = random.randint(1,len(cards)-1)
      user_list.append(number1)
    for _ in range(2):
      computer_number = random.randint(1,len(cards)-1)
      computer_list.append(computer_number)
    # to store the total score of the player and the computer we are creating two variable
    user_score = 0
    computer_score = 0
    # for the user array list
    for score in user_list:
      user_score += score
    # for the computer array list
    for score in computer_list:
      computer_score += score
    # print(computer_list)
    print(f"Your card's: {user_list}, current score    {user_score}")
    print(f"delar first card's {computer_list[0]}")

    '''now i am going to check if the user_score and computer_score is less then 17 then we are going to ask the user to input for to take another card or not'''
    want_cards = False
    if user_score < 17:
      while  input("Type 'y' to add another cards , Type 'n' to pass the game : ").lower() == "y":
        user_list.append(number1)
        user_score += number1
        print(f"Your final hand :{user_list}, final score: {user_score}")
        print(f"computer final hand :{computer_list}, final score: {computer_score}")

      print(f"Your final hand :{user_list}, final score: {user_score}")
      print(f"computer final hand :{computer_list}, final score: {computer_score}")
    elif computer_score<17:
      computer_list.append(computer_number)
      print(f"Your final hand :{user_list}, final score: {user_score}")
      print(f"computer final hand :{computer_list}, final score: {computer_score}")  
      
    result = result_of_game(user_score,computer_score)
    print(result)
  elif choose == "n":
    choose = False
    clear()