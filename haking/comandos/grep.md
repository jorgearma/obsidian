```

```

| Objetivo                              | Comando ejemplo                                                                    |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| Buscar líneas con "millionth"         | `grep millionth data.txt`                                                          |
| Mostrar líneas antes y después        | `grep -C 2 millionth data.txt`                                                     |
| Mostrar solo la palabra encontrada    | `grep -o millionth data.txt`                                                       |
| Mostrar palabra antes y después       | `grep -oP '\w+\s+millionth\s+\w+' data.txt`                                        |
| Mostrar palabra antes y después (awk) | `awk '{for(i=1;i<=NF;i++) if($i=="millionth") print $(i-1), $i, $(i+1)}' data.txt` |
