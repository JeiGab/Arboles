class Nodo:
    def __init__(self, dato, datoB=None):
        self.dato = dato
        self.ladoizq = None
        self.ladoder = None
        self.datoB = datoB

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.insertar_rec(self.raiz, dato)

    def insertar_rec(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.ladoizq is None:
                nodo.ladoizq = Nodo(dato)
            else:
                self.insertar_rec(nodo.ladoizq, dato)
        else:
            if nodo.ladoder is None:
                nodo.ladoder = Nodo(dato)
            else:
                self.insertar_rec(nodo.ladoder, dato)

    def imprimir_inorden(self, nodo):
        if nodo:
            self.imprimir_inorden(nodo.ladoizq)
            print(nodo.dato, end=' ')
            self.imprimir_inorden(nodo.ladoder)     

    def busqueda(self, dato):
        resultado = self.busqueda_rec(self.raiz, dato)
        if resultado:
            print("Sí está el dato")
        else:
            print("No está el dato")

    def busqueda_rec(self, nodo, dato):
        aux = nodo
        while aux:
            if aux.dato == dato:
                return True
            elif dato < aux.dato:
                aux = aux.ladoizq
            else:
                aux = aux.ladoder
        return False



arbol = ArbolBinarioBusqueda()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Valores en orden:")
arbol.imprimir_inorden(arbol.raiz)
print()

arbol.busqueda(80)
