from utils import *


filename = "operations.json"

account_list = get_operations_json(filename)

new_c = get_executed_operations(account_list)
sort_data = sort_by_date(new_c)
first_five_op = print_five_operations(sort_data)

for i in range(5):
    a = get_id_info(first_five_op, i)
    print(f"{get_date(a)} {get_description(a)} \n{get_from(a)} -> {get_to(a)} \n{get_amount(a)} \n")
