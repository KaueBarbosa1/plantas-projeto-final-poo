from plantafrutifera import PlantaFrutifera
from plantamedicinal import PlantaMedicinal
from plantacitrica import PlantaCitrica
from cupula import Cupula

if __name__ == "__main__":
    maracuja = PlantaFrutifera("Maracujá", 3, 5, "fruto amarelo", "floresta tropical")
    babosa = PlantaMedicinal("Babosa", 0.3, 1, "cicatrizante e hidratante", "cerrado seco")
    limao = PlantaCitrica("Limão", 4, 6, "fruto cítrico", "azedo", "regiões subtropicais")

    print(maracuja.descrever())
    print(babosa.descrever())
    print(limao.descrever())

    cupula_plantas = Cupula("Plantas")
    cupula_plantas.adicionar_planta(maracuja)
    cupula_plantas.adicionar_planta(babosa)
    cupula_plantas.adicionar_planta(limao)

    cupula_plantas.listar_plantas()
