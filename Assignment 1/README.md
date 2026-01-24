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
    {'Item': 'Chipotle Burrito', 'Price_2016': 7.50, 'Price_2024': 11.50},
    {'Item': 'Recreation', 'Price_2016': 400, 'Price_2024': 500},
]

# Define the Inflation Calculation Function
def calculate_inflation(base, current):
    """Calculate percentage change between base and current price"""
    return ((current - base) / base) * 100

# Calculate and Display Individual Item Inflation
print("=" * 60)
print("INDIVIDUAL ITEM INFLATION RATES (2016-2024)")
print("=" * 60)
for item in student_basket:
    rate = calculate_inflation(item['Price_2016'], item['Price_2024'])
    print(f"{item['Item']:<20}: {rate:>6.2f}% Inflation")
print("=" * 60)

# ============================================================================
# PART 2: FETCH OFFICIAL CPI DATA FROM FRED
# ============================================================================

# Initialize FRED API (Replace with your API key)
fred = Fred(api_key='ef2d505eb7284a52a07c876e73d6ce20')

# Fetch National CPI Series
print("\nFetching data from FRED...")
official_cpi = fred.get_series('CPIAUCSL')  # National CPI-U
tuition = fred.get_series('CUSR0000SEEB')  # Tuition and fees
rent = fred.get_series('CUSR0000SEHA')  # Rent of primary residence
chipotle_burrito = fred.get_series('CUSR0000SEHC')  # Food away from home
recreation = fred.get_series('PCESV')  # Recreation services

# ============================================================================
# PART 3: NORMALIZE ALL SERIES TO 2016 = 100
# ============================================================================

# Create DataFrame with all series
df = pd.DataFrame({
    "Official CPI": official_cpi,
    "Tuition": tuition,
    "Rent": rent,
    "Chipotle Burrito": chipotle_burrito,
    "Recreation": recreation
})

# Remove missing values
df = df.dropna()

# Get base year values (2016)
base_values = df[df.index.year == 2016].iloc[0]

# Normalize all series to 2016 = 100
df_indexed = (df / base_values) * 100

# Display base year normalized values
print("\nNormalized Values (2016 = 100):")
print(df_indexed[df_indexed.index.year == 2016].head())

# ============================================================================
# PART 4: VISUALIZE INDIVIDUAL COMPONENTS
# ============================================================================

