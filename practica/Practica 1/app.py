
from Piezas import Piezas


from lista_piezas import lista_piezas




class app:
    

    def datos(self):
        print("")
        print("-202202182")
        print("-José Luis Espinoza Jolón")
        print("-Introduccion a la programacion y Computacion 2")
        print("-Seccion D")


    def tablero_piezas(self):
        tablero_nuevo = lista_piezas()
        
        print("")
        print("")
        print("-------------------Crear Tablero ------------------")
        fila = int(input("Ingrese la fila para el tablero: "))
        columan =  int(input("Ingrese la columnas para el tablero: "))
        tablero_nuevo.iniciar_tablero(fila,columan)
        tablero_nuevo.filas = fila
        tablero_nuevo.columnas = columan
        print("")
        tablero_nuevo.tablero_consola()
        print("")
        print("-------------------Crear Piezas ------------------")
        new_piezas =True

        while new_piezas:
            print("A. Azul")
            print("R. Rojo")
            print("V. verde")
            print("P. Purpura")
            print("N. Naranja")
            color = input("Ingrese la opcion que quiere: ")
            print("")

            fila_nueva = int(input(f"en que fila quieres ponerla {1}-{fila}: "))
            columan_nueva = int(input(f"en que columan quieres {1}-{columan}:  "))

            tablero_nuevo.acutalizar_piezas(fila_nueva,columan_nueva,color)
            print("")
            print("")

            tablero_nuevo.tablero_consola()
            respuesta = input("desea agregar piesa S/N:")
            print("")
            print("")
            print("----------------------------------------------------")
            if respuesta== "N" or respuesta =="n":
                new_piezas = False
        tablero_nuevo.tablero_consola()
        print("-------------------Fin del tablero------------------")
        print("")
        tablero_nuevo.graficar()


    def menu(self):
        print("")
        print("--------------------------------------")
        print("Menu principal")
        print("--------------------------------------")
        print("")
        print("1. Cargar tablero")
        print("2. Procesar archivo")
        print("3. Salida")
        opcion = int(input("->Ingrese una opcion: "))

        if opcion == 1:
            self.tablero_piezas()
            self.menu()
        elif opcion == 2:
            self.datos()
            self.menu()
        elif opcion == 3:
            print("GRACIAS")
        else:
            print("Opcion invalida vuelve intentarlo: ")
            self.menu()

app_llamar = app()

app_llamar.menu()