
# IT Project Instructions

## Prerequisites

### Install Latest Git
Download and install Git from: https://git-scm.com/download

### Install Latest Python
Download and install Python from: https://www.python.org/downloads/

---

# Steps to Follow

## Open a Terminal
- **Windows:** Use `cmd`
- **Linux/MacOS:** Use `shell`

## Enter the Following Commands
```bash
mkdir itproject
cd itproject
git clone https://github.com/the-darklord/IT-Project.git
cd IT-Project
pip install virtualenv
virtualenv django-env
```

### For Windows:
```bash
cd django-env/Scripts
activate
cd ../..
```

### For Linux/MacOS:
```bash
cd django-env/bin
source activate
cd ../..
```

### For All:
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py clearsessions
python manage.py runserver
```

## Open a Web Browser and Enter:
```
http://localhost:8000
```
