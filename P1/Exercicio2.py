def main():
  
    base = float(input("Digite a base: "))
    exp  = int(input("Digite o expoente inteiro: "))
    pot  = potencia(base, exp)
    print("potencia({}, {}) = {}".format(base, exp, pot))

def potencia(base, expoente):

    pot = (expoente ** base)

    return pot

main()


