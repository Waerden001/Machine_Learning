#@title ```time_series.py```


def plot_column(df, feature):
    """Plot the resampled column of df, e.g. plot_column(df, "Inflation") plots the "Inflation" column
    
    :param: df, pandas.DataFrame, the data, e.g. df = pd.read_excel("USMacroData", "All")
    :param: feature, str, name of column to be plotted. 
    """
    y = df[feature]
    y.plot(figsize=(15, 6))
    plt.show()


def plot_component(df, feature):
    """Decompose the time series data into trend, seasonal, and residual components.
    
    :param: df, pd.DataFram.
    :param: feature, str,column name/feature name we want to decompose
    :rtype: None
    """
    decomposition = sm.tsa.seasonal_decompose(df[feature], model='additive',freq=52)
    fig = decomposition.plot()
    plt.show()
    ###### This section uses ARIMA to analyze the data and make predictions.########################################

# Grid search to find the best ARIMA parameters 
def arima_parameters(df, feature, search_range=2):
    """Grid search for the optimal parameters of the Arima model for given data (df) and feature.
    :param: df, pdf.DataFrame, data
    :param: feature, str, feature name.
    :param: search_range, int, the range for the search of the parameters, the default value is 2
    """
    p = d = q = range(0, search_range)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    
    minimal_aic = 0
    optimal_param =[]
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(df[feature],order=param, seasonal_order=param_seasonal, enforce_stationarity=False, enforce_invertibility=False)
                results = mod.fit()
                print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                if results.aic < minimal_aic:
                    optimal_param = [param, param_seasonal]
                    minimal_aic = results.aic
                    print(minimal_aic)
            except:
                continue
    print('\n Optimal parameters ARIMA{}x{}12 - Minimal AIC:{}'.format(optimal_param[0], optimal_param[1], minimal_aic))
    return optimal_param[0], optimal_param[1]
