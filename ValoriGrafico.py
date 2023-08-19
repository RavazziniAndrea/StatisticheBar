import DatiNonValidiException

class ValoriGrafico:

    def __init__(self, grafico, tempo):
        if not self.check_valid(grafico, tempo):
            raise DatiNonValidiException("Valori a null. Errore")
        self.grafico = grafico
        self.tempo = tempo

    def check_valid(grafico, tempo):
        return grafico == None or tempo == None 

    def get_grafico(self):
        return self.grafico
    
    def set_grafico(self, grafico):
        self.grafico = grafico

    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, tempo):
        self.tempo = tempo