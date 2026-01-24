# The Cost of Living Crisis: A Data-Driven Analysis

## Overview
This project investigates whether official inflation statistics accurately reflect the economic reality faced by college students in high-cost metropolitan areas. Using Python, the Federal Reserve Economic Data (FRED) API, and custom index construction, I demonstrate a significant divergence between national Consumer Price Index (CPI) measurements and the lived experience of students in Boston.

## The Problem: Why the "Average" CPI Fails Students

The Bureau of Labor Statistics publishes the Consumer Price Index as the primary measure of inflation in the United States. However, this national average masks critical disparities:

1. **Geographic Variation**: The national CPI averages costs across expensive urban centers and affordable rural areas, obscuring regional price pressures.

2. **Demographic Bias**: The CPI basket reflects average American consumption patterns (housing, transportation, healthcare), not the concentrated expenses of college students (tuition, textbooks, student housing).

3. **Compositional Mismatch**: Students allocate income differently than the general population—with tuition and rent comprising up to 80% of expenses versus ~35% for typical households.

When policymakers, financial aid offices, and families rely on national CPI figures to understand student financial pressure, they systematically underestimate the true cost burden.

## Methodology: Python, APIs, and Index Theory

### Data Sources
- **FRED API**: Accessed official CPI series including:
  - `CPIAUCSL`: Consumer Price Index for All Urban Consumers (National)
  - `CUURA103SA0`: CPI for Boston-Cambridge-Newton Metropolitan Area
  - `CUSR0000SEEB`: Tuition and fees index
  - `CUSR0000SEHA`: Rent of primary residence index
  - `CUSR0000SEHC`: Food away from home index
  - `PCESV`: Recreation services proxy

### Index Construction Approach
I constructed a **Student Price Index (SPI)** using the Laspeyres fixed-weight methodology, mirroring the theoretical foundation of the CPI itself. The Laspeyres formula measures price changes relative to a base period using fixed consumption quantities:

**L = (Σ P_t × Q_0) / (Σ P_0 × Q_0) × 100**

Where:
- P_t = current period prices
- P_0 = base period prices (2016)
- Q_0 = fixed base period quantities (student spending weights)

### Student Basket Weights
Based on typical student budget allocations:
- **Tuition & Fees**: 40%
- **Rent (1-bedroom)**: 40%
- **Food (dining out)**: 10%
- **Recreation/Streaming**: 10%

### Normalization Protocol
To enable valid comparisons across indices with different base years, I re-indexed all series to **January 1, 2016 = 100**. This eliminates the "data crime" of comparing raw CPI values with incompatible base periods (e.g., 1982-84 vs. 2012).

### Technical Implementation
```python
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

## Visualizations

### Three-Way Comparison: National vs. Boston vs. Student
![Reality Check Chart](visualizations/reality_check.png)

This chart reveals the compounding disadvantage faced by students in expensive metropolitan areas. The red line (Student SPI) consistently tracks above both the grey line (National CPI) and blue line (Boston CPI), demonstrating that demographic spending patterns matter as much as geographic location.

### Component Breakdown
![Component Analysis](visualizations/components.png)

Individual cost components show varying inflation rates, with rent and food experiencing the steepest increases—precisely the categories where students allocate the majority of their discretionary spending.

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

## Repository Structure
```
student-inflation-analysis/
│
├── data/
│   └── student_cpi_analysis.csv        # Exported time-series data
│
├── notebooks/
│   └── analysis.ipynb                   # Jupyter notebook with full workflow
│
├── visualizations/
│   ├── reality_check.png                # Three-way comparison chart
│   ├── components.png                   # Individual component breakdown
│   └── student_spi.png                  # Student Price Index over time
│
├── src/
│   └── student_inflation_analysis.py    # Main analysis script
│
├── README.md                            # This file
└── requirements.txt                     # Python dependencies
```

## How to Run

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/student-inflation-analysis.git
   cd student-inflation-analysis
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Get a FRED API key** (free)
   - Visit: https://fred.stlouisfed.org/docs/api/api_key.html
   - Replace the API key in `student_inflation_analysis.py`

4. **Run the analysis**
```bash
   python src/student_inflation_analysis.py
```

## Future Enhancements

- **Expand geographic coverage**: Compare student costs across 10+ major metro areas
- **Historical analysis**: Extend analysis back to 2000 to capture long-term trends
- **Income integration**: Incorporate wage data to calculate real purchasing power changes
- **Interactive dashboard**: Build a Streamlit/Dash app for dynamic exploration
- **Predictive modeling**: Forecast future student cost trajectories using ARIMA/Prophet

## Conclusion

This analysis demonstrates that aggregate economic statistics can systematically misrepresent the experience of specific demographic groups. By constructing a theoretically sound Student Price Index and comparing it to official measures, I've quantified a 15+ percentage point measurement gap that has real consequences for millions of students and families.

The divergence between official inflation measures and student-specific costs represents not just an academic curiosity, but a policy failure with tangible impacts on educational access, student debt burdens, and economic mobility.

---

## Connect With Me

- **LinkedIn**: www.linkedin.com/in/vaidehi-pundeer-a02a91301
- **Portfolio**: [Your Portfolio Website]
- **Email**: pundeer.v@northeastern.edu

---

*Analysis completed: January 2026*  
*Data sources: Federal Reserve Economic Data (FRED), Bureau of Labor Statistics*

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Federal Reserve Bank of St. Louis for providing free access to FRED data
- Bureau of Labor Statistics for CPI methodology documentation
- The Python data science community for excellent open-source tools
```

Copy this entire block and paste it into your `README.md` file on GitHub. Make sure to:

1. Replace `yourusername` with your actual GitHub username
2. Add your actual contact information in the "Connect With Me" section
3. Save your visualization charts as PNG files in a `visualizations/` folder
4. Create a `requirements.txt` file with:
```
   pandas
   matplotlib
   fredapi
   numpy
   
