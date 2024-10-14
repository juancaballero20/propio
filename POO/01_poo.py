import datetime

class vehiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        
    def pico_placa(self):
        ultimo_num = int(self.placa[-1])
        hoy = datetime.datetime.now().weekday()
        if hoy % 2 == 0:
            if ultimo_num in [6, 7, 8, 9, 0]:
                return "El vehiculo tiene pico y placa de 06:00 a.m hasta las 09:00 p.m"
            
            else:
                return "El vehiculo esta libre de pico y placa, por hoy"
        
        else: 
            if ultimo_num in [1, 2, 3, 4, 5]:
                return "El vehiculo tiene pico y placa de 06:00 a.m hasta las 09:00 p.m"
            
            else:
                return "El vehiculo esta libre de pico y placa, por hoy"
        
marca = input("Ingrese la marca de su vehiculo: ")
modelo = input("Ingrese el modelo de su vehiculo: ")
placa = input("Ingrese la placa de su vehiculo: ")

vehiculo1 = vehiculo(marca, modelo, placa)

print(vehiculo1.pico_placa())
