import turtle
import os
if (os.name == 'nt'):
    os.system("cls")
else:
    os.system("clear")

print("#"*40)

print("_______Welcome to PC Logo_______ ")

print("#"*40)

# print("We")
john=turtle.Turtle()
screen=turtle.Screen()

john.shape("turtle")
john.speed(10)

john.pensize(10)
help="Available commands are : fd,rt,lt,bk,color,dot,undo,circle\n Example: fd 40, rt 120, circle"
print("Type help to list all available commands")
print("Enter commands (input quit to end ) : \n");
colors=["white","brown","black","violet","green","blue","pink"]
cmd_list=[]
choice=input("").strip()
while(choice!="quit"):
    if (choice=="help"):
        print(help)
    elif (choice[0:2]=="fd"):
        john.forward(float(choice[3::]))
    elif (choice[0:2]=="rt"):
        john.rt(float(choice[3::]))
    elif (choice[0:2]=="lt"):
        john.lt(float(choice[3::]))
    elif (choice[0:2]=="bk"):
        john.backward(float(choice[3::]))
    elif (choice=="color"):
        for i in range(0,len(colors)):
            print("Enter : ")
            print(i," -> ",colors[i])
        color_choice=int(input("Enter a number : "))
        # try:
        john.color(colors[color_choice])
        # except:
            # print("Enter a number among the ones provided")
        
    elif (choice=="dot"):
        pensize=float(input(f"Enter the pensize(Default : {max(john.pensize()+5,2*john.pensize())}) : ") or max(john.pensize()+5,2*john.pensize()))
        color=input(f"Enter the color: (Default : {john.pencolor()})") or john.pencolor()
        john.dot(pensize,color)
    elif (choice=="undo"):
        john.undo()
    elif (choice=="circle"):
        radius=float(input("Enter radius : "))
        john.circle(radius)

    choice=input("").strip()

exit()
# screen.exitonclick()


