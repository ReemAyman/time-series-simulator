# Time Series Simulator
A python project that aims to generate time series data. The data is read from .yaml file which has the following configurations: 
- Start date. 
- End date.
- Sampling frequency.
- Seasonality (Daily, Weekly, and Quarterly).
- Trend.
  - Linear (given slope and magnitude).
- Data type (Additive or Multiplicative). 
- Noise.
  - Percentage (of noise along the generated time series data).
- Outliers.
- Number of missing data points.
  - Percentage.
- Number of datasets generated.

The results are generated in a multiple .csv file format, where each file represents a single dataset.
