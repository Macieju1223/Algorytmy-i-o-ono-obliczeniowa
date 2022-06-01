import json
import random

import numpy as np
import pandas as pd
from decimal import Decimal
import re
from pprint import pprint
import csv
import matplotlib.pyplot as plt
from collections import namedtuple
# import random

# dict = {
#     "country": ["Brazil", "Russia", "India", "China", "South Africa"],
#     "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#     "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#     "population": [200.4, 143.5, 1252, 1357, 52.98] 
#        }

# brics = pd.DataFrame(dict)
# print(brics)

# tabelka = pd.read_csv('tabelka.csv')
# print(tabelka)
# print('tabelka csv--------')
# print(type(tabelka))

# print('--------')

# dates = pd.date_range("20130101", periods=10)
# print(dates)

# df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD"))
# print(df)

# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )

# print(df2)
# print('numpy_sort:' , np.sort(tabelka))



# Create 2 new lists height and weight
# height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# # Create 2 numpy arrays from height and weight
# np_height = np.array(height)
# np_weight = np.array(weight)

# print(np_height)
# print(np.sort(np_height))
# print('--------')
# print(np_weight)
# print(np.sort(np_weight))

# con = np.concatenate((np_height,np_weight))
# print(np.sort(con))
# print(np.ceil(con))

# for i in range(100):
#     print('Errorr', random.randint(100,400), 'something went wrong')

# prices = {
#     'bananas': [2.99, 3.49, 5.99],
#     'oranges': [4.15, 5.15, 6.05],
#     'apples': [0.91, 1.43, 3.35]
# }
# print('---------------')
# # prices = np.array({
# #     'bananas': [2.99, 3.49, 5.99],
# #     'oranges': [4.15, 5.15, 6.05],
# #     'apples': [0.91, 1.43, 3.35]
# # })

# print(pd.DataFrame(prices).describe())


# srednia = pd.DataFrame(prices)

# print(np.mean(srednia))
# print(srednia)

# print(tabelka.to_string())

# print(tabelka)

# print(tabelka.tail(1))


# prices = pd.read_csv('tabelka.csv', skiprows=[0])

# graces = pd.DataFrame({
#     'eva': [12,32,12],
#     'dave': [43,433,34],
#     'steve': [323,12,63]
# })

# print(graces[(graces >= 80) & (graces <= 500)])
# print(graces)
# print(graces.at[0,'eva'])
# print(graces.describe())

# print(prices.describe())
# print(graces.T.describe())
# print(graces.T.mean())
# # creates a view not changing the original object

# print('----sorting---------')

# print(graces.sort_index(ascending=False))
# print('111111')
# print(graces.sort_index(axis=1)) # ---- alfabetic order
# print(graces.sort_values(by=0,axis=1,ascending=False)) # -- sorted by valuse in a row
# print(graces.T.sort_values(by=0,ascending=False)) # -- same a previous but difrent
# print(graces.loc[0].sort_values(ascending=False))
# print(graces.sort_values(by=0,axis=1,ascending=False,inplace=True))

# print('------------')

# temps = {
#     'mon': [68,89],
#     'tue': [71,93],
#     'wed': [66,82],
#     'thu': [75,97],
#     'fri': [62,79]
# }

# temperatures = pd.DataFrame(temps,index=['low','hight'])
# print(temperatures)
# print(temperatures.loc[:,'mon':'wed'])
# print('---')
# print(temperatures.loc['low'])
# print(temperatures.mean())
# print(temperatures.mean(axis=1))

# print('-----strings-----')

# print(f'{Decimal("100000000000000000000000.0"):.3f}')
# # duuuuzzaaa liczba

# print(f'{58:c}{45:c}{41:c}')  # ASCII usfull

# print(f'[{27:10d}]')
# print(f'[{27:10f}]')
# print(f'[{27:<10d}]')
# print(f'[{27:<10f}]')
# print(f'[{27:^7d}]')
# print(f'[{27:+010d}]')
# print(f'[{27:-10d}]')
# print(f'[{27:+010d}]')

# a = 'amanda'
# print(f'[{a:>10}]')
# print(f'[{a:^10}]')

# n1 = 10240.473
# n2 = -3210.9521

# print(f'{n1:+10,.2f}\n{n2:+10,.2f}')

# print('{:.2f}'.format(17.489))
# print('{} {}'.format('Amanda','Cyan'))
# print('{0} {0} {1}'.format('happy', 'Bithday'))
# print('{first} {second} {last}'.format(first = 'amanda', second = 'likes', last = 'cats'))

