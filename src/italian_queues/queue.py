from italian_queues.node import Node


class ItalianQueue:
    def __init__(self):
        self._totally_linear_queue = None

    def push(self, value):
        if self._totally_linear_queue is None:
            self._totally_linear_queue = Node(value)
        else:
            self._totally_linear_queue._insert(value)

    def pop(self):
        if self._totally_linear_queue is None:
            raise IndexError("🤌 🤌 🤌")

        being_served = self._totally_linear_queue.value

        if self.left_present() and self.right_present():
            next_in_queue = self._extract_successor()
            self._self_update_queue(next_in_queue)
        elif self.left_present():
            self._totally_linear_queue = self.get_left()
        elif self.right_present():
            self._totally_linear_queue = self.get_right()
        else:
            self._totally_linear_queue = None

        return being_served

    def get_left(self):
        return NotImplemented

    def get_right(self):
        return NotImplemented

    def _extract_successor(self):
        return NotImplemented

    def left_present(self):
        return NotImplemented

    def right_present(self):
        return NotImplemented

    def _self_update_queue(self, next_in_queue):
        return NotImplemented
