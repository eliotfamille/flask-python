# Journal de decouverte, ANDRAINARILANTO Eliot Famille

## Mission 1 : Faire tourner Flask
- Essaye : lancer sans debug, puis avec debug, erreur volontaire (retirer les ""), lancer sans app
- Observe :
  - sans debug : modification pas visible (relancer le serveur)
  - avec debug : le terminal signale le changement et redemarre (reloading)
  - erreur volontaire : page de debogage dans le navigateur (TypeError), meme erreur dans le terminal
  - sans app : ca marche quand meme (fichier app.py trouve)
- Doc : j'ais directement rechercher dans la barre de recherche
- Explique :
  - debug : rechargement automatique, erreurs detaillees dans le navigateur
  - jamais en production : le debogueur execute du code Python depuis le navigateur (risque majeur)
  - app facultatif : fichier nomme app.py ou wsgi.py trouve tout seul

## Mission 2 : Jouer avec les URL
- Essaye : route avec id seul, print du type, convertisseur int, adresse abc, slash final, tache 99, abort 404
- Observe :
  - id seul : Tache introuvable (anormal)
  - print : type str, valeur 2 (une chaine)
  - convertisseur int : tache 2 OK, adresse abc donne 404
  - slash final : 404
  - tache 99 avec return texte : code 200
  - tache 99 avec abort 404 : code 404
- Doc : Quickstart.j'ais directement rechercher dans la barre de recherche
- Explique :
  - sans convertisseur, id est une chaine (2 en texte) et la liste contient des entiers (2 en nombre), donc jamais egal
  - int : convertit en entier, et donne 404 si ce n'est pas un entier
  - slash final : la route est definie sans slash, donc l'adresse avec slash donne 404
  - 404 mieux que 200 : le code dit vraiment que la page n'existe pas (navigateur, moteurs de recherche)

## Mission 3 : Afficher les taches
- Essaye : afficher la liste, boucle for, loop.index, filtres, if terminee, variable inconnue, titre avec balise b, compter les restantes
- Observe :
  - liste affichee telle quelle : forme Python brute (crochets, dictionnaires)
  - boucle for : t.titre marche sur un dictionnaire (Jinja cherche l'attribut, puis la cle)
  - filtres OK : upper, length, sort sur attribut titre
  - variable inconnue : rien affiche, pas d'erreur
  - titre avec balise b : affiche tel quel, pas en gras
  - restantes : filtres rejectattr(terminee), list, length
- Doc : Quickstart.j'ais directement rechercher dans la barre de recherche
- Explique :
  - accolades doubles : afficher une valeur. Accolades avec pourcentage : instruction (for, if)
  - variable inconnue : valeur vide, pas d'erreur
  - balise b pas en gras : echappement automatique (le signe inferieur devient du texte), protege contre XSS (injection de code)

## Mission 4 : Un menu commun
- Essaye : base.html avec extends, texte hors bloc, bloc titre avec super, style.css, lien vers route inexistante, renommer le dossier templates
- Observe :
  - code source : page complete, base.html avec le contenu de taches.html dedans
  - texte hors bloc : pas affiche
  - super : affiche aussi le contenu du bloc du parent
  - static style.css : le fichier css s'affiche
  - lien vers ajouter inexistante : BuildError
  - dossier template (sans s) : TemplateNotFound
- Doc : Jinja, Quickstart. j'ais directement rechercher dans la barre de recherche
- Explique :
  - extends : reprend le template parent et remplit ses blocs (premiere ligne du fichier)
  - texte hors bloc disparait : l'enfant ne peut remplir que les blocs du parent
  - super : reprend le contenu du bloc parent
  - Flask cherche dans templates et static (a cote de app.py)

## Mission 5 : Ajouter une tache
- Essaye : ajout sans redirection puis F5, onglet Reseau, redirect, titre vide, cle de formulaire fausse, formulaire sans method post
- Observe :
  - sans redirection, F5 : le navigateur demande de renvoyer le formulaire, tache en double
  - Reseau : requete POST sur la page ajouter
  - avec redirect : POST code 302, puis GET code 200 (F5 refait seulement le GET, pas de doublon)
  - titre vide : accepte (donc validation necessaire)
  - validation : titre non vide, 80 caracteres au plus, priorite parmi les trois valeurs, sinon reafficher le formulaire
  - cle fausse avec crochets : erreur 400 (Bad Request)
  - sans method post : envoi en GET, donnees visibles dans l'adresse (query string)
- Doc : Quickstart. j'ais directement rechercher dans la barre de recherche
- Explique :
  - rediriger apres POST : evite le doublon au F5 (motif POST, redirection, GET)
  - get : valeur par defaut si le champ manque (pas d'erreur). Crochets : erreur 400 si le champ manque
  - formulaire en GET : donnees dans l'adresse (query string), visibles, gardees dans l'historique

## Mission 6 : Messages et memoire
- Essaye : flash sans cle secrete, avec cle et F5, filtre avec args et session, fenetre privee, modifier le cookie session
- Observe :
  - sans cle : RuntimeError (session indisponible, secret_key absente)
  - avec cle : message affiche une fois, disparait apres F5
  - url_for avec filtre actives : adresse avec parametre filtre (query string)
  - retour sur la page sans parametre : dernier filtre garde (session)
  - fenetre privee : filtre par defaut toutes, rien de memorise
  - cookie modifie : Flask l'ignore, session vide
- Doc : Quickstart. j'ais directement rechercher dans la barre de recherche
- Explique :
  - flash utilise la session, et la session est signee avec la cle secrete
  - message disparu apres F5 : un message flash est lu une seule fois
  - session stockee dans un cookie du navigateur (signe, pas chiffre). Fenetre privee : cookies separes, vides
  - cookie modifie : la signature ne correspond plus, donc cookie ignore

## Bonus
- Boutons Terminer et Supprimer : formulaires POST et pas des liens, car un lien est un GET et un GET ne doit pas modifier les donnees (robots, prechargement, clic accidentel)
- Page 404 perso : errorhandler 404, renvoyer le template avec le code 404
- Route api : le navigateur recoit du JSON (liste convertie en reponse JSON). Doc : Quickstart. j'ais directement rechercher dans la barre de recherche
