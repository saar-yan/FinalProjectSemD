import re


class Checkings:
    @staticmethod
    def check_product_data(product: list) -> bool:
        pass

    @staticmethod
    def check_catalog_number(catalog_number: str) -> bool:
        return re.match(r'^[A-Za-z]{8}$', catalog_number) and isinstance(catalog_number, str)
    @staticmethod
    def check_product_name(product_name:str)->bool:
        pass
