<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=009688&center=true&vCenter=true&width=900&lines=Library+Management+API;Async+FastAPI+%7C+Neon+Postgres+%7C+Docker;Full+CRUD+for+Books+%26+Users;Production-Ready+Backend+Architecture" />

<p>
  <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/FastAPI-Async-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-Neon-00E699?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

</div>

<h2 align="center">⚡ Overview</h2>

<p align="center">
  <b>What does a truly async, containerized, cloud-connected REST API look like?</b><br>
  I built a production-grade <b>Library Management API</b> with full CRUD for Books and Users,
  running on a fully asynchronous stack — from the HTTP layer down to the database driver.
</p>

<p align="center">
  This project explores:<br>
  ⚡ <b>True Async I/O:</b> FastAPI + asyncpg with no blocking calls anywhere in the stack.<br>
  ☁️ <b>Cloud Postgres:</b> Connected to a Neon serverless Postgres instance over SSL.<br>
  🐳 <b>Docker:</b> Fully containerized with a clean, minimal python:3.12-slim image.<br>
  🔄 <b>Alembic Migrations:</b> Schema versioning for safe, repeatable database changes.<br>
  🛡️ <b>Performance Middleware:</b> Custom HTTP middleware measuring per-request processing time.
</p>

<br>

<h2 align="center">⚙️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,docker" />
</p>

<table align="center">
  <tr>
    <th>Category</th>
    <th>Technology</th>
    <th>Role</th>
  </tr>
  <tr>
    <td align="center"><b>Framework</b></td>
    <td align="center"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /></td>
    <td align="center">Async ASGI web framework</td>
  </tr>
  <tr>
    <td align="center"><b>Database</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Neon-PostgreSQL-00E699?style=flat-square&logo=postgresql&logoColor=white" /></td>
    <td align="center">Serverless cloud Postgres</td>
  </tr>
  <tr>
    <td align="center"><b>Async Driver</b></td>
    <td align="center"><img src="https://img.shields.io/badge/asyncpg-Driver-4169E1?style=flat-square&logo=python&logoColor=white" /></td>
    <td align="center">Non-blocking Postgres driver</td>
  </tr>
  <tr>
    <td align="center"><b>ORM</b></td>
    <td align="center"><img src="https://img.shields.io/badge/SQLAlchemy-Async-red?style=flat-square&logo=databricks&logoColor=white" /></td>
    <td align="center">Async ORM + session management</td>
  </tr>
  <tr>
    <td align="center"><b>Migrations</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Alembic-Migrations-6BA539?style=flat-square&logo=python" /></td>
    <td align="center">Versioned schema management</td>
  </tr>
  <tr>
    <td align="center"><b>Validation</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pydantic-v2-blue?style=flat-square&logo=python" /></td>
    <td align="center">Request & response schemas</td>
  </tr>
  <tr>
    <td align="center"><b>Container</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /></td>
    <td align="center">python:3.12-slim image</td>
  </tr>
</table>

<br>

<h2 align="center">🛣️ API Endpoints</h2>

**Books**

| Method | Endpoint | Description |
|:---|:---|:---|
| `POST` | `/books/` | Create a new book (linked to an owner) |
| `GET` | `/books/` | Retrieve all books |
| `GET` | `/books/{id}` | Retrieve a single book by ID |
| `PUT` | `/books/{id}` | Update a book's details |
| `DELETE` | `/books/{id}` | Delete a book |

**Users**

| Method | Endpoint | Description |
|:---|:---|:---|
| `POST` | `/users/` | Register a new user |
| `GET` | `/users/` | Retrieve all users |
| `GET` | `/users/{id}` | Retrieve a single user by ID |
| `PUT` | `/users/{id}` | Update user details |
| `DELETE` | `/users/{id}` | Delete a user |

<br>

<h2 align="center">🧠 Architecture & Engineering Decisions</h2>

<p align="center">
  Every layer of this API is non-blocking — from request handling to database queries.
</p>

### 🔧 Key Techniques

- **Fully Async Stack:** Used `create_async_engine` + `asyncpg` so database queries never block the event loop. SQLAlchemy's `AsyncSession` handles all ORM operations without a single `await` misfire.
- **SSL-Secured Neon Connection:** Neon requires SSL. Rather than embedding `?sslmode=require` in the URL (which conflicts with asyncpg), a custom `ssl.SSLContext` is passed via `connect_args` — a subtle but critical distinction.
- **Lifespan Events:** Database table creation runs inside FastAPI's `@asynccontextmanager lifespan` hook — the modern replacement for deprecated `on_event("startup")` handlers.
- **Performance Middleware:** A custom HTTP middleware injects an `X-Process-Time` header into every response and logs processing time to the console — useful for profiling in development.
- **Schema vs. Model Separation:** `BookCreate` / `UserCreate` (Pydantic) handle incoming data. `Book` / `User` (SQLAlchemy) handle persistence. `owner_id` on books enforces the User → Book relationship at the schema level.
- **Alembic Migrations:** Schema changes are version-controlled via Alembic, enabling safe rollbacks and repeatable deployments.
- **Docker:** The app runs in a `python:3.12-slim` container, copying only the `app/` directory into `/code/app` and launching via `fastapi run` on port 80.

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

### Option A — Run locally

**1. Clone the repository**

```bash
git clone https://github.com/ManzarMaaz/library-api.git
cd library-api
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:

```env
DATABASE_URL="postgresql+asyncpg://user:password@your-neon-host/dbname"
```

> Get your connection string from [neon.tech](https://neon.tech). Use the `postgresql+asyncpg://` prefix — **not** `postgresql://`.

**5. Run Alembic migrations**

```bash
alembic upgrade head
```

**6. Launch the server**

```bash
uvicorn app.main:app --reload
```

Navigate to `http://127.0.0.1:8000/docs` for the Swagger UI.

---

### Option B — Run with Docker

**1. Build the image**

```bash
docker build -t library-api .
```

**2. Run the container**

```bash
docker run -p 80:80 -e DATABASE_URL="postgresql+asyncpg://user:password@host/dbname" library-api
```

Navigate to `http://localhost/docs` for the Swagger UI.

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
