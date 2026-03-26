# 🎮 Inventário de Jogos - API Flask

## 📌 Descrição

API RESTful para gerenciamento de inventário de jogos, permitindo cadastrar, listar, atualizar e remover jogos utilizando Flask e SQLite.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/inventario-jogos-api.git
cd inventario-jogos-api
```

### 2. (Opcional) Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Criar o banco de dados

```bash
python init_db.py
```

---

### 5. Executar a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🔥 Endpoints da API

### 📌 GET - Listar todos os jogos

```bash
curl http://127.0.0.1:5000/jogos
```

---

### 📌 GET - Buscar jogo por ID

```bash
curl http://127.0.0.1:5000/jogos/1
```

---

### 📌 POST - Inserir jogo

```bash
curl -X POST http://127.0.0.1:5000/jogos \
-H "Content-Type: application/json" \
-d '{"nome":"God of War","genero":"Ação","plataforma":"PS5","preco":199.90,"estoque":10}'
```

---

### 📌 PUT - Atualizar jogo

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 \
-H "Content-Type: application/json" \
-d '{"nome":"God of War Ragnarok","genero":"Ação","plataforma":"PS5","preco":249.90,"estoque":5}'
```

---

### 📌 DELETE - Remover jogo

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

## ✅ Funcionalidades

* ✔ Cadastro de jogos
* ✔ Listagem completa
* ✔ Busca por ID
* ✔ Atualização de dados
* ✔ Remoção de registros

---

## 🛠 Tecnologias utilizadas

* Python
* Flask
* SQLite

---

## 📌 Observações

* API seguindo padrão REST
* Retornos em JSON
* Status HTTP corretos (200, 201, 204, 404)
* Código organizado e reutilizável

---

## 💡 Autor

Projeto desenvolvido para fins acadêmicos.
