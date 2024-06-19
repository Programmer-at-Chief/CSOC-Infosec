# Encoding

#### ASCII

Created a small script to convert hex values to ascii.

[ASCII.py](Scripts/ASCII.py)

Flag : crypto{ASCII_pr1nt4bl3}

#### Hex

Just used the bytes.fromhex() function, another method can be used . It is commented out in the file.

[Hex.py](Scripts/Hex.py)

Flag : crypto{You_will_be_working_with_hex_strings_a_lot}

#### Base64

I used base64.b64encode() to convert ascii string to base64 encoded one .

[Base64.py](Scripts/Base64.py)

Flag : crypto/Base+64+Encoding+is+Web+Safe/

#### Bytes and Big Integers

I used the simple hex() and bytes.fromhex() functions to convert the decimal to hex and then to byte array.

[Bytes_and_Big_Integers.py](Scripts/Bytes_and_Big_Integers.py)

Flag : crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}

#### 

# XOR

#### Xor Starter

I used simple string manipulation and pwn.xor() to complete the challenge.

[Xor_Starter.py](Scripts/XOR_Starter.py)

#### Xor properties

I convert all the keys to byte array and used a simple for loop to xor 3 of the 4 given keys.

[Xor_Properties.py](Scripts/Xor_Properties.py)

Flag : crypto{x0r_i5_ass0c1at1v3}

#### Favourite Byte

I used a loop for all the integers from 0 to 255 and iterated through the byte string to xor all the elements of the byte string with the integer and find the appropriate string.

[Favourite_Byte.py](Scripts/Favourite_Byte.py)

Flag : crypto{0x10_15_my_f4v0ur173_by7e}

#### You either know, XOR you don't

Ok , this one took calculations , random guessess and a lot of time. As I was unable to find the correct key through the program alone , I used cyberchef and found "myXORke" and added "y" , just so as to complete a word , and it worked.

[Know_Xor.py](Script/Know_Xor.py)

Flag : crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}

# Mathematics

#### GCD

This one was easy. Just keep taking modulus till one of them  becomes zero.

[GCD.py](Scripts/GCD.py)

Flag: 1512

#### Extended GCD

I searched more about extended gcd and got the x,y formula related to x1,y1 . After applying it through recursion , I reached the answer.

[extended_GCD.py](Scripts/extended_GCD.py)

Flag : -8404

#### Modular Arithematic I

This was simple , just calculation.

[Mod1.py](Scripts/Mod1.py)

Flag : 4

#### Modular Arithematic II

After studying the Fermat Number Theorem I found that for base p and power p-1 the ans is 1, also my python program which used binary exponentation also gave same answer.

[Mod2.py](Scripts/Mod2.py)

Flag : 1

#### Modular Inverse

This was a special case of Fermat Number Theorem, it took some time to construct but was obvious once understood. Mainly, simple binary exponentation and mod function were required.

[Mod_Inv.py](Scripts/Mod_Inv.py)

Flag : 9

# Data Formats

CERTainly not

I did a lot of search for this one from man pages to chat-gpt. Finally I was able to locate the modulus using a simple python script of the pycryptodome library

[Cert.py](Scripts/Cert.py)

Flag : 22825373692019530804306212864609512775374171823993708516509897631547513634635856375624003737068034549047677999310941837454378829351398302382629658264078775456838626207507725494030600516872852306191255492926495965536379271875310457319107936020730050476235278671528265817571433919561175665096171189758406136453987966255236963782666066962654678464950075923060327358691356632908606498231755963567382339010985222623205586923466405809217426670333410014429905146941652293366212903733630083016398810887356019977409467374742266276267137547021576874204809506045914964491063393800499167416471949021995447722415959979785959569497

#### SSH Keys

This one was tough , because RSA.import_key() won't take the base64 keys direclty and that's why it required some research beforehand. Chatgpt helped a lot in this case.

[ssh.py](Scripts/ssh.py)

Flag : 3931406272922523448436194599820093016241472658151801552845094518579507815990600459669259603645261532927611152984942840889898756532060894857045175300145765800633499005451738872081381267004069865557395638550041114206143085403607234109293286336393552756893984605214352988705258638979454736514997314223669075900783806715398880310695945945147755132919037973889075191785977797861557228678159538882153544717797100401096435062359474129755625453831882490603560134477043235433202708948615234536984715872113343812760102812323180391544496030163653046931414723851374554873036582282389904838597668286543337426581680817796038711228401443244655162199302352017964997866677317161014083116730535875521286631858102768961098851209400973899393964931605067856005410998631842673030901078008408649613538143799959803685041566964514489809211962984534322348394428010908984318940411698961150731204316670646676976361958828528229837610795843145048243492909
