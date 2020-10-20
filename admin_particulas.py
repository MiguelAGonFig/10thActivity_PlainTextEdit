from particula import Particula

class Admin_particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, part:Particula):
        self.__particulas.append(part)

    def agregar_inicio(self, part:Particula):
        self.__particulas.insert(0, part)
    
    def consultar(self):
        for part in self.__particulas:
            print(part)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
        