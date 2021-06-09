from numpy.core.numeric import NaN
import pandas as pd
from columns import col
# data=pd.read_excel(r'\\192.168.1.39\Muniyappan\DryOut\yvrokar.XLSX')
df_yvrokar=pd.read_excel(r'\\192.168.1.39\Muniyappan\DryOut\yvrokar.XLSX')
df_yvrokar.columns=[sub.replace('.', '') for sub in df_yvrokar.columns]
df_yqlab=pd.read_excel(r'\\192.168.1.39\Muniyappan\DryOut\yqlab.XLSX')
df_yqlab.columns=[sub.replace('.', '') for sub in df_yqlab.columns]
boolean=df_yvrokar['Tank'].isna()
df_yvrokar=df_yvrokar[~boolean]
df_yvrokar["QtyDiff"]=df_yvrokar["Physical Balance"]-df_yvrokar["Quantity"]
df_yvrokar["Status"]=df_yvrokar["QtyDiff"].map(lambda x:"Dormant" if abs(x)<10 else ("Receipt" if x>10 else "Dispatch"))
df_yqlab=df_yqlab[df_yqlab['Sample Type']=='COMPOSITE']
df_yqlab=df_yqlab[df_yqlab['Inspection Lot']!=0]
df_yqlab.sort_values(['SNo'],inplace=True,ignore_index=True)
df_yqlab=df_yqlab[col] #[df_yqlab['Storage Tank']=='T006']
df_yvrokar=df_yvrokar.astype('str')
df_yqlab=df_yqlab.astype('str')
df = pd.merge(left=df_yvrokar, right=df_yqlab, how='inner',left_on=['Tank'], right_on=['Storage Tank'])
df['Material']=df['Material_x']
print(df.columns)
df=df[['Tank','SNo','Lab Register No', 'Plant','Batch','Inspection Lot', 'Material',
       'Material Description', 'Qty in Storage (KL)', 'Sample Drawn By',
       'Sample Drawn Date', 'Source of Sample', 'Name of Source',
       'Sample Type', 'Qty of Sample (L)', 'Test Required', 'Test Reason',
       'Last Receipt Date', 'Test Laboratory',
       'Dispatching Location Test Report No', 'SKO Flash Point', 'Created By',
       'Created On']]
print(df)