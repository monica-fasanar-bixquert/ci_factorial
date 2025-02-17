import pytest
from src.factorial import factorial

def test_factorial_1_falla():
    assert factorial(1) == 1

def test_factorial_1_pasa():
    assert factorial(1) == 1

def test_tipo_falla():
    assert factorial('a') == False

def test_tipo_pasa():
    assert factorial(5) == 120

def test_negativo_falla():
    assert factorial(-1) == False

def test_negativo_pasa():
    assert factorial(-1) == False

def test_positivo_falla():
    assert factorial(5) == 120

def test_positivo_pasa():
    assert factorial(5) == 120
