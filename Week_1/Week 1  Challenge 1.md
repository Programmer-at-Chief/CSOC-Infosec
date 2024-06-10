**

Week 1: 

Challenge 1:

1. Information

First , I opened the file through neovim(text editor) and found out that the jpeg header has been modified with photoshop .

![](Week%201%20%20Challenge%201/2024-06-10-22-51-55-image.png)



The rdf:resource contains some sort of encoded strings . I copied it passed it through base64 decoder .

![](Week%201%20%20Challenge%201/2024-06-10-22-52-16-image.png)

The flag is unfolded.

2. Matryoshka doll

Matryoshka dolls contain smaller size dolls inside themselves, this idea could be extended to the image hiding some important files inside. Also as one such challenge was part of Freshers CTF , I remembered the tool used, binwalk.

So , I used binwalk to check for hidden files .

![](Week%201%20%20Challenge%201/2024-06-10-22-52-41-image.png) 

There was another image and a zip file inside.

The zip file contains the same image as inside, the image upon analysing with binwalk showed further hidden files inside.

![](Week%201%20%20Challenge%201/2024-06-10-22-53-37-image.png)



Another image inside with more hidden files.

![](Week%201%20%20Challenge%201/2024-06-10-22-53-56-image.png)

Another image found inside which upon binwalking showed a file flag.txt.

![](Week%201%20%20Challenge%201/2024-06-10-22-54-17-image.png)

![](Week%201%20%20Challenge%201/2024-06-10-22-54-38-image.png)

Flag.txt contains the required flag.

3. tunn3l v1s10n

First I used the file command to display the type of file which showed only data , means no file type could be verified. Then I decided to open the file using a hex editor and the first line start with BM which meant it was a bitmap image .

