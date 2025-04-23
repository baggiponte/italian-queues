# Italian Queues

## Installation

Of course, we want to be blazingly fast, so we have to use `uv`.

```bash
uv add https://github.com/baggiponte/italian-queues
```

## Usage

```python
from italian_queues.queue import ItalianQueue

# Test behavior
queue = ItalianQueue()
data = {1, 2, 3}

# Let’s make this Pythonic 🐍
[ _ := queue.push(value) for value in data ]

while data:
    data.remove(queue.pop())
```
