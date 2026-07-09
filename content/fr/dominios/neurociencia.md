# Domaine : Neurosciences — Crises d'Épilepsie (CHB-MIT)

## 1. Contexte

Les **crises d'épilepsie** sont des transitions de régime dans la dynamique corticale. L'EEG multicanal est le prototype d'un système où :

- il y a de nombreuses variables (canaux/bandes),
- l'événement est annoté,
- l'intérêt clinique porte sur l'état **pré-ictal**.

CHB-MIT (PhysioNet) propose des enregistrements pédiatriques avec annotations de crises.

## 2. Limites des EWS Classiques

- Un canal unique peut ne pas montrer de CSD (ralentissement critique) clair.
- Les artefacts et le sommeil faussent la var/l'AR1.
- La transition est **spatialement distribuée** : la signature réside dans la **synchronisation des modèles**, et non seulement dans la puissance d'un canal.

## 3. Apport Tau + RECD

- Multivarié : puissances de bande ou enveloppes de 4 à 8 canaux/bandes.
- Φ₁–Φ₃ capturent la **co-ordination symbolique** pré-ictale.
- excess3 comme proxy de la configuration de réseau irréductible.
- Comparaison avec la TE classique et les indices de synchronisation standards (PLV, etc.) en mode complet (Full).

## 4. Jeu de Données

- Extrait synthétique ou traité de type pré-ictal (le CHB-MIT brut n'est pas redistribué dans son intégralité).
- Scripts de téléchargement sous les conditions d'utilisation (ToS) de PhysioNet.

## 5. Maturité

**Moyenne-Haute** dans la plateforme v1 : pipeline prêt ; preuves empiriques en cours de consolidation (moins mature que le CCTP).

## 6. Références

- CHB-MIT PhysioNet ; littérature sur la prédiction des crises ; cadre ordinal du paradigme.
