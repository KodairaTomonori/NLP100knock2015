# unix command sort and uniq
# output viriety of the column 1, and count frequency.
# command: cut -f1 filename | sort | uniq -c
require 'set'


word_counter = Hash.new([])
word_counter.default = 1

fin = open("../data/hightemp.txt")

# extract string of field 1 and store map with it's frequency
while line = fin.gets do
  word_counter[line.slice(/[^\t]+/)] += 1
end

# write file, sort by frequency(value)
fout = open("../data/sort_frequency.txt", 'w')
for key, value in word_counter.sort{|a, b| a[1] <=> b[1]}.reverse
     fout.write(value.to_s + "\t" + key + "\n")
end


