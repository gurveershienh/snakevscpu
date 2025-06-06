# Snake vs CPU 🐍
![Gameplay Demo](src/assets/snakevscpu_demo.gif)

It’s Snake. But not just *any* snake. This is **Player vs. CPU Snake**, built with `pygame-ce`, where squishy human (blue) reflexes go head-to-head with a cold, calculating AI serpent (green) who does not know mercy.

The CPU snake is powered by a greedy algorithm. It moves fast, grows quickly, and can be outsmarted

Play it here ---> https://gurveershienh.github.io/snakevscpu/

Compiled to  WebAssembly using pygbag

---

## Features

- Classic Snake gameplay with an AI twist  
- CPU-controlled snake that aggressively targets fruit  
- Real-time collision, fruit handling, and dynamic score tracking  
- Modular code structure using object-oriented Python  
- Built with `pygame-ce` for fast, frame-based game logic  

---

Gameplay Overview:
- Blue snake: You 
- Green snake: Rival CPU 
- Red fruit: Yummy

---

## Controls

- `W` / `↑` — Up  
- `A` / `←` — Left  
- `S` / `↓` — Down  
- `D` / `→` — Right  

Avoid walls, yourself, and your AI enemy.

---

## Greedy Snake AI

The CPU snake uses a **greedy pathfinding algorithm**. On each update cycle, it evaluates available directions and chooses the one that brings it closest to the fruit while avoiding collisions with:
- The board edges
- Its own body
- The player snake

It uses **squared Euclidean distance** for fast calculation and purely local heuristics—no full pathfinding, no memory. It’s hungry and reckless.
