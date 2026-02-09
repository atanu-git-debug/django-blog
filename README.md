# Django Blog Platform

A full‑stack blog web application built with Django featuring authentication, admin dashboard, post & category management, and a user comment system.

---

## 🚀 Features

### Authentication

* User registration & login (Django default authentication)
* Secure password hashing & validation
* Session‑based login system
* Logout functionality

### Dashboard

* Personalized dashboard after login
* Statistics overview (Total Categories & Posts)
* Sidebar navigation panel

### Category Management (CRUD)

* Create categories
* Update categories
* Delete categories
* Automatic created & updated timestamps

### Post Management (CRUD)

* Create, edit and delete blog posts
* Assign category & author
* Upload featured image
* Publish / draft status
* Featured post option for homepage banner

### Comment System

* Users can comment on posts
* Interactive discussion under articles

### Additional Functionalities

* Search posts
* Featured post banner on homepage
* Dynamic rendering from database
* Clean UI layout

---

## 🛠 Tech Stack

* Python
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite

---

## 📂 Project Structure (Simplified)

```
django-blog/
│
├── about/            # Static/about pages
├── blog_main/        # Main project configuration (settings, urls, wsgi)
├── blogs/            # Blog app (posts, comments, homepage)
├── dashboard/        # Admin dashboard & management panel
├── follow_us/        # Extra pages / contact section
├── templates/        # HTML templates
├── db.sqlite3        # Development database
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```
git clone https://github.com/atanu-git-debug/django-blog.git
cd django-blog
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser

```
python manage.py createsuperuser
```

6. Run server

```
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Learning Outcomes

* Django authentication system
* Model relationships (ForeignKey & user relations)
* File & media handling
* CRUD operations in Django
* Template inheritance
* Building dashboards & structured UI

---

## 🔮 Future Improvements

* Like & bookmark posts
* Rich text editor
* REST API (Django REST Framework)
* Pagination
* User profile page

---

## 👤 Author

Atanu Maity

GitHub: [https://github.com/atanu-git-debug/django-blog](https://github.com/atanu-git-debug/django-blog)

---



