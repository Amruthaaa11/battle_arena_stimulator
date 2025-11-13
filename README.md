# Battle_arena_stimulator
A simple Python-based character battle game.

## Features

- Randomized character creation (strength and health)
- Dice-based combat rounds
- Automatic damage calculation and health tracking
- Console-based gameplay with round-by-round updates

## How It Works

Each character is assigned:
- **Strength**: `(1d6 * 1d8) / 2 + 12`
- **Health**: `(1d6 * 1d12) / 2 + 10`

Combat proceeds in rounds:
- Both characters roll a 6-sided die.
- The higher roll wins the round.
- The loser takes damage equal to the absolute difference in strength.
- The game ends when one character’s health drops to zero or below.

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- VS Code or any Python-compatible IDE

### Run the Game

```bash
python battle_game.py
