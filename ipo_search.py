import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from datetime import datetime, timedelta
# Load environment variables
load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Please set GOOGLE_API_KEY in your .env file")

# Configure the API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def search_latest_ipos(time, next_fourth_day):


    try:
        # Create a prompt to search for latest IPOs in India
        prompt = """
            You are a financial markets research assistant.
            Search for the latest mainboard IPOs in India with the following filters and return the data in JSON format only:
            Do Live Search for IPOs that are currently live as of {time} or that will open within the next 4 days (i.e., between {time} and {next_fourth_day}).

            For each IPO that meets the criteria, return the following fields:

            Company Name

            IPO Open Date

            IPO Close Date

            Price Band (in INR)

            Lot Size

            One Lot Price (calculated as Lot Size × lower bound of Price Band)

            Grey Market Premium (GMP)

            Price After Grey Market (calculated as lower bound of Price Band ± GMP)

            Issue Size (in ₹ crores)

            Status: Live or Upcoming

            Output must be structured as pure JSON — no extra explanation or formatting.


        """
        # print(prompt)
        # Generate response
        response = model.generate_content(prompt)

        return response.text
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    time = datetime.now().strftime("%d %B %Y")
    next_fourth_day = (datetime.now() + timedelta(days=4)).strftime("%d %B %Y")
    # print(time, next_fourth_day)
    response = search_latest_ipos(time, next_fourth_day)    
    print(response)
    response_text = response.strip()  # Trim any leading or trailing whitespace
    if response_text.startswith("```json"):
        response_text = response_text[7:]  # Remove the starting ```json
    if response_text.endswith("```"):
        response_text = response_text[:-3]  # Remove the ending ```
    response = response_text
    # Parse the JSON response
    try:
        ipos = json.loads(response)
        print(ipos)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {str(e)}")