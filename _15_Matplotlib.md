# Matplotlib ____ Python Library

A simple guide to learn Matplotlib step by step, in easy English, with examples.

---

## 1. What is Matplotlib?

Matplotlib is a Python library used to make **charts and graphs** — like line charts, bar charts, and pie charts.

If you've used Recharts in React, this does the same job, but in Python.

```python
import matplotlib.pyplot as plt
```

We always give it the short name `plt`.

---

## 2. Install Matplotlib

```bash
pip install matplotlib
```

---

## 3. Your First Chart

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.show()
```

- `plt.plot(x, y)` draws the chart (a line by default).
- `plt.show()` opens/displays the chart.

Think of `x` as positions along the bottom, and `y` as the height at each position.

---

## 4. Adding Titles and Labels

Always label your charts so people know what they're looking at.

```python
plt.plot(x, y)
plt.title("Sales Over Time")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
```

---

## 5. Line Charts (Styling)

```python
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.show()
```

- `color` = line color (`"red"`, `"blue"`, `"green"`, or hex code like `"#ff5733"`)
- `linestyle` = `"-"` solid, `"--"` dashed, `":"` dotted
- `marker` = `"o"` circle, `"s"` square, `"x"` cross — marks each data point

### Multiple lines on one chart

```python
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 20, 10, 25]

plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")
plt.legend()   # shows the labels as a small box on the chart
plt.show()
```

---

## 6. Bar Charts

Good for comparing categories (like comparing sales between cities).

```python
cities = ["Lahore", "Karachi", "Peshawar"]
sales = [250, 400, 180]

plt.bar(cities, sales)
plt.title("Sales by City")
plt.show()
```

Horizontal bar chart:

```python
plt.barh(cities, sales)
plt.show()
```

---

## 7. Pie Charts

Good for showing parts of a whole (like percentages).

```python
labels = ["Chrome", "Firefox", "Safari"]
usage = [65, 15, 20]

plt.pie(usage, labels=labels, autopct="%1.1f%%")
plt.title("Browser Usage")
plt.show()
```

`autopct="%1.1f%%"` shows the percentage number on each slice.

---

## 8. Scatter Plots

Good for showing the relationship between two things (like height vs weight).

```python
height = [150, 160, 165, 170, 180]
weight = [50, 55, 60, 65, 75]

plt.scatter(height, weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
```

Each dot is one data point instead of a connected line.

---

## 9. Histograms

Good for showing how numbers are spread out (like test scores or ages).

```python
scores = [55, 60, 62, 70, 72, 75, 80, 85, 88, 90, 92, 95]

plt.hist(scores, bins=5)
plt.title("Score Distribution")
plt.show()
```

`bins=5` means it groups the numbers into 5 buckets and counts how many fall in each.

---

## 10. Changing Figure Size

```python
plt.figure(figsize=(8, 5))   # width=8, height=5 (in inches)
plt.plot(x, y)
plt.show()
```

---

## 11. Multiple Charts Side by Side (Subplots)

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))   # 1 row, 2 columns

axes[0].plot(x, y1)
axes[0].set_title("Product A")

axes[1].plot(x, y2)
axes[1].set_title("Product B")

plt.show()
```

Think of `axes[0]` and `axes[1]` as two separate mini-charts placed next to each other.

---

## 12. Saving a Chart as an Image

```python
plt.plot(x, y)
plt.savefig("chart.png")
```

Do this **before** `plt.show()`, or the saved file might be blank.

---

## 13. Using Matplotlib with Pandas

This is very common — you make a DataFrame, then plot straight from it.

```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "city": ["Lahore", "Karachi", "Peshawar"],
    "sales": [250, 400, 180]
}
df = pd.DataFrame(data)

df.plot(kind="bar", x="city", y="sales")
plt.title("Sales by City")
plt.show()
```

`kind` can be `"line"`, `"bar"`, `"pie"`, `"hist"`, `"scatter"`, etc.

---

## 14. A Small Practice Example

```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [120, 150, 100, 180, 220]

plt.figure(figsize=(7, 4))
plt.bar(days, visitors, color="skyblue")
plt.title("Website Visitors This Week")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.savefig("visitors.png")
plt.show()
```

---

## Quick Cheat Sheet

| What you want to do | Code |
|---|---|
| Line chart | `plt.plot(x, y)` |
| Bar chart | `plt.bar(x, y)` |
| Horizontal bar | `plt.barh(x, y)` |
| Pie chart | `plt.pie(values, labels=labels)` |
| Scatter plot | `plt.scatter(x, y)` |
| Histogram | `plt.hist(data, bins=10)` |
| Title | `plt.title("My Title")` |
| Axis labels | `plt.xlabel("X")`, `plt.ylabel("Y")` |
| Show legend | `plt.legend()` |
| Change size | `plt.figure(figsize=(8,5))` |
| Multiple charts | `plt.subplots(rows, cols)` |
| Save chart | `plt.savefig("file.png")` |
| Show chart | `plt.show()` |
| Plot from Pandas | `df.plot(kind="bar", x="col1", y="col2")` |

---

## What to Practice Next

1. Make a simple line chart with a title and axis labels.
2. Try a bar chart comparing 3-4 categories (like sales by city).
3. Try a pie chart showing percentages.
4. Load a small CSV with Pandas and plot a column directly with `df.plot()`.
5. Try putting two charts side by side using `subplots()`.

Once these feel comfortable, you can explore more advanced Matplotlib features: customizing colors/themes, annotations, log scales, and combining it with Seaborn (a library built on top of Matplotlib that makes charts look nicer with less code).