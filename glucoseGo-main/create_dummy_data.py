import os
import numpy as np
import pandas as pd

# Reproducible random data
np.random.seed(42)

# Number of synthetic exercise sessions
n = 500

# Create output directory expected by glucoseGo
directory = "data/tidy_data/final_df"
os.makedirs(directory, exist_ok=True)

# --------------------------------------------------
# Create synthetic feature data
# --------------------------------------------------

X = pd.DataFrame({
    "start_glc": np.random.normal(150, 35, n).clip(70, 300),
    "duration": np.random.randint(10, 121, n),
    "intensity": np.random.uniform(1, 10, n),

    "form_of_exercise_aer": np.random.randint(0, 2, n),
    "form_of_exercise_ana": np.random.randint(0, 2, n),
    "form_of_exercise_mix": np.random.randint(0, 2, n),

    "years_since_diagnosis": np.random.randint(1, 40, n),
    "hba1c": np.random.normal(7.2, 0.8, n).clip(5, 12),

    "time_of_day_morning": np.random.randint(0, 2, n),
    "time_of_day_afternoon": np.random.randint(0, 2, n),
    "time_of_day_evening": np.random.randint(0, 2, n),

    "sex_male": np.random.randint(0, 2, n),
    "sex_female": np.random.randint(0, 2, n),

    "bmi": np.random.normal(25, 4, n).clip(16, 45),
    "age": np.random.randint(18, 70, n)
})

# --------------------------------------------------
# Create synthetic hypo outcome
# --------------------------------------------------

# Artificial relationship purely for testing:
# lower starting glucose + longer exercise = more hypo risk
risk = (
    -0.035 * (X["start_glc"] - 130)
    + 0.025 * (X["duration"] - 45)
)

probability = 1 / (1 + np.exp(-risk))

y = np.random.binomial(1, probability)

# --------------------------------------------------
# Create df.csv
# --------------------------------------------------

df = pd.DataFrame({
    "y": y,

    # Multiple observations per synthetic participant.
    # Included because the original notebook expects this column.
    "stratify": np.random.randint(1, 21, n)
})

# Save files
X.to_csv(os.path.join(directory, "X.csv"), index=False)
df.to_csv(os.path.join(directory, "df.csv"), index=False)

print("Dummy data created successfully.")
print(f"Number of rows: {n}")
print(f"Hypoglycemia cases: {y.sum()}")
print(f"Non-hypoglycemia cases: {(y == 0).sum()}")
print()
print("Files:")
print(os.path.join(directory, "X.csv"))
print(os.path.join(directory, "df.csv"))