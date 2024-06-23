from te import Te

sabor=int (input("Ingrese el numero del té\n 1. Negro\n 2. Veerde\n 3. Hierbas\n"))
formato=int(input("De cuantos Gramos? (300 o 500): "))

te=Te(sabor, formato)


print(f"Su pedido es {te.obtener_sabor()}, le recomendamos consumir {te.obtener_tiempo_recomendacion(sabor)[1]} y lo repose por {te.obtener_tiempo_recomendacion(sabor)[0]} min.")
print(f"Valor: $ {te.obtener_precio(formato)}\nFormato: {te.formato}\nDuracion: {te.duracion} dias")
    