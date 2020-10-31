import tempfile

tmp = tempfile.NamedTemporaryFile()

# Open the file for writing. And write the data.
with open(tmp.name, 'w') as f:
    f.write("James|22|M\n")
    f.write("Sarah|31|F\n")
    f.write("Mindy|25|F")

# Read in the data from our file, line by line
with open(tmp.name, "r") as f:
    for line in f:
      print(line)