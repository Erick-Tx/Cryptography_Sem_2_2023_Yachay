
M = 8
e = 5
p = 269

#is prime
def es_primo(p):
    if p <= 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if es_primo(p) == True:
    #Calculate
    result = (M**e)%p
    print("El resultado obtenido es:", result)

else:
    print("'p' no es un número primo.")
