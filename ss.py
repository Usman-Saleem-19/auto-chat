#https://pythonguides.com/python-screen-capture/
from PIL import ImageGrab

# change the region according to your screen, and to where the real person message is seen on the screen 
def capture_region_pil(left = 680, top = 775, right = 1200, bottom = 940, fname = "ss.png"):
    """
    Captures a specific region of the screen
    Args:
        left (int): Left coordinate
        top (int): Top coordinate  
        right (int): Right coordinate
        bottom (int): Bottom coordinate
    """

    # Define the region to capture (left, top, right, bottom)
    bbox = (left, top, right, bottom)

    # Capture the specified region
    screenshot = ImageGrab.grab(bbox)

    # Generate filename
    filename = fname

    # Save the screenshot
    screenshot.save(filename, "PNG")
    print(f"Region screenshot saved as: {filename}")

#capture_region_pil()