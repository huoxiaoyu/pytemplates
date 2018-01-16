from matplotlib import gridspec
sens_id = xsens[xsens.isnull() == False][:30].index
df = piddf[piddf.pid.isin(list(sens_id))]
fig = plt.figure(figsize=(20,30))
gs = gridspec.GridSpec(6, 5)
x = []
for i in range(6):
    x = x + [i]*5
y = range(5)*6

for i in range(len(sens_id)):
    dfx = df[df.pid == sens_id[i]]
    ax = fig.add_subplot(gs[x[i],y[i]])
    plt.scatter(dfx.price_diff, dfx.ifpre)