# print(f'{58:c}{45:c}{41:c}')
# print('{:c}{:c}{:c}'.format(58,45,41))
# a = 'Amanda'
# print(f'[{a:>10}]\n[{a:<10}]\n[{a:^10}]')
# print(f'{n1:+10,.2f}\n{n2:+10,.2f}')

# name = 'MAciej'
# sur = 'Urbaniak'

# name += ' ' + sur
# con = '>' * len(name)
# print('{0}\n{1}\n{0}'.format(con,name,con))

# print('------sentences------')

# sentence = "\t \n this is a testy string. \t\t \n"
# print(sentence)
# print(sentence.strip()) # removed all white spaces
# print(sentence.lstrip())
# print(sentence.rstrip())

# name = '          merge asdad       '

# print(name.strip())

# values = '1\t2\3\t4\t5'
# print(values)
# print(values.replace('\t', ','))

# nums = '1 2 3 4 5'
# print(nums.replace(' ', ' --> '))
# print(' ------ ')

# let = 'a, b, c, d'
# print(let.split(','))

# x = ','.join([str(i) for i in range(100)])
# print(x)

# pat = '02215'
# print('----pamdas-again-----')
# zips = pd.Series({
#     'boston': '02215',
#     'miami': '3310'
# })
# cities = pd.Series([
#     'boston, MA 02215',
#     'miami, FL 3310'
# ])
# contracts = [
#     ['mike brown','demo@info.xl','232123123'],
#     ['dave stown','dave@123132.com','222222222']
# ]

# def get_formated_phone(value):
#     result = re.fullmatch(r'(\d{3})-(\d{3})-(\d{3})', value)
#     return result

# print(zips)

# print(zips.str.match(r'\d{5}'))
# print(cities.str.contains(r' [A-Z]{2}'))
# contracts = pd.DataFrame(contracts, columns=['name','email','phone'])

# print(contracts,'\n-----------')
# print(contracts['phone'])

# print(a)
# print('--------files-------')

# def records_example():
#     accounts = open('accounts.txt','r')
#     text_file = open('tem_file.txt','w')
#     with accounts,text_file:
#         for record in accounts:
#             account, name, balance = record.split()
#             if account != '300':
#                 text_file.write(record)
#             else:
#                 new_record = ' '.join([account, 'Wiliams',balance])
#                 text_file.write(new_record + '\n')



# dictionary:dict = {
#     'accounts':[
#         {
#             'account': 100,
#             'name': 'Jones',
#             'balance': 24.98,
#         },
#         {
#             'account': 200,
#             'name': 'Doe',
#             'balance': 345.67,
#         }
#     ]
# }
# with open('accounts.json','w') as accounts:
#     json.dump(dictionary,accounts)

# with open('accounts.json', 'r') as acc:
#     acc_json = json.load(acc)

# pprint(acc_json)


# grades:dict={
#     'gradebook': [
#         {
#             'student': 1,
#             'name': 'Red',
#             'grade': 'A',
#         },
#         {
#             'student': 2,
#             'name': 'Green',
#             'grade': 'B',
#         },
#         {
#             'student': 3,
#             'name': 'White',
#             'grade': 'A',
#         },
#     ]
# }
# with open('grades.json','w') as file:
#     json.dump(grades,file)

# with open('grades.json','r') as file:
#     gradds = json.load(file)
# pprint(gradds)

# print('---------------\n')
# def division():
#     while True:
#         try:
#             num1 = int(input('enter num : '))
#             num2 = int(input('enter domin : '))
#             res = num1 / num2
#         except ValueError:
#             print('wrong numbers')
#             return 0
#         except ZeroDivisionError:
#             print('division throu 0')
#         else:
#             print(f'{num1:.3f} / {num2:.3f} = {res:.3f}')

# print('--------------------\n')
# def csv_file():
#     with open('acoounts.csv', mode='w', newline='') as accounts:
#         writer = csv.writer(accounts)
#         writer.writerow([100,'Jones',24.98])
#         writer.writerow([200,'Doe',355.23])
#         writer.writerow([300,'White',0.00])
#         writer.writerow([400,'Stone',-42.16])
#         writer.writerow([500,'Rich',224.12])
#         writer.writerow([600,'laila',2322.1])
#         writer.writerow([700,'Cow',123123121231312312312.09])

