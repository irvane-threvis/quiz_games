 

Rapport d'explication du projet Quiz Game en python

Membres du groupe :

 NOMS	      PENOMS
.COMPAORE	Ivan  Kisito
.NACOULMA	W. Betsaleel
.TOUGOUMA	Irvane Threvis
.YAMEOGO	W Hyacinthe
.ZONGO	P Juste Landry


1. Présentation Générale du Projet
Le projet Quiz Game est une application de jeu de questions-réponses interactive développée en Python. Il s'appuie sur la bibliothèque Tkinter pour l'interface graphique, utilise des fichiers JSON pour stocker les questions et les scores, et est conçu pour proposer une expérience utilisateur fluide et adaptable selon le niveau du joueur.
Le jeu présente différentes catégories de difficultés (facile, moyen, difficile) et enregistre les résultats des joueurs pour un suivi des performances.
II). Explication des différentes parties du projet
1.main.py (lancement du jeu)
C'est le fichier principal. Il initialise l'interface graphique et démarre le jeu.
 

2.GAME_UI.PY (INTERFACE GRAPHIQUE TKINTER)
•	C’est le centre du jeu : tout ce que le joueur voit est géré ici.
•	Voici le déroulement:
                a) Saisie Du Prénom
                
•	Une fenêtre demande le prénom du joueur
                b) choix du niveau
                
•	Le joueur choisit : facile, moyen, difficile.
                c)choix de la catégorie
	Par exemple : maths, histoire, physique (en fonction des questions disponibles dans les fichiers. Json).

                d)affichage des questions
                
•	Le jeu montre chaque question, avec les réponses proposées.
•	Si c’est une question avec image, elle est affichée aussi.
                e) Réponse du joueur
                
•	Si la réponse est correcte, un message « Bravo » s'affiche, et un bonus de score est ajouté.
•	Sinon, l'explication est affichée.

                f) Affichage du score final
•	Quand toutes les questions sont terminées, le score est affiché.
•	L'utilisateur peut rejouer ou quitter.


3.quiz_manager.py (gestion des questions)
Ce fichier gère la logique du quiz :
•	Il garde une liste de questions.
•	Il donne la prochaine question (get_question()).
•	Il vérifie la réponse choisie (check_answer()).
•	Il garde le score à jour.


4.difficulty.py (définition des règles selon la difficulté)
Ce fichier donne les bonus de score en fonction du niveau choisi :
•	easy → +1 point
•	medium → +1 points
•	hard → +1 points


5.data/questions/*.json (les questions du jeu)
Ces fichiers sont utilisés pour :
1.	Organiser les questions par difficulté et par catégorie :
o	Le quiz charge le fichier selon le niveau choisi.
o	Il filtre ensuite par catégorie (ex : maths, info, etc.).
3.	Rendu dynamiquement le contenu du quiz :
o	Le programme lit ces fichiers JSON quand tu choisis une catégorie.
o	Les questions sont ensuite affichées dans l'interface graphique.


6.Data/scores. Json (enregistrement des scores)
. Quand le jeu se termine, ce fichier enregistre le nom du joueur, le niveau, et le score dans le fichier data/scores.json.
. Il utilise le format JSON pour garder une trace des joueurs avec la fonction Save score().
