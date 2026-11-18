# Langton's Ant (Python Turtle)

A lightweight implementation of **Langton's Ant**—a two-dimensional Turing machine and cellular automaton—built using Python's built-in `turtle` graphics library.

## How It Works

An agent (represented by a red square) moves across a 10×10 pixel grid following two deterministic rules:

1. **On an empty (white) cell:** Turn **90° right**, flip the cell to **black**, and move forward one grid step.
2. **On a filled (black) cell:** Turn **90° left**, flip the cell back to **white**, and move forward one grid step.

Despite these simple local rules, the simulation goes through three distinct phases:
* **Simplicity (~first 500 steps):** Produces small, symmetrical patterns.
* **Chaos (~steps 500 to 10,000):** Generates a pseudo-random, irregular cluster of black and white cells.
* **Emergent Order (~step 10,000+):** Suddenly breaks out into a repeating, diagonal **"highway"** pattern of 104 steps that continues indefinitely.

## Implementation Highlights

* **Grid-Aligned Stamping:** Both the trail turtle (`t`) and the active cursor (`pat`) use scaled `'square'` turtle shapes (`GRID_STEP / CURSOR_SIZE`) so stamps align dead-center on a uniform 10×10 coordinate grid without manual polygon drawing.
* **O(1) State Tracking via Dictionary:** Because Python's `turtle` canvas cannot read pixel colors directly, filled cells are stored in a dictionary mapping rounded `(x, y)` tuples to their unique stamp IDs (`filled_spots[current_pos] = t.stamp()`). When revisiting a filled cell, `t.clearstamp(filled_spots.pop(current_pos))` removes both the dictionary entry and the visual stamp in a single operation.
* **Batched Frame Rendering:** Uses `screen.tracer(0)` paired with `screen.update()` every `STEPS_PER_FRAME` iterations to bypass per-step GUI repaints, reaching the ~10,000-step highway phase in seconds.

## Requirements & Running

* **Python 3.x** (no external dependencies required—uses only `turtle` and `random` from the standard library)

```bash
python langtons_ant.py
