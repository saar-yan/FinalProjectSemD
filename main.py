from filereader import *
from  Store import Store
if __name__ == '__main__':
    file_path = 'Products.txt'
    try:

        valid_products = Filereader.read_data_file(file_path)
        store = Store(valid_products)

        # store.not_sold_products()
        # store.best_month_seller()

        # store.total_month_revenue()
        store.cheapest_and_expensive_pro()
        store.add_products_to_db()
        print(valid_products)



        # q = QueryzHandler("localhost", "DBWithPython", "root", "")
        # check authenticate
        # print(q.execute_fetch("SELECT * FROM accounts WHERE account_id=%s", (1,)))
        #
        # q.execute_non_fetch("DELETE FROM accounts WHERE account_id=%s", (1,))
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
