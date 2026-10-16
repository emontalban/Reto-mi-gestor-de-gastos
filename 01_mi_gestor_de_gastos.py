

def calcular_gastos():

    #1.Guardar varios gastos en una lista
    gastos = [15.50, 42.00, 8.75, 25.00, 12.30, 35.00, 19.99]
    print(f"1. Lista de gastos registrados (en €):")
    for gasto in gastos:
        print(f"{gasto} €")
   
    #2.Calcular el total de los gastos
    total_gastos= sum(gastos)
    print(f" Gasto total de la semana: {total_gastos} €")


    #3.Calcular el gasto medio
    gasto_medio = sum(gastos) / len(gastos)
    print(f"El gasto medio de la semana es de {gasto_medio: 0.2f} €")
    
    #4.Mostrar qué gastos superan los 20 €
    gastos_superiores_a_20 = 0
    for gasto in gastos:
        if gasto > 20:
            gastos_superiores_a_20 += 1
            print(f"El gasto de {gasto} € supera los 20 €")

       
        
    #5.Mostrar un mensaje indicando si el gasto total supera un presupuesto semanal de 100 €
    if total_gastos > 100:
        print("El gasto total supera los 100 €")


calcular_gastos()