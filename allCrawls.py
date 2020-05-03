from igramscraper.instagram import Instagram # pylint: disable=no-name-in-module
from time import sleep
from crawl import storenew_html, append_html, getAllFollowers
import os

instagram = Instagram()
instagram.with_credentials('', '') 
instagram.login()

seed = 'birrellsamantha'
print(len(seed))

account = instagram.get_account(seed)

counter = 399



followers = instagram.get_followers(account.identifier, 1000, 150, delayed=True) # Get 150 followers of 'kevin', 100 a time with random delay between requests


filepath = "/Users/Bluck/Documents/GitHub/instagram-scraper/Data/" +  str(counter) + ".txt"

    
storenew_html("UserName: " + seed +  " Count: " +  str(account.followed_by_count) + "\nFollowers:\n", counter)


for follower in followers['accounts']:
        append_html(follower.username , counter)



while counter < 1000:
    file = open(filepath, "r")
    
    while True:

        username = file.readline().rstrip()
        
        
        if "UserName:" in username:
            username = file.readline().strip()
        if "Followers:" in username:
            username = file.readline().strip()
        if " " in username:
            username = file.readline().strip()
        if not username:
            break
       
        #print(username)
        account = instagram.get_account(username)
        followers = instagram.get_followers(account.identifier, 1000, 150, delayed=True)
        counter += 1

        sleep(2) # Delay to mimic user
    
        storenew_html("UserName: " + username +  " Count: " +  str(account.followed_by_count) + " \nFollowers:\n", counter)

        for follower in followers['accounts']:
                append_html(follower.username , counter)
    