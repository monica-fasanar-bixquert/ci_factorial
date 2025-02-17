"""Módulo que contiene la función factorial"""

def factorial(entero):
    """
    Función para obtener el factorial de un número.
    Entrada:
    - entero: número entero a partir del cual se calculará el factorial.
    Salida:
    - False/Número entero: en caso de ser una entrada incorrecta o poder
    calcular el factorial.
    """
    if not isinstance(entero, int):
        return False
    if entero < 0:
        return False
    if entero == 0 or entero == 1:
        return 1
    return entero * factorial(entero-1)
