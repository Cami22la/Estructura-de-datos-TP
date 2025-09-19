class ServidorCorreo:
    """
    Clase que representa el servidor de correo electronico.
    Gestiona usuarios, mensajes y proporciona interfaz para operaciones del sistema.
    """
    
    def __init__(self, nombre, dominio):
        # Atributos privados (encapsulamiento)
        self._nombre = nombre
        self._dominio = dominio
        self._usuarios = {}
    
    # PROPIEDADES (GETTERS) 
    @property
    def nombre(self):
        """Getter para el nombre del servidor"""
        return self._nombre
    
    @property
    def dominio(self):
        """Getter para el dominio del servidor"""
        return self._dominio
    
    # METODOS PUBLICOS 
    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en el servidor
        """
        if usuario.direccion_correo not in self._usuarios:
            self._usuarios[usuario.direccion_correo] = usuario
            print(f"Usuario registrado: {usuario.direccion_correo}")
            return True
        else:
            print(f"El usuario {usuario.direccion_correo} ya existe")
            return False
    
    def enviar_mensaje(self, mensaje):
        """
        Procesa el envío de un mensaje a todos sus destinatarios
        """
        print(f"Procesando mensaje: '{mensaje.asunto}'")
        
        exitoso = True
        for destinatario in mensaje.destinatarios:
            if destinatario in self._usuarios:
                usuario_destino = self._usuarios[destinatario]
                usuario_destino.agregar_mensaje_a_carpeta("inbox", mensaje)
                print(f"Entregado a: {destinatario}")
            else:
                print(f"Destinatario no encontrado: {destinatario}")
                exitoso = False
        
        return exitoso
    
    def obtener_usuario(self, email):
        """
        Obtiene un usuario por su direccion de email
        """
        return self._usuarios.get(email)
    
    def listar_usuarios(self):
        """
        Retorna la lista de emails de usuarios registrados
        """
        return list(self._usuarios.keys())
    
    def cantidad_usuarios(self):
        """
        Retorna la cantidad de usuarios registrados
        """
        return len(self._usuarios)
    
    def autenticar_usuario(self, email, contraseña):
        """
        Autentica a un usuario con su email y contraseña
        """
        usuario = self.obtener_usuario(email)
        if usuario and hasattr(usuario, 'verificar_contraseña'):
            return usuario.verificar_contraseña(contraseña)
        return False
    
    def __str__(self):
        """Representacion en string del servidor"""
        return f"Servidor: {self._nombre} | Dominio: {self._dominio} | Usuarios: {self.cantidad_usuarios()}"