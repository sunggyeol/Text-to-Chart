import openai
import re
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the .env file
load_dotenv()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def text_to_ticker(query):
    # Define the prompt to guide the model
    prompt = (
        f"Identify and extract a single US stock ticker from the given query: '{query}'. "
        "A US stock ticker consists of 1-5 uppercase letters (e.g., 'AAPL'). "
        "If a specific ticker is explicitly mentioned in the query, return that ticker. "
        "If no explicit ticker is mentioned, determine the most relevant company related to the query's context. "
        "For example, if the query involves smartphones, return 'AAPL' for Apple if no other ticker is specified. "
        "Ensure that a ticker is identified and returned even if it is not directly mentioned in the query. "
        "The output should be a single ticker in the format 'AAPL'."
    )
    
    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a stock ticker extraction model."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=15
    )
    
    # Extract the response
    message = response.choices[0].message.content.strip()
    
    # Regex for US and Korean stock tickers
    # US stock tickers: 1-5 uppercase letters
    # Korean stock tickers: 6-digit numeric or alphanumeric (example: KOSDAQ ticker)
    ticker = re.findall(r'\b[A-Z]{1,5}\b|\b\d{6}\b', message)
    
    # Return the first ticker or None if no ticker found
    return ticker[0] if ticker else None

# # Example usage
# if __name__ == "__main__":
#     query = "What is the best memory company?"
#     ticker = extract_one_ticker_from_gpt(query)
#     if ticker:
#         print(ticker)
#     else:
#         print("No ticker found.")
