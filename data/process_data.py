# import csv
#
# input_files = [
#     "data/daily_sales_data_0.csv",
#     "data/daily_sales_data_1.csv",
#     "data/daily_sales_data_2.csv",
# ]
#
# output_file= "../output.csv"
# with open(output_file, "w", newline="") as out:
#     writer = csv.writer(out)
#     writer.writerow(["Sales","Dates","Region"])
#
#     for file in input_files:
#         with open(file, newline="") as f:
#             reader = csv.DictReader(f)
#
#             for row in reader:
#                 if row ["product"]== "Pink Morsels":
#                     quantity = int(row["quantity"])
#                     price = float(row["price"])
#                     sales = quantity * price
#                     date = row["date"]
#                     region = row["region"]
#                     writer.writerow([sales,date,region])