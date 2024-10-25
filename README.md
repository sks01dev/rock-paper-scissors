# RPS 9000 - Rock, Paper, Scissors Game 🎮

Welcome to **RPS 9000**, a fun and interactive Rock-Paper-Scissors game built in Python! Test your skills against a simple AI and see who comes out on top. This project is designed to be straightforward and engaging, with real-time score tracking and a clean user experience.

## 🎉 Features

- **Play Rock, Paper, Scissors** with an AI opponent.
- **Emoji-based display** for each move: 🥊, 📜, ✂️.
- **Score tracking** after each round for both user and AI.
- **Easy exit** with final score display.

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** installed on your system.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/RPS-9000.git
   ```
2. **Navigate into the directory**:
   ```bash
   cd RPS-9000
   ```

### Run the Game
To start playing, simply run:
```bash
python3 rps.py
```

### How to Play

1. **Enter your move** when prompted: `rock`, `paper`, or `scissors`.
2. **Invalid moves** will prompt you to re-enter a valid option.
3. **Type "exit"** anytime to quit the game, and see your final score.

## 🛠️ How It Works

This game has three core components:

1. **User Input** - The game asks for your move, validates it, and checks for the "exit" command.
2. **AI Move** - The AI randomly selects a move from the available options.
3. **Score Tracking** - After each round, scores update based on who won the round.

### Game Logic

The winner of each round is decided by the following rules:
- 🥊 Rock beats ✂️ Scissors
- 📜 Paper beats 🥊 Rock
- ✂️ Scissors beat 📜 Paper
- Same moves result in a tie

### Example Gameplay

```
Welcome to RPS 9000!
Rock, paper or scissors? (type "exit" to quit) >> rock
-----
You: 🥊
AI: 📜
-----
AI wins...
Score - You: 0 | AI: 1
```

## 📂 Project Structure

- **rps.py** - The main game file.

## 🤝 Contributing

1. **Fork the repository**.
2. **Create a branch** for any feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes** and open a pull request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy playing RPS 9000, and may the best player win! 🏆
