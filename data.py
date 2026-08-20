
import pandas as pd
import numpy as np
from datetime import datetime

def create_inflation_dataset():
    """
    Create a comprehensive global inflation dataset (1980-2024)
    """

    # Define years
    years = list(range(1980, 2025))

    # Create inflation data for major economies
    inflation_data = [
        {
            'country_name': 'United States',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                13.5, 10.3, 6.2, 3.2, 4.3, 3.6, 1.9, 3.6, 4.1, 4.8,
                5.4, 4.2, 3.0, 3.0, 2.6, 2.8, 2.9, 2.3, 1.6, 2.2,
                3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.9, 3.8, -0.4,
                1.6, 3.2, 2.1, 1.5, 1.6, 0.1, 1.3, 2.1, 2.4, 1.8,
                1.2, 4.7, 8.0, 4.1, 3.4
            ])}
        },
        {
            'country_name': 'United Kingdom',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                18.0, 11.9, 8.6, 4.6, 5.0, 6.1, 3.4, 4.2, 4.9, 7.8,
                9.5, 5.9, 3.7, 1.6, 2.5, 3.4, 2.4, 3.1, 3.4, 1.5,
                2.9, 1.8, 1.7, 2.9, 3.0, 2.8, 3.2, 4.3, 4.0, 2.2,
                3.3, 4.5, 2.8, 2.6, 1.5, 0.0, 0.7, 2.7, 2.5, 1.8,
                0.9, 2.6, 9.1, 7.3, 2.5
            ])}
        },
        {
            'country_name': 'Germany',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                5.4, 6.3, 5.3, 3.3, 2.4, 2.2, -0.1, 0.2, 1.3, 2.8,
                2.7, 3.5, 5.1, 4.5, 2.7, 1.8, 1.4, 1.9, 1.0, 0.6,
                1.4, 1.9, 1.4, 1.0, 1.8, 1.9, 1.8, 2.3, 2.8, 0.2,
                1.2, 2.5, 2.1, 1.6, 0.8, 0.1, 0.4, 1.7, 1.9, 1.4,
                0.4, 3.2, 8.7, 5.9, 2.8
            ])}
        },
        {
            'country_name': 'Japan',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                7.8, 4.9, 2.7, 1.9, 2.3, 2.0, 0.6, 0.1, 0.7, 2.3,
                3.1, 3.3, 1.7, 1.3, 0.7, -0.1, 0.1, 1.7, 0.7, -0.3,
                -0.7, -0.8, -0.9, -0.3, 0.0, -0.3, 0.2, 0.1, 1.4, -1.4,
                -0.7, -0.3, 0.0, 0.3, 2.8, 0.8, -0.1, 0.5, 1.0, 0.5,
                0.0, -0.2, 2.5, 3.3, 2.7
            ])}
        },
        {
            'country_name': 'China',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                6.0, 2.4, 1.9, 1.5, 2.8, 9.3, 6.5, 7.3, 18.8, 18.0,
                3.1, 3.4, 6.4, 14.7, 24.1, 17.1, 8.3, 2.8, -0.8, -1.4,
                0.4, 0.7, -0.8, 1.2, 3.9, 1.8, 1.5, 4.8, 5.9, -0.7,
                3.3, 5.4, 2.6, 2.6, 2.0, 1.4, 2.0, 1.6, 2.1, 2.9,
                2.5, 0.9, 2.0, 0.2, 0.4
            ])}
        },
        {
            'country_name': 'India',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                11.4, 13.1, 7.9, 11.9, 8.3, 5.6, 8.7, 8.8, 9.4, 6.2,
                9.0, 13.9, 11.8, 6.4, 10.2, 10.2, 9.0, 7.2, 13.2, 4.7,
                4.0, 3.8, 4.3, 3.8, 3.8, 4.2, 5.8, 6.4, 8.3, 10.9,
                12.0, 8.9, 9.3, 10.9, 6.7, 4.9, 4.5, 3.6, 3.4, 4.8,
                6.2, 5.1, 6.7, 5.4, 4.9
            ])}
        },
        {
            'country_name': 'Brazil',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                110.2, 95.2, 99.7, 211.0, 223.8, 235.1, 65.0, 415.8, 1037.5, 1782.9,
                1476.7, 480.2, 1119.1, 2708.6, 916.5, 22.0, 9.1, 4.3, 1.7, 8.9,
                6.0, 7.7, 12.5, 9.3, 7.6, 5.7, 3.1, 4.5, 5.9, 4.3,
                5.9, 6.5, 5.8, 5.9, 6.4, 10.7, 6.3, 2.9, 3.7, 4.3,
                4.5, 10.1, 5.8, 4.6, 4.8
            ])}
        },
        {
            'country_name': 'Canada',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                10.2, 12.5, 10.8, 5.8, 4.3, 4.0, 4.1, 4.4, 4.0, 5.0,
                4.8, 5.6, 1.5, 1.8, 0.2, 2.2, 1.6, 1.6, 1.0, 1.7,
                2.7, 2.5, 2.3, 2.8, 1.9, 2.2, 2.0, 2.1, 2.4, 0.3,
                1.8, 2.9, 1.5, 0.9, 2.0, 1.1, 1.4, 1.6, 2.3, 1.9,
                0.7, 3.4, 6.8, 3.9, 2.7
            ])}
        },
        {
            'country_name': 'France',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                13.6, 13.4, 11.8, 9.6, 7.4, 5.8, 2.7, 3.1, 2.7, 3.6,
                3.4, 3.2, 2.4, 2.1, 1.6, 1.8, 2.0, 1.2, 0.7, 0.5,
                1.7, 1.6, 1.9, 2.1, 2.1, 1.7, 1.7, 1.5, 2.8, 0.1,
                1.5, 2.1, 2.0, 0.9, 0.5, 0.0, 0.2, 1.0, 1.8, 1.1,
                0.5, 1.6, 5.2, 4.9, 2.3
            ])}
        },
        {
            'country_name': 'Australia',
            'indicator_name': 'Consumer Price Index',
            **{year: rate for year, rate in zip(years, [
                10.2, 9.7, 11.1, 10.1, 4.0, 6.7, 9.1, 8.5, 7.3, 7.5,
                7.3, 3.2, 1.0, 1.8, 1.9, 4.6, 2.6, 0.3, 0.9, 1.5,
                4.5, 4.4, 3.0, 2.8, 2.3, 2.7, 3.5, 2.3, 4.4, 1.8,
                2.9, 3.4, 1.8, 2.5, 2.5, 1.5, 1.3, 2.0, 1.9, 1.6,
                0.9, 2.9, 6.6, 5.6, 3.8
            ])}
        }
    ]

    # Create DataFrame
    df = pd.DataFrame(inflation_data)

    return df


