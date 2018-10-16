f = open("yeast.fasta", 'r')
lines = f.readlines()
line_num = 0
header_num = 0
for line in lines:
    line_num += 1
    if line[0] == '>':
        header_num += 1
print "line number: %s" % line_num
print "header number: %s" % header_num
