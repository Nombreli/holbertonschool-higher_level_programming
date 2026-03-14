#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # sys.argv[1:] arqumentləri götürür (skriptin adını çıxmaqla)
    # Onları tam ədədə (int) çevirib cəmləyirik
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
