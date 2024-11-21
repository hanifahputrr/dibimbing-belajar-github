import pandas as pd

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    read_csv("username.csv")