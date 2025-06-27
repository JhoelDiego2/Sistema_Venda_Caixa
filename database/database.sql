CREATE DATABASE Mita_Control;
USE Mita_Control;

CREATE TABLE IF NOT EXISTS EMPRESA (
    id_empresa        INT            AUTO_INCREMENT PRIMARY KEY,
    nome              VARCHAR(100)   NOT NULL,
    cnpj              VARCHAR(14) NOT NULL
);


CREATE TABLE IF NOT EXISTS USUARIO (
    id_usuario        INT            AUTO_INCREMENT PRIMARY KEY,
    nome              VARCHAR(100)   NOT NULL,
    email             VARCHAR(100)   NOT NULL, 
    senha             VARCHAR(255)   NOT NULL, 
    fk_supervisor     INT            NULL, 

    CONSTRAINT fk_supervisor_regular 
        FOREIGN KEY (fk_supervisor) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE IF NOT EXISTS CARGO (
    id_cargo          INT            AUTO_INCREMENT ,
    nome              VARCHAR(100)   NOT NULL,
    nivel_acesso      ENUM('1', '2'), 
    fk_empresa        INT, 
    fk_usuario        INT, 

	CONSTRAINT pk_composta_cargo PRIMARY KEY (id_cargo, fk_empresa, fk_usuario),
    CONSTRAINT fk_empresa_cargo 
        FOREIGN KEY (fk_empresa) REFERENCES EMPRESA(id_empresa),
	CONSTRAINT fk_cargo_usuario 
        FOREIGN KEY (fk_usuario) REFERENCES USUARIO(id_usuario)
);


CREATE TABLE IF NOT EXISTS PRODUTO (
    id_produto        INT            AUTO_INCREMENT PRIMARY KEY,
    nome              VARCHAR(100)   NOT NULL,
    preco             DECIMAL(10,2)  NOT NULL
);


CREATE TABLE IF NOT EXISTS CAIXA (
    id_caixa           INT            AUTO_INCREMENT PRIMARY KEY,
    nome               VARCHAR(45),
    data               DATE,
    fk_empresa         INT, 

    CONSTRAINT fk_empresa_caixa
        FOREIGN KEY (fk_empresa) REFERENCES EMPRESA(id_empresa)
);


CREATE TABLE IF NOT EXISTS MOVIMENTACAO (
    id_movimentacao    INT            AUTO_INCREMENT PRIMARY KEY,
    tipo               ENUM       ('entrada', 'saida'),
    valor              DECIMAL(10,2),
    descricao          TEXT,    
    data_movimentacao  DATETIME,
    fk_caixa           INT,

    CONSTRAINT fk_caixa_movimentacao 
        FOREIGN KEY (fk_caixa) REFERENCES CAIXA(id_caixa)
);

CREATE TABLE IF NOT EXISTS ESTOQUE (
    id_estoque        INT AUTO_INCREMENT PRIMARY KEY,
    quantidade        INT DEFAULT 0,
    fk_produto        INT,
    fk_empresa        INT,
    CONSTRAINT fk_produto_estoque FOREIGN KEY (fk_produto) REFERENCES PRODUTO(id_produto),
    CONSTRAINT fk_empresa_estoque FOREIGN KEY (fk_empresa) REFERENCES EMPRESA(id_empresa)
);

CREATE TABLE IF NOT EXISTS VENDA (
    id_venda          INT            AUTO_INCREMENT PRIMARY KEY,
    data_venda        DATETIME,
    total             DECIMAL(10,2),
    fk_caixa        INT,

    CONSTRAINT fk_usuario_venda 
        FOREIGN KEY (fk_caixa) REFERENCES CAIXA(id_caixa)
);


CREATE TABLE IF NOT EXISTS ITEM_VENDA (
    id_item           INT            AUTO_INCREMENT PRIMARY KEY,
    quantidade        INT,
    preco_unitario    DECIMAL(10,2),
    fk_venda          INT,
    fk_produto        INT,

    CONSTRAINT fk_venda_item 
        FOREIGN KEY (fk_venda) REFERENCES VENDA(id_venda),
    CONSTRAINT fk_produto_item 
        FOREIGN KEY (fk_produto) REFERENCES PRODUTO(id_produto)
);


