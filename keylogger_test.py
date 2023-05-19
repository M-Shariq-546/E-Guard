#!/usr/bin/env python3
import smtplib
import time


def mail_it():
    from_address = "Shariqhacker55@gmail.com"
    from_address_password = "Shariq@555"
    to_list = ["Shariqhacker55@gmail.com"]
    message = 'Message!'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_address, from_address_password)
    server.sendmail(from_address, to_list, message)
    server.close()


times_run = 10

while times_run > 0:
    mail_it()
    print(f'Sent email # {times_run}')
    time.sleep(5)
    times_run -= 1
