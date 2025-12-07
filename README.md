# SmartEnergySystem

> **Projet de Collaboration**  
> Ce projet a été développé en collaboration avec [Ahmed Mbarek](https://github.com/Burden19)

## 📋 Table des Matières
- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Stack Technologique](#stack-technologique)
- [Architecture du Système](#architecture-du-système)
- [Structure du Projet](#structure-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Lancement de l'Application](#lancement-de-lapplication)
- [Utilisation](#utilisation)
- [Modules du Système](#modules-du-système)
- [Intégration Python](#intégration-python)
- [API et Endpoints](#api-et-endpoints)
- [Tests](#tests)
- [Dépannage](#dépannage)
- [Contribution](#contribution)
- [Licence](#licence)

## 🏠 Aperçu

SmartEnergySystem est un système intelligent de gestion énergétique développé en Java, conçu pour optimiser la consommation et la production d'énergie dans les environnements domestiques et commerciaux. Le système intègre des algorithmes d'intelligence artificielle pour fournir des analyses prédictives et des recommandations d'optimisation énergétique en temps réel.

## ✨ Fonctionnalités

### Gestion Énergétique
- **Monitoring en Temps Réel** : Surveillance continue de la consommation et production énergétique
- **Analyse Prédictive** : Prévision de la consommation future basée sur l'historique et les patterns
- **Optimisation Automatique** : Suggestions intelligentes pour réduire les coûts énergétiques
- **Alertes et Notifications** : Système d'alerte pour consommation anormale ou pannes

### Gestion des Appareils
- **Contrôle Centralisé** : Interface unique pour gérer tous les appareils connectés
- **Planification Intelligente** : Programmation automatique basée sur les tarifs énergétiques
- **Profils d'Utilisation** : Création de profils personnalisés pour différents scénarios

### Analyse et Rapports
- **Tableaux de Bord Interactifs** : Visualisation graphique des données énergétiques
- **Rapports Détaillés** : Génération de rapports de consommation périodiques
- **Comparaisons Historiques** : Analyse des tendances sur différentes périodes
- **Calcul des Économies** : Estimation des économies réalisées grâce aux optimisations

## 🛠 Stack Technologique

### Backend Principal
- **Java** (92.6%) - Cœur du système
  - Spring Boot - Framework principal
  - Spring Data JPA - Gestion des données
  - Hibernate - ORM (Object-Relational Mapping)
  - Maven - Gestion des dépendances

### Intelligence Artificielle
- **Python** (7.4%) - Modules d'analyse et ML
  - NumPy - Calculs numériques
  - Pandas - Manipulation de données
  - Scikit-learn - Algorithmes de machine learning
  - TensorFlow/PyTorch - Deep learning (si applicable)

### Base de Données
- H2 Database (Développement)
- PostgreSQL/MySQL (Production)

### Outils de Développement
- IntelliJ IDEA - IDE principal
- Git - Contrôle de version
- JUnit - Tests unitaires

## 🏗 Architecture du Système

```
┌─────────────────────────────────────────────────────────────┐
│                    Interface Utilisateur                     │
│                   (Web/Mobile/Desktop)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                      API REST Layer                          │
│                    (Controllers)                             │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    Service Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │Energy Service│  │Device Service│  │Analytics Svc │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                  Data Access Layer                           │
│                   (Repositories)                             │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    Database Layer                            │
│              (H2/PostgreSQL/MySQL)                           │
└──────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                 Python ML Module                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │Prediction    │  │Optimization  │  │Anomaly Det.  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Structure du Projet

```
SmartEnergySystem/
├── .idea/                          # Configuration IntelliJ IDEA
│   ├── compiler.xml
│   ├── misc.xml
│   └── workspace.xml
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/smartenergy/
│   │   │       ├── config/         # Configuration Spring
│   │   │       ├── controller/     # REST Controllers
│   │   │       ├── model/          # Entités JPA
│   │   │       ├── repository/     # Repositories
│   │   │       ├── service/        # Logique métier
│   │   │       ├── dto/            # Data Transfer Objects
│   │   │       ├── exception/      # Gestion des exceptions
│   │   │       ├── util/           # Utilitaires
│   │   │       └── Application.java # Point d'entrée
│   │   │
│   │   ├── resources/
│   │   │   ├── application.properties  # Configuration
│   │   │   ├── application-dev.properties
│   │   │   ├── application-prod.properties
│   │   │   ├── static/             # Ressources statiques
│   │   │   └── templates/          # Templates (si applicable)
│   │   │
│   │   └── python/                 # Scripts Python
│   │       ├── predictor.py        # Prédiction énergétique
│   │       ├── optimizer.py        # Optimisation
│   │       ├── analyzer.py         # Analyse de données
│   │       └── requirements.txt    # Dépendances Python
│   │
│   └── test/
│       └── java/                   # Tests unitaires et d'intégration
│           └── com/smartenergy/
│               ├── controller/
│               ├── service/
│               └── repository/
│
├── pom.xml                         # Configuration Maven
├── .gitignore                      # Fichiers ignorés par Git
└── README.md                       # Ce fichier
```

## 📋 Prérequis

Avant d'installer et d'exécuter le système, assurez-vous d'avoir :

### Obligatoire
- **JDK 11 ou supérieur** - Java Development Kit
- **Maven 3.6+** - Outil de build
- **Python 3.8+** - Pour les modules d'IA

### Recommandé
- **IntelliJ IDEA** - IDE pour le développement
- **Postman** - Pour tester les API
- **Git** - Contrôle de version

### Optionnel (Production)
- **PostgreSQL 12+** ou **MySQL 8+**
- **Docker** - Pour la conteneurisation
- **Nginx** - Serveur web reverse proxy

## 🚀 Installation

### 1. Cloner le Dépôt

```bash
git clone https://github.com/dvli999/SmartEnergySystem.git
cd SmartEnergySystem
```

### 2. Installer les Dépendances Java

```bash
mvn clean install
```

Cette commande va :
- Télécharger toutes les dépendances Maven
- Compiler le code source
- Exécuter les tests
- Créer le fichier JAR exécutable

### 3. Installer les Dépendances Python

```bash
cd src/main/python
pip install -r requirements.txt
cd ../../..
```

Ou avec un environnement virtuel (recommandé) :

```bash
cd src/main/python
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ../../..
```

### 4. Configuration de la Base de Données

#### Option A : H2 (Développement - Par défaut)
Aucune configuration supplémentaire nécessaire. La base de données sera créée automatiquement.

#### Option B : PostgreSQL (Production)

1. Créer la base de données :
```sql
CREATE DATABASE smartenergy_db;
CREATE USER smartenergy_user WITH PASSWORD 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE smartenergy_db TO smartenergy_user;
```

2. Modifier `application-prod.properties` :
```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/smartenergy_db
spring.datasource.username=smartenergy_user
spring.datasource.password=votre_mot_de_passe
spring.jpa.hibernate.ddl-auto=update
```

## ⚙️ Configuration

### Fichier application.properties

```properties
# Configuration du serveur
server.port=8080
server.servlet.context-path=/api

# Configuration de la base de données H2 (Développement)
spring.datasource.url=jdbc:h2:file:./data/smartenergy
spring.datasource.driver-class-name=org.h2.Driver
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

# Configuration JPA
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Configuration du logging
logging.level.root=INFO
logging.level.com.smartenergy=DEBUG
logging.file.name=logs/smartenergy.log

# Configuration Python
python.script.path=src/main/python
python.executable=python3

# Configuration de l'analyse énergétique
energy.analysis.interval=300000  # 5 minutes en ms
energy.threshold.high=5000       # Watts
energy.threshold.low=100         # Watts
```

## ▶️ Lancement de l'Application

### Mode Développement

```bash
mvn spring-boot:run
```

Ou :

```bash
mvn clean package
java -jar target/SmartEnergySystem-1.0.0.jar
```

### Mode Production

```bash
java -jar target/SmartEnergySystem-1.0.0.jar --spring.profiles.active=prod
```

### Avec Docker (Optionnel)

```bash
docker build -t smartenergy-system .
docker run -p 8080:8080 smartenergy-system
```

### Vérification du Lancement

L'application sera accessible sur :
- **API REST** : http://localhost:8080/api
- **Console H2** : http://localhost:8080/h2-console
- **Swagger UI** : http://localhost:8080/swagger-ui.html (si configuré)

## 📱 Utilisation

### Endpoints Principaux

#### Gestion de l'Énergie
```bash
# Obtenir la consommation actuelle
GET /api/energy/current

# Obtenir l'historique de consommation
GET /api/energy/history?startDate=2024-01-01&endDate=2024-12-31

# Obtenir les prédictions
GET /api/energy/predictions?horizon=24

# Obtenir les statistiques
GET /api/energy/statistics
```

#### Gestion des Appareils
```bash
# Lister tous les appareils
GET /api/devices

# Ajouter un appareil
POST /api/devices
Content-Type: application/json
{
  "name": "Climatiseur Salon",
  "type": "AC",
  "power": 2000,
  "location": "Salon"
}

# Mettre à jour un appareil
PUT /api/devices/{id}

# Supprimer un appareil
DELETE /api/devices/{id}

# Contrôler un appareil
POST /api/devices/{id}/control
{
  "action": "ON",
  "schedule": "2024-12-07T14:00:00"
}
```

#### Analyses et Rapports
```bash
# Générer un rapport
GET /api/reports/generate?period=monthly&format=pdf

# Obtenir les économies réalisées
GET /api/analytics/savings

# Détection d'anomalies
GET /api/analytics/anomalies
```

## 🔧 Modules du Système

### 1. Module de Collecte de Données (Data Collection)
- Collecte en temps réel des données de consommation
- Intégration avec les compteurs intelligents
- Agrégation et validation des données

### 2. Module d'Analyse (Analytics)
- Calcul des statistiques de consommation
- Identification des patterns d'utilisation
- Comparaisons historiques

### 3. Module de Prédiction (Prediction)
- Algorithmes de machine learning pour prédire la consommation
- Modèles basés sur l'historique et les facteurs externes
- Ajustement automatique des modèles

### 4. Module d'Optimisation (Optimization)
- Recommandations pour réduire la consommation
- Planification intelligente des appareils
- Optimisation basée sur les tarifs énergétiques

### 5. Module de Notification (Notification)
- Alertes en cas de consommation anormale
- Notifications de maintenance
- Rapports périodiques automatiques

## 🐍 Intégration Python

### Communication Java-Python

Le système utilise plusieurs méthodes pour intégrer Python :

1. **Process Execution** : Exécution de scripts Python via Runtime
2. **REST API** : Service Python exposant des endpoints
3. **Py4J** : Bridge direct Java-Python (si implémenté)

### Scripts Python Disponibles

#### predictor.py
```python
# Prédiction de la consommation énergétique
# Utilise des modèles de time series (ARIMA, LSTM)
python predictor.py --input data.csv --horizon 24 --output predictions.json
```

#### optimizer.py
```python
# Optimisation de la consommation
# Algorithmes génétiques ou optimisation linéaire
python optimizer.py --devices devices.json --constraints constraints.json
```

#### analyzer.py
```python
# Analyse et détection d'anomalies
python analyzer.py --data consumption.csv --threshold 2.5
```

## 🧪 Tests

### Exécuter Tous les Tests

```bash
mvn test
```

### Tests Unitaires Seulement

```bash
mvn test -Dtest=*Test
```

### Tests d'Intégration

```bash
mvn verify
```

### Couverture de Code

```bash
mvn jacoco:report
```

Le rapport sera disponible dans `target/site/jacoco/index.html`

## 🔍 Dépannage

### Problèmes Courants

#### 1. Port 8080 déjà utilisé
```bash
# Modifier le port dans application.properties
server.port=8081
```

#### 2. Erreur de connexion à la base de données
```bash
# Vérifier les credentials dans application.properties
# Vérifier que le service de base de données est démarré
```

#### 3. Module Python non trouvé
```bash
# Vérifier l'installation Python
python --version
pip list

# Réinstaller les dépendances
pip install -r src/main/python/requirements.txt
```

#### 4. Erreur de compilation Maven
```bash
# Nettoyer et rebuilder
mvn clean install -U
```

### Logs

Les logs sont disponibles dans :
- Console : Sortie standard
- Fichier : `logs/smartenergy.log`

Pour augmenter le niveau de détail :
```properties
logging.level.com.smartenergy=DEBUG
```

## 📊 Surveillance et Monitoring

### Actuator Endpoints (si Spring Boot Actuator est activé)

```bash
# Health check
GET /actuator/health

# Metrics
GET /actuator/metrics

# Info
GET /actuator/info
```

## 🚀 Déploiement

### Build pour Production

```bash
mvn clean package -P prod
```

### Déploiement avec Docker

```dockerfile
# Dockerfile
FROM openjdk:11-jre-slim
COPY target/SmartEnergySystem-1.0.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

```bash
docker build -t smartenergy:latest .
docker run -d -p 8080:8080 --name smartenergy smartenergy:latest
```

### Variables d'Environnement

```bash
export DB_URL=jdbc:postgresql://localhost:5432/smartenergy_db
export DB_USERNAME=smartenergy_user
export DB_PASSWORD=votre_mot_de_passe
export PYTHON_PATH=/usr/bin/python3
```

## 🔒 Sécurité

### Recommandations

- Utiliser HTTPS en production
- Implémenter l'authentification JWT
- Chiffrer les données sensibles
- Mettre à jour régulièrement les dépendances
- Utiliser des variables d'environnement pour les secrets

### Authentification (si implémenté)

```bash
# Login
POST /api/auth/login
{
  "username": "user@example.com",
  "password": "password"
}

# Utiliser le token dans les requêtes
Authorization: Bearer <token>
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Suivez ces étapes :

### Workflow de Contribution

1. **Fork** le dépôt
2. **Créer** une branche de fonctionnalité
   ```bash
   git checkout -b feature/NouvelleFonctionnalite
   ```
3. **Commiter** vos changements
   ```bash
   git commit -m 'Ajout d'une nouvelle fonctionnalité'
   ```
4. **Pousser** vers la branche
   ```bash
   git push origin feature/NouvelleFonctionnalite
   ```
5. **Ouvrir** une Pull Request

### Standards de Code

- Suivre les conventions Java standard
- Commenter le code complexe
- Écrire des tests pour les nouvelles fonctionnalités
- Utiliser des noms de variables descriptifs
- Respecter le style de code existant

### Commits

Format recommandé :
```
type(scope): description courte

Description détaillée si nécessaire

Fixes #123
```

Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 📝 Licence

Ce projet est open source. Consultez le fichier LICENSE pour plus de détails.

## 👥 Auteurs et Contributeurs

### Développeurs Principaux
- **Mohamed Ali Thabet** - [Profil GitHub](https://github.com/dvli999)
- **Ahmed Mbarek** - [Profil GitHub](https://github.com/Burden19)

### Remerciements
Merci à tous les contributeurs qui ont participé à ce projet.

## 📧 Contact et Support

### Obtenir de l'Aide
- **Issues GitHub** : [Ouvrir une issue](https://github.com/dvli999/SmartEnergySystem/issues)
- **Documentation** : Consultez le wiki du projet
- **Email** : contact@smartenergy.example.com (si applicable)

### Signaler un Bug
Utilisez le template d'issue GitHub avec :
- Description du problème
- Étapes pour reproduire
- Comportement attendu vs observé
- Captures d'écran si applicable
- Environnement (OS, version Java, etc.)

## 🗺 Roadmap

### Version 2.0 (Planifiée)
- [ ] Interface web complète avec React
- [ ] Application mobile (iOS/Android)
- [ ] Intégration avec plus de fournisseurs d'énergie
- [ ] Support multi-utilisateurs
- [ ] Tableau de bord personnalisable
- [ ] Export de données avancé

### Version 1.5 (En cours)
- [ ] Amélioration des algorithmes de prédiction
- [ ] Nouvelles visualisations de données
- [ ] API GraphQL
- [ ] Support Docker Compose

## 📚 Ressources Additionnelles

### Documentation
- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Maven Documentation](https://maven.apache.org/guides/)
- [Python ML Libraries](https://scikit-learn.org/)

### Liens Utiles
- [Guide de contribution](CONTRIBUTING.md)
- [Code de conduite](CODE_OF_CONDUCT.md)
- [Changelog](CHANGELOG.md)

---

**Note** : Ce projet est conçu à des fins éducatives et de recherche. Pour une utilisation en production, veuillez vous assurer d'implémenter toutes les mesures de sécurité nécessaires et de respecter les réglementations locales en matière de gestion énergétique.

**Dernière mise à jour** : Décembre 2024
