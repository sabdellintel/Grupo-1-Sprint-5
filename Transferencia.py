class Transferencia:
    def __init__(self, tipo, estado, cupoDiarioRestante, monto, saldo, targetasActuales, chequerasActuales, fecha):
        self.tipo = tipo
        self.estado = estado
        self.cupoDiarioRestante = cupoDiarioRestante
        self.monto = monto
        self.saldo = saldo
        self.targetasActuales = targetasActuales
        self.chequerasActuales = chequerasActuales
        self.fecha = fecha
    
    def __str__(self) -> str: #Solo para pruebas
        return f"Tipo: {self.tipo}\nEstado: {self.estado}\nCupo Diario Restante: {self.cupoDiarioRestante}\nMonto: {self.monto}\nSaldo: {self.saldo}\nTargetas Actuales: {self.targetasActuales}\nChequeras Actuales: {self.chequerasActuales}"