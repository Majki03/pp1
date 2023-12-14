from queue import Queue

# Create an instance of the Queue class
queue_instance = Queue()

# Add values to the queue
print("Adding values to the queue:")
queue_instance.enqueue(2)
queue_instance.enqueue(5)
queue_instance.enqueue(8)

# Display queue content
print("\nQueue after adding values:")
queue_instance.display()

# Remove values from the queue
print("\nRemoving values from the queue:")
removed_value = queue_instance.dequeue()
if removed_value is not None:
    print(f"Removed value: {removed_value}")
else:
    print("Queue is empty.")

# Display updated queue content
print("\nQueue after removing a value:")