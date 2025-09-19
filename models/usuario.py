class Usuario:
    """
    Clase que representa un usuario del sistema de correo electrónico.
    Implementa encapsulamiento con atributos privados y métodos de acceso controlado.
    """
    
    def __init__(self, nombre, direccion_correo, contraseña):
        # Atributos privados (encapsulamiento)
        self._nombre = nombre
        self._direccion_correo = direccion_correo
        self._contraseña = contraseña
        self._carpetas = {
            "inbox": [],
            "sent": [],
            "drafts": []
        }
    
    # ========== PROPIEDADES (GETTERS) ==========
    @property
    def nombre(self):
        """Getter para el nombre del usuario"""
        return self._nombre
    
    @property
    def direccion_correo(self):
        """Getter para la dirección de correo"""
        return self._direccion_correo
    
    # ========== MÉTODOS PÚBLICOS ==========
    def agregar_mensaje_a_carpeta(self, nombre_carpeta, mensaje):
        """
        Agrega un mensaje a una carpeta específica
        """
        if nombre_carpeta in self._carpetas:
            self._carpetas[nombre_carpeta].append(mensaje)
            return True
        return False
    
    def obtener_carpeta(self, nombre_carpeta):
        """
        Retorna los mensajes de una carpeta específica
        """
        return self._carpetas.get(nombre_carpeta)
    
    def listar_carpetas(self):
        """
        Retorna la lista de carpetas disponibles
        """
        return list(self._carpetas.keys())
    
    def verificar_contraseña(self, contraseña):
        """
        Verifica si la contraseña proporcionada es correcta
        """
        return self._contraseña == contraseña
    
    def __str__(self):
        """Representación en string del usuario"""
        return f"Usuario: {self._nombre} ({self._direccion_correo})"