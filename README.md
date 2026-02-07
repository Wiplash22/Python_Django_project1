# Python Django Projects

This repository contains two Django projects developed for learning and demonstration purposes.

## Projects

### 1. Project 1 (`project1`)
A fundamental Django project that demonstrates basic view rendering and template context usage.

**Features:**
- **Hello App**: Displays a list of movies using a static dictionary passed from the view to the template.
- **Simple Rendering**: Shows how to render HTML templates with dynamic data.

**Setup:**
1. Navigate to the `project1` directory:
   ```bash
   cd project1
   ```
2. Install Django (if not already installed):
   ```bash
   pip install django
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Access the app at `http://127.0.0.1:8000/hello/` (check `urls.py` for exact route if different).

---

### 2. Movie Manager (`movie_manager`)
A more advanced CRUD (Create, Read, Update, Delete) application for managing movie records.

**Features:**
- **Create**: Add new movies with details and poster images.
- **Read**: List all movies available in the database.
- **Update**: Edit existing movie details.
- **Delete**: Remove movies from the database.
- **Visit Counter**: Uses cookies to track the number of visits to the list page.
- **PostgreSQL**: Configured to use PostgreSQL as the backend database.

**Prerequisites:**
- **PostgreSQL**: You need to have PostgreSQL installed and running.
- **Database**: Create a database named `movies_db`.
- **User/Password**: The settings are configured for user `postgres` and password `1234`. You may need to update `movie_manager/settings.py` to match your local PostgreSQL credentials.

**Setup:**
1. Navigate to the `movie_manager` directory:
   ```bash
   cd movie_manager
   ```
2. Install Django and psycopg2 (for PostgreSQL):
   ```bash
   pip install django psycopg2
   ```
3. Apply migrations to create database tables:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the app to manage movies.

## Virtual Environment

It is recommended to use a virtual environment for managing dependencies.

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate
```
