import random
import string

caracteres_permitidos = string.ascii_letters + string.digits + "!@#$%&"

tamanho_da_senha = 12
senha_gerada = ''.join(random.choice(caracteres_permitidos) for _ in range(tamanho_da_senha))

print(senha_gerada)
