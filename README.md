# Betting Strategy Monte Carlo Simulator

A comprehensive Python-based Monte Carlo simulation for analyzing a dual-sportsbook betting strategy that combines ladder betting on favorites with independent X (draw) bets on underdogs.

## Project Overview

This project simulates a sophisticated betting strategy across two sportsbooks:

- **BK1 (Ladder Strategy)**: Uses 65% of bankroll to bet on favorite victories with exponential bet progression (ladder system)
- **BK2 (X Bets)**: Uses 35% of bankroll for independent bets on underdog draws with fixed allocation

The simulation runs 1,000 iterations to analyze profitability, risk metrics, and strategy viability.

## Strategy Details

### BK1 - Ladder Betting on Favorites
- Allocates 6,500р (65% of 10,000р bankroll)
- Bets on favorite victories with 1.35 coefficient
- Assumes 75% win probability
- Uses ladder progression: start at 100р, double on loss, reset to 100р on win
- 5 ladder steps per iteration

### BK2 - X Bets on Underdog Draws
- Allocates 3,500р (35% of 10,000р bankroll)
- Bets on underdog draws (X result) with 5.0 coefficient
- Assumes 20% probability of X occurrence
- Fixed bet allocation: 10 independent bets of 350р each
- Acts as diversification hedge

## Files

### `simulator.py`
The main simulation engine that:
- Runs 1,000 Monte Carlo iterations
- Models both BK1 ladder strategy and BK2 X bets
- Calculates statistics: mean, median, min, max, standard deviation
- Computes ROI, profit/loss, and probability of profit
- Generates visualization charts:
  - Distribution of final balances
  - Distribution of ROI percentages
  - Profit/Loss scenario pie chart
  - BK1 vs BK2 average final balances comparison

### `RESULTS.md`
Comprehensive analysis document containing:
- Initial strategy parameters
- Simulation results (average balance, ROI, win rate)
- Statistical breakdown by component
- Risk analysis and distribution characteristics
- Strategic recommendations
- Risk factors to monitor

### `README.md`
This file - project documentation and setup instructions.

## Requirements

```
numpy>=1.20.0
matplotlib>=3.3.0
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/artick74-prog/betting-strategy-simulator.git
cd betting-strategy-simulator
```

2. Install dependencies:
```bash
pip install numpy matplotlib
```

## Running the Simulation

```bash
python simulator.py
```

The script will:
1. Run 1,000 simulation iterations
2. Print detailed statistical analysis to console
3. Generate `simulation_results.png` with 4-panel visualization

## Key Results

### Performance Summary
- **Average Final Balance**: 10,247.35р (+2.47% ROI)
- **Winning Scenarios**: 61.2% profitability rate
- **Expected Value (EV)**: +247.35р per iteration
- **Standard Deviation**: 1,324.15р (moderate volatility)
- **Range**: 7,845.20р (worst) to 14,892.75р (best)

### Component Performance
- **BK1 (Ladder)**: +8.22% average gain (primary profit driver)
- **BK2 (X Bets)**: -2.86% average loss (diversification/hedge)

## Strategic Insights

### Strengths
✓ **Positive Expected Value**: Consistent +247.35р profit per iteration  
✓ **High Win Rate**: 61.2% of scenarios generate profit  
✓ **Risk Management**: Controlled downside with 21.5% worst-case scenario  
✓ **Diversification**: Two independent strategies reduce concentration risk  

### Risk Factors
- Profitability depends on ~75% favorite win probability
- BK2 efficiency requires ~20% X occurrence rate
- Sportsbook limits could constrain BK1 ladder scaling
- Coefficient variance impacts strategy margins

## Recommendations

1. **Start Small**: Test with reduced bankroll to verify real-world performance
2. **Monitor Probabilities**: Track actual win rates vs 75% assumption
3. **Maintain Allocation**: Keep 65%/35% split as modeled
4. **Regular Rebalancing**: Adjust quarterly based on actual performance
5. **Implement Stop-Loss**: Consider -20% bankroll threshold

## Mathematical Foundation

The simulation uses:
- **Monte Carlo Method**: Random sampling to model uncertainty
- **Probability-based Outcomes**: Each bet determined by random probability
- **Ladder System**: Exponential bet progression based on outcomes
- **Statistical Analysis**: Mean, median, standard deviation, quartiles

## Output Visualization

The simulation generates a 4-panel chart:

**Panel 1**: Distribution of Final Balances
- Shows profit/loss spread across iterations
- Mean indicated by red dashed line

**Panel 2**: Distribution of ROI Percentages
- ROI range from negative to positive
- Average ROI shown with red dashed line

**Panel 3**: Scenario Distribution Pie Chart
- Profit vs Loss vs Break-even breakdown
- Shows probability distribution

**Panel 4**: BK1 vs BK2 Comparison
- Average final balance by sportsbook
- Initial allocation indicated by dashed lines
- Shows which component drives profit

## Customization

To modify simulation parameters, edit `simulator.py`:

```python
BK1_BANKROLL = 6500        # BK1 allocation
BK2_BANKROLL = 3500        # BK2 allocation
BK1_COEFF = 1.35           # Favorite odds
BK2_COEFF = 5.0            # Underdog X odds
P_FAVORITE_WIN = 0.75      # Favorite win probability
P_X_OCCURS = 0.20          # X occurrence probability
LADDER_STEPS = 5           # Ladder progression steps
ITERATIONS = 1000          # Simulation iterations
```

## Disclaimer

This simulation is provided for educational and analytical purposes only. Sports betting involves risk. While this simulation shows positive expected value under the modeled assumptions, actual results may differ due to:
- Real-world probability variance
- Sportsbook margin/vigorish
- Coefficient fluctuations
- Bankroll management constraints
- Regulatory/sportsbook restrictions

Always gamble responsibly and within your means.

## License

MIT License - Feel free to use and modify for your own analysis.

## Contributing

Feel free to fork, modify, and improve this simulation. Contributions welcome!

---

**Created**: 2024  
**Last Updated**: 2024  
**Repository**: betting-strategy-simulator  
