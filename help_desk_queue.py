# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None 
    
    def enqueue(self, value): 
        new_node = Node(value)
        if self.rear: 
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node
        
    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next 
        if self.front is None:
            self.rear = None
        return value 

    def peek(self):
        return self.front.value if self.front else None

    def is_empty(self):
        return self.front is None 
    
    def print_queue(self):
        current = self.front
        if not current: 
            print("No customers in the queue.")
            return
        while current: print(current.value)
        current = current.next
     


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")
            # Add the customer to the queue
            
        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"{customer} has been helped and removed from the queue.")
            else: 
                print("No customers to help.")

            # Help the next customer in the queue and return message that they were helped
           
        elif choice == "3":
            customer = queue.peek()
            if customer: 
                print(f"Next customer: {customer}")
            else: 
                print("No customers waiting")
            # Peek at the next customer in the queue and return their name
        

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
