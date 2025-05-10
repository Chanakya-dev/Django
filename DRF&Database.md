## ✅ **Step 1: Installing Django REST Framework (DRF)**

### 🔹 Install DRF via pip:

```bash
pip install djangorestframework
```

---

## ✅ **Step 2: Register DRF in `settings.py`**

### 🔹 Add `'rest_framework'` to `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

That’s all you need to start using DRF.

---

## ✅ **Step 3: Database Packages You Might Need**

Here are the **common database backends** and their **required packages**:

| Database             | Package to Install              |
| -------------------- | ------------------------------- |
| SQLite (default)     | Built-in with Python/Django     |
| PostgreSQL           | `psycopg2` or `psycopg2-binary` |
| MySQL                | `mysqlclient` or `PyMySQL`      |
| Oracle               | `cx_Oracle`                     |
| MongoDB (via Djongo) | `djongo` and `pymongo`          |

---

## ✅ **Step 4: Configuration for Each Database**

---

### 🔹 1. **SQLite (Default)**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

---

### 🔹 2. **PostgreSQL**

```bash
pip install psycopg2-binary
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 🔹 3. **MySQL**

```bash
pip install mysqlclient
```

*or*

```bash
pip install pymysql
```

Then in `__init__.py` (project folder), if using `pymysql`:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 🔹 4. **Oracle**

```bash
pip install cx_Oracle
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'your_service_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}
```

---

### 🔹 5. **MongoDB (via Djongo)**

```bash
pip install djongo pymongo
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_db_name',
    }
}
```

---
