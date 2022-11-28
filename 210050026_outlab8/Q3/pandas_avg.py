import pandas as pd

def read_data(file_name):
    r"""
        This function reads the contents from the file,
        specified by the file_name into a pandas DataFrame.
    """
    dataFrame = pd.read_csv("example_input.csv")
    return dataFrame

def compute_avg(data_frame):
    r"""
        This function takes in a DataFrame and returns another 
        DataFrame with the computed averages
    """
    return data_frame.groupby("programme").mean("cgpa")

if __name__ == '__main__':
    df = read_data('example_input.csv')
    print('\n=============INPUT DF=============\n')
    print(df)
    print('\n=============EXPECTED OUTPUT=============\n')
    print(compute_avg(df))