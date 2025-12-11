# FastAPI RoadMap With GPT 🚀

A comprehensive, milestone-based learning path for mastering FastAPI, created with the assistance of ChatGPT. This repository provides a flexible, hands-on approach to learning FastAPI through progressive modules—from basics to production-ready applications. Learn at your own pace and avoid tutorial hell by building real mini-projects after each concept.

## 📚 Overview

This project serves as both a learning resource and a reference implementation for FastAPI development. It's organized into progressive milestones that cover everything from basic setup to advanced production-ready features. Each module builds upon the previous one with practical mini-projects, creating a complete learning journey that emphasizes doing over watching.

## ✨ Features

- **Milestone-Based Learning**: Focus on completion, not time spent
- **Hands-on Mini-Projects**: Build something real after every module
- **AI-Assisted Content**: Roadmap and examples curated with ChatGPT
- **Production-Ready Patterns**: Industry best practices and patterns
- **Comprehensive Coverage**: From basics to advanced topics
- **Flexible Self-Paced Learning**: No strict timelines—learn at your speed
- **Anti-Tutorial Hell**: Build projects immediately after learning concepts

## 🎯 Who Is This For?

- **Beginners**: New to FastAPI and want a structured, practical learning path
- **Intermediate Developers**: Looking to strengthen FastAPI knowledge with real projects
- **Backend Engineers**: Transitioning from other frameworks to FastAPI
- **API Developers**: Want to build modern, high-performance APIs
- **Self-Learners**: Prefer organized, milestone-driven learning materials

## 📁 Project Structure

```
FastApiRoadMapWithGpt/
├── __pycache__/              # Python cache files
├── app/                      # Main application directory
│   ├── routers/             # API route definitions
│   ├── models/              # Data models
│   ├── schemas/             # Pydantic schemas
│   ├── database/            # Database configuration
│   └── main.py              # Application entry point
├── app-module5/             # Modules 2 through 5 implementations (the rest will be in sepreate repos)
├── module1.py               # Module 1: Basics
├── fastapi_flexible_roadmap.md  # Complete learning roadmap
├── .env                     # Environment variables (create this)
└── README.md                # This file
```

## 🗺️ Learning Roadmap

### ⚙️ Setup (Before Module 1)
**Goal**: Get your development environment ready

- Install Python 3.8+, pip, and venv
- Create virtual environment
- Install FastAPI and Uvicorn

**Time Estimate**: 15-30 minutes

---

### 🧩 Module 1: FastAPI Basics
**Status**: ✅ Complete

**What You'll Learn**:
- Setting up FastAPI project
- Creating your first endpoint
- Path parameters (`/hello/{name}`)
- Query parameters (`/search?q=...`)
- Pydantic models for validation
- POST endpoints with request bodies

**Mini Projects**: 
- Greeter API
- User Registration API

**Key Skills**: Basic routing, request handling, data validation

---

### 🧰 Module 2: CRUD Basics
**Status**: ✅ Complete

**What You'll Learn**:
- In-memory data storage (Python lists)
- Implement all CRUD operations:
  - `GET /users` - List all users
  - `GET /users/{user_id}` - Get specific user
  - `POST /users` - Create new user
  - `PUT /users/{user_id}` - Update user
  - `DELETE /users/{user_id}` - Delete user

**Mini Project**: Mini-User Manager API

**Key Skills**: RESTful API design, CRUD patterns, HTTP methods

---

### 💾 Module 3: Data Persistence
**Status**: ✅ Complete

**What You'll Learn**:
- File-based data storage (JSON files)
- FastAPI lifespan events
- Loading and saving data automatically
- Data persistence between server restarts

**Mini Project**: Persistent User API

**Key Skills**: File I/O, application lifecycle management

---

### ⚙️ Module 4: Project Structure & Validation
**Status**: ✅ Complete

**What You'll Learn**:
- Professional project organization
- Folder structure: `app/`, `routes/`, `models.py`, `database.py`
- Advanced validation (unique emails, IDs)
- Consistent error handling with `HTTPException`
- HTTP status codes (200, 201, 404, 409, etc.)
- PATCH method for partial updates
- Dependency injection with `Depends()`
- Email validation with `EmailStr`
- Optional parameters handling

**Mini Project**: Refactored User Manager API

**Key Skills**: Code organization, validation, error handling, DRY principles

---

### 🧠 Module 5: Environment & Database
**Status**: ✅ Complete

**What You'll Learn**:
- Environment variables with `python-dotenv`
- SQLModel (SQLAlchemy ORM + Pydantic combined)
- Database schema creation
- SQLite database integration
- Production-grade error handling
- Database CRUD operations with ORM

**Mini Project**: SQLite-backed User API

