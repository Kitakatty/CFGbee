filename = "regex.py"
text = open(filename).read()
text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
open(filename, "w").write(text)
