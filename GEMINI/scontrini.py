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
image = cv2.imread("../assets/scontrino2.jpg")  # Use cropped image if necessary
image = PIL_Image.fromarray(image)  # Convert cv2 image to PIL Image

# Prepare prompt
prompt = "Give me only 3 words for this image output: Location, Date, Total Final Price. (note that the location have to be specific, only the city is not enough)"
contents = [image, prompt]

# Get response
response = model.generate_content(contents)

print("\n-------Response--------")
print(response.text)

# Define CSV file path
csv_file = "bilancio.csv"

# Parse extracted response
try:
    location, date, total_price = response.text.split(", ")
    data_dict = {"Location": location, "Date": date, "Total Price": total_price}
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
