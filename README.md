```markdown
# SmartEnergySystem

Ce README explique en détail comment fonctionne le projet SmartEnergySystem, ce qu'il contient, et comment le construire/configurer/exécuter. Ce projet a été réalisé en collaboration avec https://github.com/Burden19 .

Résumé rapide
------------
SmartEnergySystem est un projet Java (Maven) visant à gérer ou simuler des composants d'un système énergétique intelligent. Le projet s'appuie sur la messagerie JMS (ActiveMQ) pour l'échange d'informations entre composants. Le projet cible Java 1.8 et utilise SLF4J pour le logging.

Informations extraites du projet
-------------------------------
- groupId : `com.smartenergy`  
- artifactId : `SmartEnergySystem`  
- version : `1.0-SNAPSHOT`  
- Java : 1.8 (source/target)  
- Dépendances principales :
  - `org.apache.activemq:activemq-all:5.15.13` (JMS / ActiveMQ)
  - `org.slf4j:slf4j-api:1.7.36`
  - `org.slf4j:slf4j-simple:1.7.36`
- Plugin d'exécution Maven :
  - `org.codehaus.mojo:exec-maven-plugin` avec `mainClass` configuré sur `controller.ControllerMain`
- Structure de code repérée :
  - `src/main/` (code Java et ressources attendus)
  - `src/python/` (scripts Python; probablement utilitaires/tests/simulations)
  - fichiers IDE et `.gitignore` présents

Architecture et fonctionnement (vue générale)
--------------------------------------------
La description suivante est une vue d'ensemble basée sur la configuration et les conventions observées dans le dépôt. Pour les détails précis, consultez les sources Java dans `src/main/java` et les scripts dans `src/python`.

1. Composants principaux
   - Controller : Le point d'entrée principal identifié est `controller.ControllerMain`. Il s'agit probablement du composant qui orchestre le système, démarre les services nécessaires (connecteurs JMS, RMI, etc.) et coordonne les agents ou capteurs simulés.
   - Agents / Capteurs (attendus) : Le dépôt devrait contenir des classes représentant des entités du système (agents, capteurs, consommateurs/ producteurs d'énergie). Ces composants communiquent via des messages (JMS) ou via d'autres mécanismes (RMI/CORBA si utilisés).
   - Broker JMS : ActiveMQ est référencé comme mécanisme de messagerie. Les composants publient/consomment des messages sur des queues/topics pour l'échange d'événements et de commandes.

2. Communications
   - JMS (ActiveMQ) : Principal moyen de communication asynchrone. ActiveMQ peut être lancé localement (standalone ou via Docker) et le code se connectera au broker pour envoyer/recevoir des messages.
     - Port par défaut d'ActiveMQ : 61616 (TCP). Vérifiez la configuration dans le code/source pour voir si un port/URL spécifique est utilisé.
   - RMI / CORBA : Le `pom.xml` contient des commentaires indiquant que RMI (inclus en Java) et CORBA (présent dans JDK 8) sont envisagés/compatibles. Si le projet utilise ces mécanismes, attendez-vous à :
     - RMI : registre RMI (port par défaut 1099) et interfaces distantes.
     - CORBA : ORB intégré de Java 8 si utilisé.
   - Logging : SLF4J avec l'implémentation simple (`slf4j-simple`) est inclus — le logging utilisera la SimpleLogger par défaut (niveau configurable via propriétés système ou variables d'environnement SLF4J_SIMPLE).

3. Scripts Python
   - Le dossier `src/python/` suggère la présence de scripts utilitaires (ex. clients de simulation, générateurs d'événements, outils d'analyse). Inspectez ces fichiers pour savoir comment simuler des capteurs ou interagir avec l'application Java.

Comment construire et exécuter
-----------------------------
Prérequis :
- Java JDK 8 (ou la version spécifiée dans `pom.xml`)
- Maven 3.x
- Git pour cloner le dépôt
- (Optionnel mais recommandé) ActiveMQ broker pour la messagerie

Étapes typiques :

1. Cloner le dépôt
   git clone https://github.com/dvli999/SmartEnergySystem.git
   cd SmartEnergySystem


2. Compiler et empaqueter
   mvn clean package

   Après compilation, l'artifact JAR se trouvera dans `target/` (vérifiez le `artifactId` et la `version` dans `pom.xml` pour le nom exact).

3. Lancer l'application
   - Exécuter via Maven exec plugin (déjà configuré) :
     mvn exec:java
     (Le `pom.xml` a `mainClass` = `controller.ControllerMain`, donc `mvn exec:java` invoquera cette classe.)
   - Ou exécuter le JAR :
     java -jar target/SmartEnergySystem-1.0-SNAPSHOT.jar
     (Adaptez le nom du jar si nécessaire.)

4. Interagir
   - Vérifiez les logs en sortie console (SLF4J SimpleLogger) pour confirmer la connexion au broker et l'initialisation des composants.
   - Pour tester, exécutez éventuellement les scripts Python dans `src/python/` qui simulent des messages/événements destinés au broker.

Configuration et paramètres
--------------------------
- Vérifiez dans le code et les fichiers de ressources (ex. `src/main/resources`) s'il existe des fichiers de configuration (`.properties` / `.yaml`) pour :
  - URL/host et port du broker JMS (ActiveMQ)
  - Noms de queues/topics utilisés
  - Paramètres RMI/CORBA s'ils sont présents
  - Paramètres de logging (niveau, format) pour SLF4J SimpleLogger — variables utiles : `org.slf4j.simpleLogger.defaultLogLevel` etc.

- Variables d'environnement courantes à vérifier / définir :
  - BROKER_URL: ex. `tcp://localhost:61616`
  - RMI_REGISTRY_PORT: ex. `1099`

Tests
-----
- Exécuter les tests (si présents) :
  mvn test
- Explorez `src/test/` pour comprendre la couverture et les scénarios de tests.

Dépannage courant
-----------------
- Erreur de connexion JMS : assurez-vous qu'ActiveMQ est démarré et que l'URL/port correspondent à la configuration du code.
- Erreur de classe principale ou NoClassDefFoundError : vérifiez que le packaging a inclus toutes les dépendances ou exécutez via `mvn exec:java`.
- Logging inexistant : SLF4J SimpleLogger est inclus — contrôlez les variables d'environnement ou les propriétés système pour régler le niveau de log.

----------
1. Forkez le dépôt.
2. Créez une branche : `git checkout -b feat/ma-fonctionnalite`.
3. Ajoutez/committez vos changements.
4. Exécutez les tests et la compilation : `mvn clean package && mvn test`.
5. Ouvrez une Pull Request décrivant vos modifications.

-------
Pour toute question ou demande d'amélioration, ouvrez une issue dans le dépôt GitHub : https://github.com/dvli999/SmartEnergySystem/issues

```
