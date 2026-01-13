import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv( r'C:\Users\Eitan Tannenbaum\Downloads\mew_data.csv', index_col=0)

# Step 2: Convert the index labels to lowercase
df.index = df.index.str.lower()

# Step 3: Specify the indexes of the rows you want to select
selected_labels = ['Maf'  ,
'Hnf4a'   ,
'Klf5'   ,
'Junb'  ,
'Relb'  ,
'Hivep1',
'Nfkb1' ,
'Tcf7l1' ,
'Fosl1'   ,
'Tead4'  ,
'Pbx1'   ,
'Hnf1b'  ,


'Gatm'    ,
'Slc34a1'  ,
'Plcb1'   ,
'Fhit'    ,
'Bcas3'   ,
'Esrrg'   ,
'Unc13c'  ,
'Kynu'    ,
'Plxdc2'  ,
'Pdzrn3'  ,
'Slc13a'  ,
'Gas2'    ,
'Mpped2'  ,
'Slc16a'  ,
'Btbd3'   ,
'Abca4'   ,
'Slc6a1'  ,
'Gcnt1'   ,
'Atxn2'   ,
'Acsm5'   ,
'Nrg1'    ,
'Pvt1'    ,
'Ptprm'   ,
'Tshz2'   ,
'Myh9'    ,
'Tet3'    ,
'Syne2'   ,
'Sc34a1'  ,
'Dab2'  ,
'Vcam1'  ,
'Havcr1' ,
'Slc6a13' ,
'Slc13a3' ]
selected_labels_lower = [label.lower() for label in selected_labels]
  # Add your specific index labels here

# Print DataFrame before selection
print("DataFrame before selection:")
print(df)

# Step 4: Select the rows with the specified index labels
df_selected = df[df.index.isin(selected_labels_lower)]

# Print DataFrame after selection
print("DataFrame after selection:")
print(df_selected)

# Step 5: Convert selected indexes to all uppercase
df_selected.index = df_selected.index.str.upper()

# Step 6: Save the selected rows to a new CSV file
df_selected.to_csv(r'C:\Users\Eitan Tannenbaum\Downloads\selected_data.csv')
