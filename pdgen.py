#Password Generator
import random as r

l=['A', 'B', 'C', 'D', 'E', 'F', 'G','0', '1', '2', '3', '4', 
   '5', '6', '7', '8', '9', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't','1', '2', '3', 
     '4', '5', '6', '7', '8', '9', 'u', 'v', 'w', 'x', 'y', 'z',
     '!', '@', '#', '$', '%', '&', '*', '-', '_', '+', '=', '[', ']', '{', '}', 
     ':', '.', '/', '<', '>', '?', '0', '1', '2', '3', '4', '5', 
     '6', '7', '8', '9']

def ask1():
    global pwd1
    print("Registered E-mail into 3 alphanumeric char ")
    pwd1=input("for eg: abcd1234@idk.com into 'a12' :")
    pwd1.lower()
    pwd1=pwd1[::-1]
def ask2():
    global pwd3
    print("Enter 3 letter word for the desired platform")
    pwd3=input("as given above:")
    pwd3=pwd3.upper()
    pwd3=pwd3.encode().hex()
def fileop():
    print("01.Insta-INS\n02.Fb-FBK\n03.Whatsapp-WHT\n04.Reddit-RED\n05.Github-GIT")
    print("06.LinkedIn-LIN\n07.Telegram-TEL\n08.Gmail-GML\n09.Mega-MEG\n10.Twitter-TWT")
    print("11.SBI-SBI\n12.Microsoft-MFT\n13.Amazon-AMZ\n14.Discord-DIS\n15.Coinswitch-CSW")
    print("16.CoinDCX-CDX\n17.Groww-GRW\n18.xiaomi-XOM\n19.paytm-PYM\n20.Snapchat-SPC")

#Phase1
r.shuffle(l)
fileop()
ask1()
ask2()
#Phase2
r.shuffle(l)
p = r.sample(l,6)
pwd2=("".join(map(str, p)))
#Print:)
fnp=[pwd1,pwd2,pwd3]
fp="".join(fnp)
print("Password is: ",fp)
#print(pwd1,pwd2,pwd3)

"""
New updates
#6/8/10/12/14  digit passw
#removal of some chars

"""