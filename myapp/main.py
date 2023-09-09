# my_ran_string = "This is good"
# def return_backwards_string(random_string):
#     return "".join(reversed(random_string))

# if __name__ == '__main__':
#   print(return_backwards_string(my_ran_string))
import pandas as pd
def read_csv():
    df = pd.read_csv("./dsets/automobiles.csv")
    return df
    pass
def mpg_cat(mpg):
    if mpg < 15:
        return ("Low")
    elif mpg < 25:
        return ("Moderate")
    else:
        return ("High")

def my_stats(df):
    return df.describe()
    pass

if __name__ == "__main__":
    df = read_csv()
    print('Descriptive Analysis of the Automobiles Dataset:')
    print(my_stats(df))
    df['Fuel Efficiency'] = df.loc[:,'mpg'].apply(mpg_cat)
    print('\n-----------------------------------------------\n')
    print('A segment of an insightful info about the Automobile Dataset:')
    print(df.iloc[20:41,:]) 
    #print(df.sort_values('yr', ascending = False).head(20))
   
    