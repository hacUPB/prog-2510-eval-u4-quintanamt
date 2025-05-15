import os #listar archivos
import csv #Archivos csv
import matplotlib.pyplot as plt


def menu_principal():
    print('\nAPLICACIÓN CLI DE ANÁLISIS DE DATOS')
    print('-----------------------------------')
    print('1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos')
    print('2. Procesar archivo de texto .txt')
    print('3. Procesar archivo separado por comas (.csv)')
    print('4. Salir')
    opcion = input('Elija un número de opción: ')
    return opcion



def submenu_txt():
    print('\n--- SUBMENÚ TXT ---')
    print('1. Contar palabras')
    print('2. Reemplazar texto')
    print('3. Histograma de vocales')
    print('4. Volver al menú principal')  
    opcion = input('Elija un número de opción: ')
    return opcion

def submenu_csv():
    print('\n--- SUBMENÚ CSV ---')
    print('1. Mostrar las 15 primeras filas')
    print('2. Calcular estadísticas')
    print('3. Graficar una columna completa con los datos')
    print('4. Volver al menú principal')  
    opcion = input('Elija un número de opción: ')
    return opcion


def contar_palabras():
    with open("sample1.txt") as archivo:
        contenido = archivo.read()

        palabras = contenido.split()
        num_palabras = len(palabras)

        num_caracteres_total = len (contenido)
        num_caracteres_sin_espacio = len(contenido.replace(" "," "))

        print("\n--- ESTADÍSTICAS ---")
        print(f"Palabras: {num_palabras}")
        print(f"Caracteres totales: {num_caracteres_total}")
        print(f"Caracteres sin espacios: {num_caracteres_sin_espacio}")

    return num_palabras, num_caracteres_total, num_caracteres_sin_espacio

def reemplazar_una_palabra_por_otra():
    palabra_a_buscar = input("Ingrese la palabra que desea reemplazar: ")
    palabra_de_reemplazo = input("Ingrese la palabra de reemplazo: ")

    with open("sample1.txt", 'r') as archivo:
        contenido = archivo.read()
        nuevo_contenido = contenido.replace(palabra_a_buscar, palabra_de_reemplazo)
        archivo = open("sample1.txt" , 'w')
        archivo.write(nuevo_contenido)
        archivo.close()

        print("La palabra '" + palabra_a_buscar + "' reemplazada por '" + palabra_de_reemplazo + "'")


    return palabra_a_buscar , palabra_de_reemplazo

def contar_vocales():
    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    
    with open("sample1.txt") as archivo:
        for letra in archivo.read().lower():
            if letra in vocales:
                vocales[letra] += 1
    
    plt.bar(vocales.keys(), vocales.values())
    plt.title('Histograma')
    plt.xlabel('Vocales')
    plt.ylabel('Numero de repeticiones')
    plt.show()

def primeras_15_lineas():
        num_filas = 15
        with open('sample2.csv', 'r') as csvfile:
            lector = csv.reader(csvfile)
            encabezados = next(lector) 
            print("Encabezados:", encabezados)
            for i, fila in enumerate(lector):
                if i >= num_filas:
                 break
                print(fila)








def main():
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            print(os.getcwd())
            print(os.listdir())
        elif opcion == '2':
            while True:
                opcion_txt = submenu_txt()
                if opcion_txt == '1':
                    contar_palabras()
                elif opcion_txt == '2':
                    reemplazar_una_palabra_por_otra()
                elif opcion_txt == '3':
                    contar_vocales()
                elif opcion_txt == '4':
                    break 
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == '3':
            while True:
                opcion_csv = submenu_csv()
                if opcion_csv == '1':
                    primeras_15_lineas()
                elif opcion_csv == '2':
                    print("")
                elif opcion_csv == '3':
                    print("")
                elif opcion_csv == '4':
                    break 
                else:
                    print("Opción no valida, Intente de nuevo. ")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
