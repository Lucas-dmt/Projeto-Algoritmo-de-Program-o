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
menor = 10**9
verdes = 0
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

    zona = classificar_zona(leitura)

    if zona == "VERDE":
        verdes += 1
        vermelhas_consecutivas = 0
        print("=== ZONA VERDE ===")
    elif zona == "AMARELA":
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

media = soma / total
percentual_verde = (verdes / total) * 100

print("\n === RESULTADOS FINAIS ===")
print("A média das pressões é:", media)
print(f"Das {n} leituras, {percentual_verde}% são verdes ")
print("A menor pressão foi:", menor)

if travado:
    percentual = (total / n) * 100
    print(f"Processo interrompido com {percentual:.2f}% das leituras realizadas")
