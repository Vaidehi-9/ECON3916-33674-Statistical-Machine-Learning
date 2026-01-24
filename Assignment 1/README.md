# ============================================================================
# The Cost of Living Crisis: A Data-Driven Analysis
# Student Price Index vs. National CPI Comparison
# Author: [Vaidehi P]
# Date: January 2026
# ============================================================================

# INSTALLATION
# Run this first if fredapi is not installed
# !pip install fredapi

# ============================================================================
# PART 1: MANUAL BASKET CONSTRUCTION & INFLATION CALCULATION
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# Manual Data Construction: Student Basket (2016 vs 2024)
student_basket = [
    {'Item': 'Tuition', 'Price_2016': 45000, 'Price_2024': 58000},
    {'Item': 'Rent (1 Bed)', 'Price_2016': 1200, 'Price_2024': 1800},
    {'Item': 'Chipotle Burrito', 'Price_2016': 7.50, 'Price_2024': 11
