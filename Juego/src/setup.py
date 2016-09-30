import cs_Freeze

executables = [cx_Freeze.Executable("setup.py")]

cx_Freeze.setup(
        name = "Jueguito Pedorro",
        options = {"build_exe" : {"packages" : ["pygame"], "include_files" : ["Imagenes/Enemigo1.png", "Imagenes/Personaje.png", "Imagenes/Disparo.png", "Imagenes/Fondo.jpg", "Imagenes/Curacion.png"]}},
        description = "Juego hecho por pato para vos!!!",
        executables = executables
        )
