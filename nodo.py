class nodo_estado:
    def __init__(self, EA, EP, A, n):
        self.valor = EA
        self.padre = EP
        self.accion = A
        self.nivel = n
        self.distancia = None
    
    def get_estado(self):
        return self.valor

    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def get_distancia(self):
        return self.distancia

    def set_distancia(self, distancia):
        self.distancia = distancia

    def __eq__(self, e):
        return self.valor == e