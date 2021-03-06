#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *


def get_case_pattern(text_chunk_list):
    verb = '動詞'; particle = '助詞'
    get_pattern_flag = False
    for sentence_chunk_list in text_chunk_list:
        check_print = False
        for chunk in sentence_chunk_list:
            get_pattern_flag = False

            particle_words = ''
            for num in chunk.srcs:
                num = int(num)
                if chunk.check_phrase_pos(verb) \
                and sentence_chunk_list[num].check_phrase_pos(particle):
                    particle_words += str(sentence_chunk_list[num].get_pos_word(particle) )
                    get_pattern_flag = True
                    check_print = True
            if get_pattern_flag:
                print chunk.get_pos_word(verb), '\t', particle_words
        if check_print:
            print ''

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_case_pattern(text_chunk_list)
