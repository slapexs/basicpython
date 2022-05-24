# Short if/else

score = 66

if score >= 50:
    print("Pass")
else:
    print("Fail")

def showtext(msg):
    print(msg)

# Ternary operator
print("Pass") if score >= 70 else showtext("Fail")