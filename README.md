# Projeto Concessionária

![badge](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
[![license](https://img.shields.io/github/license/ThalesBergamim/projeto_concessionaria.svg)](LICENSE)

## Índice

- [Funcionalidades](#funcionalidades)
- [Imagens do Sistema](#imagens-do-sistema)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Uso](#instalação-e-uso)
- [Licença](#licença)

## Funcionalidades

- Cadastro de veículos com informações detalhadas (modelo, marca, ano, preço, etc.).
- Visualização, edição e exclusão de veículos.
- Integração com Gemini API para geração da descrição automática.
- Relatórios de carros em estoque.
- Autenticação de usuários com diferentes níveis de acesso.
- Autenticação de usúarios utilizando o Login do google.

## Imagens do Sistema

#### Tela de Login
![Tela de login](./screenshots/Login.jpg)
#### Tela de Cadastro
![Tela de Cadastro](./screenshots/Registre-se.jpg)
#### Cadastro de veículos
![Tela de Cadastro de Veículos](./screenshots/Cadastrar%20Carro.jpg)
#### Edição de veículos
![Tela de edição de Veículos](./screenshots/Editar.jpg)
#### Detalhes de veículos
![Tela de Detalhes de Veículos](./screenshots/Detalhes%20.jpg)

## Tecnologias Utilizadas

- **Back-end:** Python com Django
- **Front-end:** HTML, CSS, JavaScript
- **Banco de Dados:** PostgreSQL

## Instalação e Uso

### Clonando o repositório

```bash
 git clone https://github.com/ThalesBergamim/projeto_concessionaria.git
```

### Criando um ambiente virtual

```bash
 python -m venv venv
```

### Instalando as dependências

```bash
 pip install -r requirements.txt
```

### Realizando as migrações do banco de dados

```bash
 python manage.py migrate
```

### Iniciando o servidor de desenvolvimento

```bash
 python manage.py runserver
```

### Acessando a aplicação

Abra o navegador e vá para `http://localhost:8000`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
