from encryptorDicts import lKNVDict,nKLVDict

def encode(message : str,passWord : str) -> str:
    '''encodes a message using the given password'''
    encodedMsg = ""
    message = message.lower()
    passStepper = 0
    for currentMsgChar in message:
        if currentMsgChar in lKNVDict:
            keyShiftVal = lKNVDict[passWord[passStepper]]
            currentEncodedChar = lKNVDict[currentMsgChar]+keyShiftVal
            if currentEncodedChar > 26:
                currentEncodedChar -= 26
            currentEncodedChar = nKLVDict[currentEncodedChar]
            encodedMsg += currentEncodedChar
            passStepper += 1
            if passStepper > len(passWord)-1:
                passStepper = 0
        else:
            encodedMsg += currentMsgChar
    return encodedMsg

def decode(message : str,passWord : str) -> str:
    '''encodes a message using the given password'''
    decodedMsg = ""
    message = message.lower()
    passStepper = 0
    for currentMsgChar in message:
        if currentMsgChar in lKNVDict:
            keyShiftVal = lKNVDict[passWord[passStepper]] #I'll be strictly honest here,
            currentDecodedChar = lKNVDict[currentMsgChar]-keyShiftVal #I don't know how ANY OF THIS WORKS!
            if currentDecodedChar <= 0:
                currentDecodedChar += 26
            currentDecodedChar = nKLVDict[currentDecodedChar] #but it does its job w/o a fuss so i'll leave it like that.
            decodedMsg += currentDecodedChar
            passStepper += 1
            if passStepper > len(passWord)-1:
                passStepper = 0
        else:
            decodedMsg += currentMsgChar
    return decodedMsg

runningFlag = True #just setting up the while loop
while runningFlag == True:
    userChoice = "F"
    print("Hello! (e)ncode or (d)ecode? !q to quit.")
    userChoice = input()
    choiceValid = False
    while choiceValid == False:  #case handling, incorrect input handling
        if userChoice == 'e' or userChoice == 'E' or userChoice == 'd' or userChoice == 'D' or userChoice == '!q' or userChoice == '!Q':
            #egregiously long case checklist in the line above to verify if the choice is valid.
            #also, this is up here because choiceValid would still be False when the loop is first entered.
            choiceValid = True
        if choiceValid == False: #Now it won't print the error message if the stuff is right.
            print("That's not right! Use e to encode, or d to decode! !q to quit!") #error message, try again
            userChoice = input()
    if userChoice == "e" or userChoice == "E": #encoding
        print("Encoding selected!")
        print(encode(input("What message do you want to encode?\n"),input("What password do you want?\n"))) #just do the input INSIDE the function because we roll close to the error's edge like that.
    elif userChoice == "d" or userChoice == "D": #decoding
        print("Decoding selected!")
        print(decode(input("What message do you want decoded?\n"),input("What password do you want?\n")))
    elif userChoice == "!q" or userChoice == "!Q": #quitting the program
        print("Goodbye, have a nice day!")
        runningFlag = False #this exits the loop.
    else:
        print("Something's very wrong here in the userChoice parser, so i'll just crash.") #Error? Don't keep going - just CRASH!
        int("DIE PROGRAM DIE") #(evil laughter after this)