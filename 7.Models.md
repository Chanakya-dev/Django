## 📝 **Django Models and Model Fields**

### **1. What are Django Models?**

* **Django Models** are Python classes that define the structure of your database tables. Each model class corresponds to a single table in the database, and the attributes of the class represent the fields of the table.
* Models are used for **creating**, **retrieving**, **updating**, and **deleting** data in your database (CRUD operations).

#### **Key Points About Django Models:**

* **Inherit from `django.db.models.Model`**: All model classes should inherit from `django.db.models.Model`.
* **Database Abstraction**: Django automatically handles the SQL code required to create, update, and delete database records.
* **Automatic Migration System**: Django provides an automatic migration system to manage changes to the database schema.

---

### **2. Creating a Basic Model**

To create a model, define a Python class and inherit from `models.Model`. Each class attribute corresponds to a database field.

#### Example of a Basic Model:

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

#### **Explanation:**

* **`name`**: A `CharField` that stores a short string (like a name). `max_length` is required.
* **`email`**: An `EmailField` that validates the email format.
* **`age`**: An `IntegerField` that stores the user's age.
* **`date_joined`**: A `DateTimeField` that stores the timestamp when the user was created. The `auto_now_add=True` argument automatically sets this field when the object is created.

---

### **3. Model Fields in Django**

Django provides various field types for different kinds of data. Here are some of the most commonly used model fields:

#### **Text Fields:**

1. **`CharField(max_length)`**: A field for storing short text (e.g., names, titles).

   * Example: `name = models.CharField(max_length=100)`

2. **`TextField()`**: A field for storing large text without a maximum length (e.g., descriptions, articles).

   * Example: `description = models.TextField()`

#### **Numeric Fields:**

1. **`IntegerField()`**: A field for storing integers.

   * Example: `age = models.IntegerField()`

2. **`FloatField()`**: A field for storing floating-point numbers.

   * Example: `price = models.FloatField()`

3. **`DecimalField(max_digits, decimal_places)`**: A field for fixed-precision decimal numbers.

   * Example: `price = models.DecimalField(max_digits=5, decimal_places=2)`

#### **Boolean Fields:**

1. **`BooleanField()`**: A field for storing `True` or `False` values.

   * Example: `is_active = models.BooleanField(default=True)`

#### **Date/Time Fields:**

1. **`DateField()`**: A field for storing date values (without time).

   * Example: `birthdate = models.DateField()`

2. **`DateTimeField()`**: A field for storing both date and time.

   * Example: `created_at = models.DateTimeField(auto_now_add=True)`

3. **`TimeField()`**: A field for storing time values.

   * Example: `event_time = models.TimeField()`

#### **File/Media Fields:**

1. **`FileField(upload_to)`**: A field for uploading files.

   * Example: `file = models.FileField(upload_to='documents/')`

2. **`ImageField(upload_to)`**: A field for uploading image files.

   * Example: `profile_picture = models.ImageField(upload_to='profile_pics/')`

---

### **4. Meta Class in Django Models**

Django models allow you to define metadata (data about data) in a special `Meta` class within the model. This allows customization of things like the table name, ordering, verbose name, etc.

#### Example of a Meta Class:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['price']
        verbose_name = "Product Item"
        verbose_name_plural = "Product Items"
```

* **`ordering`**: Specifies the default ordering for the model’s querysets.
* **`verbose_name`**: A human-readable singular name for the object (used in the admin interface).
* **`verbose_name_plural`**: The plural form of `verbose_name`.

---

### **5. Working with Django Migrations**

* **Migrations** are Django’s way of propagating changes you make to your models into the database schema. They are a way to evolve your database as your models change.
* After creating or modifying a model, you need to generate and apply migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

  * **`makemigrations`**: Creates migration files from your model changes.
  * **`migrate`**: Applies the migration files to the database, updating the schema.

---

### **Summary:**

* **Models**: Python classes that define the structure of your database.
* **Model Fields**: Represent different types of data stored in a model. Examples include `CharField`, `IntegerField`, `DateTimeField`
* **Meta Class**: Used for additional customization of model behavior (e.g., ordering, verbose name).
* **Migrations**: Used to propagate changes to models into the database schema.

---
