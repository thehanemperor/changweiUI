result = [['慈善晚会', '2020央视跨年晚会直播', '中秋晚会2019', '春晚', '2020中央跨年晚会', '酒宴晚会', '2020各大卫视跨年', 'bilibili跨年晚会', '晚会拍摄']]
re2 = ['慈善晚会', '2020央视跨年晚会直播', '中秋晚会2019', '春晚', '2020中央跨年晚会', '酒宴晚会', '2020各大卫视跨年', 'bilibili跨年晚会', '晚会拍摄']

print('ret2','\n'.join(re2))
print('\n'.join(str(j)  for i in result for j in i))
print(','.join(str(item) for innerlist in result for item in innerlist))