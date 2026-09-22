from Models.personaje import Personaje
from Repository.personaje_repository import guardar


def crear_personaje(nombre, clase, nivel, vida):

    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

    if not isinstance(nivel, int):
        raise ValueError("El nivel debe ser un número entero")

    if nivel < 1 or nivel > 100:
        raise ValueError("El nivel debe estar entre 1 y 100")

    if clase not in ["Guerrero", "Mago", "Arquero"]:
        raise ValueError("La clase debe ser Guerrero, Mago o Arquero")

    personaje = Personaje(nombre, clase, nivel, vida)

    guardar(personaje)

    return personaje