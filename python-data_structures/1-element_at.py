#!/usr/bin/python3
def element_at(my_list, idx):
    # İndeks mənfidirsə və ya siyahının ölçüsündən böyükdürsə None qaytar
    if idx < 0 or idx >= len(my_list):
        return None
    
    # Əgər indeks düzgündürsə, həmin elementi qaytar
    return my_list[idx]
