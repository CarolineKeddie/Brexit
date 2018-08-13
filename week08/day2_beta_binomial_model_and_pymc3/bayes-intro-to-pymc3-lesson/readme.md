<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Bayesian Estimation and Regression with `pymc3`


---


### Core

- Know that `pymc3` uses Markov-Chain Monte-Carlo methods to create samples from the posterior distribution
- Conduct a Frequentist hypothesis test using `stats.ttest_ind()` and explain why you reject or fail to reject the null hypothesis
- Conduct a Bayesian hypothesis test with `pymc3`
- Conduct Bayesian regression with `pymc3`
- Copy and paste the code for the `pymc3` model, and understand which parts of the code you need to change to suit your investigation
- Interpret the plots/print-outs that you get with `pm.plot_posterior`, `pm.summary`,  `pm.trace_to_dataframe`, and `pm.traceplot`

### Target
- Set up a `pymc3` model using a patsy formula
- Plot different possible regression lines using `pm.glm.plot_posterior_predictive`
- Explain the different choices for the distributions used for the priors and likelihoods (uniform and normal in these examples)
