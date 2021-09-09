def main():
    quant_estancias = int(input())
    m, n = input().split()
    print(cria_vetor(m))


def cria_vetor(tamanho):
    vetor = [0]*(int(tamanho*2))
    return vetor

if __name__ == "__main__":
    main()