**Key Skills**: Database design, ORM usage, environment configuration

---

### 🌍 Module 6: Advanced Features
**Status**: 🚧 In Progress

**What You'll Learn**:
- ✅ External API calls with `httpx`
- ⏳ HTML rendering with `Jinja2Templates`
- ⏳ Token-based authentication (OAuth2, JWT)
- ⏳ Protected routes with `Depends`
- ⏳ WebSockets for real-time features

**Learning Path**:
1. **httpx** - Weather Proxy API (fetch external APIs)
2. **Jinja2** - Notes Web App (render HTML templates)
3. **Authentication** - Protected Notes API (secure endpoints)
4. **WebSockets** - Live Chat (real-time communication)

**Mini Projects**: 
- Weather Proxy API
- Notes Web App with HTML UI
- Protected Notes API
- Live Note Updates or Mini-Chat 

**Key Skills**: External integrations, templating, authentication, real-time features

---

### 🏁 Module 7: Final Project
**Status**: ⏳ Not Started

**What You'll Build**: Full-Featured Task Tracker API

**Features to Implement**:
- Complete CRUD for tasks
- SQLite/PostgreSQL storage
- User authentication & authorization
- Environment-based configuration
- Automatic API documentation (`/docs`)
- Error handling and logging
- Input validation
- Response models

**Key Skills**: Integrating everything learned, production-ready API development

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Basic understanding of Python
- Familiarity with REST APIs (helpful but not required)

### Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/Ibr4h3m-k4m/FastApiRoadMapWithGpt.git
cd FastApiRoadMapWithGpt

# 2. Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic python-multipart python-dotenv sqlmodel httpx

# 4. Run Module 1 (Basic example)
uvicorn module1:app --reload

# 5. Access API documentation
# Open browser: http://localhost:8000/docs
```

### Running Different Modules

```bash
# Module 1 - Basics
uvicorn module1:app --reload

# Module 5 - Database integration
cd app-module5
uvicorn main:app --reload

# Main Application
cd app
uvicorn main:app --reload
```

## 📖 Code Examples

### Basic FastAPI Endpoint (Module 1)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/search")
def search_items(q: str = None):
    return {"query": q}
```

### Pydantic Models with Validation (Module 1)

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created", "data": user}
```

### CRUD Operations (Module 2)

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
users_db = []

@app.get("/users")
def get_users():
    return users_db

@app.post("/users", status_code=201)
def create_user(user: User):
    users_db.append(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id >= len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(user_id)
    return {"message": "User deleted"}
```

### Dependency Injection (Module 4)

```python
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def get_current_user(user_id: int):
    # Simulated user lookup
    if user_id not in range(1, 100):
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "name": f"User{user_id}"}

@app.get("/profile")
def get_profile(user: dict = Depends(get_current_user)):
    return user
```

### SQLModel Database Integration (Module 5)

```python
from fastapi import FastAPI, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/users", status_code=201)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/users")
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()
```

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server
- **Pydantic**: Data validation using Python type annotations
- **SQLModel**: SQL databases with Python objects (SQLAlchemy + Pydantic)
- **SQLAlchemy**: SQL toolkit and ORM
- **python-dotenv**: Environment variable management
- **httpx**: Modern HTTP client for external API calls
- **Python 3.8+**: Core programming language

## 📚 Learning Resources

