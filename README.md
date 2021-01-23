# Stock Volatility Bot 

This Python script uses the Alpha Vantage API and the Discord libary to send stock volatility alerts via a Discord bot. 

## How to use:

Add ticker symbols and changing thresholds in percentage in the stock.txt file. The file should follow this **specific** format:

TICKER_SYMBOL PERCENTAGE <br>
TICKER_SYMBOL PERCENTAGE

and so on... 

The script will run every hour and send you a message via Discord if a certain stock has risen above or fallen below the specified threshold. 

**Note:** You need to create a .env file to store API keys. Check out the example_keys.md file to learn more about the format. 
