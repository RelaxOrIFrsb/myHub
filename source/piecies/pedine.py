from abc import ABC, abstractmethod
import re;

patternSingolaMossa = re.compile(r"^[a-h][1-8]$")
patternMossaCompleta = re.compile(r"^[a-h][1-8] [a-h][1-8]$")


class Pedina:

    
    def __init__(self, nome, colore, posizioneIniziale):
        if not isinstance(nome, str):
            raise ValueError("Il nome deve essere una stringa.")
        elif not isinstance(colore, str):
            raise ValueError("Il colore deve essere una stringa.")
        elif not isinstance(posizioneIniziale, str) or patternSingolaMossa.match(posizioneIniziale) is None: 
            raise ValueError("La posizione iniziale deve essere una stringa nel formato 'a1', 'b2', ecc.")
        

  