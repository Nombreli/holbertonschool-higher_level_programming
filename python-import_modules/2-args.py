#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # sys.argv-nin ilk elementi faylın adıdır, ona görə onu çıxırıq
    argv = sys.argv[1:]
    count = len(argv)

    # Birinci hissə: Sayın və uyğun sonluğun çapı
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # İkinci hissə: Arqumentlərin siyahısının çapı
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
