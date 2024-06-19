# Starter

#### RSA Starter 1

I used modular exponentation idea with modulus function to achieve the ans.

Flag : 19906

[starter_1.py](Scripts/starter_1.py)



#### RSA Starter 2

This was also easily achieved using RSA encyption method and modular exponentation .

Flag : 301

[starter_2.py](Scripts/starter_2.py)

#### RSA Starter 3

I just calculated totient using the formula for totient.

Flag : 882564595536224140639625987657529300394956519977044270821168

[starter_3.py](Scripts/starter_3.py)

#### RSA Starter 4

I first used modular exponentation method with fermat little theorem but it was taking a lot of time , so I decided to use extended gcd algorithm. The latter method calculated the answer in seconds.

Flag : 121832886702415731577073962957377780195510499965398469843281

[starter_4.py](Scripts/starter_4.py)

#### RSA Starter 5

I used all the algorithms used till the 4 RSA tasks to find an efficient way to calculate the private_key and then the decoded cipher.

Flag : 13371337

[starter_5.py](Scripts/starter_5.py)

#### RSA Starter 6

I used just the hashlib library to get the sha256sum of the message and then used pow function to compute the encoded message. I didn't know about this usage of pow function , I got it from one of john hammond's rsa video.

Flag : 13480738404590090803339831649238454376183189744970683129909766078877706583282422686710545217275797376709672358894231550335007974983458408620258478729775647818876610072903021235573923300070103666940534047644900475773318682585772698155617451477448441198150710420818995347235921111812068656782998168064960965451719491072569057636701190429760047193261886092862024118487826452766513533860734724124228305158914225250488399673645732882077575252662461860972889771112594906884441454355959482925283992539925713424132009768721389828848907099772040836383856524605008942907083490383109757406940540866978237471686296661685839083475

[starter_6.py](Scripts/starter_6.py)

# Public Exponent

Salty

I just took the ciphertext value from output file ,and as e=1 , the RSA algorithm becomes ineffective as n>m so c=m in this case.

Flag : crypto{saltstack_fell_for_this!}

[salty.py](Scripts/salty.py)


