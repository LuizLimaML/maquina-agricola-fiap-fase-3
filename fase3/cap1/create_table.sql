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
);
