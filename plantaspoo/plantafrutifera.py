from planta import Planta

class PlantaFrutifera(Planta):
    def __init__(self, nome, altura, necessidade_agua, tipo_fruto, habitat):
        super().__init__(nome, altura, necessidade_agua, habitat)
        self._tipo_fruto = tipo_fruto
        self.habitat = habitat

    def descrever(self):
        return f"A planta {self._nome} tem {self._altura}m de altura, precisa de {self._necessidade_agua}L de água e produz {self._tipo_fruto}. e vive no habitat {self._habitat}."