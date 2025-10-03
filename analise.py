import pandas as pd
import matplotlib.pyplot as plt

# Crie um dicionário com alguns dados
dados = {
    'mes': ['jan', 'fev', 'mar', 'abr', 'mai'],
    'vendas': [100, 150, 120, 180, 200]
}

# Converta o dicionário em um DataFrame do Pandas
df = pd.DataFrame(dados)

# Crie um gráfico de linha com os dados
plt.figure(figsize=(8, 5))
plt.plot(df['mes'], df['vendas'], marker='o')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()

print("O grafico de vendas foi gerado com sucesso!")