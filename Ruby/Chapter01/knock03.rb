# out put circle ratio(π), but not culcurate.
# count each word length in this sentence: "Now I need a dring, alcoholic of course, after the heavy lectures involving quantum mechanics."


sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

sentence.gsub(/[.,]/, '').split(' ').each{|word|
  print(word.length)
}
puts()
