import random
import sys
from datetime import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menu():
    print(bcolors.WARNING+"                 🕸Main menu"+bcolors.ENDC)
    print(bcolors.OKBLUE + """
        1.📝 Create a new account
        2.🗝 Log in
        0.🔚 Exit
                                                                  01.‍💻 Administration
        """ + bcolors.ENDC)

def headMenu(item):

    if item.isdigit():
        if item == "1":
            registration()
        elif item == "2":
            kirish()
        elif item == "0":
            print(bcolors.FAIL + ">>>>🎧 Program is stopped<<<<" + bcolors.ENDC)
            sys.exit(1)
        elif item=="01":
           administration()
        else:
            print(bcolors.FAIL + "Error 🚫" + bcolors.ENDC)
            item = (input('Select one option:'))
            headMenu(item)
    else:
        print(bcolors.FAIL + "Error 🚫" + bcolors.ENDC)
        item = (input('Select one option:'))
        headMenu(item)

def itemCheck(massiv,a):
    b=True
    while b:
        if a==5:
            item1=input("\nPlease enter a song number to vote for :")

        else:
            item1 = input("Select one option:")

        for i in range(len(massiv)):
            if str(massiv[i]) == item1:
                b=False
                return  item1

        if b and a==1:
            print(bcolors.FAIL + "Error 🚫" + bcolors.ENDC)
        if b and a == 2:
            print(bcolors.FAIL + "Please,select [0] or [1]" + bcolors.ENDC)
            print(bcolors.OKBLUE + """
                                0.🏠 Home page
                                1.⏸ Continue
                                    """ + bcolors.ENDC)
        if b and a==3:
            backOrExit(1)
        if b and a==4:
            print(bcolors.FAIL + "Error 🚫" + bcolors.ENDC)
            backOrExit(1)
        if b and a==5:
            print(bcolors.FAIL + "The number of music is wrong." + bcolors.ENDC)
            backOrExit(1)

def registration():
    print(bcolors.OKBLUE + """
        1.📖 Register now
        0.🔙 Back
            """ + bcolors.ENDC)
    item1= itemCheck([0,1],1)
    if item1 == '1':
        print("         "+           "Assalomu alaykum!")
        name = check("Name:")
        surname = check("Surname:")
        age = check("raqam")
        number = check('telNumber')
        jins = check("gender")
        users = open("register.txt", 'a')
        id = check("id")
        login = id
        f = open("id.txt", "w")
        f.write(str(id))
        f.close()
        sname=open("name.txt","w")
        sname.write(name)
        sname.close()
        print("    " + bcolors.WARNING + "Your login:  " + str(
            name) + "\n" + "    " + "Your Password:  " + str(login) + "\nPlease don`t lost it and never give anyone!!" + bcolors.ENDC)

        users.write(str(
            id) + "  Name:" + name + "  Surename:" + surname + "  Age:" + age + "  Phone number:" + number + "  Gender:" + jins + "\n")
        users.close()
        print(bcolors.OKGREEN + "  \n          ***You are registered***" + bcolors.ENDC)
        musicMenu()
    elif item1 == '0':
        menu()
        item = (input("Select one option:"))
        headMenu(item)

def kirish():
    login = input(bcolors.OKBLUE+"🔑"+bcolors.ENDC+" Login:")
    kod = input(bcolors.OKBLUE+"🔑"+bcolors.ENDC+ " Password:")
    userName=open("name.txt","w")
    userName.write(login)
    userName.close()
    k = open("register.txt", "r")
    b = True
    for k1 in k:
        if len(k1) > 1:
            massiv = k1.split("  ")
            parol = massiv[1].split(":")

            if kod == '1' and login == '1':
                new_week_voute()
            elif kod == massiv[0] and login == parol[1]:
                f=open("id.txt","w")
                f.write(kod)
                f.close()

                musicMenu()
                b = False
                break
            else:
                b = True
    if (b == True):
        print(bcolors.FAIL + "Login or Password error 🚫" + bcolors.ENDC)
        print(bcolors.OKBLUE + """
        0.🕸 Main menu
        1.⏸ Continue
        """ + bcolors.ENDC)
        kirish1()

def kirish1():
    select = itemCheck([0,1],2)
    if select == "0":
        menu()
        item = (input('Select one option:'))
        headMenu(item)

    elif select == "1":
        kirish()

