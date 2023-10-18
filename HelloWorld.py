#Setting up the sleep command to make the program wait by importing the time variable from my computers OS
import time
#Creating an asked variable
#Setting asked to 0 bacause if asked = 0 then it will mean that they didn't ask and I still need to explain it but if they did ask then I dont need to have the dialogue explain it and I wont waste their time
asked=0
#Defining the hello world function
def HelloWorld():
#Puting the code into the hello world program
    print("Hellow!")
    #Not calling the program afterwards because it would waste time
#Creating a thing to waste more time and make it verry clear that I am not a creative person
def CreditWhereCreditIsDue():
    print('This text adventure is heavily based off of the "Oasis" side quest from Fallout 3')
#Blank print command to have a line space in between lines
    print("")
#time.sleep commands to make it wait in between lines and make it happen one at a time instead of all at once
#    time.sleep(3)
    print("I did not come up with the plot, characters, decisions, or anything else displayed in this text adventure")
    print("")
#    time.sleep(3.5)
    print("All credit for the plot goes to Bethesda (the original developers of Fallout 3), the Fallout 3 fandom website, and the YouTube videos (by Oxhorn) which I used as reference material")
    print("")
#    time.sleep(5)
    print("Reference material here ---> https://fallout.fandom.com/wiki/Oasis_(quest)")
    print("")
    print("")
    print("")
#    time.sleep(1)
#Calling the function

#Asking their name

#Defining a code so that when it asks what my name is, if i say my name is GameDev then it'll print the name of all of the functions for me to be able to skip to later in the story
def GameDev1():
    print ("GameStart()")
    print ("TextAdventureStart()")
    print ("DecisionFollow()")
    print ("EndQuest1()")
    print ("PressureOportunity()")
    print ("ExplinationBeforeEncounter()")
    print ("Ritual()")
    print ("PressureOportunity()")
    print ("FurtherExplinationBirch()")
    print ("LeaveAttempt()")
    print ("Inspection()")
    print ("MeetHarrold()")
    print ("HarroldConversation1()")
    print ("HarroldConversationRoute21()")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")

#Defining all of the functions bafore I call the first one so I can call them out of order and have it still work
def GameStart():
    CreditWhereCreditIsDue()
    name = input("(For game development reasons) What's your name? ")
    if name=="GameDev":
        print ('Welcome back')
        GameDev1()
    else:
        print ("Hi " + name)
        TextAdventureStart()
#Starts the text adventure
def TextAdventureStart():
    print('When exploring the map of Fallout 3 you encounter a strange place called "Oasis".')
#    time.sleep(2.5)
    print('On aproaching Oasis, you encounter a strange man by the name of "Tree Father Birch" who asks you to follow him.')
#    time.sleep(3)
    print('Birch explains that "He" has summoned you, but doesent say exactly who or what "He" is.')
#    time.sleep(5)
    answer = input('Type 1 and press enter to go with Birch. Type 2 and press enter to say no (ends the text adventure imediately).')
    #If/then/else starement for a different response depending on the answer
    if answer=="1":
        print('')
        #Continues the story if you decide to go with birch
        DecisionFollow()
    elif answer=="2":
        print('')
        #Ends the quest
        EndQuest1()
        #If the answer is not 1 or 2 then the program will ask the question again
    else:
        print('')
        print ("INVALID ANSWER")
        TextAdventureStart()
#Ends the quest
def EndQuest1():
    print('You refuse and end the side quest')
    quit()
#Continues the story path where you go with birch
def DecisionFollow():
    print("")
    print('While leading you to their village, Birch explains that he is the leader of "The Treeminders"')
#    time.sleep(5)
    print('Birch explains that The Treeminders are a group of people who worship "him" and treasure every bit of life he brings to their village.')
#    time.sleep(7)
    answer = input('Type 1 and press enter to ask who "he" is and why they are being so vague about it. Type 2 and press enter to let it slide and just go with it.')
    if answer=="1":
        print('')
        #Calls the weird and cryptic explination before you get to oasis
        ExplinationBeforeEncounter()
    elif answer=="2":
        print('')
        #Skips straight to oasis
        Ritual()
        #Re-asks the question again if the answer is invalid
    else:
        print('')
        print ("INVALID ANSWER")
        DecisionFollow()
def ExplinationBeforeEncounter():
    print("")
    print('"He is the one who grows, he is the one who gives, and he is the one who guides"')
