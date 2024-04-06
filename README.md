# Connect

## Installation

Docker is required to run this project. If you don't have docker installed, you can download it from [here](https://www.docker.com/products/docker-desktop)

### Steps

1) Clone this repo
    ```bash
    git clone https://github.com/rohittp0/guider.git
    ```
2) Create a venv and activate it
    - Linux / MacOs
    ```bash
   python3 -m venv venv
   ./venv/bin/activate
   ```
   - Windows
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```
3) Install dependencies
    ```bash
   pip install -r requirements.txt
    ```
4) Rename the .env.example to .env and edit the values in it
5) Set up the database
    ```bash
   docker compose up -d
    ```
6) Apply migrations
    ```bash
   python manage.py migrate
   ```
7) Enable sign in with Google
    ```bash
    python manage.py createsocial
    ```
8) Create an admin user account ( Optional )
    ```bash
   python manage.py createsuperuser
   ```
   
That's it, now you should be able to start Connect by running,
```bash
python manage.py runserver
```

Open http://localhost:8000 in your browser
