#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *

def make_noun_to_root_list(sentence_chunk_list, noun_phrase,  dst, count):
    noun_root = list()
    noun_root.append((noun_phrase, count) )
    while dst != '-1':
        dst = int(dst)
        noun_root.append((sentence_chunk_list[dst].get_phrase(), dst ) )
        dst = sentence_chunk_list[dst].dst
    return noun_root

def print_pass(root_pass_list):

    for first_head_num in range(len(root_pass_list) ):
        for other_head_num in range(first_head_num, len(root_pass_list) ):

            


def get_trace_pass(text_chunk_list):
    noun = '名詞'; count = 0
    root_pass_list = list()
    for sentence_chunk_list in text_chunk_list:
        count = 0
        for chunk in sentence_chunk_list:
            if chunk.check_phrase_pos(noun) and chunk.dst != '-1':
                noun_phrase = chunk.get_phrase()
                root_pass_list.append(make_noun_to_root_list \
                        (sentence_chunk_list, noun_phrase, chunk.dst, count) )

            count += 1     


        print '' 
                

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_trace_pass(text_chunk_list)
