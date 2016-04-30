# get word bigram and character bigram from sentnece which is "I am an NLPer."
#


module Ngram
  def n_gram(iterable, n)
    # iterable = iterable, n = integer
    n_gram_array = []
    0.upto(iterable.length - n) do |index|
      n_gram_array[index] = iterable.slice(index, n)
    end
    return n_gram_array
  end
end





if $DEBUG then
  # init
  include Ngram
  sentence = "I am an NLPer."

  # character bigram output
  puts("#{n_gram(sentence, 2)}\n")
  # word bigram output
  puts("#{n_gram(sentence.gsub(/[,.]/, '').split(' '), 2)}")
end
