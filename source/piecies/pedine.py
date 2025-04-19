from abc import ABC, abstractmethod
import re;


patternSingolaMossa = re.compile(r"^[a-h][1-8]$")
patternMossaCompleta = re.compile(r"^[a-h][1-8] [a-h][1-8]$")
coloriAccettati = ["bianco", "nero"]

class Pedina(ABC):

    



    def __init__(self, nome,colore, posizioneIniziale):
        if not isinstance(nome, str) or not isinstance(colore, str) or not isinstance(posizioneIniziale, str):
            raise TypeError("Il nome ed il colore devono essere stringhe e la posizione iniziale deve essere iserita in notazione algebraica (es a2 a4)")
        elif patternSingolaMossa.match(posizioneIniziale) is None:
            raise ValueError("La posizione inserita non è valida. Inserire la posizione in notazione algebraica rappresentante una casella sulla scacchiera(es a2 a4)")
        elif colore.lower() not in coloriAccettati:
            raise ValueError("Il colore deve essere bianco o nero")
        else:
            self.nome = nome
            self.colore = colore.lower()
            self.posizioneIniziale = posizioneIniziale
            self.posizioneAttuale = posizioneIniziale
        
    
    def __str__(self):
        return f"{self.nome} {self.colore} {self.posizioneAttuale}"
    #getters
    def getNome(self):
        return self.nome
    def getColore(self):
        return self.colore
    def getPosizioneIniziale(self):
        return self.posizioneIniziale
    def getPosizioneAttuale(self):
        return self.posizioneAttuale
    #setters
    def setNome(self, nome):
        self.nome = nome
    def setColore(self, colore):
        self.colore = colore
    def setPosizioneIniziale(self, posizioneIniziale):
        self.posizioneIniziale = posizioneIniziale
    def setPosizioneAttuale(self, posizioneAttuale):    
        self.posizioneAttuale = posizioneAttuale
    #metodi astratti
    @abstractmethod
    def mossePossibili(self):
        pass



pedoni=Pedina("pedone", "bianco", "a2")