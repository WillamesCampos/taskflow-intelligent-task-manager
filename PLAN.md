✅ 1. Módulos do Projeto TaskFlow
🔹 Módulo 1 – Autenticação e Usuários
Registro e login de usuários

Integração com Keycloak (OAuth2/OpenID Connect)

Perfis de usuário e permissões básicas

🔹 Módulo 2 – Gerenciamento de Tarefas
CRUD de tarefas

Campos: título, descrição, data de vencimento, prioridade, status, responsável

Validação de regras (ex: prazo não pode ser no passado)

🔹 Módulo 3 – Sugestão Inteligente de Prioridades (LLM)
Integração com API (ex: OpenAI, Local LLM via FastAPI)

Envio do contexto da tarefa e retorno da prioridade sugerida

Endpoint assíncrono com fallback se LLM estiver indisponível

🔹 Módulo 4 – Notificações
Notificações em tempo real com WebSockets (Django Channels)

Envio de e-mails assíncronos com Celery + RabbitMQ

Alertas automáticos para tarefas próximas do prazo

🔹 Módulo 5 – Painel Admin
Interface Django Admin com melhorias visuais

Gerenciamento de usuários e tarefas

Dashboard com métricas (opcional)

🔹 Módulo 6 – Microserviço de Mensageria (FastAPI)
Endpoint para receber mensagens e eventos de notificação

Publicação em filas RabbitMQ

Health check e documentação com Swagger

🏛️ 2. Modelagem da Arquitetura Geral
🔹 Componentes principais:
scss
Copy
Edit
[Frontend futuro]
     ↓
[API Django - Backend Principal]
     ├─ Django REST Framework (Users & Tasks)
     ├─ Django Channels (WebSocket)
     ├─ Celery Workers
     └─ Admin Interface
     
 ↕
[FastAPI Microservice]
     ├─ Endpoint para análise com LLM
     └─ Comunicação com RabbitMQ

 ↕
[RabbitMQ] ⇄ [Celery Workers]
 ↕
[PostgreSQL]  [Redis]  [SMTP/Email Service]
🔹 Tecnologias:
Django: backend principal

FastAPI: microserviço LLM

RabbitMQ: mensageria

Celery: tarefas assíncronas

PostgreSQL: banco de dados principal

Redis: broker/cache

Docker: ambiente isolado

GitHub Actions: CI/CD

Terraform: infraestrutura como código (ambientes de teste e produção)

🚀 3. Roadmap Técnico
🔹 Fase 1 – Setup & Fundamentos (Semana 1–2)
 Setup do repositório e CI/CD (GitHub Actions)

 Estrutura inicial do projeto Django e FastAPI

 Containers Docker para todos os serviços

 Configuração de Keycloak + Redis + RabbitMQ + PostgreSQL com Docker Compose

🔹 Fase 2 – Back-End Principal (Semana 3–4)
 Models, serializers e endpoints (User e Task)

 Autenticação integrada com Keycloak

 Interface Admin aprimorada

 Testes com Pytest e cobertura básica

🔹 Fase 3 – Notificações (Semana 5–6)
 WebSockets com Django Channels

 Integração com Celery e RabbitMQ para envio de e-mails

 Alertas automáticos para tarefas urgentes

🔹 Fase 4 – Integração com LLM (Semana 7)
 Criar microserviço FastAPI com endpoint /suggest-priority

 Consumo assíncrono no backend Django

 Testes de fallback + logging

🔹 Fase 5 – Infraestrutura e Deploy (Semana 8)
 Escrever templates Terraform para provisionamento

 Deploy automatizado via CI/CD

 Monitoramento básico (health checks, logs)

🔹 Fase 6 – Documentação e Portfólio (Semana 9)
 Documentar o projeto (README, arquitetura, APIs)

 Criar vídeo/demo para LinkedIn

 Publicar no GitHub com issues abertas e board