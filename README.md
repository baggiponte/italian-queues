# Italian Queues

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
