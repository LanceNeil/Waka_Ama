import tkinter as tk
"""
# Function to handle button click
def on_button_click():
    # Replace with your logic
    print("Button clicked!")
    """
class gui_c():
    def __init__(self):
        self.root = tk.Tk()
        
        root = self.root
        self.parent_path_input = tk.Entry(root)
        
        
        self.year_input = tk.Entry(root)
        
        
        self.keyword_input = tk.Entry(root)
        
        
        self.export_option = tk.Entry(root)
        
        
        
        
    def open_gui(self,function):
        # Create the main window
        root = self.root
        root.title("Scoring System GUI")

        # Set the size of the main window
        root.geometry("400x300")  # Increase the height to accommodate the button

        #Canvas
        canvas = tk.Canvas(root, width=400, height=150)
        canvas.pack()

        # Draw a rectangle (you can change this to any shape you want)
        canvas.create_rectangle(50, 50, 350, 150, fill='lightblue')

        # Add text on top of the rectangle
        canvas.create_text(200, 100, text="Waka Ama", font=("Arial", 24))
        
        # Create input for parent path
        self.parent_path_input = tk.Entry(root)
        self.parent_path_input.pack()
        
        
        # Create input for year
        self.year_input = tk.Entry(root)
        self.year_input.pack()
        
        # Create input for keyword
        self.keyword_input = tk.Entry(root)
        self.keyword_input.pack()
        
        # Create input for export to csv
        self.export_option = tk.Entry(root)
        self.export_option.pack()
        
        # Create a button
        button = tk.Button(root, text="Proceed", command=function, width=20, height=2, font=("Arial", 16))
        button.place(x=75, y=175)

        # Run the main event loop
        root.mainloop()