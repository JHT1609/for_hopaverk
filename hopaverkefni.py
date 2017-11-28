#Jóhannes Helgi Tómasson & Stefán Elís Beck


#Username & password
Users = {"kalli_kool":"dr4gon","Fannar_flotti":"password","oni0nboie_66":"rossiyagay"}

print("Viltu skrá nýjan notanda eða ertu nú þegar skráður inn á kerfið?\n######################\n#1.Skrá Nýjan notanda#\n#2.Skrá inn          #\n######################")

SL=input()
if SL=="2":
    print("##############\n# LOGIN AREA #\n##############")
    UN=input("Sláðu inn notandanafn: ")
    PW=input("Sláðu inn Leynikóðan:  ")
elif SL =="1":
    print("################\n# SIGN-IN AREA #\n################")
    UN=input("Sláðu inn notandanafn: ")
    PW=input("Sláðu inn Leynikóðan:  ")
    class User:
        def __init__(self,a,b):#Seigir um a, b og c fyrir föllin
            self.a = a
            self.b = b
        def create_user(self):
            Users.update({self.a:self.b})
            print(Users)
    p1=User(UN,PW)
    p1.create_user()



else:
    pass
