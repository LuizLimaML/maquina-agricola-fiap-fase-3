import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

dados = []
data_inicio = datetime(2026, 4, 1)
culturas = ['soja', 'milho', 'cana']

for i in range(50):
    umidade = round(random.uniform(20, 90), 2)
    fosforo = random.randint(0, 1)
    potassio = random.randint(0, 1)
    ph = round(random.uniform(4.5, 8.5), 2)
    temperatura = round(random.uniform(15, 40), 2)
    irrigacao = 1 if umidade < 40 else 0
    cultura = random.choice(culturas)

    dados.append({
        'id': i + 1,
        'data_hora': data_inicio + timedelta(hours=i*8),
        'umidade': umidade,
        'fosforo': fosforo,
        'potassio': potassio,
        'ph': ph,
        'temperatura': temperatura,
        'irrigacao': irrigacao,
        'cultura': cultura
    })

df = pd.DataFrame(dados)
df.to_csv('../../fase2/sensores.csv', index=False)
print("CSV gerado com sucesso!")
print(df.head())
print()
print(df.describe())
