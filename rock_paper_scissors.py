import random
Player_Score = 0
Computer_Score = 0
ties = 0
Win_Target = 3

print("Welcome to rock paper scissors")
print("First to 3 wins")
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    player = input("\nrock, paper, or scissors? ").lower().strip()
    if player not in choices:
        print("Choose rock, paper, or scissors only!")
        continue

    print(f"Computer chose: {computer}")

    if player == computer:
        ties += 1
    
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        Player_Score += 1
    else:
        print("You lose...")
        Computer_Score += 1

    print(f"\nSCORE - You: {Player_Score} - {Computer_Score} - computer ties = {ties}")

    if Player_Score == Win_Target:
        print("You Win!")
        break
    elif Computer_Score == Win_Target:
        print("Game over")
        break

    
    
