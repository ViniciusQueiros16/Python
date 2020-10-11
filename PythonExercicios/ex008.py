print('\033[35m========Medidadas de Distâncias========\033[m')
d = float(input('\033[4;34mUma distânciaem metros:\033[m'))
print('\033[4;31mA medida de {}m corresponde a\033[m \n\033[1;33m{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(d, (d/1000), (d/100), (d/10), (d*10), (d*100), (d*1000)))
