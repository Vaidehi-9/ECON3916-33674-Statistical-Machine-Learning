# 🍔 Global Purchasing Power Parity Analysis via the Big Mac Index

## Objective

This project applies **"Burgernomics"** to empirically test the **Law of One Price** by analyzing currency valuation through the standardized pricing of Big Mac hamburgers across international markets.

## Methodology

- **Data Construction**: Manually ingested 2015 Big Mac Index data from The Economist using Python dictionaries, capturing local prices and official exchange rates across multiple countries
- **PPP Calculation**: Computed implied Purchasing Power Parity (PPP) exchange rates by comparing local Big Mac prices to the US benchmark price
- **Valuation Analysis**: Calculated percentage over/undervaluation of currencies relative to the US Dollar, identifying potential arbitrage opportunities and deviations from PPP theory
- **Technical Implementation**: Leveraged Pandas DataFrames for data manipulation, currency conversion, and comparative analysis

## Key Findings

[**Note**: Replace this section with your actual results. Here's a template:]

The analysis revealed significant deviations from purchasing power parity across global markets:

- The **Norwegian Krone** exhibited overvaluation of approximately **X%** against the USD, suggesting Big Macs are significantly more expensive in Norway after adjusting for exchange rates
- Conversely, the **[Currency Name]** showed undervaluation of **Y%**, indicating potential arbitrage opportunities if transaction costs were negligible
- These findings highlight real-world frictions that prevent the Law of One Price from holding perfectly, including trade barriers, tax differentials, labor cost variations, and non-tradable service components in Big Mac production

## Economic Interpretation

While the Law of One Price suggests that identical goods should sell for the same price across countries when expressed in a common currency, this analysis demonstrates that **market imperfections**, **regulatory differences**, and **local economic conditions** create persistent valuation gaps. The Big Mac Index serves as an accessible, if imperfect, proxy for assessing long-term currency misalignment and understanding real-world deviations from theoretical PPP.

## Tools Used

- Python (Data Structures)
- Pandas (Data Analysis)

---

*This project demonstrates foundational skills in currency analysis, international economics, and empirical hypothesis testing.*
