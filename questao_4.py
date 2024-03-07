def calcular_total_mensal(faturamento_estados):
    return sum(faturamento_estados.values())

def calcular_percentuais(faturamento_estados):
    total_mensal = calcular_total_mensal(faturamento_estados)
    percentuais = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_estados.items()}
    return percentuais

def imprimir_percentuais(percentuais):
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

def main():
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
    percentuais = calcular_percentuais(faturamento_estados)
    imprimir_percentuais(percentuais)

if __name__ == "__main__":
    main()
