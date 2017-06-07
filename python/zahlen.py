# python script.py anfangszahl endzahl dateiname
import math
import sys

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    out = sys.argv[3]

except:
    print("error")
    sys.exit(-1)

template = "{:0%dd}\n" % math.log10(end)
with open(out, 'wb') as out_file:
    out_file.writelines(template.format(num) for num in xrange(start, end))
    
