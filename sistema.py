n = int(input("digite o número de leituras: "))
soma = 0
menor = 10**9
verdes = 0
total = 0
vermelhas_consecutivas = 0
travado = False
i = 0

while i < n:
    leitura = float(input(f"Leitura {i+1}: "))
    
    if leitura > 150:
        leitura = leitura * 1.08
    else:
        leitura = leitura * 0.96
    
    soma += leitura
    total += 1
    
    if leitura < menor:
        menor = leitura
    
    if 120 <= leitura <= 180:
        verdes += 1
        vermelhas_consecutivas = 0
    elif leitura < 250:
        vermelhas_consecutivas = 0
    else:
        vermelhas_consecutivas += 1
        if vermelhas_consecutivas >= 2:
            print("sistema travado: dois picos críticos consecutivos!")
            travado = True
            break
    
    i += 1
