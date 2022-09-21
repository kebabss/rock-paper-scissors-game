human_turn = "paper"
computer_turn = "rock"

if human_turn == computer_turn:
    print("Oops, draw!")
if human_turn == "rock" and computer_turn == "scissors":
    print("Human wins! L computer.")
if human_turn == "scissors" and computer_turn == "paper":
    print("Human wins! L computer.")
if human_turn == "paper" and computer_turn == "rock":
    print("Human wins! L computer.")
else: 
    print("Computer wins! L human.")