### Official Documentation
- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Additional Resources
- [FastAPI Tutorial Series](https://fastapi.tiangolo.com/tutorial/)
- [Real Python FastAPI Guide](https://realpython.com/fastapi-python-web-apis/)
- [Awesome FastAPI](https://github.com/mjhea0/awesome-fastapi)

## 🎓 Learning Tips & Best Practices

### For Success
1. **Follow Modules Sequentially**: Each module builds on previous concepts
2. **Complete Mini-Projects**: Build something after every module—don't just read
3. **Experiment Freely**: Modify examples, break things, fix them
4. **Use `/docs` Constantly**: Test your endpoints in the interactive documentation
5. **Refactor Regularly**: Improve your code as you learn new patterns
6. **Take Notes**: Document what you learn in your own words
7. **Avoid Tutorial Hell**: Build projects immediately after learning concepts

### Daily Practice
- Spend 20-30 minutes daily on focused learning
- Build one mini-project per module
- Review previous modules' code
- Keep a learning journal

### When Stuck
- Check `/docs` for automatic API documentation
- Read error messages carefully—FastAPI errors are helpful
- Use `print()` statements to debug
- Review the module's mini-project example
- Ask in FastAPI Discord community

## 📝 Module Checklist

Track your progress through the roadmap:

- [x] **Setup**: Development environment ready
- [x] **Module 1**: FastAPI Basics ✅
- [x] **Module 2**: CRUD Basics ✅
- [x] **Module 3**: Data Persistence ✅
- [x] **Module 4**: Project Structure & Validation ✅
- [x] **Module 5**: Environment & Database ✅
- [ ] **Module 6**: Advanced Features 🚧
  - [x] httpx (External APIs)
  - [ ] Jinja2 (Templates)
  - [ ] Authentication (Tokens)
  - [ ] WebSockets
- [ ] **Module 7**: Final Project (Task Tracker)

**Current Progress**: (5/7 modules)

## 🧪 Testing

```bash
# Install testing dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_users.py -v
```

## 🤝 Contributing

Contributions are welcome! This is a learning resource, and community input makes it better.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-module`)
3. Add your module or improvements
4. Test your changes
5. Commit with clear messages (`git commit -m 'Add WebSocket module with chat example'`)
6. Push to the branch (`git push origin feature/new-module`)
7. Open a Pull Request

### Contribution Ideas

- Add new learning modules (Module 8, 9, etc.)
- Create more mini-project examples
- Improve existing code examples
- Add comprehensive tests
- Write tutorials or guides
- Fix bugs or typos
- Add translations
- Create video tutorials

## 🌟 Key FastAPI Features Covered

- ⚡ **High Performance**: On par with NodeJS and Go
- 🔍 **Type Hints**: Full support for Python type hints
- 📚 **Auto Documentation**: Automatic interactive API docs (Swagger UI)
- ✅ **Validation**: Automatic data validation via Pydantic
- 🔐 **Security**: OAuth2, JWT tokens, API key authentication
- 🔌 **Dependency Injection**: Powerful and easy to use
- 🧪 **Testing**: Built-in testing utilities
- 🚀 **Async Support**: Native async/await support
- 💾 **Database Integration**: SQLModel, SQLAlchemy support
- 📁 **Project Structure**: Scalable application architecture

## ❓ FAQ

### Q: Do I need prior FastAPI experience?
**A:** No, this roadmap starts from the basics and progressively builds knowledge with hands-on projects.

### Q: How long does it take to complete?
**A:** It depends on your pace. Expect 4-6 weeks for thorough learning, but there's no rush—focus on understanding, not speed.

### Q: Can I skip modules?
**A:** Not recommended. Modules build on each other, and skipping creates knowledge gaps. However, if you're already familiar with basics, you might start from Module 3-4.

### Q: Is this suitable for production projects?
**A:** Yes! The patterns and practices taught are production-ready and follow industry best practices.

### Q: What if I get stuck?
**A:** Use the `/docs` endpoint, check error messages, review mini-projects, and join the FastAPI Discord community.

### Q: Do I need to know SQL?
**A:** Basic SQL knowledge helps, but SQLModel abstracts most SQL away. You'll learn as you go.

### Q: Can I use PostgreSQL instead of SQLite?
**A:** Absolutely! SQLModel works with PostgreSQL, MySQL, and other databases. Just change the connection string.

## 📧 Contact & Support

**Project Maintainer**: Ibr4h3m-k4m

**Repository**: [https://github.com/Ibr4h3m-k4m/FastApiRoadMapWithGpt](https://github.com/Ibr4h3m-k4m/FastApiRoadMapWithGpt)

- 🐛 **Report Issues**: [GitHub Issues](https://github.com/Ibr4h3m-k4m/FastApiRoadMapWithGpt/issues)
- 💡 **Suggest Features**: Open an issue with the "enhancement" label
- 💬 **Discussions**: Use GitHub Discussions for questions
- 📖 **Detailed Roadmap**: See [fastapi_flexible_roadmap.md](fastapi_flexible_roadmap.md)


## 🔗 Useful Links

- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Python Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [REST API Best Practices](https://restfulapi.net/)

## 📊 Project Stats

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Progress](https://img.shields.io/badge/progress-71%25-yellow.svg)

---

## 💡 Final Words

**Remember**: Learning FastAPI is a marathon, not a sprint. Focus on understanding concepts through building real projects rather than rushing through tutorials. Each mini-project reinforces what you've learned and prepares you for the next milestone.

### Your Learning Journey
1. **Build after every module** - Don't just read, create
2. **Experiment freely** - Breaking things teaches you how they work
3. **Review regularly** - Go back and improve old code with new knowledge
4. **Join the community** - Learn from others, share your progress
5. **Stay consistent** - 20-30 minutes daily beats 5 hours once a week

**Happy Learning! 🎉**

*Master FastAPI one milestone at a time. Every expert was once a beginner who refused to give up.*

---

Made with 💻 and ☕ by Ibr4h3m-k4m | Powered by AI LLMs 