import tkinter as tk
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the root window, we just need the dialog

# Show a confirmation dialog
response = messagebox.askyesno("Confirm", "Do you want to proceed?")

# Check the response
if response:  # If the response is Yes
    print("You chose Yes.")
else:  # If the response is No
    print("You chose No.")

#root.mainloop()  # Start the Tkinter event loop (necessary for the window to stay open)
