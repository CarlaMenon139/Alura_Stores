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

# URLs das lojas
url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

# Carregar os dados
df1 = carregar_dados(url1)
df2 = carregar_dados(url2)
df3 = carregar_dados(url3)
df4 = carregar_dados(url4)

# Faturamento total por loja (para comparação geral)
faturamento_total_lojas = {
    'Loja 1': df1['Preço'].sum(),
    'Loja 2': df2['Preço'].sum(),
    'Loja 3': df3['Preço'].sum(),
    'Loja 4': df4['Preço'].sum(),
}

df_faturamento_total = pd.DataFrame.from_dict(faturamento_total_lojas, orient='index', columns=['Faturamento'])

# Exibir gráfico comparativo das lojas
plt.figure(figsize=(8,6))
df_faturamento_total.plot(kind='bar', legend=False, color='mediumseagreen')
plt.title('Faturamento Total por Loja')
plt.ylabel('Faturamento (R$)')
plt.xlabel('Lojas')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Agora juntando todas as lojas num DataFrame único para análises gerais
df_geral = pd.concat([df1, df2, df3, df4])

# Outras análises
faturamento = faturamento_total(df_geral)
categorias = categorias_populares(df_geral)
media = media_avaliacao(df_geral)
produtos_vendidos = produtos_mais_vendidos(df_geral)
produtos_pouco_vendidos = produtos_menos_vendidos(df_geral)
frete = custo_medio_frete(df_geral)

# Exibir análises no console
print("\nFaturamento total por loja (baseado no local da compra):")
print(faturamento)

print("\nCategorias mais populares:")
print(categorias)

print(f"\nMédia de avaliação dos clientes: {media:.2f}")

print("\nTop 5 produtos mais vendidos:")
print(produtos_vendidos)

print("\nTop 5 produtos menos vendidos:")
print(produtos_pouco_vendidos)

print(f"\nCusto médio do frete: R$ {frete:.2f}")

# Gráficos
# 1. Faturamento total por loja (baseado em local da compra)
plt.figure(figsize=(10,6))
faturamento.plot(kind='bar', color='skyblue')
plt.title('Faturamento Total por Local de Compra')
plt.ylabel('Faturamento (R$)')
plt.xlabel('Local')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Categorias mais populares
plt.figure(figsize=(10,6))
categorias.plot(kind='bar', color='lightgreen')
plt.title('Categorias Mais Populares')
plt.ylabel('Quantidade de Produtos')
plt.xlabel('Categoria de Produto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Média de avaliação
plt.figure(figsize=(6,6))
plt.bar(['Avaliação Média'], [media], color='lightcoral')
plt.title('Média de Avaliação dos Clientes')
plt.ylabel('Avaliação')
plt.ylim(0,5)
plt.tight_layout()
plt.show()

# 4. Top 5 produtos mais vendidos
plt.figure(figsize=(10,6))
produtos_vendidos.plot(kind='bar', color='orange')
plt.title('Top 5 Produtos Mais Vendidos')
plt.ylabel('Quantidade Vendida')
plt.xlabel('Produto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Gráfico de pizza do custo de frete
quantidade_frete = [
    df_geral[df_geral['Frete'] < 10].shape[0],
    df_geral[(df_geral['Frete'] >= 10) & (df_geral['Frete'] < 20)].shape[0],
    df_geral[df_geral['Frete'] >= 20].shape[0]
]

faixa_frete = ['< R$10', 'R$10 a R$19,99', '≥ R$20']

plt.figure(figsize=(8, 8))
plt.pie(
    quantidade_frete,
    labels=faixa_frete,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightblue', 'lightgreen', 'lightcoral']
)
plt.title('Distribuição do Custo de Frete')
plt.axis('equal')
plt.show()
