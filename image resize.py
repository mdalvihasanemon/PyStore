from PIL import Image

def resize_image(input_file, output_file, width, height):
    with Image.open(input_file) as img:
        img = img.resize((width, height))
        img.save(output_file)
        print(f"Resized image saved as {output_file}")

resize_image("input.jpg", "output.jpg", 800, 600)
