import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get eraser coordinates
    eraser_coords = canvas.coords(eraser)
    left_x, top_y, right_x, bottom_y = eraser_coords
    
    # Find overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Change color to white for all overlapping objects except the eraser
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='black')

def move_eraser(event, canvas):
    """Move eraser to mouse position and erase"""
    mouse_x, mouse_y = event.x, event.y
    canvas.coords(eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
    erase_objects(canvas, eraser)

def main():
    # Set up the window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Create grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    # Wait for first click to create eraser
    def create_eraser(event):
        global eraser
        eraser = canvas.create_rectangle(
            event.x, event.y, 
            event.x + ERASER_SIZE, event.y + ERASER_SIZE, 
            fill='pink'
        )
        # Bind mouse motion to move eraser after it's created
        canvas.bind('<B1-Motion>', lambda event: move_eraser(event, canvas))
        # Unbind the click event after eraser is created
        canvas.unbind('<Button-1>')

    # Bind the first click to create the eraser
    canvas.bind('<Button-1>', create_eraser)

    # Start the main loop
    root.mainloop()

if __name__ == '__main__':
    main()