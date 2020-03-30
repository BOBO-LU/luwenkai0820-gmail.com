import re
test_string = '　　↪ 現場加送 條碼大作戰遊戲 STEAM 價值 $399'
pattern = '↪'
ans=re.findall(pattern,test_string)
if (ans == ['↪']):
    print(ans)
else:
    print('no', end= "")
    print(ans)