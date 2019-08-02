from scipy.special import erfinv

SQ2 = 2.0**0.5


def get_z(alpha):
    y = 2*(1-alpha) - 1
    return SQ2*erfinv(y)


def get_conf(mean, sigma, n, conf):
    z = 1 - conf/100
    error = get_z(z/2)
    margin = error*sigma/(n**0.5)
    return (mean - margin, mean + margin)


def get_prop(p_hat, n, conf):
    z = 1 - conf/100
    error = get_z(z/2)
    margin = error*(p_hat*(1 - p_hat)/n)**0.5
    p_plus = round(p_hat + margin, ndigits=4)
    p_minus = round(p_hat - margin, ndigits=4)
    print(f"alpha: {round(z, ndigits=3)}\nCI: ({p_minus}, {p_plus})")


get_prop(
    p_hat=0.2,
    n=130,
    conf=95
)