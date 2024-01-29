import random
import os
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0 #0 will be blackjack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose \n"


  if user_score == computer_score:
    return "DRAW \n"
  elif computer_score == 0:
    return "LOSE, opponent has Blackjack \n"
  elif user_score == 0:
    return "BLACKJACK!! \n"
  elif user_score > 21:
    return "You bust. YOU LOSE! \n"
  elif computer_score > 21:
    return "Opponent bust. YOU WIN! \n"
  elif user_score > computer_score:
    return "YOU WIN! \n"
  else:
    return "YOU LOSE! \n"


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to hit, type 'n' to stand: \n")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("")
  print(f"   Your final hand: {user_cards}, final score: {user_score}\n")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}\n")
  print(compare(user_score, computer_score))


def clear():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()