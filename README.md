# 🧠 Projeto Flask + SQLite3

> Projeto que eu fiz para estudar **Flask** e **SQLite3** — um simples sistema de cadastro e login totalmente funcional, agora com estrutura modular e criptografia de senhas.

---

## 🚀 Funcionalidades

- Cadastro de novos usuários com validação de dados  
- Login seguro com **hash de senha (PBKDF2 + SHA256)** ✅  
- Sessões seguras e logout  
- Banco de dados **SQLite3** local  
- Estrutura modular usando **Blueprints**  
- Código organizado em camadas (`app/`, `Database/`, etc.)  
- Interface simples e intuitiva

---

## 🗂️ Estrutura do Projeto

```
Projeto_Flask_SQLite3/
├── run.py
├── app/
│   ├── __init__.py          # create_app + registro dos blueprints
│   ├── db.py                # camada de acesso ao SQLite
│   ├── auth.py              # rotas de autenticação (login/cadastro/logout)
│   ├── routes.py            # rotas principais (/, /portal, páginas)
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── cadastro.html
│   │   ├── portal.html
│   │   └── portais/
│   │       ├── pagina1.html
│   │       ├── pagina2.html
│   │       └── pagina3.html
│   └── static/
│       └── style.css
├── Database/
│   ├── init_db.py
│   └── usuarios.db          # ignorado pelo git
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧰 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [SQLite3](https://www.sqlite.org/)  
- [Werkzeug Security](https://werkzeug.palletsprojects.com/) (para hash de senha)

---

## ⚙️ Como Rodar Localmente

1. **Clone o repositório:**  
   ```bash
   git clone https://github.com/MatheusM-V/Projeto_Flask_SQLite3.git
   cd Projeto_Flask_SQLite3
   ```

2. **Instale as dependências:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Crie o banco de dados:**  
   ```bash
   python Database/init_db.py
   ```

4. **Execute o servidor:**  
   ```bash
   python run.py
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
Senha: **admin**  

> ⚠️ Este usuário é apenas um exemplo local — altere ou remova antes de usar em ambiente real.

---

## 💡 Melhorias Feitas / Futuras

- Criptografia de senhas com `werkzeug.security` ✅  
- Estrutura modular com **Blueprints** ✅  
- Mensagens visuais com `flash()` 🔜  
- Interface moderna com **Bootstrap** ou **Tailwind CSS** 🔜  
- Deploy gratuito no **Render** ou **Railway** 🔜

---

## 🧑‍💻 Autor

**Matheus Vitorino**  
📚 Desenvolvido para fins de estudo e prática com Flask + SQLite3  
🔗 [GitHub - Matheus Vitorino](https://github.com/MatheusM-V)

---

Esse README foi feito pelo ChatGPT, porque... preguiça, mas agora tá bonito demais 😎