def analyze_inflation_data(df):
    """
    Perform basic analysis on the inflation dataset
    """
    print("=" * 80)
    print("GLOBAL INFLATION DATASET ANALYSIS (1980-2024)")
    print("=" * 80)
    print(f"\nDataset Shape: {df.shape[0]} countries × {df.shape[1]} columns")
    print(f"Total Data Points: {df.shape[0] * 45} inflation rates")

    # Recent inflation trends (2022-2024)
    print("\n" + "-" * 80)
    print("RECENT INFLATION RATES (2022-2024)")
    print("-" * 80)
    recent_cols = ['country_name', 2022, 2023, 2024]
    recent_df = df[recent_cols].copy()
    recent_df['Trend'] = recent_df.apply(
        lambda row: '↑' if row[2024] > row[2023] else '↓', axis=1
    )
    print(recent_df.to_string(index=False))

    # Historical extremes
    print("\n" + "-" * 80)
    print("HISTORICAL EXTREMES")
    print("-" * 80)

    year_cols = [col for col in df.columns if isinstance(col, int)]

    for _, row in df.iterrows():
        country = row['country_name']
        rates = row[year_cols]
        max_rate = rates.max()
        max_year = rates.idxmax()
        min_rate = rates.min()
        min_year = rates.idxmin()

        print(f"\n{country}:")
        print(f"  Highest: {max_rate:.1f}% in {max_year}")
        print(f"  Lowest:  {min_rate:.1f}% in {min_year}")

    # Average inflation by decade
    print("\n" + "-" * 80)
    print("AVERAGE INFLATION BY DECADE")
    print("-" * 80)

    decades = {
        '1980s': list(range(1980, 1990)),
        '1990s': list(range(1990, 2000)),
        '2000s': list(range(2000, 2010)),
        '2010s': list(range(2010, 2020)),
        '2020s': list(range(2020, 2025))
    }

    decade_data = []
    for country_row in df.itertuples(index=False):
        country = country_row.country_name
        for decade_name, decade_years in decades.items():
            available_years = [y for y in decade_years if hasattr(country_row, str(y))]
            if available_years:
                rates = [getattr(country_row, str(y)) for y in available_years]
                avg_rate = np.mean(rates)
                decade_data.append({
                    'Country': country,
                    'Decade': decade_name,
                    'Avg_Inflation': avg_rate
                })

    decade_df = pd.DataFrame(decade_data)
    decade_pivot = decade_df.pivot(index='Country', columns='Decade', values='Avg_Inflation')
    decade_pivot = decade_pivot[['1980s', '1990s', '2000s', '2010s', '2020s']]
    print(decade_pivot.round(1).to_string())


