from collections import deque

portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

peaks = deque([
    [80, "Vihren"],
    [90, "Kutelo"],
    [100, "Banski Suhodol"],
    [60, "Polezhan"],
    [70, "Kamenitza"]
])

conquered_peaks = []
days = 7
for index in range(days):
    current_portion = portions.pop()
    current_stamina = stamina.popleft()
    result = current_portion + current_stamina
    if not peaks:
        break
    current_peak_level, current_peak_name = peaks[0]
    if result >= current_peak_level:
        conquered_peaks.append(current_peak_name)
        peaks.popleft()


if peaks:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:
    print("Conquered peaks:")
    [print(peak) for peak in conquered_peaks]
