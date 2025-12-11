# 🚀 FastAPI Milestone Roadmap (Flexible Pace)

This plan helps you learn FastAPI effectively without falling into tutorial hell.
Each module focuses on a milestone rather than strict days, so you can learn at your own speed.

---

## ⚙️ Setup (Before Module 1)

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
mkdir fastapi_lab && cd fastapi_lab
python3 -m venv venv && source venv/bin/activate
pip install fastapi uvicorn
```

---

## 🧩 Module 1 — FastAPI Basics
- [X] Install FastAPI & Uvicorn
- [X] Create simple `GET /` route
- [X] Use path parameters `/hello/{name}`
- [X] Use query parameters `/search?q=...`
- [X] Define Pydantic `User` model
- [X] Add `POST /users` endpoint

🎯 Mini Projects: “Greeter API”, “User Registration API”

---

## 🧰 Module 2 — CRUD Basics
- [X] Use a Python list as a fake database
- [X] Implement `GET /users` and `GET /users/{user_id}`
- [X] Implement `POST /users`
- [X] Implement `PUT /users/{user_id}` and `DELETE /users/{user_id}`

🎯 Mini Project: “Mini-User Manager API”

---

## 💾 Module 3 — Data Persistence
- [X] Save/load data to/from `.json` files
- [X] Use FastAPI 'lifespan' events

🎯 Mini Project: “Persistent User API”

---

## ⚙️ Module 4 — Project Structure & Validation
- [X] Organize folders: `app/`, `routes/`, `models.py`, `database.py`
- [X] Fix api crud logic (no double id/email/name, non updatable id)
- [X] Implement Consistent Status Handling using HTTPException and add PATCH HTTP method
- [X] Use `Depends()` for shared logic (simplify the logic to avoid writing the same code repedeatly and avoid additional loops)
- [X] Validate emails with `EmailStr`
- [X] Handle optional parameters

🎯 Mini Project: Refactor User Manager API

---

## 🧠 Module 5 — Environment & Database
- [X] Install `python-dotenv` and load `.env`
- [X] Install `sqlmodel` (SQLAlchemy ORM + Pydantic)
- [X] Create tables and CRUD with SQLite
- [X] Use `HTTPException` for error handling

🎯 Mini Project: SQLite-backed User API

---

## 🌍 Module 6 — Advanced Features
- [X] Fetch external APIs with `httpx`
- [ ] Render HTML templates with `Jinja2Templates`
- [ ] Implement token-based authentication with `Depends`
- [ ] Explore WebSockets (optional)

🎯 Mini Projects: “Weather Proxy API”, “Notes Web App”, “Protected Notes API”

1️⃣ Start with httpx (External API Requests) 

Easiest starting point

Helps you understand async requests & FastAPI integration

👉 Mini-Project: Weather Proxy API

You call a real weather API → return simplified JSON.
2️⃣ Add Jinja2 HTML Templates

Learn rendering HTML pages

Perfect for building small dynamic web UIs

👉 Mini-Project: Notes Web App (HTML UI)

List notes → add notes → show them in templates.

3️⃣ Implement Token-Based Authentication

Learn Depends, OAuth2PasswordBearer, tokens

Introduces protected routes

👉 Mini-Project: Protected Notes API

Users must log in → get token → access /notes.

4️⃣ Explore WebSockets (Optional)

Real-time features

Chat, notifications

👉 Mini-Project (optional): Live Note Updates or Mini-Chat

---

## 🏁 Module 7 — Final Project
Combine everything learned:
- CRUD for tasks
- SQLite storage
- Authentication middleware
- `.env` configuration
- `/docs` documentation

🎯 Mini Project: “Task Tracker”

---

## 🔹 Tips for Success
- Focus on **modules**, not time spent
- Build mini-projects immediately after learning concepts
- Refactor and improve your code incrementally
- Test routes regularly using `/docs`
- Keep notes and save daily progress