#  Use a list of lists to solve the following problem. A company has four salespeople (1 to 4)
# who sell five different products (1 to 5). Once a day, each salesperson passes in a slip for each different type of product sold. Each slip contains:
# a) The salesperson number.
# b) The product number.
# c) The number of that product sold that day.
# Thus, each salesperson passes in between 0 and 5 sales slips per day. Assume that the information
# from all of the slips for last month is available. Write a program that will read all this information for
# last month’s sales and summarize the total sales by salesperson by product. All totals should be
# stored in list sales. After processing all the information for last month, display the results in tabular format,
#  with each of the columns representing a particular salesperson and each of the rows representing a particular product. 
# Cross-total each row to get the total sales of each product for last
# month; cross-total each column to get the total sales by salesperson for last month. Your tabular
# printout should include these cross-totals to the right of the totaled rows and at the bottom of the
# totaled columns.


sale_slips =[['seller_1',[3,23,5],[2,4,54],[23,41,8],[1,3,4],[5,2,6]],
             ["seller_2",[7,3,2],[3,6,8],[9,7,2],[8,3,4],[8,4,3]],
             ["seller_3",[21,3,1],[4,5,2],[7,3,4],[6,3,2],[8,9,12]],
             ["seller_4",[4,3,9],[12,4,1],[4,7,9],[4,3,1],[7,6,2]]
            ]
sales = []
total_product = []

total_product_1 = sum(sale_slips[0][1] + sale_slips[1][1] + sale_slips[2][1] +sale_slips[3][1])
total_product.append(total_product_1)

total_product_2 = sum(sale_slips[0][2] + sale_slips[1][2] + sale_slips[2][2] +sale_slips[3][2])
total_product.append(total_product_2)

total_product_3 = sum(sale_slips[0][3] + sale_slips[1][3] + sale_slips[2][3] +sale_slips[3][3])
total_product.append(total_product_3)

total_product_4 = sum(sale_slips[0][4] + sale_slips[1][4] + sale_slips[2][4] +sale_slips[3][4])
total_product.append(total_product_4)

total_product_5 = sum(sale_slips[0][5] + sale_slips[1][5] + sale_slips[2][5] +sale_slips[3][5])
total_product.append(total_product_5)



sale1 = sum(sale_slips[0][1] + sale_slips[0][2] + sale_slips[0][3] + sale_slips[0][4] + sale_slips[0][5])
sales.append(sale1)

sale2 = sum(sale_slips[1][1] + sale_slips[1][2] + sale_slips[1][3] + sale_slips[1][4] + sale_slips[1][5])
sales.append(sale2)


sale3 = sum(sale_slips[2][1] + sale_slips[2][2] + sale_slips[2][3] + sale_slips[2][4] + sale_slips[2][5])
sales.append(sale3)

sale4 = sum(sale_slips[3][1] + sale_slips[3][2] + sale_slips[3][3] + sale_slips[3][5] + sale_slips[3][1])
sales.append(sale4)
fp = '1st'
sp = '2nd'
tp = '3rd'
thp = '4th'
fthp = '5th'

print(f'\n\t\t\t\t\t\t{fp} {sp}  {tp} {thp} {fthp}')
print("---------------------------------------------------------------------")
print(f'first salesperson total slip per product are   : {sum(sale_slips[0][1])}  {sum(sale_slips[0][2])}  {sum(sale_slips[0][3])}   {sum(sale_slips[0][4])}   {sum(sale_slips[0][5])}')
print(f'second salesperson total slips per prodect are : {sum(sale_slips[1][1])}  {sum(sale_slips[1][2])}  {sum(sale_slips[1][3])}   {sum(sale_slips[1][4])}   {sum(sale_slips[1][5])}')
print(f'third salesperson total slips per prodect are :  {sum(sale_slips[2][1])}  {sum(sale_slips[2][2])}  {sum(sale_slips[2][3])}   {sum(sale_slips[2][4])}   {sum(sale_slips[2][5])}')
print(f'fouth salesperson total slips per prodect are :  {sum(sale_slips[3][1])}  {sum(sale_slips[3][2])}  {sum(sale_slips[3][3])}   {sum(sale_slips[3][5])}   {sum(sale_slips[3][4])}')
print(f'Total each product :\t\t\t\t {total_product[0]}  {total_product[1]}  {total_product[2]}  {total_product[3]}  {total_product[4]}')
