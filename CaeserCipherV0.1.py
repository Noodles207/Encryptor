encodeDict = {
    'a' : 'u',
    'b' : 'v',
    'c' : 'w',
    'd' : 'x',
    'e' : 'y',
    'f' : 'z',
    'g' : 'a',
    'h' : 'b',
    'i' : 'c',
    'j' : 'd',
    'k' : 'e',
    'l' : 'f',
    'm' : 'g',
    'n' : 'h',
    'o' : 'i',
    'p' : 'j',
    'q' : 'k',
    'r' : 'l',
    's' : 'm',
    't' : 'n',
    'u' : 'o',
    'v' : 'p',
    'w' : 'q',
    'x' : 'r',
    'y' : 's',
    'z' : 't',
}
decodeDict = {
    'u' : 'a',
    'v' : 'b',
    'w' : 'c',
    'x' : 'd',
    'y' : 'e',
    'z' : 'f',
    'a' : 'g',
    'b' : 'h',
    'c' : 'i',
    'd' : 'j',
    'e' : 'k',
    'f' : 'l',
    'g' : 'm',
    'h' : 'n',
    'i' : 'o',
    'j' : 'p',
    'k' : 'q',
    'l' : 'r',
    'm' : 's',
    'n' : 't',
    'o' : 'u',
    'p' : 'v',
    'q' : 'w',
    'r' : 'x',
    's' : 'y',
    't' : 'z',
}

def decoder(encoded : str,decodeTool : dict) -> str: #uses decodeTool to let you swap out dictionaries or use different ones in different calls of the function if you use this anywhere else.
    '''Decodes a message using the given dictionary.'''
    decoded = ""
    for character in encoded.lower():
        if character in decodeTool:
            decoded += decodeTool[character] #appends the current char, but filtered through the decoder.
        elif character == '/': #turns slashes back into spaces
            decoded += ' '
    return decoded
def encoder(unEncoded : str,encodeTool : dict) -> str:
    '''Encodes a message with the given dictionary.'''
    encoded = ""
    for character in unEncoded.lower():
        if character in encodeTool:
            encoded += encodeTool[character] #appends the current character, filtered through the encoder
        elif character == ' ': #replaces spaces with slashes for more confusion
            encoded += '/'
    return encoded

runningFlag = True #just setting up the while loop
while runningFlag == True:
    userChoice = ""
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
        print(encoder(input("What message do you want to encode?\n"),encodeDict)) #just do the input INSIDE the function because we roll close to the error's edge like that.
    elif userChoice == "d" or userChoice == "D": #decoding
        print("Decoding selected!")
        print(decoder(input("What message do you want decoded?\n"),decodeDict))
    elif userChoice == "!q" or userChoice == "!Q": #quitting the program
        print("Goodbye, have a nice day!")
        runningFlag = False #this exits the loop.
    else:
        print("Something's very wrong here in the userChoice parser, so i'll just crash.") #Error? Don't keep going - just CRASH!
        int("DIE PROGRAM DIE") #(evil laughter after this)