# get set from two string which are "paraparaparadise" and "paragraph".
# then culculate union, intersection, and each difference.
# and check  each set include 'se'


# init
require 'set'
require './chapter01-05-n-gram'
include Ngram

str1, str2 = "paraparaparadise", "paragraph"
set1, set2 = Set.new(n_gram(str1, 2)), Set.new(n_gram(str2, 2))



# print result

print "set1: "
p set1

print "set2: "
p set2

print "union: "
p set1 + set2

print "intersection: "
p set1 & set2

print "set1 - set2: "
p set1 - set2

print "set2 - set1: "
p set2 - set1

puts "Does 'se' include set1 ?: #{set1.include?('se')}" 
puts "Does 'se' include set2 ?: #{set2.include?('se')}"
