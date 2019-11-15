import matplotlib.pyplot as plt
import numpy as np

def plot(learner,nsuggest):
    f,ax  = plt.subplots(1,1)
    plot_func(ax,learner.gps[0].predict,learner.scandetails.thresholds[0],NX= 21, NY = 21)
    ax.scatter(learner.X[:-nsuggest,0],learner.X[:-nsuggest,1],c = 'w', zorder = 999)
    ax.scatter(learner.X[-nsuggest:,0],learner.X[-nsuggest:,1],c = 'r', zorder = 999)
    f.set_size_inches(5,5)

def plotfunc(grid,func):
    NX,NY = grid.shape[1:]
    X = np.swapaxes(grid,0,-1).reshape(NX*NY,2)
    v = func(X)
    v =  v.reshape(NY,NX).T
    return v

def plot_func(ax,func,thresh,vmin = -1, vmax = 1,NX = 101,NY = 101):

    grid = x,y = np.mgrid[0:1:NX*1j,0:1:NY*1j]

    v = plotfunc(grid,func)
    ax.contourf(x,y,v, vmin=vmin,vmax = vmax,levels = 300)
    # ax.colorbar()
    ax.contour(x,y,v, vmin=vmin,vmax=vmax,levels = 30, colors = 'k')
    ax.contour(x,y,v, vmin=vmin,vmax=vmax,levels = [thresh], colors = 'r')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
