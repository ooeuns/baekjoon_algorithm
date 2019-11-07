nums = [int(input()) for _ in range(10)]
mod = []
for num in nums:
    mod.append(num%42)
mod = set(mod)
print(len(mod))
