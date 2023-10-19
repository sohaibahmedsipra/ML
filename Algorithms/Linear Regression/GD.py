import matplotlib.pyplot as plt
import pandas as pd


def grad_descent (m,b,points,L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].studyhours
        y = points.iloc[i].score

        m_gradient += (-1)*(2/n)*x*(y-(m*x+b))
        b_gradient += (-1)*(2/n)*(y-(m*x+b))

    new_m = m-(m_gradient*L)
    new_b = b-(b_gradient*L)

    return new_m,new_b


def main():
    # Importing the dataset
    dataset = pd.read_csv('data.csv')

    m=0;
    b=0;
    L = 0.0001
    epochs = 300

    for i in range(epochs):
        if(i%50==0):
            print("Epochs ",i)
        m,b = grad_descent(m,b,dataset,L)

    print("Final Coefficients-> m:",m," b:",b)

    plt.scatter(dataset.studyhours,dataset.score,color="black")
    plt.plot(list(range(0,50)),[m*x+b for x in range(0,50)],color="red" )
    plt.show()

if __name__ == "__main__":
    main()
