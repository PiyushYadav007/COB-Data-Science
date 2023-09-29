import pandas as pd


file_path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTSS-TcErkXNk8KB0AlijhitwetxeHD2M3R0HJl2QPMAyFq0fxFX4PFKnzAWLDnratIz67DNL6GsZnV/pub?output=csv"
df = pd.read_csv(file_path)
df.fillna(df.mean(), inplace=True)

def remove_outliers(dataframe, column_names):
    for column in column_names:
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        dataframe = dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
    return dataframe

columns_to_remove_outliers = ["column1", "column2","column3", "column4","column5", "column6","column7", "column8","column9", "column10"]


df_cleaned = remove_outliers(df, columns_to_remove_outliers)


df_cleaned.to_csv("cleaned_dataset.csv", index=False)

print("Cleaning and preprocessing completed. Cleaned dataset saved as cleaned_dataset.csv")
