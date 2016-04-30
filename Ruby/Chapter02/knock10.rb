# implement unix command `wc'
# this command is counting lines.



fin = open("../data/hightemp.txt")
count = 0
fin.each {|line|
  count += 1
}

p count
