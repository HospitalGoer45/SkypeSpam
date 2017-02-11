from skpy import Skype
import time
print "This will get you a temporary ban from sending messages if used for too long. I suggest use for less than 10 minutes at a time"

sk = Skype(raw_input("Username: "), raw_input("Password: ")) # connect to Skype

ch = sk.contacts[raw_input("Contact Name: ")].chat

mess = raw_input("Desired Message: ")

i = 0

while 1:	
	if i%15 == 0:
		print "sent ", i, " messages"
		time.sleep(5.5)
	i = i + 1
	ch.sendMsg(mess) # plain-text message
	time.sleep(.001)
	print mess
