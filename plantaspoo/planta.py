from abc import ABC, abstractmethod

class Planta(ABC):
    def __init__(self, nome, altura, necessidade_agua, habitat):
        self._nome = nome
        self._altura = altura
        self._necessidade_agua = necessidade_agua
        self._habitat = habitat

    @abstractmethod
    def descrever(self):
        pass

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("A altura deve ser positiva.")

    def get_necessidade_agua(self):
        return self._necessidade_agua

    def set_necessidade_agua(self, necessidade_agua):
        self._necessidade_agua = necessidade_agua

    def get_habitat(self):
        return self._habitat

    def set_habitat(self, habitat):
        self._habitat = habitat



