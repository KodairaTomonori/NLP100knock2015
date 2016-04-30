# implement unix command split
# this command is the action of dividing a thing into N parts.

# open file
fin = open("../data/hightemp.txt")
N = (ARGV[0] != nil and ARGV[0].match(/\d+/) != nil) ? ARGV[0].to_i : 2

line_array = []

# count number of columns and store array with lines
line_count = 0
while line = fin.gets
  line_count += 1
  line_array << line
end


split_length = (line_count / N)
line_count = 0
f_num = 0

# write file, each split_length 
for line in line_array do 
  if line_count % split_length == 0 then
    f_num += 1
    fout = open("../data/split_" + f_num.to_s + ".txt", 'w')
  end
  line_count += 1
  fout.write(line)
end
