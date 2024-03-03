
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, new_elememt):
        self.items.insert(0, new_elememt)

    def pop(self):
        if not self.is_empty():
            self.items.pop(0)
            return "O'chirildi"

        else:
            return "O'chirish uchun element topilmadi"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Stack bo'sh"

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print("Stekni bo'shlikka tekshirish: ", stack.is_empty())
    stack.push(9)
    print("Stekni bo'shlikka tekshirish: ", stack.is_empty())
    print("Stack elementlari: ", *stack.items)
    stack.push(0)
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(8)
    print("Stack elementlari: ", *stack.items)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print("O'chirilgandan so'ng stack elementlari: ", *stack.items)
    print("Stack elementlar soni: ", stack.size())
