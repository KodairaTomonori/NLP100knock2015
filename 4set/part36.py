#coding: utf-8

from part30 import *
        
if __name__ == "__main__":
  import sys
  from collections import defaultdict
  mecab_file = open(sys.argv[1], 'r')
  
  base = 'base'
  
  word_frequency = defaultdict(lambda:0)
  
  line_list = makeLineList(mecab_file)
  for morpheme_list in line_list:
    for morpheme_dict in morpheme_list:
      word_frequency[morpheme_dict[base] ] += 1
      
  count = 1
  for word, frequency in sorted(word_frequency.items(), key = lambda x:-x[1]):
    print word, frequency
    count += 1
    if count > 10: break