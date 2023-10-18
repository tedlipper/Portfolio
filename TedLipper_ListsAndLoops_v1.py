#Prints ten numbers from the fibinachi sequence with a loop
print("Prints ten numbers from the fibinachi sequence with a loop")
A=1
B=1
X=10
print(A)
print(B)
while X>0:
    print(A+B)
    A=A+B
    print(A+B)
    B=A+B
    X=X-1


print("")
#Makes a list from 0 to 26
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
#Makes a list from 0 to 26 in an easier way
numbers2= list(range(27))
#Makes a list of all of the numbers in the aphabet
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ,"K", "L" ,"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
#Prints the length of the numbers list
print("Prints the length of the numbers list")
print(len(numbers))
print("")

#Prints the length of the letters list
print("Prints the length of the letters list")
print(len(letters))
print("")

#Prints the numbers list
print("Prints the numbers list")
print(numbers)
print("")

#Prints the other numbers list
print("Prints the other numbers list")
print(numbers2)
print("")

#Prints the letters list
print("Prints the letters list")
print(letters)
print("")

#Prints the numbers in between 7 and 12
print("Prints the numbers in between 7 and 12")
print(numbers[7:13])
print("")

#Prints the Numbers between 18 and 20
print("Prints the Numbers between 18 and 20")
print(numbers2[18:21])
print("")

#Prints every other number
print("Prints every other number")
print(numbers[::2])
print("")

#Prints every third number
print("Prints every third number")
print(numbers[::3])
print("")

#Prints every fifth number
print("Prints every fifth number")
print(numbers[::5])
print("")

#Says hello world using the letters list
print("Says hello world using the letters list")
print(letters[7]+letters[4]+letters[11]+letters[11]+letters[14]+letters[26]+letters[-5]+letters[-13]+letters[-10]+letters[-16]+letters[3])
print("")




