# Savefile Manipulation

## Supertuxkart

This is an open source remake of mario kart. By default only some of the levels and carts are open. It is a pc game.

![](/home/aman/.config/marktext/images/2024-06-25-13-13-47-image.png)

![](/home/aman/.config/marktext/images/2024-06-25-13-14-18-image.png)

The savefile is an xml document located at ~/.config/supertuxkart/config-0.10/config.xml   ![](/home/aman/.config/marktext/images/2024-06-25-13-14-55-image.png)

On changing the value from 0 to 2. All levels and carts can be opened.

![](/home/aman/.config/marktext/images/2024-06-25-13-17-04-image.png)

![](/home/aman/.config/marktext/images/2024-06-25-13-17-30-image.png)

As you can see, now all the tracks and carts are unlocked.

## Shattered Pixel Dungeon

This is a rouge like game available on android , windows and linux.

![](Savefile%20Manipulation/2024-07-02-14-19-46-image.png)

This is the beginning of how the game starts, the player has to discover more doors and passage-ways to expand the map .

![](Savefile%20Manipulation/2024-07-02-14-22-55-image.png)

This the game after some playing, the save file for the game is located at 

`$HOME/.local/share/.shatteredpixel/shattered-pixel-dungeon/game1/game.dat`  

, the file game.dat is actually a gzip compressed file which

on decompressing provides a json text file which has all the player configurations.

![](Savefile%20Manipulation/2024-07-02-14-27-43-image.png)

After modifying the file and compressing it and then renaming it to game.dat , I was able to amp up my player.

![](Savefile%20Manipulation/2024-07-02-15-53-42-image.png)

As you can see I upgrade my weapon ,health , experience and many more using the savefile.


