import streamlit as st
import pandas as pd
import plotly.express as px


# Load the data with caching for better performance
@st.cache_data
def load_data(file_path="labor_stats.csv"):
    """
    Load labor statistics data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: A pandas DataFrame with the loaded data.
    """
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])  # Ensure 'date' column is in datetime format
    return df


# Function to calculate summary statistics for each data series
def calculate_summary(data):
    """
    Calculate summary statistics for each data series.

    Args:
        data (pd.DataFrame): The filtered data.

    Returns:
        pd.DataFrame: A summary table with the latest value, previous value, and change.
    """
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
    """
    Main function to run the Streamlit dashboard application.
    """
    st.set_page_config(page_title="Labor Statistics Dashboard", layout="wide")

    # Set background color for a better user experience
    st.markdown(
        """
        <style>
        .main {
            background-color: #f7f7f7;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and description
    st.title("Labor Statistics Dashboard")
    st.write(
        "Welcome to the interactive dashboard for U.S. labor statistics. "
        "Use the filters on the left to customize your view."
    )

    # Load the dataset
    data = load_data()

    # Sidebar for user input
    st.sidebar.header("Filters")
    series_options = data["series"].unique()
    all_option = "Select All"
    series_options = [all_option] + list(series_options)
    selected_series = st.sidebar.multiselect("Select data series", series_options, default=[all_option])

    if all_option in selected_series:
        selected_series = data["series"].unique()

    # Filter data based on user selection
    filtered_data = data[data["series"].isin(selected_series)]

    # Add data export option
    st.sidebar.download_button(
        label="Download Filtered Data",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_labor_stats.csv",
        mime="text/csv"
    )

    # Display key metrics
    st.subheader("Key Metrics")
    if not filtered_data.empty:
        total_records = len(filtered_data)
        latest_data = filtered_data.sort_values(by="date", ascending=False).groupby("series").first()
        avg_latest_value = latest_data["value"].mean()

        col1, col2 = st.columns(2)
        col1.metric("Total Records", total_records)
        col2.metric("Avg Latest Value", f"{avg_latest_value:.2f}")
    else:
        st.warning("No data available for the selected series.")

    # Summary statistics
    st.subheader("Summary Statistics")
    if not filtered_data.empty:
        latest_data = filtered_data.sort_values(by="date", ascending=False).groupby("series").head(2)
        summary_stats = calculate_summary(latest_data)
        st.table(summary_stats)
    else:
        st.warning("Please select at least one series to display.")

    # Pie chart visualization
    st.subheader("Labor Statistics Distribution")
    if not filtered_data.empty:
        latest_data = filtered_data.sort_values(by="date", ascending=False).groupby("series").first()
        pie_data = latest_data.reset_index()[["series", "value"]]

        fig_pie = px.pie(
            pie_data, values="value", names="series",
            color_discrete_sequence=px.colors.sequential.RdBu,
            hover_data={"value": True, "series": True}
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.warning("Please select at least one series to display.")

    # Line graph visualization
    st.subheader("Labor Statistics Trends")
    if not filtered_data.empty:
        if len(selected_series) == len(data["series"].unique()):
            fig_line = px.line(
                filtered_data, x="date", y="value", color="series",
                facet_col="series", facet_col_wrap=3,
                hover_data={"value": True, "date": True, "series": True}
            )
            fig_line.for_each_yaxis(lambda axis: axis.update(matches=None))
        else:
            fig_line = px.line(
                filtered_data, x="date", y="value", color="series",
                title="Labor Statistics Trends",
                hover_data={"value": True, "date": True, "series": True}
            )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Please select at least one series to display.")

    # Bar chart visualization
    st.subheader("Average Value by Series")
    if not filtered_data.empty:
        bar_data = filtered_data.groupby("series")["value"].mean().reset_index()
        fig_bar = px.bar(
            bar_data, x="series", y="value", color="series",
            color_discrete_sequence=px.colors.sequential.RdBu,
            hover_data={"value": True, "series": True}
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("Please select at least one series to display.")


if __name__ == "__main__":
    main()
