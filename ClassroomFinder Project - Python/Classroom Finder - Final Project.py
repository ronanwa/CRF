#Ronan Wallace
#Final Project - ClassroomFinder

#imports graphics
from graphics import *


#creates a global error message if yes or no is NOT typed
ynErrorMessage="Oops! Try again but answer with yes or no next time! "


#Opens the classes txt file and takes all of the information line by line and creates a global list of that data
classInfo=[line.strip().split(",") for line in open("classes.txt","r")]
#Creates a global list of dictionaries (Teachers are the key and their corresponding item number are the values)
classes=[{i[0]:[i[2]]} for i in classInfo]
#Creates a global list of dictionaries (Item numbers are the key and their corresponding class names are the values)
classNames=[{i[2]:i[1:2]} for i in classInfo]
#Creates a global list of dictionaries (Item numbers are the key and their corresponding room numbers as the values)
roomNumbers=[{int(i[2]):[i[-1]]} for i in classInfo]
#Creates a global list of dictionaries (Item numbers are the key and their corresponding building name as the values)
classLocations=[{i[2]:[i[3]]} for i in classInfo]


#Creates a building class for the class and building names and the item and room numbers (Used in summarizing the location of your chosen class(es))
class location:
    def __init__(self,className,itemNumber,buildingName,roomNumber):
        self.classN=className
        self.itemN=itemNumber
        self.buildingN=buildingName
        self.roomN=roomNumber


#creates main function
def main():
    #Creates initial program description
    print("Welcome to the ClassFinder program! In this program, I will help you find your classroom building and \ngive you the room that it is \
located in. Let's begin, shall we?")
    print("- "*51)
    #Creates empty list for class item numbers
    itemNum=[]
    #Asks user if they remember their class item number
    answer=input("Do you remember your item number? (y/n) ")
    print()
    #calls the classGetter function with the user's input as a parameter in the function
    itemNum.append(classGetter(answer))
    print("\nItem number successfully recorded!")
    print("- -"*34)

    #Sets a condition to 0 for the while loop
    condition1=0
    #ERROR LOOP - While loop will continue to ask the user to type a version of y or no until it is entered.
    #Repeats if y/n is not typed. Loop terminates when y/yes or n/no is entered
    while condition1==0:
        #Asks the user if they would like to find more classes
        answer2=input("Do you have any other classes you'd like to find? (y/n) ")
        print()
        if answer2.lower()=="y" or answer2.lower()=="yes" or answer2.lower()=="n" or answer2.lower()=="no":
            condition1=1
        #If anything other than y/yes or n/no is entered, display an error message
        else:
            print(ynErrorMessage)
            print()

    #If the user says yes, the program will ask if they remember the item number
    while answer2.lower()=="y" or answer2.lower()=="yes":
        condition4=0
        #ERROR LOOP - While loop will continue to ask the user to type a version of y or no until it is entered.
        #Repeats if y/n is not typed. Loop terminates when y/yes or n/no is
        while condition4==0:
            answer3=input("Do you remember your item number? (y/n) ")
            print()
            if answer3.lower()=="y" or answer3.lower()=="yes" or answer3.lower()=="n" or answer3.lower()=="no":
                condition4=1
            else:
                print(ynErrorMessage)
                print()
        #Calls the classGetter function passing in the user's previous answer as a parameter. Returns an item number and appends it
        #to the final list of classes that the user would like to find
        itemNum.append(classGetter(answer3))
        print("\nItem number successfully recorded!")
        print("- -"*35)
        condition2=0
        #ERROR LOOP - While loop will continue to ask the user to type a version of y or no until it is entered.
        #Repeats if y/n is not typed. Loop terminates when y/yes or n/no is
        while condition2==0:
            #Asks user if they want to add another class
            answer2=input("Do you have any other classes you'd like to find? (y/n) ")
            print()
            if answer2.lower()=="y" or answer2.lower()=="yes" or answer2.lower()=="n" or answer2.lower()=="no":
                condition2=1
            else:
                print(ynErrorMessage)
                print()

            
    #If the user says no to finding anymore classes, then the program will begin retrieving the class location images
    if answer2.lower()=="n"or answer2.lower()=="no":
        print("Beginning image process...")
        #Calls the getLocation function, passing in the list of item numbers as the parameter
        buildingLIST=getLocation(itemNum)
        clsName=[]
        roomNums=[]

        #Creates a list of the desired class names - iterates through the list of dictionaries and iterates through the contents of those dictionaries
        for i in classNames:
            #Iterates through the keys of those dictionaries
            for key in i.keys():
                #Assigns the current key to a variable
                classNum=int(key)
                #Iterates through the range of the length of the list
                for j in range(len(itemNum)):
                    #If the current item number in itemNum is equal to the item number in classNum, then retrieve
                    #the values of that dictionary
                    if itemNum[j]==classNum:
                        for value in i.values():
                            for x in value:
                                clsName.append(x)
                                
        #Creates a list of the room numbers that correlate with the desired classrooms - iterates through the list of dictionaries and iterates
        #through the contents of those dictionaries
        for s in roomNumbers:
            #Iterates through the keys of those dictionaries
            for key in s.keys():
                #Assigns the current key to a variable
                classNum=int(key)
                #Iterates through the range of the length of the list
                for n in range(len(itemNum)):
                    #If the current item number in itemNum is equal to the item number in classNum, then retrieve
                    #the values of that dictionary
                    if itemNum[n]==classNum:
                        for value in s.values():
                            for p in value:
                                roomNums.append(p)
                                
        #Displays the campus images of every desired class in a seperate window - Info of the class is given in the name of the graphic window                      
        for d in range(len(buildingLIST)):
            displayClassLocation(buildingLIST[d],clsName[d],roomNums[d])
            
    print("Process Completed!")
    print()

    #Displays a summary of the desired classes
    summarizeInfo(clsName,itemNum,buildingLIST,roomNums)
    print("\nAll done! Your class locations have been displayed. Thanks for using ClassFinder! :)")

