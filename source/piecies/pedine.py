from abc import ABC, abstractmethod
import re;

#nella mia idea la classe scachhiera andra a controllar lei se il pedone esiste o meno nella mossa del giocatore e poi
#passera la mossa alla pedina per controllare se è valida o meno

#pensandoci bene il pedone non deve sapere se è presente o meno sulla scacchiera e nemmeno la sua posizione iniziale
#la scacchiera deve sapere se il pedone è presente o meno e la sua posizione iniziale
#la pedina deve sapere solo se la mossa è valida o meno

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
            
        
    
    def __str__(self):
        return f"{self.nome} {self.colore}"
    #getters
    def getNome(self):
        return self.nome
    def getColore(self):
        return self.colore
    def getPosizioneIniziale(self):
        return self.posizioneIniziale
    #setters
    def setNome(self, nome):
        self.nome = nome
    def setColore(self, colore):
        self.colore = colore
    def setPosizioneIniziale(self, posizioneIniziale):
        self.posizioneIniziale = posizioneIniziale
    #metodi astratti
    @abstractmethod
    def convalidaMossa(self):
        pass



class Pedone(Pedina):
    def __init__(self,colore, posizioneIniziale):
        super().__init__("Pedone", colore, posizioneIniziale)
      
    def __str__(self):
        return super().__str__()
    
    def convalidaMossa(self,mossa):
        if not isinstance(mossa, str):
            raise TypeError("La mossa deve essere una stringa")
        elif patternMossaCompleta.match(mossa) is None:
            raise ValueError("La mossa inserita non è valida. Inserire la mossa in notazione algebraica (es a2 a4)")
        elif self.colore == "bianco":
            posizioneAttuale = mossa.split(" ")[0]
            posiziioneFinale = mossa.split(" ")[1]
            
            if posizioneAttuale ==self.posizioneIniziale:  #siamo nel caso iniziale del pedone dobbiamo poter dare la possibilità di muoverci di 1 o 2
                if posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])-1:
                    return True
                elif posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])-2:
                    return True
                else:   
                    return False
            else: #siamo nel caso in cui il pedone non è alla sua posizione iniziale
                if posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])-1:
                    return True
                else:   
                    return False #non può muoversi di 2 o comunque non puo andare indietro neanche a sinistra o destra
        elif self.colore == "nero":
            posizioneAttuale =mossa.split(" ")[0]
            posiziioneFinale = mossa.split(" ")[1]
            if posizioneAttuale ==self.posizioneIniziale:
                if posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])+1:
                    return True
                elif posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])+2:
                    return True
                else:   
                    return False
            else: 
                if posizioneAttuale[0]== posiziioneFinale[0] and int(posizioneAttuale[1])==int(posiziioneFinale[1])+1:
                    return True
                else:   
                    return False

        



pedone=Pedone("bianco", "a2")
print(pedone)
if pedone.convalidaMossa("a2 a4"):
    print("Mossa valida")
else:
    print("Mossa non valida")