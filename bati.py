# Name: Bati Jano
# Id: UGR/30230/15
# section: 20

# Import the Image module from the Pillow library
from PIL import Image
import os  # Import os for robust path handling

# --- Configuration ---
input_filename = "bati.jpg"
output_basename = "bati_processed" # Base name for output files
# -------------------

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the input image
image_path = os.path.join(script_dir, input_filename)

# Define output filenames using the script directory
red_output_path = os.path.join(script_dir, f"{output_basename}_red.jpg")
green_output_path = os.path.join(script_dir, f"{output_basename}_green.jpg")
blue_output_path = os.path.join(script_dir, f"{output_basename}_blue.jpg")
gray_output_path = os.path.join(script_dir, f"{output_basename}_gray.jpg")
inverted_output_path = os.path.join(script_dir, f"{output_basename}_inverted.jpg")

try:
    # Load the image using Pillow
    # .convert("RGB") ensures it's in RGB format, even if it was grayscale or RGBA
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    print(f"Loaded image '{input_filename}' ({w}x{h})")

    # Create new blank images for color channels (mode "RGB", size (w, h))
    red_img = Image.new("RGB", (w, h))
    green_img = Image.new("RGB", (w, h))
    blue_img = Image.new("RGB", (w, h))

    # Create new blank image for grayscale (mode "L" is 8-bit grayscale)
    gray_img = Image.new("L", (w, h))

    # Get pixel access objects for faster manipulation (recommended)
    original_pixels = img.load()
    red_pixels = red_img.load()
    green_pixels = green_img.load()
    blue_pixels = blue_img.load()
    gray_pixels = gray_img.load()

    print("Processing pixel data...")
    # Loop through pixels
    for x in range(w):
        for y in range(h):
            # Get original RGB values using the pixel access object
            r, g, b = original_pixels[x, y]

            # Set pixels for color channel images
            red_pixels[x, y] = (r, 0, 0)
            green_pixels[x, y] = (0, g, 0)
            blue_pixels[x, y] = (0, 0, b)

            # Calculate grayscale value using the formula
            gscale = int(0.2989 * r + 0.5890 * g + 0.01140 * b)
            # Clamp value just in case (though formula usually stays in range)
            gscale = max(0, min(255, gscale))
            # Set pixel in grayscale image
            gray_pixels[x, y] = gscale

    # --- Show and Save Color Channels ---
    print(f"Saving Red channel to {red_output_path}")
    red_img.show(title="Red Channel")
    red_img.save(red_output_path)

    print(f"Saving Green channel to {green_output_path}")
    green_img.show(title="Green Channel")
    green_img.save(green_output_path)

    print(f"Saving Blue channel to {blue_output_path}")
    blue_img.show(title="Blue Channel")
    blue_img.save(blue_output_path)

    # --- Show and Save Grayscale Image ---
    print(f"Saving Grayscale image to {gray_output_path}")
    gray_img.show(title="Grayscale")
    # Convert grayscale ('L' mode) to 'RGB' before saving as JPG for better compatibility
    gray_img.convert("RGB").save(gray_output_path)

    # --- Invert the Grayscale Image ---
    print("Inverting grayscale image...")
    # Create a new image for the inverted result
    inv_img = Image.new("L", (w, h))
    inv_pixels = inv_img.load()

    for x in range(w):
        for y in range(h):
            # Get the grayscale value we calculated earlier
            gscale_val = gray_pixels[x, y]
            # Calculate inverted value
            inv_val = 255 - gscale_val
            inv_pixels[x, y] = inv_val

    # --- Show and Save Inverted Image ---
    print(f"Saving Inverted image to {inverted_output_path}")
    inv_img.show(title="Inverted Grayscale")
    # Convert inverted grayscale ('L' mode) to 'RGB' before saving as JPG
    inv_img.convert("RGB").save(inverted_output_path)

    print("Processing complete.")

except FileNotFoundError:
    print(f"Error: Input image file not found at '{image_path}'")
    print("Please ensure 'bati.jpg' is in the same directory as the script.")
except Exception as e:
    # Catch other potential errors (e.g., issues with Pillow, invalid image)
    print(f"An unexpected error occurred: {e}")