from nodo import nodo
from Piezas import Piezas

import os

class lista_piezas:


    def __init__(self) :
        self.primero = None
        self.columnas = 0
        self.filas = 0


    def insertar(self,Piezas):
        if self.primero is None:
            self.primero = nodo(Piezas=Piezas)
            return
        aux =  self.primero
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = nodo(Piezas=Piezas)

    def recorrer_imprimir(self):
        print("")
        print("")

        aux = self.primero
        while aux:
            print("Fila: ",aux.piezas.fila , "columan: ", aux.piezas.columna, "color: ",aux.piezas.color)
            aux = aux.siguiente

    def iniciar_tablero(self,filas,columas):
        for i in range(1,filas+1):
            for j in range(1,columas+1):
                self.insertar(Piezas(i,j," "))

    
    def acutalizar_piezas(self, fila, columna,color):
        aux =self.primero
        while aux != None:
            if aux.Piezas.fila == fila and aux.Piezas.colum == columna:
                aux.Piezas.color = color
                print("---------------------------")
                print("se pinto la pieza con exito")
                return
            aux = aux.siguiente
        print("---------------------------")
        print("posicion de piesa no encontrada")


    def devolver_color(self,fila,columna):
        aux = self.primero
        while aux != None:
            if aux.Piezas.fila == fila and aux.Piezas.colum == columna:
                return aux.Piezas.color
            aux = aux.siguiente
    
    def tablero_consola(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                print("|",self.devolver_color(i,j), end="\t")
            print("|")
        print("")

    
    def graficar(self):
        f = open('bb.dot','w')
        texto="digraph G {\n node [shape=plaintext];\nlabel=\"Colorea Guatematel\";\nsome_node [\nlabel=<\n<table border=\"0\" cellborder=\"0\" cellspacing=\"0\" width=\"100%\" height=\"100%\">\n"
        for i in range(1, self.filas + 1):
            texto+="<tr>\n"
            for j in range(1, self.columnas + 1):
                colores = self.devolver_color(i,j)
                if colores == "A":
                    texto+="<td bgcolor=\""+"blue"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
                elif  colores == "R":
                    texto+="<td bgcolor=\""+"red"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
                elif  colores == "V":
                    texto+="<td bgcolor=\""+"green"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
                elif  colores == "P":
                    texto+="<td bgcolor=\""+"purple"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
                elif  colores == "N":
                    texto+="<td bgcolor=\""+"orange"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
                elif  colores == " ":
                    texto+="<td bgcolor=\""+"white"+"\" width=\"1\" height=\"1\">"+str(i)+","+str(j)+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>\n];\n}"
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Grafica.png')
        print("Tablero Juego")






