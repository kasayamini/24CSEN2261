class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)  
        new_node.next = self.top 
        self.top = new_node  

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_node = self.top  
        self.top = self.top.next 
        return popped_node.data  

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Current stack:")
    stack.display()

    print("Top element:", stack.peek())

    print("Popped element:", stack.pop())

    print("Stack after popping an element:")
    stack.display()

    print("Is the stack empty?", stack.is_empty())

    print("Popped elements:")
    print(stack.pop()) 
    print(stack.pop())  

    print("Stack after popping all elements:")
    stack.display()

    print("Is the stack empty?", stack.is_empty())



OUTPUT :
Current stack:
40 -> 30 -> 20 -> 10 -> None
Top element: 40
Popped element: 40
Stack after popping an element:
30 -> 20 -> 10 -> None
Is the stack empty? False
Popped elements:
30
20
Stack after popping all elements:
10 -> None
Is the stack empty? False
