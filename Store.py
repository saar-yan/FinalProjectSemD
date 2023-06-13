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
        :return: A dictionary with product names as keys and their total revenue as values.
        """
        total_revenue = {}
        for product in self._valid_products:
            product_name = product[1]
            product_amount = int(product[2])
            product_price = float(product[3])
            total_revenue[product_name] = product_price * product_amount
        return total_revenue

    def best_month_seller(self) ->str:
        """
        Find the product with the highest revenue in the month.
        :return: The name of the best-selling product.
        """
        month_income = self.total_month_revenue()
        best_seller = max(month_income, key=month_income.get)

        return best_seller
