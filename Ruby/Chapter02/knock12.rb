# impliment unix command 'cut -d \t -fn'
# this command is cut column



fin = open("../data/hightemp.txt")
col1, col2 = open("../data/col1.txt", 'w'), open("../data/col2.txt", 'w')


fin.each {|line|
  fields = line.split(/\t/)
  col1.write(fields[0] + "\n")
  col2.write(fields[1] + "\n")
}


