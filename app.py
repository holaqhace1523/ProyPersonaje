from flask import Flask, request, jsonify
from Services.personaje_service import crear_personaje
from Repository.personaje_repository import obtener_todos

app = Flask(__name__)


@app.route("/personajes", methods=["GET"])
def personajes():
    lista = obtener_todos()

    return jsonify([personaje.to_dict() for personaje in lista])


@app.route("/personajes/crear", methods=["POST"])
def crear():

    datos = request.get_json()

    try:
        personaje = crear_personaje(
            datos["nombre"],
            datos["clase"],
            datos["nivel"],
            datos["vida"]
        )

        return jsonify(personaje.to_dict()), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)