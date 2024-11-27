import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_1=[rock,paper,scissors]
print("what do you choose? Type 0 for rock,1 for paper or 2 for scissor")
user_choice=int(input())
print(list_1[user_choice])

print("computer choose:")
computer_choice=random.randint(0,2)
print(list_1[computer_choice])
if user_choice==0 and computer_choice==1:
    print("you loose!")
elif user_choice==1 and computer_choice==0:
    print("you win!")
elif user_choice==1 and computer_choice==2:
    print("you loose!")
elif user_choice==2 and computer_choice==1:
    print("you win!")
elif user_choice==0 and computer_choice==2:
    print("you win!")
elif user_choice==2 and computer_choice==0:
    print("you loose!")
elif user_choice==computer_choice:
    print("it's a draw")




