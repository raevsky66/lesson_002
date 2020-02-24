#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

ml = ((sites['Moscow'][0]-sites['London'][0])**2 +(sites['Moscow'][1]-sites['London'][1])**2)**.5
mp = ((sites['Moscow'][0]-sites['Paris'][0])**2 +(sites['Moscow'][1]-sites['Paris'][1])**2)**.5
lp = ((sites['Paris'][0]-sites['London'][0])**2 +(sites['Paris'][1]-sites['London'][1])**2)**.5

distances["MP"] = mp
distances["ml"] = ml
distances["lp"] = lp


print(distances)




