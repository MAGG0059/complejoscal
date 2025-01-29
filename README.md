# Project Title

Calculadora Números Complejos

# Prerequisitos

- Python 3.x instalado
- Visual Studio Code, IDLE, o cualquier editor de texto/IDE

# Installing

1. Descargar el archivo `operaciones_complejos.py`.
2. Abrirlo en Visual Studio Code, IDLE o tu editor preferido.
3. Ejecutar el archivo para probar las operaciones.

# Running the tests
El sistema cuenta con pruebas automatizadas en el archivo Testcomplex.py, donde se verifican todas las operaciones implementadas en operaciones_complejos.py.

# Ejemplo de prueba:

python
assert sumacplx((5, 3), (2, 1)) == (7, 4)
assert multcplx((1, -1), (1, 1)) == (2, 0)

Ejemplo:

Copiar
Editar
flake8 operaciones_complejos.py

# Deployment
Para desplegar este proyecto en un entorno en vivo:

Empaqueta la librería con setuptools.
Publícala en PyPI o distribúyela como un script independiente.
Ejemplo:
python setup.py sdist
pip install dist/operaciones-numeros-complejos-0.1.tar.gz
Built With
Python - Lenguaje de programación
Math Library - Para funciones matemáticas, de más librerias de python paras las pruebas.

# Versioning


# Authors
Manuel Alejandro Guarnizo

# License


# Acknowledgments
Librerias de python.
Github.
