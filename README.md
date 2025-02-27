# accountix
Recite ocr for business applications

## Project objective

We are building a platform for accounting people to increase time consuming in manualy trascribing bills into database. The code thakes the recite and translate them into a csv file that can be downloaded.

## GEMINI

We use `gemini-1.5-pro` to analize recite picture and parse it in to text. Then we extract only the needed columns and save it in a database (Location,Date,Total Price).

Note, to change the model just chnage the name for example go ttry with `gemini-2.0-pro-exp-02-05`.

### Usage

1. Create Gemini API form the website
2. create a `.env` file where to store the API key (we will call it in the code). The file should look something like this:

    ```
    GEMINI_API_KEY=<your_key>
    ```

3. Create virtual environment: `python -m venv env`
4. Activate it: `source env/bin/activate`
5. Install dependencies: `pip install opencv-python pandas python-dotenv Pillow google-generativeai`
6. Run code: `python scontrini.py`


## GOOGLE VISION