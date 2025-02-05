metragem = float(input('digite uma metragem '))
km = metragem /1000
hm = metragem /100
dam = metragem /10
dm = metragem * 10
cm = metragem * 100
mm = metragem *1000

print(f'A sua metragem convertida em: \n km {km} \n hm {hm} \n dam {dam} \n dm {dm:.0f} \n cm {cm:.0f} \n mm {mm:.0f}')
