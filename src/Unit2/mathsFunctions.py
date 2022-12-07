#Functions which do not require import
a=-78
print(abs(a))
print(pow(a,3))
ls=[45,61,5456,122,2]
print(max(ls))
print(min(ls))
print(round(4566.4564,2))
print(round(456.7854656))

#Functions which require import
import math
print(math.floor(12.6))
print(math.ceil(12.6))
print(math.fmod(12,2))
print(math.fabs(-12.6))
print(math.factorial(5))
print(math.gcd(45,54))
print(math.trunc(12.69794646))
print(math.copysign(6.2,-5))
print(math.fsum({12.6,4}))
print(math.fsum([12.6,4]))
print(math.exp(1))
print(math.log(10,8))
print(math.log10(456))
print(math.pow(10,8))
print(math.sqrt(646))

#trigonometry function
print(math.sin(30))#now 30 is in radian
print(math.sin(math.radians(30)))#math.radians convert rad value to degree

print(math.hypot(2,4))
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)