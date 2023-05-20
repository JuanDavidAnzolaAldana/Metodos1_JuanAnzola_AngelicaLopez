import os
import urllib.request
import numpy
import pandas
import emcee
import corner
import matplotlib.pyplot as plt
#Punto a
def cargar():
    if not os.path.exists(os.path.dirname(__file__)+"/Data"):
        os.mkdir(os.path.dirname(__file__)+"/Data")
    if not os.path.exists(os.path.dirname(__file__)+"/Data/metropolis.csv"):
        url="https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Gaussiano.csv"
        urllib.request.urlretrieve(url,os.path.dirname(__file__)+"/Data/metropolis.csv")
    return pandas.read_csv(os.path.dirname(__file__)+"/Data/metropolis.csv")
#Punto b
def logPrior(p):
    m,s=p
    if 3<=m and m<=5 and 0.5<=s and s<=3.5:
        return 0
    else:
        return -numpy.infty
#Punto c
def Likelihood(p,x):
    m,s=p
    return numpy.exp(-((x-m)**2)/(2*(s**2)))/(s*((2*numpy.pi)**(1/2)))
#Punto d
def logPosterior(p,x):
    pri=logPrior(p)
    if numpy.isfinite(pri):
        return numpy.sum(numpy.log(Likelihood(p,x)))+pri
    else:
        return -numpy.infty
#Puntos e, f, g
def Metropolis(X,Posterior):
    n_walkers, n_params = 5, 2
    p0 = numpy.zeros((n_walkers,n_params))
    p0[:,0] = 2.
    p0[:,1] = 2.
    p0 += numpy.random.rand(n_walkers,n_params)
    sampler = emcee.EnsembleSampler(n_walkers,n_params,Posterior,args=[X])
    pos,prob,state = sampler.run_mcmc(p0,20000,progress=True)
    fig, axes = plt.subplots(n_params, figsize=(10, 5), sharex=True)
    samples = sampler.get_chain()
    labels = ["$\mu$","$\sigma$"]
    for i in range(n_params):
        ax = axes[i]
        ax.plot(samples[:,:,i], "k", alpha=0.7)
        ax.set_xlim(0, len(samples))
        ax.set_ylabel(labels[i],rotation=0, fontsize=15)
        ax.yaxis.set_label_coords(-0.1, 0.5)
    axes[-1].set_xlabel("step number",fontsize=15)
    plt.show()
    flat_samples = sampler.get_chain(discard=1000, thin=15, flat=True)
    truths = numpy.percentile(pos, 50, axis=0)
    figure = corner.corner(flat_samples, 
                       truths=truths, 
                       labels=labels, 
                       show_titles=True)
    plt.show()
X=cargar().x
Metropolis(X, logPosterior)