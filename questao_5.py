def inverter_string(texto):
    texto_invertido = ''
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

def main():
    string_original = input("Digite a string que deseja inverter: ")
    string_invertida = inverter_string(string_original)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
