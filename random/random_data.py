# %%
import numpy as np
import pandas as pd


# %%
def create_df(size: int, set_types: bool = False):
    dates = pd.date_range("2020-01-01", "2022-12-31")

    df = pd.DataFrame()
    df["x"] = np.random.randint(0, 100, size=size)
    df["y"] = np.random.randint(0, 100, size=size)
    df["value"] = np.random.normal(100, 10, size=size)
    df["color"] = np.random.choice(["red", "green", "blue", "yellow"], size=size)
    df["s"] = np.random.choice(["Yes", "No"], size=size)
    df["date"] = np.random.choice(dates, size=size)

    # Set types to check memory usage and speed
    if set_types:
        df["x"] = df["x"].astype("int8")
        df["y"] = df["y"].astype("int8")
        df["value"] = df["value"].astype("float32")
        df["color"] = df["color"].astype("category")
        df["s"] = df["s"].map({"Yes": True, "No": False})
    return df

# %%
%%timeit -n 1 -r 1
# Test speed and memory usage
df = create_df(10_000_000, set_types=False)
df.info()

# %%
%%timeit -n 1 -r 1
df = create_df(10_000_000, set_types=True)
df.info()

# %%
# Test sampling and scatter plot
df = create_df(100_000, set_types=True)
mini_sample = df.sample(n=2_000).copy()
mini_sample.plot.scatter(x='x',y='y',c='value',colormap='viridis')