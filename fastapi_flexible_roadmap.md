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
- [ ] Use a Python list as a fake database
- [ ] Implement `GET /users` and `GET /users/{user_id}`
- [ ] Implement `POST /users`
- [ ] Implement `PUT /users/{user_id}` and `DELETE /users/{user_id}`

🎯 Mini Project: “Mini-User Manager API”

---

## 💾 Module 3 — Data Persistence
- [ ] Save/load data to/from `.json` files
- [ ] Use FastAPI `startup` & `shutdown` events

🎯 Mini Project: “Persistent User API”

---

## ⚙️ Module 4 — Project Structure & Validation
- [ ] Organize folders: `app/`, `routes/`, `models.py`, `database.py`
- [ ] Use `Depends()` for shared logic
- [ ] Validate emails with `EmailStr`
- [ ] Handle optional parameters

🎯 Mini Project: Refactor User Manager API

---

## 🧠 Module 5 — Environment & Database
- [ ] Install `python-dotenv` and load `.env`
- [ ] Install `sqlmodel` (SQLAlchemy ORM + Pydantic)
- [ ] Create tables and CRUD with SQLite
- [ ] Use `HTTPException` for error handling

🎯 Mini Project: SQLite-backed User API

---

## 🌍 Module 6 — Advanced Features
- [ ] Fetch external APIs with `httpx`
- [ ] Render HTML templates with `Jinja2Templates`
- [ ] Implement token-based authentication with `Depends`
- [ ] Explore WebSockets (optional)

🎯 Mini Projects: “Weather Proxy API”, “Notes Web App”, “Protected Notes API”

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

