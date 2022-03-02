IP地址无效化：  
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。  
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。   

输入：address = "1.1.1.1"  
输出："1[.]1[.]1[.]1"

```python3
class Solution1:
    def defangIpaddr(self, address):
        s = []
        for i in range(len(address)):
            if address[i] != '.':
                s.append(address[i])
            else:
                s.append('[.]')
        return "".join(s)
```