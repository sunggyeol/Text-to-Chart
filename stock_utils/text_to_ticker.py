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
        f"Extract a single stock ticker from the following query: '{query}'. "
        "The ticker can be a US stock ticker (1-5 uppercase letters) or a Korean stock ticker (e.g., numeric code or alphanumeric). "
        "If a ticker is explicitly mentioned, return that ticker. If no ticker is mentioned, provide the ticker of the most relevant company associated with the query. "
        "For example, if the query is about smartphones, you might return Apple (AAPL) if no other ticker is mentioned. "
        "If the query is about refrigerators, you might return Samsung (005930) or LG (066570). "
        "If there are multiple relevant tickers, provide only one ticker."
    )

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
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
