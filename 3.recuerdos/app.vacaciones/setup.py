from cx_Freeze import setup, Executable

setup(
    name="bienvenida",
    version="1.0",
    description="Mi aplicación de bienvenida",
    executables=[Executable("bienvenida.py")]
)

