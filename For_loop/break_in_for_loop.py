monthly_sales = [42,36,78,90,65,54]
months  = ["jan","feb","mar","apr","may","jun"]

thresold = 50

for sales_amount, months in zip(monthly_sales, months):
    if sales_amount < thresold:
        print(f"Sales amount {sales_amount} is less than the thresold {thresold} in {months}")
    else:
        print(f"Sales amount {sales_amount} is greater than the thresold {thresold} in {months}")
# the use of zip is that include the jan and 42 together for above ex
