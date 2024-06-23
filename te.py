class Te():
    duracion= 365
        
    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato
        
    
    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor ==1: #te negro
            tiempo= 3
            recomendacion= 'para el desayuno'
        elif sabor ==2: #te verde
            tiempo= 5
            recomendacion= 'al medio dia'
        elif sabor ==3: #te hierbas
            tiempo= 6
            recomendacion= 'al atardecer'
        return tiempo, recomendacion
            
    @staticmethod
    def obtener_precio(formato):
        if formato ==300 : 
            precio=3000
        elif formato ==500:
            precio=5000
        return precio
    
    def obtener_sabor(self):
        if self.sabor==1: 
            texto='te negro' 
        elif self.sabor==2:
            texto='te verde' 
        elif self.sabor==3:
            texto='te hierbas'
        return texto