#     with open('acoounts.csv',mode='r') as accounts:
#         print(f'{"account":<10}{"name":<10}{"ballance":<10}')
#         reader = csv.reader(accounts)
#         for rec in reader:
#             account,name,balance = rec
#             print(f'{account:<10}{name:<10}{float(balance):.2f}')

# # df = pd.read_csv('acoounts.csv',
# #                     names=['account','name','balance'])
# titanic = pd.read_csv('titanicsurvivals.csv')
# # print((titanic['survived'] == 'yes').describe())
# # plt.hist(titanic)
# # plt.show()
# print('----------')
# name = 'Allen, Miss. Elisabeth Walton'
# tab = [x for x in titanic['name']]
# for x in range(len(titanic)):
#     if name in tab[x]:
#         print(titanic.iloc[x])
#
# # print(titanic.iloc[31:61]['name'])
# # print('-----')
# #
# slownik: dict = {
#     'country':['Brazil','Rusia','India','China','South Africa'],
#     'capital':['Brasilia','Moscov','New Delhi','Beijing','Pretoria'],
#     'area':[8.516, 17.10, 3.286, 9.597, 1.221],
#     'population':[200.4, 143.5, 1252, 1357, 52.98]
# }
# data = pd.DataFrame(slownik)
# plt.bar(slownik['country'],slownik['population'])
# plt.pie(slownik['area'], labels=slownik['country'])
# plt.show()
# Data_Frame = pd.DataFrame(slownik, index=['A', 'B', 'C', 'D', 'E'])
# print(Data_Frame)
# print('-------')
# print(Data_Frame.sort_values('area', ascending=False))

# x = np.random.randint(10, size=10)
# y = np.random.randint(10, size=10)
# plt.bar(x,y)
# plt.show()
# plt.plot(x,y)
# plt.show()
# plt.hist(y)
# plt.show()
# plt.hist(x)
# plt.show()


class WellPaidDuck:
    def __repr__(self):
        return f'ima well paid duck\n{self.earnings()}'

    @staticmethod
    def earnings():
        return Decimal('1_000_000.00')


class NamedTuples:
    def __repr__(self):
        return self.named_cards()

    @staticmethod
    def named_cards():
        card_obj = namedtuple('card', ['face', 'suit'])
        card = card_obj(face='Ace', suit='Spades')
        return f'{card.face} of {card.suit}'

    @staticmethod
    def cards_value():
        card_obj = namedtuple('card', ['face', 'suit'])
        card = card_obj(face='Ace', suit='Spades')
        values = ['Queen', 'Hearts']
        card = card._make(values)
        return card

    @staticmethod
    def cards_dict():
        card_obj = namedtuple('card', ['face', 'suit'])
        card = card_obj(face='Ace', suit='Spades')
        values = ['Queen', 'Hearts']
        card = card._make(values)
        card = card._asdict()
        return card


class TabelkaCsv:
    def __init__(self):
        self.titanic = pd.read_csv('titanicsurvivals.csv')
        self.tabelka = pd.read_csv('tabelka.csv')

    def tabelka_csv(self):
        plik_csv = pd.DataFrame(self.tabelka)
        return plik_csv

    def wykresy(self):
        dane = pd.DataFrame(self.titanic)
        tabelka = pd.DataFrame(self.tabelka)
        dane.groupby(['survived'])['name'].count().plot(kind='barh')
        plt.show()
        dane.groupby(['age'])['sex'].count().plot(kind='hist')
        plt.show()
        dane.groupby(['passengerClass'])['sex'].count().plot(kind='pie')
        plt.show()

    def loock_by_name(self,name):
        data = self.titanic
        tab = [x for x in data['name']]
        for x in range(len(data)):
            if name in tab[x]:
                member = data.iloc[x]
                return member
        return 'no member with that name'



if __name__ == '__main__':
    # initiate = WellPaidDuck()
    # print(initiate)
    #
    # initiate = NamedTuples()
    # print(initiate)
    #
    # initiate = NamedTuples()
    # print(initiate.cards_value())
    #
    # initiate = NamedTuples()
    # print(initiate.cards_dict())
    initiate = TabelkaCsv()
    # print(initiate.tabelka_csv())
    print(initiate.wykresy())
    print('---------')
    print(initiate.loock_by_name('Allen, Miss. Elisabeth Walton'))


# data_frame = pd.read_csv('homes.csv')
# grouped = data_frame.groupby(['Rooms'])['Sell'].count().plot(kind='barh')
# plt.show()