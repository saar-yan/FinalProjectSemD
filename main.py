from Filereader import *
from  Store import *
if __name__ == '__main__':
    file_path = 'Products.txt'
    try:

        valid_products = Filereader.read_data_file(file_path)
        store = Store(valid_products)
        store.total_month_revenue()
        store.best_month_seller()
          # print(valid_products)
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
# s