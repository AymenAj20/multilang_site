# Multilang Site

Ce projet est une application Django simple et multilingue permettant de gérer des articles de blog, de rechercher des articles et d'intégrer un chatbot basé sur l'API GPT-3 d'OpenAI.

## Prérequis

Assurez-vous d'avoir installé les logiciels suivants sur votre machine :

- Python 3.x
- pip
- virtualenv

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/multilang_site.git
    cd multilang_site
    ```

2. Créez et activez un environnement virtuel :

    ```bash
    virtualenv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3. Installez les dépendances nécessaires :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :

    Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :

    ```dotenv
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. Appliquez les migrations de la base de données :

    ```bash
    python manage.py migrate
    ```

6. Créez un superutilisateur pour accéder à l'admin Django :

    ```bash
    python manage.py createsuperuser
    ```

7. Démarrez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

8. Accédez à l'application dans votre navigateur :

    ```
    http://127.0.0.1:8000/api   
    ```

## Utilisation

### Affichage des Articles

Pour afficher la liste des articles, accédez à la page principale. Les articles par défaut sont affichés avec leurs titres, contenus et dates de publication.

### Changer la Langue

Pour changer la langue de l'interface, utilisez les boutons disponibles en bas de la page principale pour basculer entre les langues (Français et Anglais).

### Fonctionnalité de Recherche

Utilisez la barre de recherche pour rechercher des articles par contenu. Les résultats affichés incluent les articles correspondants ainsi que les résultats augmentés par le modèle GPT-3.

### Chatbot

Accédez à la page du chatbot pour poser des questions et obtenir des réponses générées par l'API GPT-3 d'OpenAI.

## Dépendances

Les dépendances du projet sont listées dans le fichier `requirements.txt`. Pour les installer, exécutez :

```bash
pip install -r requirements.txt
