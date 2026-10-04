contents = ["documents to be here",
            "presentations to be here", "reports to be reported here"]
filenames = ["doc.txt", "presentation.txt", "report.txt"]

for content, filename in zip(contents, filenames):
    file = open(
        f"/Users/madhu/Documents/Study/Python_20_Projects/Todo/files/{filename}", 'w')
    file.write(content)
