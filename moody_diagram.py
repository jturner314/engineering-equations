#!/usr/bin/env python3

# Copyright (C) 2013  Jim Turner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt
import numpy as np
from numpy import log10, sqrt
from scipy.optimize import brentq

@np.vectorize
def solve_colebrook(rel_roughness, reynolds_num):
    """Solve the Colebrook equation for the friction factor.

    Positional arguments:
    rel_roughness -- absolute roughness / pipe diameter
    reynolds_num -- Reynolds number of the flow

    """
    def colebrook(f):
        return 1/sqrt(f) + 2*log10(rel_roughness/3.7 + 2.51/(reynolds_num*sqrt(f)))
    return brentq(colebrook, 0.005, 0.1)

def format_num(num, precision=1):
    """Format a decimal number in LaTeX math.

    Numbers with a base-10 exponent less than -3 or greater than 3 are formatted
    in scientific notation.

    Positional argument:
    num -- the number to format

    Keyword argument:
    precision -- the precision of the mantissa for scientific notation

    """
    exponent = np.floor(log10(num))
    mantissa = num / 10**exponent
    if -3.1 < exponent < 3.1:
        return '${}$'.format(num)
    else:
        format_str = r'${:.'+str(precision)+r'f}\times10^{{{:.0f}}}$'
        return format_str.format(mantissa, exponent)

def main():
    """Plot a Moody chart and write it to moody-diagram.eps in the working directory.

    This plots a basic moody chart with the relevant lines and annotations for
    transitional flow and smooth pipes. The friction factors for the turbulent
    region are calculated by solving the implicit Colebrook equation.

    """
    # Change figure size and font to match LaTeX
    fig_width = 450 / 72.27
    plt.rc('axes', labelsize=10)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', serif='Computer Modern Roman', size=10)
    plt.rc('figure', figsize=(fig_width, fig_width*0.7))

    # Axes parameters, data points, label values
    xmin, xmax = 5E2, 1E8
    ymin, ymax = 0.008, 0.1
    laminar_Re = np.linspace(1, 2100, 100)
    turbulent_Re = np.logspace(log10(2100), log10(xmax), 100)
    rel_roughness = np.array((5E-2, 4E-2, 3E-2, 2E-2, 1.5E-2, 1E-2, 8E-3, 6E-3, 4E-3,
                              2E-3, 1E-3, 5E-4, 2E-4, 1E-4, 5E-5, 2E-5, 1E-5))
    friction_labels = (0.008, 0.009, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.025,
                       0.03, 0.035, 0.04, 0.045, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1)

    # Laminar flow
    plt.plot(laminar_Re, 64/laminar_Re, 'b-')

    # Turbulent flow
    for rough in rel_roughness:
        plt.plot(turbulent_Re, solve_colebrook(rough, turbulent_Re), 'b-')

    # Smooth pipe
    plt.plot(turbulent_Re, solve_colebrook(0, turbulent_Re), 'b-')
    plt.annotate("Smooth Pipe", xy=(2E6, solve_colebrook(0, 2E6)), xycoords='data',
                 xytext=(-20,-20), textcoords='offset points', ha='right',
                 backgroundcolor='w', arrowprops={'arrowstyle': '->'})

    # Transitional flow
    plt.axvspan(2100, 4000, color='#d9d9ff')
    plt.annotate("Transitional Flow", xy=(3050,0.0135), xycoords='data',
                 xytext=(20,-20), textcoords='offset points',
                 backgroundcolor='w', arrowprops={'arrowstyle': '->'})

    # Grid
    plt.grid(which='both', color='gray', ls='-', lw=0.2)
    for line in plt.gca().lines:
        line.set_zorder(3)

    # Reynolds number labels (horizontal axis)
    plt.xlim(xmin, xmax)
    plt.xscale('log')
    plt.xlabel(r"Reynolds Number, $\mathit{Re}=\rho{}VD/\mu$")

    # Friction factor labels (left vertical axis)
    plt.ylim(ymin, ymax)
    plt.yscale('log')
    plt.gca().tick_params(which='both', right='off', top='off')
    plt.yticks(friction_labels, [format_num(fric) for fric in friction_labels])
    plt.ylabel(r"Friction Factor, $f$")

    # Relative roughness labels (right vertical axis)
    plt.twinx()
    plt.ylim(ymin, ymax)
    plt.yscale('log')
    plt.yticks(solve_colebrook(rel_roughness, xmax),
               [format_num(rough, 0) for rough in rel_roughness])
    plt.gca().tick_params(which='both', bottom='off', top='off', left='off', right='off')
    plt.ylabel(r"Relative Roughness, $\varepsilon/D$")

    # Save figure
    plt.savefig("moody-diagram.eps", bbox_inches='tight')

if __name__ == '__main__':
    main()