def check(mode):
    if (mode == 'id'):
        b = True
        id = 1
        while (b):
            id = random.randint(1000000, 9999999)
            idlar = idlar_royhati()
            if id not in idlar:
                b = False
        return id

    if mode == 'gender':
        b = True
        jins = ""
        while (b):
            gender = input("Male=1 Female=2 :")
            if gender == "1":
                jins = "Male"
                b = False
            if gender == "2":
                jins = "Female"
                b = False
        return jins

    if mode == 'Name:' or mode == "Surname:":
        b = True
        name = ""
        while (b):
            gender = input(mode)
            if gender.isalpha() and len(gender) > 0 and len(gender) < 12:
                name = gender
                b = False
            else:
                error("numbers")
        return name.capitalize()

    if (mode == 'raqam'):
        age = ""
        b = True
        while (b):
            age = input("️Age:")
            if age.isalpha():
                error("letters")

            elif age.isdigit() and int(age) < 150 and int(age) > 12:
                b = False
            else:
                b = True
                print(bcolors.FAIL + """
                
                If you are under 12 and over 150, you will not be able to register!
                """ + bcolors.ENDC)
                print(bcolors.OKBLUE + """
                    0.🕸Main page
                    1.⏸Continue
                """ + bcolors.ENDC)
                selectway = int(input("Select one option::"))
                if selectway == 0:
                    menu()
                    number = (input("Select one option:"))
                    headMenu(number)
                    b = False

                else:
                    pass
        return age

    if (mode == 'telNumber'):
        b = True
        name = ""
        while (b):
            gender = input("️+998 ")
            if gender.isdigit() and len(gender) == 9:
                name = gender
                b = False
            elif gender.isalpha() or gender.isspace():
                error("letters")
        return name

def error(text):
    print(bcolors.FAIL + "         Error 🚫" + bcolors.ENDC)
    print(bcolors.FAIL + "         Please,don`t use " + text + " or symbols and any space!" + bcolors.ENDC)

def idlar_royhati():
    f = open("register.txt", "r")
    id_massiv = []
    for x in f:
        try:
            id_massiv.append(int(x[0:7]))
        except:
            pass

    return id_massiv

def musicMenu():
    userName()
    print("             "+bcolors.OKBLUE+"\n\n🎧"+bcolors.ENDC+bcolors.OKBLUE+"              🏠 Home page "+bcolors.ENDC)
    print(bcolors.OKBLUE + """
        1. 🎼 List of songs
        2. 🥇 Rating of songs
        3. 📜 The songs I voted for
        4. 🔍 Search
        0. 🕸 Main menu
    """ + bcolors.ENDC)
    select = itemCheck([0,1,2,3,4],3)
    if select == '1':
        massiv=listOfSongs()
        listOfSongs2(massiv)
        print("""
        2.🔍 Search
        """)

        backOrExit(2)
    elif select == '2':
        rating()
    elif select=="3":
        print(bcolors.OKBLUE+"""
                  📜 The songs I voted for
        """+bcolors.ENDC)
        history()
        sys.exit(1)
    elif select == '4':
        massiv=search()
        if massiv=="empty":
            print("Sorry! no result ⭕️")
            backOrExit(1)
        else:
            listOfSongs2(massiv)
            backOrExit(1)
    elif select == '0':
        menu()
        item = (input('Select one option:'))
        headMenu(item)

def backOrExit(mode):
    print(bcolors.OKBLUE + """
        1.🔙 Back
        0.🔚 Exit
    """ + bcolors.ENDC)
    select1=1
    if mode ==1:
        select1 = int(itemCheck([0,1],4))
    if mode ==2:
        select1 = int(itemCheck([0,1,2],4))

    if select1 == 1:
        musicMenu()
    if select1 == 0:
        print(bcolors.FAIL + ">>>>🎧 Program is stopped<<<<" + bcolors.ENDC)
        sys.exit(1)
    if select1== 2:
        massiv=search()
        if massiv == "empty":
            print("Sorry! no result ⭕️")
            backOrExit(1)
        else:
            listOfSongs2(massiv)
            backOrExit(1)

def listOfSongs():
    userName()
    print(bcolors.WARNING + "\n                 🎼 List of songs" + bcolors.ENDC+"\n")
    massiv1=[]
    list = open("list_songs", "r")
    count = 0
    for item in list:
        count += 1
        massiv = item.split("like")
        print("  "+str(count) + bcolors.OKBLUE + ". 🎵 " + bcolors.ENDC + massiv[0])
        massiv1.append(count)
    list.close()
    return massiv1

