import sys

def cal_medicine(w, h):
    # 기저 사례
    if w == 0 and h == 0:
        return 1

    # 이미 왔던 곳이라면
    if medicine[w][h]: return medicine[w][h]

    if w > 0: medicine[w][h] += cal_medicine(w-1, h+1)
    if h > 0: medicine[w][h] += cal_medicine(w, h-1)

    return medicine[w][h]

while True:
    N = int(sys.stdin.readline())
    if N == 0: break

    medicine = [[0] * 300 for _ in range(300)]
    print(cal_medicine(N, 0))


