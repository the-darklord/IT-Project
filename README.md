<h1>
  IT Project Instructions
</h1>

<h2>
  Prerequisuites : 
</h2>
<br>
<h4> Install Latest Git </h4>

```bash
https://git-scm.com/download
```

<h4> Install Latest Python </h4>

```bash
https://www.python.org/downloads/
```

<br> <br>
<hr>
<h1>
  Steps to Follow : 
</h1>
<br>
<h4> Open a Terminal </h4>
cmd in Windows

shell in Linux/MacOS
<h4> Enter the Following </h4>

```bash
mkdir itproject
cd itproject
git clone https://github.com/the-darklord/IT-Project.git
cd IT-Project
pip install virtualenv
virtualenv django-env
```

For Windows :
```bash
cd django-env/Scripts
activate
cd ../..
```

For Linux/MacOS
```bash
cd django-env/bin
source activate
cd ../..
```

For All
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py clearsessions
python manage.py runserver
```
Open a Web Browser and Enter the following :
```bash
http://localhost:8000
```