#Displays the information of the class and where the class is located
def summarizeInfo(className,itemNumber,buildingName,roomNumber):
    print("Class Summary:")
    for i in range(len(className)):
        summary=[]
        #Uses the location class to create a list of information about each college course
        summary.append(location(className[i],itemNumber[i],buildingName[i],roomNumber[i]))
        #Determines whether the class is online, arranged, off-campus, or normal. Displays info accordingly using the location class
        for j in range(1):
            if summary[j].roomN=="ONL":
                print(">",summary[j].classN,"is an online class and does not meet at any location.")
            elif summary[j].roomN=="ARR":
                print(">",summary[j].classN,"is an arranged course. Contact your instructor for information on the location.")
            elif summary[j].buildingN=="CTC":
                print(">",summary[j].classN,"is not located at Clark College campus. It is located at the Columbia Tech Center.")
            else:
                print(">",summary[j].classN,"is located in building",summary[j].buildingN,"in room","#"+str(summary[j].roomN))

#Function that returns a list of building names according to the item number list (user input)    
def getLocation(itemNum):
    buildingList=[]
    #Iterates through the list of dictionaries (Uses the class locations list)
    for a in classLocations:
        #Iterates through the keys of those dictionaries
        for key in a.keys():
            #Assigns the current key to a variable
            classNum=int(key)
            #Iterates through the range of the length of the list "teacherNums"
            for b in range(len(itemNum)):
                #If the current item number in teacherNums is equal to the item number in classNum, then retrieve
                #the values of that dictionary and append them to the empty list "classNameList"
                if itemNum[b]==classNum:
                    for value in a.values():
                        for y in value:
                            buildingList.append(y)
    return buildingList


