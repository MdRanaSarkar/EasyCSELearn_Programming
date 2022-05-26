import re
name = "00Rana"
if re.fullmatch('[A-Za-z]{2,25}([A-Za-z]{2,25})?', name):
    print(name)
else:
    print("wrong name")