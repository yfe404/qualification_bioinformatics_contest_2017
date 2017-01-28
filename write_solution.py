
f = open('result.mordor')
values = [ int(x) for x  in f.readline().split(" ") ]
reads = []
order = []

line = f.readline()

while line:
  reads.append(line.strip())
  line = f.readline()

f.close()

order = values [2*len(reads):-1]
pairs = values [0:2*len(reads)]
print (pairs)
#print( order)
#print (reads)


cursor = 1
solution_as_array = []
solution_indices = [ 0 for x in order ]

for i in range(0, len(reads)):
#  print(order[i])
#  print (i, " ", order[i] ) 
#  print (order)
#  print ((pairs[2*order[i]], pairs[2*order[i]+1]))
  if pairs[2*order[i]] ==  pairs[2*order[i]+1] and pairs[2*order[i]] == 0:
    solution_indices[order[i]] = -1
  else :
    r = reads[order[i]]
    solution_as_array.append(r)
    solution_indices[order[i]] = cursor
    cursor += len(r)

#print (solution_as_array)
#print (solution_indices)
print( "".join(solution_as_array))

for index in solution_indices:
  print (index)
