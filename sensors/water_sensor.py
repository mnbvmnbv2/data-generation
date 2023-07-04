# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# %%
def create_df(start_date: str, end_date: str, visualize: bool = False):
    time_delta = datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(
        start_date
    )
    num_hours = time_delta.days * 24 + 1
    times = pd.date_range(start=start_date, end=end_date, periods=num_hours)

    df = pd.DataFrame()

    # get temperatures
    # Set the range of temperatures
    min_value = (np.sin(np.linspace(-2, -2 * np.pi - 2, 24)) + 1) * 2
    max_value = (np.sin(np.linspace(-2, -2 * np.pi - 2, 24)) + 20) * 2
    # hourly bias
    hourly_bias_temperature = (np.sin(np.linspace(-2, -2 * np.pi - 2, 24))) * 0.5

    # Initialize with a starting temperature
    temperature = [10]

    # Generate the random walk
    for i in range(num_hours - 1):
        hour = i % 24

        while True:
            # Generate a random step
            step = np.random.normal(loc=0, scale=0.5)

            # add together with bias
            next_temperature = temperature[-1] + step + hourly_bias_temperature[hour]

            # Check if the next position is within the range
            if (
                next_temperature >= min_value[hour]
                and next_temperature <= max_value[hour]
            ):
                # Accept the step and update the position
                temperature.append(next_temperature)
                break

    temperature = np.array(temperature)

    df["time"] = times
    df["temperature"] = temperature

    # Set types
    df["time"] = df["time"].astype("datetime64[ns]")
    df["temperature"] = df["temperature"].astype("float32")

    if visualize:
        plt.plot(df["time"], df["temperature"])
        plt.show()
    return df


# %%
dataframe = create_df("2022-01-01", "2023-01-01", visualize=True)
