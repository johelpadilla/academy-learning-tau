# Mathématiques du Paradigme — Carte

Cette section de la plateforme détaille les blocs computationnels. Ordre pédagogique :

1. **Modèles Ordinaux (Bandt–Pompe)** — l'alphabet.
2. **Tau Systémique (τ_s)** — le thermomètre relationnel.
3. **Fenêtre Adaptative (Breathing Window)** — le rythme d'observation.
4. **RECD Φ₁–Φ₃ + excess3** — l'horloge et ses niveaux *(voir Fondamentaux)*.
5. **TDA + Nombres de Betti (Tier 4)** — topologie du nuage d'états.
6. **Mémoire Ordinale** — TE (Transfer Entropy) symbolique / MI (Mutual Information) de rang.
7. **Surrogates** — IAAFT et phase-shuffle comme modèles nuls.

## Notation Commune

| Symbole | Signification |
|---------|-------------|
| \(X \in \mathbb{R}^{T\times N}\) | Série multivariée |
| \(m, \tau\) | Dimension et délai Bandt–Pompe |
| \(W\), stride | Fenêtre et pas de τ_s |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveaux de conjonction |
| excess3 | Proxy continu de synergie |
| \(\lambda\) | Intensité du régime / réorganisation |
| \(\alpha_k(\lambda)\) | Poids du ΔRECD |

## Complexité Indicative

- Bandt–Pompe univarié : \(O(T \cdot m \log m)\) (ou \(O(T)\) avec m fixe=3 et numba).
- Φ₁ : \(O(T \cdot N^2)\).
- Φ₂ : \(O(T \cdot N^2 \cdot d)\).
- Φ₃ / excess3 : \(O((T/w) \cdot w \cdot \mathrm{co\hat{u}t\ de\ comptage})\) ; avec \(m=3\), un petit \(N\) est réalisable.
- Surrogates : × n_surr le coût de la métrique choisie.

## Mode Fast vs Full

| Bloc | Fast | Full |
|--------|------|------|
| τ_s + RECD | Oui | Oui |
| EWS Classiques | Oui | Oui |
| Surrogates | n=8 | n≥50 |
| TDA Betti | Non | Oui |
| Mémoire ordinale | Non | Oui |
