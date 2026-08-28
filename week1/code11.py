secs = 3725
h = secs // 3600
m = (secs % 3600) // 60
s = secs % 60
print(f"{h}:{m:02d}:{s:02d}")