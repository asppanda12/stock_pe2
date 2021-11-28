import finnhub
finnhub_client = finnhub.Client(api_key="c6hp3bqad3ia9lmm14j0")

print(finnhub_client.stock_symbols('NSE:NTPC'))
