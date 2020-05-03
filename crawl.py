from igramscraper.instagram import Instagram # pylint: disable=no-name-in-module
from time import sleep
import os
import random

#create the file for storing parsed html text
def storenew_html(text, fileName):
    #combine filepath name with newly created file
    filepath = os.path.join('/Users/Bluck/Documents/GitHub/instagram-scraper/Data', (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists('/Users/Bluck/Documents/GitHub/instagram-scraper/Data'):
         #if directory does not exist then create it
        os.makedirs('/Users/Bluck/Documents/GitHub/instagram-scraper/Data')
    #create the file    
    parsedFile = open(filepath, "w")
    parsedFile.write(text)
    parsedFile.close()

#append to the file for storing parsed html text
def append_html(text, fileName):
    #combine filepath name with newly created file
    filepath = os.path.join('/Users/Bluck/Documents/GitHub/instagram-scraper/Data', (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists('/Users/Bluck/Documents/GitHub/instagram-scraper/Data'):
         #if directory does not exist then create it
        os.makedirs('/Users/Bluck/Documents/GitHub/instagram-scraper/Data')
    #create the file    
    parsedFile = open(filepath, "a")
    #print(text)
    parsedFile.write(text + "\n")
    parsedFile.close()

def getAllFollowers(followers, counter, profile):
    

    









