from sklearn import neighbors

features = [[80,85,88,78],[95,94,93,92],[90,90,90,90],[80,80,80,80]]
lables = [0,1,1,0]

clf=neighbors.KNeighborsClassifier(3)
clf=clf.fit(features, lables)

while True:
    result = int(input("道法："))
    result1 = int(input("生物："))
    result2 = int(input("地理："))
    result3 = int(input("历史："))
    print(clf.predict([[result, result1, result2, result3]]))
    print('\n')
    result4 = int(input("(1为退出，0为继续)是否退出："))
    print('\n')
    if result4 == 1:
        break
    else:
        continue