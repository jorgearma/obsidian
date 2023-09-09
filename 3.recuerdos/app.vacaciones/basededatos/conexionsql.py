import mysql.connector

try:

 conecion=mysql.connector.connect(host='localhost',
                                 user='root' ,
                                 passwd='',
                                 database='base_prueba')


except exception as err:
    print('error coenctado a la base')
else:
    print('coenctado a mysql')
try:
    curl01 = conecion.cursor()
    insertar="insert into usuarios values(1002,'jorge','abc321')"
    curl01.execute(insertar)
    conecion.commit()

except exception as err:
    print('error al insertar datos',err)
else:
    print('datos correctos')
conecion.close()
