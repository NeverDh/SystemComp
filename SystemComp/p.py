import subprocess
from sys import stdout


x = subprocess.Popen(["wmic", "bios", "get", "serialnumber"], stdout=subprocess.PIPE, shell=True)
z = str(x.communicate())

h = 0
l = 0


while  z[0 + h: 2 + h] != r"\n" :
    h = h + 1
    
while z[h: 1+h] != " " :
    h = h + 1
    l = l + 1

a = z[h - l + 2: h]



x = subprocess.Popen(["systeminfo"], stdout=subprocess.PIPE, shell=True)
z = str(x.communicate())

w = 0



while z[1 + w : 19 + w] != "Modelo do sistema:":
    w = w + 1

i = w
while  z[w + 44: w + 46] != r"\r" :
    w = w + 1

b = z[i + 44: w + 44]

print("\nCOPIE E COLE AS INFORMAÇÕES NO FORMULARIO!\n")

print("NÚMERO DE PATRIMÔNIO:\n" + a + "\n")
print("MODELO:\n" + b + "\n")

input("PRESSIONE ENTER PARA SAIR")




