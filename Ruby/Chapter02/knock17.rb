# unix command sort and uniq
# output viriety of the column 1.
# command: cut -f1 filename | sort | uniq
require 'set'


word_list = Set.new

fin = open("../data/hightemp.txt")

# extract string of field 1 and store set with it
while line = fin.gets do
  word_list << line.slice(/[^\t]+/)
end


# write file
fout = open("../data/differences.txt", 'w')
for word in word_list
   fout.write(word + "\n")
end


