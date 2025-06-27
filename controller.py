from models import inserir_produto, listar_produtos

def autenticar(nome, preco, estoque):
    if nome and preco > 0 and estoque >= 0:
        inserir_produto(nome, preco, estoque)
        return {'ok': True}
    else:
        return {'ok': False, 'msg': 'Dados inválidos'}

def listar_produtos_controller():
    return listar_produtos()
