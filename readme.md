# Blog Final - Fernando Quintela

Proyecto final del curso de Python para Coderhouse — Blog y Messenger.

# Requisitos
- Python 3.13
- Django 5.2.5
- Ver `requirements.txt` para ver las dependencias.

# Instalación (local)
```bash
git clone <TU_REPO_URL>
cd blog_final
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
