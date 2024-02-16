#Pixel Manipulation for image Encryption

from PIL import Image

def encrypt_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get the pixel data
    pixels = image.load()
    width, height = image.size
    
    # Encrypt the image by applying a basic mathematical operation to each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example: increment each pixel value by 10
            r = (r + 10) % 256
            g = (g + 10) % 256
            b = (b + 10) % 256
            pixels[x, y] = (r, g, b)
            
    # Save the encrypted image
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    image.save(encrypted_image_path)
    print(f"Image encrypted and saved as: {encrypted_image_path}")

def decrypt_image(encrypted_image_path):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    
    # Get the pixel data
    pixels = encrypted_image.load()
    width, height = encrypted_image.size
    
    # Decrypt the image by reversing the mathematical operation applied during encryption
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example: decrement each pixel value by 10
            r = (r - 10) % 256
            g = (g - 10) % 256
            b = (b - 10) % 256
            pixels[x, y] = (r, g, b)
            
    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    encrypted_image.save(decrypted_image_path)
    print(f"Image decrypted and saved as: {decrypted_image_path}")

def main():
    while True:
        print("\nImage Encryption Menu:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit") 
        
        choice = input("Select an option (1, 2, or 3): ")
        
        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            encrypt_image(image_path)
        elif choice == '2':
            encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ")
            decrypt_image(encrypted_image_path)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
