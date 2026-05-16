-- 1. Todos os registros
SELECT * FROM RM573370_SENSORES;

-- 2. Media de umidade por cultura
SELECT cultura, AVG(umidade) AS media_umidade FROM RM573370_SENSORES GROUP BY cultura;

-- 3. Registros com irrigacao ativa
SELECT * FROM RM573370_SENSORES WHERE irrigacao = 1;

-- 4. pH fora do ideal
SELECT * FROM RM573370_SENSORES WHERE ph < 5.5 OR ph > 7.5;

-- 5. Temperatura acima de 35
SELECT * FROM RM573370_SENSORES WHERE temperatura > 35;

-- 6. Contagem por cultura
SELECT cultura, COUNT(*) AS total FROM RM573370_SENSORES GROUP BY cultura;

-- 7. Solo deficiente (fosforo=0 e potassio=0)
SELECT * FROM RM573370_SENSORES WHERE fosforo = 0 AND potassio = 0;

-- 8. Top 5 menor umidade
SELECT * FROM (SELECT * FROM RM573370_SENSORES ORDER BY umidade ASC) WHERE ROWNUM <= 5;
