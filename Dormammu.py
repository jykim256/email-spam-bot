import time,smtplib,random
from tqdm import tqdm
from spamText import text

email = 'YOUR GMAIL HERE'
receive = 'TARGET EMAIL HERE'
ps = 'FIND THIS OUT THROUGH GMAIL SETTINGS'
num_of_emails = 150

# initialize smtp object and log in
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(email,ps)
# iterate through spam
# replace subject and content
# tqdm helps visualize the emails being sent
for i in tqdm(range(num_of_emails)):
	print(i)
	subject = 'Subject: Dormammu id=' + str(random.randint(10**40,10**50)) + ','
	content = 'I\'ve come to bargain.\n' + text + text+'\n\n\n\n-------------\nWith Kindest Regards,\nBee. Obama'
	smtpObj.sendmail(email,receive, subject + '\n' + content)
	time.sleep(2)
smtpObj.quit()