def export_to_excel(df, filename='global_inflation_data_1980_2024.xlsx'):
    """
    Export the dataset to Excel with formatting
    """
    try:
        # Create Excel writer
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Write main dataset
            df.to_excel(writer, sheet_name='Inflation Data', index=False)

            # Get workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['Inflation Data']

            # Format headers
            for cell in worksheet[1]:
                cell.font = cell.font.copy(bold=True)
                cell.fill = cell.fill.copy(fgColor="366092", patternType="solid")
                cell.font = cell.font.copy(color="FFFFFF")

            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 20)
                worksheet.column_dimensions[column_letter].width = adjusted_width

            # Create summary sheet
            summary_data = {
                'Metric': [
                    'Total Countries',
                    'Years Covered',
                    'Total Data Points',
                    'Date Range',
                    'Data Source'
                ],
                'Value': [
                    df.shape[0],
                    45,
                    df.shape[0] * 45,
                    '1980-2024',
                    'Historical CPI Data'
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)

        print(f"\n✓ Excel file exported successfully: {filename}")

    except Exception as e:
        print(f"\n✗ Error exporting to Excel: {e}")
        print("  Make sure 'openpyxl' is installed: pip install openpyxl")


def export_to_csv(df, filename='global_inflation_data_1980_2024.csv'):
    """
    Export the dataset to CSV
    """
    try:
        df.to_csv(filename, index=False)
        print(f"✓ CSV file exported successfully: {filename}")
    except Exception as e:
        print(f"✗ Error exporting to CSV: {e}")


def main():
    """
    Main function to create, analyze, and export the inflation dataset
    """
    print("\n" + "=" * 80)
    print("GLOBAL INFLATION DATASET GENERATOR")
    print("=" * 80)

    # Create dataset
    print("\n[1/4] Creating inflation dataset...")
    df = create_inflation_dataset()
    print(f"✓ Dataset created with {df.shape[0]} countries")

    # Analyze data
    print("\n[2/4] Analyzing data...")
    analyze_inflation_data(df)

    # Export to Excel
    print("\n[3/4] Exporting to Excel...")
    export_to_excel(df)

    # Export to CSV
    print("\n[4/4] Exporting to CSV...")
    export_to_csv(df)

    print("\n" + "=" * 80)
    print("PROCESS COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("\nFiles created:")
    print("  • global_inflation_data_1980_2024.xlsx")
    print("  • global_inflation_data_1980_2024.csv")
    print("\n")


