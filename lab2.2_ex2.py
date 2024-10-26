x = 100
y = 7.49

print(f"{y}")
print("{0:f} {0:.1f}".format(y, y+1))

print("{:5}\n".format(x))
print(f"{x*2:^5}{x:<5}")

print(f"""->({x:4.2f}+{y:.2f})/3={(x+y)/3:.2f})""")
print("X:{0:<5}\nY:{1:<5.2f}\n".format(x, y))