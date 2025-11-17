import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Strategy Parameters
BK1_BANKROLL = 6500  # 65% allocated to ladder strategy
BK2_BANKROLL = 3500  # 35% allocated to X bets
BK1_COEFF = 1.35     # Coefficient for favorite wins
BK2_COEFF = 5.0      # Coefficient for underdog X bets
P_FAVORITE_WIN = 0.75    # Probability favorite wins
P_X_OCCURS = 0.20        # Probability of X (draw) on underdog
LADDER_STEPS = 5
ITERATIONS = 1000

# Results storage
results = []

np.random.seed(42)

for iteration in range(ITERATIONS):
    bk1_balance = BK1_BANKROLL
    bk2_balance = BK2_BANKROLL
    total_balance = bk1_balance + bk2_balance
    
    # BK1: Ladder strategy on favorites
    ladder_bet = 100  # Starting bet
    ladder_wins = 0
    ladder_losses = 0
    
    for step in range(LADDER_STEPS):
        if np.random.random() < P_FAVORITE_WIN:
            # Win
            winnings = ladder_bet * (BK1_COEFF - 1)
            bk1_balance += winnings
            ladder_wins += 1
            ladder_bet = 100  # Reset to base
        else:
            # Loss - double bet for next attempt
            bk1_balance -= ladder_bet
            ladder_losses += 1
            ladder_bet *= 2
            if bk1_balance <= 0:
                bk1_balance = 0
                break
    
    # BK2: Independent X bets
    num_x_bets = 10
    x_wins = 0
    x_losses = 0
    bet_amount = BK2_BANKROLL / num_x_bets
    
    for bet in range(num_x_bets):
        if np.random.random() < P_X_OCCURS:
            winnings = bet_amount * (BK2_COEFF - 1)
            bk2_balance += winnings
            x_wins += 1
        else:
            bk2_balance -= bet_amount
            x_losses += 1
            if bk2_balance <= 0:
                bk2_balance = 0
                break
    
    # Calculate final balance
    final_balance = bk1_balance + bk2_balance
    profit_loss = final_balance - (BK1_BANKROLL + BK2_BANKROLL)
    roi = (profit_loss / (BK1_BANKROLL + BK2_BANKROLL)) * 100
    
    results.append({
        'final_balance': final_balance,
        'profit_loss': profit_loss,
        'roi': roi,
        'bk1_balance': bk1_balance,
        'bk2_balance': bk2_balance,
        'ladder_wins': ladder_wins,
        'ladder_losses': ladder_losses,
        'x_wins': x_wins,
        'x_losses': x_losses
    })

# Analysis
final_balances = [r['final_balance'] for r in results]
rois = [r['roi'] for r in results]
profits = [r['profit_loss'] for r in results]

print('\n=== BETTING STRATEGY SIMULATION RESULTS ===')
print(f'Iterations: {ITERATIONS}')
print(f'\nStarting Bankroll: {BK1_BANKROLL + BK2_BANKROLL}р')
print(f'  BK1 (Ladder): {BK1_BANKROLL}р')
print(f'  BK2 (X bets): {BK2_BANKROLL}р')
print(f'\nAverage Final Balance: {np.mean(final_balances):.2f}р')
print(f'Median Final Balance: {np.median(final_balances):.2f}р')
print(f'Min Final Balance: {np.min(final_balances):.2f}р')
print(f'Max Final Balance: {np.max(final_balances):.2f}р')
print(f'Std Dev: {np.std(final_balances):.2f}р')
print(f'\nAverage Profit/Loss: {np.mean(profits):.2f}р')
print(f'Average ROI: {np.mean(rois):.2f}%')
print(f'\nWinning Scenarios: {sum(1 for p in profits if p > 0)} ({100*sum(1 for p in profits if p > 0)/len(profits):.1f}%)')
print(f'Losing Scenarios: {sum(1 for p in profits if p < 0)} ({100*sum(1 for p in profits if p < 0)/len(profits):.1f}%)')
print(f'Break-even: {sum(1 for p in profits if p == 0)} ({100*sum(1 for p in profits if p == 0)/len(profits):.1f}%)')
print(f'\nExpected Value (EV): {np.mean(profits):.2f}р')
print(f'Probability of Profit: {sum(1 for p in profits if p > 0) / len(profits) * 100:.1f}%')

print('\n=== STRATEGY STATISTICS ===')
avg_ladder_wins = np.mean([r['ladder_wins'] for r in results])
avg_ladder_losses = np.mean([r['ladder_losses'] for r in results])
avg_x_wins = np.mean([r['x_wins'] for r in results])
avg_x_losses = np.mean([r['x_losses'] for r in results])

print(f'Avg BK1 Ladder Wins: {avg_ladder_wins:.2f}')
print(f'Avg BK1 Ladder Losses: {avg_ladder_losses:.2f}')
print(f'Avg BK2 X Wins: {avg_x_wins:.2f}')
print(f'Avg BK2 X Losses: {avg_x_losses:.2f}')
print(f'\nAvg BK1 Final Balance: {np.mean([r["bk1_balance"] for r in results]):.2f}р')
print(f'Avg BK2 Final Balance: {np.mean([r["bk2_balance"] for r in results]):.2f}р')

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Betting Strategy Monte Carlo Simulation Results (1000 iterations)', fontsize=16, fontweight='bold')

# Histogram of final balances
axes[0, 0].hist(final_balances, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].axvline(np.mean(final_balances), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(final_balances):.0f}р')
axes[0, 0].set_xlabel('Final Balance (р)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Distribution of Final Balances')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Histogram of ROI
axes[0, 1].hist(rois, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
axes[0, 1].axvline(np.mean(rois), color='red', linestyle='--', linewidth=2, label=f'Mean ROI: {np.mean(rois):.2f}%')
axes[0, 1].set_xlabel('ROI (%)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of ROI')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Profit/Loss pie chart
win_count = sum(1 for p in profits if p > 0)
lose_count = sum(1 for p in profits if p < 0)
break_count = sum(1 for p in profits if p == 0)
axes[1, 0].pie([win_count, lose_count, break_count], labels=['Profit', 'Loss', 'Break-even'], 
              colors=['green', 'red', 'gray'], autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Scenarios Distribution')

# BK1 vs BK2 average balances
bk1_avgs = np.mean([r['bk1_balance'] for r in results])
bk2_avgs = np.mean([r['bk2_balance'] for r in results])
axes[1, 1].bar(['BK1 (Ladder)', 'BK2 (X Bets)'], [bk1_avgs, bk2_avgs], color=['steelblue', 'coral'])
axes[1, 1].axhline(BK1_BANKROLL, color='steelblue', linestyle='--', alpha=0.5, label='BK1 Initial')
axes[1, 1].axhline(BK2_BANKROLL, color='coral', linestyle='--', alpha=0.5, label='BK2 Initial')
axes[1, 1].set_ylabel('Average Balance (р)')
axes[1, 1].set_title('Average Final Balances by Sportsbook')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('simulation_results.png', dpi=100, bbox_inches='tight')
print('\nChart saved as simulation_results.png')

print('\n=== CONCLUSION ===')
if np.mean(profits) > 0:
    print(f'Strategy is PROFITABLE with average EV of {np.mean(profits):.2f}р per iteration')
else:
    print(f'Strategy is NOT PROFITABLE with average loss of {abs(np.mean(profits)):.2f}р per iteration')

if sum(1 for p in profits if p > 0) / len(profits) > 0.5:
    print('Probability of profit exceeds 50% - strategy shows potential')
else:
    print('Probability of profit is below 50% - strategy needs refinement')
