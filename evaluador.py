
import csv

def promedio(a, b, c):
    return (a + b + c) / 3

ruta = "resultados.csv"

with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Promedio", "Estado"])

    while True:
        nombre = input("Ingrese nombre del alumno (o escriba 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break

        try:
            calif1 = float(input("Ingrese calificación de Ciencias: "))
            calif2 = float(input("Ingrese calificación de Matemáticas: "))
            calif3 = float(input("Ingrese calificación de Estadísticas: "))
        except ValueError:
            print("⚠️ Ingresaste un valor no numérico. Intentalo de nuevo.
")
            continue

        calc = promedio(calif1, calif2, calif3)
        promedio_redondeado = round(calc, 2)
        estado = "Aprobado" if calc >= 6 else "Reprobado"

        print(f"El/La alumno/a: {nombre} ha {estado.lower()} con un promedio de: {promedio_redondeado}\n")

        escritor.writerow([nombre, promedio_redondeado, estado])

print("✅ Evaluación finalizada. Resultados guardados en 'resultados.csv'")
