<div align="center">

# 🔬 DSKit

### The CLI utility belt for Data Scientists

[![CI](https://github.com/yourusername/dskit/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/dskit/actions)
[![PyPI version](https://badge.fury.io/py/dskit-cli.svg)](https://badge.fury.io/py/dskit-cli)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Inspect · Profile · Clean · Convert · Analyze — all from your terminal.**

No notebooks. No boilerplate. Just data.

</div>

---

## ✨ Why DSKit?

Every data scientist repeats the same 5 tasks at the start of every project:

1. Load a dataset and check its shape, types, and missing values
2. Profile the data to understand distributions
3. Clean duplicates, nulls, and whitespace issues
4. Get quick descriptive statistics
5. Convert between CSV, JSON, Parquet, and Excel

DSKit does all of this in one command. No boilerplate, no notebook startup time, no imports.

---

## 🚀 Installation

```bash
pip install dskit-cli
```

For data profiling support:
```bash
pip install "dskit-cli[profile]"
```

**Requirements:** Python 3.8+

---

## 📖 Commands

### `dskit inspect` — Instant dataset overview

```bash
dskit inspect data.csv
dskit inspect data.parquet --rows 10
```

```
────────────────────────────────────────────────────────────
  📄 Inspecting: data.csv
────────────────────────────────────────────────────────────
  Shape:             10,000 rows × 8 columns
  File size:         1.24 MB
  Memory usage:      632.1 KB
  Duplicates:        47 rows

  Column Info
  Column               Type         Missing    %Missing   Unique
  ··········································································
  user_id              int64        0          0.0        10000
  age                  float64      312        3.1        67
  salary               float64      88         0.9        4821
  city                 object       0          0.0        52
  signup_date          object       0          0.0        1825
  is_active            bool         0          0.0        2
  score                float64      201        2.0        9998
  category             object       0          0.0        5
```

---

### `dskit profile` — Full HTML report

```bash
dskit profile data.csv
dskit profile data.csv --output my_report.html --minimal
```

Generates a rich interactive HTML report powered by `ydata-profiling`, including histograms, correlations, missing value heatmaps, and more.

---

### `dskit clean` — Auto-fix common data issues

```bash
# Drop duplicates
dskit clean data.csv --drop-duplicates --output clean.csv

# Fill missing numeric values with column mean
dskit clean data.csv --fill-na mean --output clean.csv

# Strip whitespace from string columns
dskit clean data.csv --strip-whitespace --output clean.csv

# Combine everything
dskit clean data.csv --drop-duplicates --fill-na median --strip-whitespace --output clean.csv
```

```
────────────────────────────────────────────────────────────
  🧹 Cleaning: data.csv
────────────────────────────────────────────────────────────
  ✓ Dropped 47 duplicate rows
  ✓ Filled NaN values using 'median' strategy
  ✓ Stripped whitespace from 3 string column(s)

  Before: 10,000 rows × 8 cols
  After:  9,953 rows × 8 cols

  ✅ Saved → clean.csv
```

---

### `dskit stats` — Descriptive statistics

```bash
dskit stats data.csv
dskit stats data.csv --col age
dskit stats data.csv --col salary --percentiles
```

```
────────────────────────────────────────────────────────────
  📈 Statistics: data.csv
────────────────────────────────────────────────────────────

  salary
    Count:             9,912
    Missing:           88
    Mean:              72,841.3300
    Std Dev:           18,442.1100
    Min:               22,000.0000
    Max:               195,000.000
    Median:            68,500.0000
    Skewness:          1.2341
    Kurtosis:          2.8810
    P5:                42,000.0000
    P25:               58,000.0000
    P75:               84,000.0000
    P95:               112,000.000
    P99:               148,000.000
```

---

### `dskit convert` — Format conversion

```bash
dskit convert data.csv --to parquet
dskit convert data.parquet --to csv --output exported.csv
dskit convert data.csv --to excel --output report.xlsx
dskit convert data.json --to csv
```

Supports: `csv` ↔ `json` ↔ `parquet` ↔ `excel`

---

## 🗺️ Supported File Formats

| Format  | Read | Write | Extension      |
|---------|------|-------|----------------|
| CSV     | ✅   | ✅    | `.csv`         |
| TSV     | ✅   | ❌    | `.tsv`         |
| JSON    | ✅   | ✅    | `.json`        |
| Parquet | ✅   | ✅    | `.parquet`     |
| Excel   | ✅   | ✅    | `.xlsx`, `.xls`|

---

## 🧩 Quick Reference

```bash
dskit --help                          # Show all commands
dskit inspect data.csv                # Quick overview
dskit inspect data.csv --rows 10      # Show 10 preview rows
dskit profile data.csv                # Full HTML profile
dskit profile data.csv --minimal      # Faster minimal profile
dskit clean data.csv --drop-duplicates --output out.csv
dskit clean data.csv --fill-na mean   # Fill NaN with mean
dskit clean data.csv --fill-na drop   # Drop rows with NaN
dskit stats data.csv                  # Stats for all numeric cols
dskit stats data.csv --col price      # Stats for one column
dskit stats data.csv --percentiles    # Include P5–P99
dskit convert data.csv --to parquet   # Convert to Parquet
dskit convert data.json --to csv      # Convert JSON to CSV
```

---

## 📦 Dependencies

| Package          | Purpose                    |
|------------------|----------------------------|
| `pandas`         | Data loading & manipulation|
| `pyarrow`        | Parquet support            |
| `openpyxl`       | Excel support              |
| `tabulate`       | Table formatting           |
| `ydata-profiling`| HTML reports *(optional)*  |

---

## 🧪 Running Tests

```bash
git clone https://github.com/yourusername/dskit.git
cd dskit
pip install -e ".[dev]"
pytest tests/ -v
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Ideas for new commands? [Open an issue](https://github.com/yourusername/dskit/issues/new) and let's discuss.

---

## 📄 License

MIT © [Your Name](https://github.com/yourusername)

---

<div align="center">

If DSKit saved you time, please consider giving it a ⭐

</div>
