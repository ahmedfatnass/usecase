# usecase
Superviser la production nucléaire en infrajournalier<br>
o Récupérer les données depuis l’API RTE (https://data.rte-france.com/) <br>
   Créer un compte et récupérer la clé <br>
   API à utiliser : https://data.rte-france.com/catalog/-/api/generation/ActualGeneration/v1.1 <br>
   Documentation de l’API : https://data.rte-france.com/catalog/-
  /api/doc/user-guide/Actual+Generation/1.1 <br>
   Endpoint à utiliser : /actual_generations_per_unit <br>
  o Transformer la donnée  <br>
   Récupérer la moyenne heure par heure <br>
  o Afficher un graphe <br>
   Afficher un barplot de la somme de la production infrajournalière par heure 
  du jour sur la période 01/12/2022 à 10/12/2022. <br>
  o Ecrire un test de non-régression pertinent <br>
BONUS : <br>
Automatiser le rafraîchissement en temps réel de l’interface sur une période hebdomadaire 
glissante <br>
