Conecta a SQL Server y lee los datos en un DataFrame:

```python
import pandas as pd
import pyodbc

# Conexión a SQL Server
conexion = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=nombre_servidor;'
                          'DATABASE=nombre_base_datos;'
                          'UID=tu_usuario;'
                          'PWD=tu_contraseña')

# Cargar las tablas en DataFrames
df_players = pd.read_sql("SELECT * FROM ID_player_team", conexion)
df_ataques = pd.read_sql("SELECT * FROM ataques_stats", conexion)
df_clasic = pd.read_sql("SELECT * FROM clasic_stats", conexion)
df_defensivas = pd.read_sql("SELECT * FROM defensivas_stats", conexion)
df_disciplina = pd.read_sql("SELECT * FROM disciplina_stats", conexion)
df_eficiencia = pd.read_sql("SELECT * FROM eficiencia_stats", conexion)

# Cerrar la conexión
conexion.close()

import pandas as pd
from sqlalchemy import create_engine


connection_string = 'mssql+pyodbc://sa:Jorgejorge1@localhost,1433/BeyondStats?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)

# Leer las tablas usando pandas con el engine de SQLAlchemy
df_disciplina = pd.read_sql("SELECT * FROM disciplina_stats", engine)
df_eficiencia = pd.read_sql("SELECT * FROM eficiencia_stats", engine)

# Mostrar los primeros registros para verificar
print(df_disciplina.head())
print(df_eficiencia.head())


```