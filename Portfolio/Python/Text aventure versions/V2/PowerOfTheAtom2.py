#imports tge rune variable for the time.sleep command
import time
#sets a variable that i probably forgot to use
MetTheSheriff=False
print("I've made some changes to the plot that this was based on in the interest of time so if anything seems weird or contrived just go with it because it's probably easier than explaining all of the lore of the world outside of Megaton")
print('')
print('')
print('')
time.sleep (3)
def WelcomeToMegaton():
    print ("Welcome to Megaton")
    time.sleep (1)
    print ("Megaton is a city built around a crater with an undetonated nuclear bomb from a bygone war in the center; after which the town is named.")
    time.sleep (1)
    print ("The undetonated nuclear weapon has become a monument to the city.")
    time.sleep (1)
    print ("It's been around so long that people don't even realise its a threat anymore.")
    time.sleep (1)
    print ("The towns leadership hasn't bothered to hire someone to disarm the bomb either.")
    time.sleep (1)
    print ("You just so happen to be a retired explosives expert who is making your way into town.")
    time.sleep (1)
    print("")
    FirstDecisionWhereToGo()
def FirstDecisionWhereToGo():
    print ("Type 1 and press enter to ask around about the undetonated nuclear bomb in the middle of the city.")
    time.sleep (1)
    WhereToGo=input("Type 2 and press enter to go about your buisness as if theres nothing wrong with an undetonated nuclear bomb in the middle of a city")
    if WhereToGo== "1":
        AskAboutTheBomb()
    elif WhereToGo== "2":
        IgnoreTheBomb()
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        FirstDecisionWhereToGo()
def AskAboutTheBomb():
    print ("you ask about the nuclear bomb and eventualy you encounter the town sheriff")
    time.sleep (1)
    print ('"Im going to have to ask you to stop asking around about the bomb" The sheriff says')
    time.sleep (1)
    print ('"It makes people nervous, especialy because of that rumor thats been going around"')
    time.sleep (1)
    OportunityToAskAboutTheRumor()
def OportunityToAskAboutTheRumor():
    print ('Type 1 and press enter to ask about the rumor')
    time.sleep (1)
    AskRumor=input("Type 2 and press enter to ignore the rumor and offer to disarm the bomb")
    if AskRumor=="1":
        RumorExplination()
    elif AskRumor=="2":
        Ending1()
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        OportunityToAskAboutTheRumor()
def RumorExplination():
    print ('"Theres been this guy, Burke"')
    time.sleep (1)
    print ('"'+"He's dresed like he's here for buisness but hangs around doing basicaly nothing."+'"')
    time.sleep (1)
    print ('"'+"I've heard people say he has his eye set on that monument; some even say he wants to detonate it"+'"')
    time.sleep (1)
    print ('"' + "Regardless of whether these claims are true I can't have you going around worying the people that something dangerous is going to happen" + '"')
    OportunityToFindBurke()
def OportunityToFindBurke():
    MetTheSheriff=True
    print ('Type 1 and press enter to offer to find Burke and ask what his deal is')
    time.sleep (1)
    AskRumor=input("Type 2 and press enter to ignore the rumor and offer to disarm the bomb")
    if AskRumor=="1":
        FindBurke()
    elif AskRumor=="2":
        Ending1()
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        OportunityToAskAboutTheRumor()
def FindBurke():
    print('"Thanks, thats one less thing for me to worry about" the sheriff says"')
    time.sleep (2.3)
    print('As you encounter Burke he introduces himself')
    FoundBurke()
def IgnoreTheBomb():
    print("As you make your way to the shop you're aproached by a strange man who introduces himself as Br. Burke")
    FoundBurke()
def FoundBurke():
    time.sleep (1)
    print("Mr. Burke is dressed in very formal buisness atire and is carrying around a breifcase")
    time.sleep (1)
    print ('"'+"I understand you're an explosives expert. Yes?"+'" Mr. Burke says')
    time.sleep (1)
    print ('"Well then in that case I have a buisness proposition for you"')
    time.sleep (1)
    print ("He opens his briefcase and pulls out a small device")
    time.sleep (1)
    print ('"Take this and place it on the monument in the center of the city" he says')
    time.sleep (1)
    print ('"'+"It's magnetic so it schould stick to the surphase of it prettey easily"+'"')
    time.sleep (1)
    print ('"'+"I'd do it myself but can't get anywhere near that bomb with the sheriff already on my case"+'"') 
    time.sleep (1)
    print ('"'+"After that meet me outside of Megaton and you'll be rewarded with $30,000"+'"')
    time.sleep (1)
    Ending23Choice()
def Ending23Choice():
    print ('Type 1 and press enter to take the device and use it as evidince to turn Burke in to the sheriff and disarm the bomb after Burke is arested')
    Ending=input('Type 2 to place the device on the bomb and detonate it from a safe distance for the $30,000 reward from burke')
    if Ending=="1":
        print("Congratulations! you got Ending 2 (the best outcome for this text adventure)! Burke is Now in jail and the bomb is now disarmed! Play again and make different decisions to see the different endings")
    elif Ending=="2":
        print("Congratulations! you got Ending 3 (the most evil outcome for this text adventure)! The town of Megaton is now dead because of you, but youre richer because of it! Play again and make different decisions to see the different endings")
def Ending1():
    print ('"'+"You'd actually do that for me?"+'"')
    time.sleep (1)
    print ('"Thanks"')
    time.sleep (1)
    print ("you difuse the bomb and the whole town becomes just a little bit safer")
    time.sleep (1)
    print ("Congratulations! You got Ending 1 (the easiest and by far the least interesting ending)! The town of Megaton is now safe! Play again and make different decisions to see the different endings")
    



WelcomeToMegaton()

