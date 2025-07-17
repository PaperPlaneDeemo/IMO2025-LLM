import json
import os
import matplotlib.pyplot as plt
import numpy as np

# Load evaluation data
with open('imo_2025_evaluation.json', 'r') as f:
    data = json.load(f)

models = list(data['models'].keys())
problems = [f'problem_{i+1}' for i in range(data['evaluation_metadata']['total_problems'])]

# Assign 8 distinct colors
COLORS = [
    '#1f77b4',  # blue
    '#ff7f0e',  # orange
    '#2ca02c',  # green
    '#d62728',  # red
    '#9467bd',  # purple
    '#8c564b',  # brown
    '#e377c2',  # pink
    '#7f7f7f',  # gray
]

# Prepare data for plotting
token_counts = {model: [] for model in models}
costs = {model: [] for model in models}

for model in models:
    for prob in problems:
        entry = data['models'][model][prob]
        # Handle null as 0 for grok4
        if model == 'xai_grok_4':
            token = entry['token_count'] if entry['token_count'] is not None else 0
            cost = entry['cost'] if entry['cost'] is not None else 0
        else:
            token = entry['token_count']
            cost = entry['cost']
        token_counts[model].append(token)
        costs[model].append(cost)

# 计算每个模型的总token和总cost
total_token = {model: sum(token_counts[model]) for model in models}
total_cost = {model: sum(costs[model]) for model in models}

# 按总token降序排序模型
sorted_models_by_token = sorted(models, key=lambda m: total_token[m], reverse=True)
# 按总cost降序排序模型
sorted_models_by_cost = sorted(models, key=lambda m: total_cost[m], reverse=True)

x = np.arange(len(problems))  # the label locations
width = 0.09  # the width of the bars

# Plot token_count as grouped bar chart（按总token降序排序）
plt.figure(figsize=(12, 7))
for idx, model in enumerate(sorted_models_by_token):
    plt.bar(x + idx * width, token_counts[model], width, label=model, color=COLORS[idx % len(COLORS)])
plt.title('Token Count per Problem by Model (Sorted by Total Token)')
plt.xlabel('Problem')
plt.ylabel('Token Count')
plt.xticks(x + width * (len(models) - 1) / 2, problems)
plt.legend()
plt.tight_layout()
plt.savefig('plots/token_count_per_problem.png')
plt.close()

# Plot cost as grouped bar chart（按总cost降序排序）
plt.figure(figsize=(12, 7))
for idx, model in enumerate(sorted_models_by_cost):
    plt.bar(x + idx * width, costs[model], width, label=model, color=COLORS[idx % len(COLORS)])
plt.title('Cost per Problem by Model (Sorted by Total Cost)')
plt.xlabel('Problem')
plt.ylabel('Cost (USD)')
plt.xticks(x + width * (len(models) - 1) / 2, problems)
plt.legend()
plt.tight_layout()
plt.savefig('plots/cost_per_problem.png')
plt.close() 