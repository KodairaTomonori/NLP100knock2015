#coding: utf-8


from part36 import *
import matplotlib.pyplot as plt

def plotBarChart(top10_words):
  X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  Y =  top10_words.values()
  plt.bar(X, Y, align = 'center')
  key = list()
  for i, j in top10_words.items():
    key.append(i.decode('utf-8'))
  plt.xticks(X, key )
  plt.show()

if __name__ == '__main__':
  import sys

  mecab_file = open(sys.argv[1], 'r')
  top_words = getTopWord(mecab_file)
  plotBarChart(top_words)