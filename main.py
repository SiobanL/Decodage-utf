def toHeightBit(s: str)-> str:
    """Convertis une chaine de caractere qui represente 1 octet sur moins de 8 bits

    Args:
        s (str): octet de moins de 8 bits

    Returns:
        str: un octet de 8 bits
    """
    temp: list = ["0","0","0","0","0","0","0","0"]

    for i in range(0, len(s), 1):
        temp[(len(temp)-1)-i] = s[len(s)-1-i]
    
    return "".join(temp)

def decToBin(i: int)-> str:
    """Convertis un nombre entier decimale en binaire

    Args:
        i (int): nombre a convertir

    Returns:
        str: nombre convertis en binaire
    """
    if (i == 0):
        return ""
    return decToBin(i//2) + str(i%2)

def parity(s: str)->str:
    """Verifie la parite binaire sur plusieurs bits et met un 1 logique si le nombre est pair 0 sinon

    Args:
        s (str): bits pour tester la parite

    Returns:
        str: bits avec la verification de la parité
    """
    t: int = 0
    for i in range(0, len(s), 1):
        if s[i] == "1":
            t += 1

    s = list(s)
    s[0] = "1" if (t%2 == 0) else "0"
    return "".join(s)

def prtBin(s:str)->str:
    """Convertis une chaine de caractere en valeur binaire ascii

    Args:
        s (str): chaine a convertir

    Returns:
        str: chaine converti avec verification de la parite
    """
    for i in s:
        print(ord(i))
        print(parity(toHeightBit(decToBin(ord(i)))))

def test()-> None:
    print(decToBin(10))
    print(decToBin(15))
    print(decToBin(16))
    print(parity(toHeightBit(decToBin(10))))

def main()->None:
    s: str = "Bons examen!"
    prtBin(s)
    # test()

if __name__ == "__main__":
    main()