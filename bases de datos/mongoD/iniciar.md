
1


Puede iniciar el [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod)proceso emitiendo el siguiente comando:

```
sudo systemctl start mongod
```

Si recibe un error similar al siguiente al iniciar [`mongod`:](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod

`Failed to start mongod.service: Unit mongod.service not found.`

Ejecute el siguiente comando primero:

```
sudo systemctl daemon-reload
```

Luego ejecute el comando de inicio anterior nuevamente.

#### Verifique que MongoDB se haya iniciado correctamente.[![](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/#verify-that-mongodb-has-started-successfully "Enlace permanente a este encabezado")

```
sudo systemctl status mongod
```

Opcionalmente, puede asegurarse de que MongoDB comience después de reiniciar el sistema emitiendo el siguiente comando:

```
sudo systemctl enable mongod
```

3

#### Detenga MongoDB.[![](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/#stop-mongodb "Enlace permanente a este encabezado")

Según sea necesario, puede detener el [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod)proceso emitiendo el siguiente comando:

```
sudo systemctl stop mongod
```

4

1
Puede reiniciar el [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod)proceso emitiendo el siguiente comando:

```
sudo systemctl restart mongod
```

Puede seguir el estado del proceso en busca de errores o mensajes importantes observando el resultado del `/var/log/mongodb/mongod.log`archivo.

#### Comience a usar MongoDB.[![](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/#begin-using-mongodb "Enlace permanente a este encabezado")

Empezar un[`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)sesión en la misma máquina host que el archivo [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod). Tu puedes correr[`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh) sin ninguna opción de línea de comandos para conectarse a un [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod)servidor que se esté ejecutando en su host local con el puerto predeterminado 27017.

```
mongosh
```