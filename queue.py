
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_element(self, new_element):
        self.items.append(new_element)

    def delete_element(self):
        if not self.is_empty():
            self.items.pop()
            return "Qo'shildi"
        else:
            return "stack bosh"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "stack bosh"

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    print("queue bo'shlikka tekshirish: ", queue.is_empty())
    queue.add_element(9)
    print("queue bo'shlikka tekshirish: ", queue.is_empty())
    print("queue elementlari: ", *queue.items)
    queue.add_element(0)
    queue.add_element(3)
    queue.add_element(5)
    queue.add_element(2)
    queue.add_element(8)
    print("queue elementlari: ", *queue.items)
    queue.delete_element()
    queue.delete_element()
    queue.delete_element()
    queue.delete_element()
    print("O'chirilgandan so'ng queue elementlari: ", *queue.items)
    print("queue elementlar soni: ", queue.size())

