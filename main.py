import subprocess
import webbrowser
from ursina import *
import threading
import os
import paramiko
import tkinter as tk



#_____IP SetUp______
IP = ''
root = tk.Tk()
ip = tk.Entry(root,width=50)
ip.pack()
def ip_GET():
    global IP
    IP = ip.get()
    root.destroy()
sub_but = tk.Button(root,text = 'set IP',command = ip_GET)
sub_but.pack()
root.mainloop()




#Check If Server Is OnLine
McS = paramiko.SSHClient()
McS.set_missing_host_key_policy(paramiko.AutoAddPolicy)
on = False
try:
    McS.connect(IP,username='idochen',password='123456789',timeout=3)
    stdin, stdout, stderr = McS.exec_command('cat isiton.txt')
    out = stdout.read()
    if out == b'ON\n':
        on = True
        print('nocie')
    else:
        on = False
        print('not noice')
except:
    'NON'



#stdin, stdout, stderr = McS.exec_command('cat isiton.txt')
#out = stdout.read()
#if out == b'ON\n':
    #print('nocie')
#else:
    #print('not noice')


#Main GUI/ Ursina
app = Ursina()
load_texture('bg','assets\\bg.gif')
load_texture('but','assets\\but.png')

esegg = 0
def input(key):
    global ONorOFF, esegg
    if starMD.hovered:
        if key == 'left mouse down':
            ONorOFF += 1
            #SF3.enable()
            #EN2.enable()
    if SF3.hovered:
        if key == 'left mouse down':
            print_on_screen('Starting...',duration=3,position=(-0.05,0,-0.1))
            threading.Thread(target=start_SF3Server).start()
    if EN2.hovered:
        if key == 'left mouse down':
            print_on_screen('Starting...', duration=3, position=(-0.05, 0, -0.1))
            threading.Thread(target=start_EN2Server).start()
    if starVN.hovered:
        if key == 'left mouse down':
            print_on_screen('Starting...', duration=3, position=(-0.05, 0, -0.1))
            threading.Thread(target=start_VNServer).start()
    if turnOFF.hovered:
        if key == 'left mouse down':
            server_ONLINE()
            ShutDown()
    if KillAll.hovered:
        if key == 'left mouse down':
            threading.Thread(target=Kill_All).start()
    if startNG.hovered:
        if key == 'left mouse down':
            threading.Thread(target=start_NGrock).start()
    if ServerON.hovered:
        if key == 'left mouse down':
            threading.Thread(target=server_ONLINE).start()
    if esg.hovered:
        if key == 'left mouse down':
            esegg += 1


clock = 0
ONorOFF = 0
def update():
    global clock,ONorOFF,esegg
    if ONorOFF == 0:
        SF3.disable()
        EN2.disable()
    if ONorOFF == 1:
        SF3.enable()
        EN2.enable()
    if ONorOFF > 1:
        ONorOFF = 0
    clock += 1 * time.dt
    if on == False:
        if clock >= 30:
            print('checked if Server Online')
            print(clock)
            clock = 0
            threading.Thread(target=server_ONLINE).start()
    if on == True:
        ServerON.color = color.rgb(110, 174, 0)
        ServerON.text = 'ON'
    if on == False:
        ServerON.color = color.rgb(237, 40, 0)
        ServerON.text = 'OFF'





def server_ONLINE():
    global on
    try:
        McS.connect(IP, username='idochen', password='123456789', timeout=3)
        stdin, stdout, stderr = McS.exec_command('cat isiton.txt')
        out = stdout.read()
        if out == b'ON\n':
            on = True
        else:
            on = False
    except:
        'sex'

def ShutDown():
    try:
        McS.connect(IP, username='idochen', password='123456789', timeout=3)
        stdin, stdout, stderr = McS.exec_command('echo 123456789 | sudo -S shutdown -h now')
    except:
        'nice'

def start_SF3Server():
    #subprocess.call([r'C:\Minecraft Server Runner\SF3.bat'])
    os.system('cmd /k "plink -batch idochen@' + IP + '-pw 123456789 bash StartSF3.sh')

def start_EN2Server():
    #subprocess.call([r'C:\Minecraft Server Runner\EN.bat'])
    os.system('cmd /k "plink -batch idochen@'+IP+'-pw 123456789 bash runserver.sh')

def start_VNServer():
    #subprocess.call([r'C:\Minecraft Server Runner\runVanilla.bat'])
    os.system('cmd /k "plink -batch idochen@' + IP + '-pw 123456789 bash RunVanillaServer.sh')

def start_NGrock():
    webbrowser.open("https://dashboard.ngrok.com/endpoints/status", new=1)
    #subprocess.call([r'C:\Minecraft Server Runner\ngrokstarter.bat'])
    os.system('cmd /k "plink -batch idochen@' + IP + '-pw 123456789 bash ng.sh')

def Kill_All():
    #subprocess.call([r'C:\Minecraft Server Runner\KILL\KillAlll.bat'])
    os.system('cmd /k "plink -batch idochen@' + IP + '-pw 123456789 killall5 -9')

def start_Filezilla():
    os.startfile('C:\Program Files\FileZilla FTP Client\\filezilla.exe')




headline = Text('Minecraft Dashboard',color=color.black,font = 'assets\Minecrafter.Alt.ttf',scale = (3,3),position= (-0.47,0.4))
Credit = Text('Made By Ido Chen',font = 'assets\Minecrafter.Alt.ttf',scale = (1,1),color = color.yellow,position= (-0.4,0.32))
starMD = Button('Start MD Server',texture = 'but', scale=(0.3,0.07),color = color.white, y=.2, x=-.31 )
starVN = Button('Start VN Server', scale=(0.3,0.07), color=color.white, y=.09, x=-.31,texture = 'but' )
turnOFF = Button("(|)", scale=(0.06,0.06), color=color.red, y=-.47, x=-.11,texture = 'but' )
KillAll = Button('KILL ALL', scale=(0.3,0.07), color=color.white, y=-.02, x=-.31,texture = 'but' )
startNG = Button('Ngrok', scale=(0.15,0.1), color=color.white, y=-.45, x=.57,texture = 'but')
startFZ = Button('Files', scale=(0.15,0.1), color=color.white, y=-.45, x=.42,on_click = start_Filezilla,texture = 'but')
SF3 = Button('SF3' ,scale=(0.1,0.1), color=color.black, position=(-.1,.2), enabled = False,texture = 'but')
EN2 = Button('EN2' ,scale=(0.1,0.1), color=color.black , position=(.01,.2), enabled = False,texture = 'but')
esg = Button(scale=(0.03,0.03), position=(.42,.2),visible = False)
#bg = Entity(model = 'quad',scale=(25,15),texture='bg', position=(-.22,1.5,0.1))
a = Animation('assets\\bg.gif',scale = (17,13))
ServerON = Button('OFF' ,scale=(0.5,0.05), color=color.red , position=(-.39,-.47),texture = 'but')
IP_GUI = Text('ip = '+IP,position=(-.61,-.40))

window.size = (900,700)
window.borderless = False
window.center_on_screen()


app.run()