# unix command sort and uniq
# output viriety of the column 1.
# command: cut -f1 filename | sort | uniq
require 'set'


temp_line_list = []

fin = open("../data/hightemp.txt")

# extract temperature(column 3), and store it and line 
while line = fin.gets do
  temp_line_list << [line.slice(/\d\d\.\d|\d\d/).to_f, line] 
end

# write file, 
fout = open("../data/sort_temp.txt", 'w')
for num, line in temp_line_list.sort
  fout.write(line)
end


