import re

# Usamos una expresión regular avanzada para extraer palabras en mayúsculas de una cadena
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y Expresiones REGULARES"

# Expresión regular que busca palabras completamente en mayúsculas
patron = r'\b[A-Z]{2,}\b'

# Encontramos todas las coincidencias
palabras_mayusculas = re.findall(patron, cadena)
print("Palabras en mayúsculas:", palabras_mayusculas)