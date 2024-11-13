
# Password Generator (Python & PySide6)

## Description
Ce projet est une application graphique développée en Python avec `PySide6` pour générer des mots de passe sécurisés en fonction de différents critères (minuscules, majuscules, chiffres, symboles). Il permet de personnaliser la longueur du mot de passe et de choisir les types de caractères à inclure. Un bouton "Copier" facilite l'utilisation du mot de passe généré.

## Fonctionnalités
- Génération de mots de passe aléatoires avec des options de personnalisation :
    - Inclure des **lettres minuscules**
    - Inclure des **lettres majuscules**
    - Inclure des **chiffres**
    - Inclure des **symboles**
- Choix de la **longueur du mot de passe** (jusqu'à 30 caractères)
- Copie du mot de passe généré dans le presse-papiers
- Interface graphique conviviale avec `PySide6`

## Prérequis
- **Python 3.x** installé sur votre système
- **pip** pour installer les dépendances

## Installation et utilisation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/pauldecalf/Password-Generator-Python.git
   cd Password-Generator-Python
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python3 -m venv venv
   ```

3. **Activer l'environnement virtuel** :
    - Sur Windows :
      ```powershell
      .\venv\Scripts\activate.ps1
      ```
    - Sur macOS/Linux :
      ```bash
      source venv/bin/activate
      ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer l'application** :
   ```bash
   python main.py
   ```

## Générer le fichier `requirements.txt`
Pour geler les dépendances, exécutez la commande suivante :
```bash
pip freeze > requirements.txt
```

## Technologies utilisées
- **Python 3**
- **PySide6** pour l'interface graphique

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez ajouter des fonctionnalités ou améliorer le code existant, n'hésitez pas à créer une pull request.

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amélioration`)
3. Commit les modifications (`git commit -m 'Ajouter une fonctionnalité'`)
4. Pousser sur la branche (`git push origin feature/amélioration`)
5. Ouvrir une pull request
