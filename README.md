<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=009688&center=true&vCenter=true&width=900&lines=Library+Management+API;Deployed+on+Railway+%F0%9F%9A%82;Async+FastAPI+%7C+JWT+Auth+%7C+Docker+CI%2FCD;Silicon+Valley-Grade+Backend+Infrastructure" />

<p>
  <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://library-api-production-0fd2.up.railway.app/docs">
    <img src="https://img.shields.io/badge/Live%20Demo-Railway-7B2FBE?style=for-the-badge&logo=railway&logoColor=white" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.14-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/Coverage-65%25-009688?style=for-the-badge&logo=pytest&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/FastAPI-Async-009688?style=flat-square&logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-Neon-00E699?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Multi--Stage-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-Auth-black?style=flat-square&logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/Alembic-Migrations-6BA539?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Ruff-Linter-D7FF64?style=flat-square&logo=python&logoColor=black" />
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

</div>

<h2 align="center">⚡ Overview</h2>

<p align="center">
  <b>Not just an API — a complete backend engineering system, live on the internet.</b><br>
  This project goes beyond writing endpoints. It covers the full journey from local development
  to a <b>production deployment on Railway</b> — with JWT authentication, Docker CI/CD,
  automated testing, and code quality enforcement baked in at every layer.
</p>

<p align="center">
  <a href="https://library-api-production-0fd2.up.railway.app/docs">
    <b>🔗 Live API → library-api-production-0fd2.up.railway.app</b>
  </a>
</p>

<br>

<h2 align="center">🏗️ Architecture at a Glance</h2>

```mermaid
graph TD
    A[Client Request] --> B[Railway Cloud]
    B --> C[Docker Container]
    C --> D[FastAPI + Uvicorn]
    D --> E{JWT Middleware}
    E -->|Authenticated| F[APIRouter]
    E -->|Rejected| G[401 Unauthorized]
    F --> H[Books Router]
    F --> I[Users Router]
    H --> J[AsyncSession / asyncpg]
    I --> J
    J --> K[(Neon PostgreSQL)]
    L[Pre-commit + Ruff] -->|blocks bad code| D
    M[Pytest + httpx CI] -->|runs in Docker| D
```

<br>

<h2 align="center">⚙️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,docker,railway" />
</p>

<table align="center">
  <tr>
    <th>Layer</th>
    <th>Technology</th>
    <th>Role</th>
  </tr>
  <tr>
    <td align="center"><b>Framework</b></td>
    <td align="center"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /></td>
    <td align="center">Async ASGI web framework</td>
  </tr>
  <tr>
    <td align="center"><b>Auth</b></td>
    <td align="center"><img src="https://img.shields.io/badge/JWT-python--jose-black?style=flat-square&logo=jsonwebtokens&logoColor=white" /></td>
    <td align="center">Token-based auth + bcrypt hashing</td>
  </tr>
  <tr>
    <td align="center"><b>Database</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Neon-PostgreSQL-00E699?style=flat-square&logo=postgresql&logoColor=white" /></td>
    <td align="center">Serverless cloud Postgres</td>
  </tr>
  <tr>
    <td align="center"><b>Async Driver</b></td>
    <td align="center"><img src="https://img.shields.io/badge/asyncpg-4169E1?style=flat-square&logo=python&logoColor=white" /></td>
    <td align="center">Non-blocking Postgres driver</td>
  </tr>
  <tr>
    <td align="center"><b>ORM</b></td>
    <td align="center"><img src="https://img.shields.io/badge/SQLAlchemy-Async-red?style=flat-square&logo=databricks&logoColor=white" /></td>
    <td align="center">Async ORM + session management</td>
  </tr>
  <tr>
    <td align="center"><b>Migrations</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Alembic-6BA539?style=flat-square&logo=python" /></td>
    <td align="center">Versioned schema management</td>
  </tr>
  <tr>
    <td align="center"><b>Container</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Docker-Multi--Stage-2496ED?style=flat-square&logo=docker&logoColor=white" /></td>
    <td align="center">Lean prod image, heavy dev image separated</td>
  </tr>
  <tr>
    <td align="center"><b>Orchestration</b></td>
    <td align="center"><img src="https://img.shields.io/badge/docker--compose-2496ED?style=flat-square&logo=docker&logoColor=white" /></td>
    <td align="center">Syncs FastAPI container + Neon DB</td>
  </tr>
  <tr>
    <td align="center"><b>Testing</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pytest-httpx.AsyncClient-009688?style=flat-square&logo=pytest&logoColor=white" /></td>
    <td align="center">Async test suite — 65% coverage</td>
  </tr>
  <tr>
    <td align="center"><b>Code Quality</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Ruff-pre--commit-D7FF64?style=flat-square&logo=python&logoColor=black" /></td>
    <td align="center">Lint + auto-fix before every commit</td>
  </tr>
  <tr>
    <td align="center"><b>Deployment</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Railway-7B2FBE?style=flat-square&logo=railway&logoColor=white" /></td>
    <td align="center">Live cloud deployment w/ encrypted env vars</td>
  </tr>
