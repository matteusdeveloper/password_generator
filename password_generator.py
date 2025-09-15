import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    """
    Gera uma senha aleatória e segura.

    Args:
        length (int): O comprimento da senha.
        include_uppercase (bool): Inclui letras maiúsculas.
        include_numbers (bool): Inclui números.
        include_symbols (bool): Inclui símbolos.

    Returns:
        str: A senha gerada.
    """
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        return "Erro: Nenhuma opção de caractere selecionada."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Função principal para interagir com o usuário e gerar a senha.
    """
    print("Bem-vindo(a) ao Gerador de Senhas!")

    try:
        length = int(input("Digite o comprimento da senha desejada (ex: 12): "))
        if length <= 0:
            print("O comprimento deve ser um número positivo.")
            return

        include_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        include_numbers = input("Incluir números? (s/n): ").lower() == 's'
        include_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"\nSua senha gerada é: {password}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o comprimento.")

if __name__ == "__main__":
    main()
