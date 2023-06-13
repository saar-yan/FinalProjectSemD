import re


class Checkings:
    @staticmethod
    def check_product_data(product: list) -> bool:
        if len(product) != 4:
            return False

        catalog_number = product[0]
        product_name = product[1]
        quantity_sold = product[2]
        product_price = product[3]

        if not Checkings.check_catalog_number(catalog_number):

            return False

        if not Checkings.check_product_name(product_name):
            return False

        if not Checkings.check_quantity_sold(quantity_sold):
            return False

        if not Checkings.check_product_price(product_price):
            return False

        return True

    @staticmethod
    def check_catalog_number(catalog_number: str) -> bool:
        match = re.match(r'^[A-Za-z0-9]{8}$', catalog_number)
        is_valid = match is not None and isinstance(catalog_number, str)
        return is_valid
    @staticmethod
    def check_product_name(product_name: str) -> bool:
        return re.match(r'^[A-Z][a-zA-Z]{2,19}$', product_name) and isinstance(product_name, str)

    @staticmethod
    def check_quantity_sold(quantity_sold: str) -> bool:
        is_valid = isinstance(quantity_sold, str) and quantity_sold.isdigit()

        return is_valid

    @staticmethod
    def check_product_price(product_price: str) -> bool:
        price = float(product_price)
        is_valid = isinstance(price, float) and price > 0.0

        return is_valid

    @staticmethod
    def check_file_path(file_path: str) -> bool:
        return isinstance(file_path, str)


