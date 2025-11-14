2025/11/14
MANZABA ZAMBANO JOSUÉ FABIÁN  
Este programa, que está escrito en Python, utiliza los cuatro elementos fundamentales de la Programación Orientada a Objetos (POO): encapsulamiento, a través de atributos protegidos con @property y @setter para regular el acceso a datos; herencia, donde las clases Motocicleta y Automóvil derivan de la superclase Vehículo; composición, al combinar objetos de la clase Motor dentro de cada vehículo; y polimorfismo, mediante la reescritura del método __str__() con ayuda de super().  Cada clase abarca diversos métodos de conducta que imitan acciones reales, como arrancar motores, tocar el claxon o hacer caballitos.
El programa principal desarrolla dos autos (Chevrolet y Toyota Camry) y dos motocicletas (DUCATI y Yamaha), les asigna motores particulares y pone en práctica varios procedimientos para exhibir toda la funcionalidad.  La salida presenta de manera ordenada la condición de cada auto, las operaciones que se han llevado a cabo y el modo en que los decoradores posibilitan el acceso y la modificación de atributos con validación automática.  Este sistema evidencia que, a través de la correcta implementación de sus principios básicos, la POO posibilita el desarrollo de un código que se puede reutilizar, está bien organizado y resulta sencillo mantenerlo.
DIAGRAMA UML
┌─────────────────────────────────────┐
│            Motor                     │
├─────────────────────────────────────┤
│ - __tipo: str                       │
│ - __potencia: int                   │
│ - __encendido: bool                 │
├─────────────────────────────────────┤
│ + tipo @property                    │
│ + potencia @property                │
│ + encendido @property               │
│ + encender_motor(): str             │
│ + detener_motor(): str              │
│ + acelerar(): str                   │
│ + __str__(): str                    │
└─────────────────────────────────────┘
                  ▲
                  │ (Composición)
                  │
┌─────────────────────────────────────┐
│           Vehiculo                   │
├─────────────────────────────────────┤
│ - __marca: str                      │
│ - __modelo: str                     │
│ - __anio: int                       │
│ - __encendido: bool                 │
├─────────────────────────────────────┤
│ + marca @property                   │
│ + modelo @property                  │
│ + anio @property                    │
│ + encender(): str                   │
│ + apagar(): str                     │
│ + obtener_edad(): int               │
│ + __str__(): str                    │
└─────────────────────────────────────┘
          ▲                  ▲
          │                  │
          │ (Herencia)       │ (Herencia)
          │                  │
┌─────────┴──────────┐  ┌───┴────────────────────┐
│    Automovil       │  │    Motocicleta         │
├────────────────────┤  ├────────────────────────┤
│ - __numero_puertas │  │ - __cilindraje: int    │
│ - __motor: Motor   │  │ - __motor: Motor       │
│ - __maletero       │  │ - __caballito: bool    │
├────────────────────┤  ├────────────────────────┤
│ + numero_puertas   │  │ + cilindraje           │
│ + motor            │  │ + motor                │
│ + abrir_maletero() │  │ + hacer_caballito()    │
│ + cerrar_maletero()│  │ + terminar_caballito() │
│ + tocar_claxon()   │  │ + usar_patada_arranque()│
│ + activar_aire()   │  │ + activar_turbo()      │
│ + __str__()        │  │ + __str__()            │
