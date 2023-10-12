import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum(scope='session'):
   yield Accumulator() #se ejecuta todo el codigo hasta aqui hasta q terminen todos los tests de ejecutar con esta fixture
   #despues del yield  como tareas de limpieza
   print('DONE with the test completes')

@pytest.fixture
def accum2():
   return Accumulator()