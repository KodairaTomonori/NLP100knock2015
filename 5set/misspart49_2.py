#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *

def make_noun_to_root(sentence_chunk_list, noun_phrase,  dst):
    noun_root ='' 
    noun_root += noun_phrase
    while dst != '-1':
        noun_phrase += ' -> ' + sentence_chunk_list[int(dst)].get_phrase()
        dst = sentence_chunk_list[int(dst)].dst
    return noun_phrase.split(' -> ')

def print_minimum_pass(root_pass_list):
    list_num = len(root_pass_list)
    for top_noun_pass_1 in root_pass_list:
        for other_noun_pass_1 in root_pass_list:
            top_noun_pass = list(top_noun_pass_1)
            other_noun_pass = list(other_noun_pass_1)

            minimum_pass = ''
            match_flag = False
            if top_noun_pass == other_noun_pass or other_noun_pass == [] or top_noun_pass == []:
                continue
            first_word = top_noun_pass.pop(0)
            last_word = top_noun_pass.pop()
            if last_word == other_noun_pass[-1]:
               for phrase in top_noun_pass:
                   if phrase in other_noun_pass:
                       match_flag = True
                       if minimum_pass == '' or minimum_pass == ' ':
                           minimum_pass = first_word + ' -> ' + minimum_pass + ' -> Y'
                       break
                   else:
                       minimum_pass += ' -> ' +  phrase
               if match_flag == False and minimum_pass != '':
                   minimum_pass = first_word + ' | ' + minimum_pass + ' | ' + last_word
               if minimum_pass != '' and minimum_pass != ' -> Y' :
                   print minimum_pass
            else:
                continue


        

def get_trace_pass(text_chunk_list):
    noun = '名詞'
    root_pass_list = list()
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1':
                noun_phrase = chunk.get_phrase()
                root_pass_list.append(make_noun_to_root(sentence_chunk_list, \
                    noun_phrase, chunk.dst) )

        print_minimum_pass(root_pass_list)        

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
