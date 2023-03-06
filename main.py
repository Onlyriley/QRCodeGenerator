import os
import qrcode

# Define file locations
INPUT = os.path.join(".", "Input")
OUTPUT = os.path.join(".", "Output")

# Method for creating and saving qr codes
def generate_qr(data):
    qr = qrcode.make(data)
    sequence = 1
    filename = os.path.join(OUTPUT, "QR" + str(sequence) + ".png")
    if os.path.isfile(filename):
        while(os.path.isfile(filename)):
            sequence += 1
            filename = os.path.join(OUTPUT, "QR" + str(sequence) + ".png")
    qr.save(os.path.join(filename))
    print("QR code saved at " + filename)

# Main loop for getting user input and using the generate_qr method
if __name__ == "__main__":
    print("Enter data for QR Code")
    while True:
        data = input("> ")
        generate_qr(data)