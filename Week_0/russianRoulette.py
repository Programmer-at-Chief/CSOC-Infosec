import random as rand
import os
import time

## This game class is the main functional unit of the program handling everything from the intro to the exit of the game
class Game:
    points=0;
    def __init__(self):
        pass
    def clearScreen(self):
        if (os.name == 'nt'):
            os.system("cls")
        else:
            os.system("clear")
    def intro(self):
        self.clearScreen()
        
        print("-"*40)
        # print("Russian Roulette")
        print('''
██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║
██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║
██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║
██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗
██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░
██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░
██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗
╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝''')
        print('''
█████████████████████████████████████████████████████████████████████████████████████████████
█▄─█─▄█─▄▄─█▄─██─▄███▄─▄▄▀█▄─▄█▄─▄▄─███─▄▄─█▄─▄▄▀███▄─█─▄█─▄▄─█▄─██─▄███▄─▄▄▀█▄─▄█▄─▄▄─██░█░█
██▄─▄██─██─██─██─█████─██─██─███─▄█▀███─██─██─▄─▄████▄─▄██─██─██─██─█████─██─██─███─▄█▀██▄█▄█
▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▄▀▄▀''')
        print("-"*40)

    def play(self,choice,bullet):
        print("Click...")
        time.sleep(2)
        if (choice==bullet):
            self.clearScreen()
            print('''
░█▀▀▀█ █──█ █─█ █▀▀█ 　 █▀▀▄ █── █──█ █▀▀█ ▀▀█▀▀ 　 █ █ 
─▀▀▀▄▄ █──█ █▀▄ █▄▄█ 　 █▀▀▄ █── █▄▄█ █▄▄█ ──█── 　 ▀ ▀ 
░█▄▄▄█ ─▀▀▀ ▀─▀ ▀──▀ 　 ▀▀▀─ ▀▀▀ ▄▄▄█ ▀──▀ ──▀── 　 ▄ ▄''')
            return False
        else:
            self.clearScreen()
            # print("You are safe...(Not for long )")
            print('''
█▄█ █▀█ █░█   ▄▀█ █▀█ █▀▀   █▀ ▄▀█ █▀▀ █▀▀   
░█░ █▄█ █▄█   █▀█ █▀▄ ██▄   ▄█ █▀█ █▀░ ██▄ ▄ ▄ ▄ (Not for long)''')
            self.points+=1
            return True
    def end(self):
        print("-"*40)
        print("Thanks for playing !!")
        print("-"*40)
        exit()
    def displayPoints(self):
        print(f"\nYour points are {self.points}\n")


game=Game()
game.intro()
print("Enter \n1 -> To play the game \n0 -> To exit")
choice=-1

# the choice is taken as input with error handling to have smooth functioning
while(choice not in [0,1]):
    try: 
        choice=int(input("Enter your choice : "))
    except:
        print("Invalid number")

if (not choice):
    game.displayPoints()
    game.end()
game.clearScreen()
time.sleep(1)
print("\nThe gun is handed to you ... ")
time.sleep(1)
print()
# Time command is used in many places to make the games move forward in a timely manner providing it a bit real feel
time.sleep(1)
alive=True
skip=int(input("Enter the rounds to skip : "))
skips=["Clk.","Clik ..","Click..","Clicck ....","Clikkk......."]
skip=skip%6
# A random bullet is classified as deadly using the randrange function
bullet=rand.randrange(0,6)
for i in range(skip):
    print(skips[5-skip+i])
    time.sleep(1)

# An infinite while loop makes sure the game can be played endlessly
while(choice & alive):
    if (game.points==0):
        pull=input("\nEnter pull to pull the trigger (-1 to cancel) : ")
    else:
        pull=input("\nYou are tough ehh. Wanna try again (pull/-1 to cancel) : ")
    while (pull!="pull"):
        if (pull=="-1"):
            game.displayPoints()
            game.end()
        print("Do it, bro.")
        pull=input("Enter pull to pull the trigger (-1 to cancel) : ")
    alive=game.play(skip,bullet)
    if (not alive):
        game.displayPoints()
        game.end()
    skip=(skip+1)%6

