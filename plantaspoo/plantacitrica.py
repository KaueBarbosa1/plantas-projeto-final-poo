from plantafrutifera import PlantaFrutifera

class PlantaCitrica(PlantaFrutifera):
    def __init__(self, nome, altura, necessidade_agua, tipo_fruto, acidez, habitat):
        super().__init__(nome, altura, necessidade_agua, tipo_fruto, habitat)
        self._acidez = acidez
        self.habitat = habitat

    def descrever(self):
        return f"A planta {self._nome} produz {self._tipo_fruto}, tem {self._altura}m de altura, precisa de {self._necessidade_agua}L de água e tem acidez {self._acidez}. e vive no habitat {self._habitat}."