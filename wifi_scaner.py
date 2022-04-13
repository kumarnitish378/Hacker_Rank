from subprocess import  check_output
from os import startfile
def wifi_network_name(out):
    File=[]
    for i in range (len(out)):
          File.append(chr(out[i]))
    data = ""
    for j in File:
        if j != "":
            data = data+j
    File =[]
    File.append(data.replace("\r\n",""))
    a = File[0]
    b = list(map(str, a.split("All User Profile     :")))
    File = []
    for i in b[2::]:
        File.append(i.replace(" ","*"))
    return File

def plain_text(out): # this function convert byte data to string data
    data = ""
    for i in range(len(out)):
        data = data+chr(out[i])
    return data
def password(lst):
    for i in lst:
        a = i[::-1]
        a = a[2::]
        a = a[::-1]
        com = "netsh wlan show profiles "+a
        com = com+" key=clear"
        print(com)
        a = ""
def password1(a):
    lst =[]
    if "Key Content  " in a:
        passw = a[a.index("Key Content    "):a.index("Key Content  ") + 40:]
        passw = passw.replace("Key Content          ", "Password ")
        passw = passw.replace("\\r\\n", "")
        passw = passw.replace("\\", "")
        lst.append(passw)
    if "SSID name              :" in a:
        lst.append(a[a.index("SSID name    "):a.index("SSID name    ") + 40:])
    return lst
# command = str(input("$ "))
command = "netsh wlan show profiles"
a = check_output((command), shell=True)
if command == "netsh wlan show profiles":
    lst = wifi_network_name(a)
    for i in lst:
        b = "netsh wlan show profiles "+i+" key=clear"
        b = check_output(b, shell=True)
        print(plain_text(b),file=open("wifi_details.txt",'a'))
        # print(password1(str(b)))
else:
    print(plain_text(a))
startfile("wifi_details.txt")
exit(0)
