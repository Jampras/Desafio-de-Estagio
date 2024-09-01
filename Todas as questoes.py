
print("")
print("")
#QUESTAO 1
print(" --------  QUESTAO 1  -------- ")
print("")
print (" 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;")
print ( "Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }")
print ("Imprimir(SOMA);")
print ("Ao final do processamento, qual será o valor da variável SOMA? ")
print("")
print("")

def calcular_soma(indice):

  soma = 0
  for k in range(1, indice):
    soma += k
  return soma

# Valores do problema original
indice = 13

# Chamando a função e imprimindo o resultado
resultado = calcular_soma(indice)
print(f"RESPOSTA: A soma dos números de 1 até {indice-1} é: {resultado}")

print("")
print("")

#QUESTAO 2

print(" --------  QUESTAO 2  -------- ")
print("")
print("2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.")
print("")
print("IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;")
print("")
print("")
def pertence_fibonacci(num):
    
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verificação e saída
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

print("")
print("")

#QUESTAO 3
print(" --------  QUESTAO 3  -------- ")
print("")
print(" 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:")
print(" • O menor valor de faturamento ocorrido em um dia do mês;")
print(" • O maior valor de faturamento ocorrido em um dia do mês;")
print(" • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.")
import json

# Exemplo de conteúdo JSON
faturamento_json = '''
{
    "faturamento_diario": [1000.0, 2000.0, 0.0, 0.0, 1500.0, 700.0, 1200.0, 0.0, 0.0, 2500.0,
                           800.0, 1500.0, 0.0, 1700.0, 2300.0, 4500.0, 3700.0, 0.0, 2100.0, 
                           0.0, 2900.0, 3100.0, 0.0, 0.0, 2200.0, 2800.0, 2600.0, 0.0, 0.0, 3000.0]
}
'''

# Carregar os dados do JSON
dados = json.loads(faturamento_json)
faturamento_diario = dados["faturamento_diario"]

# Filtrar apenas os dias com faturamento > 0
faturamento_valido = [f for f in faturamento_diario if f > 0]

# 1. Menor valor de faturamento ocorrido em um dia do mês
menor_faturamento = min(faturamento_valido)

# 2. Maior valor de faturamento ocorrido em um dia do mês
maior_faturamento = max(faturamento_valido)

# 3. Média mensal dos dias com faturamento > 0
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Número de dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for f in faturamento_valido if f > media_mensal)

# Exibindo os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media} dias")


print("")
print("")

#QUESTAO 4

print(" --------  QUESTAO 4  -------- ")
print("")
print("4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:")
print("• SP – R$67.836,43")
print ("• RJ – R$36.678,66")
print ("• MG – R$29.229,88")
print ("• ES – R$27.165,48")
print ("• Outros – R$19.849,53")
print ("")

print ("Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. ")

def calcular_percentual_estados(faturamento_por_estado):

  # Calcula o faturamento total
  faturamento_total = sum(faturamento_por_estado.values())

  # Calcula o percentual de cada estado
  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}

  return percentuais

# Dados de exemplo
faturamento = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'Outros': 19849.53
}

# Calcula os percentuais
resultados = calcular_percentual_estados(faturamento)

# Imprime os resultados
for estado, percentual in resultados.items():
  print(f"O estado {estado} representa {percentual:.2f}% do faturamento total.")

print ("")
print ("")

#QUESTAO 5 

print(" --------  QUESTAO 5  -------- ")
print("")
print("5) Escreva um programa que inverta os caracteres de um string.")
print("IMPORTANTE:")
print("a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;")
print("b) Evite usar funções prontas, como, por exemplo, reverse;")
print("")

def inverter_string(texto):
    """Inverte os caracteres de uma string."""
    return texto[::-1]

def menu_interativo():
    while True:
        print("Menu:")
        print("1. Digitar uma palavra")
        print("2. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao not in (1, 2):
                raise ValueError
        except ValueError:
            print("Opção inválida. Por favor, digite 1 ou 2.")
            continue
        
        if opcao == 1:
            palavra = input("Digite a palavra: ")
            print(f"A palavra invertida é: {inverter_string(palavra)}")
        else:
            print(f"Saindo...")
            break

menu_interativo()