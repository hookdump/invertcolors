import sys
import argparse
from PIL import Image

def invert_colors(image_path, output_path):
    try:
        image = Image.open(image_path).convert("RGBA")
        inverted_image = Image.new("RGBA", image.size)
        for x in range(image.width):
            for y in range(image.height):
                r, g, b, a = image.getpixel((x, y))
                inverted_color = (255 - r, 255 - g, 255 - b, a)
                inverted_image.putpixel((x, y), inverted_color)
        inverted_image.save(output_path)
        print(f"Inverted image saved to: {output_path}")
    except FileNotFoundError:
        print("Error: Input image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Invert colors of a PNG image while preserving transparency.")
    parser.add_argument("input", help="Input PNG file path")
    parser.add_argument("output", help="Output file path for the inverted image")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    invert_colors(input_path, output_path)

if __name__ == "__main__":
    main()

