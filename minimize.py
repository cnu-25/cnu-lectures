from scipy.optimize import minimize as sp_minimize

import jax


__all__ = \
    [
        "minimize"
    ]


def minimize(fun, *args, **kwargs):
    """Wrapper for :func:`scipy.optimize.minimize` using JAX for
    gradient-based minimization. Automatically constructs `jac` from `fun`
    using :func:`jax.vjp`.
    """

    J_vjp_cache = None

    def J_vjp(x):
        nonlocal J_vjp_cache
        if J_vjp_cache is None or not (J_vjp_cache[0] == x).all():
            J_vjp_cache = x.copy(), jax.vjp(fun, x)
        return J_vjp_cache[1]

    def J(x):
        J_val, _ = J_vjp(x)
        return J_val

    def dJ(x):
        _, vjp = J_vjp(x)
        dJ_val, = vjp(1.0)
        return dJ_val

    return sp_minimize(J, *args, jac=dJ, **kwargs)
