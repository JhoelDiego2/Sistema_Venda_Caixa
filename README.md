# 🧾 Sistema de Vendas e Caixa - Loja Cristina

Um sistema completo para gestão de vendas, controle de caixa e organização de estoque em uma loja de pequeno a médio porte. Este projeto foi desenvolvido para consolidar conhecimentos em **Python**, **MySQL** e **interfaces gráficas com CustomTkinter**.

<!-- <div align="center">
  <img src="https://imgur.com/aSuaImagemAqui.png" width="600"/>
</div>

--- -->

## 🧠 Visão Geral

Este sistema permite gerenciar:
- 📦 **Produtos:** cadastro, preços, estoque
- 👤 **Usuários:** com tipos (admin e regular)
- 💳 **Vendas e Pagamentos:** registro detalhado de cada venda
- 💰 **Caixa:** controle diário de abertura e fechamento
- 📈 **Relatórios:** vendas por usuário, faturamento diário e histórico do caixa

---

## 📌 Funcionalidades

### 📋 Cadastro e Gestão
- Produtos com nome, preço e controle de estoque
- Usuários com permissões distintas (admin ou regular)
- Vendas vinculadas ao usuário vendedor
- Itens de venda com quantidade e preço unitário

### 💼 Controle de Caixa
- Abertura e fechamento diário
- Registro de entradas e saídas (movimentações)
- Histórico completo das transações de caixa

### 📊 Relatórios
- Relatório de vendas por usuário e por data
- Consulta de estoque atual
- Relatório de movimentações financeiras do caixa

---

## 💻 Tecnologias Utilizadas

| Camada         | Ferramentas                       |
|----------------|------------------------------------|
| **Front-End**  | Python + [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) |
| **Back-End**   | Python (pymysql) + MySQL           |
| **Banco de Dados** | MySQL (modelo `loja_cristina`) |
| **Extras**     | Pandas para relatórios             |

---

## 🛠️ Instalação e Execução

### Pré-requisitos:
- Python 3.10 ou superior
- MySQL Server
- Pip atualizado

### Passo a passo:

1. Clone o projeto:
   ```bash
   git clone https://github.com/JhoelDiego2/Sistema_Venda_Caixa.git
   cd Sistema_Venda_Caixa
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Configure o banco de dados:

-  Crie o banco usando o script abaixo ou o arquivo database.sql incluído.

- Atualize as configurações no arquivo Python (host, user, password).

4. Execute o sistema:
   ```bash
   python main.py
## 📌 Status do Projeto

🚧 **Em Desenvolvimento**

### ✅ Funcionalidades já disponíveis:
- [x] Banco de dados
### 🔜 Próximas etapas:
- [ ] Cadastro de produtos e usuários
- [ ] Registro de vendas com itens
- [ ] Controle de caixa com abertura e movimentações
- [ ] Geração de relatórios em PDF
- [ ] Exportação de dados para Excel
- [ ] Responsividade (versão web ou mobile)
- [ ] Autenticação de login com hash de senha

---

## ✒️ Autor

Desenvolvido por **Jhoel Diego Mamani Mita**  
Este projeto faz parte de um estudo prático de Python com banco de dados, visando construir uma solução útil e aplicável no mundo real.

---

## 🤝 Contribuição

Quer contribuir?

- Relate bugs e sugestões via *Issues*
- Envie *Pull Requests* com melhorias ou novas funções
- Compartilhe ideias de expansão do sistema

> “Gestão eficiente começa com organização. Este projeto é meu passo nesse caminho.”
