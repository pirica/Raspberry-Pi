import sys

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    out = sys.argv[3]
except:
    print("error")
    sys.exit(-1)
    
out_file = open(out, "a")
for i in range(start, end):
    out_file.write(str(i)+'\n')
out_file.close()
