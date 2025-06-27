from database.database import get_connection

def inserir_produto(nome, preco, estoque):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)",
                       (nome, preco, estoque))
        conn.commit()
        cursor.close()
        conn.close()

def listar_produtos():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return produtos

def criar_empresa(nome, cnpj):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO EMPRESA (nome, cnpj) VALUES (%a, %a)", 
            (nome, cnpj))
        resposta = cursor.fetchall()
        cursor.close()
        conn.close()
        return resposta

def criar_primer_usuario(nome, email, senha):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USUARIO (nome, email, senha) VALUES (%a, %a)", 
                       (nome, email, senha))
        resposta = cursor.fetchall()
        cursor.close()
        conn.close()
        return resposta
    
def criar_primer_cargo(nome, fk_empresa, fk_usuario):
    nivel_acesso = '1'
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USUARIO (nome, nivel_acesso, fk_empresa, fk_usuario) VALUES (%a, %a)", 
                       (nome, nivel_acesso,  fk_empresa, fk_usuario))
        resposta = cursor.fetchall()
        cursor.close()
        conn.close()
        return resposta