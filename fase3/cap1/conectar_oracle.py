import oracledb
import pandas as pd

user = "RM573370"
password = "280600"
dsn = "oracle.fiap.com.br:1521/ORCL"

try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
    print("Conectado no Oracle!")
    cur = conn.cursor()

    # dropar tabela se existir
    try:
        cur.execute("DROP TABLE RM573370_SENSORES")
        print("Tabela antiga removida.")
    except:
        print("Tabela nao existia.")

    # criar tabela
    cur.execute("""
        CREATE TABLE RM573370_SENSORES (
            id NUMBER PRIMARY KEY,
            data_hora TIMESTAMP,
            umidade NUMBER(5,2),
            fosforo NUMBER(1),
            potassio NUMBER(1),
            ph NUMBER(4,2),
            temperatura NUMBER(5,2),
            irrigacao NUMBER(1),
            cultura VARCHAR2(20)
        )
    """)
    print("Tabela criada.")

    # ler csv
    df = pd.read_csv('../../fase2/sensores.csv')

    # inserir dados
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO RM573370_SENSORES
            (id, data_hora, umidade, fosforo, potassio, ph, temperatura, irrigacao, cultura)
            VALUES (:1, TO_TIMESTAMP(:2, 'YYYY-MM-DD HH24:MI:SS'), :3, :4, :5, :6, :7, :8, :9)
        """, (
            int(row['id']),
            str(row['data_hora']),
            float(row['umidade']),
            int(row['fosforo']),
            int(row['potassio']),
            float(row['ph']),
            float(row['temperatura']),
            int(row['irrigacao']),
            str(row['cultura'])
        ))
    conn.commit()
    print(f"{len(df)} registros inseridos.")

    # executar queries
    queries = [
        ("1. Todos os registros (primeiros 5)", "SELECT * FROM RM573370_SENSORES WHERE ROWNUM <= 5"),
        ("2. Media de umidade por cultura", "SELECT cultura, AVG(umidade) FROM RM573370_SENSORES GROUP BY cultura"),
        ("3. Registros com irrigacao ativa", "SELECT COUNT(*) FROM RM573370_SENSORES WHERE irrigacao = 1"),
        ("4. pH fora do ideal", "SELECT COUNT(*) FROM RM573370_SENSORES WHERE ph < 5.5 OR ph > 7.5"),
        ("5. Temperatura acima de 35", "SELECT COUNT(*) FROM RM573370_SENSORES WHERE temperatura > 35"),
        ("6. Contagem por cultura", "SELECT cultura, COUNT(*) FROM RM573370_SENSORES GROUP BY cultura"),
        ("7. Solo deficiente", "SELECT COUNT(*) FROM RM573370_SENSORES WHERE fosforo = 0 AND potassio = 0"),
        ("8. Top 5 menor umidade", "SELECT * FROM (SELECT * FROM RM573370_SENSORES ORDER BY umidade ASC) WHERE ROWNUM <= 5"),
    ]

    for titulo, q in queries:
        print()
        print("===", titulo, "===")
        cur.execute(q)
        for r in cur.fetchall():
            print(r)

    cur.close()
    conn.close()
    print()
    print("Tudo certo!")

except Exception as e:
    print("Erro:", e)
