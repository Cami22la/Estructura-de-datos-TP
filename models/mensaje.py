class Mensaje:
    # Constructor
    def __init__(self, remitente, destinario, asunto, cuerpo, prioridad):
        self._remitente = remitente                
        self._destinatario = destinario            
        self._asunto = asunto                      
        self._cuerpo = cuerpo                      
        self._prioridad = prioridad                
        self._leido = False                        
        
    # PROPIEDADES (getters) 
    @property
    def remitente(self):
        return self._remitente
    
    @property
    def destinatario(self):
        # Se devuelve una copia de la lista de destinatarios para evitar modificarla desde afuera
        return self._destinatario.copy()
    
    @property 
    def asunto(self):
        return self._asunto
    
    @property
    def cuerpo(self):
        return self._cuerpo
    
    @property
    def prioridad(self):
        return self._prioridad
    
    @property
    def leido(self):
        return self._leido
    
    # MÉTODOS
    def marcar_como_leido(self):
        """Marca el mensaje como leído"""
        self._leido = True
        
    def marcar_como_no_leido(self):
        """Marca el mensaje como no leído"""
        self._leido = False
        
    def es_urgente(self):
        """Verifica si el mensaje tiene prioridad 'urgente'"""
        return self._prioridad == "urgente"
    
    def agregar_destinario(self, destinario):
        """Agrega un nuevo destinatario a la lista si no estaba antes"""
        if destinario not in self._destinatario:
            self._destinatario.append(destinario)
            
    def __str__(self):
        """Representación en texto del mensaje"""
        estado_urgencia = "urgente" if self.es_urgente() else "no urgente"
        estado_de_lectura = "leido" if self._leido else "no leido"
        return f"de: {self._remitente} | asunto: {self._asunto} | {estado_urgencia} | {estado_de_lectura}"   