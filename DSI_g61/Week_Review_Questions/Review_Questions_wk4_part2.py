# Week 4 Part 2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 16})

def cost(X, y, coeffs):
    if X.shape[1] == coeffs.shape[0]:
        N = X.shape[0]
        yp = np.dot(X, coeffs)
        return 1/N * np.sum((y-yp)**2)
    else:
        raise ValueError("Error: array dimension mismatch.")

def grad_cost(X, y, coeffs):
    if X.shape[1] == coeffs.shape[0]:
        N = X.shape[0]
        yp = np.dot(X, coeffs)
        return -2/N * np.dot(X.T, (y - yp))
    else:
        raise ValueError("Error: array dimension mismatch.")

def update_coeffs(coeffs, alpha, grad_cost):
    return coeffs - alpha * grad_cost

def batch_grad_descent(X, y, coeffs, alpha, m_iter=10000, eps_conv=0.005):
    cost_new = 1
    costs = []
    for i in range(m_iter):
        cost_old = cost_new
        cost_new = cost(X, y, coeffs)
        costs.append(cost_new)
        converged = abs((cost_new - cost_old))/cost_old < eps_conv
        if converged:
            break
        grad_coeffs = grad_cost(X, y, coeffs)
        coeffs = update_coeffs(coeffs, alpha, grad_coeffs)
    print("Coefficients converged at {0} iterations.".format(i))
    return coeffs, costs

def plot_costs(costs):
    num_costs = len(costs)
    iterations = range(num_costs)
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.plot(iterations, costs, 'k-')
    ax.set_title('Cost function for batch gradient descent')
    ax.set_xlabel('iteration')
    ax.set_ylabel('cost')
    plt.show()


if __name__ == '__main__':
    X = np.array([[-9, -7, -1],
                  [ 6, -5, -2],
                  [-7, -1,  8],
                  [ 3, -1,  6]])

    y = np.array([[-26],
                  [-10],
                  [ 15],
                  [ 19]])

    alpha = 0.0001
    coeffs = np.array([[1, 1, 1]]).T
    print("\nInitial guesses for coefficients")
    print(coeffs)
    grad_coeffs = grad_cost(X, y, coeffs)
    print("\nGradients after 1 update")
    print(grad_coeffs)
    coeffs = update_coeffs(coeffs, alpha, grad_coeffs)
    print("\nCoefficients after 1 update")
    print(coeffs)
    print("\nPerforming batch gradient descent...")
    coeffs = np.array([[1, 1, 1]]).T
    coeffs, costs = batch_grad_descent(X, y, coeffs, alpha, eps_conv=0.009)
    print("Coefficients:")
    print(coeffs.round(4))
    print("(FYI the true coefficients were [1, 2, 3].T)")
    print("Plotting cost curve...")
    plot_costs(costs)
