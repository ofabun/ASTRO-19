#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:30:40 2026

@author: oliver
"""

import numpy as np

def main():
    # generating values  0 to 2 (inclusive)
    x = np.linspace(0, 2*np.pi, 1000)

    # finding values after executing sin(x)
    y = np.sin(x)

    # print as a simple table
    print("x\tsin(x)")
    for xi, yi in zip(x, y):
        print(f"{xi:.6f}\t{yi:.6f}")


if __name__ == "__main__":
    main()