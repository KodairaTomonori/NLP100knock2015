# implement unix command 'tail'　
# mendoi syouryaku
#



fin = open("../data/hightemp.txt")
q = Queue.new()
N = ARGV[0].match(/\d+/) ? ARGV[0].to_i : 10

N.times {
  q.enq(1)
}

fin.each {|line|
  q.deq()
  q.enq(line)
}

fin.close()
fout = open("../data/tail.tsv", 'w')
N.times {
  fout.write(q.deq())
}
fout.close()
