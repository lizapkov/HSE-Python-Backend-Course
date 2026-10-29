from typing import List
from models.product import Product

def extract_prices(products: List[Product]) ->  List[float]:
    prices = list(map(lambda product: product.get_price(), products))
    return prices
