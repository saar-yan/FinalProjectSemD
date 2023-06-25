from query_handler import *


class Store:
    def __init__(self, valid_products):
        """
        Initialize the Store with valid products.
        :param valid_products: A list of valid products.
        """
        self.valid_products = valid_products

    @property
    def valid_products(self):
        """
        Get the valid products.
        :return: A list of valid products.
        """
        return self._valid_products

    @valid_products.setter
    def valid_products(self, products):
        """
        Set the valid products, checking if it is an instance of a list.
        :param products: A list of valid products.
        :raises TypeError: If the products is not an instance of a list.
        """
        if isinstance(products, list):
            self._valid_products = products
        else:
            raise TypeError("Valid products must be an instance of a list.")

    def total_month_revenue(self) -> dict:
        """
        Calculate the total revenue for each product in the month.
        :print: A dictionary with product names as keys and their total revenue as values.
        """
        total_revenue = {}
        for product in self._valid_products:
            product_name = product[1]
            product_amount = int(product[2])
            product_price = float(product[3])
            total_revenue[product_name] = product_price * product_amount

        print("Total month revenue: ", total_revenue)

    def best_month_seller(self) -> None:
        """
        Find the product with the highest revenue in the month.
        :print: The name of the best-selling product.
        """
        # month_income = self.total_month_revenue()
        total_revenue = {}
        for product in self._valid_products:
            product_name = product[1]
            product_amount = int(product[2])
            product_price = float(product[3])
            total_revenue[product_name] = product_price * product_amount

        best_seller = max(total_revenue, key=total_revenue.get)
        print("Best Month seller: ", best_seller)

    def not_sold_products(self) -> None:
        """
        Find the products with that are not sold this month
        print A List with not sold products
        """
        print("Not sold products:")
        for product in self._valid_products:
            if product[2] == '0':
                print(product)

    def cheapest_and_expensive_pro(self) -> None:
        """
        Find the products with that are not sold this month
        print cheapest and expensive products
        """

        products = {}
        max = 0
        min = 1000000000
        for product in self._valid_products:
            product_price = float(product[3])
            if product_price > max:
                max = product_price
                product_max = product
            if product_price < min:
                min = product_price
                product_min = product

        print(f"The Must Expensive Product: {product_max} \nThe Cheapest Product: {product_min}")

    def add_products_to_db(self) -> None:
        """
           Find the products with that are not sold this month
           print cheapest and expensive products
        """
        # q = QueryHandler("localhost", "Products", "root", "")
        # for product in self._valid_products:
        #     sku = product[0]
        #     product_name = product[1]
        #     quantity_sold = int(product[2])
        #     price_per_unit = float(product[3])
        #     query = "INSERT INTO products (sku, product_name, quantity_sold, price_per_unit) " \
        #             "VALUES (%s, %s, %s, %s) " \
        #             "ON DUPLICATE KEY UPDATE price_per_unit = VALUES(price_per_unit)"
        #     values = (sku, product_name, quantity_sold, price_per_unit)
        #     try:
        #         q.execute_non_fetch(query, values)
        #     except BaseException as e:
        #         print(f"Error adding product {product_name} to the database: {e}")
