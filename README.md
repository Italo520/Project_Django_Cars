🔗 Este documento também está disponível em [Português](./README.pt-br.md).

# Project Django Cars

This is a Django web application for managing a catalog of cars. It allows users to view a list of available cars, search for specific models, and add new cars to the system. The project also includes an admin interface for more detailed management of car brands and individual car entries.

## Features

* **Car Listings:** View all cars in a grid layout, showing a photo, brand, model, factory year, and price.
* **Add New Car:** A form to add new cars to the catalog, including details like model, brand, factory year, model year, plate, value, and a photo.
* **Search Functionality:** Users can search for cars by model name.
* **Brand Management:** Cars are associated with specific brands. Brands can be managed through the Django admin interface.
* **Image Uploads:** Each car entry can have an associated photo.
* **Admin Panel:** The Django admin interface is configured for managing `Car` and `Brand` models, with custom list displays and search fields.
* **Custom Validations:**
    * The minimum value for a car is R$20,000.
    * The factory year of a car cannot be earlier than 1975.

## Project Structure

Project_Django_Cars  
├── app/  
│   ├── settings.py  
│   ├── urls.py  
│   ├── asgi.py  
│   ├── wsgi.py  
│   └── templates/  
│       └── base.html  
├── cars/  
│   ├── models.py  
│   ├── views.py  
│   ├── forms.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── templates/  
│   │   ├── cars.html  
│   │   └── new_car.html  
│   └── migrations/  
├── manage.py  
├── media/  
└── db.sqlite3  

## Prerequisites

* Python (3.12.10 recommended)
* Django ( 5.2.1 recommended)  
* Pillow (for ImageField handling)

## Setup and Installation

1.  **Clone the repository (or download the files):**
    ```bash
    # If it were a git repository
    # git clone <repository-url>
    # cd Project_Django_Cars-e6def20114e3ef975df51d68a9d4b215b36c15e5
    ```
    Navigate to the `Project_Django_Cars-e6def20114e3ef975df51d68a9d4b215b36c15e5` directory.

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install Django==5.2.1 Pillow
    ```

4.  **Apply migrations:**
    This will create the necessary database tables based on the models.
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    Follow the prompts to create an administrator account.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Ensure the `media` directory exists:**
    The `settings.py` defines `MEDIA_ROOT` as `os.path.join(BASE_DIR,'media')`. Make sure a directory named `media` exists at the same level as your `manage.py` file. If not, create it.

## Running the Project

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the application in your web browser:**
    * **Car Listings:** [http://127.0.0.1:8000/cars/](http://127.0.0.1:8000/cars/)
    * **Add New Car:** [http://127.0.0.1:8000/new_car/](http://127.0.0.1:8000/new_car/)
    * **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (Log in with the superuser credentials)

## Key Configuration Points (from `app/settings.py`)

* **`DEBUG = True`**: The application is currently running in debug mode.
* **`INSTALLED_APPS`**: Includes `'django.contrib.admin'`, `'django.contrib.auth'`, `'django.contrib.contenttypes'`, `'django.contrib.sessions'`, `'django.contrib.messages'`, `'django.contrib.staticfiles'`, and the custom app `'cars'`.
* **`DATABASES`**: Configured to use SQLite (`'ENGINE': 'django.db.backends.sqlite3'`) with the database file `db.sqlite3` located in `BASE_DIR`.
* **`TEMPLATES`**: The main template directory is set to `['app/templates']`.
* **`MEDIA_ROOT`**: Set to `os.path.join(BASE_DIR,'media')`. This is where uploaded files (car photos) will be stored.
* **`MEDIA_URL`**: Set to `'/media/'`. This is the URL prefix for accessing media files.
