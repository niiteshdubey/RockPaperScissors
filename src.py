import random
#get input from user
def userAction():
    user_input=input("enter a choice (rock), (paper), (scissors): ")
    user_action=user_input.lower()
    return user_action
#get action from computer
def computerAction():
    choices=['rock','paper','scissors']
    computer_action=random.choice(choices)
    return computer_action
#determining winnner
def winner(user_action,computer_action):
    if user_action==computer_action:
        print(f"Both players chose {user_action}. It's a tie.")
    elif user_action=='rock':
        if computer_action=='paper':
            print('Paper covers rock. You lose!')
        else:
            print('Rock smashes scissors. You win!')
    elif user_action=='paper':
        if computer_action=="rock":
            print("Paper covers rock. You win!")
        else:
            print("Scissors cuts paper. You lose!")
    elif user_action=='scissors':
        if computer_action=='rock':
            print("Rock smashes scissors. You lose!")
        else:
            print("Scissors cuts paper. You win!")
def main():
    while True:
        user_action=userAction()
        computer_action=computerAction()
        winner(user_action, computer_action)
        play_again=input('Play again? (y/n): ')
        if play_again.lower()=='n':
            break
if __name__=="__main__":
    main()
    