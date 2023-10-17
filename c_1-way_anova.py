import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib import rcParams
import csv

def load_csv(filename, skip_first_row=True, delimiter=','):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        out = []
        i = 0
        for row in reader:
            if(skip_first_row == True):
                if(i == 0):
                    i = i + 1
                    continue

            out.append(row)
            i = i + 1
        
    return out

def main():
    alpha = 0.05

    filename = '../../data/th_incomes.csv'
    x = load_csv(filename, False, ',')
    
    # --------------------------------------------------------------------
    # Prepare input data
    # --------------------------------------------------------------------
    xp = []
    for i in range(1, len(x), 1):
        #x[i][0] = int(x[i][0])
        x[i][1] = float(x[i][1])
        x[i][2] = float(x[i][2])
        x[i][3] = float(x[i][3])
        x[i][4] = float(x[i][4])
        x[i][5] = float(x[i][5])
        x[i][6] = float(x[i][6])
        x[i][7] = float(x[i][7])
        x[i][8] = float(x[i][8])
        x[i][9] = float(x[i][9])
        x[i][10] = float(x[i][10])
        #x[i][11] = float(x[i][11])
        #x[i][12] = float(x[i][12])

        xp.append(x[i][1:11])
    xp = numpy.asarray(xp)

    # --------------------------------------------------------------------
    # Generate graph
    # --------------------------------------------------------------------
    plt.clf()
    plt.figure(figsize=(8,8))
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['TH SarabunPSK']
    data = [
        xp[0,:],
        xp[1,:],
        xp[2,:],
        xp[3,:],
    ]
    labels = [
        x[0][0],
        x[1][0],
        x[2][0],
        x[3][0],
    ]
    plt.boxplot(
        data,
        labels=labels,
        showmeans=True,
        meanline=True)
    plt.tight_layout()
    plt.savefig(
        'th_incomes.png', 
        dpi=200)

    # --------------------------------------------------------------------
    # Perform one-way ANONA
    # --------------------------------------------------------------------
    result = 0.0

    # Show the result
    if(result.pvalue < alpha):
        print('Means of the input data are statistically different.')
    else:
        print('Means of the input data are NOT statiscally different.')


if __name__ == '__main__':
    main()