#Hello world function definition
def Howdy():
    #Hello world print
    print ("Howdy")
#Hello world function call
Howdy()
#Adding function that adds both numbers and words
def Adds(input1 , input2):
    print(input1 + input2)
#Testing different kinds of inputs with a function call
Adds(2,3)
Adds("two","three")
#Defining function
def GoBackTo2016():
    #Defining the shame message
    ShameMessage = "Bro look at this fukin dumbass UwU"
    #Statement to set answer variable to input and ask for input after asking input question
    answer = input("Whats 9 + 10:")
    #Checking if answer is 21 and printing "Noice" if it is
    if answer=="21":
        print ("Noice")
    #Shaming the the user for not recognizing an old meme
    else: print (ShameMessage)
#Calling the function
GoBackTo2016()
