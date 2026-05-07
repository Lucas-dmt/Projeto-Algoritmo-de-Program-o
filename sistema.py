def ajuste_termico(leitura):
    if leitura > 150:
        return leitura * 1.08
    else:
        return leitura * 0.96


def classificar_zona(leitura_ajustada):
    if 120 <= leitura_ajustada <= 180:
        return "VERDE"
    elif leitura_ajustada < 250:
        return "AMARELA"
    else:
        return "VERMELHA"


n = int(input("digite o número de leituras: "))
soma = 0
maior = 0
menor = 10**9
verdes = 0
amarela = 0
total = 0
vermelhas_consecutivas = 0
travado = False
i = 0

while i < n:
    leitura = float(input(f"Leitura {i+1}: "))

    if leitura > 150:
        leitura = ajuste_termico(leitura)
        print("Acréscimo de 8% (expansão térmica.)")
    else:
        leitura = ajuste_termico(leitura)
        print("Redução de 4% (contração)")

    soma += leitura
    total += 1

    if leitura < menor:
        menor = leitura
    if leitura > maior:
        maior = leitura

    zona = classificar_zona(leitura)

    if zona == "VERDE":
        verdes += 1
        vermelhas_consecutivas = 0
        print("=== ZONA VERDE ===")
        print("OK: Sistema operando dentro da estabilidade")
    elif zona == "AMARELA":
        amarela += 1
        vermelhas_consecutivas = 0
        print("ATENÇÃO: Pressão fora do padrão ideal")
        print("=== ZONA AMARELA ===")
    else:
        print("ALERTA CRÍTICO: Risco operacional detectado! ")
        print("=== ZONA VERMELHA ===")
        vermelhas_consecutivas += 1
        if vermelhas_consecutivas >= 2:
            print("sistema travado: dois picos críticos consecutivos!")
            travado = True
            break

    i += 1

media = soma / total
percentual_verde = (verdes / total) * 100
percentual_amarela = (amarela / total) * 100
percentual_vermelha = (vermelhas_consecutivas / total) * 100

print("\n === RESULTADOS FINAIS ===")
print("A média das pressões é:", media)
print(f"Das {n} leituras, {percentual_verde}% são verdes ")
print(f"Das {n} leituras, {percentual_amarela}% são amarelas")
print(f"Das {n} leituras, {percentual_vermelha}% são vermelhas")
print("A menor pressão foi:", menor)
print("A maior pressão foi:", maior)

if travado:
    percentual = (total / n) * 100
    print(f"Processo interrompido com {percentual:.2f}% das leituras realizadas")
