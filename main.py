import re
import pandas as pd
import itertools
import numpy as np
import argparseInput as arg
import os

path_infile = arg.commandline()
f = open(path_infile, mode="r", encoding="utf-8")
line = f.readline()
count = 1
filename, ext = os.path.splitext(path_infile)
path_outfile = filename+"s"+ext
g = open(path_outfile, mode="w", encoding="utf-8")


regex_response = r"応答：.+"
pattern_response = re.compile(regex_response)
regex_factor = r"因子：.+"
pattern_factor = re.compile(regex_factor)
regex_level = r"水準：.+"
pattern_level = re.compile(regex_level)
regex_repeat = r"繰り返し数：.+"
pattern_repeat = re.compile(regex_repeat)
regex_table = "\|"
pattern_table = re.compile(regex_table)

while line:
    m1 = pattern_response.match(line)
    if m1:
        response = m1.group()[3:]
        # file ope.
        g.write(line)
        line = f.readline()
        count+=1
        m2 = pattern_factor.match(line)
        if m2:
            factor = m2.group()[3:]
            factor = factor.split("/")
            factor_num = len(factor)
            # file ope.
            g.write(line)
            line = f.readline()
            count+=1
            m3 = pattern_level.match(line)
            if m3:
                level = m3.group()[3:]
                level = level.split("/")
                levels_list = []
                for i in range(factor_num):
                    levels = level[i].split(",")
                    levels_list.append(levels)
                plan = list(itertools.product(*levels_list))
                no = np.arange(start=1, stop=len(plan)+1).tolist()
                df = pd.DataFrame(plan, index=no, columns=factor)
                print(df) # plan
                # file ope.
                g.write(line)
                line = f.readline()
                count+=1
                m4 = pattern_repeat.match(line)
                if m4:
                    repeat = m4.group()[6:]
                    # 上書き設定を追加
                    g.write(line)
                    line = f.readline()
                    count+=1
                    g.write(line)
                    line = f.readline()
                    count+=1
                    m5 = pattern_table.match(line)
                    if m5:
                        g.write(line)
                        line = f.readline()
                        count += 1
                    else:
                        # 書き込みを入れる
                        g.write(df.to_markdown())
                        g.write("\n"*2)
                        # 読み込みを書き込む
                        g.write(line)
                        line=f.readline()
                        count += 1
    else:
        g.write(line)
        line = f.readline()
        count+=1
f.close()
g.close()

