import decimal
from decimal import Decimal

print(type(decimal.localcontext()), type(decimal.getcontext()))

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))
    print(round(y, 1))
print(round(x, 1))
print(round(y, 1))

print(format(Decimal("0.10"), ".100 f"))
