"""
Construction cost-data analysis — worked example.

Companion code for the chapter "AI-Assisted Programming for Construction
Professionals". This is the script discussed in the chapter's worked example:
it reads a CSV of construction cost data, computes budget variance per work
package, and saves a bar chart.

It was generated with AI assistance from a constrained prompt:

    Write a Python script that analyses construction cost data from a CSV file.
    Constraints:
      - Use only the pandas and matplotlib libraries.
      - Do not call external APIs or require internet access.
      - Do not use deprecated pandas functions (target pandas 1.5 or later).
      - Handle missing or invalid values rather than failing on them.
      - For each work package, calculate the variance between budgeted and
        actual cost.
      - Produce a bar chart of cost variance by work package and save it as an
        image file.

Run:  python construction_cost_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_cost_data.csv")
df.columns = df.columns.str.strip().str.lower()
df = df.dropna(subset=["budgeted_cost", "actual_cost"])

df["variance"] = df["actual_cost"] - df["budgeted_cost"]
summary = df.groupby("work_package")["variance"].sum().sort_values()

colours = (summary > 0).map({True: "firebrick", False: "seagreen"})
summary.plot(kind="bar", color=colours)
plt.ylabel("Cost variance (positive = over budget)")
plt.tight_layout()
plt.savefig("cost_variance.png", dpi=150)
print("Saved cost_variance.png")
