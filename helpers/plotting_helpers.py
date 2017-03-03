import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns


def plot_correlation_map(df):
    # Compute pairwise correlation of columns
    # using Pearson correlation coefficient
    corr = df.corr()
    
    fig , ax = plt.subplots(figsize = (12, 10))
    cmap = sns.diverging_palette(220 ,10 ,as_cmap = True )    
    ax = sns.heatmap(corr, cmap = cmap, square = True, 
                                 ax = ax, annot = True)
    # Save the figure
    fig.savefig('./figures/correlation_map.png', 
                      bbox_inches='tight')

def plot_categories(df, category, target):
    # Plot a factorplot
    ax = sns.factorplot(category, target, data = df)
    ax.add_legend()
    
    # Save the figure
    ax.savefig('./figures/%s distribution.png' %category, 
                      bbox_inches = 'tight')
   
def plot_histogram(df, variable, target):
    fig = plt.figure(figsize = (8, 6))
    
    # plot histogram segmented by output
    for output, label, color in zip(range(2), ['Not Survived', 'Survived'], ['r', 'g']):
        df[df[target] == output][variable].plot.hist(color = color, label = label,                                                                            
                                                                            alpha = 0.3, edgecolor = 'k')
                                                                               
    plt.xlabel('%s' %variable)
    plt.title("The distribution of %s?" %variable)
    plt.legend(loc='best')
    
    # save the figure
    fig.savefig('./figures/%s distribution.png' %variable, 
                      bbox_inches='tight')
    