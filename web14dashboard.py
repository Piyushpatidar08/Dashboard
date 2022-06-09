#!/usr/bin/env python
# coding: utf-8

# In[99]:


from piyush import *


# In[100]:


input01 = get_data_by_subsheet("https://docs.google.com/spreadsheets/d/1Gdkv8PxMbHTTRBOB87XvQ08-o75L5sWmUD1xjln73as/edit#gid=0","input_01")


# In[101]:


input01=  input01[input01['Student_code'].map(len) > 6].reset_index()


# In[102]:


input01.drop(['index'],1,inplace = True)


# In[103]:


input01['Student_code'] = input01['Student_code'].str.lower()


# In[104]:


input01['Company'] = input01['Company'].str.lower()


# In[105]:


input01.drop(input01[input01['Student_code'] == 'fwqr_091'].index, inplace = True)


# In[106]:


input01.drop(input01[input01['Student_code'] == 'fw14_546'].index, inplace = True)


# In[107]:


#fw14_546


# In[ ]:





# In[108]:


input01['Company'] = input01.Company.replace('kennect','kennect.io')


# In[109]:


input01['Company'] =  input01.Company.replace('cloudboom','cloudbloom')


# In[110]:


#import sys
#sys.path.append('/home/ubuntu/analytics/saket/my_modules/')
#from drive_file import *


# In[111]:


#data =get_data_by_subsheet("https://docs.google.com/spreadsheets/d/1vlyCW9nFwuNtj6CIm2ng4Mm8AZfG3Y4R1-fyb4kKedQ/edit#gid=0","compid")


# In[112]:


#ws=gc.open_by_url("https://docs.google.com/spreadsheets/d/1vlyCW9nFwuNtj6CIm2ng4Mm8AZfG3Y4R1-fyb4kKedQ/edit#gid=0")
#values=ws.worksheet('compid').get_all_values()
#data=pd.DataFrame(values[2:],columns=values[1])


# In[113]:


#data


# In[114]:


#compi = data[['Company Name','Company Profile ID']]


# In[115]:


#compi['Company Name'] = compi['Company Name'].str.lower()


# In[116]:


#[['Student_code','Company Profile ID','Date']]


# In[117]:


#compi


# In[118]:


#compopp = pd.merge(input01,compi,how='left', left_on = ['Company'], right_on = ['Company Name'])#[['Student_code','Company Profile ID','Date']]


# In[119]:


#compopp


# In[120]:


#populate("https://docs.google.com/spreadsheets/d/1vlyCW9nFwuNtj6CIm2ng4Mm8AZfG3Y4R1-fyb4kKedQ/edit#gid=112670257","web14",compopp)


# In[121]:


#newdf = compopp.drop_duplicates(
  #subset = ['Student_code', 'Company Profile ID'],
  #keep = 'first').reset_index(drop = True)


# In[122]:


#newdf


# In[123]:


#from piyush import *


# In[124]:


#populate("https://docs.google.com/spreadsheets/d/1-SEnlmKIiG72bRhxc0w39mt2mVKDVp5abs0zWd-UCiY/edit#gid=400493859","raw14",lastround1)


# In[125]:


#lastround = pd.merge(input01,compi,how='left', left_on = ['Company'], right_on = ['Company Name'])[['Student_code','Company Profile ID','Date','Round']]


# In[126]:


#lastround1 = lastround.drop_duplicates(
  #subset = ['Student_code', 'Company Profile ID'],
  #keep = 'last').reset_index(drop = True)


# In[127]:


#lastround1[lastround1['Company Profile ID'].isna()]


# In[128]:


#populate("https://docs.google.com/spreadsheets/d/1-SEnlmKIiG72bRhxc0w39mt2mVKDVp5abs0zWd-UCiY/edit#gid=400493859","raw14",lastround1)


# In[ ]:





# In[129]:


studash = pd.pivot_table(input01, index = ['Student_code','Name','Flag'],columns = ['Round'],values = 'Company' ,aggfunc='count',fill_value='0')


# In[130]:


studash


# In[131]:


input01[input01['Student_code'] == 'fwqr_091']


# In[132]:


studash


# In[133]:


studash.columns.name = None
studash = studash.reset_index()


# In[134]:


studash['Student_code'] = studash['Student_code'].str.lower()


# In[ ]:





# In[135]:


ca = input01[['Student_code','Company']].groupby(['Student_code']).nunique()


# In[136]:


ca


# In[137]:


ca.columns.name = None
ca = ca.reset_index()


# In[138]:


ca['total_company_applied'] = ca['Company']


# In[139]:


ca.drop(['Company'],axis = 1,inplace = True)


# In[140]:


ca['Student_code'] = ca['Student_code'].str.lower()



# In[141]:


ca.Student_code.value_counts()


# In[142]:


studentdashboard = pd.merge(studash,ca,how = 'left',left_on = ['Student_code'],right_on = ['Student_code'])


# In[143]:


studentdashboard.rename(columns = {1:'Round_1',2:'Round_2',3:'Round_3',4:'Round_4',5:'Round_5'}, inplace = True)


# In[147]:


studentdashboard['Student_code'].value_counts()


# In[148]:


#studentdashboard.drop(['index'],axis =1,inplace = True)


# In[150]:


populate("https://docs.google.com/spreadsheets/d/1Gdkv8PxMbHTTRBOB87XvQ08-o75L5sWmUD1xjln73as/edit#gid=0","student_dashboard",studentdashboard)


