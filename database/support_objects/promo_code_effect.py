from .base_json import BaseJson
from typing import Optional, List
from database.models import Product


class PromoCodeEffect(BaseJson):

    def __init__(self, min_sum: Optional[int] = None,
                 max_sum: Optional[int] = None,
                 products: Optional[List] = list()):
        self.min_sum = min_sum
        self.max_sum = max_sum
        self.products = products

    def is_valid(self, product: Product) -> bool:
        if self.min_sum <= product.cost <= self.max_sum:
            if product.name in self.products or 'ANY' in self.products:
                return True
        return False
