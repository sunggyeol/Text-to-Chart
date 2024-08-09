from stock_utils import text_to_ticker, ticker_to_chart

def process_query_and_display_chart(query):
    ticker = text_to_ticker(query)
    print("Ticker:", ticker)
    
    if ticker:
        ticker_to_chart(ticker)
    else:
        print("No ticker found in the query.")
    return ticker

# Example usage
if __name__ == "__main__":
    query = "What is the best electric vehicle company?"
    ticker = process_query_and_display_chart(query)
