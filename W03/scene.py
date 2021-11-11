import tkinter as tk
import random

def main():
    # The width and height of the scene window.
    width = 1600
    height = 900

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # tree_center = scene_left + 500
    # tree_top = scene_top + 100
    # tree_height = 150
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    draw_sky(canvas, scene_left, scene_top, scene_height, scene_width, "dark orange")
    scene_center_x = (scene_width - 1) / 2
    scene_center_y = (scene_height - 1) / 2
    scene_quarter_y = scene_center_y + scene_height / 4
    draw_sun(canvas, scene_center_x, scene_quarter_y, 300, 300, "yellow")
    ocean_top_y = int(scene_quarter_y)
    draw_ocean(canvas, scene_left, scene_right, ocean_top_y, scene_bottom)
    cloud_bottom = int(scene_center_y)
    draw_cloud(canvas, scene_left, scene_top, scene_right, cloud_bottom)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
# EXAMPLE
# def draw_pine_tree(canvas, peak_x, peak_y, height):
#     """Draw a single pine tree.
#     Parameters
#         canvas: The tkinter canvas where this
#             function will draw a pine tree.
#         peak_x, peak_y: The x and y location in pixels where
#             this function will draw the top peak of a pine tree.
#         height: The height in pixels of the pine tree that
#             this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = peak_x - trunk_width / 2
#     trunk_right = peak_x + trunk_width / 2
#     trunk_bottom = peak_y + height

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = peak_x - skirt_width / 2
#     skirt_right = peak_x + skirt_width / 2
#     skirt_bottom = peak_y + skirt_height

#     # Draw the trunk of the pine tree.
#     canvas.create_rectangle(trunk_left, skirt_bottom,
#             trunk_right, trunk_bottom,
#             outline="gray20", width=1, fill="tan3")

#     # Draw the crown (also called skirt) of the pine tree.
#     canvas.create_polygon(peak_x, peak_y,
#             skirt_right, skirt_bottom,
#             skirt_left, skirt_bottom,
#             outline="gray20", width=1, fill="dark green")

def draw_sky(canvas, x, y, height, width, color):
    """Draw the sky
    Parameters
        canvas: the tkinter canvas where this function will draw the sky
        x: left location of sky
        y: top location of sky
        height: height of sky in window
        width: width of sky in window
        color: color of sky
    Return: nothing
    """
    x1 = x + width
    y1 = y + height
    canvas.create_rectangle(x, y, x1, y1, fill = color, outline = color)

def draw_sun(canvas, x_center, y_center, height, width, color):
    """Draw the sun
    Parameters
        canvas:
        x_center:
        y_center:
        height:
        width: 
    Return: nothing
    """
    x = x_center - width / 2
    y = y_center - height / 2
    x1 = x_center + width / 2
    y1 = y_center + height / 2
    canvas.create_oval(x, y, x1, y1, fill = color, outline = color)

def draw_triangle_wave(canvas, center_x, center_y, radius, color):
    """Draw a blue-ish triangle that represents wave
    Parameters
        canvas:
        center_x:
        center_y:
        color:
    Return: nothing
    """
    x = center_x
    y = center_y - radius
    x1 = center_x - radius
    y1 = center_y
    x2 = center_x + radius
    y2 = center_y
    canvas.create_polygon(x, y, x1, y1, x2, y2, fill = color)

def draw_ocean(canvas, left_x, right_x, top_y, bottom_y):
    """Draw the ocean
    Parameters
        canvas:
    Return: nothing
    """
    for i in range(10000):
        x = random.randint(left_x, right_x)
        y = random.randint(top_y, bottom_y)
        radius = random.randint(10, 50)
        draw_triangle_wave(canvas, x, y, radius, "blue")

def draw_randomized_oval(canvas, center_x, center_y, color):
    """Randomize the oval for the cloud
    Parameters
    Return: nothing
    """
    for i in range(10):
        x = -1 * random.randint(0, 50) + center_x
        y = -1 * random.randint(0, 50) + center_y
        x1 = random.randint(0, 50) + center_x
        y1 = random.randint(0, 50) + center_y
        canvas.create_oval(x, y, x1, y1, fill = color, outline = color)

def draw_cloud(canvas, left_x, top_y, right_x, bottom_y):
    """Draw a cloud
    Parameters
        canvas:
    Return: nothing
    """
    iii = random.randint(0, 20)
    for i in range(iii):
        center_x = random.randint(left_x, right_x)
        center_y = random.randint(top_y, bottom_y)
        draw_randomized_oval(canvas, center_x, center_y, "pink")

# Call the main function so that
# this program will start executing.
main()