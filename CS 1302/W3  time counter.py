seconds = int(input())
hour=seconds//3600
second1=seconds%3600
mint=second1//60
second=second1%60
print(f"{hour:02d}:{mint:02d}:{second:02d}")