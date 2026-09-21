class Stack:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def is_full(self) -> bool:
        return self.capacity == len(self.data)

    def pop(self) -> any:
        remove_data = self.data.pop()
        return remove_data

    def push(self,value:any) -> None:
        if self.is_full():
            print("Full")
            return
        self.data.append(value)

    def top(self) ->any:
        top_element = self.data[-1]
        return top_element

    