#Function that gets information from the user. Goes through a series of questions to help the user remember his item number and returns the item number
def classGetter(answer):
    #The program will continue to ask the user to enter yes or no if they do not enter y, yes, n, or no
    #(while answer doesnt equal, give oops message)
    while answer.lower()!="y" and answer.lower()!="yes" and answer.lower()!="n" and answer.lower()!="no":
        print(ynErrorMessage)
        print()
        answer=input("Do you remember your item number? (y/n) ")
        print()
    #If answer equals y/yes, user inputs the remembered item number. 
    if answer.lower()=="y"or answer.lower()=="yes":
        itemNum=input("What is your class item number? ")
        print()
        #Calls itemNumChecker function
        checkedNumber=itemNumChecker(itemNum)
        #Returns the verified item number
        return checkedNumber
    #If answer equals n/no, ask the user for the teacher they are enrolled with
    elif answer.lower()=="n"or answer.lower()=="no":
        teacher=input("Oh shoot! Let's see if we can rejog your memory. Who is your teacher? \n(Last name) ")
        teacher=teacher.lower()
        print()
        #Creates an empty list to append the teacher item numbers into
        teacherNums=[]

        #Error proof teacher name input
        condition3=0
        while condition3==0:
            #Iterates through the classes list
            for i in classes:
                #Iterates through all of the keys in the dictionaries and assigns the current key to teacherName
                for key in i.keys():
                    teacherName=key
                    #If the current key is equal to the user input of their teacher's name then iterate through the
                    #values of that key and store them in a list
                    if teacherName==teacher:
                        for value in i.values():
                            #Required because the value type is one list, this for loop iterates through that list
                            #and appends the integers into a list
                            for x in value:
                                teacherNums.append(int(x))
            #Error proof - displays error message if the typed professor is not found
            if teacherNums==[]:
                teacher=input("Oh shoot! Looks like that teacher doesn't exist in our data, try a professor that will be teaching in winter quarter at Clark College! \n(Last name) ")
                teacher=teacher.lower()
                print()
            else:
                condition3=1
                        
        #Displays a header for the classes that are taught by a professor
        print("Here are some class taught by Professor",teacher.title())
        #Creates an empty list to append the class names into
        classNameList=[]

        #Iterates through the list of dictionaries
        for i in classNames:
            #Iterates through the keys of those dictionaries
            for key in i.keys():
                #Assigns the current key to a variable
                classNum=int(key)
                #Iterates through the range of the length of the list "teacherNums"
                for j in range(len(teacherNums)):
                    #If the current item number in teacherNums is equal to the item number in classNum, then retrieve
                    #the values of that dictionary and append them to the empty list "classNameList"
                    if teacherNums[j]==classNum:
                        for value in i.values():
                            for x in value:
                                classNameList.append(x)

        #Loops the range of the length of the list "teacherNums"; Displays the class name and the corresponding item
        #number for the user to recognize which class he is taking. They will then input that number in the next step
        for i in range(len(teacherNums)):
            variableA=classNameList[i]
            variableB=teacherNums[i]
            dash="-"
            print(variableA,dash,variableB)
        print()
            
        #Asks for which item number that corresponds with the class that they are taking
        itemNum=input("What is your class item number? ")
        #Checks the user input to make sure that the input is 1) a number and not "dfghj" and 2) to make sure it's at the correct length
        checkedIN=itemNumChecker(itemNum)
        #Returns item number
        return checkedIN


#This function checks the specifications of the item number user input. Makes sure that it is a four digit integer (Item number format)
def itemNumChecker(itemNum):
    #Creates a while loop to continuously ask for an input until the specifications of the input is met (A four digit "item number" must be entered)
    while type(itemNum)!=type(8):
        #Try evaluating the integer. (Strings cannot be evaluated)
        try:
            itemNum=eval(itemNum)
            #If first try is successful, check to see if the input is four consecutive integers
            while len(str(itemNum))!= 4:
                print()
                #If the length of the item number does not equal four, display an error message asking the user to re-enter the item number
                itemNum=input("Try entering a four digit integer! What is your class item number? ")
        #If try fails because it is not a number, display an error message asking for another input
        except:
            print()
            itemNum=input("Try entering a four digit integer! What is your class item number? ")
    #Repeats while loop until the specifications of the number is met. Finally, the function returns the verified number
    return itemNum


#This function will retieve the correct images of the classroom location based on the item numbers given by the user
def displayClassLocation(buildingName,className,roomNumber):
    #If the class is an online course, the program will notify the user
    if roomNumber=="ONL":
        className=className+" - There is no location for this classroom"
    #If the class is an arranged course, the program will notify the user
    elif roomNumber=="ARR":
        className=className+" - The location of this classroom will be given by your instructor"
    #If roomNumber is anything else, the program will treat it as a normal class
    else:
        className=className+" Location - Room Number: "+roomNumber
    #Creates a window to use (800*800 pixels)
    win=GraphWin(className,800,800)
    #Sets coordinates for ease of use
    win.setCoords(0,0,8,8)
    #Constructs the file name ("blank.png")
    buildingName=buildingName+".png"
    #Displays the image (campus map with class location)
    image=Image(Point(4,4),buildingName)
    image.draw(win)

main()

