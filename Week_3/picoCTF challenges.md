# PicoCTF Challenges

### Web Gaunlet

#### 1

This was a series of five challenges, the first one was pretty straight forward , 

username: admin'--    password : 123

The second part filtered out --, so I had to use the other comment format,

username: admin'/*    password: 123

The third part was solved just like second one as /* comment format was not blocked,

username: admin'/*    password: 123

The fourth part did not allow admin to be written in input, I first tried username : adadminmin/* as to conceal admin in another admin to bypass first check, but it didn't work. After much searching , I came across this article https://sqldocs.org/sqlite/sqlite-string-concatenation/

it was about string concatenation, so instead of writing admin , I could divide it into two substrings and enter its concatenation as a username input

username: ad'||'min'/*     password: 123

The fifth round filters were already bypassed by my fourth round answers, so the same tricks worked again.

username: ad'||'min'/*    password: 123 

Thus , the flag was revealed.

flag : picoCTF{y0u_m4d3_1t_cab35b843fdd6bd889f76566c6279114}

Video : [PicoCTF: Web Gaunlet1 WriteUp - YouTube](https://youtu.be/C_uxP3f1SRE)

#### 2

This challenge had just one round and a load of filters. After tons of password bypass through various payloads still the round could not be solved. I went through multiple payloads on github and https://book.hacktricks.xyz/pentesting-web/login-bypass/sql-login-bypass but none worked .So I decided to work on the sql database type used. Interesting, sqlite has a glob function which works same as like but with bash escape syntax , so '*' meant any character. This function revealed the flag.

username : ad'||'min    password: ' glob '*

flag: `picoCTF{0n3_m0r3_t1m3_b55c7a5682db6cb0192b28772d4f4131}`

Video: [PicoCTF: Web Gaunlet2 WriteUp - YouTube](https://youtu.be/3GsDHV_J9Z4)

#### 3

This challenge had a 25 query length limit and the same filters as previous challenge , so the previous challenge query worked here again, the glob function was very useful and unique to sqlite.

username: ad'||'min    password: 'glob '* 

flag: `picoCTF{k3ep_1t_sh0rt_eb90a623e2c581bcd3127d9d60a4dead}`

Video: 

### Irish Name Repo

#### 1

In this challenge a site was given , with a login challenge. The site had no other information, the pages 1,2,3,4 all pointed to the same info. No login was begin accepted by the page. I turned to burpsuite for more analysis, where I found that on trying to login a peculiar string was appearing in the html headers.

![](picoCTF%20challenges/2024-06-26-23-37-04-image.png)

The debug is 0 , on changing it to one , a sql query was seen.

![](picoCTF%20challenges/2024-06-26-23-37-52-image.png)

I tried a simple payload, by changing admin to admin'--  and the flag was revealed.

Flag : picoCTF{s0m3_SQL_f8adf3fb}

Video : [PicoCTF: Irish Name Repo1 writeup - YouTube](https://youtu.be/a6XdgkTgZq0)

#### 2

This challenge was also solved the same way as Irish Name Repo 1 . The payload admin'-- also worked in this.

Flag : picoCTF{m0R3_SQL_plz_aee925db}

Video : [PicoCTF: Irish Name Repo2 writeup - YouTube](https://youtu.be/AnIchwlhbjM)

#### 3

In this challenge , only password was required to be submitted . The sql prompt was : 

SELECT * FROM admin where password = '

but the problem was the inputs were not interpreted correctly when the inputs were examined using debug=1 as done in challenge 1 and 2. 

![](picoCTF%20challenges/2024-06-27-00-17-40-image.png)

Firstly, I though that the input was translated to german as it looked alike 😅. Then upon further research, I found that it was a rot13 cipher. So I encoded my input with rot13, also "' or true -- " was not working so I changed the payload to "' or 1=1 --" and the flag was revealed.

![](picoCTF%20challenges/2024-06-27-00-20-51-image.png)

Flag : picoCTF{3v3n_m0r3_SQL_7f5767f6}

Video : [PicoCTF: Irish Name Repo3 WriteUp - YouTube](https://youtu.be/JQzqkLt1cqc)

### JaWT Scrathpad

In this challenge, I decided to start directly with burp and when I forwared through a site , I got a jwt cookie and looked up on how to decipher it.It was a base64 encoded string, divided into 3 parts but the third part was not base64.

![](picoCTF%20challenges/2024-06-26-20-13-51-image.png)

![](picoCTF%20challenges/2024-06-26-20-15-04-image.png)

As can be seen here the second part of the cookie had username but the last part is not base64. I came across this site https://jwt.io/ that could decode the cookie into its respective values.

![](picoCTF%20challenges/2024-06-26-22-02-47-image.png)

After some hours of tinkering, I realised that the payload was something that was not provided and was to be user generated to edit the cookie value. It would be a password , also on the webpage there was a link to john the ripper which could help in getting the password.

I used rockyou wordlist and got the password.

![](picoCTF%20challenges/2024-06-26-22-05-40-image.png)

After changing the user value and key ,

![](picoCTF%20challenges/2024-06-26-22-06-12-image.png)

and using that for jwt cookie value the flag was revealed.

Flag : picoCTF{jawt_was_just_what_you_thought_f859ab2f}

Video : [PicoCTF: Jawt ScratchPad writeup - YouTube](https://youtu.be/oyD06Stmcus)

### Who are you?

![](/home/aman/.config/marktext/images/2024-06-25-17-52-44-image.png)

Now PicoBrowser is not an actual browser(trust me I searched for it), but I don't need an actual browser to verify myself, just a simple html user-agent change would work.

![](/home/aman/.config/marktext/images/2024-06-25-17-55-46-image.png)

I used firefox to change my user-agent to PicoBrowser , but it gave another warning.

![](/home/aman/.config/marktext/images/2024-06-25-17-56-16-image.png)

Upon some html searching , I found out that the site was requesting a resource , but the data was not given to the same site . I came across this article : https://rahulk2903.medium.com/burp-suite-repeater-tryhackme-walkthrough-907c11548c4e , burpsuite could be used to do this but i decided to use curl.

![](/home/aman/.config/marktext/images/2024-06-25-21-01-35-image.png)

The output was :

![](/home/aman/.config/marktext/images/2024-06-25-21-02-00-image.png)

So , i used the date header

![](/home/aman/.config/marktext/images/2024-06-25-21-04-12-image.png)

Output: I don&#39;t trust users who can be tracked.</h3>

For this , I used a lot of different headers like 

Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'

Cache-Control: no-store, no-cache, must-revalidate, proxy-revalidate 

Pragma: no-cache

Feature-Policy: geolocation 'none'; microphone 'none'; camera 'none'

Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

, etc but the one which finally worked was do not track header which requests the site to not track user details , however if the site respects this request or not depends on the site only.

![](/home/aman/.config/marktext/images/2024-06-25-21-09-41-image.png)

Output: This website is only for people from Sweden.

![](/home/aman/.config/marktext/images/2024-06-25-21-11-20-image.png)

This tag would be useful here, 

![](/home/aman/.config/marktext/images/2024-06-25-21-12-58-image.png)

Output: You&#39;re in Sweden but you don&#39;t speak Swedish?

So the language needs to be changed here.

![](/home/aman/.config/marktext/images/2024-06-25-21-14-38-image.png)

And the flag is displayed.

![](/home/aman/.config/marktext/images/2024-06-25-21-14-57-image.png)

Flag : picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_f56f58a5}

Video : [PicoCTF: Who are you? writeup - YouTube](https://youtu.be/zHU8XqO5rNE)

### Secrets

On the site there is a secrets direcotry, so I tried to use dirb but it was not giving any good files. I tried robots.txt,admin and other possible sites, but it was of no use.So, I shifted to go to the location myself.

![](picoCTF%20challenges/2024-06-26-11-14-32-image.png)

![](picoCTF%20challenges/2024-06-26-11-16-42-image.png)

In the secret directory there is a hidden folder, which contains a login page.On trying to login , it said incorrect credentials and the url changed.

![](picoCTF%20challenges/2024-06-26-11-19-07-image.png)

There is a superhidden database , initially I tried to think of some sql attack and tried some payloads from username and password , but it didn't work. So i tried to change the link itself to access the page. Firstly, I tried going to http://saturn.picoctf.net:49930/secret/hidden/superhidden/Fxdfgwd.html , but this gave error 404. So , I removed the html page and voila !! . The flag was received.

![](picoCTF%20challenges/2024-06-26-11-23-16-image.png)

Flag : picoCTF{succ3ss_@h3n1c@10n_51b260fe}

Video : https://youtu.be/YL3rReNWUUY

### Client-side-again

This challenge presented a login page, with a password unable to be guessed direclty. In the sources tab to the devtools , there was a html file which had an array of strings which contained picoCTF in it. I used chatgpt to read the html file and explain it and there was a password verification which created substrings from the input and ran multiple checks on it to verify.

![](picoCTF%20challenges/2024-06-26-17-00-13-image.png)

So I decided to make multiple guesses to make a string to form a password as the verify function which was used to verify a password has some contradictions which would not allow any password to get through. After some tries I was able to make the flag.

Flag : picoCTF{not_this_again_337115}

Video : [PicoCTF: Client Side Again writeup - YouTube](https://youtu.be/z3XpeKgy3aA)

### Intro to Burp

So, the initial site stopped after saying that otp is wrong , so i entered to burpsuite to analyze more. 

![](picoCTF%20challenges/2024-06-26-01-39-47-image.png)

Fill this page with random data.

On the first intercept where the html starts with POST do nothing just forward it.

![](picoCTF%20challenges/2024-06-26-01-40-46-image.png)

But on the second intercept where the html starts with GET , change it to post and thus the flag is received.

![](picoCTF%20challenges/2024-06-26-01-41-47-image.png)

Well, I don't completely understand how this worked maybe this was just a bug supposed to be exploited.

Flag : picoCTF{#0TP_Bypvss_SuCc3$S_3e3ddc76}

Video : [PicoCTF: Intro To Burp Writeup - YouTube](https://youtu.be/2K5eksixLew)

### Java Script Kiddie

#### 1

In this challenge , the site that was provided had an image which was not being displayed correctly, so that first thing  I did was to look at the site code, the html had a cipher like encoding on a base64 encoded png. 

![](picoCTF%20challenges/2024-06-29-20-33-48-image.png)

This is an encryption function which was working on a user input and a bytes array, the bytes array was visibile in the network tab as it was begin fetched using a get function in the site code.

![](picoCTF%20challenges/2024-06-29-20-35-17-image.png)

This array contained numberical values from 0-255 (in the ascii range), this array was the ascii representation of an image which had undergone encryption using the assemble_png function on its hex values. The ascii was divided into 42 chunks of 16 values each and was shifting the values between each chunks at the corresponding index based on a key. The correct key would reassemble the image and provide the unshifted image with the flag. So , i reverse engineered the function and came up with a simple script. The script returns the key values but some things are to be done by hand as ,I was getting multiple values for the key and had to try each and every one to get the answer.

script: [JavaScipt_Kiddie.py](JavaScipt_Kiddie.py)

The final keys formed were,

![](picoCTF%20challenges/2024-06-29-20-43-36-image.png)

The values 6 and 2 were to be substituted at the respective positions to get further keys.

final key : 489474845167104

The image revealed a qr code which had the flag.

![](picoCTF%20challenges/2024-06-29-21-06-25-image.png)

Flag : picoCTF{7b15cfb95f05286e37a22dda25935e1e}

Video : [PicoCTF: Java Script Kiddie1 WriteUp - YouTube](https://youtu.be/6v8UdZRLcts)

2

This challenge was just like the first one except the key was 32 digits and only even indexes of the key were used to transform the image, so the odd indexes could be kept 0 .

In this one , I worked smartly and wrote the program to just display the hex output and changed the key for each magic number, as a result the answer key was retrieved rather quickly than automating everything.

Script: [JavaScript_Kiddie2.py](JavaScript_Kiddie2.py)

Video: [PicoCTF: Java Script Kiddie2 WriteUp - YouTube](https://youtu.be/n50A6E4RYAg)
