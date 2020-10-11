print('\033[34m=\033[m'*12, '\033[31mPintando Paredes\033[m', '\033[34m=\033[m'*12)
l = float(input('\033[33mLargura da parede: '))
a = float(input('Altura da parede: \033[m'))
m = l * a
print('\033[4;35mSua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, m))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(m/2))