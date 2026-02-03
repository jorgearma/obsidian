```bash
find . -type d -name ".git"

find . -type d -name ".git" -exec rm -rf {} +

grep --color=auto -rnw '/var/www/html/config.php' -ie "PASSWORD" --color=always 2> /dev/null

grep -rniE --color=always 'dbUserPassword\s*[:=]\s*["'\'']?[A-Za-z0-9!@#$%^&*()_+=-]{4,}' . 2>/dev/null

find . -type f -exec grep -i -I "dbUserPassword" {} /dev/null \;


## busca testo legibles 
find . -type f -exec file {} \; | grep ": ASCII text"

## texto espesifico
find . -type f -exec grep -I -H "texto_que_buscas" {} \; 2>/dev/null

## tamaño y legible
find . -type f -size 1033c -exec file {} \; | grep ": ASCII text"


```
