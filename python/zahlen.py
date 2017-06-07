import math
import sys

try:
    start = int(sys.argv[1])  # python script.py *ANFANGSZAHL* endzahl
    end = int(sys.argv[2])  # python script.py anfangszahl *ENDZAHL*
    out = sys.argv[3]  # python script.py anfangszahl endzahl *DATEINAME/SPEICHERORT*

except:
    print("error")  # Fehlermeldung
    sys.exit(-1)  # Beendung des Skripts bei Falscheingabe

template = "{:0%dd}\n" % math.log10(end)  #
with open(out, 'wb') as out_file:  #
    out_file.writelines(template.format(num) for num in xrange(start, end))  #
