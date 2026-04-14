# A* Pathfinding Visualizer

An interactive, educational pathfinding visualizer built with [Pygame Zero](https://pygame-zero.readthedocs.io/). Watch the A* algorithm explore a grid in real time, place walls to create obstacles, and see the shortest path traced back once the goal is reached.

![A* visualizer demo](a_star.gif)

---

## Features

- **Step-by-step visualization** — the algorithm advances at a configurable tick rate so you can follow each expansion
- **Random board generation** — every reset picks a new grid size and scatters random walls
- **Configurable movement** — switch between 4-directional and 8-directional (diagonal) movement
- **Configurable heuristic** — Manhattan distance (default) or Euclidean distance
- **Interactive** — place/remove walls and reposition the goal with the mouse

## Color Legend

| Color | Meaning |
|-------|---------|
| Pink | Start cell |
| Red | Goal cell |
| Blue | Open set (frontier) |
| Green | Visited (closed set) |
| Gray | Wall |
| Magenta | Final path |

## Controls

| Input | Action |
|-------|--------|
| `S` | Start the search |
| `R` | Reset with a new random board |
| Left click | Toggle wall on a cell |
| Right click | Move the goal to that cell |

## Getting Started

### Prerequisites

- Python 3.8+
- Pygame Zero

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

## Configuration

Open `main.py` and tweak the constants at the top:

```python
# Movement directions (4 or 8)
MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 4 directions
# MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 8 directions

# Heuristic function (Manhattan or Euclidean)
DISTANCE_FUNC = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) # manhattan distance
# DISTANCE_FUNC = lambda p1, p2: math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) # euclidean distance

DELAY = 5 # Frames between each algorithm step (lower = faster)
```

## How It Works

1. Cells are placed into a **priority queue** ordered by their estimated distance to the goal (heuristic *h(n)*).
2. At each tick the cell with the lowest *h* value is popped, marked visited, and its unvisited neighbours are enqueued.
3. Each cell records its **predecessor**, so when the goal is reached the full path can be traced back to the start.

## License

[MIT](LICENSE)