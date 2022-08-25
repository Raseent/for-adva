import re
txt="the train in spain"
x=re.search("^the",txt)
if x:
    print("found")
else:
    print("npt found")
    