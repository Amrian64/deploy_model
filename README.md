

# Start a project
<table>
    <tr>
        <td>
            <a href="start_env.md">
                Start project and environnement
            </a>
        </td>
    </tr>   
</table>

# Setup - Mise en production  :

## 1.1 Installer docker : https://docs.docker.com/get-docker/
* `docker info`

## 1.2 Installe cli GCP
* `brew install --cask google-cloud-sdk`
* Lancer dans le terminal : `/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/install.sh`
* `gcloud auth login`
* Si pas authentifié : `gcloud auth login`
* Config pour utiliser des commandes docker avec **gcp** : `gcloud auth configure-docker`

Info : https://cloud.google.com/sdk/gcloud/reference/app/open-console

## 1.3 Creer un projet dans GCP et Activer l'api container registry du projet.

## 1.4 Regler le projet gcp dans le cli
* `export PROJECT_ID=remplacer-avec-projet-id-gcloud`
* `echo $PROJECT_ID`
* `gcloud config set project $PROJECT_ID`
* Verifier que la config gcp cli est bien réglé sur votre projet : `gcloud config list`.

## 1.5 Créer un service acount:

* https://console.cloud.google.com/apis/credentials/serviceaccountkey
* Allé dans votre projet
* Clicker sur le bouton : Créer un compte de service
* Choisir le role : Propriétaire.
* Créer une clé json (en cliquant sur le nom du service acount que vous venez de créer)
* stocker le json dans un endroit sûr dans votre ordinateur.
* créer une variable d'environnement : pour stocker le path dans lequel ce trouver votre json : export `GOOGLE_APPLICATION_CREDENTIALS= ~/gcp_keys/elevated-style.json`
* Regarder les service acount lié au project_id : `gcloud iam service-accounts list`.

PS : voir si la facturation est activé : https://cloud.google.com/billing/docs/how-to/modify-project

## 1.5 Régler docker
* `export DOCKER_IMAGE_NAME=definir-le-nom-de-image-docker`
* `echo $DOCKER_IMAGE_NAME`

## 1.6 Construire l'image :
Depuis le terminal en local Creer une image docker avec la nomenclature suivante :
* `docker build -t  eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME .`
* `docker build -t eu.gcr.io/demo-elevated-style-321915/api .`

## 1.7 Tester l'image en local
* `docker run -p 8080:8000 eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME`
* exemple = `docker run -p 8080:8000 eu.gcr.io/demo-elevated-style-321915/api`

* `docker run -e PORT=8000 -p 8080:8000 eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME`
* exemple ==> http://localhost:8080/predict?pclass=1&age=22&adult_male=1&fare=100

Pour lancer un terminal dans le container : `docker run -it api sh`

## 1.8 Pusher l'image dans container registry
* `docker push eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME`

## 1.9 Deploiement de l'image `container registry` dans `google cloud run`
* `gcloud run deploy --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region europe-west1
    Si probleme d'authentification, le faire manuellement depuis l'image stocké dans container registry`


    