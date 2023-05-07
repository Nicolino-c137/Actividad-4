class Ventana:
    __titulo= ''
    __x_sup_izq= 0
    __y_sup_izq= 0
    __x_inf_der= 0
    __y_inf_der= 0
    
    def __init__(self,titulo,xIzq= 0,yIzq= 0,xDer= 50,yDer= 50):
        self.__titulo= titulo
        #0 es el menor valor que se le pueden asignar a las coordenadas del vertice superior izquierdo 
        #500 el el mayor valor que se le puede asignar a las coordenadas del vertice inferior derecho
        self.__x_sup_izq= max(0,xIzq)
        self.__y_sup_izq= max(0,yIzq)
        self.__x_inf_der= min(xDer,500)
        self.__y_inf_der= min(yDer,500)
        if self.__x_sup_izq >= self.__x_inf_der:
            self.__x_sup_izq= self.__x_inf_der - 1
        if self.__y_sup_izq >= self.__y_inf_der:
            self.__y_sup_izq= self.__y_inf_der -1
            
    def mostrar(self):
        print(f"""
Nombre de la ventana = {self.__titulo}
Coordenas del vertice superior izquierdo = ({self.__x_sup_izq},{self.__y_sup_izq})
Coordenadas del vertice inferior derecho = ({self.__x_inf_der},{self.__y_inf_der})""")
        
    def getTitulo(self):
        return self.__titulo 
    
    def alto(self):
        return self.__y_inf_der - self.__y_sup_izq
    
    def ancho(self):
        return self.__x_inf_der - self.__x_sup_izq
    
    def moverDerecha(self,desplazamiento= 1):
        self.__x_sup_izq+= desplazamiento
        self.__x_inf_der+= desplazamiento
    
    def moverIzquierda(self,desplazamiento= 1):
        self.__x_sup_izq-= desplazamiento
        self.__x_inf_der-= desplazamiento
    
    def subir(self,desplazamiento= 1):
        self.__y_sup_izq+= desplazamiento
        self.__y_inf_der+= desplazamiento
    
    def bajar(self,desplazamiento= 1):
        self.__y_sup_izq-= desplazamiento
        self.__y_inf_der-= desplazamiento