import random
import string

caracteres_especiais = "@#$!%&"
letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits

todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

def gerar_senha(comprimento=12):
    senha = ''.join(random.choice(todos_caracteres) for _ in range(comprimento))
    return senha

comprimento_da_senha = 12  # Você pode ajustar o comprimento da senha conforme necessário
senha_gerada = gerar_senha(comprimento_da_senha)
print(senha_gerada)
