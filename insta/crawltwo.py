from igramscraper.instagram import Instagram

instagram = Instagram()

# authentication supported
instagram.with_credentials('', '')
instagram.login()

#Getting an account by id
account = instagram.get_account('bluck')

# Available fields
'''print('Account info:')
print('Id: ', account.identifier)
print('Username: ', account.username)
print('Full name: ', account.full_name)
print('Biography: ', account.biography)

print('External Url: ', account.external_url)
print('Number of published posts: ', account.media_count)
print('Number of followers: ', account.followed_by_count)
print('Number of follows: ', account.follows_count)
print('Is private: ', account.is_private)
print('Is verified: ', account.is_verified)'''

followers = instagram.get_followers(account.identifier, 90, 90, delayed=True)
for follower in followers['accounts']:
        print('bluck ', follower.username)

account = instagram.get_account('erick.rojas.988')
followers = instagram.get_followers(account.identifier, 90, 90, delayed=True)
for follower in followers['accounts']:
        print('eric ', follower.username)




# or simply for printing use 
#print(account)