# import random

# def sentence(n):
#     objects = ["rat","egg","table"]#,"water","food"]
#     subject =["Lola","Bisi","kemi"]#,"Sola","Wumi","kumi"]
#     verbs = ["went","saw","wrote"]#,"ate","drank"]


#     ramd=[]
#     for _ in range(n):
#         sen1 = random.choice(objects)
#         sen2 = random.choice(subject)
#         sen3 = random.choice(verbs)
#         sent = sen2 +" "+ sen3 +" "+ sen1
#         r = sent.split(",")
#         ramd +=r
#     for i in ramd:
#         print(i)
    
# sentence(int(input(" Enter number : ")))

import random

# messages = ['It is certain',
#  'It is decidedly so',
#  'Yes definitely',
#  'Reply hazy try again',
#  'Ask again later',
#  'Concentrate and ask again',
#  'My reply is no',
# 'Outlook not so good',
#              'Very doubtful']

# # index = random.randint(0, len(messages) - 1)
# #
# # print(messages[index])


# # print(random.choice(messages))


# # todo: have a list of subjects, verbs and objects. And randomly generate 10 sentences.
# # todo: create a generator function that can take an integer and will print n number of sentences.
# # todo: modify your function to generate unique sentences.


# subjects = ['Ade', 'Ola', 'Bolu']
# verbs = ['eats', 'drinks', 'drives']
# objs = ['food', 'water', 'car']

# def generate_words(n: int):
#  sentences = []
#  for i in range(n):
#   sentence = f'{random.choice(subjects)} {random.choice(verbs)} {random.choice(objs)}'
#   if sentence not in sentences or len(sentences) != len(subjects) * len(verbs) * len(objs):
#     sentences.append(sentence)
#     print(sentence)
#   else:
#    print("No more unique sentences to generate")
#    break

#  print(len(sentences))

# generate_words(1000)
passlen = int(input("Enter the length of password : "))
chara =[5,6,3,9,2,6,4,0,7]
p = random.choice(chara)

print(p)