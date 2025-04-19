from abc import ABC, abstractmethod
import re;

#nella mia idea la classe scachhiera andra a controllar lei se il pedone esiste o meno nella mossa del giocatore e poi
#passera la mossa alla pedina per controllare se è valida o meno

#pensandoci bene il pedone non deve sapere se è presente o meno sulla scacchiera e nemmeno la sua posizione iniziale
#la scacchiera deve sapere se il pedone è presente o meno e la sua posizione iniziale
#la pedina deve sapere solo se la mossa è valida o meno

#immagino anche di fare la funzione per controllare se la mossa del pedone è una mangiata 
#adesso viene capita anche la mossa di mangiata,sarà la scacchiera a controllare se il pedone è presente o meno e se potra mangiare qualcosa
#([a-h])([2-7]) ([a-h])([3-6]) questa regex controlla le mangiate laterali
#la mia idea è che i controlli della validita sintattici della mossa siano fatti dalla scacchiera, quindi alla funzione arriva una mossa già valida sintatticamente, devo solo controllare se la  mossa è valida per la pedina ma sintatiticamente è gia valida per gli scacchi in generale


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
 
    def getNome(self):
        return self.nome
    def getColore(self):
        return self.colore
    def getposizioneInizialeScacchiera(self):
        return self.posizioneInizialeScacchiera
  
    def setNome(self, nome):
        self.nome = nome
    def setColore(self, colore):
        self.colore = colore
    def setposizioneInizialeScacchiera(self, posizioneInizialeScacchiera):
        self.posizioneInizialeScacchiera = posizioneInizialeScacchiera
    def calcolaDifferenze(self, mossa: str):
        mossadiPartenza, mossaDiArrivo = mossa.split(" ")
        differenzaColonne = abs(ord(mossaDiArrivo[0]) - ord(mossadiPartenza[0]))
        differenzaRighe = abs(int(mossaDiArrivo[1]) - int(mossadiPartenza[1]))
        return differenzaColonne, differenzaRighe
    
    @abstractmethod
    def possibiliMosse(self):
        pass



class Pedone(Pedina):
    def __init__(self,colore, posizioneInizialeScacchiera):
        super().__init__("Pedone", colore, posizioneInizialeScacchiera)
      
    def __str__(self):
        return super().__str__()
    
    def possibiliMosse(self,mossa :str,primaMossaPedone : bool) -> bool: 
        
       
        mossadiPartenza, mossaDiArrivo = mossa.split(" ")

        differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)


        if mossadiPartenza[0] == mossaDiArrivo[0]:
            if self.colore == "bianco" and differenzaRighe in [1, 2] and primaMossaPedone:
                return True
            elif self.colore == "bianco" and differenzaRighe == 1:
                return True
            elif self.colore == "nero" and differenzaRighe in [-1, -2] and primaMossaPedone:
                return True
            elif self.colore == "nero" and differenzaRighe == -1:
                return True

        
        if differenzaColonne == 1:
            if self.colore == "bianco" and differenzaRighe == 1:
                return True
            elif self.colore == "nero" and differenzaRighe == -1:
                return True

        return False

class Cavallo(Pedina):
    def __init__(self,colore, posizioneInizialeScacchiera):
        super().__init__("Cavallo", colore, posizioneInizialeScacchiera)
      
    def __str__(self):
        return super().__str__()
    
    def possibiliMosse(self,mossa :str)->bool: 
        mossadiPartenza, mossaDiArrivo = mossa.split(" ")
        differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)
       
        if (differenzaColonne == 2 and differenzaRighe == 1) or (differenzaColonne == 1 and differenzaRighe == 2):
            return True
        else:   
            return False



class Torre(Pedina):
    def __init__(self,colore, posizioneInizialeScacchiera):
        super().__init__("Torre", colore, posizioneInizialeScacchiera)
    def __str__(self):
        return super().__str__()
    def possibiliMosse(self,mossa :str)->bool: 
        
        differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)
      
        if (differenzaColonne == 0 and differenzaRighe > 0) or (differenzaColonne > 0 and differenzaRighe == 0):
            return True
        else:
            return False

class Alfiere(Pedina):
    def __init__(self,colore, posizioneInizialeScacchiera):
        super().__init__("Alfiere", colore, posizioneInizialeScacchiera)
    def __str__(self):
        return super().__str__()
    def possibiliMosse(self,mossa :str) -> bool: 
        mossadiPartenza, mossaDiArrivo = mossa.split(" ")
        differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)
    
        if differenzaColonne == differenzaRighe and differenzaColonne > 0:
            return True
        else:
            return False

class Regina(Pedina):
      def __init__(self, colore, posizioneInizialeScacchiera):
        super().__init__("Regina", colore, posizioneInizialeScacchiera)

      def __str__(self):
         return super().__str__()

      def possibiliMosse(self, mossa: str) -> bool:
          
          mossadiPartenza, mossaDiArrivo = mossa.split(" ")

          differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)

          return (
            (differenzaColonne == 0 and differenzaRighe > 0) or
            (differenzaRighe == 0 and differenzaColonne > 0) or
            (differenzaColonne == differenzaRighe and differenzaColonne > 0)
          )
      
class Re(Pedina):
    def __init__(self, colore, posizioneInizialeScacchiera):
        super().__init__("Re", colore, posizioneInizialeScacchiera)

    def __str__(self):
        return super().__str__()

    def possibiliMosse(self, mossa: str) -> bool:

        mossadiPartenza, mossaDiArrivo = mossa.split(" ")

        differenzaColonne, differenzaRighe = self.calcolaDifferenze(mossa)
        
        if (differenzaColonne <= 1 and differenzaRighe <= 1) and (differenzaColonne > 0 or differenzaRighe > 0):
            return True

        return False
    
