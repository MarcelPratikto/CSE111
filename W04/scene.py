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
    # calculate position of sky then draw it    
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    draw_sky(canvas, scene_left, scene_top, scene_height, scene_width, "dark orange")
    # calculate position of the sun the draw it
    scene_center_x = (scene_width - 1) / 2
    scene_center_y = (scene_height - 1) / 2
    scene_quarter_y = scene_center_y + scene_height / 4
    sun_x = scene_center_x
    sun_y = scene_quarter_y    
    sun_height = 300
    sun_width = 300
    sun_position = draw_sun(canvas, sun_x, sun_y, sun_height, sun_width, "yellow")
    # calculate position of ocean then draw it
    ocean_top_y = int(scene_quarter_y)
    draw_ocean(canvas, scene_left, scene_right, ocean_top_y, scene_bottom, sun_position)
    # calculate position of cloud then draw it
    cloud_bottom = int(scene_center_y)
    draw_cloud(canvas, scene_left, scene_top, scene_right, cloud_bottom)

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
    Return: an array of the position of the sun
    """
    x = x_center - width / 2
    y = y_center - height / 2
    x1 = x_center + width / 2
    y1 = y_center + height / 2
    canvas.create_oval(x, y, x1, y1, fill = color, outline = color)
    position = [x, y, x1, y1]
    return position

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

def draw_ocean(canvas, left_x, right_x, top_y, bottom_y, sun_position):
    """Draw the ocean
    Parameters
        canvas:
    Return: nothing
    """
    for i in range(10000):
        x = random.randint(left_x, right_x)
        y = random.randint(top_y, bottom_y)
        radius = random.randint(10, 50)
        # turn orange if it's in the position of the sunset
        # otherwise, wave color is blue
        sun_x = sun_position[0]
        sun_y = sun_position[1]
        sun_x1 = sun_position[2]
        sun_y1 = sun_position[3]
        if x >= sun_x and x <= sun_x1:
            chance = random.randint(0, 100)
            if chance > 75:
                draw_triangle_wave(canvas, x, y, radius, "blue")
            else:    
                draw_triangle_wave(canvas, x, y, radius, "orange")
        else:
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