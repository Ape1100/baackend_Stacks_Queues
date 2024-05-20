#queue data structure using a linked list, each node will respresent and order, 
#the front  and rear pointers will track of the head and tail of the queue.

class Order:
    def __init__(self, order_number, items, prep_time):
        self.order_number = order_number
        self.items = items
        self.prep_time = prep_time
        self.next = None

class OrderQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, order_number, items, prep_time):
        new_order = Order(order_number, items, prep_time)
        if self.is_empty():
            self.front = new_order
        else:
            self.rear.next = new_order
        self.rear = new_order

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Business is slow.")
            return None
        else:
            removed_order = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_order

    def display_orders(self):
        current_order = self.front
        while current_order:
            print(f"Order {current_order.order_number}: {current_order.items} | Preparation Time: {current_order.prep_time}")
            current_order = current_order.next

# Examples
kitchen_queue = OrderQueue()
kitchen_queue.enqueue(1, ["Pizza", "Coke"], 20)
kitchen_queue.enqueue(2, ["Burger", "Fries"], 15)
kitchen_queue.enqueue(3, ["Salad", "Water"], 10)

print("Kitchen Order Queue:")
kitchen_queue.display_orders()

print("\nProcessing orders...")
processed_order = kitchen_queue.dequeue()
print(f"\nCompleted Order: {processed_order.order_number}")

print("\nUpdated Kitchen Order Queue:")
kitchen_queue.display_orders()
