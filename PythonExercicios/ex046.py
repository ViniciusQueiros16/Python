from time import sleep
import emoji
print('\033[34m{:=^60}'.format('\033[31mFogos de Artifício\033[34m'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[31m:boom: :boom: :boom: :boom:', use_aliases=True))
