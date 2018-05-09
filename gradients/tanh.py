from __future__ import print_function

import numpy as np

def eval_numerical_gradient(f, x, verbose=False, h=1e-5):
    """A naive implementation of numerical gradient of f at x.

    Used for gradient checking.

    f: function taking a single array argument and returning a scalar.
    x: array starting point for evaluation.

    Based on http://cs231n.github.io/assignments2016/assignment1/, with a
    bit of cleanup.
    Also uses the centered formula described in
    http://cs231n.github.io/neural-networks-3/#gradcheck

    Returns a numerical gradient, same shape as x.
    """
    grad = np.zeros_like(x)
    # iterate over all indexes in x
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        oldval = x[ix]
        x[ix] = oldval + h
        fxph = f(x) # evalute f(x + h)
        x[ix] = oldval - h
        fxmh = f(x) # evaluate f(x - h)
        x[ix] = oldval # restore

        # compute the partial derivative with centered formula
        grad[ix] = (fxph - fxmh) / (2 * h)
        if verbose:
            print(ix, grad[ix])
        it.iternext()
    return grad


def tanh_grad(x):
    return 1 - np.tanh(x) ** 2


if __name__ == '__main__':
    x = np.array([1.0, 2.1, 0.3, 0.7])
    print('tanh', np.tanh(x))
    print('tanh_grad', tanh_grad(x))

    # Note: eval_numerical_gradient works for scalar functions. Therefore we'll
    # run it for each element of tanh separately.
    print('Numerical gradient')
    for i in range(x.shape[0]):
        print(i, eval_numerical_gradient(lambda z: np.tanh(z)[i], x))
