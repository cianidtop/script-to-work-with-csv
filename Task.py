import pandas as pd
import csv

file = pd.read_csv('home_task.csv', sep=';', index_col='Order code') #Reading a file, using Pandas


#Check fields to find a passes
issue_date = file['Order Date'] != '2019-11-28'
issue_price = file['Price'] == ''
issue_number = file['Order Number'] == ''
issues = file.loc [issue_date & issue_number & issue_price]
issues.to_csv('Косяки.csv')

#Here I'm creating .csv for every supplier in file. Actually, here's my f*ck up 'cause i did it like copy-n-paste not using
#"For..in.." method because of i don't now how to give not equal names to files...
filter_provide = file['Provide'] == 'suppplier_A'
a_file = file.loc[filter_provide]
a = a_file.fillna(0)# Change passes to zero
a.to_csv('suppplier_A.csv')
#

filter_provide = file['Provide'] == 'suppplier_B'
b_file = file.loc[filter_provide]
b = b_file.fillna(0)# Change passes to zero
b.to_csv('suppplier_B.csv')
#

filter_provide = file['Provide'] == 'suppplier_C'
c_file = file.loc[filter_provide]
c = c_file.fillna(0)# Change passes to zero
c.to_csv('suppplier_C.csv')
#

filter_provide = file['Provide'] == 'suppplier_D'
d_file = file.loc[filter_provide]
d = d_file.fillna(0)# Change passes to zero
d.to_csv('suppplier_D.csv')
#

filter_provide = file['Provide'] == 'suppplier_E'
e_file = file.loc[filter_provide]
e = e_file.fillna(0)# Change passes to zero
e.to_csv('suppplier_E.csv')
#

filter_provide = file['Provide'] == 'suppplier_F'
f_file = file.loc[filter_provide]
f = f_file.fillna(0)# Change passes to zero
f.to_csv('suppplier_F.csv')
#

filter_provide = file['Provide'] == 'suppplier_G'
g_file = file.loc[filter_provide]
g = g_file.fillna(0)# Change passes to zero
g.to_csv('suppplier_G.csv')
#

filter_provide = file['Provide'] == 'suppplier_H'
h_file = file.loc[filter_provide]
h = h_file.fillna(0)# Change passes to zero
h.to_csv('suppplier_H.csv')
#

filter_provide = file['Provide'] == 'suppplier_I'
i_file = file.loc[filter_provide]
i = i_file.fillna(0)# Change passes to zero
i.to_csv('suppplier_I.csv')
#

filter_provide = file['Provide'] == 'suppplier_J'
j_file = file.loc[filter_provide]
j = j_file.fillna(0)# Change passes to zero
j.to_csv('suppplier_J.csv')
#

filter_provide = file['Provide'] == 'suppplier_K'
k_file = file.loc[filter_provide]
k = k_file.fillna(0)# Change passes to zero
k.to_csv('suppplier_K.csv')
#

filter_provide = file['Provide'] == 'suppplier_L'
l_file = file.loc[filter_provide]
l = l_file.fillna(0)# Change passes to zero
l.to_csv('suppplier_L.csv')
#

filter_provide = file['Provide'] == 'suppplier_M'
m_file = file.loc[filter_provide]
m = m_file.fillna(0)# Change passes to zero
m.to_csv('suppplier_M.csv')
#

filter_provide = file['Provide'] == 'suppplier_N'
n_file = file.loc[filter_provide]
n = n_file.fillna(0)# Change passes to zero
n.to_csv('suppplier_N.csv')
#

filter_provide = file['Provide'] == 'suppplier_O'
o_file = file.loc[filter_provide]
o = o_file.fillna(0)# Change passes to zero
o.to_csv('suppplier_O.csv')
#

filter_provide = file['Provide'] == 'suppplier_P'
p_file = file.loc[filter_provide]
p = p_file.fillna(0)# Change passes to zero
p.to_csv('suppplier_P.csv')
#

filter_provide = file['Provide'] == 'suppplier_Q'
q_file = file.loc[filter_provide]
q = q_file.fillna(0)# Change passes to zero
q.to_csv('suppplier_Q.csv')
#

filter_provide = file['Provide'] == 'suppplier_R'
r_file = file.loc[filter_provide]
r = r_file.fillna(0)# Change passes to zero
r.to_csv('suppplier_R.csv')
#

filter_provide = file['Provide'] == 'suppplier_S'
s_file = file.loc[filter_provide]
s = s_file.fillna(0)# Change passes to zero
s.to_csv('suppplier_S.csv')
#

filter_provide = file['Provide'] == 'suppplier_T'
t_file = file.loc[filter_provide]
t = t_file.fillna(0)# Change passes to zero
t.to_csv('suppplier_T.csv')
#

filter_provide = file['Provide'] == 'suppplier_U'
u_file = file.loc[filter_provide]
u = u_file.fillna(0)# Change passes to zero
u.to_csv('suppplier_U.csv')
#

filter_provide = file['Provide'] == 'suppplier_V'
v_file = file.loc[filter_provide]
v = v_file.fillna(0)# Change passes to zero
v.to_csv('suppplier_V.csv')
#

filter_provide = file['Provide'] == 'suppplier_W'
w_file = file.loc[filter_provide]
w = w_file.fillna(0)# Change passes to zero
w.to_csv('suppplier_W.csv')
#

filter_provide = file['Provide'] == 'suppplier_X'
x_file = file.loc[filter_provide]
x = x_file.fillna(0)# Change passes to zero
x.to_csv('suppplier_X.csv')
#

filter_provide = file['Provide'] == 'suppplier_Y'
y_file = file.loc[filter_provide]
y = y_file.fillna(0)# Change passes to zero
y.to_csv('suppplier_Y.csv')
#

filter_provide = file['Provide'] == 'suppplier_Z'
z_file = file.loc[filter_provide]
z = z_file.fillna(0)# Change passes to zero
z.to_csv('suppplier_Z.csv')
#