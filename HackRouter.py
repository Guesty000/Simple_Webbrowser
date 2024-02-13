import tkinter as tk
import webbrowser

# Create the main window
root = tk.Tk()
root.title("Simple Browser")

# Create an entry field for the URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=10)

# Create a button to load the URL
def load_url():
    url = url_entry.get()
    webbrowser.open(url)
    
load_button = tk.Button(root, text="Go", command=load_url)
load_button.pack()

# Create a menu bar
menu_bar = tk.Menu(root)

# Add a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Window")
file_menu.add_command(label="Open File...")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add an edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add the menu bar to the window
root.config(menu=menu_bar)

# Set the background color of the window
root.config(bg="#000000")

# Add padding and margin around widgets
url_entry.pack(padx=10, pady=10)
load_button.pack(pady=10)

# Run the application
root.mainloop()
