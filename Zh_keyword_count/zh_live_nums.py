import re

base_file = open('./交易库商标名称名录.txt', 'r+', encoding='utf-8')
base_set = set()
while True:
    lines = base_file.readlines(4096)
    for line in lines:
        word = re.compile('"(.*)"').findall(line)[0]
        base_set.add(word)
    if not lines:
        break

contrast_file = open('./知乎LIVE/live_nums.txt', 'r+', encoding='utf-8')
contrast_ls = []

while True:
    contrast_lines = contrast_file.readlines(4096)
    for line in contrast_lines:
        word = re.compile(r'(.*?)\t.*').findall(line)[0]
        contrast_ls.append(word)
    if not contrast_lines:
        break

result_file = open('./知乎LIVE/result_live_nums.txt', 'w+', encoding='utf-8')

for word in base_set:
    nums = contrast_ls.count(word)
    result_file.write(word + '\t' + str(nums) + '\n')

result_file.close()
print('finished!!!')