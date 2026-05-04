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
        print("Acréscimo de 8% (expansão térmica.)")
    else:
        leitura = leitura * 0.96
        print("Redução de 4% (contração)")
    soma += leitura
    total += 1
    if leitura < menor:
        menor = leitura
    if 120 <= leitura <= 180:
        verdes += 1
        vermelhas_consecutivas = 0
        print("=== ZONA VERDE ===")
    elif leitura < 250:
        vermelhas_consecutivas = 0
        print("=== ZONA AMARELA ===")
    else:
        print("=== ZONA VERMELHA ===")
        vermelhas_consecutivas += 1
        if vermelhas_consecutivas >= 2:
            print("sistema travado: dois picos críticos consecutivos!")
            travado = True
            break
    i += 1
media=soma/total
percentual_verde = (verdes/total)*100
print("\n === RESULTADOS FINAIS ===")
print("A média das pressões é:", media)
print(f"Das {n} leituras, {percentual_verde}% são verdes ")
print("A menor pressão foi:", menor)

if travado:
    percentual = (total/n)*100
    print(f"Processo interrompido com {percentual:.2f}% das leituras realizadas")