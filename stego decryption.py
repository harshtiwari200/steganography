import cv2
import string

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct image path

# Initialize dictionaries for encoding and decoding
d = {}
c = {}

# Populate dictionaries with ASCII characters in the range 0-254
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Ask for the passcode (no predefined passcode)
pas = input("Enter passcode for Decryption: ")

# Load the same passcode used during encryption (this should be the same as encryption passcode)
encryption_passcode = input("Enter the passcode used for encryption: ")

# Decrypt the message if the passcode matches
if pas == encryption_passcode:
    message = ""
    n = 0
    m = 0
    z = 0

    # Loop through the image and decode the secret message
    while n < img.shape[0] and m < img.shape[1]:
        pixel_value = img[n, m, z]  # Extract pixel value at [n, m] for channel z

        # Ensure pixel_value is within the valid range (0-254) to match the dictionary
        if pixel_value < 255:
            try:
                message += c[pixel_value]  # Decode using the dictionary
            except KeyError:
                message += '?'  # Placeholder for invalid pixel values
        else:
            message += '?'  # Placeholder for any unexpected pixel value outside the range

        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Iterate through the 3 color channels: B, G, R

        # If we have reached the end of the row, move to the next row
        if m == img.shape[1]:
            m = 0
            n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
