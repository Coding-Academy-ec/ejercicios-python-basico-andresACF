from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Andrés Cornejo"
    edad = 21
    estatura = 1.70
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Andrés Cornejo\nEdad: 21\nEstatura: 1.70\n"
