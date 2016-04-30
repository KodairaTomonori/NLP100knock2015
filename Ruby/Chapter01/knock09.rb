# typoglycemia program
# - if shuffle characters of a word without head and tail character,
#   the shuffled word is understanded.
# apply a sentence that is "I couldn't believe that I could actually understand what I was reading 
# : the phenomenal power of the human mind ."


def typoglycemia(word)
  if word.length < 3 
    return word
  end
  return word[0] + word.slice(1..-2).split('').shuffle.join + word[-1]
end


def sentence_typoglycemia(sentence)
  applyed_wordlist = []
  sentence.split(' ').each{|word| 
    applyed_wordlist.push(typoglycemia(word))
  }
  return applyed_wordlist.join(' ')
end

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

p sentence_typoglycemia(sentence)
