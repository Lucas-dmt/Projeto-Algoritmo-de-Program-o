def ajustar(leitura):
    if leitura > 150:
        print("Acréscimo de 8%")
        return leitura * 1.08
    else:
        print("Redução de 4%")
        return leitura * 0.96


def zona(leitura):
    if 120 <= leitura <= 180:
        print("=== VERDE ===")
        return "verde"
    elif leitura < 250:
        print("=== AMARELA ===")
        return "amarela"
    else:
        print("=== VERMELHA ===")
        return "vermelha"


n = int(input("Digite o número de leituras: "))

soma = 0
verdes = 0
vermelhas_consecutivas = 0
total = 0

for i in range(n):
    leitura = float(input(f"Leitura {i+1}: "))

    leitura = ajustar(leitura)
    tipo = zona(leitura)

    soma += leitura
    total += 1

    # define o menor usando a primeira leitura
    if i == 0:
        menor = leitura
    elif leitura < menor:
        menor = leitura

    if tipo == "verde":
        verdes += 1
        vermelhas_consecutivas = 0

    elif tipo == "vermelha":
        vermelhas_consecutivas += 1

        if vermelhas_consecutivas >= 2:
            print("Sistema travado!")
            break
    else:
        vermelhas_consecutivas = 0


# resultados
print("\n=== RESULTADOS ===")

if total > 0:
    media = soma / total
    perc = (verdes / total) * 100
else:
    media = 0
    perc = 0

print(f"Média: {media:.2f}")
print(f"{perc:.2f}% verdes")
print(f"Menor valor: {menor}")