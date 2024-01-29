# external_file.py

from trial import ListLabelApp
import time

# Create an instance of ListLabelApp
app = ListLabelApp()

# Function to update items from another file
def update_items_from_external():
    new_items = ["Updated Item 1", "Updated Item 2", "Updated Item 3", "Updated Item 4", "Updated Item 5"]
    app.update_items_external(new_items)

# Call the update_items_from_external function
update_items_from_external()

# You can continue to call this function as needed
# For example, you might call it periodically in a loop or in response to some event
while True:
    # Update items every 5 seconds (for demonstration purposes)
    time.sleep(5)
    update_items_from_external()
