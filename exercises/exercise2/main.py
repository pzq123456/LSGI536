import pandas as pd
import matplotlib.pyplot as plt
import os

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path = ./
PATH = os.path.join(PARENT_DIR, 'exercise2\\')

names = ['vegetation', 'soil', 'water', 'urban']

def read_csv(path):
    return pd.read_csv(path)

def getStatistics(df):
    return df.describe()

# draw curve for each band
# | Band 1 0.5-0.59 | Band 2 0.61-0.68 | Band 3 0.79-0.89 |
def draw_curve_helper(df, name):
    column_names = ['Band1', 'Band2', 'Band3']

    # just draw the mean value for each band
    stastics = getStatistics(df)

    # print(stastics)

    # get the mean value for each band
    mean_values = stastics.loc['mean'][1:] # [value1, value2, value3]

    return {name: mean_values}

def draw_curve(arrs):
    x_name = ['Band 1 0.5-0.59', 'Band 2 0.61-0.68', 'Band 3 0.79-0.89']
    # print(arrs)
    for arr in arrs:
        for key, value in arr.items():
            plt.plot(value, label= key)
    plt.legend()
    # x-axis
    plt.xticks(range(len(x_name)), x_name)
    # title
    plt.title('Mean reflectance values of different land cover types')
    plt.show()

# 去掉第一个字符的帮助函数
def remove_first_char(s):
    return s[2:]





# exercises\exercise2\vegetation.csv
if __name__ == '__main__':
    arrs = []
    for name in names:
        path = PATH + name + '.csv'
        # print(PATH + name + '.csv')
        df = read_csv(path)
        # print(draw_curve_helper(df, name))
        arrs.append(draw_curve_helper(df, name))
    draw_curve(arrs)
        # print(df.head())
        # print(getStatistics(df))
