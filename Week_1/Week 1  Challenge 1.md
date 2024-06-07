**

Week 1: 

Challenge 1:

1. Information
    

First , I opened the file through neovim(text editor) and found out that the jpeg header has been modified with photoshop .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcpuifNCVci0wMd2P1xUW5vKx-YkgppqTV_0hVB926slaYJlbtvS-pQzr98tHrXufS_iczhH5Qqovqzyx-Er0mRlHkO_ornVIw-hg8ab78QxfkXA1AN87Mt2Es4ZiHdy1UAhL5KM8Ihsu0Gn8hPQ8eT6KxH?key=N3QcwmYrq-KgaYkAvO2Yfw)

The rdf:resource contains some sort of encoded strings . I copied it passed it through base64 decoder .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfRzqWyJIJCA-IR0LKAwAhi8da6foUuHvHehN2fMJ0Z_W-JROYGPmy30rAjigjbtbxkLWXHZKz3_UelO-laj7pFFK2uJ8OIPeqFIUKbdoU0Ihygev0r5mAJIldytuaG4WckSLXrXf2yGhphguqyxqzOWpug?key=N3QcwmYrq-KgaYkAvO2Yfw)

The flag is unfolded.

  

2. Matryoshka doll
    

Matryoshka dolls contain smaller size dolls inside themselves, this idea could be extended to the image hiding some important files inside.

So , I used binwalk to check for hidden files . 

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXedkpIgdtwr4QgLr-2HEVfyoZmU_bD46H756AIhzeVcT4YRXMONCwG2G1vm5K4xW-IaJjTJGIoHIUm9B1ng2X3U4YvOZvwqLgrv1ZXnvuZfj2rNDszN3h9Mnx5GOKbbLGc9ru0WkcEY9xsWVqPkC3KFWiiB?key=N3QcwmYrq-KgaYkAvO2Yfw)

There was another image and a zip file inside.

The zip file contains the same image as inside, the image upon analysing with binwalk showed further hidden files inside.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfnB2A5n47PCDDLRv2kwbVzSnYHozfv3W-adQi_JKmOT5c15FeH_pBeWcXzdGVMnmf4qer3O3GC7jii2pUVlLY0uw8oBmy9nJM5AKeqZ3esp_cix-y1wDTSJX5uAHAT_B9l_g15TcST-WBonKh9r88fDjs?key=N3QcwmYrq-KgaYkAvO2Yfw)

Another image inside with more hidden files.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe4rvyQERVDeEP9995shYfR2hKyXCX7oavkPY9sihLyUWK4zyzuorXmSLStOwmuvIQoDxERiBDxBouh9_ESf5lpRyDetJjN7TX32RgQnM4y6se47YUTwyZQJkyQY9mV4TmSMLLY7HKC_uxsK_I_wRTcgaE5?key=N3QcwmYrq-KgaYkAvO2Yfw)

Another image found inside which upon binwalking showed a file flag.txt.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeOJHS3Aq7BRWneZDEIChjvAaBfTpM-gO5P0l51cnvww61hohlQe2W0F91ly9-KR6RBDDr0P35ivLvPNBkeKw5J7442MRQzRujHeUeUsyWYyRggfYglyp4tWUBAx10ato-CcGl5Okg2KepwBzKR_p_LPxDM?key=N3QcwmYrq-KgaYkAvO2Yfw)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeTx3Anm_ghYshUY9wG-Cbb2WFz-6T1MRo96yDGlHuGO4ZZ2GOkMMIjds_iea0WXwzvr1qBOlBpRJMkJVigNhpGSvCTAkQ9USIdTTOFgHlxJUInT8jnx8mTEPivWFt17Flbu3evAVBXV5hL8tXlYYiYmnh-?key=N3QcwmYrq-KgaYkAvO2Yfw)

Flag.txt contains the required flag.

  

3. tunn3l v1s10n
    

