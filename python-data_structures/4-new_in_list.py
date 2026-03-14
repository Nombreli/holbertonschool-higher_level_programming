#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Əvvəlcə orijinal siyahının kopyasını yaradırıq
    new_list = my_list[:]

    # İndeks səhvdirsə, birbaşa kopyanı (dəyişiklik etmədən) qaytarırıq
    if idx < 0 or idx >= len(my_list):
        return new_list

    # İndeks düzdürsə, kopyada elementi dəyişirik
    new_list[idx] = element
    return new_list
