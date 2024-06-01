import random as rand
import os
import time
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
time.sleep(1)
alive=True
skip=int(input("Enter the rounds to skip : "))
skips=["Clk.","Clik ..","Click..","Clicck ....","Clikkk......."]
skip=skip%6
bullet=rand.randrange(0,6)
for i in range(skip):
    print(skips[5-skip+i])
    time.sleep(1)

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

