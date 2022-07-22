# import csv

# with open("info.csv","r") as f:
#     handler = csv.DictReader(f)
#     for k,v in enumerate(handler):
#         print(k, ":", v)

# with open("info3.csv","w") as f:
#     header = ["basheer","balogun","male"]
#     handler = csv.DictWriter(f,fieldnames=header)
#     handler.writeheader()
#         handler.writerow({"basheer":"firstname","balogun":"lastname"})

import csv

header = ['firstname', 'lastname', 'middlename', 'age','occupation','date_of_birth','gender','marital_status','email']
data = [
    ['Basheer', 'Balogun', 'Olamilekan', 'male',''],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('info3.csv', 'w',) as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)


