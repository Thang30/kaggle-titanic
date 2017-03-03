from sklearn import model_selection
import matplotlib.pyplot as plt

def evaluate_models(models, X_train, Y_train):
    results = []
    names = []
    scoring = 'accuracy'
    for name, model in models:
        # cross-validation
        kfold = model_selection.KFold(n_splits = 10, random_state = 7)
        cv_results = model_selection.cross_val_score(model, 
                                                     X_train, Y_train, cv = kfold, 
                                                     scoring = scoring)
        
        # store the results
        results.append(cv_results)
        names.append(name)
        message = "%s: %f +/- %f" % (name, cv_results.mean(), cv_results.std())
        print(message)
    return results, names
        
def boxplot_algorithm_comparison(results, names):
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)

