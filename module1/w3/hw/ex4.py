from typing import Any


class MyQueue:

  def __init__(self, capacity: int) -> None:
    if capacity <= 0:
      raise ValueError("Capacity must be greater than 0")
    self.capacity = capacity
    self.data = []

  def is_empty(self) -> bool:
    return len(self.data) == 0

  def is_full(self) -> bool:
    return len(self.data) == self.capacity

  def dequeue(self) -> Any:
    if self.is_empty():
      return None
    return self.data.pop(0)

  def enqueue(self, value: Any) -> None:
    if self.is_full():
      print("Queue is full!")
      return
    self.data.append(value)

  def front(self) -> Any:
    if self.is_empty():
      return None
    return self.data[0]


def main() -> None:
    queue1 = MyQueue(capacity=5)

    queue1.enqueue(1)

    queue1.enqueue(2)

    print(queue1.is_full())
    # >> False

    print(queue1.front())
    # >> 1

    print(queue1.dequeue())
    # >> 1

    print(queue1.front())
    # >> 2

    print(queue1.dequeue())
    # >> 2

    print(queue1.is_empty())
    # >> True

if __name__ == "__main__":
    main()