## 📝 **Django Templates**

### **What are Templates in Django?**

Django templates allow you to separate the presentation (HTML structure) of your web application from its logic (Python code). Templates are used to generate dynamic HTML by embedding Python-like syntax inside HTML files.

Django templates provide a way to embed Python code in HTML files using special template tags and filters.

---

### **Key Concepts of Django Templates**

1. **Template Files**:

   * Template files are usually stored in the `templates` directory of your Django app.
   * They can be HTML files or any other content type you want to generate dynamically (e.g., XML, JSON).

   Example:

   ```
   myapp/
       templates/
           myapp/
               home.html
   ```

2. **Template Rendering**:

   * Rendering a template involves combining the template file with data and returning the resulting HTML to the client.
   * This is done using the `render()` function.

   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html', {'message': 'Hello, world!'})
   ```

   In this example, the data `{'message': 'Hello, world!'}` will be passed to the `home.html` template.

---

### **Template Syntax**

Django templates are very flexible and allow you to use logic and data inside HTML.

#### 1. **Variables**

* Variables are inserted into the template using `{{ variable_name }}`.

Example:

```html
<h1>{{ message }}</h1>
```

This would output the value of `message`.

#### 2. **Template Tags**

* Template tags are enclosed within `{% %}` and are used for logic, loops, and other functions.
* Some common tags include `if`, `for`, and `block`.

Example of an `if` tag:

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

Example of a `for` loop:

```html
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

#### 3. **Filters**

* Filters are used to modify variables before displaying them.
* They are applied to variables using the `|` (pipe) character.

Example of using a filter:

```html
<p>{{ message|lower }}</p>
```

This would convert the value of `message` to lowercase.

Common filters:

* `lower` – Converts a string to lowercase.
* `upper` – Converts a string to uppercase.
* `date` – Formats a date.
* `length` – Returns the length of a list or string.

Example of `date` filter:

```html
<p>{{ post_date|date:"F j, Y" }}</p>
```

This will format the `post_date` in a readable format like "January 1, 2025".

#### 4. **Comments**

* Django templates allow you to add comments that won’t be rendered in the HTML output.
* Template comments are enclosed by `{# #}`.

Example:

```html
{# This is a comment #}
<p>This will be displayed</p>
```

#### 5. **Inheritance**

* Template inheritance allows you to create a base template with a common layout (like a header, footer, and navigation), and then extend it in other templates.

Base Template (base.html):

```html
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    {% block content %}{% endblock %}
</body>
</html>
```

Child Template (home.html):

```html
{% extends 'base.html' %}

{% block content %}
    <h2>Welcome to the Home Page!</h2>
{% endblock %}
```

In this case, `home.html` inherits the structure defined in `base.html` but overrides the `content` block to provide its own content.

---

### **Template Loading and Configuration**

1. **Template Settings**:

   * Django looks for templates in directories listed under the `TEMPLATES` setting in your `settings.py` file.

   Example:

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   * The `DIRS` option specifies where Django will look for global templates (like `base.html`), and `APP_DIRS=True` ensures Django looks for templates within each app's `templates` folder.

---

### **Common Template Usage**

1. **Static Files (CSS, JS, Images)**:

   * You can include static files (CSS, JavaScript, images) using `{% load static %}` in your template and the `{% static 'path/to/file' %}` tag.

   Example:

   ```html
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/styles.css' %}">
   <script src="{% static 'js/app.js' %}"></script>
   ```

2. **Forms**:

   * Django makes it easy to display forms. You can either manually render form fields or use Django's form rendering system.

   Example:

   ```html
   <form method="post">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Submit</button>
   </form>
   ```

3. **URL Tag**:

   * The `{% url %}` tag generates the URL for a given view by name.

   Example:

   ```html
   <a href="{% url 'home' %}">Home</a>
   ```

---

### **Advanced Template Features**

1. **Custom Template Tags and Filters**:

   * Django allows you to create custom template tags and filters for more complex functionality.
   * Custom tags are defined in a `templatetags` directory within your app.

2. **Template Context**:

   * You can pass context variables to your templates from views, allowing dynamic data to be displayed in the template.

   Example:

   ```python
   def home(request):
       context = {
           'name': 'John Doe',
           'age': 30,
       }
       return render(request, 'home.html', context)
   ```

---

### **Summary**

Django templates help you separate the HTML structure from your Python code, making it easier to maintain and manage your web application’s front end. Here are the key points:

* **Variables**: Used to display dynamic data.
* **Tags**: Control logic (loops, conditionals, etc.).
* **Filters**: Modify data before displaying it.
* **Inheritance**: Reuse common layout across pages.
* **Static Files**: Load CSS, JS, and images in templates.
* **Custom Tags/Filters**: Extend template functionality.
