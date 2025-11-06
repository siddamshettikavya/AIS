from PIL import Image

def compress_image(input_path, output_path, quality=60):
    """
    Compress an image using Pillow.
    input_path: path of the original image
    output_path: path to save the compressed image
    quality: compression quality (1–100)
    """
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)
    print(f"Image saved at {output_path} with {quality}% quality.")

if __name__ == "__main__":
    print("Pillow is installed and ready!")
    print("\nImage compression function is available.")
    print("Usage: compress_image('input.jpg', 'compressed.jpg', quality=50)")
    print("\nNote: To compress an image, provide valid image file paths.")
