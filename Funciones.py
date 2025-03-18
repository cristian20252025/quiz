def pares_primos_gemelos(limite):
    pares_gemelos=[]
    for numero in range (2,limite):
        if es_primo(numero) and es_primo(numero +2 ):
            pares_gemelos.append((numero, numero + 2))
    return pares_gemelos

def es_primo(numero):
    if numero<2:
        return False
    for i in range(2,int(numero**0.5) + 1):
        if numero % i ==0:
            return False
        return True
