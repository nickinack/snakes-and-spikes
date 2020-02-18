# Snakes and Spikes!

Snakes and Spikes is an elementary python game designed to relieve you from stress and boredom! The multiplayer game features a rabbit desperately trying to reach the other ed of the river as it gets past moving obstacles (snakes) and spikes.

## Installation

Download the python script. Run the following bash script:

```bash
pip3 install pygame
```

```bash
python3 game.py
```

## Rules

There are three levels in this game. The speed of moving obstacles increase as you enter further levels. Time penalty of one point per second is present. When you reach the other end successfully, controls transfer to the next player and the you get a 30 point bonus for crossing all the obstacles. If you collide with anyone od the obstacles, players transfer to the next player , and you loose 100 points. After 3 rounds, the winner will be displayed!
