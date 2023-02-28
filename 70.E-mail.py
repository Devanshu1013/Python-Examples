import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('devpraja101@gmail.com','DevPraja@101')
message = "Oyy Chutia \n shu karu chu baby"
server.sendmail('devpraja101@gmail.com','jdbharadva2002@gmail.com',message)

print("message Send")