# In[48]:


#pipeline = pd.pivot_table(input01, index = [''])


# In[151]:


studash = pd.pivot_table(input01, index = ['Student_code','Name','Flag'],columns = ['Round'],values = 'Company' ,aggfunc='count',fill_value='0')


# In[152]:


pipeline = pd.pivot_table(input01, index = ['Student_code','Name','Flag'],columns = ['Company'],values = ['Round'] )


# In[153]:


input01.columns


# In[154]:


new = input01[['Student_code', 'Name', 'Flag','Company', 'Round', 'Date',
       'Start_Time']]


# In[155]:


new['Shedule'] = new[new.columns[4:]].apply(
    lambda x: '/ '.join(x.dropna().astype(str)),
    axis=1
)


# In[156]:


new


# In[157]:


df = new.drop_duplicates(['Student_code', 'Company'], keep='last').reset_index()


# In[158]:


df


# In[159]:


df.drop(['index','Round','Date','Start_Time'],axis=1,inplace = True)


# In[160]:


#df.drop(['Name','Flag'],axis=1,inplace = True)


# In[161]:


df


# In[162]:


pipeline = df.pivot_table(index = ['Student_code','Name','Flag'], columns = 'Company',values='Shedule',aggfunc=lambda x: ' '.join(x)).fillna('')


# In[163]:


pipeline.columns.name = None
pipeline = pipeline.reset_index()


# In[164]:


pipeline


# In[165]:


populate("https://docs.google.com/spreadsheets/d/1Gdkv8PxMbHTTRBOB87XvQ08-o75L5sWmUD1xjln73as/edit#gid=307549406","pipeline",pipeline)


# In[166]:


new_df = (
    input01.pivot_table(index=['Company'],
                    columns = ['Round'],values='interviewType',
                    aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
)


# In[167]:


new_df


# In[168]:


totalstudent = pd.DataFrame(input01['Student_code'].groupby(input01['Company']).nunique())


# In[169]:


totalstudent.columns.name = None
totalstudent = totalstudent.reset_index()


# In[170]:


comp_dash = pd.merge(new_df,totalstudent, how = 'left', left_on=['Company'], right_on = ['Company'])
comp_dash


# In[171]:


comp_dash['total_student_applied'] = comp_dash['Student_code']

comp_dash = comp_dash.drop('Student_code',axis=1)


# In[172]:


comp_dash.rename(columns = {1:'Round_1',2:'Round_2',3:'Round_3',4:'Round_4',5:'Round_5'}, inplace = True)


# In[173]:


comp_dash 


# In[174]:


populate("https://docs.google.com/spreadsheets/d/1Gdkv8PxMbHTTRBOB87XvQ08-o75L5sWmUD1xjln73as/edit#gid=1298863868","company_dashboard",comp_dash)


# In[175]:


studentdashboard['Round_1'] = studentdashboard['Round_1'].astype(float)
studentdashboard['Round_2'] = studentdashboard['Round_2'].astype(float)
studentdashboard['Round_3'] = studentdashboard['Round_3'].astype(float)
studentdashboard['Round_4'] = studentdashboard['Round_4'].astype(float)
studentdashboard['Round_5'] = studentdashboard['Round_5'].astype(float)


# In[176]:


studentdashboard['total_round_given'] = studentdashboard['Round_1'] + studentdashboard['Round_2'] + studentdashboard['Round_3'] + studentdashboard['Round_4'] + studentdashboard['Round_5']
studentdashboard['total_round_clear'] = studentdashboard['Round_2'] + studentdashboard['Round_3'] + studentdashboard['Round_4'] + studentdashboard['Round_5']
studentdashboard['round_clear_percentage'] = (studentdashboard['total_round_clear']  / studentdashboard['total_round_given'])*100


# In[177]:


studentdashboard.rename(columns = {'Student_code':'code','Name':'name','Flag':'flag','Round_1':'round_1','Round_2':'round_2','Round_3':'round_3','Round_4':'round_4'},inplace = True)


# In[178]:


pd.read_sql("select*from web14dashboard",engine1).columns


# In[179]:


#engine1.execute("alter table web14dashboard add round_4 float")


# In[180]:


for index,row in studentdashboard.iterrows():
    fields=tuple(row[row.notnull()].index)
    values=tuple(row[row.notnull()].values)
    s=" ,".join(["{}=EXCLUDED.{}".format(x,x) for x in fields])
    fields=" ,".join(fields)
    query="""insert into web14dashboard ({}) values {} ON CONFLICT (code) DO UPDATE set {} ;""".format(fields,values,s)
    engine1.execute(query)
    print(index,query)


# In[181]:


#studentdashboard.to_sql('web14dashboard', con=engine1)


# In[182]:


studentdashboard


# In[81]:


#engine1.execute("CREATE UNIQUE INDEX index_code ON web14dashboard (code);")


# In[82]:


pd.read_sql("select*from web14dashboard",engine1)


# In[83]:


#engine1.execute("ALTER TABLE web14dashboard add COLUMN Round_5 float;")


# In[84]:


#engine1.execute("delete from web14dashboard where code = 'fwqr_091'")


# In[85]:


#engine1.execute("GRANT ALL on web14dashboard TO analytics;")


# In[ ]:





# In[ ]:




