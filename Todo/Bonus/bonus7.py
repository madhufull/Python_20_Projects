filenames = ["1.doc", "2.presentation", "3.report"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)