plt.figure(figsize=(12, 7))
df_indexed.plot(figsize=(12, 7))
plt.title("Individual Cost Components (2016 = 100)", fontsize=14, fontweight='bold')
plt.ylabel("Index Level", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================================
# PART 5: CONSTRUCT WEIGHTED STUDENT PRICE INDEX (SPI)
# ============================================================================

# Define Student Spending Weights (Laspeyres Fixed-Weight Method)
weights = {
    'Tuition': 0.4,  # 40% of student budget
    'Rent': 0.4,  # 40% of student budget
    'Chipotle Burrito': 0.1,  # 10% (food)
    'Recreation': 0.1  # 10% (entertainment)
}

# Calculate Weighted Student Price Index
df_indexed['Student_SPI'] = df_indexed[list(weights.keys())].mul(pd.Series(weights)).sum(axis=1)

# ============================================================================
# PART 6: VISUALIZE STUDENT PRICE INDEX
# ============================================================================

plt.figure(figsize=(12, 7))
plt.plot(df_indexed.index, df_indexed['Student_SPI'],
         marker='o', linestyle='-', color='green', linewidth=2.5)
plt.title("Student Price Index (SPI) - 2016 = 100", fontsize=14, fontweight='bold')
plt.ylabel("SPI Value", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=100, color='black', linestyle=':', linewidth=1, alpha=0.5)
plt.tight_layout()
plt.show()

# ============================================================================
# PART 7: DEMONSTRATE THE "DATA CRIME" (Different Base Years)
# ============================================================================

# Create raw (non-normalized) comparison
df_raw = pd.DataFrame({
    'Tuition CPI': tuition,
    'Recreation / Streaming Proxy': recreation
}).dropna()

plt.figure(figsize=(12, 7))
plt.plot(df_raw.index, df_raw['Tuition CPI'], label='Tuition CPI (Base ~1982)', linewidth=2)
plt.plot(df_raw.index, df_raw['Recreation / Streaming Proxy'], 
         label='Recreation CPI (Base ~2002)', linewidth=2)
plt.title("BAD CHART: Raw CPI Indices with Different Base Years", 
          fontsize=14, fontweight='bold', color='red')
plt.ylabel("Index Level (INCOMPARABLE!)", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("DATA CRIME EXPLANATION:")
print("=" * 60)
print("Comparing raw indices with different base years is misleading")
print("because they measure percent changes from different starting points.")
print("It's like comparing inches to centimeters without conversion!")
print("SOLUTION: Always normalize to a common base year (e.g., 2016 = 100)")
print("=" * 60)

# ============================================================================
# PART 8: FETCH BOSTON REGIONAL CPI
# ============================================================================

# Fetch Boston-Cambridge-Newton CPI
print("\nFetching Boston regional CPI data...")
boston_cpi = fred.get_series('CUURA103SA0')  # Boston-Cambridge-Newton CPI

# Create comprehensive comparison DataFrame
df_comparison = pd.DataFrame({
    'National_CPI': official_cpi,
    'Boston_CPI': boston_cpi,
    'Student_SPI': df_indexed['Student_SPI']
})

# Handle missing values
df_comparison = df_comparison.ffill().dropna()

# Normalize to Jan 1, 2016 = 100
base_date = pd.Timestamp('2016-01-01')
base_values = df_comparison[df_comparison.index >= base_date].iloc[0]
df_comparison_indexed = (df_comparison / base_values) * 100

# ============================================================================
# PART 9: THE ULTIMATE REALITY CHECK (3-Way Comparison)
# ============================================================================

plt.figure(figsize=(14, 8))

# National CPI (Grey)
plt.plot(df_comparison_indexed.index, 
         df_comparison_indexed['National_CPI'], 
         color='grey', 
         linewidth=3, 
         label='National CPI (All Urban Consumers)',
         alpha=0.8)

# Boston CPI (Blue)
plt.plot(df_comparison_indexed.index, 
         df_comparison_indexed['Boston_CPI'], 
         color='blue', 
         linewidth=3, 
         label='Boston-Cambridge-Newton CPI',
         alpha=0.8)

# Student SPI (Red)
plt.plot(df_comparison_indexed.index, 
         df_comparison_indexed['Student_SPI'], 
         color='red', 
         linewidth=3, 
         linestyle='--',
         label='Student Price Index (Custom Basket)',
         alpha=0.9)

# Formatting
plt.title('The Ultimate Reality Check: National vs. Boston vs. Student Inflation', 
          fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Price Index (Jan 2016 = 100)', fontsize=13)
plt.xlabel('Year', fontsize=13)
plt.legend(loc='upper left', fontsize=12, framealpha=0.95, shadow=True)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axhline(y=100, color='black', linestyle=':', linewidth=1.5, alpha=0.6)
plt.tight_layout()
plt.show()

# ============================================================================
# PART 10: QUANTITATIVE ANALYSIS & SUMMARY STATISTICS
# ============================================================================

print("\n" + "=" * 70)
print("THE ULTIMATE REALITY CHECK: HOW MUCH WORSE IS IT FOR STUDENTS?")
print("=" * 70)

# Latest values
latest_date = df_comparison_indexed.index[-1]
national_latest = df_comparison_indexed['National_CPI'].iloc[-1]
boston_latest = df_comparison_indexed['Boston_CPI'].iloc[-1]
student_latest = df_comparison_indexed['Student_SPI'].iloc[-1]

print(f"\n📊 LATEST INDEX VALUES (as of {latest_date.strftime('%B %Y')}):")
print(f"{'National CPI:':<25} {national_latest:>8.2f}")
print(f"{'Boston CPI:':<25} {boston_latest:>8.2f}")
print(f"{'Student SPI:':<25} {student_latest:>8.2f}")

# Cumulative inflation
print(f"\n📈 CUMULATIVE INFLATION SINCE JANUARY 2016:")
national_inflation = national_latest - 100
boston_inflation = boston_latest - 100
student_inflation = student_latest - 100

print(f"{'National:':<25} {national_inflation:>7.1f}%")
print(f"{'Boston:':<25} {boston_inflation:>7.1f}%")
print(f"{'Student:':<25} {student_inflation:>7.1f}%")

# Hidden tax calculation
print(f"\n💰 YOUR 'HIDDEN TAX' (Student vs. National):")
hidden_tax = student_latest - national_latest
print(f"   +{hidden_tax:.1f} percentage points MORE inflation than official CPI!")
print(f"   Translation: If national CPI says prices rose {national_inflation:.1f}%,")
print(f"   your actual costs rose {student_inflation:.1f}% - a {hidden_tax:.1f}% gap!")

# Boston premium
print(f"\n🏙️  BOSTON PREMIUM (Boston vs. National):")
boston_premium = boston_latest - national_latest
print(f"   +{boston_premium:.1f} percentage points")

# Real-world dollar impact
print(f"\n💵 REAL-WORLD IMPACT:")
print(f"   If your 2016 budget was $50,000:")
print(f"   • National CPI predicts: ${50000 * (national_latest/100):,.0f} needed in {latest_date.year}")
print(f"   • Your ACTUAL costs:     ${50000 * (student_latest/100):,.0f} needed in {latest_date.year}")
print(f"   • SHORTFALL:             ${50000 * (student_latest - national_latest)/100:,.0f}")

print("=" * 70)

# ============================================================================
# PART 11: COMPONENT BREAKDOWN TABLE
# ============================================================================

print("\n" + "=" * 70)
print("COMPONENT-LEVEL BREAKDOWN: WHERE THE PAIN COMES FROM")
print("=" * 70)

# Get latest values for each component
tuition_2016 = df_indexed[df_indexed.index.year == 2016]['Tuition'].iloc[0]
tuition_latest = df_indexed['Tuition'].iloc[-1]
tuition_inflation = ((tuition_latest - tuition_2016) / tuition_2016) * 100

rent_2016 = df_indexed[df_indexed.index.year == 2016]['Rent'].iloc[0]
rent_latest = df_indexed['Rent'].iloc[-1]
rent_inflation = ((rent_latest - rent_2016) / rent_2016) * 100

food_2016 = df_indexed[df_indexed.index.year == 2016]['Chipotle Burrito'].iloc[0]
food_latest = df_indexed['Chipotle Burrito'].iloc[-1]
food_inflation = ((food_latest - food_2016) / food_2016) * 100

rec_2016 = df_indexed[df_indexed.index.year == 2016]['Recreation'].iloc[0]
rec_latest = df_indexed['Recreation'].iloc[-1]
rec_inflation = ((rec_latest - rec_2016) / rec_2016) * 100

print(f"\n{'Category':<25} {'Weight':<10} {'Inflation':<15} {'Index Value':<15}")
print("-" * 70)
print(f"{'Tuition & Fees':<25} {weights['Tuition']*100:>6.0f}%     {tuition_inflation:>7.1f}%        {tuition_latest:>8.2f}")
print(f"{'Rent (1 Bedroom)':<25} {weights['Rent']*100:>6.0f}%     {rent_inflation:>7.1f}%        {rent_latest:>8.2f}")
print(f"{'Food Away from Home':<25} {weights['Chipotle Burrito']*100:>6.0f}%     {food_inflation:>7.1f}%        {food_latest:>8.2f}")
print(f"{'Recreation':<25} {weights['Recreation']*100:>6.0f}%     {rec_inflation:>7.1f}%        {rec_latest:>8.2f}")
print("-" * 70)
print(f"{'WEIGHTED AVERAGE (SPI)':<25} {'100%':>9}  {student_inflation:>7.1f}%        {student_latest:>8.2f}")
print("=" * 70)

# ============================================================================
# PART 12: EXPORT DATA FOR PORTFOLIO
# ============================================================================

# Save final comparison data to CSV
output_filename = 'student_cpi_analysis.csv'
df_comparison_indexed.to_csv(output_filename)
print(f"\n✅ Data exported to: {output_filename}")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE!")
print("=" * 70)
print("\n🎯 KEY TAKEAWAYS:")
print(f"   1. Students face {hidden_tax:.1f}pp more inflation than official stats show")
print(f"   2. Boston adds another {boston_premium:.1f}pp premium on top of national rates")
print(f"   3. The concentration in high-inflation categories (rent, tuition) drives the gap")
print(f"   4. Policy decisions based on national CPI systematically underfund student needs")
print("\n📁 Next Steps:")
print("   • Add this analysis to your GitHub portfolio")
print("   • Use the exported CSV for further analysis")
print("   • Share visualizations on LinkedIn")
print("=" * 70)
