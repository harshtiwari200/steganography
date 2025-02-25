import cv2
import os

def create_character_maps():
    """Create character maps for encoding and decoding."""
    d = {chr(i): i for i in range(256)}  # Map characters to ASCII values (0-255)
    return d

def encrypt_image(image_path, message, password):
    """Encrypt a message into an image."""
    img = cv2.imread(image_path)  # Read the image

    d = create_character_maps()  # Get character maps

    # Initialize position variables
    n, m, z = 0, 0, 0

    # Embed the secret message into the image
    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    # Save the modified image
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")  # Open the image on Windows

if __name__ == "__main__":
    image_path = "mypic.jpg"  # Replace with the actual image path
    secret_message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Encrypt the message
    encrypt_image(image_path, secret_message, password)
