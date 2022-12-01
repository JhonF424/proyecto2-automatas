import json


class json:
    def __init__(self, url: str):
        self.my_json = self.leer_json(url)

    @staticmethod
    def leer_json(url: str) -> dict:
        try:
            with open(url) as mi_json:
                dict_datos = json.load(mi_json)
                return dict_datos
        except FileNotFoundError:
            print("Error archivo no encontrado, nombre del error: {}".format(
                FileNotFoundError))
            dict_datos = {}
            return dict_datos
