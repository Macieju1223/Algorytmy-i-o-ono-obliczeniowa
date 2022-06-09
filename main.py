import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from csv_files import files
from textblob import TextBlob, Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.sentiments import BaseSentimentAnalyzer
from pathlib import Path
from pprint import pprint


class Weather:

    def open_csv(self, num):
        """opens csv files"""
        path = 'csv_files/'
        file = pd.read_csv(f'{path}{files.csv_list[num]}')
        file = pd.DataFrame(file)
        celsius = self.converter(file[' Average Temperature'])
        file['Average Celsius'] = celsius
        return file

    def describe_to_file(self):
        """vcreates file and overwrites it with avarage temperatures"""
        with open('avarage_temps.csv', 'w') as file:
            for num in range(len(files.csv_list)):
                avarage_temp = self.open_csv(num)
                file.write(f'\t{files.csv_list[num]}\n{avarage_temp.mean()}\n\t\n')

    @staticmethod
    def converter(farenheit):
        """converts fahrenheit to celsius"""
        celcius = 5 / 9 * (farenheit - 32)
        return celcius

    @staticmethod
    def list_of_farenheit(list):
        """converts fahrenheit list to celsius"""
        c = lambda f: 5 / 9 * (f - 32)
        temps = [(f, c(f)) for f in list]
        temps = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
        return temps

    def weather_chart(self):
        """show one chart"""
        temps = self.list_of_farenheit([x for x in range(0, 110, 10)])
        temps.plot(x='Fahrenheit', y='Celsius', style='.-', color='red')
        plt.show()

    def multiple_charts(self):
        """Shows multiple charts"""
        temps: dict = {}
        for num in range(len(files.csv_list)):
            temps.update({
                files.months_in_year[num]: self.open_csv(num)['Average Celsius'].mean()
            })
        figure, axis = plt.subplots(2, 2)
        axis[0, 0].bar(temps.keys(), temps.values(), color='yellow')
        axis[0, 0].set_title('Celsius')

        axis[0, 1].plot(temps.keys(), temps.values(), color='red')
        axis[0, 1].set_title('Celsius bow')

        axis[1, 0].scatter(temps.keys(), temps.values())
        axis[1, 0].set_title('dots')

        plt.show()


class LanguageCommunication:

    @staticmethod
    def test():
        text = 'today is a day like any other. Tomorrow i hope to wake up'
        blob = TextBlob(text)
        print('-------------')
        print(blob.sentences)
        print(blob.words)
        print(blob.tags)
        print(blob.noun_phrases)
        print(blob.sentiment)

    @staticmethod
    def test_sentiments():
        """assign sentences to negattive or possitive"""
        text = 'Today is a beautiful day. Tomorrow looks like bad weather.'
        blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
        print('------------------')
        for sentence in blob.sentences:
            print(sentence.sentiment)

    @staticmethod
    def language_detecting():
        """it suposed to check language, but it's not work anymore"""
        text = 'Today is a beautiful day. Tomorrow looks like bad weather.'
        blob = TextBlob(text, analyzer=BaseSentimentAnalyzer)
        print('------------')

    @staticmethod
    def word_function():
        """checking words in txt"""
        index = Word('index')
        print('---------')
        print(index.pluralize())
        animals = TextBlob('dog cat fish bird marcin').words
        print(animals.pluralize())
        for word in animals:
            word = Word(word)
            print(word.spellcheck())

    @staticmethod
    def read_files():
        """reading text files with blob"""
        blob = TextBlob(Path('avarage_temps.csv').read_text())
        print('-----------')
        pprint(blob.word_counts)
        print(blob.word_counts['valley'])


