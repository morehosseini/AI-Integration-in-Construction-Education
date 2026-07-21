# Worked example: construction cost-data analysis

This is the worked example discussed in the chapter "AI-Assisted Programming for
Construction Professionals". It shows AI-assisted programming at the scale of a
single, self-contained script: a constrained prompt, generated code, and a
result the professional validates.

## Files

- `construction_cost_analysis.py` — the script (reads a CSV, computes budget
  variance per work package, saves a bar chart).
- `sample_cost_data.csv` — a small sample dataset. One row has a missing
  `Actual Cost` value, so the example also demonstrates handling incomplete
  data — common in real construction records.

## Run it

```bash
pip install pandas matplotlib
python construction_cost_analysis.py
```

This produces `cost_variance.png`.

## The point of the example

The code was generated from a natural-language prompt with explicit
constraints (see the header of the script). The constraints — restricting the
libraries, pinning the pandas version, requiring offline operation, and
requiring the code to cope with missing values — are what make the generated
code dependable. Running the script is not the end of the process: the
professional still checks that the column headings matched the file, that
dropping incomplete rows did not discard material data, and that the variances
are consistent with what is known about the project.
