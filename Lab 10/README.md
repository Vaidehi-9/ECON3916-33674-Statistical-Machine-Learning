## Structural Forensics: Diagnosing Spurious Correlation in Macroeconomic Time-Series Data

**Tools:** Python · pandas · seaborn · statsmodels · Plotly · FRED API

Macroeconomic variables are rarely independent — but not every correlation is meaningful. This project investigates the "everything is correlated" trap that emerges when working with raw, non-stationary time-series data, using a live basket of five Federal Reserve Economic Data (FRED) indicators: CPI, M2 Money Supply, Industrial Production, the Federal Funds Rate, and Unemployment (2010–2024).

**The analysis proceeds in four methodological stages.** First, raw-level data is ingested via `pandas_datareader` and visualized as a correlation heatmap, exposing near-perfect spurious correlations (e.g., CPI–M2 at r = 0.99) driven by shared upward time trends rather than genuine structural relationships. Second, Variance Inflation Factors (VIF) are calculated using `statsmodels` to quantify multicollinearity across predictors; M2 and Industrial Production return VIF scores exceeding 180, rendering any regression coefficients on raw levels statistically indefensible.

Third, non-stationary variables are transformed into Year-over-Year (YoY) percentage growth rates, removing the common trend component and producing correlations that reflect short-run structural dynamics. Notable findings include the Fed Funds–CPI correlation reversing sign (−0.51 → +0.42), consistent with the Taylor Rule, and the Unemployment–Industrial Production relationship surviving transformation at r = −0.55, validating Okun's Law. Finally, a Directed Acyclic Graph (DAG) formalizes the causal assumptions underlying the data — identifying "Expansionary Macro Policy" as an unobserved fork confounder that generates a backdoor path between M2 and CPI, and clarifying which variables must be conditioned on to satisfy the backdoor criterion.

The project concludes with an interactive Plotly dashboard featuring a dropdown toggle between the raw-level and YoY correlation matrices, built using Plotly's `updatemenus` declarative callback architecture for client-side, zero-latency interactivity.

**Key takeaway:** Statistical correlation is a hypothesis, not a finding. Structural credibility requires stationarity testing, multicollinearity diagnostics, and explicit causal assumptions — all three of which are demonstrated here before a single regression coefficient is trusted.
