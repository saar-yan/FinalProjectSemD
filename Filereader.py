from Checkings import *


class Filereader:
    @staticmethod
    def read_data_file(file_path: str) -> list:
        """
        :param file_path:  Read the data file and validate the product data.
        :return:  list: A list of valid products.
        :raise FileNotFoundError: If the file is not found.
        :raise: TypeError: If the file_path is not a string.
        """
        if not Checkings.check_file_path(file_path):
            raise TypeError("File path must be a string.")

        valid_products = []
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    product_data = line.strip().split(',')

                    if Checkings.check_product_data(product_data):
                        valid_products.append(product_data)
                    else:
                        raise ValueError(f"Invalid product data: {line}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

        return valid_products
# s