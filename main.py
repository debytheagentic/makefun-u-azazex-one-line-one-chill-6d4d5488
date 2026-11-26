import os

ENTRY = "The sleep app kept one recording: at 3:14 a.m., someone in my bed answers a question in my own voice, and gets it wrong."


def main():
    n = len(ENTRY)
    if not 1 <= n <= 200 or not ENTRY.strip():
        print(f"LEN={n}")
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"LEN={n}")


if __name__ == "__main__":
    main()
