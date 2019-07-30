from scipy.special import erfinv

SQ2 = 2.0**0.5


def get_z(alpha):
    y = 2*(1-alpha) - 1
    return SQ2*erfinv(y)


def get_conf(mean, sigma, n, conf):
    z = 1 - conf/100
    error = get_z(z/2)
    margin = error*sigma/(n**0.5)
    return (mean-margin, mean+margin)


