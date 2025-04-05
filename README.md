# Greedy Snake Showdown 🐍

It’s Snake. But not just *any* snake. This is **Player vs. CPU Snake**, built with `pygame-ce`, where your squishy human reflexes go head-to-head with a cold, calculating AI serpent who does not know mercy.

**Warning:** The CPU snake is OP and does not believe in fairness.

## 🐍 Features

- Classic Snake gameplay, but multiplayer(ish)
- Greedy AI snake that hunts fruit like it owes it money
- Basic score tracking (no trophies, just numbers)
- Arcade-style visual with customizable snake colors
- Built with `pygame-ce`, so it runs on actual pixels
- BFS AI class ready to be implemented if you feel spicy

## 🛠 Installation

Clone the repo and install the requirements (you *do* have Python, right?):

```bash
git clone https://github.com/gurveershienh/snakevscpu.git
cd snakevscpu/src
```

Create a virtual environment (or live dangerously without one):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

> You’ll need `pygame-ce`. It's in the `requirements.txt`, don't worry.

## 🎮 Usage

To start the game, just run:

```bash
python main.py
```

You’ll see:
- A green snake: you
- An orange snake: your robot rival
- A red fruit: the prize
- Victory: unlikely

## 🎯 Controls

- `W` / `↑` — Up  
- `A` / `←` — Left  
- `S` / `↓` — Down  
- `D` / `→` — Right  

Avoid walls, your own body, and the AI snake who has no chill.

## 🧠 AI Details

- **GreedySnake**: Chooses the shortest path to the fruit without basic regard for consequences.
- **GreedyBFSSnake**: Planned but not implemented. Probably less terrifying than the greedy one. Maybe.


## 📁 Project Structure

```
.
├── main.py           # Game loop and logic
├── snake.py          # All snake classes, fruit, score, and unfinished dreams
├── requirements.txt  # pygame-ce lives here
└── assets/           # Fonts and any future graphics
```

## ❗️Known Issues

- CPU snake sometimes wins at life. That’s not a bug, that’s just evolution.
- Fruit can spawn close to snake bodies. Might fix, might not.
- Score tracking is based on length difference, not skill.

## 📜 License

No license yet. Assume all rights reserved unless you're adding the BFS logic, in which case... carry on.

---

Enjoy the chaos. Try to win. You won't.
