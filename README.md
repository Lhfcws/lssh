## LSSH
LSSH is just a simple ssh tool for lazy people.   
It's not secure, but convenient for daily work.   
Recommend to the coders who have to usually ssh to Unix servers. Not Recommend to the secure server.  

**[Installation]**  

1. First you should make sure you have ssh && sshpass.  `sudo apt-get install sshpass`  
2. Download lssh.zip (or git clone) and uncompress.
3. set `alias lssh='python2 /home/lhfcws/local/lssh/scripts/lssh.py'` in ~/.bashrc
4. `source ~/.bashrc`

*lssh -h* to see the more details.

**[Others]**

There're something that needs to be improved in this project, like storing password in salted base64 encryption, forking a process instead of run commands in python, using `expect` to automatically create the first-time ssh connection according to the give host list. 
