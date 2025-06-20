# 🇧🇷 Brasileirão Data Pipeline

Este projeto é um pipeline de dados focado na extração, processamento e armazenamento de estatísticas do **Campeonato Brasileiro Série A**. 
Ele coleta dados automaticamente da API [Football-Data.org](https://www.football-data.org/), processa e salva os dados em formatos estruturados (JSON/CSV) e os envia para um banco de dados relacional (PostgreSQL).

---

## 🚀 Funcionalidades

- 🔄 Extração automática de dados via API REST (jogos, artilheiros, etc)
- 🧹 Processamento e limpeza dos dados
- 📦 Armazenamento dos dados:
  - Dados brutos em JSON
  - Dados processados em CSV
  - Dados estruturados no PostgreSQL
- ⏱️ Automação do processo de coleta (em construção)
- 📊 Suporte futuro para dashboards e análises

---

## 🧱 Estrutura do Projeto

│
├── data/
│ ├── raw/ # Dados brutos extraídos da API
│ └── processed/ # Dados limpos e estruturados
│
├── src/
│ ├── extract/ # Scripts de extração de dados
│ ├── transform/ # Scripts de limpeza e transformação
│ └── load/ # Scripts para carregar dados no PostgreSQL
│
└── .env # Variáveis de ambiente (URLs e tokens)
 


---

## 🧪 Tecnologias Utilizadas

- Python 3.11
- PostgreSQL
- Pandas
- Requests
- dotenv
- JSON / CSV
- (Futuramente: Azure / n8n para automação)

---

## ⚙️ Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/brasileirao-data-pipeline.git
   cd brasileirao-data-pipeline
