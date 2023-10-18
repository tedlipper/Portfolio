"""
Any and all code in this project is the work of Ted
The script name for this file is PowerOfTheAtom
Its purpose is to be the main script to run the text adventure

"""
#Importing the time library so the time.sleep command works
import time
import DataStorage
#Defining a variable that I dont think i actually used
MetTheSheriff=False
#Creating the storage list
Path = []
#printing a bunch of things to pad out the time
print('')
print('')
print('')
print(DataStorage.Openinglines1[0])
print(DataStorage.Openinglines1[1])
print(DataStorage.Openinglines1[2])
print(DataStorage.Openinglines1[3])
print('')
print('')
print('')
#first use if the time.sleep command time.sleep makes the program wait
time.sleep (3)
#defining all of my functions before calling the start
def WelcomeToMegaton():
    print ("Welcome to Megaton")
    time.sleep (1)
    print ("Megaton is a city built in a crater")
    time.sleep (1)
    print ("with an undetonated nuclear bomb from a bygone war in the center")
    print ("after which the town is named.")
    time.sleep (1)
    print ("The undetonated nuclear weapon has become a monument to the city.")
    time.sleep (1)
    print ("It's been around so long, people don't see it as a threat anymore.")
    time.sleep (1)
    print ("The towns leadership hasn't bothered to disarm the bomb either.")
    time.sleep (1)
    print ("You just so happen to be a retired explosives expert")
    time.sleep (1)
    print ("who is making your way into town.")
    time.sleep (1)
    print("")
    #calls another function for the first time
    FirstDecisionWhereToGo()
#decision branch
def FirstDecisionWhereToGo():
    #decision tree
    print ("Type 1 and press enter to ask around about the undetonated nuke")
    time.sleep (1)
    #Sets a variable to be the input
    WhereToGo=input("Type 2 and press enter to ignore the old monument")
    Path.append(WhereToGo)
    #calls the apropriate function depending on the input
    #outcome 1
    if WhereToGo== "1":
        AskAboutTheBomb()
    #outcomne 2
    elif WhereToGo== "2":
        IgnoreTheBomb()
    #else statement in case they type in something else
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        FirstDecisionWhereToGo()
#Story text
def AskAboutTheBomb():
    print ("You ask about the nuclear bomb")
    time.sleep (1)
    print ("Eventualy you encounter the town sheriff")
    time.sleep (1)
    print ('"Im going to have to ask you to stop asking around about the bomb"')
    print ('The sheriff says')
    time.sleep (1)
    print ('"It makes people nervous, especialy because of that Burke guy"')
    time.sleep (1)
    OportunityToAskAboutTheRumor()
#Decision branch
def OportunityToAskAboutTheRumor():
    print ('Type 1 and press enter to ask about the Burke')
    time.sleep (1)
    AskRumor=input("Type 2 and press enter offer to disarm the bomb")
    Path.append(AskRumor)
    if AskRumor=="1":
        RumorExplination()
    elif AskRumor=="2":
        Ending1()
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        OportunityToAskAboutTheRumor()
#Story text
def RumorExplination():
    print ('"Theres been this guy, Burke"')
    time.sleep (1)
    print ('"'+"He's dresed like he's here for buisness"+ '"')
    time.sleep (1)
    print ('"' +"But he hangs around the saloon doing basicaly nothing."+'"')
    time.sleep (1)
    print ('"'+"I've heard people say he wants to detonate that monument" + '"')
    time.sleep (1)
    print ('"But without any solid evidince we cant convict him of anything"')
    print ('"Regardless of whether these claims are true you need to stop"')
    print ('"Asking makes people scared something bad is going to happen"')
    print ('"and the last thing i need right now is a massive public freakout"')
    OportunityToFindBurke()
#Decision branch
def OportunityToFindBurke():
    MetTheSheriff=True
    print ('Type 1 and press enter to offer to find Burke')
    time.sleep (1)
    AskRumor=input("Type 2 and press enter to offer to disarm the bomb")
    Path.append(AskRumor)
    if AskRumor=="1":
        FindBurke()
    elif AskRumor=="2":
        Ending1()
    else:
        print ("Invalid answer...")
        time.sleep (3)
        print ("Asking question again")
        OportunityToAskAboutTheRumor()

#FindBurke and IgnoreTheBomb are different starts to the FoundBurke function
#FindBurke and IgnoreTheBomb both contextualise the Foundburke function
#This is so I dont have to rewrite the same conversation twice
def FindBurke():
    print('"Thanks, thats one less thing for me to worry about"')
    time.sleep (2.3)
    print('As you encounter Burke he introduces himself')
    FoundBurke()
def IgnoreTheBomb():
    print("As you make your way to the shop you're aproached by a strange man")
    print("who introduces himself as Br. Burke")
    FoundBurke()

#the encounter where you meet burke
def FoundBurke():
    time.sleep (1)
    print ("Mr. Burke is dressed in very formal buisness atire")
    print ("and is carrying a large black breifcase")
    time.sleep (1)
    print ('"I understand youre an explosives expert. Yes?" Mr. Burke says')
    time.sleep (1)
    print ('"Well then in that case I have a buisness proposition for you"')
    time.sleep (1)
    print ('"My employer wants this little town taken of the map"')
    time.sleep (1)
    print ('"Id do it myself but cant get anywhere near that bomb"')
    time.sleep (1)
    print ('"At least not with the sheriff already on my case"') 
    time.sleep (1)
    print ("He opens his briefcase and pulls out a small device")
    time.sleep (1)
    print ('"Take this and place it on the monument in the center of the city"')
    time.sleep (1)
    print ('"'+"It's magnetic so it should stick to the surphase of it"+'"')
    time.sleep (1)
    print ('"After that meet me outside of Megaton"')
    print ('"Youll be rewarded with $30,000 if you go through with this"')
    time.sleep (1)
    print ('You take the device')
    Ending23Choice()
#Decision branch for endings 2 and 3
def Ending23Choice():
    print ('Type 1 and press enter use the device as evidince to turn Burke in')
    Ending=input('Type 2 to place the device on the bomb')
    Path.append(Ending)
    if Ending=="1":
        print("Congratulations! you got Ending 2")
        print("the best outcome for this text adventure!")
        print("your path was" + str(Path))
        print("Burke is Now in jail and the bomb is now disarmed!")
        print("Play again and make different decisions for a different ending")
    elif Ending=="2":
        print("Congratulations! you got Ending 3")
        print("The most evil outcome for this text adventure!")
        print("your path was" + str(Path))
        print("You placed the device on the undetonated bomb")
        print("When you met Burke outside of megaton he detonated the monument")
        print("As a man of buisnes he gave you the $30,00")
        print("The town of Megaton is now dead because of you")
        print("Play again and make different decisions for a different ending")
    else:
        print("you should understand how this works by now")
        print("sigh")
        print("restarting question")
        Ending23Choice()
#Ending 1
def Ending1():
    print ('"'+"You'd actually do that for me?"+'"')
    time.sleep (1)
    print ('"Thanks"')
    time.sleep (1)
    print ("You difuse the bomb and the town is a little bit safer now")
    print ("thanks to you")
    time.sleep (1)
    print ("your path was" + str(Path))
    print ("Congratulations! You got Ending 1")
    print ("the easiest and by far the least interesting ending!")
    print ("The town of Megaton is now safe!")
    print ("Play again and make different decisions for a different ending")
    


#the function that calls it all
#the one line of code that this wouldnt work without
WelcomeToMegaton()
