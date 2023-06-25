from Checkings import *

import datetime


class Filereader:
    @staticmethod
    def read_data_file(file_path: str) -> list:
        """
        Read the data file and validate the product data.

        :param file_path: The path of the file to be read.
        :return: A list of valid products.
        :raises FileNotFoundError: If the file is not found.
        :raises TypeError: If the file_path is not a string.
        """
        if not Checkings.check_file_path(file_path):
            raise TypeError("File path must be a string.")

        valid_products = []
        error_log = []  # List to store error messages

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    product_data = line.strip().split(',')

                    if Checkings.check_product_data(product_data):
                        valid_products.append(product_data)

                    else:
                        error_message = f"Invalid product data: {line}"
                        error_log.append(error_message)
                        print(error_message)  # Print the error message

        except FileNotFoundError:
            error_message = f"File not found: {file_path}"
            error_log.append(error_message)
            print(error_message)  # Print the error message

        if error_log:
            # Write errors to log.errors file with date and time
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_filename = "errors.log"
            with open(log_filename, 'a') as log_file:
                log_file.write(f"{current_datetime}: {', '.join(error_log)}\n")

        return valid_products
