class Motor:
    '''
    Clase Motor - Utilizada para composición en vehículos
    Representa el motor de un vehículo con sus características y comportamientos
    '''

    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia
        self._encendido = False

    # Propiedades con @property y @setter
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, nueva_potencia):
        if nueva_potencia > 0:
            self._potencia = nueva_potencia
        else:
            print("Error: La potencia debe ser mayor a 0")

    @property
    def encendido(self):
        return self._encendido

    # Métodos de comportamiento
    def encender_motor(self):
        '''Enciende el motor del vehículo'''
        if not self._encendido:
            self._encendido = True
            return f"Motor {self._tipo} de {self._potencia}HP encendido. ¡BROOM!"
        return "El motor ya está encendido"

    def detener_motor(self):
        '''Detiene el motor del vehículo'''
        if self._encendido:
            self._encendido = False
            return "Motor detenido correctamente"
        return "El motor ya está apagado"

    def __str__(self):
            return f'Motor: {self.__dict__.__str__()}'