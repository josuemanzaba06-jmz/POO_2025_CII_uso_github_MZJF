class Vehiculo:
     '''
     Clase que permite crear un objeto de tipo Vehiculo
     '''

     def __init__(self, marca=str ,modelo=str,anio=int):
            self._marca = marca
            self._modelo = modelo
            self._anio = anio
            self._encendido = False

     @property
     def marca(self):
        return self._marca

     @marca.setter
     def marca(self, nueva_marca):
        self._marca = nueva_marca


     @property
     def modelo(self):
        return self._modelo

     @modelo.setter
     def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo


     @property
     def anio(self):
        return self._anio

     @anio.setter
     def anio(self, nuevo_anio):
        self._anio = nuevo_anio

     @property
     def encendido(self):
        return self._encendido

     def __str__(self):
        return f'Vehiculo: {self.__dict__.__str__()}'

     # Métodos o Comportamientos
     def encender(self):
            '''Enciende el vehículo'''
            if not self._encendido:
                self._encendido = True
                return f"{self._marca} {self._modelo} encendido"
            return "El vehículo ya está encendido"

     def apagar(self):
            '''Apaga el vehículo'''
            if self._encendido:
                self._encendido = False
                return f"{self._marca} {self._modelo} apagado"
            return "El vehículo ya está apagado"

     def __str__(self):
         return f'Vehiculo: {self.__dict__.__str__()}'

if __name__ == '__main__':
     v1= Vehiculo(marca="Toyota", modelo="RAV4", anio=2023)

     print(f'marca: {v1._marca}')
     print(f'modelo: {v1._modelo}')
     print(f'anio: {v1._anio}')