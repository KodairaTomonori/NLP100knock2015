# implement unix command `sed -e pattern file'
# this command replace from 'xxx' to 'XXX'
#


fin = open("../data/hightemp.txt")

fin.each {|line|
  print line.gsub(/[\t]/, ' ')
  
}
