def  series_Fibonachi(numberelement):
	i=2
	a1=1
	a2=2
	a3=0
	while i<numberelement:
		a3=a1+a2
		a1=a2
		a2=a3
		i=i+1
	return a3

def num_fibonachi(number):
	sum_num=2
	a1=1
	a2=2
	a3=0
	while a3<number:
		a3=a1+a2
		a1=a2
		a2=a3
		if a3%2==0:
			sum_num+=a3

	return sum_num

#print(num_fibonachi(4000000))
#def Largest_prime_factor(number):