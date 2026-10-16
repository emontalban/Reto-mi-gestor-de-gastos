def calcular_gastos():

    #1.Guardar varios gastos en una lista
    gastos = [15.50, 42.00, 8.75, 25.00, 12.30, 35.00, 19.99]

    #2.Calcular el total de los gastos
    total_gastos= sum(gastos)
    print(f"2. Gasto total de la semana: {total_gastos:.2f} €")


calcular_gastos()