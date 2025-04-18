import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(url):
    """Carrega os dados de um arquivo CSV a partir da URL."""
    return pd.read_csv(url)

def faturamento_total(df):
    """Calcula o faturamento total por loja."""
    df['Faturamento'] = df['Preço']
    return df.groupby('Local da compra')['Faturamento'].sum().sort_values(ascending=False)

def categorias_populares(df):
    """Calcula as categorias mais populares."""
    return df['Categoria do Produto'].value_counts()

def media_avaliacao(df):
    """Calcula a média de avaliação dos clientes."""
    return df['Avaliação da compra'].mean()

def produtos_mais_vendidos(df):
    """Calcula os produtos mais vendidos."""
    return df['Produto'].value_counts().head(5)

def produtos_menos_vendidos(df):
    """Calcula os produtos menos vendidos."""
    return df['Produto'].value_counts().tail(5)

def custo_medio_frete(df):
    """Calcula o custo médio do frete."""
    df['Frete'] = df['Frete'].round(2)
    return df['Frete'].mean()

# URL para os dados
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"

# Carregar os dados
loja = carregar_dados(url)

# Faturamento total por loja
faturamento = faturamento_total(loja)

# Categorias mais populares
categorias = categorias_populares(loja)

# Produtos mais vendidos
produtos_vendidos = produtos_mais_vendidos(loja)

# Custo médio do frete
frete = custo_medio_frete(loja)

# Carregar os dados
loja = carregar_dados(url)

# Exibindo os resultados das análises
print("\nFaturamento total por loja:")
print(faturamento_total(loja))

print("\nCategorias mais populares:")
print(categorias_populares(loja))

print(f"\nMédia de avaliação dos clientes: {media_avaliacao(loja):.2f}")

print("\nTop 5 produtos mais vendidos:")
print(produtos_mais_vendidos(loja))

print("\nTop 5 produtos menos vendidos:")
print(produtos_menos_vendidos(loja))

print(f"\nCusto médio do frete: R$ {custo_medio_frete(loja):.2f}")


# 1. Gráfico de barras do Faturamento Total por Loja
plt.figure(figsize=(10,6))
faturamento.plot(kind='bar', color='skyblue')
plt.title('Faturamento Total por Loja')
plt.ylabel('Faturamento (R$)')
plt.xlabel('Loja')
plt.xticks(rotation=45)
plt.show()

#2.Gráfico de Barras das Categorias mais Populares
plt.figure(figsize=(10,6))
categorias.plot(kind='bar', color= 'lightgreen')
plt.title('Categorias Mais Populares')
plt.ylabel('Quantidade de Produtos')
plt.xlabel('Categoria de Produto')
plt.xticks(rotation=45)
plt.show()

# 3. Gráfico de barras das Avaliações
# Média de avaliação dos clientes
media = media_avaliacao(loja)
plt.figure(figsize=(6, 6))
plt.bar(['Avaliação Média'], [media], color='lightcoral')
plt.title('Média de Avaliação dos Clientes')
plt.ylabel('Avaliação')
plt.ylim(0,5)
plt.show()

# 4. Gráfico de barras dos Produtos Mais Vendidos
plt.figure(figsize=(10,6))
produtos_vendidos.plot(kind='bar', color='orange')
plt.title('Top5 Produtos Mais Vendidos')
plt.ylabel('Quantidade Vendida')
plt.xlabel('Produto')
plt.xticks(rotation=45)
plt.show()

# 5. Gráfico de pizza para o Custo Médio de Frete
# Podemos mostrar uma distribuição entre frete baixo, médio e alto

df = loja  

quantidade_frete = [
    df[df['Frete'] < 10].shape[0],
    df[(df['Frete'] >= 10) & (df['Frete'] < 20)].shape[0],
    df[df['Frete'] >= 20].shape[0]
]

# Definindo os rótulos
faixa_frete = ['< R$10', 'R$10 a R$19,99', '≥ R$20']

# Plotando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(
    quantidade_frete,
    labels=faixa_frete,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightblue', 'lightgreen', 'lightcoral']
)
plt.title('Distribuição do Custo de Frete')
plt.axis('equal')  # Para manter o formato redondo
plt.show()
