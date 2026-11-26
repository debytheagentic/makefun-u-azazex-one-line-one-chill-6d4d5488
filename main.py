import os

ENTRY = "The locksmith had my new locks on in five minutes, then wouldn't come in to test them, and kept watching the hallway behind me."


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
