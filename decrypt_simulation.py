import base64

# Educational decryption simulation

INPUT_FILE = "encrypted_data.txt"
OUTPUT_FILE = "decrypted_data.txt"

with open(INPUT_FILE, "rb") as file:
    encrypted_data = file.read()

decrypted_data = base64.b64decode(encrypted_data)

with open(OUTPUT_FILE, "wb") as file:
    file.write(decrypted_data)

print("File decrypted (educational simulation).")
