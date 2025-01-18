from PIL import Image
import os

def resize_image(input_path, output_path, width=None, height=None):
    try:
        with Image.open(input_path) as img:
            original_width, original_height = img.size
            
            if width and height:
                new_size = (width, height)
            elif width:
                ratio = width / original_width
                new_size = (width, int(original_height * ratio))
            elif height:
                ratio = height / original_height
                new_size = (int(original_width * ratio), height)
            else:
                return "Either width or height must be specified."
            
            resized_img = img.resize(new_size, Image.ANTIALIAS)
            resized_img.save(output_path)
            
            return f"Image resized and saved to {output_path}. New dimensions: {new_size}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the Image Resizer! 🖼️")
    input_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter the path to save the resized image: ").strip()
    width = input("Enter the new width (leave blank if not resizing by width): ").strip()
    height = input("Enter the new height (leave blank if not resizing by height): ").strip()
    
    width = int(width) if width else None
    height = int(height) if height else None
    
    result = resize_image(input_path, output_path, width, height)
    print(result)
