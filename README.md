# accountix
Recite ocr for business applications

## Table of Content

## Table of Contents

- [Project Objective](#project-objective)
- [Project Structure](#project-structure)
- [GEMINI](#gemini)
  - [Usage](#usage)
- [GOOGLE VISION](#google-vision)
  - [Usage](#usage-1)
- [Gemini vs Google Vision](#gemini-vs-google-vision)

## Project objective

We are building a platform for accounting people to increase time consuming in manualy trascribing bills into database. The code thakes the recite and translate them into a csv file that can be downloaded.

## Project Structure

- `assets`: Contains the input images
- `GEMINI`: Contains the code to parse the images and save them in a database using Gemini
- `GOOGLE_VISION`: Contains the code to parse the images and save them in a database using Google Vision
- `.env`: Contains the APIs (save them in the form of <NAME>=<your_api>)

## GEMINI

We use `gemini-1.5-pro` to analize recite picture and parse it in to text. Then we extract only the needed columns and save it in a database (Location,Date,Total Price).

Note, to change the model just chnage the name for example go ttry with `gemini-2.0-pro-exp-02-05`.

### Usage

1. Create Gemini API form the website
2. create a `.env` file (in `/accountix` folder) where to store the API key (we will call it in the code). The file should look something like this:

    ```
    GEMINI_API_KEY=<your_key>
    ```

3. Create virtual environment (in same folder where you cloned accountix (`cd ..`)): `python -m venv env`
4. Activate it: `source env/bin/activate`
5. Install dependencies: `pip install opencv-python pandas python-dotenv Pillow google-generativeai`
6. Move to GEMINI directory: `cd /accountix/GEMINI`
7. Run code: `python main_G.py`


## GOOGLE VISION

### usage


<br>
<br>

## Gemini vs GoogleVision

Pros and cons of both the APIs:


| Comparison          | Gemini (Free) | Google Vision (Free) | Gemini (Plus) | Google Vision (Plus) |
|---------------------|--------------|----------------------|--------------|----------------------|
| **Price**          | Free         | Free                 | $X/month     | $Y/month             |
| **Precision**      | High         | Medium               | Higher       | High                 |
| **Requests per Minute (RPM) Before Saturation** | 60  | 180   | 300  | 600  |
| **Premium Plan Cost** | N/A         | N/A                  | $X/month     | $Y/month             |
| **Premium Plan RPM**  | N/A         | N/A                  | 600          | 1200                 |
| **Time to process**   | N/A         | N/A                  | N/A          | N/A                 |
| **Best Use Case**   | Detailed text extraction | Fast bulk processing | High-accuracy extraction | Large-scale processing |

