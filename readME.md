# About
Ecriture des tests associés aux services, TDD
Exécuter les tests dans un container
Exposer les services sous forme d’API
Déployer l’API
Référencer l’API dans l’Azure API Management
Ajouter une fonctionnalité avec persistance via Cosmos DB


Application TDD + API
# Ressources:
https://dmerej.info/blog/fr/post/tester-en-python-pytest-et-tdd/
• Comprendre le TDD
• Reprendre le programme mvc.py
• Tester que le résultat en sortie est bien le paramètre d’entrée mis en majuscule
• Packager l’application dans une API avec FastAPI
http://localhost:3000/text/uppercase?source=« YOUR_TEXT »
• Packager l’application dans une API avec FastAPI
• Avec l’approche TDD, écrire un endpoint qui permet de savoir si un mot est un palindrome
http://localhost:3000/text/palindrome?source=« YOUR_TEXT »


## Lancer le server

uvicorn api.app:app --reload