![](https://camo.githubusercontent.com/fedca6c9fc772023edb17ca3160028046ffc3428c120588a44667dc9c656ed73/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e58656441616d78477049534362393863676258714b35436b344764795566765a742d4f70426d584d746a46507333475f5f7975334c5234795a6e5666563766414c6c58625971494e3774746143775758466f506d2d30793068304b54742d41756757655f7335384543584474355549524c673654786c6b6b4f4b67484c595073666c696d6b425f66703968514a374b744168785166304e5844383f6b65793d4e335163776d5972712d4b6761596b41764f32596677)



Then after searching quite a bit I came across this article : [https://www.donwalizerjr.com/understanding-bmp/](https://www.donwalizerjr.com/understanding-bmp/) about hex values of bitmap images . As a read through , some of the bits of the image were corrupted .

![](https://camo.githubusercontent.com/abcaf61bd425890b620850c3510b56f89952ad11c7d0acb048182ec4b9f59537/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e58634d675445364e62477a32673930397a7136674d61486751745f5a5f6f6767676e34456b754e555a69316a32716a4f6632386c4545713069576452302d472d47332d34624f6873636d77426b747a593869656a776d2d4d3031385059532d6466726e79626e4350744c496e75615a4d766d65393975574657514951654e3051506d626d594e657a343343736738376453764a6a664f5762764d3f6b65793d4e335163776d5972712d4b6761596b41764f32596677)



The first 8 bytes are wrong according to the conventional bitmaps.

![](https://camo.githubusercontent.com/88314c217961131ce10b0b840528b315b46405b64d93b388655ad17ccd1dae19/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e5863386f6774386148736c41527867674d4b4770724e453644735641557532615432644d4b3479414f476c2d4b513639786f56444479666f4e41307a374f374f526a72584e7336474764586d54494559535a62375138616175526d6a49327643477849516e783166413758474c71736c4f564f66727653534c72343371554b67716f726e4b585a48426a6c345065585a4f59443278686235644d3f6b65793d4e335163776d5972712d4b6761596b41764f32596677)

After changing I received this image. 

![](https://camo.githubusercontent.com/4890e267db2682eba8eacc4471894af3ce8fd16099b24dbf2dc3c1b79a4e06d5/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e58664545587747514159684835622d61734d376b476b6b536c796647494c75554b614b7743716b6c56325f324858436270795a6b64434551776a446a3473425f655965366938654b4c6f4b6d79766f57416a6d7479762d33475a4865574c6d4e3271745455574b2d485178754577555373634c6d652d3443694a6e39656659687268456f4d5535337157306172473765356f5a4c3559654f44553f6b65793d4e335163776d5972712d4b6761596b41764f32596677)



The flag written is wrong , but the image seems to be cropped and feels like a small part of a big image. Steganography tools did not work on the bitmap. So I decided to change the height and width bits of the image and after 10-20 tries I came across the correct flag.

![](https://camo.githubusercontent.com/8b3cc5434f870f7dae373d725a9edb5788e814a9f09188f6fa49c52c33cee703/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e586655792d314c76486749392d76504c4c784c6c4775595046655561764d54714455736461697662433341363369394d714b593333636c527a5052304d5f6363585333317a637a6450665f324b4f316f323434684e725f527a5235386e47364546616c3071446f6368627542796f316952466849415848364f666734495776515f4142646a494c645856506753526c595a595233536546685a51783f6b65793d4e335163776d5972712d4b6761596b41764f32596677)



4. MacroHard WeakEdge

Given file is a powerpoint document which on opening does not give any useful information. However , on analysing with binwalk it contains a lot of hidden files.

![](https://camo.githubusercontent.com/9d2331502f08994c0a2673e576606ae4c36495392e20d6f55b7518571387fea5/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e58643442526f55664350653746525152514d594d3973315f317969725a3177623252586f5f495359734b33447a4430686b35506631693530577941513667794a6841487955482d41596d52734c5844763451464b7751595a704b6830786c68754a32372d694f545a303971647a737a6c6148475976625533635077694c76653638304d6d4264537964623242474a34544f526a4d4c57666e6464693f6b65793d4e335163776d5972712d4b6761596b41764f32596677)

![](https://camo.githubusercontent.com/6ba9f54280c073fcc77ff43b16c81adf170adc958976acddd36eea750ef5a3a7/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e58663070645a457a49572d724a786c727079357336676745664e62794963516e4a663661497644464d4f306d384a7563364f7238764d353234456b43447830727856394750334954414e586f554b6844524a716635644a31542d556d4d50706c375356627a6572556832423378445f6c505f354579356d34585443315654713256656c4146455a596633726c45305a5076573434734a5373456f3f6b65793d4e335163776d5972712d4b6761596b41764f32596677)

There is a file named hidden in the given location.

![](https://camo.githubusercontent.com/3dbcd12d8b47c9a16b4bef97404f705c1549a0134f85f2bd71427f2088e4ba22/68747470733a2f2f6c68372d75732e676f6f676c6575736572636f6e74656e742e636f6d2f646f63737a2f41445f346e586356666b4f577968414a624649653875506b62346d5651745676424b5775596f796a6b5a673165523652564e4e436f643463432d615749743961466d75464f564f37664e3977384956376877747171594254574b3951414c534368756f676735544f377065733175573871364642643378646f48457248636f654155455674615768703748793150616932754b3976567873626f6f65656976473f6b65793d4e335163776d5972712d4b6761596b41764f32596677)

It contains some gibberish characters . But upon analysing it seems this is a base64 encoded string. Decoding it gives the flag.
![](Week%201%20%20Challenge%201/2024-06-10-22-42-06-image.png)

5. Enhance![](Week%201%20%20Challenge%201/2024-06-10-22-43-49-image.png)!
   On opening the file through a text editor , in the end some characters can be observed.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-43-25-image.png)From the curly braces , I could tells that this is part of a flag and only the tspan lines contains it . So i filtered that out.
   
   
   Thus the flag is picoCTF{3nh4nc3d_d0a757bf}

6. advanced-potion-making
   File command in linux does not give any useful information as to what the file type is.
   By opening the file in hexeditor , by the IHDR block the given file can be recognised as a png file. But the  filetype header may have wrong values.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-44-22-image.png)By comparing the hex of given file with a correct png file .
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-45-04-image.png)After correcting the values, the file type is displayed by the file command.


![](Week%201%20%20Challenge%201/2024-06-10-22-45-28-image.png)Opening the image using pinta(application on linux) , just a red canvas is displayed.

![](Week%201%20%20Challenge%201/2024-06-10-22-45-56-image.png)However, if when I tried to color the canvas using bucket tool. The flag is displayed.

![](Week%201%20%20Challenge%201/2024-06-10-22-46-19-image.png)The flag is : picoCTF{wiz4rdry}

7. File types
   The file command doesn't identify the file as a pdf.
   ![](Week%201%20%20Challenge%201/2024-06-10-22-46-41-image.png)             
   
      
   The file cannot be opened using a pdf reader. But as the filetype is shell archive ,I converted the file to a bash executable with permissions.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-47-11-image.png)On executing , another file is given as output.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-47-36-image.png)After a series of tasks of determining file archive types and extracting them using suitable tools , a ascii text file is obtained.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-47-57-image.png)The file contains two hexadecimal strings. When the strings are converted to ascii , the flag is obtained.
   
   ![](Week%201%20%20Challenge%201/2024-06-10-22-48-17-image.png)The flag is : picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}

8. Hideme
   An image of the picoCTF logo is provided , with no useful exifdata . But upon using binwalk on the image , I observed that the image contains some hidden data.


![](Week%201%20%20Challenge%201/2024-06-10-22-48-48-image.png)The folder secret contains another image , containing the flag.

![](Week%201%20%20Challenge%201/2024-06-10-22-49-13-image.png)The flag is : picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}

9. MSB
   As the name suggests, msb (most significant bit) , I decided to use zsteg first to check for any bitwise operations for finding flags in the modified image bits, but zsteg was of no use . I tried to use binwalk , it did give a binary file but it had no traces of a flag. So , last option was stegsolve which could be used to get the msb from an image. After some tries with different variation of r , g and b bits , when all the three bits were selected and output to a file.
   ![](Week%201%20%20Challenge%201/2024-06-10-22-49-37-image.png)

The flag was present in the output file.
![](Week%201%20%20Challenge%201/2024-06-10-22-50-24-image.png)
The flag is : picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_24d55bee}

10. extensions
    Upon opening the file using cat command the file causes a font corruption in the terminal . On examining the file through file command , I found that the file is in fact a png file , with the wrong extensions provided.
    
    ![](Week%201%20%20Challenge%201/2024-06-10-22-50-48-image.png)The flag is : picoCTF{now_you_know_about_extensions}

**


