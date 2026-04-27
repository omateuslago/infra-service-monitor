# 🚀 Infra Service Monitor

Sistema full stack para monitoramento de serviços, APIs e websites em tempo real.

Projeto desenvolvido para demonstrar habilidades práticas em:

- Back-end
- Front-end
- Docker
- APIs REST
- Banco de Dados
- Integração entre serviços

---

## 📸 Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/fe2e1dd9-3f23-48e7-89c3-d36ac2e95b75" width="100%">
</p>

---

## 🎯 Objetivo

Aplicação inspirada em plataformas como:

- UptimeRobot
- BetterStack
- Pingdom
- StatusCake

Foco em:

- Monitoramento de disponibilidade
- Health checks automáticos
- Tempo de resposta
- Dashboard administrativo
- Arquitetura distribuída

---

## 🧱 Arquitetura

```text
infra-service-monitor/
│
├── backend/
│   ├── InfraMonitorAPI   -> API ASP.NET Core
│   └── monitor-agent     -> Worker Python
│
├── frontend/             -> Dashboard React
│
└── docker-compose.yml    -> Orquestração completa
```

---

## ⚙️ Stack Utilizada

### Backend

- C#
- ASP.NET Core Web API
- Entity Framework Core
- SQL Server

### Frontend

- React
- JavaScript
- CSS3

### Worker / Monitoramento

- Python
- Requests

### DevOps / Infra

- Docker
- Docker Compose

---

## 🔥 Funcionalidades

### ✅ Cadastro de Serviços

Cadastre URLs para monitoramento.

Exemplos:

- Google
- YouTube
- APIs internas

### ✅ Verificações Automáticas

Worker executa checks periódicos:

- Status online / offline
- Tempo de resposta
- Histórico de verificações

### ✅ Dashboard em Tempo Real

Visualização de:

- Total de serviços
- Quantidade online
- Quantidade offline
- Últimos checks
- Tempo de resposta colorido

---

## 🚀 Como Executar

### Clone o projeto

```bash
git clone https://github.com/omateuslago/infra-service-monitor.git
cd infra-service-monitor
```

### Suba o ambiente completo

```bash
docker compose up --build
```

---

## 🌐 Acessos

### Frontend

```text
http://localhost:3000
```

### API

```text
http://localhost:5000
```

### Swagger

```text
http://localhost:5000/swagger
```

---

## 🧠 Conhecimentos Demonstrados

- APIs REST
- Controllers ASP.NET Core
- Entity Framework Core
- SQL Server
- React Hooks
- Consumo de APIs
- Estado e renderização dinâmica
- Docker Compose
- Containers e redes
- Integração C# + Python + React
- Debug real de ambiente

---

## 👨‍💻 Autor

**Mateus Lago**

GitHub:  
https://github.com/omateuslago
