# Assistant technique intelligent (RAG + agents) — secteur Industrie

## Introduction
Le projet consitste a coder un agent technique intelligent (RAG + agent IA ) pour la maintenance industrielle, il aide les techniciens à retrouv er la bonne procédure pour réparer une machine en panne en qlq secondes au lieu de 35 minutes.

## Probleme
Ferro-Nord Équipements (client fictif, ETI ~1150 salariés, ~3400 machines
chez ~600 clients) a ~14 000 pages de documentation technique dispersée
(manuels, schémas, PDF scannés, Word, Excel) à travers plusieurs
générations de machines. Face à une panne, un technicien :
- perd du temps à chercher la bonne procédure ~35 min/intervention 
-interrompt un collègue senior
-risque d'appliquer la mauvaise procédure du au nombreux générations de machines 

## Impact estimé 
 ~585 k€/an de temps improductif** (62 techniciens x
~1h/jour perdue x ~210 jours), hors pénalités SLA.

## objectif 
Un assistant qui répond aux questions techniques des SAV en citant la
bonne procédure, avec les bons garde-fous (pas d'invention).

## KPI cibles

| KPI                          | Cible v1      |
|-------------------------------|---------------|
| Temps de recherche moyen      | < 2 min (vs ~35 min) |
| Réponses correctes et sourcées| > 85 %        |
| Taux d'hallucination          | < 2 %         |
| Coût moyen / requête          | < 0,05 €      |

## Stack (prévue)

Python, PostgreSQL + pgvector, FastAPI, LangGraph, Docker, RAGAS.

## Statut

🚧 En cours de développement (Semaine 1/26 du programme) — architecture
et fonctionnalités en construction.


