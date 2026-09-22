class Personaje:

    def __init__(self, nombre, clase, nivel, vida):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida = vida

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "clase": self.clase,
            "nivel": self.nivel,
            "vida": self.vida
        }