# usecase
Superviser la production nucléaire en infrajournalier
  o Récupérer les données depuis l’API RTE (https://data.rte-france.com/) 
   Créer un compte et récupérer la clé 
   API à utiliser : https://data.rte-france.com/catalog/-/api/generation/ActualGeneration/v1.1
   Documentation de l’API : https://data.rte-france.com/catalog/-
  /api/doc/user-guide/Actual+Generation/1.1
   Endpoint à utiliser : /actual_generations_per_unit 
  o Transformer la donnée 
   Récupérer la moyenne heure par heure 
  o Afficher un graphe 
   Afficher un barplot de la somme de la production infrajournalière par heure 
  du jour sur la période 01/12/2022 à 10/12/2022. 
  o Ecrire un test de non-régression pertinent 
BONUS : 
Automatiser le rafraîchissement en temps réel de l’interface sur une période hebdomadaire 
glissante 
