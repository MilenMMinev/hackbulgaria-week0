
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def simplify_fraction(fraction):
	d = gcd(fraction[0], fraction[1])
	print(d)
	return(fraction[0] // d, fraction[1] // d)


