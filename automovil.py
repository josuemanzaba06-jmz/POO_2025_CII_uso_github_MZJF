from motor import Motor
from vehiculo import Vehiculo
class Automovil(Vehiculo):
    '''
    Clase que hereda de Vehiculo para crear un tipo Automovil - Hereda de Vehiculo
    Características específicas, puertas y maletero
    '''

    def __init__(self, marca:str, modelo:str, anio:int, numero_puertas:int, motor:Motor):
        Vehiculo.__init__(self, marca=marca ,modelo=modelo,anio=anio)
        self._numero_puertas = numero_puertas
        self._motor = motor  # Composición
        self._maletero_abierto = False


    @property
    def numero_puertas(self):
        return self._numero_puertas


    @numero_puertas.setter
    def numero_puertas(self, nuevo_numero):
         if nuevo_numero in [2, 3, 4, 5]:
            self._numero_puertas = nuevo_numero
         else:
             print("Error: Número de puertas inválido")


    @property
    def motor(self):
        return self._motor


    @property
    def maletero_abierto(self):
        return self._maletero_abierto


    # Métodos de comportamiento
    def abrir_maletero(self):
        '''Abre el maletero del automóvil'''
        if not self._maletero_abierto:
            self._maletero_abierto = True
            return "Maletero abierto"
        return "El maletero ya está abierto"


    def cerrar_maletero(self):
        '''Cierra el maletero del automóvil'''
        if self._maletero_abierto:
            self._maletero_abierto = False
            return "Maletero cerrado"
        return "El maletero ya está cerrado"


    def tocar_claxon(self):
            '''Toca el claxon del automóvil'''
            return "¡Piiii! ¡Piiii!"


    def __str__(self):
        return f'Automovil: {self.__dict__.__str__()}'

if __name__ == '__main__':
    automovil1= Automovil(marca="Toyota", modelo="RAV4", anio=2023, numero_puertas=4, motor=Motor("4 Cilindros", 203))
    automovil2= Automovil(marca="Chevrolet", modelo="Camaro", anio=2024, numero_puertas=2, motor=Motor("V8", 455))
    print(f'marca: {automovil1.marca}')
    print(f'modelo: {automovil1.modelo}')
    print(f'anio: {automovil1.anio}')
    print(f'numero_puertas: {automovil1.numero_puertas}')
    print(f'motor: {automovil1.motor}')

    print(f" Encender auto :{automovil1.encender()}")
    print(f"  Encender motor :{automovil1.motor.encender_motor()}")
    print(f" Tocar claxon: {automovil1.tocar_claxon()}")
    print(f" Abrir maletero: {automovil1.abrir_maletero()}")

    print('*'.center(80, '*'))
    print(f'marca: {automovil2.marca}')
    print(f'modelo: {automovil2.modelo}')
    print(f'anio: {automovil2.anio}')
    print(f'numero_puertas: {automovil2.numero_puertas}')
    print(f'motor: {automovil2.motor}')

    print(f" Encender auto :{automovil2.encender()}")
    print(f"  Encender motor :{automovil2.motor.encender_motor()}")
    print(f" Tocar claxon: {automovil2.tocar_claxon()}")
    print(f" Abrir maletero: {automovil2.abrir_maletero()}")




