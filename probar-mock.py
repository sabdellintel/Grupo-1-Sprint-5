import json

# Abrir y cargar el archivo JSON
with open("mock.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Acceder a la lista de usuarios
usuarios = json_data["usuarios"]

# Recorrer cada usuario
for usuario in usuarios:
    numero = usuario["numero"]
    nombre = usuario["nombre"]
    apellido = usuario["apellido"]
    dni = usuario["DNI"]
    tipo = usuario["tipo"]

    print(f"Usuario {numero}: {nombre} {apellido}, DNI: {dni}, Tipo: {tipo}")

    # Acceder a las transacciones del usuario
    transacciones = usuario["transacciones"]

    # Recorrer cada transacción del usuario
    for transaccion in transacciones:
        estado = transaccion["estado"]
        tipo_transaccion = transaccion["tipo"]
        cuentaNumero = transaccion["cuentaNumero"]
        monto = transaccion["monto"]
        fecha = transaccion["fecha"]
        razonRechazo = transaccion.get("razonRechazo", "")

        print(f"  Transacción {transaccion['numero']}: {tipo_transaccion} - {estado}")
        print(f"    Fecha: {fecha}")
        print(f"    Monto: {monto}")
        if estado == "RECHAZADA":
            print(f"    Razón de rechazo: {razonRechazo}")
