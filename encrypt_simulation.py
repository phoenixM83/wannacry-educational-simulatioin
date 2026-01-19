import base64

# Educational encryption simulation
# This code does NOT encrypt real system files

INPUT_FILE = "sample_data.txt"
OUTPUT_FILE = "encrypted_data.txt"

with open(INPUT_FILE, "rb") as file:
    original_data = file.read()

encrypted_data = base64.b64encode(original_data)

with open(OUTPUT_FILE, "wb") as file:
    file.write(encrypted_data)

print("File encrypted (educ
