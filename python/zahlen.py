import sys

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    out = sys.argv[3]

except Exception as error:
    print("error")
    sys.exit(-1)

out_file = open(out, "a")  # a versucht Datei zu öffnen, wenn nicht da, erstellen
for i in range(start, end):  # range erstellt Zahlen zwischen start & stop
    out_file.write(str(i) + '\n')  # i wird jede Runde einen Wert höher
out_file.close()
