# 🚀 Asteroids — Pygame Arcade Game

A modern take on the classic **Asteroids** arcade game, built using Python and Pygame. In this game, you control a triangular spaceship that can rotate, move, and shoot bullets to destroy randomly spawning asteroids. Asteroids split into smaller ones when hit, and the game ends if your ship collides with any of them.

---

## 🎮 Features

- 🔄 Full 360° rotation for the player's spaceship  
- 🛰️ Movement based on direction of rotation (thrust forward and backward)  
- 💥 Bullet firing with cooldowns  
- 🌑 Random asteroid spawning from screen edges  
- 🪨 Asteroid splitting upon impact  
- ❌ Collision detection between player, bullets, and asteroids  
- 🕹️ Sprite-based architecture using `pygame.sprite.Group`

---

## 🕹️ Controls

| Key        | Action                  |
|------------|-------------------------|
| `A`        | Rotate left             |
| `D`        | Rotate right            |
| `W`        | Thrust forward          |
| `S`        | Thrust backward         |
| `SPACEBAR` | Shoot                   |
| `ESC` or Close Window | Exit game     |

---

## 🛠️ Requirements

- Python 3.8 or later  
- Pygame (`pip install pygame`)

---

## 📁 File Structure

```
asteroids/
├── main.py              # Game loop and entry point
├── constants.py         # Global settings and game constants
├── players.py           # Player (spaceship) logic
├── asteroids.py         # Asteroid logic and splitting
├── asteroidfield.py     # Spawning asteroids at screen edges
├── circleshape.py       # Base class for circular game objects
├── shot.py              # Bullet (shot) logic
```

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install pygame
   ```

2. **Run the game**
   ```bash
   python3 main.py
   ```

3. **Play!**
   - Use `W`, `A`, `S`, `D` to move and rotate.
   - Press `SPACEBAR` to shoot.
   - Destroy asteroids and avoid crashing!

---

## 📌 Game Logic Overview

- **Player** is a rotating triangle with shooting and thrust movement.  
- **Shots** are small circles that travel in the direction the player faces.  
- **Asteroids** spawn randomly from screen edges and move inward.  
- **Splitting**: When a bullet hits a large asteroid, it splits into two smaller ones.  
- **Game Over** occurs if an asteroid collides with the player.

---

## 👨‍💻 Credits

- Inspired by the classic *Asteroids* arcade game.  
- Built with love using [Pygame](https://www.pygame.org/).  
- Project based on course material from [Boot.dev](https://boot.dev/)  
- Special thanks to [Lane Wagner](https://www.linkedin.com/in/wagslane/) for course content and game design inspiration.

---

## 🧠 Ideas for Improvement

- Add sound effects and background music  
- Implement score tracking and lives  
- Add a start menu and "Game Over" screen  
- Create power-ups or additional weapons