First I used the file command to display the type of file which showed only data , means no file type could be verified. Then I decided to open the file using a hex editor and the first line start with BM which meant it was a bitmap image .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXedAamxGpISCb98cgbXqK5Ck4GdyUfvZt-OpBmXMtjFPs3G__yu3LR4yZnVfV7fALlXbYqIN7ttaCwWXFoPm-0y0h0KTt-AugWe_s58ECXDt5UIRLg6TxlkkOKgHLYPsflimkB_fp9hQJ7KtAhxQf0NXD8?key=N3QcwmYrq-KgaYkAvO2Yfw)

Then after searching quite a bit I came across this article : [https://www.donwalizerjr.com/understanding-bmp/](https://www.donwalizerjr.com/understanding-bmp/) about hex values of bitmap images . As a read through , some of the bits of the image were corrupted .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcMgTE6NbGz2g909zq6gMaHgQt_Z_ogggn4EkuNUZi1j2qjOf28lEEq0iWdR0-G-G3-4bOhscmwBktzY8iejwm-M018PYS-dfrnybnCPtLInuaZMvme99uWFWQIQeN0QPmbmYNez43Csg87dSvJjfOWbvM?key=N3QcwmYrq-KgaYkAvO2Yfw)

The first 8 bytes are wrong according to the conventional bitmaps .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc8ogt8aHslARxggMKGprNE6DsVAUu2aT2dMK4yAOGl-KQ69xoVDDyfoNA0z7O7ORjrXNs6GGdXmTIEYSZb7Q8aauRmjI2vCGxIQnx1fA7XGLqslOVOfrvSSLr43qUKgqornKXZHBjl4PeXZOYD2xhb5dM?key=N3QcwmYrq-KgaYkAvO2Yfw)After changing I received this image. 

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfEEXwGQAYhH5b-asM7kGkkSlyfGILuUKaKwCqklV2_2HXCbpyZkdCEQwjDj4sB_eYe6i8eKLoKmyvoWAjmtyv-3GZHeWLmN2qtTUWK-HQxuEwUSscLme-4CiJn9efYhrhEoMU53qW0arG7e5oZL5YeODU?key=N3QcwmYrq-KgaYkAvO2Yfw)

The flag written is wrong , but the image seems to be cropped and feels like a small part of a big image. Steganography tools did not work on the bitmap. So I decided to change the height and width bits of the image and after 10-20 tries I came across the correct flag.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe-cuFAc1wMzL9OcLWpWOtgQV8CR7N_Sy5_PwcBHHPz-OkLkf6oclfF3hR0IRQ30-pzC7Ksnfzezg-qcUE0nKWMryc5RvJ7sRI_nuJHbU6pyIAbBOinSwh8d0Cm-2yfwaTycokvLXl6iSgxujVlGl1DNzRf?key=N3QcwmYrq-KgaYkAvO2Yfw)![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfUy-1LvHgI9-vPLLxLlGuYPFeUavMTqDUsdaivbC3A63i9MqKY33clRzPR0M_ccXS31zczdPf_2KO1o244hNr_RzR58nG6EFal0qDochbuByo1iRFhIAXH6Ofg4IWvQ_ABdjILdXVPgSRlYZYR3SeFhZQx?key=N3QcwmYrq-KgaYkAvO2Yfw)

  

4. MacroHard WeakEdge
    

Given file is a powerpoint document which on opening does not give any useful information. However , on analysing with binwalk it contains a lot of hidden files.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXd4BRoUfCPe7FRQRQMYM9s1_1yirZ1wb2RXo_ISYsK3DzD0hk5Pf1i50WyAQ6gyJhAHyUH-AYmRsLXDv4QFKwQYZpKh0xlhuJ27-iOTZ09qdzszlaHGYvbU3cPwiLve680MmBdSydb2BGJ4TORjMLWfnddi?key=N3QcwmYrq-KgaYkAvO2Yfw)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXf0pdZEzIW-rJxlrpy5s6ggEfNbyIcQnJf6aIvDFMO0m8Juc6Or8vM524EkCDx0rxV9GP3ITANXoUKhDRJqf5dJ1T-UmMPpl7SVbzerUh2B3xD_lP_5Ey5m4XTC1VTq2VelAFEZYf3rlE0ZPvW44sJSsEo?key=N3QcwmYrq-KgaYkAvO2Yfw)

