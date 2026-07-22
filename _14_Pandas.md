# Pandas ____ Python Library

A simple guide to learn Pandas step by step, in easy English, with examples.

---

## 1. What is Pandas?

Pandas is a Python library used to work with **tables of data** — like an Excel sheet or a database table, but inside Python.

It is built on top of NumPy, so if you know a bit of NumPy, this will feel familiar.

```python
import pandas as pd
```

We always give it the short name `pd`.

---

## 2. Install Pandas

```bash
pip install pandas
```

---

## 3. The Two Main Building Blocks

Pandas has two main things you will use all the time:

- **Series** = a single column of data (like one list, with labels).
- **DataFrame** = a full table made of many columns (like a spreadsheet).

```python
import pandas as pd

# Series - one column
s = pd.Series([10, 20, 30])
print(s)
# 0    10
# 1    20
# 2    30

# DataFrame - a full table
df = pd.DataFrame({
    "name": ["Ali", "Sara", "Zulkaif"],
    "age": [22, 25, 23]
})
print(df)
#       name  age
# 0      Ali   22
# 1     Sara   25
# 2  Zulkaif   23
```

Think of a DataFrame as a table with rows and columns, just like a database table or an Excel file.

---

## 4. Creating a DataFrame

The most common way is from a Python dictionary:

```python
data = {
    "name": ["Ali", "Sara", "Zulkaif"],
    "age": [22, 25, 23],
    "city": ["Lahore", "Karachi", "Peshawar"]
}
df = pd.DataFrame(data)
```

You can also create one from a list of lists:

```python
df = pd.DataFrame(
    [["Ali", 22], ["Sara", 25]],
    columns=["name", "age"]
)
```

---

## 5. Reading Files (CSV, Excel)

This is one of the most useful things Pandas does — read data files directly into a table.

```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
```

To save a DataFrame back to a file:

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

`index=False` means "don't save the row numbers as a column."

---

## 6. Looking at Your Data

These are the first commands you should run on any new dataset.

```python
df.head()      # shows first 5 rows
df.tail()      # shows last 5 rows
df.shape       # (rows, columns) -> e.g. (100, 5)
df.columns     # list of column names
df.info()      # column names, types, and missing values
df.describe()  # quick statistics (average, min, max, etc.) for number columns
```

---

## 7. Selecting Columns

```python
df["name"]           # one column (as a Series)
df[["name", "age"]]  # multiple columns (as a DataFrame) - note the double brackets
```

---

## 8. Selecting Rows

```python
df.loc[0]        # row with label/index 0
df.iloc[0]        # row at position 0 (works like a normal list position)
df.loc[0:2]        # rows 0 to 2 (by label)
df.iloc[0:2]        # rows 0 to 2 (by position)
```

**Simple rule:** `loc` uses labels (names), `iloc` uses plain position numbers (like list indexing). If your rows are just numbered 0,1,2..., they behave almost the same.

---

## 9. Filtering Rows (Very Important)

This is like asking: "Give me only the rows that match this condition."

```python
df[df["age"] > 23]
# only rows where age is greater than 23

df[df["city"] == "Peshawar"]
# only rows where city is Peshawar

df[(df["age"] > 20) & (df["city"] == "Lahore")]
# combine conditions with & (and), | (or)
```

**Tip:** Always put each condition in its own brackets when combining with `&` or `|`.

---

## 10. Adding and Changing Columns

```python
df["age_next_year"] = df["age"] + 1        # add a new column
df["is_adult"] = df["age"] >= 18            # column of True/False

df["name"] = df["name"].str.upper()          # change text in a column
```

---

## 11. Removing Columns or Rows

```python
df.drop("city", axis=1)          # remove a column (axis=1 means column)
df.drop(0, axis=0)                # remove row with index 0 (axis=0 means row)

df.drop("city", axis=1, inplace=True)   # inplace=True changes df directly, no need to reassign
```

---

## 12. Handling Missing Data

Real data often has empty/missing values. Pandas shows these as `NaN`.

```python
df.isnull()             # True/False table showing where data is missing
df.isnull().sum()        # count missing values per column

df.dropna()               # remove rows that have any missing value
df.fillna(0)               # replace missing values with 0
df["age"].fillna(df["age"].mean())  # fill missing age with the average age
```

---

## 13. Sorting Data

```python
df.sort_values("age")                     # sort by age, smallest first
df.sort_values("age", ascending=False)    # largest first
```

---

## 14. Grouping Data (like Excel Pivot Tables)

This is one of the most powerful Pandas features — grouping rows and calculating something for each group.

```python
df.groupby("city")["age"].mean()
# average age for each city

df.groupby("city").size()
# how many rows (people) per city
```

Think of it like: "For each city, calculate the average age."

---

## 15. Basic Math and Stats on Columns

```python
df["age"].sum()
df["age"].mean()
df["age"].min()
df["age"].max()
df["age"].count()      # how many non-missing values
```

---

## 16. Renaming Columns

```python
df.rename(columns={"name": "full_name"}, inplace=True)
```

---

## 17. Merging / Joining Tables

If you have two tables that share a common column (like `id`), you can join them, similar to a SQL join.

```python
df1 = pd.DataFrame({"id": [1, 2], "name": ["Ali", "Sara"]})
df2 = pd.DataFrame({"id": [1, 2], "score": [85, 90]})

merged = pd.merge(df1, df2, on="id")
print(merged)
#    id  name  score
# 0   1   Ali     85
# 1   2  Sara     90
```

---

## 18. A Small Practice Example

```python
data = {
    "name": ["Ali", "Sara", "Zulkaif", "Hina"],
    "score": [78, 85, 92, 45],
    "city": ["Lahore", "Karachi", "Peshawar", "Lahore"]
}
df = pd.DataFrame(data)

print("Average score:", df["score"].mean())
print("Top scorer:")
print(df[df["score"] == df["score"].max()])
print("Passing students (score >= 50):")
print(df[df["score"] >= 50])
print("Average score by city:")
print(df.groupby("city")["score"].mean())
```

---

## Quick Cheat Sheet

| What you want to do | Code |
|---|---|
| Read a CSV file | `pd.read_csv("file.csv")` |
| See first rows | `df.head()` |
| Table shape | `df.shape` |
| Column info | `df.info()` |
| Quick stats | `df.describe()` |
| Pick a column | `df["col"]` |
| Pick multiple columns | `df[["col1","col2"]]` |
| Pick a row by position | `df.iloc[0]` |
| Filter rows | `df[df["col"] > 5]` |
| Add a column | `df["new"] = ...` |
| Remove a column | `df.drop("col", axis=1)` |
| Handle missing data | `df.dropna()`, `df.fillna(0)` |
| Sort | `df.sort_values("col")` |
| Group and summarize | `df.groupby("col")["other"].mean()` |
| Join two tables | `pd.merge(df1, df2, on="id")` |
| Save to file | `df.to_csv("out.csv", index=False)` |

---

## What to Practice Next

1. Load a small CSV file and run `.head()`, `.info()`, `.describe()` on it.
2. Practice selecting columns and filtering rows with conditions.
3. Add a new column based on math from an existing column.
4. Try `groupby()` to summarize data (like average score per city).
5. Practice handling missing values with `fillna()` and `dropna()`.

Once these feel comfortable, you can move to more advanced Pandas topics: pivot tables, multi-level indexing, working with dates/time, and combining Pandas with charts (like Matplotlib or the Recharts-style dashboards you've already built, but on the Python/data side).