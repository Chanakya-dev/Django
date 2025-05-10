# 🧾 Django Notes – Part 1: Basic Commands & Installations

## ✅ 1. What is Django?

Django is a **high-level Python web framework** that allows you to build secure, scalable, and maintainable web applications quickly.

---

## 🛠️ 2. Installing Django

### 📦 Install via pip:

```bash
pip install django
```

To install a specific version:

```bash
pip install django==4.2
```

---

## 🆕 3. Creating a Django Project

```bash
django-admin startproject projectname
```

Example:

```bash
django-admin startproject mysite
```

This creates a folder structure like:

```
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 🚀 4. Running the Development Server

Navigate into your project folder:

```bash
cd mysite
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/` in your browser.

---

## 🧩 5. Creating a Django App

Apps are components inside the Django project.

```bash
python manage.py startapp appname
```

Example:

```bash
python manage.py startapp users
```

Folder structure:

```
users/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
```

---

## 🏗️ 6. Adding the App to the Project

Open `mysite/settings.py`, find the `INSTALLED_APPS` list and add your app:

```python
INSTALLED_APPS = [
    ...
    'users',
]
```
---
