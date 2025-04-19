from abc import ABC, abstractmethod
import re;

#nella mia idea la classe scachhiera andra a controllar lei se il pedone esiste o meno nella mossa del giocatore e poi
#passera la mossa alla pedina per controllare se è valida o meno

#pensandoci bene il pedone non deve sapere se è presente o meno sulla scacchiera e nemmeno la sua posizione iniziale
#la scacchiera deve sapere se il pedone è presente o meno e la sua posizione iniziale
#la pedina deve sapere solo se la mossa è valida o meno

#immagino anche di fare la funzione per controllare se la mossa del pedone è una mangiata 

#([a-h])([2-7]) ([a-h])([3-6]) questa regex controlla le mangiate laterali

patternSingolaMossa = re.compile(r"^[a-h][1-8]$")
patternMossaCompleta = re.compile(r"^[a-h][1-8] [a-h][1-8]$")
coloriAccettati = ["bianco", "nero"]

class Pedina(ABC):
 

    def __init__(self, nome,colore, posizioneInizialeScacchiera):
        if not isinstance(nome, str) or not isinstance(colore, str) or not isinstance(posizioneInizialeScacchiera, str):
            raise TypeError("Il nome ed il colore devono essere stringhe e la posizione iniziale deve essere iserita in notazione algebraica (es a2 a4)")
        elif patternSingolaMossa.match(posizioneInizialeScacchiera) is None:
            raise ValueError("La posizione inserita non è valida. Inserire la posizione in notazione algebraica rappresentante una casella sulla scacchiera(es a2 a4)")
        elif colore.lower() not in coloriAccettati:
            raise ValueError("Il colore deve essere bianco o nero")
        else:
            self.nome = nome
            self.colore = colore.lower()
            self.posizioneInizialeScacchiera = posizioneInizialeScacchiera
            
        
    
    def __str__(self):
        return f"{self.nome} {self.colore}"
    #getters
    def getNome(self):
        return self.nome
    def getColore(self):
        return self.colore
    def getposizioneInizialeScacchiera(self):
        return self.posizioneInizialeScacchiera
    #setters
    def setNome(self, nome):
        self.nome = nome
    def setColore(self, colore):
        self.colore = colore
    def setposizioneInizialeScacchiera(self, posizioneInizialeScacchiera):
        self.posizioneInizialeScacchiera = posizioneInizialeScacchiera
    #metodi astratti
    @abstractmethod
    def possibiliMosse(self):
        pass



class Pedone(Pedina):
    def __init__(self,colore, posizioneInizialeScacchiera):
        super().__init__("Pedone", colore, posizioneInizialeScacchiera)
      
    def __str__(self):
        return super().__str__()
    
    def possibiliMosse(self,mossa :str,primaMossaPedone : bool): #la mia idea è che i controlli della validita sintattici della mossa siano fatti dalla scacchiera, quindi alla funzione arriva una mossa già valida sintatticamente, devo solo controllare se la  mossa è valida per la pedina ma sintatiticamente è gia valida per gli scacchi in generale
                                                            
        if self.colore =="bianco":
            if primaMossaPedone:
                mossadiPartenza= mossa.split(" ")[0]
                mossaDiArrivo= mossa.split(" ")[1]
                if mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == 2:
                    return True
                elif mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == 1:
                    return True
                else :
                    return False
            else:
                mossadiPartenza= mossa.split(" ")[0]
                mossaDiArrivo= mossa.split(" ")[1]
                if mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == 1:
                    return True
                else :
                    return False
            
        else:  
            if primaMossaPedone:
                mossadiPartenza= mossa.split(" ")[0]
                mossaDiArrivo= mossa.split(" ")[1]
                if mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == -2:
                    return True
                elif mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == -1:
                    return True
                else :
                    return False
            else:
                mossadiPartenza= mossa.split(" ")[0]
                mossaDiArrivo= mossa.split(" ")[1]
                if mossadiPartenza[0] == mossaDiArrivo[0] and int(mossaDiArrivo[1]) - int(mossadiPartenza[1]) == -1:
                    return True
                else :
                    return False
            

pedone= Pedone("bianco", "a2")
print(pedone.possibiliMosse("a2 a4",True))
print(pedone.possibiliMosse("a2 a4",False))    
if patternMossaCompleta.match("a2 b3") is None:
    print("La mossa non è valida")
else:
    print("La mossa è valida")

