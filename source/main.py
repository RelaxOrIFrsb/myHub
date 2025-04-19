from piecies.pedinev3 import *
def main():
    # Testing
     pedone_bianco = Pedone("bianco", "a2")
     pedone_nero = Pedone("nero", "a7")

# Test mosse valide
     print("\nCasi di test per il pedone:\n")
     print(pedone_bianco.possibiliMosse("a2 a4", True))  # True (prima mossa, due passi)
     print(pedone_bianco.possibiliMosse("a2 a3", False))  # True (un passo)
     print(pedone_bianco.possibiliMosse("a2 b3", False))  # True (mangiata in diagonale)

     print(pedone_nero.possibiliMosse("a7 a5", True))  # True (prima mossa, due passi)
     print(pedone_nero.possibiliMosse("a7 a6", False))  # True (un passo)
     print(pedone_nero.possibiliMosse("a7 b6", False))  # True (mangiata in diagonale)

# Test mosse non valide
     print(pedone_bianco.possibiliMosse("a2 a5", True))  # False (troppi passi)
     print(pedone_bianco.possibiliMosse("a2 b4", False))  # False (mossa diagonale senza mangiata)
     print(pedone_nero.possibiliMosse("a7 a4", True))  # False (troppi passi)
     print(pedone_nero.possibiliMosse("a7 b5", False))  # False (mossa diagonale senza mangiata)

# Test con un cavallo
     # Testing
     cavallo = Cavallo("bianco", "b1")

        # Test mosse valide
     print("\nCasi di test per il cavallo:\n")
     print(cavallo.possibiliMosse("b1 a3"))  # True (mossa valida)
     print(cavallo.possibiliMosse("b1 c3"))  # True (mossa valida)
     print(cavallo.possibiliMosse("b1 d2"))  # True (mossa valida)

        # Test mosse non valide
     print(cavallo.possibiliMosse("b1 b3"))  # False (non è una mossa a "L")
     print(cavallo.possibiliMosse("b1 c4"))  # False (non è una mossa a "L")
     
     print("\nCasi di test per la torre:\n")
     # Testing
     torre = Torre("bianco", "a1")

    # Test mosse valide
     print(torre.possibiliMosse("a1 a8"))  # True (movimento verticale)
     print(torre.possibiliMosse("a1 h1"))  # True (movimento orizzontale)

    # Test mosse non valide
     print(torre.possibiliMosse("a1 b2"))  # False (movimento diagonale)
     print(torre.possibiliMosse("a1 c3"))  # False (movimento non lineare)

     # Test con un alfiere
     alfiere = Alfiere("bianco", "c1")
     # Test mosse valide
     print("\nCasi di test per l'alfiere:\n")
     print(alfiere.possibiliMosse("c1 d2"))  # True (movimento diagonale)
     print(alfiere.possibiliMosse("c1 b2"))  # True (movimento diagonale)
     print(alfiere.possibiliMosse("c1 a3"))  # True (movimento diagonale)
     # Test mosse non valide
     print(alfiere.possibiliMosse("c1 c2"))  # False (movimento verticale)
     print(alfiere.possibiliMosse("c1 d3"))  # False (movimento non diagonale)
     print(alfiere.possibiliMosse("c1 e2"))  # False (movimento non diagonale)

      # Testing
     regina = Regina("bianco", "d1")

    # Test mosse valide
     print("\nCasi di test per la regina:\n")
     print(regina.possibiliMosse("d1 d8"))  # True (movimento verticale)
     print(regina.possibiliMosse("d1 h1"))  # True (movimento orizzontale)
     print(regina.possibiliMosse("d1 h5"))  # True (movimento diagonale)
     print(regina.possibiliMosse("d1 a4"))  # True (movimento diagonale)

    # Test mosse non valide
     print(regina.possibiliMosse("d1 e3"))  # False (non è una mossa valida)
     print(regina.possibiliMosse("d1 c3"))  # False (non è una mossa valida)


     # Testing
     re = Re("bianco", "e1")

        # Test mosse valide
     print("\nCasi di test per il re:\n")
     print(re.possibiliMosse("e1 e2"))  # True (movimento verticale)
     print(re.possibiliMosse("e1 f1"))  # True (movimento orizzontale)
     print(re.possibiliMosse("e1 f2"))  # True (movimento diagonale)
     print(re.possibiliMosse("e1 d2"))  # True (movimento diagonale)

        # Test mosse non valide
     print(re.possibiliMosse("e1 e3"))  # False (troppo lontano)
     print(re.possibiliMosse("e1 g1"))  # False (troppo lontano)
     print(re.possibiliMosse("e1 c3"))  # False (non è una mossa valida)
if __name__ == "__main__":
    main()
