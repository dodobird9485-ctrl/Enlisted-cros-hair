from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import Canvas
import ctypes

# Create transparent image
img_size = 30
img = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw red dot in center
dot_radius = 5
center = img_size // 2
draw.ellipse(
    [center - dot_radius, center - dot_radius, center + dot_radius, center + dot_radius],
    fill=(255, 0, 0, 255)
)

# Save image
img.save('crosshair_dot.png')

# Create tkinter window
root = tk.Tk()
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')
root.overrideredirect(True)
root.config(bg='black')

# Get screen center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Position at center
x = screen_width // 2 - img_size // 2
y = screen_height // 2 - img_size // 2
root.geometry(f'{img_size}x{img_size}+{x}+{y}')

# Add image to canvas
canvas = Canvas(root, width=img_size, height=img_size, bg='black', highlightthickness=0)
canvas.pack()
canvas.image = tk.PhotoImage(file='crosshair_dot.png')
canvas.create_image(0, 0, image=canvas.image, anchor='nw')

# Make window click-through
try:
    hwnd = root.winfo_id()
    WS_EX_TRANSPARENT = 0x20
    WS_EX_LAYERED = 0x80000
    GWL_EXSTYLE = -20
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, WS_EX_TRANSPARENT | WS_EX_LAYERED)
    ctypes.windll.user32.SetWindowPos(hwnd, -1, x, y, img_size, img_size, 0)
except Exception as e:
    print(f"Error: {e}")

# Bind ESC to close
root.bind('<Escape>', lambda e: root.quit())

root.mainloop()

# Cleanup
import os
os.remove('crosshair_dot.png')