class Algorithms:

    @staticmethod
    def read_csv():
        """method opens csv file"""
        path = 'csv_files/housing-sales-borough.csv'
        file = pd.read_csv(path)
        file = pd.DataFrame(file)
        return file

    def show_areas(self):
        """method prints all available areas in csv file"""
        file = self.read_csv()
        areas = [x for x in file['Area']]
        for num in range(len(areas)):
            print(num, ' : ', areas[num])
        return areas

    def sales_changes(self, area='Lambeth'):
        """method creates 2 charts with changes in sales since 1995 to 2014 of specific area"""
        file = self.read_csv()
        file = file.loc[:, file.columns != 'Code']
        file = file.set_index('Area')
        numpy_array = np.array(file.loc[area])
        labels = [x[6:] for x in list(file.columns)]

        figure, axis = plt.subplots(2)
        axis[0].plot(numpy_array, labels,
                     marker='o', mfc='b', mec='b', color='r', linewidth=0.4
                     )
        axis[0].set_title(f'Sale changes for {area} since 1995 - 2014')

        percent = numpy_array * 100 / sum(numpy_array)
        percent = np.round(percent, 2)

        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(numpy_array)))
        axis[1].pie(percent,
                    labels=labels, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        plt.show()

    def areas_compare(self, areas=['Lambeth', 'Lewisham'], year='1995'):
        """method compares two areas and creates charts"""
        file = self.read_csv()
        all_sales: dict = {}
        file = file.loc[:, file.columns != 'Code']
        file['sum'] = file.sum(numeric_only=True, axis=1)

        for num in range(len(file)):
            all_sales.update({
                file['Area'][num]: file[f'Sales-{year}'][num]
            })
        all_sales.update({
            'total': sum(all_sales.values())
        })
        sales: list = [all_sales[areas[0]], all_sales[areas[1]]]
        figure, axis = plt.subplots(2)
        axis[0].barh(areas, sales, color='red')
        axis[0].set_title(f'Sales compare for {areas[0]} - {areas[1]} in {year}')

        colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(sales)))
        axis[1].pie(sales, labels=areas, colors=colors, center=(4, 4),
                    wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        plt.show()

    def because_why_not(self):
        """it creates charts, lots of random charts"""
        file = self.read_csv()
        file = file.loc[:, file.columns != 'Code']
        array = np.array(file)

        random_area = random.choices(array)
        figure, axis = plt.subplots(3, 4)
        axis[0][0].barh(random_area[0][1:], random_area[0][1:], color='red')
        axis[0][0].axis("off")
        axis[0][0].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[0][1].hist(random_area[0][1:])
        axis[0][1].axis("off")
        axis[0][1].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[0][2].eventplot(random_area[0][1:])
        axis[0][2].axis("off")
        axis[0][2].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[0][3].hist2d(random_area[0][1:], random_area[0][1:])
        axis[0][3].axis("off")
        axis[0][3].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[1][0].plot(random_area[0][1:])
        axis[1][0].axis("off")
        axis[1][0].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[1][1].pie(random_area[0][1:])
        axis[1][1].axis("off")
        axis[1][1].set_title(f'{random_area[0][:1]}')

        random_area = random.choices(array)
        axis[1][2].stem(random_area[0][1:], random_area[0][1:])
        axis[1][2].axis("off")
        axis[1][2].set_title(f'{random_area[0][:1]}')

        x = np.random.uniform(-5, 5, 126)
        y = np.random.uniform(-5, 5, 126)
        axis[1][3].triplot(x, y)
        axis[1][3].axis("off")
        axis[1][3].set_title('Triplot sample')

        random_area = random.choices(array)
        axis[2][0].step(random_area[0][1:], random_area[0][1:])
        axis[2][0].axis("off")
        axis[2][0].set_title(f'{random_area[0][:1]}')

        x = np.random.randn(5000)
        y = 1.2 * x + np.random.randn(5000) / 3
        axis[2][1].hexbin(x, y, gridsize=40)
        axis[2][1].axis("off")
        axis[2][1].set_title('Hexbin sample')

        x = np.random.uniform(-3, 3, 256)
        y = np.random.uniform(-3, 3, 256)
        z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
        axis[2][2].plot(x, y, 'o', markersize=0.5, color='pink')
        axis[2][2].tripcolor(x, y, z)
        axis[2][2].axis("off")
        axis[2][2].set_title('tripcolor sample')

        X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
        Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-X ** 2 - Y ** 2)
        levels = np.linspace(np.min(Z), np.max(Z), 7)
        axis[2][3].contour(X, Y, Z, levels=levels)
        axis[2][3].axis("off")
        axis[2][3].set_title('Contour sample')

        plt.show()


if __name__ == '__main__':
    pd.set_option("display.precision", 2)
    # initiate = Weather()
    # initiate.weather_chart()
    # initiate.describe_to_file()
    # initiate.multiple_charts()

    # initiate = LanguageCommunication()
    # initiate.test()
    # initiate.test_sentiments()
    # initiate.language_detecting()
    # initiate.word_function()
    # initiate.read_files()

    initiate = Algorithms()

    areas = initiate.show_areas()
    # initiate.areas_compare([areas[4], areas[9]], '2014')  # --- you can specify which areas you want compare in year
    initiate.sales_changes(areas[-11])  # --- change area by giving area name
    # initiate.because_why_not()  # --- try it out