There is a file named hidden in the given location.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcVfkOWyhAJbFIe8uPkb4mVQtVvBKWuYoyjkZg1eR6RVNNCod4cC-aWIt9aFmuFOVO7fN9w8IV7hwtqqYBTWK9QALSChuogg5TO7pes1uW8q6FBd3xdoHErHcoeAUEVtaWhp7Hy1Pai2uK9vVxsbooeeivG?key=N3QcwmYrq-KgaYkAvO2Yfw)

It contains some gibberish characters . But upon analysing it seems this is a base64 encoded string. Decoding it gives the flag.
![[Pasted image 20240604130235.png]]

5. Enhance!
On opening the file through a text editor , in the end some characters can be observed.
![[Pasted image 20240604131554.png]]
 From the curly braces , I could tells that this is part of a flag and only the tspan lines contains it . So i filtered that out.
 ![[Pasted image 20240604131740.png]]

 Thus the flag is picoCTF{3nh4nc3d_d0a757bf}
6. advanced-potion-making
File command in linux does not give any useful information as to what the file type is.
By opening the file in hexeditor , by the IHDR block the given file can be recognised as a png file. But the  filetype header may have wrong values.
![[Pasted image 20240607155002.png]]
By comparing the hex of given file with a correct png file .
 ![[Pasted image 20240607155227.png]]
After correcting the values, the file type is displayed by the file command.

![[Pasted image 20240607155337.png]]
Opening the image using pinta(application on linux) , just a red canvas is displayed.
![[Pasted image 20240607155649.png]]
However, if when I tried to color the canvas using bucket tool. The flag is displayed.
![[Pasted image 20240607155809.png]]
The flag is : picoCTF{wiz4rdry}
	
7. File types
The file command doesn't identify the file as a pdf.
![[Pasted image 20240607160319.png]]				
The file cannot be opened using a pdf reader. But as the filetype is shell archive ,I converted the file to a bash executable with permissions.
![[Pasted image 20240607172453.png]]
On executing , another file is given as output.
![[Pasted image 20240607172701.png]]
After a series of tasks of determining file archive types and extracting them using suitable tools , a ascii text file is obtained.
![[Pasted image 20240607173150.png]]
The file contains two hexadecimal strings. When the strings are converted to ascii , the flag is obtained.
![[Pasted image 20240607173250.png]]
The flag is : picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}

8. Hideme
An image of the picoCTF logo is provided , with no useful exifdata . But upon using binwalk on the image , I observed that the image contains some hidden data.

![[Pasted image 20240607174000.png]]
The folder secret contains another image , containing the flag.
![[Pasted image 20240607174038.png]]
The flag is : picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}

9. MSB
As the name suggests, msb (most significant bit) , I decided to use zsteg first to check for any bitwise operations for finding flags in the modified image bits, but zsteg was of no use . I tried to use binwalk , it did give a binary file but it had no traces of a flag. So , last option was stegsolve which could be used to get the msb from an image. After some tries with different variation of r , g and b bits , when all the three bits were selected and output to a file.
![[Pasted image 20240608001423.png]]

The flag was present in the output file.
![[Pasted image 20240608001508.png]]
The flag is : picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_24d55bee}
10. extensions
Upon opening the file using cat command the file causes a font corruption in the terminal . On examining the file through file command , I found that the file is in fact a png file , with the wrong extensions provided.
![[Pasted image 20240607174512.png]]
The flag is : picoCTF{now_you_know_about_extensions}

**

