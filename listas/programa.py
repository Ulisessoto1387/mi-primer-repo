def double(arr):
    # Multiplica cada elemento de la lista por 2.
    resultado = []
    for num in arr:
        resultado.append(num * 2)
    return resultado

def maximum(arr):
    # Devuelve el valor más grande de la lista.
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def average(arr):
    #Calcula el promedio de los elementos.
    suma_total = sum(arr)
    return suma_total / len(arr)

def main():
    # Prueba las funciones con varias listas.
    listas_de_prueba = [
        [1, 2, 3, 4, 5],
        [10, -2, 30, 5],
        [100, 200]
    ]
    
    for i, lista in enumerate(listas_de_prueba):
        print(f"Prueba {i+1}: {lista}")
        print(f"Doble:  {double(lista)}")
        print(f"Máx:   {maximum(lista)}")
        print(f"Prom:  {average(lista)}\n")

if __name__ == "__main__":
    main()

