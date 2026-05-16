## FarmTech Solutions - Fase 3

Projeto da Fase 3 do curso da FIAP. Sistema simples de monitoramento de sensores agricolas (umidade, pH, fosforo, potassio, temperatura) que armazena os dados no Oracle, mostra num dashboard em Streamlit e ainda usa Machine Learning pra classificar culturas.

## Como rodar

1. Instalar as dependencias:
```
pip install -r requirements.txt
```

2. Gerar os dados dos sensores:
```
cd fase3/cap1
python gerar_dados.py
```

3. Conectar no Oracle e subir os dados:
```
python conectar_oracle.py
```

4. Rodar o dashboard:
```
streamlit run dashboard.py
```

5. Abrir o notebook de ML:
```
jupyter notebook analise_ml.ipynb
```

## Estrutura do projeto

- `fase2/sensores.csv` - dados gerados dos sensores
- `fase3/cap1/gerar_dados.py` - gera o CSV
- `fase3/cap1/conectar_oracle.py` - conecta no Oracle e insere os dados
- `fase3/cap1/create_table.sql` - cria a tabela no Oracle
- `fase3/cap1/queries.sql` - as 8 consultas SQL
- `fase3/cap1/dashboard.py` - dashboard em Streamlit
- `fase3/cap1/analise_ml.ipynb` - notebook com 5 modelos de ML
- `docs/prints/` - prints do Oracle

## Consultas SQL

1. Todos os registros da tabela
2. Media de umidade por cultura
3. Registros com irrigacao ativa
4. pH fora do ideal (< 5.5 ou > 7.5)
5. Temperatura acima de 35 graus
6. Contagem de registros por cultura
7. Solo deficiente (fosforo=0 e potassio=0)
8. Top 5 menores umidades

## Prints do Oracle

### 1. Importando os dados
![Importando os dados](docs/prints/01%20-%20Importando%20os%20dados.png)

### 2. Importando os dados (continuacao)
![Importando os dados 2](docs/prints/02%20-%20Importando%20os%20dados.png)

### 3. Selecao de colunas
![Selecao de colunas](docs/prints/03%20-%20Importando%20os%20dados%20-%20Sele%C3%A7%C3%A3o%20de%20Colunas.png)

### 4. Definicao do tipo das colunas
![Definicao do tipo das colunas](docs/prints/04%20-%20Importando%20os%20dados%20-%20Defini%C3%A7%C3%A3o%20Tipo%20das%20Colunas.png)

### 5. Dados importados
![Dados importados](docs/prints/05%20-%20Dados%20Importados.png)

### 6. Efetuando consultas
![Efetuando consultas](docs/prints/06%20-%20Efeturando%20Consultas.png)

## Video

[link do youtube aqui]

## Autores

Luiz Davi Moreira Lima - RM573370
