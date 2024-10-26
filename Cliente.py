from Cuenta import Cuenta

class Cliente:
    def __init__(self, numero:int, nombre:str, apellido:str, dni:int, tipo:Cuenta):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo

    def __str__(self) -> str:
        return f"\nNumero: {self.numero}, Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}\n"
    
    def verificarTransferencia(self, transferencia):
        return self.__str__() + self.tipo.verificarTransferencia(transferencia)