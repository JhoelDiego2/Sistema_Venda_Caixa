CREATE DATABASE loja_cristina;
USE loja_cristina;

CREATE TABLE PRODUTO (
    id_produto        INT            AUTO_INCREMENT PRIMARY KEY,
    nome              VARCHAR(100)   NOT NULL,
    preco             DECIMAL(10,2)  NOT NULL,
    estoque           INT DEFAULT 0
);


CREATE TABLE USUARIO (
    id_usuario        INT            AUTO_INCREMENT PRIMARY KEY,
    nome              VARCHAR(100)   NOT NULL,
    email             VARCHAR(100), 
    senha             VARCHAR(255)   NOT NULL, 
    fk_supervisor     INT            NULL, 
    tipo_usuario      ENUM           ('admin', 'regular'),

    CONSTRAINT fk_supervisor_regular 
        FOREIGN KEY (fk_supervisor) REFERENCES USUARIO(id_usuario)
);


CREATE TABLE VENDA (
    id_venda          INT            AUTO_INCREMENT PRIMARY KEY,
    fk_usuario        INT,
    data_venda        DATETIME,
    total             DECIMAL(10,2),

    CONSTRAINT fk_usuario_venda 
        FOREIGN KEY (fk_usuario) REFERENCES USUARIO(id_usuario)
);


CREATE TABLE ITEM_VENDA (
    id_item           INT            AUTO_INCREMENT PRIMARY KEY,
    fk_venda          INT,
    fk_produto        INT,
    quantidade        INT,
    preco_unitario    DECIMAL(10,2),

    CONSTRAINT fk_venda_item 
        FOREIGN KEY (fk_venda) REFERENCES VENDA(id_venda),
    CONSTRAINT fk_produto_item 
        FOREIGN KEY (fk_produto) REFERENCES PRODUTO(id_produto)
);


CREATE TABLE CAIXA (
    id_caixa           INT            AUTO_INCREMENT PRIMARY KEY,
    data               DATE,
    saldo_abertura     DECIMAL(10,2),
    saldo_fechamento   DECIMAL(10,2)
);


CREATE TABLE MOVIMENTACAO (
    id_movimentacao    INT            AUTO_INCREMENT PRIMARY KEY,
    fk_caixa           INT,
    tipo               ENUM           ('entrada', 'saida'),
    valor              DECIMAL(10,2),
    descricao          TEXT,

    data_movimentacao  DATETIME,
    CONSTRAINT fk_caixa_movimentacao 
        FOREIGN KEY (fk_caixa) REFERENCES CAIXA(id_caixa)
);

