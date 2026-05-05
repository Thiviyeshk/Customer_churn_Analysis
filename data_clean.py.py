import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    df = df.drop(columns=[
        'Customer_ID',
        'Name',
        'Email',
        'Last_Support_Ticket'
    ])

    df = df.dropna()

    return df


def save_clean_data(df, path):
    df.to_csv(path, index=False)