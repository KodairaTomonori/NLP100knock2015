# Decompose this sentence that is  "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", 
# and get 1 or 2 characters from head.
# In addition, associative array.: from characters to order.
#



#init
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

num = 0
num_gene = Enumerator.new do |y|
  [1, 5, 6, 7, 8, 9, 15, 16, 19, 0].each{|x| y.yield(x)}
end
next_num = num_gene.next

symbol = Hash.new

# process
sentence.split(' ').each{|word|
  num += 1
  get_num = 2
  if num == next_num then
    next_num = num_gene.next
    get_num -= 1
  end
  #puts("order: #{num}, symbol: #{word.slice(0, get_num)}")
  symbol[word.slice(0, get_num)] = num
}

symbol.each_pair {|sym, order| 
  puts("sym : #{sym}, num : #{order}")
}
