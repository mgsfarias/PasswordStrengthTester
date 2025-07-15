# 🔐 Password Strength Tester

Verifique a força de senhas em tempo real, receba recomendações de segurança e descubra se sua senha já vazou em bases públicas usando a API do [HaveIBeenPwned](https://haveibeenpwned.com).

## 📸 Captura de tela
![Screenshot](screenshot.png)

## 🧠 Funcionalidades

- Verificação de força de senha com análise em tempo real.
- Feedback visual (cor e texto) de acordo com critérios de segurança.
- Estimativa de tempo para quebra via ataque de força bruta.
- Integração com a API do **HaveIBeenPwned** para detectar senhas vazadas.
- Interface moderna e leve com `ttkbootstrap`.

## 🛠️ Tecnologias Usadas

- Python 3.x
- [`ttkbootstrap`](https://github.com/israel-dryer/ttkbootstrap) para interface estilizada
- `requests` para acesso à API do HaveIBeenPwned
- `hashlib` para hashing de senha SHA-1

## ▶️ Como usar

### 1. Clone o projeto
```bash
git clone https://github.com/seu-usuario/password-strength-tester.git
cd password-strength-tester
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute
```bash
python app.py
```

## 🔄 Funcionalidades Futuras

- [ ] Gerador de senhas fortes
- [ ] Modo escuro/claro alternável
- [ ] Histórico de senhas testadas (local)
- [ ] Versão web com Flask
- [ ] Empacotamento `.exe`

## 📁 Organização do Projeto

```
password-strength-tester/
├── app.py               # Script principal da aplicação
├── requirements.txt     # Dependências
└── README.md            # Documentação
```

## ✅ Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir um Issue ou enviar um Pull Request.

## ⚠️ Aviso

Este projeto tem fins **educacionais** e de **conscientização em cibersegurança**. Não armazena senhas digitadas e não as transmite além do hash parcial (5 caracteres) à API do HaveIBeenPwned.

## 📜 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
