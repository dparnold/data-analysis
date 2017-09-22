import os
import matplotlib as plt
from matplotlib.backends.backend_pgf import FigureCanvasPgf
plt.backend_bases.register_backend('pdf', FigureCanvasPgf)
import matplotlib.pyplot as p

# get these values from latex document
textwidth_cm = 15.05293  # A4 page width at a border of 3 cm
font_size = 11

# update plt defauls
inch_per_cm = 0.393700787
golden_mean = (5**.5-1.0)/2.0
fig_width = textwidth_cm * inch_per_cm
fig_height = fig_width * golden_mean * 1 #0.85


# use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# import packages for instance for using SI-units
params = {'text.latex.preamble': [r'\usepackage{siunitx}',
                                  r'\usepackage{sfmath}',
                                  r'\sisetup{detect-family = true}',
                                  r'\usepackage{amsmath}']}
plt.rcParams.update(params)

# update plt defauls
params_resize = {
                 'figure.figsize': (fig_width, fig_height),
                 'figure.subplot.left': 0.175,
                 'figure.subplot.bottom': 0.18,
                 'figure.subplot.right': 0.95,
                 'figure.subplot.top': 0.95,
                 }
p.rcParams.update(params_resize)

params_text = {
               'axes.labelsize': font_size,        # ax labels
               'font.size': font_size,
               'legend.fontsize': font_size-4,
               'xtick.labelsize': font_size-2,     # ticks-labels of x axis
               'ytick.labelsize': font_size-2,
               }
p.rcParams.update(params_text)


params_axes = {
               "axes.titlesize": 15
               }

p.rcParams.update(params_axes)

params_lines = {
               "lines.markersize": 4,
               'lines.linewidth': 1.0,
               }

p.rcParams.update(params_lines)

params_legend = {
                 "legend.numpoints": 1,
                 "legend.fancybox":True
                 }

p.rcParams.update(params_legend)

params_figure = {
                 "figure.dpi": 300
                 }

p.rcParams.update(params_figure)

# change colormap
params_colormap={
                "image.cmap":"inferno"
                }
p.rcParams.update(params_colormap)


# useful functions
def makeInset(ax,scale=0.7):
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(item.get_fontsize()*scale)
        ax.xaxis.labelpad *= scale
        ax.yaxis.labelpad *= scale

def max_ticks(ax=None, nx=5, ny=None):
    ax = p.gca() if ax is None else ax
    ax.xaxis.set_major_locator(plt.ticker.MaxNLocator(nx))
    ax.yaxis.set_major_locator(plt.ticker.MaxNLocator(nx if not ny else ny))

def set_locator_dx(dx, ax=None):
    ax = p.gca() if ax is None else ax
    ax.xaxis.set_major_locator(plt.ticker.MultipleLocator(dx))

def set_locator_dy(dy, ax=None):
    ax = p.gca() if ax is None else ax
    ax.yaxis.set_major_locator(plt.ticker.MultipleLocator(dy))

def savepdf(fname):
    fname_pdf = fname if fname.lower().endswith(".pdf") else fname+".pdf"
    fname_eps = os.path.splitext(fname_pdf)[0]+".eps"    
    p.tight_layout(.5)
    p.savefig(fname_eps)
    os.system("epstopdf '{0}' && rm '{0}'".format(fname_eps))
