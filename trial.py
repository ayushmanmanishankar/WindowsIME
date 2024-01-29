import tkinter as tk
import time

class ListLabelApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("List Label Example")
        self.root.overrideredirect(True)

        # List of items
        self.items = []

        # Create a label with the list items
        self.label_text = "\n".join(self.items)
        self.label = tk.Label(self.root, text=self.label_text, padx=20, pady=20, font=("Arial", 12), anchor="w", wraplength=300)
        self.label.pack()

    def update_items(self,items):
        # Delete all items from the list
        self.items = items
        self.update_label()

    def update_label(self):
        # Update the label with the current list items
        self.label_text = "\n".join(self.items)
        self.label.config(text=self.label_text)

    def run(self):
        time.sleep(5)
        self.root.mainloop()

    def apply_border_around_first_item(self):
        # Apply border around the first item
        self.label.config(borderwidth=1, relief="solid")

# Create an instance of ListLabelApp and run the application
app = ListLabelApp()
app.update_items(["2","3"])
app.run()