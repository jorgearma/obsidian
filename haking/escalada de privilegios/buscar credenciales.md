```shell
grep --color=auto -rnw '/var/www/html/config.php' -ie "PASSWORD" --color=always 2> /dev/null

grep -rniE --color=always 'dbUserPassword\s*[:=]\s*["'\'']?[A-Za-z0-9!@#$%^&*()_+=-]{4,}' . 2>/dev/null

find . -type f -exec grep -i -I "dbUserPassword" {} /dev/null \;
```