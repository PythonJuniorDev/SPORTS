# 📌 Athlete Management System
**Building my first own API!**

## 🎯 API Purpose
The API makes it possible for the gym to register the instructors and the athletes. It also provides the instructors with a personal access code. 
Further relevant information of the athlete can be stored: contact information, the contact person, group lesson, level, etc.

## 📚 API Reference
- `/athlete/` – list, create, update, delete athletes  
- `/instructor/` – same for instructors  
- `/personal access code/` – manage access codes
- `/api-auth/` – login/logout for the API

### 🧩 MODELS
- Create a FK to `Operator` in the `Garage` model  
- Create in the `Tariff` model two FKs:  
  - To the `Operator` model  
  - To the `Garage` model  
- Arguments: `default=None`, `null=True`, `on_delete=CASCADE`

### 🛠️ SERIALIZERS
- Create two `PrimaryKeyRelatedFields` in the `Operator` class:  
  - To the `Garage` class  
  - To the `Tariff` class

### 👁️ VIEWS
- Import filters from `django restframework`  
- Use filters:  
  - `SearchFilter`  
  - `OrderingFilter`

### 🔗 URLS (ROOT)
- Import `DefaultRouter` from `restframework`  
- Register the viewsets with the router

### 🧑‍💼 ADMIN
- Create a superuser via the terminal to use the admin  
- Register models to display & customize your models in the Django admin panel
