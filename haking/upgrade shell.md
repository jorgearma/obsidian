```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'


##2
Ctrl + Z
##3

stty raw -echo
fg

##4

export TERM=xterm
export SHELL=/bin/bash


##5

reset

```