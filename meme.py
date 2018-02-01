"""
this is very important program
meme.py
github.com/waaaldemar
"""

import random
import os
import csv
import re
import sys
from twython import Twython

def startProgramQuestion():
    startProgramAgain = True
    while startProgramAgain is True:
        startProgram = input("Start program? y/n: ")

        if startProgram == "y":
            pass
            startProgramAgain = False
        elif startProgram == "n":
            print("Exiting program..")
            sys.exit(0)
        else:
            print("Sorry I dont understand")
            startProgramAgain = True

startProgramQuestion()

def createMemes():

    # create txt
    memeTextCreate = open("text.txt", "w")
    memeTextCreate.write("mood\n")
    memeTextCreate.write("this is so me\n")
    memeTextCreate.write("LMAO Who did this\n")
    memeTextCreate.write("LMAOooo\n")
    memeTextCreate.write("I hate this pic\n")

    memeTextCreate.close()

    # create list of very funny things
    l1 = "i see myself in the mirror"
    l2 = "i hit my toe"
    l3 = "mom is mad at me"
    l4 = "i program useless things"
    l5 = "i have to clean my room"
    l6 = "i see my dog"
    l7 = "i see my mom"

    mfwList = ([l1,l2,l3,l4,l5,l6,l7])

    # create funny mfw-memes (i know they are not that funny relax)
    mfwChoice1 = random.choice(mfwList)
    mfwFull1 = ("mfw ",mfwChoice1)
    mfwFullFixed1 = ''.join( c for c in mfwFull1 if c not in "''(),?:!/;" )

    mfwChoice2 = random.choice(mfwList)
    mfwFull2 = ("mfw ",mfwChoice2)
    mfwFullFixed2 = ''.join( c for c in mfwFull2 if c not in "''(),?:!/;" )

    mfwChoice3 = random.choice(mfwList)
    mfwFull3 = ("mfw ",mfwChoice3)
    mfwFullFixed3 = ''.join( c for c in mfwFull3 if c not in "''(),?:!/;" )

    # write it to txt
    memeText = open("text.txt", "a")
    memeText.write(mfwFullFixed1)
    memeText.write("\n")
    memeText.write(mfwFullFixed2)
    memeText.write("\n")
    memeText.write(mfwFullFixed3)
    memeText.write("\n")

    memeText.close()

createMemes()

def main():

    textSelectionAgain = True
    while textSelectionAgain is True:

        # select meme text / make file in to a list
        memeText2 = []
        with open("text.txt", newline="") as inputfile:
            for row in csv.reader(inputfile):
                memeText2.append(row)
        inputfile.close()

        # choose the text from a list
        textSelection = random.choice(memeText2)
        # Make it into a clean string
        textSelectionFixed = ''.join( c for c in textSelection if c not in "''(),?:!/;" )
        print(textSelectionFixed)

        # check used text from txt file
        usedTextCheck = open("used_text.txt", "r")
        usedTextString = usedTextCheck.read()
        # print(usedTextString)

        # check has the text been used before
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(textSelectionFixed), usedTextString))

        if count >= 1:
            print("count equals 1 or more")
            textSelectionAgain = True
            print("Going back")

        else:
            print("All worked according to plan")
            textSelectionAgain = False

        usedTextCheck.close()

    # check used images from txt file
    usedImagesCheck = open("used_img.txt", "r")
    usedImagesString = usedImagesCheck.read()

    picSelectionAgain = True
    while picSelectionAgain is True:

        # select picture
        picSelection = random.choice(os.listdir("path/to/your/img"))
        print(picSelection)

        # check has the img been used before
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(picSelection), usedImagesString))
        # print(count)
        if count >= 1:
            # print("count equals 1 or more")
            picSelectionAgain = True

        else:
            # print("All worked according to plan")
            picSelectionAgain = False

            # print(picSelection)
            openPicCmd = ("gpicview img/"+picSelection)
            os.system(openPicCmd)
            
    tweetMeme = True
    while tweetMeme is True:
        tweetMemeQuestion = input("Tweet meme? y/n: ")

        if tweetMemeQuestion == "y":
            #pass
            tweetMeme = False
        elif tweetMemeQuestion == "n":
            print("Exiting program..")
            return main()
            
        else:
            print("Sorry I dont understand")
            tweetMeme = True

    # tweet the maymay
    APP_KEY = ""
    APP_SECRET = ""
    OAUTH_TOKEN = ""
    OAUTH_TOKEN_SECRET = ""

    twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    
    picSelectionWithDir = "img/"+picSelection
    
    TweetPhoto = picSelectionWithDir
    photo = open(TweetPhoto,"rb")
    
    twitter.update_status_with_media(media=photo,status=textSelectionFixed)
    
    # write used text to txt
    usedtextSelection = open("used_text.txt", "w")
    usedtextSelection.write(textSelectionFixed)
    usedtextSelection.write("\n")
    usedtextSelection.close()

    # write the img name to file so you dont use it again
    usedImages = open("used_img.txt", "a")
    usedImages.write(picSelection)
    usedImages.write("\n")
    usedImages.close()

main()
