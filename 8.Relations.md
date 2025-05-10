## 🛠️ Project: Blog Post API

We'll build a simple blog system with these features:

* Create authors and their profiles.
* Add posts by authors.
* Assign categories to posts.
* View posts and filter by category or author.

---

## ✅ Step 1: Project & App Setup

### 1. Create virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 2. Install Django and DRF

```bash
pip install django djangorestframework
```

### 3. Create project and app

```bash
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
```

---

## ✅ Step 2: Basic Configuration

### 1. Add apps to `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'blog',
]
```

---

## ✅ Step 3: Models (`blog/models.py`)

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()
    website = models.URLField()

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category)
    published_at = models.DateTimeField(auto_now_add=True)
```

---

## ✅ Step 4: Make Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ✅ Step 5: Register Models in Admin (optional)

In `blog/admin.py`:

```python
from django.contrib import admin
from .models import Author, Profile, Post, Category

admin.site.register(Author)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
```

---

## ✅ Step 6: Create Serializers (`blog/serializers.py`)

```python
from rest_framework import serializers
from .models import Author, Profile, Post, Category

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

---

## ✅ Step 7: Create Views (`blog/views.py`)

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Post, Category
from .serializers import AuthorSerializer, PostSerializer, CategorySerializer

@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_post_by_author(request, author_id):
    posts = Post.objects.filter(author_id=author_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
```

---

## ✅ Step 8: Create URLs

In `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_all_posts),
    path('posts/author/<int:author_id>/', views.get_post_by_author),
    path('posts/create/', views.create_post),
]
```

In `blog_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]
```

---

## ✅ Step 9: Run and Test

```bash
python manage.py runserver
```

Visit:

* `http://localhost:8000/api/posts/` – Get all posts.
* `http://localhost:8000/api/posts/author/1/` – Filter by author.
* POST to `http://localhost:8000/api/posts/create/` with:

```json
{
  "title": "My First Post",
  "content": "Hello, world!",
  "author": 1,
  "categories": [1, 2]
}
```

---
