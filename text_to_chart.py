from stock_utils import text_to_ticker, ticker_to_chart

def process_query_and_display_chart(query):
    ticker = text_to_ticker(query)
    print("Ticker:", ticker)
    
    if ticker:
        ticker_to_chart(ticker)
        return ticker
    print("No ticker found in the query.")
    return None

# Example usage
if __name__ == "__main__":
    query = "What is the best telecom service provider?"
    ticker = process_query_and_display_chart(query)
