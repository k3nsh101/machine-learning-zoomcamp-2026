# Homework 1

> [!NOTE]
> This homework uses the pinned 2026 car fuel-efficiency release in the course
> repository. The plan and report are available in `cohorts/2026/data/`.

## Set up the environment

You need to install Python, NumPy, Pandas, Matplotlib, and Seaborn. For that, you can use the instructions from
[06-environment.md](06-environment.md).

## Q1. Pandas version

What version of Pandas did you install?

You can get the version information using the `__version__` field:

```python
pd.__version__
```

> Answer

```
3.0.5
```

## Getting the data

For this homework, we'll use the 2026 Car Fuel Efficiency dataset. Download it from <a href='https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'>here</a>.

You can do it with wget:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas.

## Q2. Records count

How many records are in the dataset?

- 5000
- 9000
- 10000
- 15000

> Answer

```
10000
```

## Q3. Fuel types

How many fuel types are presented in the dataset?

- 1
- 2
- 3
- 4

> Answer

```
3
```

## Q4. Missing values

How many columns in the dataset have missing values?

- 0
- 1
- 2
- 3
- 4

> Answer

```
2
```

## Q5. Max fuel efficiency

What's the maximum fuel efficiency of cars from Asia?

- 21.2
- 31.2
- 41.2
- 51.2

> Answer

```
41.2
```

## Q6. Median value of horsepower

1. Find the median value of the `horsepower` column in the dataset.
2. Next, calculate the most frequent value of the same `horsepower` column.
3. Use the `fillna` method to fill the missing values in the `horsepower` column with the most frequent value from the previous step.
4. Now, calculate the median value of `horsepower` once again.

Has it changed?

- Yes, it increased
- Yes, it decreased
- No

> Answer

```
No
```

## Q7. Sum of weights

1. Select all the cars from Asia
2. Select only columns `vehicle_weight` and `model_year`
3. Select the first 7 values
4. Get the underlying NumPy array. Let's call it `X`.
5. Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
6. Invert `XTX`.
7. Create an array `y` with values `[1100, 1300, 800, 900, 1000, 1100, 1200]`.
8. Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
9. What's the sum of all the elements of the result?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.

- 0.0369
- 0.369
- 3.69
- 36.9

> Answer

```
0.369
```
