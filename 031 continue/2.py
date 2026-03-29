# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  Misal: cüt ədədləri atlayaraq tək ədədləri yazdırmaq      ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

for i in range(10, 0, -1):
    if i % 2 == 0:
        continue
    print("i`nin dəyəri:", i)

# Output:
# ──> i`nin dəyəri: 9
# ──> i`nin dəyəri: 7
# ──> i`nin dəyəri: 5
# ──> i`nin dəyəri: 3
# ──> i`nin dəyəri: 1