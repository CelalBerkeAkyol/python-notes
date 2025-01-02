
#{<expression> for x in <sequence> if <condition>}
	# Liste comprehension ile benzer şekilde çalışır, ancak tekrar eden öğeleri otomatik olarak çıkarır.
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)