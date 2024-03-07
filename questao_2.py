def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def main():
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()