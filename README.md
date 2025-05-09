# DraftGenius

**Fantasy Draft Assistant for Premier League (2024–25 Season)**  
A simple command‑line tool that helps you build an optimal 11‑player fantasy squad under a budget and with team‑limit constraints.

## 🔍 Overview

DraftGenius reads a fixed `players.csv` roster of all 20 Premier League teams (2024–25) and uses a greedy value‑per‑cost algorithm to pick:

- **Exactly 11 players**  
- **Stays within your salary cap**  
- **No more than 3 players from any one real‑world team**

You can also override squad size or per‑team limits via command‑line flags.

## ⚙️ Requirements

- Python 3.7+  
- Standard library only (no external packages)