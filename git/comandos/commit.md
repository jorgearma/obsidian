```shell
git commit # Agregar commit a la historia
```

```shell
git commit -m 'Message' # Agregar con mensaje directamente
```

```shell
git commit --amend # Agregar commit a la historia
# Equivale a git reset --soft HEAD^ y luego git commit -c ORIG_HEAD
```

```shell
git commit [-a|--all] # Agrega todos los archivos agregados y modificados y luego confirma
```

```shell
git commit [-v|--verbose] # Muetra el diff en el editor
```