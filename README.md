# OpenClassrooms: Projet 10 - Créez une API sécurisée RESTful en utilisant Django REST.

Ce programme a été développé dans le cadre du projet 11 d'OpenClassrooms. 


![Projet 10 OpenClassrooms Güdlft](.readme/landry_anthony_P10_softdesk_openclassrooms_developpeur_application_python.png)

## 🔹 Installation

Pour commencer, assurez-vous d'avoir Python installé sur votre système.

Ensuite, suivez ces étapes pour installer et exécuter le programme :

- [x] 1. Clonez ce dépôt dans le répertoire de votre choix en utilisant la commande suivante :
    
    ```bash
    git clone https://github.com/Anthony-landry/P10-SoftDesk.git
    ```
    
- [x] 2. Accédez au dossier P4-ChessTournaments.
    
- [x] 3. Créez un nouvel environnement virtuel en utilisant la commande suivante :
    
    ```bash
    python -m venv env
    ```
    
- [x] 4. Activez l'environnement virtuel :
    
    * Sur Windows :
        
        ```bash
        env\Scripts\activate.bat
        ```
        
    * Sur Linux :
        
        ```bash
        source env/bin/activate
        ```
        
- [x] 5. Installez les packages requis en exécutant la commande suivante :
    
    ```bash
    pip install -r requirements.txt
    ```
    
- [x] 6. Faire les migrations :
    
    ```bash
    python manage.py migrate
    ```

- [x] 7. Si la database est vide créer un SuperUser pour accder à la partie administatrion de django :
    
    ```bash
    python manage.py createsuperuser
    ```

    Pour changer le password administateur :
    ```bash
    python manage.py changepassword admin
    ```

- [x] 8.Remplir le fichier .env :

un fichier .env ce trouve à la racine du pojet

```bash
.env
SECRET_KEY='METTRE VOTRE CLE SECRET'
SIGNING_KEY='METTRE VOTRE CLE SECRET'
DEBUG='True'
ALGORITHM="HS256"
```

    par défaut id : admin / password : Abcd.1234!

- [x] 9. Lancer le serveur :
    
    ```bash
    python manage.py runserver 
    ```


# Liste des points de terminaison de l'API :

Une collection postman vous est proposé avec tout les points de terminaison de API.

Fichier nommé : **Postman_collection_P10_OCR_API_SoftDesk.json** à ouvrir avec postman.


| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL (base: http://127.0.0.1:8000/api)*   |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscrire un utilisateur    	                                          | POST           | /account/signup/                          |
| 2   | Récupérer un token pour la connexion d'un utilisateur                     | POST           | /token/                                   |
| 3   | Créer un projet 		                                          | POST           | /projet/		                       |
| 4   | Lister les projets 				     	                  | GET            | /projet/               	               |
| 5   | Récupérer un projet via son id			                          | GET            | /projet/{id}  			       |
| 6   | Modifier un projet via son id 		                                  | PUT            | /projet/{id}/                  	       |
| 7   | Supprimer un projet via son id	                                          | DELETE 	   | /projet/{id}/               	       |
| 8   | Créer un collaborateur			                                  | POST           | /account/contributors/		       |
| 9   | Lister les collaborateurs						  | GET            | /account/contributors/		       |
| 10  | Récupérer un collaborateur via son id                     	          | GET            | /account/contributors/{id}/	       |
| 11  | Supprimer un collaborateur via son id                                     | DELETE         | /account/contributors/{id}/	       |
| 12  | Créer un problème 		                                          | POST           | /issue/		                       |
| 13  | Lister les problèmes 				     	                  | GET            | /issue/               	               |
| 14  | Récupérer un problème via son id		                          | GET            | /issue/{id}  		               |
| 15  | Modifier un problème via son id		                                  | PUT            | /issue/{id}/               	       |
| 16  | Supprimer un problème via son id                                          | DELETE         | /issue/{id}/               	       |
| 17  | Créer un commentaire			                                  | POST           | /comment/				       |
| 18  | Lister les commentaires							  | GET            | /comment/				       |
| 19  | Récupérer un commentaire via son id                     	          | GET            | /comment/{id}/			       |
| 20  | Modifier un commentaire via son id                                        | PUT            | /comment/{id}/			       |
| 21  | Supprimer un commentaire via son id                                       | DELETE         | /comment/{id}/			       |

# RPGD

- Utilisateur : droit à l’acces et la la rectification.
-  Utilisateur : Droit a l’oubli; utlisateur doit pouvoir supprimer ses données personnelles, sans trace.
- Utilisateur : le consentement pour etre contacter ou pas et partager ses données personnelles.
- Utilisateur : l’age légal 15ans pour valider l’inscritption.


# OWASP

- utiliser PiPenv pour contenir les failles de sécurité et rester à jour.
- utilisation de JWT :  Il permet l’échange sécurisé de jetons (tokens) entre plusieurs parties. Cette sécurité de l’échange se traduit par la vérification de l’intégrité et de l’authenticité des données
- Les acces ncessute des autorisations spéciales. 

# Green code

- L’application est pensé et structuré en considération des enjeux énergétiques.
- Pagination des ressources: pour éviter que le serveur surchauffe.
