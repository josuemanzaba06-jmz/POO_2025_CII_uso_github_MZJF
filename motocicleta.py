from vehiculo import Vehiculo
from motor import Motor
class Motocicleta(Vehiculo):
    '''
    Clase que hereda de Vehiculo para crear un tipo Motocicleta - Hereda de Vehiculo
    Características específicas, cilindraje
    '''

    def __init__(self, marca: str, modelo: str, anio: int, cilindraje: int, motor: Motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self._motor = motor  # Composición
        self._caballito_activo = False

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        if nuevo_cilindraje > 0:
            self._cilindraje = nuevo_cilindraje
        else:
            print("Error: El cilindraje debe ser mayor a 0")

    @property
    def motor(self):
        return self._motor

    @property
    def caballito_activo(self):
        return self._caballito_activo

    # Métodos de comportamiento
    def hacer_caballito(self):
        '''Realiza un caballito con la motocicleta'''
        if not self._caballito_activo:
            self._caballito_activo = True
            return "¡Haciendo caballito!  Rueda trasera arriba"
        return "Ya estás haciendo un caballito"

    def terminar_caballito(self):
        '''Termina el caballito'''
        if self._caballito_activo:
            self._caballito_activo = False
            return "Caballito terminado, ambas ruedas en el suelo"
        return "No estás haciendo un caballito"

    def usar_patada_arranque(self):
        '''Usa la patada de arranque (kick start)'''
        return f"¡Patada de arranque! *KICK* {self._motor.encender_motor()}"

    def __str__(self):
        return f'Motocicleta: {self.__dict__.__str__()}'


if __name__ == '__main__':
    motocicleta1= Motocicleta(marca="Yamaha", modelo="MT-09", anio=2023,cilindraje=889, motor=Motor("Tricilíndrico", 119))
    motocicleta2= Motocicleta(marca="Ducati", modelo="Panigale V4", anio=2024, cilindraje=1103 ,motor=Motor("V4", 214))
    print(f'marca: {motocicleta1.marca}')
    print(f'modelo: {motocicleta1.modelo}')
    print(f'anio: {motocicleta1.anio}')
    print(f'cilindraje: {motocicleta1.cilindraje}')
    print(f'motor: {motocicleta1.motor}')

    print('*'.center(80, '*'))
    print(f'marca: {motocicleta2.marca}')
    print(f'modelo: {motocicleta2.modelo}')
    print(f'anio: {motocicleta2.anio}')
    print(f'cilindraje: {motocicleta2.cilindraje}')
    print(f'motor: {motocicleta2.motor}')