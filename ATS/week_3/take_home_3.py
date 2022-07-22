#  Create a dictionary of 20 random values in the range 1–99. Determine whether there are any
# duplicate values in the dictionary. (Hint: you many want to sort the list first.)


import random

# random_values = random.randrange(1,99)

def dict_without_duplication():
    empty_list =[]

    for i in range(1,21):
        random_values = random.randrange(1,99)
        if not random_values in empty_list:
            empty_list.append(random_values)
        else:
            continue
    dict_created = {x: x for x in empty_list}

    return dict_created

if __name__ == "__main__":
    myfunc = dict_without_duplication()
    print(myfunc)