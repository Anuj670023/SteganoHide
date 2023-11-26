import cv2
import os
img_path = "C:\\Users\\azur0\\OneDrive\\Desktop\\Project\\Screenshot 2023-11-22 131844.PNG"
img = cv2.imread(img_path)
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
m = 0
n = 0
z = 0
# Encrypt the secret message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3
cv2.imwrite("EncryptedImage.png", img)
os.system("start EncryptedImage.png")
message = ""
n = 0
m = 0
z = 0
# Get the passcode for decryption
pas = input("Enter passcode for Decryption: ")
# Check if the passcode is correct
if password == pas:
    # Decrypt the message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
