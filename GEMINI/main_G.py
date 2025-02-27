import os
import cv2 # pip install opencv-python
import pandas as pd # pip install pandas
from dotenv import load_dotenv # pip install python-dotenv
from PIL import Image as PIL_Image # pip install Pillow
import google.generativeai as genai # pip install google-generativeai

# Load environment variables
load_dotenv()
GEMINI_API = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel("gemini-1.5-pro")

# Load image
image = cv2.imread("../assets/scontrino0.jpg")  # Use cropped image if necessary
image = PIL_Image.fromarray(image)  # Convert cv2 image to PIL Image

# Prepare prompt
prompt = """
    Give me only the necessary words image output classes, separated by a dash (-):
    Location, Shop, Date, Total Final Price, IVA.
    (note that the location have to be the specific address of the shop, usualy starting with 'via' or 'piazza' or 'viale' or etc...)
    (note that the shop is the name of the place, and usualy is between 1 - 3 words)
    (note that the date have to be in the format DD/MM/YYYY)
    (note that the total final price have to be in the format X.XX)
    (note that the IVA usualy is a number of 11 digits)
"""
contents = [image, prompt]

# Get response
response = model.generate_content(contents)

print("\n-------Response--------")
print(response.text)

# Define CSV file path
csv_file = "bilancio_G.csv"

# Parse extracted response
try:
    location, shop, date, total_price, iva = response.text.split("-")
    data_dict = {"Location": location, "Shop": shop, "Date": date, "Total Price": total_price, "IVA": iva}
except ValueError:
    print("Error: Could not parse the response. Ensure the format is 'Location, Date, Total Price'.")
    exit()

# Check if file exists and append data
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)  # Use pd.concat()
else:
    df = pd.DataFrame([data_dict])

# Save the updated CSV
df.to_csv(csv_file, index=False)
print(f"Data appended to {csv_file} successfully!")
