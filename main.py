# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
###################PACKAGES#########################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.ticker as tck
from matplotlib.ticker import FuncFormatter

####################################################

####################CLASSES#########################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

####################################################
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#################SAMPLE SPACE#######################


fig, ax = plt.subplots()


######Function Range############
#xrange = 2*np.pi     #X axis in terms of \pi
xrange = 5

yrange = 3

###########DISCONTINUOUS FUNCTIONS###############
def df(k):
    y = abs(k)/k
    y[:-1][np.diff(y) >= 0.5] = np.nan
    return y


x = np.linspace(-xrange, xrange, 200000)
#y1 = (np.sin(x))
#y2 = (np.cos(x))
y3 = df(x)

plt.xlim(-xrange, xrange)
plt.ylim(-yrange, yrange)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.axvline(x = 0, color = 'k', linestyle = '-')

#ax.plot(x, y1,label = r'$Sin(x)$')
#ax.plot(x, y2,label = '$Cos(x)$')
ax.plot(x, y3,label = r'$\frac{|x|}{x}$')

ax.grid()


'''
############################################################
q = ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))
def frac3(num,d0):
    gcd = np.gcd(num, d0)
    n1 = num/gcd
    d1 = d0/gcd

    if n1 == d1:
        wh_num = 'nil'
        deno = 'nil'
        numer = 'nil'
    elif n1>d1:
        wh_num = n1//d1
        st = n1%d1
        if st == 0:
            deno = 'nil'
            numer = 'nil'
        else:
            deno = d1
            numer = st
    elif n1<d1:
        wh_num = 'nil'
        deno = d1
        numer = n1
    else:
        wh_num = 0
        deno = 'nil'
        numer = 'nil'


    return(wh_num, numer, deno)

def format_func(value, tick_number):
    """Formatter for setting the xticks to multiples of \pi/4."""
    k = int(np.round(4*value/np.pi))
    if k<0:
        sign = "-"
    else:
        sign = ""
#####################################
    f = frac3(abs(k), 4)
    wh_num = f[0]
    numer = f[1]
    denom = f[2]

    if wh_num == 'nil' and numer == 'nil' and denom == 'nil':
        return '$' + sign + '\pi' + '$'
    elif wh_num == 'nil' and numer == 0:
        return '0'
    elif wh_num == 'nil':
        return '$' + sign + r'\frac{' + str(int(numer)) + '}{' + str(int(denom)) + '}' + '\pi' + '$'
    elif numer == 'nil' and denom == 'nil':
        return '$' + sign + str(int(wh_num)) + '\pi' + '$'
    else:
        return '$' + sign + str(int(wh_num)) + r'\frac{' + str(int(numer)) + '}{' + str(int(denom)) + '}' + '\pi' + '$'
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
############################################################
'''


ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Function')
plt.legend()

plt.show()