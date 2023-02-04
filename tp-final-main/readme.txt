Etapes et commandes à réaliser pour initialiser un projet

- Se placer dans le répertoire où l'on souhaite créer notre projet
- Créer un répertoire du nom de notre projet avec : mkdir myproject
- Se placer dedans avec : cd myproject
- Créer un environnement virtuel avec : python -m venv .venv
- Activer l'environnement virtuel avec : .\.venv\Scripts\activate (sous Windows) ou source .venv/bin/activate (sous Mac)
- Installer la bibliothèque Django avec : pip install django
- Initialiser notre projet en créant un dossier project qui contiendra la configuration 
de notre projet avec : django-admin startproject project . (n'oublier pas le .)
- Appliquer les migrations initiales avec : python manage.py migrate
- Lancer le serveur avec : python manage.py runserver
- Arrêter le serveur avec : Ctrl+C (sous Windows) ou Cmd+C (sous Mac) 
- Initialiser une application avec : python manage.py startapp myapp
- Modifier le fichier settings.py du dossier project pour faire apparaitre l'application dans INSTALLED_APPS 
en faisant référence à la classe MyappConfig du fichier apps.py de l'application : 'myapp.apps.MyappConfig'
