from planta import Planta

class PlantaMedicinal(Planta):
    def __init__(self, nome, altura, necessidade_agua, propriedade_medicinal, habitat):
        super().__init__(nome, altura, necessidade_agua, habitat)
        self._propriedade_medicinal = propriedade_medicinal
        self.habitat = habitat

    def descrever(self):
        return f"A planta {self._nome} tem {self._altura}m de altura, precisa de {self._necessidade_agua}L de água e possui propriedades medicinais como {self._propriedade_medicinal}. e vive no habitat {self._habitat}."
