# Manuel de zPortapapeles

Cette extension a comme base l'extension Fake Clipboard Announcement. 

Avec zPortapapeles nous aurons l'annonce des pulsations pour copier, coller, défaire, couper et sélectionner tout.

Il a été inclus à l'extension la possibilité d'activer et de désactiver des sons qui renforcent les messages ainsi qu'un historique avec lequel nous pouvons copier au focus.

## Gestes de commandes...

Dans la section Gestes de commandes... de NVDA Si nous recherchons la catégorie zPortapapeles nous pouvons ajouter une combinaison de touches non assignée par défaut  à l'historique pour afficher le dialogue.

Nous aurons également une section où nous pouvons modifier les déclencheurs des touches faisant référence au Presse-papiers, cette section ne le modifiera que si notre langue ou notre système a des autres touches assignées par défaut au presse-papiers.

## Paramètres de l'extension

Dans les Paramètres de  NVDA dans la catégorie Paramètres  de zPortapapeles nous pouvons activer et désactiver à partir des cases à cocher si à la fois nous voulons les sons comme si nous voulons avoir l'historique activé, nous pouvons également choisir si nous souhaitons recevoir les messages verbalisés.

Si la case de l'historique est activée, nous aurons une liste déroulante dans laquelle choisir la durée  de temps de surveillance du presse-papiers et une case pour activer ou désactiver si nous voulons un son lorsque nous ajoutons quelque chose à l'historique.

Si la case est désactivée à la fois la liste déroulante comme la possibilité de choisir si nous voulons les sons dans l'historique n'apparaissent pas.

Noter que si nous commençons à recevoir des erreurs de presse-papiers est opportun d'augmenter la durée de temps de surveillance du presse-papiers.

## Dialogue de l'Historique

À ce dialogue, nous devrons lui assigner dans le dialogue Gestes de commandes... une combinaison de touches par défaut laquelle n'est pas assignée.

Le dialogue s'ouvrira uniquement lorsque vous avez une entrée enregistrée, tant que vous n'avez pas de entrées, nous ne pouvons pas l'ouvrir.

Tout sera signalé avec des messages informatifs, de même, si nous avons déjà le dialogue ouvert.

Une fois que le dialogue est ouvert, celui-ci  est composé de La liste des entrées que vous avez et 4 boutons qui sont les suivants:

* Effacer ou Alt+E: Si nous appuyons sur ce bouton effacera l'entrée selon laquelle  la liste a le focus.

* Effacer tout ou Alt+T: Effacera toutes les entrées de l'historique.

* Rafraîchir ou Alt+R: Rafraîchira l'historique avec les nouvelles entrées ajoutées, c'est bien au cas où nous ajoutons à l'historique pendant que le dialogue est ouvert.

* Fermer ou Alt+F, Échap ou Alt+F4: Fermera le dialogue de l'historique.

Lorsque nous sommes sur la liste si nous appuyons sur Entrée, l'entrée qui a le focus sera copié à l'application qui est derrière le dialogue de l'historique.

Par exemple, si nous avons ouvert le Bloc-notes et nous ouvrons l'historique et nous appuyons sur Entrée dans la première  entrée il copiera au Bloc-notes l'élément que nous avons sélectionné.

## Limitations  de zPortapapeles

zPortapapeles n'est pas compatible avec d'autres extensions installées qui font la même chose comme Fake Clipboard Announcement ou Clipspeak. Elle peut y avoir d'autres, et dans ce cas, vous devrez les désactiver si vous souhaitez utiliser zPortapapeles.

Annoter que les entrées de l'historique seront effacées lorsque nous redémarrons NVDA.

L'historique de presse-papiers Windows peut avoir des entrées en double si nous utilisons l'historique de zPortapapeles. Nous devrons choisir ce que nous voulons utiliser.

## Remerciements 

* Javi Domínguez: Pour son aide désintéressée et contribuer à la fonction de surveillance du presse-papiers.
* Portugais Brésil: pedro-hdias
* Russe: Valentin Kupriyanov
* Turc: Umut KORKMAZ
* Italien: Alessio Lenzi
* Français: Rémy Ruiz

# Journal des changements.
## Version 0.3.

* Ajouter une détection s'il y a un texte sélectionné lors de la copie.

Maintenant, l'extension lorsque nous faisons  copier s'il ne détecte pas de texte, nous le signalera avec un message.

* Ajouté pour désactiver et activer rapidement les fonctions de l'extension par rapport au presse-papiers.

Dans le dialogue Gestes de commandes nous pouvons configurer une combinaison pour activer et désactiver rapidement se  qui est relatif au presse-papiers.

Lorsque nous désactivons le presse-papiers et les messages seront les natifs de Windows à côté  des messages que NVDA a prédéfini pour le presse-papiers.

Cela n'affectera pas l'historique que si c'est actif, celui-ci continuera  à être actif.

* Ajout de la compatibilité avec les claviers qui utilisent des caractères cirilliques.

Un problème a été résolu dans les distributions de clavier qui utilisent des caractères cirilliques.

* Ajout des langues Russe, Turc, Italien et Portugais Brésil.

## Version 0.2.

* Changé toutes les fonctions du presse-papiers à cTypes

Maintenant, le presse-papiers sera traité directement avec des fonctions du système évitant d'utiliser les fonctions de NVDA et WXPython.

* Préparé l'extension afin d'être traduite.

## Version 0.1.5.

* Verbaliser ce qui a été copié dans le presse-papiers et ajouté à l'Historique.

Si nous avons activé l'option Activer ou désactiver l'historique du presse-papiers dans les paramètres de l'extension nous aurons cette nouvelle option.

Avec cette option ce qui est copié à l'historique  ou si vous êtes déjà dans l'historique cette dernière qui est copiée au presse-papiers sera lu par NVDA.

Il ne sera mentionné que cette dernière qui est copiée et une seule fois sera mentionnée afin de ne pas saturer jusqu'à ce qu'il ne dise plus qu'une autre chaîne qui est copiée la précédente ne sera répété à nouveau.

* Le presse-papiers sera effacé lorsque vous démarrez l'extension pour la première fois.

Maintenant, ce que nous avions dans le presse-papiers ne sera plus copié lorsque nous avons démarré NVDA, maintenant, le presse-papier démarre propre.

Cela n'affecte pas l'historique de presse-papiers Windows.

*** AVERTISSEMENT: Ceci nous devons le prendre en compte car il peut être effacé quelque chose d'important que nous ayons eu dans le presse-papiers. ***

## Version 0.1.4.

* Changé la façon d'obtenir les données du presse-papiers.

## Version 0.1.3.

* Augmentation de la condition de l'extension à NVDA 2021.2 comme une version minimale à utiliser.

* Des options ont été ajoutées à l'historique.

Maintenant, nous pouvons choisir la durée de temps de surveillance comme si nous voulons un son lorsque quelque chose est copié à l'historique.

* Ajout de la compatibilité avec Word et Excel afin de ne pas annoncer les touches du presse-papiers.

* Maintenant, le presse-papiers est surveillé de sorte que toute extension qui copie au presse-papiers soit déjà compatible, même la copie de NVDA au focus.

## Version 0.1.2.

* Il a été ajouté Activer ou désactiver les annonces verbalisés du presse-papiers dans Paramètres.

Dans les applications autorisées, les messages correspondant aux touches du presse-papiers seront omises.

## Version 0.1.1.

* La façon de gérer les captures du presse-papiers et sa gestion ont été changées.

* C'est  corrigé l'erreur qui laissé ouvert le presse-papiers.

## Version 0.1.

* Version initiale.