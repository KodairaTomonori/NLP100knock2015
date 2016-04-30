# impliment unix command 'head -n N'
# pick up from head to Nth row. N from command line.
#


fin = open("../data/hightemp.txt")
N = ARGV[0] != nil ? ARGV[0].to_i : 10
fout = open("../data/head.tsv", 'w')
N.times {|n|
  fin.gets != nil ? fout.write($_) : break
}
fin.close()

