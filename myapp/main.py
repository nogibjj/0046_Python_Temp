# my_ran_string = "This is good"
# def return_backwards_string(random_string):
#     return "".join(reversed(random_string))

# if __name__ == '__main__':
#   print(return_backwards_string(my_ran_string))
import pandas as pd

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
    df = pd.read_csv("./dsets/automobiles.csv")
    print(my_stats(df))
    df['Fuel Efficiency'] = df.loc[:,'mpg'].apply(mpg_cat)
    print(df.iloc[20:41,:]) 
    #print(df.sort_values('yr', ascending = False).head(20))
    