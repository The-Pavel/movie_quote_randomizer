import requests

def get_quote():
  quote = requests.get("https://movie-quote-api.herokuapp.com/v1/quote/").json()
  return f"'{quote.get('quote')}' -- {quote.get('role')} ({quote.get('show')})"


if __name__ == '__main__':
  print(get_quote())