#    time.sleep(4)
    print('"No one speaks his name out of reverence for his magesty"')
#    time.sleep(4.5)
    print('"Thanks to him, The Treeminders have a home" Birch says.')
#    time.sleep(3)
    answer = input('Type 1 and press enter to pressure further about it. Type 2 let it slide and just go with it.')
    if answer=="1":
        print ('')
        asked=1
        #Calls even further and slightly less cryptic answer to who "He" is
        FurtherExplinationBirch()
    elif answer=="2":
        print('')
        #Skips straight to Oasis
        Ritual()
        #Re-Asks the question if the answer is weird
    else:
        print('')
        print ("INVALID ANSWER")
        ExplinationBeforeEncounter()
def FurtherExplinationBirch():
    print('"I would have prefered that he made the introduction but i understand your hesitation"')
    print('"The great one is a God-Tree. A living, breathing, speaking God-Tree"')
    print('"the treeminders are blessed to have this being watch over us"')
    Ritual()
#Finaly getting to Oasis
def Ritual():
    print('')
    print('Once in Oasis, Tree Father Birch says that in order to meet "Him" you must go through the "Ceremony of Purification" and that once you complete it youll be able to speak with "Him"')
    print('After undergoing the "Ceromony of Purification" (because its the only way to move the plot forwards) you momentarily fall unconcious and wake up in a clearing unharmed')
    print('Upon waking up you look around and notice the clearing has a gate around it and there is one big gnarled tree in the middle of the clearing')
    print("")
    answer = input('Type 1 to and press enter to try to leave. Type 2 to and press enter to inspect the strange tree further.')
    if answer=="1":
        print('')
        #Try to leave
        LeaveAttempt()
    elif answer=="2":
        print('')
        #Look at the tree
        Inspection()
        #Re-asks the question again
    else:
        print('')
        print ("INVALID ANSWER")
#Try to leave
def LeaveAttempt():
    print('"Its no use." you hear a strange voice behind you say')
    print('Turning around you realize that the tree has a face')
    #The name is preety self explanatory
    MeetHarrold()
    #Inspect the tree
def Inspection():
    print('Upon taking a closer look at the tree you realise the tree has a face')
    print('Steping closer you can discern the figure of a man in there')
    print('His legs and right arm are rooted to the ground')
    print('His right eye has been sealed shut and his lips apear to have rotted away')
    #Meet the talking tree/guy stuck in a tree
    MeetHarrold()
def Meetharrold():
    print('"Glad to see youre finaly awake, I cant believe they made you do that stupid ceromony" the Tree says"')
    #Harrold conversation path
    HarroldConversation1()
def HarroldConversation1():
    answer = input('Type 1 to say "I must be dreaming". Type 2 to say "Ive never met a talking tree before."')
    if answer=="1":
        print('')
        print('"I wish I was too, Then me and Herbert could be the best of friends and live side by side"')
        print('"Hes the tree, you see. We are old palls... we know each other inside and out; literaly." He says')
    elif answer=="2":
        print('')
        print('"Neither have I. Well, I mean I talk to Bob but he never really says anything back"')
        print('"He kept growing around me, maybe for calling him herbert all the time. His name is actualy Bob. I think its funny when I call him herbert though."')
        HarroldConversationRoute21()
    else:
        print('')
        print ("INVALID ANSWER")
def HarroldConversation21():
    answer = input('Type 1 and press enter to say "So youre traped in there, inside this herbert... I mean Bob thing?". Type and press enter to say "Im begining to suspect that you werent always this way."')
    if answer=="1":
        print('')
        print('"Well I supose you could look at it that way. See, Bob used to ride around on top of my head, sunk his roots right in there, ya know?"')
    elif answer=="2":
        print('')
        Action2()
    else:
        print('')
        print ("INVALID ANSWER")





GameStart()




    

def Action1():
    print('***ACTION 111111111111111111 ERROR***')
def Action2():
    print('***ACTION 222222222222222222 ERROR***')
def UnusedSoFar():


    answer = input('Type 1 to _____. Type 2 to _____.')
    if answer=="1":
        print('')
        Action1()
    elif answer=="2":
        print('')
        Action2()
    else:
        print('')
        print ("INVALID ANSWER")        
    print('')
    print('On arival to their village The Treeminders lead you into the Grove, where they introduce you to a tree named Harold.')
    print('Birch informs you that harrold is the one who asked for you to be brought in')
    print('They all await to see what you chose to say to harrold')
    

