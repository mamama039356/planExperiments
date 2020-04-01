import re
import pandas as pd

f = open("./untitled.txt", encoding="utf-8")
line = f.readline()

regex_response = r"応答：.+"
pattern_response = re.compile(regex_response)
regex_factor = r"因子：.+"
pattern_factor = re.compile(regex_factor)
regex_level = r"水準：.+"
pattern_level = re.compile(regex_level)
regex_repeat = r"繰り返し数：.+"
pattern_repeat = re.compile(regex_repeat)

while line:
#     print(line)
    factor_dict = {}
    m1 = pattern_response.match(line)
    if m1:
        response = m1.group()[3:]
        print(response)
        line = f.readline()
        m2 = pattern_factor.match(line)
        if m2:
            factor = m2.group()[3:]
            factor = factor.split("/")
            print(factor)
            factor_num = len(factor)
            line = f.readline()
            m3 = pattern_level.match(line)
            if m3:
                level = m3.group()[3:]
                level = level.split("/")
                print(level)
                level_nums = []
                level_crossover = 1
                for i in range(factor_num):
                    levels = level[i].split(",") # ここに繰り返しをかける
                    factor_dict[factor[i]] = pd.Series(levels)
                    level_nums.append(len(levels))
                    level_crossover *= level_nums[i]
                    print(level_crossover)
                for j, k in enumerate(level_nums):
                    level_nums[j] = level_crossover/k
                print(factor_dict)
                print(level_nums)
                # markdown仕様
                # 繰り返し処理
                df = pd.DataFrame(factor_dict)
                print(df)
                
                line = f.readline()
                m4 = pattern_repeat.match(line)
                if m4:
                    repeat = m4.group()[6:]
                    print(repeat)    
    line = f.readline()
f.close()        
#     factor = 
#     level = 
#     repeat =
