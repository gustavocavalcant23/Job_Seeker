# Job Seeker 💼


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey" />
  <img src="https://img.shields.io/badge/Architecture-Modular-green" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

> Agregador automatizado de vagas em tecnologia com scraping multi-fonte, persistência local e geração automática de relatórios Excel.

---

# 📌 Sobre o Projeto

**Job Seeker** é uma aplicação Python que automatiza a busca por vagas de tecnologia com base em uma query configurável.

O sistema:

- 🔎 Realiza scraping de múltiplas plataformas
- 💾 Armazena dados em SQLite
- 📊 Gera relatórios Excel automaticamente
- 🔁 Atualiza resultados por busca
- 🧹 Remove vagas antigas do banco

O foco principal do projeto é aplicar:

- Separação de responsabilidades
- Arquitetura modular
- Design limpo
- Organização escalável

---

# 🎯 Objetivo

Permitir que o usuário configure buscas de vagas de emprego e automaticamente:

- Coletar vagas compatíveis
- Persistir no banco local
- Gerar um relatório nomeado com base na busca

---

# 🏗️ Arquitetura

O projeto segue uma estrutura modular organizada por responsabilidades:

```

job_seeker/
│
├── database/
│ └── db.py
│
├── models/
│ └── jobs.py
│ 
├── reports/
│ └── report_service.py
│
├── scrapers/
│ ├── base_scraper.py
│ ├── remotar_scraper.py
│ └── nerdin_scraper.py
│
├── job_reports/
│
├── jobs.db
├── main.py
└── requirements.txt
```

---

# 🧠 Conceitos e Padrões Aplicados

## 🔹 Template Method Pattern

A classe `BaseScraper` define o fluxo padrão:

- `build_url()`
- `get()`
- `parse()`
- `run()`

Cada scraper implementa sua própria estratégia de busca.

## 🔹 Separação de Responsabilidades

- **Scrapers** → Coleta de dados
- **JobRepository** → Persistência
- **ReportService** → Geração de relatórios
- **main.py** → Orquestração

## 🎲 Persistência Local

Banco de dados SQLite:

- Leve
- Não requer servidor
- Ideal para MVP e automação local

---

# ⚙️ Instalação

## 1️⃣ Clonar o repositório

```
git clone https://github.com/gustavocavalcant23/Job_Seeker.git

cd job_seeker
```

---

## 2️⃣ Criar ambiente virtual

```
python -m venv venv
```

---

## 3️⃣ Ativar ambiente virtual

```
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

---

## 4️⃣ Instalar dependências

```
pip install -r requirements.txt
```

---

# 🔧 Configuração

Dentro da variável **query** no arquivo **main.py** defina dentro da lista as vagas que deseja buscar da seguinte forma:

```
def main():
    query = ["estagio ti", "desenvolvedor java"]

    for q in query:
        if not q:
```

---

# ▶️ Executando o projeto

```
python main.py
```

---

# 🔄 Fluxo de Execução

1. Lê as queries de main.py
2. Instancia os scrapers
3. Executa buscas
4. Salva no SQLite
5. Gera/atualiza relatório Excel
6. Remove vagas antigas

# 📊 Relatórios

A cada execução:

- Um arquivo Excel é criado na pasta `/job_reports`  para cada query
- Nome baseado na query + data atual
- Se já existir no mesmo dia → é atualizado
- Se não existir → é criado

Formato:

```
<QueryFormatada><Dia-Mes>.xlsx

# Exemplo: EstagioTi23-02.xlsx
```

---

# 📦 Tecnologias Utilizadas

- Python 3
- SQLite
- Requests
- BeautifulSoup
- OpenPyXL

---

# 🗄️ Banco de Dados

O banco SQLite é criado automaticamente na primeira execução.

Responsabilidades do `JobRepository`:

- Criar tabela
- Evitar duplicidade
- Salvar novas vagas
- Remover vagas antigas

---

# 👨‍💻 Autor

**Gustavo Cavalcante**
Desenvolvedor Python

---

# 📄 Licença

Este projeto é para fins educacionais e de estudo.
