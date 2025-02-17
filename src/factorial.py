"""Módulo que contiene la función factorial."""

from typing import Union

def factorial(numero: int) -> Union[int, bool]:
    """
    Calcula el factorial de un número.

    Entrada:
    - numero (int): Número entero no negativo.

    Salida:
    - int | bool: El factorial del número si es válido, 
        de lo contrario, False.
    """
    if not isinstance(numero, int) or numero < 0:
        return False
    if numero in (0, 1):
        return 1
    return numero * factorial(numero - 1)
