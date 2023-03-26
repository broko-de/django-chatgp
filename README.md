# Proyecto django-chatgp

Este es un proyecto de software desarrollado en python 🐍 por medio del framework Django 🦄.  Con el se busca integrar OpenIA ChatGPT 3

### Instalacion
Para poder hacer uso del proyecto primero necesitas crear una cuenta como desarrollador en https://platform.openai.com/docs/api-reference/introduction. Para poder correr el proyecto, vas a tener que seguir los siguientes pasos (para sistema operativo Windows):

1. Clonar el repositorio del repositorio
```
git clone https://github.com/broko-de/django-chatgp.git
```
2. Crear un entorno virtual para el proyecto y activarlo
```
python -m venv env
env/Script/activate
```
3. Instalar las dependencias del proyecto
```
cd djangoGPT
pip install -r requirements.txt
```
4. Crear un archivo .env en el directorio djangoGPT a la misma altura del archivo settings.py y completar con los datos de configuración segun lo indica .env.example
5. Por último, correr el servidor de desarrollo que provee Django
```
python manage.py runserver
```
