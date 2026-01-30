<div align = "center">

# Pearson's R in Linear Regression

</div>

<div align = "justify">

Pearson's correlation coefficient (denoted as R or r) is a statistical measure that quantifies the strength and direction of the linear relationship between two variables. In the context of linear regression, it measures how well the data points fit the regression line.

## Mathematical Definition

Pearson's R is calculated as:

```
R = Σ[(Xi - X̄)(Yi - Ȳ)] / √[Σ(Xi - X̄)² × Σ(Yi - Ȳ)²]

Where:
- Xi = individual x values (time/position in your code)
- Yi = individual y values (price data)
- X̄ = mean of x values
- Ȳ = mean of y values
- Σ = summation
```

## Key Properties

### Range
- Pearson's R ranges from **-1 to +1**
- **R = +1**: Perfect positive linear relationship (all points lie exactly on an upward sloping line)
- **R = -1**: Perfect negative linear relationship (all points lie exactly on a downward sloping line)
- **R = 0**: No linear relationship

### Interpretation

| R Value Range | Interpretation | Trading Context |
|---------------|----------------|-----------------|
| 0.90 to 1.00  | Very strong positive | Strong uptrend with high consistency |
| 0.70 to 0.89  | Strong positive | Clear uptrend with good reliability |
| 0.50 to 0.69  | Moderate positive | Uptrend with some noise |
| 0.30 to 0.49  | Weak positive | Slight uptrend tendency |
| 0.00 to 0.29  | Very weak/None | No clear trend |
| -0.29 to 0.00 | Very weak/None | No clear trend |
| -0.49 to -0.30| Weak negative | Slight downtrend tendency |
| -0.69 to -0.50| Moderate negative | Downtrend with some noise |
| -0.89 to -0.70| Strong negative | Clear downtrend with good reliability |
| -1.00 to -0.90| Very strong negative | Strong downtrend with high consistency |

## Relationship with R² (Coefficient of Determination)

- **R² = R × R** (R squared)
- R² represents the proportion of variance in the dependent variable that is predictable from the independent variable
- R² ranges from 0 to 1 (always positive)
- **R² = 0.81** means 81% of the price variation is explained by the linear trend

## How It's Calculated in Your Code

Looking at the `linearDeviation` function (lines 150-189 in the original code):

```pine
dsxx = 0.0  // Sum of squared deviations of price from average
dsyy = 0.0  // Sum of squared deviations of fitted values from mean
dsxy = 0.0  // Sum of cross products

for i = 0 to periods by 1
    price := source[i]
    dxt = price - average              // Deviation of actual price from mean
    dyt = interceptCopy - daY          // Deviation of fitted value from mean
    
    dsxx += math.pow(dxt, 2)           // Accumulate squared deviations
    dsyy += math.pow(dyt, 2)
    dsxy += dxt * dyt                   // Accumulate cross products

pearsonsR = dsxx == 0 or dsyy == 0 ? 0 : dsxy / math.sqrt(dsxx * dsyy)
```

This implements the formula:
```
R = dsxy / √(dsxx × dsyy)
```

## Practical Trading Applications

### 1. Trend Strength Assessment
- **High |R|** (close to ±1): The trend is strong and consistent
  - More reliable for projecting future prices
  - Breakouts from channels are more significant
  
- **Low |R|** (close to 0): The trend is weak or non-existent
  - Price is ranging or choppy
  - Linear regression may not be appropriate
  - Consider switching to different analysis methods

### 2. Risk Management
- **R > 0.7**: Strong trend
  - Trend-following strategies may work well
  - Channel breakouts are more reliable signals
  
- **|R| < 0.5**: Weak or no trend
  - Mean-reversion strategies might be more appropriate
  - Higher risk for trend-following approaches

### 3. Model Selection
- **Linear vs Exponential**: 
  - If linear R is low but price shows clear directional movement, consider exponential regression
  - Cryptocurrencies often exhibit exponential rather than linear growth patterns

### 4. Channel Reliability
- **High R**: 
  - Upper and lower channels are more reliable support/resistance levels
  - Price is more likely to respect channel boundaries
  
- **Low R**: 
  - Channels are less reliable
  - Price movements are more random
  - Wider stop-losses may be needed

## Why Pearson's R is NOT Calculated for Exponential Regression

In your code, Pearson's R is only shown for linear regression. This is because:

1. **Linear Relationship Measure**: Pearson's R specifically measures LINEAR correlation
   
2. **Exponential Transformation**: 
   - Exponential regression transforms data: `ln(y) = mx + b`
   - The correlation in log-space doesn't directly translate to the original price space
   
3. **Alternative Metrics**: For exponential regression, other measures are more appropriate:
   - R² in log-space
   - Root Mean Square Error (RMSE)
   - Mean Absolute Percentage Error (MAPE)

## Example Interpretation

If your indicator shows:
- **R = 0.85** on a stock chart

This means:
- There's a strong positive linear relationship (85% correlation)
- About **72% (0.85²)** of price variance is explained by the linear trend
- The regression line is a good fit for the data
- Trend-following strategies have higher probability of success
- Channel breakouts should be taken seriously
- The upper/lower deviation channels are reliable support/resistance zones

## Limitations

1. **Only Measures Linear Relationships**
   - Won't detect curved, exponential, or other non-linear patterns
   - A low R doesn't mean no relationship exists, just no LINEAR relationship

2. **Sensitive to Outliers**
   - Extreme price spikes can significantly affect R
   - Consider using robust regression methods for volatile assets

3. **No Causation**
   - High R doesn't imply causation
   - Past correlation doesn't guarantee future correlation

4. **Time-Dependent**
   - R changes as you adjust the lookback period
   - Different timeframes may show different correlation strengths

## Best Practices

1. **Use with Other Indicators**: Don't rely solely on R for trading decisions
2. **Monitor Changes**: Watch how R evolves over time
3. **Adjust Lookback Period**: Test different periods to find optimal settings
4. **Combine with Volume**: High R with high volume strengthens the signal
5. **Consider Market Context**: R interpretation varies by asset class and market conditions

</div>
