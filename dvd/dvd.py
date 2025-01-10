import tkinter as tk

# Image path
image_path = "dvd.png"

# Create the root window
root = tk.Tk()

# Use fullscreen to get screen dimensions
root.attributes("-fullscreen", True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes("-fullscreen", False)

# Transparent and decoration-free window
root.overrideredirect(True)
root.attributes("-transparentcolor", "black")
root.attributes("-topmost", True)
root.configure(bg="black")

# Load and scale the image to 30%
original_image = tk.PhotoImage(file=image_path)
scaled_image = original_image.subsample(3)  # Scale to 30%
image_width, image_height = scaled_image.width(), scaled_image.height()

# Canvas to display the image
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
canvas.pack()

# Add the image to the canvas
image_id = canvas.create_image(screen_width // 2, screen_height // 2, anchor=tk.NW, image=scaled_image)

# Speed and initial position
x, y = screen_width // 2, screen_height // 2
speed_x, speed_y = 4, 4

def apply_color_filter(image, blue_scale):
    """Applies a blue filter to the image using pixel manipulation."""
    new_image = tk.PhotoImage(width=image.width(), height=image.height())
    for x in range(image.width()):
        for y in range(image.height()):
            pixel = image.get(x, y)
            if pixel != (0, 0, 0):  # Skip transparent pixels
                r, g, b = map(int, pixel.split())
                b = min(255, int(b * blue_scale))  # Scale blue component
                new_pixel = f"#{r:02x}{g:02x}{b:02x}"
                new_image.put(new_pixel, (x, y))
    return new_image

def update():
    global x, y, speed_x, speed_y

    # Update position
    x += speed_x
    y += speed_y

    # Bounce off the edges
    if x <= 0 or x + image_width >= screen_width:
        speed_x = -speed_x
    if y <= 0 or y + image_height >= screen_height:
        speed_y = -speed_y

    # Move the image
    canvas.move(image_id, speed_x, speed_y)

    # Schedule the next frame
    root.after(10, update)

def open_settings(event=None):
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x250")  # Adjust window size to fit all widgets
    settings_window.resizable(False, False)
    settings_window.attributes("-topmost", True)

    def update_speed():
        global speed_x, speed_y
        try:
            new_speed = int(speed_input.get())
            speed_x = speed_y = new_speed
        except ValueError:
            pass

    def apply_blue_filter():
        global scaled_image, image_id
        try:
            scale = float(blue_scale_input.get())
            scaled_image = apply_color_filter(original_image, scale)
            canvas.itemconfig(image_id, image=scaled_image)
        except ValueError:
            pass

    def start_at_center_and_hit_corner():
        global x, y, speed_x, speed_y
        # Set the initial position to the center
        x, y = screen_width // 2, screen_height // 2

        # Define the target corner (bottom right)
        target_x, target_y = screen_width - image_width, screen_height - image_height

        # Calculate speeds to make it hit the bottom-right corner
        speed_x = (target_x - x) // 30  # Adjust speed to achieve the target position
        speed_y = (target_y - y) // 30  # Adjust speed to achieve the target position

        # Set a good initial position for bouncing (center)
        canvas.coords(image_id, x, y)

    # Speed input
    tk.Label(settings_window, text="Speed:").pack(pady=5)
    speed_input = tk.Entry(settings_window)
    speed_input.insert(0, str(abs(speed_x)))
    speed_input.pack(pady=5)
    tk.Button(settings_window, text="Update Speed", command=update_speed).pack(pady=5)

    # Blue filter input
    tk.Label(settings_window, text="Blue Filter Scale (0.1 - 2.0):").pack(pady=5)
    blue_scale_input = tk.Entry(settings_window)
    blue_scale_input.insert(0, "1.0")
    blue_scale_input.pack(pady=5)
    tk.Button(settings_window, text="Apply Blue Filter", command=apply_blue_filter).pack(pady=5)

    # Button to start the movement from the center and hit the corner
    tk.Button(settings_window, text="Start at Center & Hit Corner", command=start_at_center_and_hit_corner).pack(pady=10)

# Bind mouse click on the image to open the settings
canvas.tag_bind(image_id, "<Button-1>", open_settings)

# Exit program with Escape key
def close(event):
    root.destroy()

root.bind("<Escape>", close)

# Start the animation loop
update()

# Run the application
root.mainloop()
