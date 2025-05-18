# taskflow-intelligent-task-manager
# 📝 TaskFlow

**TaskFlow** is a modular, backend-oriented task management system designed for productivity and scalability. Built with Django and FastAPI, it demonstrates clean architecture principles, asynchronous processing, and AI-assisted task prioritization.

## 🚀 Features

- ✅ User authentication and task CRUD
- 📅 Task deadlines and priority levels
- 🔔 Real-time notifications via WebSocket
- 📬 Email alerts via Celery + RabbitMQ
- 🤖 Smart suggestions for task prioritization using LLM
- 🛠️ Admin interface (Django Admin)
- 🧱 Clean architecture structure
- 🐳 Dockerized and production-ready

## 🧰 Tech Stack

| Area | Technology |
|------|------------|
| Backend Core | Django, Django REST Framework |
| Microservices | FastAPI |
| Asynchronous Tasks | Celery, RabbitMQ |
| Realtime Notifications | Django Channels (WebSocket) |
| AI Integration | OpenAI or local LLM |
| Authentication | Django built-in auth |
| DevOps | Docker, GitHub Actions (CI/CD pipeline) |
| Architecture | Clean Architecture (pragmatic) |

## 📂 Project Structure

This project follows a pragmatic Clean Architecture approach with Django, aiming to separate concerns between domain logic, infrastructure, and interfaces.

The structure is evolving as the project grows. A detailed directory layout will be documented in a later version of this README.

## 📍 Execution Plan & Architecture Overview

### ✅ 1. Project Modules

| Module | Description |
|--------|-------------|
| **Authentication & Users** | Registration, login via Keycloak (OAuth2/OpenID), user roles and permissions |
| **Task Management** | CRUD operations for tasks (title, description, due date, priority, etc.), with validation rules |
| **Priority Suggestion (LLM)** | Integration with LLM API (OpenAI or Local), async suggestion based on task context |
| **Notifications** | Real-time alerts via WebSockets (Django Channels), async emails via Celery + RabbitMQ |
| **Admin Panel** | Improved Django Admin for task/user management, optional dashboard |
| **Messaging Microservice** | FastAPI-based microservice for event handling, LLM API, and RabbitMQ publishing |

---

### 🏛️ 2. General Architecture

```plaintext
[Frontend (future)]
      ↓
[API - Django Backend]
 ├─ Django REST Framework (Users & Tasks)
 ├─ Django Channels (WebSocket)
 ├─ Celery Workers
 └─ Django Admin

      ⇅
[FastAPI Microservice]
 ├─ /suggest-priority (LLM endpoint)
 └─ RabbitMQ publisher

      ⇅
[RabbitMQ] ⇄ [Celery Workers]
      ⇅
[PostgreSQL] [Redis] [SMTP Server]





