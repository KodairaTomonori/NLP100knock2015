# impliment unix command 'paste'
# this command is connecting each row


col1, col2 = open("../data/col1.txt"), open("../data/col2.txt")
merged = open("../data/merged.tsv", 'w')
while true
  line1, line2 = col1.gets, col2.gets
  if line1 == nil
    break
  end
  merged.write(line1.strip() + "\t" + line2)
end
