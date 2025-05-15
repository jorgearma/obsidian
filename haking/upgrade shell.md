```bash
script -qc /bin/bash /dev/null
#Upgrade shell
python3 -c 'import pty; pty.spawn("/bin/bash")'
SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw - echo ;fg
fg
reset
xterm
export TERM=xterm
export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```