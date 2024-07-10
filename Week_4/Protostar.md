# Protostar

### Stack0

Given challenge has a unsafe practise gets() which should not be used, as it stores input outside the length of the buffer. So, instead to inputing the required 64 characters, I input 65 characters and the buffer overflow changes the variable value.

Script: [Stack0.py](Scripts/Stack0.py)

![](/home/aman/.config/marktext/images/2024-07-06-13-26-41-image.png)



### Stack 1

Given program expects a 64 length buffer input, the extra program input goes to modified. Also, modified is supposed to be equal to 0x61626364 which is in little endian , so the string must have dcba at the end. 

key: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdcba

![](/home/aman/.config/marktext/images/2024-07-06-17-03-36-image.png)



### Stack 2

In this , again a 64 size buffer input is read from an environment variable GREENIE and the rest goes to modified via buffer overflow. Also , modified is compared with 0x0d0a0d0a in little endian form. So the environment variable must be a 64 size string appended by newline and carriage return characters which are ascii values of 0a and 0d characters respectively.

Script: [Stack2.py](Scripts/Stack2.py)

![](/home/aman/.config/marktext/images/2024-07-06-17-33-07-image.png)

### Stack 3

In this program, the win function is declared but not called in the main function. So we have to find a way to call it from within the program.We can do so in gdb , I have set a breakpoint before the end of the main and in that time find out the location of win function and jump to it.

![](/home/aman/.config/marktext/images/2024-07-07-00-46-14-image.png)

### Stack 4

Just like in stack 3 , I set a breakpoint at the gets statement and jumped to win function from within gdb.

![](/home/aman/.config/marktext/images/2024-07-07-00-49-26-image.png)

![](/home/aman/.config/marktext/images/2024-07-07-00-49-48-image.png)

### Stack 5




