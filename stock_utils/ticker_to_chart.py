from lightweight_charts import Chart
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

def ticker_to_chart(ticker):
    chart = Chart()
    chart.polygon.api_key(POLYGON_API_KEY)
    today_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    chart.polygon.stock(
        symbol=ticker,
        timeframe='5min',
        start_date=today_date
    )
    chart.show(block=True)

# if __name__ == '__main__':
#     create_chart('AAPL')