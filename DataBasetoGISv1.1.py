import pandas as pd

#filelocation
file=raw_input('Insert CSV Path; remove quotes: ')
user1=raw_input('Insert the folder path of where you want to save csv (include final \): ')
user2=raw_input('Name of csv (do not add.csv): ')


#have panda read csv
xl=pd.read_csv(file)

#if Nan found in column pmfromst1, removes row. axis keeps it at rows
pm1=xl.dropna(axis=0,subset=['pmfromst1'])
pm1=pm1.drop(['pmfromst2','pmtost2','pmfromst3','pmtost3'],axis=1)

#remove rows that have Nan in column pmfromst2
pm2=xl.dropna(axis=0,subset=['pmfromst2'])
pm2=pm2.drop(['pmfromst1','pmtost1','pmfromst3','pmtost3'],axis=1)#removes column from otherstations
pm2=pm2.rename(index=str,columns={'pmfromst2':'pmfromst1','pmtost2':'pmtost1'})#rename columns of stationing

#remove rows that have Nan in column pmfromst2
pm3=xl.dropna(axis=0,subset=['pmfromst3'])
pm3=pm3.drop(['pmfromst1','pmtost1','pmfromst2','pmtost2'],axis=1)
pm3=pm3.rename(index=str,columns={'pmfromst3':'pmfromst1','pmtost3':'pmtost1'})

columns=xl.columns[0:10] #defines the columns we want to transfer over; first 10 columns

pm1=pm1.append(pm2,ignore_index=True)
pm1=pm1.append(pm3,ignore_index=True)

#pm1.to_csv(userinput2,index=None,header=True)

pm1.to_csv(user1+ user2+ '.csv',
           index=None,header=True)


