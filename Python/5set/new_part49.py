#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *


def root_word( sentence_chunk_list, dst):
     word_dst = dst
     prev_dst = int(dst)
     while word_dst != '-1':#sentence_chunk_list[int(word_dst)].dst != '-1':
         word_dst = int(word_dst)
         prev_dst = word_dst
         word_dst = sentence_chunk_list[word_dst].dst
     return sentence_chunk_list[prev_dst].get_phrase()

def print_noun_to_root(sentence_chunk_list, noun_num,  other_noun_num):
    match_flag = False
    particle = '助詞'; noun = '名詞'
    minimum_pass = ''
    #phrase_chunk = sentence_chunk_list[noun_num]
    #minimum_pass = chunk.phrase_replace(noun, 'X')
    #phrase_chunk = sentence_chunk_list[phrase_chunk.dst]
    tmp_dst = sentence_chunk_list[noun_num].dst
    next_dst = lambda x: sentence_chunk_list[x].dst
    while 1:
        if tmp_dst == other_noun_num:
            minimum_pass += get_'|\tY'
            break
        elif tmp_dst == '-1':
            minimum_pass += get_noun2root_pass(sentence_chunk_list, noun_num, '-1') + '|'\
                + get_noun2root_pass(sentence_chunk_list, other_noun_num, '-1') + '|'+ root_word(sentence_chunk_list, noun_num)
            break
        else:
            tmp_dst = next_dst(tmp_dst)
           

    print minimum_pass

def get_noun2root_pass(sentence_list, start_num):
    

 '''   
    next_dst = sentence_chunk_list[int(dst)].dst  
    print noun_phrase,
    
    while 1:
        if sentence_chunk_list[int(dst)].dst == '-1':
            break
        print '-> ' + sentence_chunk_list[int(dst)].get_phrase(),
        dst = sentence_chunk_list[int(dst)].dst
        next_dst = sentence_chunk_list[int(dst)].dst
        #print dst, next_dst
'''

def make_phrase_list(sentence_chunk_list, noun_phrase,  dst):
    phrase_list = list()
    phrase_list.append(noun_phrase)
    while sentence_chunk_list[int(dst)].dst != '-1':
        phrase_list.append(sentence_chunk_list[int(dst)].get_phrase() )
        dst = sentence_chunk_list[int(dst)].dst
    return phrase_list
'''
def check_same_phrase(phrase_list1, phrase_list2):
    for phrase in phrase_list1:
        if phrase in phrase_list2:
            return True, phrase

    return False, 'NULL'
'''


def make_minimum_pass(sentence_chunk_list, noun_num_list):
    count = 0
    sub_noun_num_list = list(noun_num_list)
    for noun_chunk_num in noun_num_list:
        count += 1
        for other_noun_chunk_num in non_num_list[count:]:
            print_noun_to_root(sentence_chunk_list, noun_chunk_num, other_noun_chunk_num)

            
            

def make_noun_num_list(sentence_chunk_list):
    noun_num_list = list()
    noun = '名詞'
    for chunk in sentence_chunk_list:
        if chunk.check_phrase_pos(noun):
            noun_num_list.append(chunk.num)
    return noun_num_list

def get_trace_pass(text_chunk_list):
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        noun_num_list = make_noun_num_list(sentence_chunk_list)
        if noun_num_list != []:
            make_minimum_pass(sentence_chunk_list, noun_num_list)

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
