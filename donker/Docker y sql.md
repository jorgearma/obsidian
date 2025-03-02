sudPasos Detallados para Ejecutar SQL Server en Docker

```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker

```

```bash
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Jorgejorge1' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest


--------

docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Jorgejorge1' \
-p 1433:1433 \
-v /home/siemprearmando/Desktop/BeyondStats-LaLiga-SQL:/var/opt/mssql/sql_files \
--name La-liga \
-d mcr.microsoft.com/mssql/server:2019-latest


```
recuerda hacer la montura donde tiene los archvios
#### 3. **Verificar que el Contenedor SQL Server Está Corriendo**

Puedes verificar que el contenedor SQL Server está corriendo con el siguiente comando

```bash
docker ps

sudo docker ps -a

sudo docker start *name*

```
#### 4. **Conectarse a SQL Server Desde Tu Máquina Local**

Puedes conectarte al SQL Server que está corriendo en el contenedor usando cualquier herramienta cliente de SQL Server, como `sqlcmd`, Azure Data Studio, o SQL Server Management Studio (SSMS). Para conectarte:

- **Host**: `localhost` o `127.0.0.1`
- **Puerto**: `1433`
- **Usuario**: `sa`
- **Contraseña**: La contraseña que configuraste (`YourStrong@Passw0rd` en el ejemplo).### **. Conectar a SQL Server desde tu máquina**

Una vez que el contenedor de SQL Server esté en funcionamiento, puedes conectarte a él utilizando herramientas de cliente de SQL Server como `sqlcmd`, SQL Server Management Studio (SSMS), Azure Data Studio, o cualquier otra herramienta de gestión SQL compatible.

#### **Conectar usando `sqlcmd`**

Si estás en un entorno Linux, macOS, o Windows y tienes `sqlcmd` instalado, puedes conectarte al contenedor de SQL Server con el siguiente comando:

```bash
sqlcmd -S localhost -U sa -P YourStrong@Passw0rd


sqlcmd -S localhost,1433 -U sa -P Jorgejorge1 -i Create-tables.sql

```

