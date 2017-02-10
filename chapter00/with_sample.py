import tempfile

with tempfile.TemporaryFile() as temp:
    print('is closed?', temp.closed)  # => is closed? False
    temp.write(b'line 1\n')
    temp.write(b'line 2\n')
    temp.write(b'line 3\n')
    temp.flush()
    temp.seek(0)

    for line in temp:
        print(line)  # => line x

print('is closed?', temp.closed)  # => is closed? True
