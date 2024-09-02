class Jogador:
    def __init__(self, nome, nivel_itn):
        self.nome = nome
        self.nivel_itn = nivel_itn

    def __repr__(self):
        return f"{self.nome}, ITN: {self.nivel_itn}"
