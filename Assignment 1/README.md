# Key technical steps:
1. API authentication and time-series retrieval via fredapi
2. DataFrame construction with multiple series alignment
3. Base-year normalization: (series / base_value) × 100
4. Weighted aggregation for custom SPI
5. Comparative visualization using matplotlib
```

## Key Findings

### 1. The Student Inflation Premium
**My analysis reveals a 15.3 percentage point divergence between Student Price Index growth and National CPI inflation from 2016 to 2024.**

While the national CPI increased by approximately 28%, the Student Price Index rose by 43.3%—representing a **"hidden tax"** of over 15 percentage points that doesn't appear in official statistics.

### 2. Regional Amplification Effect
**Boston-area inflation exceeded national rates by 4.7 percentage points**, confirming that geographic location compounds the measurement gap. Students in expensive metros face a double penalty: regional cost pressures AND demographic-specific inflation.

### 3. Component-Level Analysis
Decomposing the Student Price Index reveals asymmetric inflation across categories:

| Category | 2016-2024 Inflation | National CPI Equivalent |
|----------|---------------------|-------------------------|
| Tuition & Fees | 28.9% | ~20% (education CPI) |
| Rent | 50.0% | ~32% (shelter CPI) |
| Food Away from Home | 53.3% | ~38% (food away) |
| Recreation | 25.0% | ~18% (recreation) |

The concentration of student spending in the highest-inflation categories (rent, food) explains the dramatic divergence from the national average.

### 4. Compounding Effect Over Time
The cumulative nature of inflation means small annual gaps compound significantly:
- A 2% annual difference over 8 years results in a 17.2% cumulative divergence
- Students entering college in 2016 faced a cost environment 43% more expensive by 2024, while wage and aid adjustments tracked the "official" 28% increase

## Implications

### For Students and Families
Official inflation figures dramatically understate the true cost of college attendance. Financial planning based on CPI projections will systematically underestimate required savings and borrowing.

### For Policymakers
- **Financial Aid Indexing**: Federal Pell Grant maximums and state aid programs indexed to national CPI fail to keep pace with actual student costs
- **Cost-of-Living Adjustments**: Student loan forbearance policies and income-driven repayment thresholds should account for student-specific inflation
- **Regional Equity**: Flat aid formulas ignore geographic cost variations, penalizing students in high-cost metros

### For Institutions
Universities that index tuition increases to CPI may still outpace student financial capacity when combined with housing and other mandatory costs.

## Technical Skills Demonstrated

- **API Integration**: FRED API authentication, query construction, and time-series retrieval
- **Data Wrangling**: Multi-source DataFrame construction, missing value handling, temporal alignment
- **Index Theory**: Laspeyres methodology implementation, base-year normalization, weighted aggregation
- **Statistical Analysis**: Comparative analysis, divergence quantification, component decomposition
- **Data Visualization**: Multi-series plotting, effective color coding, professional formatting with matplotlib
- **Economic Literacy**: Understanding of CPI construction, inflation measurement, and policy implications

## Tools & Libraries
- **Python 3.x**
- **pandas**: Data manipulation and time-series analysis
- **fredapi**: Federal Reserve Economic Data API wrapper
- **matplotlib**: Statistical visualization
- **NumPy**: Numerical computation

## Conclusion

This analysis demonstrates that aggregate economic statistics can systematically misrepresent the experience of specific demographic groups. By constructing a theoretically sound Student Price Index and comparing it to official measures, I've quantified a 15+ percentage point measurement gap that has real consequences for millions of students and families.

The divergence between official inflation measures and student-specific costs represents not just an academic curiosity, but a policy failure with tangible impacts on educational access, student debt burdens, and economic mobility.

---

**Repository Structure:**
```
/data          # FRED API queries and raw data
/notebooks     # Jupyter analysis workflow
/visualizations # PNG exports of key charts
README.md      # This document
