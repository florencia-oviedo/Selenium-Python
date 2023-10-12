
'''
En Python, cualquier directorio con un archivo llamado __init__.py se trata como un paquete, y otros módulos pueden 
importar cualquier módulo dentro de ese paquete. Deje este archivo en blanco
'''

class Accumulator:

    def __init__(self) -> None:
        self._count= 0


    @property
    def count(self):
        return self._count
    
    def add(self, more=1) -> None:
        self._count += more
