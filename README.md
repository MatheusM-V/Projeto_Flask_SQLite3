# 🧠 Projeto Flask + SQLite3

> Projeto que eu fiz para estudar **Flask** e **SQLite3** — um simples sistema de cadastro e login totalmente funcional.

---

## 🚀 Funcionalidades

- Cadastro de novos usuários com validação de dados  
- Login seguro com sessões do Flask  
- Logout automático  
- Banco de dados **SQLite3** local  
- Estrutura organizada em módulos (`Database/`, `templates/`, etc.)  
- Interface simples e intuitiva

---

## 🗂️ Estrutura do Projeto

```
Projeto_Flask_SQLite3/
├── app.py
├── Database/
│   ├── init_db.py
│   └── usuarios.db
├── templates/
│   ├── login.html
│   ├── cadastro.html
│   └── portal.html
├── static/
│   └── (CSS / imagens futuras)
└── .gitignore
```

---

## 🧰 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite3](https://www.sqlite.org/)

---

## ⚙️ Como Rodar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MatheusM-V/Projeto_Flask_SQLite3.git
   cd Projeto_Flask_SQLite3
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask
   ```

3. **Crie o banco de dados:**
   ```bash
   python Database/init_db.py
   ```

4. **Execute o servidor:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   ```
   http://localhost:5000
   ```
   ou na sua rede local:
   ```
   http://NOME-DO-PC:5000
   ```

---

## 🔐 Login Padrão (Exemplo)

Usuário: **admin**  
Senha: **1234**

> ⚠️ Este usuário é apenas um exemplo local — altere antes de usar em ambiente real.

---

## 💡 Possíveis Melhorias Futuras

- Criptografia de senhas com `werkzeug.security`
- Interface visual com **Bootstrap** ou **Tailwind CSS**
- Listagem de usuários e painel administrativo
- Deploy gratuito no **Render** ou **Railway**

---

## 🧑‍💻 Autor

**Matheus Vitorino**  
📚 Desenvolvido para fins de estudo e prática de Flask + SQLite3  
🔗 [GitHub - Matheus Vitorino](https://github.com/MatheusM-V)

---

Esse README foi feito pelo chat gpt pois, preguiça.
