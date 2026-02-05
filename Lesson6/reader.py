import sys
import os
import csv


def main():

    if len(sys.argv) < 3:
        print("Using python reader.py <src> <dst> <change1>")
        return

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.exists(src) or not os.path.isfile(src):
        print(f"Error: {src} is not a file or it does not exist")
        folder = os.path.dirname(src) or "."
        print(f"Files in the same folder: {folder}")
        try:
            for name in os.listdir(folder):
                print(" -", name)
        except Exception as e:
            print("Can not list folder:", e)
        return

    try:
        with open(src, newline="", encoding="utf-8") as f:
            data = list(csv.reader(f))
    except Exception as e:
        print("Error in reading CSV:", e)
        return

    for ch in changes:
        parts = ch.split(",", 2)
        if len(parts) != 3:
            print(f"Invalid change: {ch}")
            continue

        x_str, y_str, value = parts

        try:
            x = int(x_str)
            y = int(y_str)
        except ValueError:
            print(f"Invalid change: {ch}")
            continue

        if y < 0 or y >= len(data):
            print(f"Row out of range: {ch}")
            continue

        if x < 0 or x >= len(data[y]):
            print(f"Column out of range: {ch}")
            continue

        data[y][x] = value

    for row in data:
        print(",".join(row))

    try:
        with open(dst, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    except Exception as e:
        print("Error in writing CSV:", e)



if __name__ == "__main__":
    main()