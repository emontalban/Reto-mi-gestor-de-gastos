def calcular_gastos():
    # 1. Definir una lista de exactamente cinco gastos con nombre y monto
    gastos = [
        {"nombre": "Supermercado", "gasto": 18.50},
        {"nombre": "Gasolina", "gasto": 45.00},
        {"nombre": "Cafetería", "gasto": 6.20},
        {"nombre": "Cine", "gasto": 12.00},
        {"nombre": "Transporte", "gasto": 22.50}
    ]
    print(f"Lista de los gastos:")
    for gasto in gastos:
        
        print(f"{gasto['nombre']}: {gasto['gasto']} €")

    # 2. Calcular el total de los gastos usando un bucle
    total_gastos = 0
    for gasto in gastos:
        total_gastos += gasto["gasto"]

    print(f"\nEl total de los gastos es de {total_gastos} €")

    # 3. Calcular el gasto medio
    gasto_medio = total_gastos / len(gastos)
    print(f"\nEl gasto medio es de {gasto_medio: 0.2f} €")
    print("\n")

    # 4. Mostrar qué gastos superan los 20 €
    gastos_superiores_a_20 = 0
    for gasto in gastos:
        if gasto["gasto"] > 20:
            gastos_superiores_a_20 += 1
            print(f"El gasto de {gasto['nombre']} es de {gasto['gasto']} € y supera los 20 €")

    # 5. comparar presupuesto semanal de 100 €
    if total_gastos > 100:
        print(f"\nEl gasto total supera los 100 €")
        
calcular_gastos()