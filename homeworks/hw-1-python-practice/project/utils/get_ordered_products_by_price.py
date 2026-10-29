from models.product import Product
from typing import List

def get_ordered_products_by_price(products: List[Product]) -> List[Product]:
    ordered_products_price = sorted(products, key = lambda product: product.get_price(), reverse = True)
    return ordered_products_price
