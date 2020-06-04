import pandas as pd
import numpy as np

def max_facility_id(df):
    '''
    INPUT: DataFrame
    OUTPUT: int

    Write a query on the input data frame that returns the maximum facility id.
    '''

    return df['Facility ID'].max()

def number_of_censuses(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns count of how many censuses were reported
    for the specified facility id
    '''
    #return df[(df['Facility ID']== facility_id)].count()
    return (df['Facility ID'] == facility_id).sum()

def earliest_census_date(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the earliest census date for the
    specified facility id
    Note: The dates are currently stored as strings, not date objects
    Hint: pd.to_datetime is very useful
    '''
    data = df[df['Facility ID'] == facility_id]
    df['Bed Census Date'] = pd.to_datetime(df['Bed Census Date'])
    return df.groupby(df['Facility ID'])['Bed Census Date'].min()

def beds_top_ten(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the ten census dates with the highest
    number of available beds for the nursing home with the specified facility id
    REQUIREMENTS:
    Do a filter followed by a sort rather than a sort followed by a merge.
    '''
    df = df.filter(items=['Facility ID', 'Bed Census Date','Available Residential Beds'])
    x = df[df['Facility ID'] == facility_id].sort_values('Available Residential Beds', ascending=False).head(10)
    return x['Bed Census Date']

if __name__ == "__main__":
    df = pd.read_csv('data/beds.csv' )
    print df.head()
    number_of_censuses(df, 17)

    df.groupby(df['Facility ID']== 17)['Most Recently Submitted Facility Census Data'].count()
    df[df['Most Recently Submitted Facility Census Data']== True].count()
    df.groupby(df['Facility ID']== 17)[df['Most Recently Submitted Facility Census Data']== True].count()
    df.groupby(df['Facility ID']== 17)[df['Most Recently Submitted Facility Census Data']== True].count()
    df[df['Facility ID']== 17)](df['Most Recently Submitted Facility Census Data'] == True).count()
    df[df['Facility ID'] == 17]
    (df['Most Recently Submitted Facility Census Data'] == True).groupby(df[df['Facility ID']== 17]).count()
    (df['Most Recently Submitted Facility Census Data'] == True).groupby(df['Facility ID']).count()
