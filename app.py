from Cliente import Cliente
from Cuenta import Cuenta
from Transferencia import Transferencia



black = Cuenta("peso y dolar", 10000, 500000, 5, 2, -1, 0)

josesito = Cliente(1, "Jose", "Perez", 12345678, black)

t_1 = Transferencia("RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "RECHAZADA", 1000, 10000000000, 100000, 1, 1, "2021-10-10")

print(josesito.verificarTransferencia(t_1))