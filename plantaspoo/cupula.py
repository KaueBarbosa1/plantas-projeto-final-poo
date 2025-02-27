from planta import Planta

class Cupula:
    def __init__(self, nome):
        self.nome = nome
        self.plantas = []

    def adicionar_planta(self, planta):
        if isinstance(planta, Planta):
            self.plantas.append(planta)
            print(f"A planta {planta.get_nome()} foi adicionada à cúpula {self.nome}.")
        else:
            print("Apenas objetos do tipo Planta podem ser adicionados à cúpula.")

    def listar_plantas(self):
        if self.plantas:
            print(f"Plantas na cúpula {self.nome}:")
            for planta in self.plantas:
                print(planta.descrever())
        else:
            print(f"A cúpula {self.nome} está vazia.")