```shell
git branch # Mostrar ramas
```

```shell
git branch -vv # Mostrar ramas con SHA1 y commit subject line
```

```shell
git branch <nombre> # Crear rama con puntero a posición actual
```

```shell
git branch -d <nombre> # Eliminar rama (--delete)
```

```shell
git branch -D <nombre> # Forzar eliminar rama (--delete --force)
```

```shell
git branch --merged # Mostrar ramas fusionadas a la actual. Con * si aún no se incorporan últimos cambios
```

```shell
git branch --no-merged # Mostrar ramas que no han sido incorporadas a la actual
```

```shell
git branch -m <new-name> # Mover/renombrar una rama y su correspondiente reflog
```