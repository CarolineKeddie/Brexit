import numpy as np
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def autocorr_plots(y, lags=None):
    fig, ax = plt.subplots(ncols=2, figsize=(12, 4), sharey=True)
    plot_acf(y, lags=lags, ax=ax[0])
    plot_pacf(y, lags=lags, ax=ax[1])
    return fig, ax

def ts_arma(mu, phi, theta, y, eps, n=10000, sigma=0.1, plot_range=20, random_state=1):
    
    p = len(phi)
    q = len(theta)
    
    # check for having enough starting values for y and epsilon
    if len(y)<p or len(y)<q:
        print('Not enough starting values!')
        return None, None
    
    elif len(eps) < q and q>0:
        print('Specify more residuals!')
        return None, None
    
    else:
        
        phi_0 = (1-np.sum(phi))*mu

        # create arrays for y-values
        y_true = np.repeat(0.,n+1)
        y_predicted = np.repeat(0.,n+1)
        
        # create random noise
        np.random.seed(1)
        epsilon_true = sigma * np.random.randn(n+1)
        epsilon_predicted = np.repeat(0.,n+1)

        # insert starting values for y and epsilon
        for i in range(len(eps)):
            epsilon_true[i] = eps[i]
            epsilon_predicted[i] = eps[i]
        for i in range(len(y)): 
            y_true[i] = y[i]
            y_predicted[i] = y[i]

        # get the predictons
        for i in range(len(y), n+1):
            
            # add phi_0 and noise term
            y_predicted[i] = phi_0
            y_true[i] = phi_0 + epsilon_true[i]
            
            # get the AR(p) update
            if p > 0:
                if i==p:
                    y_predicted[i] += phi.dot(y_predicted[i-1::-1])
                    y_true[i] += phi.dot(y_true[i-1::-1])
                else:
                    y_predicted[i] += phi.dot(y_predicted[i-1:i-(p+1):-1])
                    y_true[i] += phi.dot(y_true[i-1:i-(p+1):-1])
           
            # get the MA(q) update
            if q > 0:
                if i==q:
                    y_predicted[i] += theta.dot(epsilon_predicted[i-1::-1])
                    y_true[i] += theta.dot(epsilon_true[i-1::-1])
                else:
                    y_predicted[i] += theta.dot(epsilon_predicted[i-1:i-(q+1):-1]) 
                    y_true[i] += theta.dot(epsilon_true[i-1:i-(q+1):-1]) 

        # plot the time series
        plt.plot(list(range(plot_range)), y_true[:plot_range], label='time series')
        plt.plot(list(range(plot_range)), y_predicted[:plot_range], label='predictions')
        plt.legend()
        plt.show()

        return y_true, y_predicted, epsilon_true