</table>

<br>

<h2 align="center">🛣️ API Endpoints</h2>

**Books**

| Method | Endpoint | Auth | Description |
|:---|:---|:---|:---|
| `POST` | `/books/` | 🔒 JWT | Create a new book (linked to owner) |
| `GET` | `/books/` | ✅ Public | Retrieve all books |
| `GET` | `/books/{id}` | ✅ Public | Retrieve a single book by ID |
| `PUT` | `/books/{id}` | 🔒 JWT | Update a book's details |
| `DELETE` | `/books/{id}` | 🔒 JWT | Delete a book |

**Users**

| Method | Endpoint | Auth | Description |
|:---|:---|:---|:---|
| `POST` | `/users/register` | ✅ Public | Register a new user |
| `POST` | `/users/login` | ✅ Public | Authenticate and receive JWT token |
| `GET` | `/users/{id}` | 🔒 JWT | Retrieve user profile |
| `PUT` | `/users/{id}` | 🔒 JWT | Update user details |
| `DELETE` | `/users/{id}` | 🔒 JWT | Delete a user |

**Health**

| Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/` | Health check — returns `{"status": "healthy", "environment": "production"}` |

<br>

<h2 align="center">🧠 Engineering Decisions</h2>

### 🔐 Authentication
JWT tokens are issued on login using `python-jose`. Passwords are hashed with `bcrypt` — plain text never touches the database. Protected routes use FastAPI's `Depends()` to verify tokens on every request.

### ⚡ Fully Async Stack
`create_async_engine` + `asyncpg` ensures zero thread blocking from HTTP handler down to the Postgres wire protocol. SQLAlchemy's `AsyncSession` handles all ORM operations without a synchronous fallback anywhere in the chain.

### 🔒 SSL Without the asyncpg URL Conflict
Neon requires SSL. Embedding `?sslmode=require` in the connection URL causes a known conflict with asyncpg. The fix: a custom `ssl.SSLContext` passed through `connect_args` — bypassing the URL parser entirely and forcing SSL at the driver level.

### 🐳 Multi-Stage Docker Build
The `Dockerfile` separates build stages so Pytest, dev tools, and test dependencies stay out of the final production image. The result is a lean, fast container that only ships what it needs to run.

### 🔄 Lifespan Events
`Base.metadata.create_all` runs inside FastAPI's `@asynccontextmanager lifespan` hook — the modern replacement for the deprecated `on_event("startup")` pattern. Engine disposal on shutdown is also handled cleanly.

### 📊 Performance Middleware
Every HTTP response carries an `X-Process-Time` header measuring exact request duration via `time.perf_counter()`. Useful for profiling bottlenecks without an external APM tool.

### 🧪 CI Testing in Docker
The test suite uses `httpx.AsyncClient` with `ASGITransport` to test the full async request cycle without spinning up a real server. Tests run inside the Docker container — the same environment as production.

### 🪝 Pre-commit + Ruff
`pre-commit` hooks run Ruff on every `git commit`. Bad syntax, unused imports, and style violations are caught and auto-fixed before they ever reach GitHub.

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

### Option A — Run locally

```bash
# 1. Clone
git clone https://github.com/ManzarMaaz/library-api.git
cd library-api

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
# Create a .env file:
DATABASE_URL="postgresql+asyncpg://user:password@your-neon-host/dbname"
SECRET_KEY="your-jwt-secret-key"
ALGORITHM="HS256"

# 5. Run Alembic migrations
alembic upgrade head

# 6. Start the server
uvicorn app.main:app --reload
```

Navigate to `http://127.0.0.1:8000/docs` for Swagger UI.

---

### Option B — Run with Docker Compose

```bash
# Build and run
docker-compose up --build

# Run tests inside the container
docker-compose run app pytest --cov=app
```

Navigate to `http://localhost/docs` for Swagger UI.

---

### Option C — Hit the live API

```
https://library-api-production-0fd2.up.railway.app/docs
```

<br>

<div align="center">
  <h3>👤 Author: Mohammed Manzar Maaz</h3>
  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <a href="https://github.com/ManzarMaaz">
      <img src="https://img.shields.io/github/followers/ManzarMaaz?label=Follow&style=social" />
    </a>
  </p>
</div>
