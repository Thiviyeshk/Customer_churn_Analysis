def encode_features(df):
    df['Login_Frequency'] = df['Login_Frequency'].map({
        'Daily': 4,
        'Weekly': 3,
        'Monthly': 2,
        'Rarely': 1
    })

    return df