import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")
print(df.head(5))
# 2

df['overweight'] = ((df['weight']/(df['height']/100)**2) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_verse = ['cardio'], value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    fig = sns.catplot(
        data = df_cat, x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar').fig
    

    # 8


    # 9
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 11: Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Diastolic ≤ Systolic
        (df['height'] >= df['height'].quantile(0.025)) &  # Remove shortest 2.5%
        (df['height'] <= df['height'].quantile(0.975)) &  # Remove tallest 2.5%
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Remove lightest 2.5%
        (df['weight'] <= df['weight'].quantile(0.975))    # Remove heaviest 2.5%
    ]

    # 12: Compute correlation matrix
    corr = df_heat.corr()

    # 13: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15: Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    # 16: Save and return figure
    fig.savefig('heatmap.png')
    return fig
