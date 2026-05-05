import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df):
    df['Churn'].value_counts().plot(kind='bar')
    plt.title("Customer Churn Distribution")
    plt.show()


def plot_usage_vs_churn(df):
    sns.boxplot(x='Churn', y='Daily_Usage_Mins', data=df)
    plt.title("Daily Usage vs Churn")
    plt.show()


def plot_login_vs_churn(df):
    sns.boxplot(x='Churn', y='Login_Frequency', data=df)
    plt.title("Login Frequency vs Churn")
    plt.show()


def plot_account_age(df):
    sns.boxplot(x='Churn', y='Account_Age_Days', data=df)
    plt.title("Account Age vs Churn")
    plt.show()