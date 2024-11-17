
# Recipe Project with Django 🍳

Welcome to the Recipe Project! This is a simple, fun web app built with Django where you can explore, create, and manage your favorite recipes. 

---

## ✨ Features

- **Create, Read, Update, Delete Recipes**: Your recipe collection, your rules!
- **Organize by Categories**: Keep things neat with categories like Breakfast, Dinner, or Desserts.
- **Image Uploads**: A picture’s worth a thousand words, so show off those tasty creations.
- **Search Recipes**: Looking for something specific? Just type it in.
- **User Accounts**: Sign up and log in to manage your own recipe stash.

---

## 🚀 Getting Started

### What You’ll Need:
- **Python** (version 3.8 or newer)
- **pip** (comes with Python)
- **A Virtual Environment** (optional, but super useful)

### Installation Steps:

1. **Clone the project**:
   ```bash
   git clone https://github.com/AdarsHH30/Recipe-Project-with-Django.git
   cd Recipe-Project-with-Django
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Run the app**:
   ```bash
   python manage.py runserver
   ```

6. **Enjoy!**  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your favorite browser.

---

## 🗂 Project Overview

Here’s what you’ll find in the project:

- **`recipes/`**: This is where the magic happens – models, views, and templates for handling recipes.
- **`static/`**: Your CSS, JavaScript, and images go here.
- **`templates/`**: The HTML templates that make things look good.
- **`manage.py`**: The Django command center.

---

## 🛠 Built With

- **Django**: The heart of the app.
- **Django Rest Framework**: For building APIs (future-proofing).
- **Pillow**: For handling recipe images.

---

## 💌 Contact

Questions, suggestions, or just want to say hi? Drop a line to [AdarsHH30](https://github.com/AdarsHH30).

---

Happy cooking! 🥗🍰🍝