def listOfSongs2(massiv):
    selectsong = int((itemCheck(massiv,5)))

    list = open("list_songs", "r")
    music_massiv = []
    ovoz_massiv = []
    for music in list:
        try:
            massiv = music.split("like")
            music_massiv.append(massiv[0])
            ovoz_massiv.append(int(massiv[1].rstrip('\n')))
        except:
            pass

    list.close()
    ovoz_massiv[selectsong - 1] = ovoz_massiv[selectsong - 1] + 1
    list = open("list_songs", "w")
    list.write("")
    list.close()
    list = open("list_songs", "a")
    for i in range(len((ovoz_massiv))):
        list.write(music_massiv[i] + "like" + str(ovoz_massiv[i]) + "\n")

    list.close()
    print(bcolors.OKBLUE+"🎵 "+bcolors.ENDC + music_massiv[selectsong - 1] + " ---> 👍 +1"+bcolors.ENDC)
    now = datetime.now()
    id_story=open("id.txt","r")
    f = open("ovozlar_royhati.txt", "a")
    f.write(id_story.readline()+"$$" + music_massiv[selectsong - 1] + "   " + str(date.today()) + "  " + now.strftime("%H:%M:%S") +"voted"+ "\n")
    f.close()
    id_story.close()

def history():
    userName()
    f=open('ovozlar_royhati.txt','r')
    user_id=open('id.txt','r')
    parol=user_id.readline()
    count=1
    for i in f:
        id=i.split("$$")[0]
        music=i.split("$$")[1]
        vaqt=music.split("   ")[1]
        music=music.split("   ")[0]
        if ( parol==id):
            print(str(count)+". "+music+"  "+bcolors.OKBLUE+vaqt+bcolors.ENDC)
            count+=1
    if count==1:
        print(bcolors.FAIL+"You have not vouted to any music yet"+bcolors.ENDC)
    f.close()
    user_id.close()
    backOrExit(1)

def new_week_voute():
    list = open("list_songs", "r")
    music_massiv = []
    ovoz_massiv = []
    for music in list:
        try:
            massiv = music.split("like")
            music_massiv.append(massiv[0])
            ovoz_massiv.append(int(massiv[1].rstrip('\n')))
        except:
            pass

    list.close()
    list = open("list_songs", "w")
    list.write("")
    list.close()
    list = open("list_songs", "a")
    for i in range(len((ovoz_massiv))):
        list.write(music_massiv[i] + "like" + "0\n")

    list.close()
    print("Rating is restarted")

def search():
    userName()
    word=input("                        "+bcolors.OKBLUE+"TV Top Music search 🔍_____ "+bcolors.ENDC)
    s=word.capitalize()
    search=[]
    result=[]
    list=open("list_songs","r")
    for musics in list:
        x=musics.split("like")
        search.append(x[0])
    count=0
    for music in search:
        count+=1
        if s in music:
            result.append(str(count)+". "+str(music))

    searchNumber=[]
    for song in result:
        print(song)
        searchNumber.append(song.split(".")[0])
    if len(searchNumber)<1:
        return "empty"
    else:
        return searchNumber

def rating():
    userName()
    print(bcolors.OKBLUE+"""
🎧              ***Welcome to TV Top Music***
                        ***Rating Of songs***
    """+bcolors.ENDC)
    list = open("list_songs", "r")
    popular = []
    popular2 = []
    reyting = []
    zaxira = []

    for music in list:
        popular.append(music.split("like")[0])
        reyting.append(int(music.split("like")[1].rstrip("\n")))
        zaxira.append(int(music.split("like")[1].rstrip("\n")))
    reyting.sort(reverse=True)
    list.close()
    for i in range(len(reyting)):
        for j in range(len(zaxira)):
            if (reyting[i] == zaxira[j]):
                if (popular[j] not in popular2):
                    popular2.append(popular[j])
    for i in range(len(popular2)):
        print(str(i + 1) + " - o'rin ---> " + popular2[i] + "  " + str(
            reyting[i]) + bcolors.OKBLUE + " 👍" + bcolors.ENDC)
    backOrExit(1)

def addMusic():
    music=input("Add any music:")
    list=open("list_songs","a")
    list.write(music+"like"+"0"+"\n")
    print("The song is added")

def administration():
    key = input("Administration Password:")
    if key.isalpha() and key == "admin":
        administration2()

    else:
        print("""
            \nWrong,administration password!
        """)
        menu()
        item = (input('Select one option:'))
        headMenu(item)

def administration2():
    print("""
                                                                                1.Add music
                                                                                2.Restart rating
                                                                                0.Back
                        """)
    admin = input("Admin:")
    if admin.isdigit() and admin == "1":
        addMusic()
        administration2()
    elif admin.isdigit() and admin == "2":
        new_week_voute()
        administration2()
    elif admin == "0":
        menu()
        item = (input('Select one option:'))
        headMenu(item)
    else:
        print("Please,select [1] or [2]")
        administration2()

def userName():
    name=open("name.txt","r")
    profileName=name.read()
    print("                                                               \n"
          "                                                                                       "
          "                    "+bcolors.OKBLUE+"🔷"+profileName+"🔷"+bcolors.ENDC)

