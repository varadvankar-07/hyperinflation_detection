products = ["iphone","ipad","ipod"]
regions  = ["US","IND","UK"]
revenue =  [20,23,45,18,12,13,70,45]

i = 0

for product in products:
    for region in regions:
        rev = revenue[i]
        i = i + 1
        print(f"{product} {region} revenue: ",rev)

        office_supplies = ["pen", "paper", "stapler"]
        kitchen_supplies = ["fork", "knife", "spoon"]
        combined_list = kitchen_supplies + office_supplies
        print(combined_list[2: 4])