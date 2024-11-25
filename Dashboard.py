import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data
def load_data(file_path="https://raw.githubusercontent.com/username/repo/main/labor_stats.csv"):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


# Function to calculate summary statistics
def calculate_summary(data):
    summary = {}
    for series in data["series"].unique():
        series_data = data[data["series"] == series]
        latest_value = series_data.iloc[0]["value"]
        previous_value = series_data.iloc[1]["value"] if len(series_data) > 1 else None
        change = (latest_value - previous_value) if previous_value else None
        summary[series] = {
            "Latest Value": latest_value,
            "Previous Value": previous_value,
            "Change": change
        }
    return pd.DataFrame.from_dict(summary, orient="index")

# Main Dashboard App
def main():
    st.title("Labor Statistics Dashboard")
    st.write("An interactive dashboard for U.S. labor statistics.")

    # Load the dataset
    data = load_data()

    # Sidebar for user input
    st.sidebar.header("Filters")
    series_options = data["series"].unique()
    selected_series = st.sidebar.multiselect("Select data series", series_options, default=series_options)

    # Filter data based on user selection
    filtered_data = data[data["series"].isin(selected_series)]

    # Summary Statistics
    st.subheader("Summary Statistics")
    if not filtered_data.empty:
        latest_data = filtered_data.sort_values(by="date", ascending=False).groupby("series").head(2)
        summary_stats = calculate_summary(latest_data)
        st.table(summary_stats)
    else:
        st.warning("Please select at least one series to display.")

    # Visualization
    st.subheader("Time-Series Plot")
    if not filtered_data.empty:
        fig = px.line(filtered_data, x="date", y="value", color="series", title="Labor Statistics Over Time")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please select at least one series to display.")

    # Display raw data
    st.subheader("Data Table")
    st.write(filtered_data)

if __name__ == "__main__":
    main()
