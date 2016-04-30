#coding: utf-8


import matplotlib.pyplot as plt
import matplotlib.pyplot as np
def get_score(num, predict_file):
    float_num = num / float(1000)
    all_count = 0
    concord_count = 0
    correct_count = 0
    correct_match_count = 0
    pre_count = 0
    b = 0
    for line in predict_file:
        all_count += 1
        correct, predict, prob = line.split('\t')
        prob = float(prob)
        if prob > float_num:
            predict = '1'
        else:
            predict = '0'
        if correct == predict:
            concord_count += 1
        if correct == '1':
            correct_count += 1
            if correct == predict:
                correct_match_count += 1
        if predict == '1':
           pre_count += 1
    acc = concord_count / float(all_count) if all_count else 1
    pre = correct_match_count / float(pre_count) if pre_count else 1
    rec = correct_match_count / float(correct_count) if correct_count else 1
    f =  2 * rec * pre / (rec + pre)
    predict_file.seek(0)
    return pre, rec



def draw_graph(result):
  acc_list = list() ; rec_list = list()
  for acc, rec in result:
    acc_list.append(acc); rec_list.append(rec)

  #plt.semilogy(freq_list)
  #plt.semilogx(range(0, len(freq_list)))
  plt.plot(acc_list, rec_list)
  plt.title('precision - recall')
  plt.xlabel('precision')
  plt.ylabel('recall')
  plt.show()
  
if __name__ == '__main__':
  import sys

  aa = 0
  predict_file = open(sys.argv[1], 'r')
  result = list()
  for i in range(1000):
      result.append(get_score(i, predict_file) )
  draw_graph(result)
