# Python-RAT
Remote Administration tool for Windows Systems written in pure Python

## Disclamer

THIS SOFTWARE IS INTENDED ONLY FOR EDUCATION PURPOSES! DO NOT USE IT TO INFLICT 
DAMAGE TO ANYONE! USING MY APPLICATION YOU ARE AUTHOMATICALLY AGREE WITH ALL RULES AND
TAKE RESPONSIBITITY FOR YOUR ACTION! THE VIOLATION OF LAWS CAN CAUSE SERIOUS CONSEQUENCES!
THE DEVELOPER FZGbzuw412 ASSUMES NO LIABILITY AND IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE 
CAUSED BY THIS PROGRAM.

## Intended for:
Windows systems

## Requirements
+ Pillow
+ pywin32
+ opencv-python
+ comtypes
+ pycaw
+ pyautogui

## Usage for server
```
#clone or download zip archive
https://github.com/FZGbzuw412/Python-RAT

#go to directory with files
cd Python-RAT 

#launch 
server.py
```

## Usage for client
```
#clone or download zip archive
https://github.com/FZGbzuw412/Python-RAT

#go to directory with files
cd Python-RAT

#install essential requirements
pip3 install -r client_requirements.txt

#launch 
client.pyw
```

##Features

System:
<br/>
help                      all commands available
writein <text>            write the text to current opened window
browser                   enter quiery to browser
turnoffmon                turn off the monitor
turnonmon                 turn on the monitor
reboot                    reboot the system
drivers                   all drivers of PC
kill                      kill the system task
sendmessage               send messagebox with the text
cpu_cores                 number of CPU cores
systeminfo (extended)     all basic info about system (via cmd)
tasklist                  all system tasks
localtime                 current system time
curpid                    PID of client's process
sysinfo (shrinked)        basic info about system (Powers of Python)
shutdown                  shutdown client's PC
isuseradmin               check if user is admin
extendrights              extend system rights
disabletaskmgr            disable Task Manager
enabletaskmgr             enable Task Manager
disableUAC                disable UAC
monitors                  get all used monitors
geolocate                 get location of computer
volumeup                  increase system volume to 100%
volumedown                decrease system volume to 0%
setvalue                  set value in registry
delkey                    delete key in registry
createkey                 create key in registry
setwallpaper              set wallpaper
exit                      terminate the session of RAT

Shell:
<br/>
pwd                       get current working directory
shell                     execute commands via cmd
cd                        change directory
[Driver]:                 change current driver
cd ..                     change directory back
dir                       get all files of current directory
abspath                   get absolute path of files

Network:
<br/>
ipconfig                  local ip
portscan                  port scanner
profiles                  network profiles
profilepswd               password for profile

Input devices:
<br/>
keyscan_start             start keylogger
send_logs                 send captured keystrokes
stop_keylogger            stop keylogger
disable(--keyboard/--mouse/--all) 
enable(--keyboard/--mouse/--all)

Video:
<br/>
screenshare               overseing remote PC
webcam                    webcam video capture
breakstream               break webcam/screenshare stream
screenshot                capture screenshot
webcam_snap               capture webcam photo

Files:
<br/>
delfile <file>            delete file
editfile <file> <text>    edit file
createfile <file>         create file
download <file> <homedir> download file
upload                    upload file
cp <file1> <file2>        copy file
mv <file> <path>          move file
searchfile <file> <dir>   search for file in mentioned directory
mkdir <dirname>           make directory
rmdir <dirname>           remove directory
startfile <file>          start file
readfile <file>           read from file
<br/>
 

## Licence
  
    Copyright (c) 2021 FZGbzuw412

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
