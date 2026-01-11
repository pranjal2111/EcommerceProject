 Ecommerce Website 🛒

A Django-based E-commerce web application that provides core online shopping functionalities such as product management, cart system, user authentication, and order handling.

This project is developed for learning and academic purposes, focusing on Django fundamentals and full-stack web development.

---

 ✨ Features

 👤 User Side

 User registration & login
 View all products
 View single product details
 Category-wise product listing
 Add products to cart
 Cart management
 Checkout & payment page (UI)
 View order history
 Inquiry form

 🛠️ Admin / Seller Side

 Add new products
 Edit existing products
 Manage products

---

 🧰 Tech Stack

Backend: Python, Django
Frontend: HTML, CSS, JavaScript
Database: SQLite3
Authentication: Django Auth System

---

 📁 Project Structure

EcommerceProject/
│
├── ecommerce/                # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/                     # Main application
│   ├── migrations/
│   ├── templates/
│   │   ├── addproduct.html
│   │   ├── editproduct.html
│   │   ├── manageproduct.html
│   │   ├── showproducts.html
│   │   ├── singleproducts.html
│   │   ├── cateviseproduct.html
│   │   ├── cart.html
│   │   ├── payment.html
│   │   ├── your_orders.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── inquiry.html
│   │   └── nav.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

 ⚙️ Installation & Setup

 1️⃣ Clone the Repository

git clone https://github.com/pranjal2111/EcommerceProject.git
cd EcommerceProject
```

 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

 3️⃣ Install Dependencies

pip install django
```

 4️⃣ Apply Migrations

python manage.py migrate
```

 5️⃣ Run Development Server

python manage.py runserver
```

Access the app at:

```
http://127.0.0.1:8000/
```

---
 🔐 Admin Panel

Create an admin user:

python manage.py createsuperuser
```

Admin panel URL:

```
http://127.0.0.1:8000/admin/
```

---
 📌 Notes

 Payment functionality is UI-based only (no gateway integration)
 Designed primarily for learning Django CRUD & workflows

---
 🚀 Future Improvements


 Payment gateway integration
 Order status tracking
 Product reviews & ratings
 REST API (Django REST Framework)
 Enhanced security & validations
 Deployment on cloud (AWS / Render / Railway)

---
 👨‍💻 Author

Pranjal Vejan
Final Year Computer Engineering Student
Python & Django Developer

 GitHub: pranjal2111

---

⭐ If you find this project helpful, consider giving it a star!
