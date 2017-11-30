import time
#Jóhannes Helgi Tómasson & Stefán Elís Beck


loop1=True
while loop1 == True:
    time.sleep(.6)
    print("Viltu skrá nýjan notanda eða ertu nú þegar skráður inn á kerfið?\n######################\n#1.Skrá Nýjan notanda#\n#2.Skrá inn          #\n######################")

    SL=input()
    if SL=="2":
        print("##############\n# LOGIN AREA #\n##############")
        UN=input("Sláðu inn notandanafn: ")
        PW=input("Sláðu inn Leynikóðan:  ")
        file=open('notendur.txt','r')
        teljari=0
        for line in file:

            login=(UN+","+PW+"\n")
            if line == login:
                print("Rétt Login")
                teljari+=1
            elif line != login:
                pass
        if teljari == 0:
            print("*********************\n*Vitlaus Innskráning*\n*********************")
    elif SL =="1":
        print("################\n# SIGN-IN AREA #\n################")

        UN=input("Sláðu inn notandanafn: ")
        PW=input("Sláðu inn Leynikóðan:  ")
        '''
        with open('notendur.txt','a') as f:
            f.write(UN+","+PW)'''

        class User:
            def __init__(self,a,b):#Seigir um a, b og c fyrir föllin
                self.a = a
                self.b = b
            def create_user(self):
                with open('notendur.txt','a') as f:
                    f.write(UN+","+PW+"\n")
        p1=User(UN,PW)
        p1.create_user()

    else:
        print('"',SL,'" Er ekki þekt skipun')
