import matplotlib.pyplot as plt

#선 스타일
""" #plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)") """

""" #plt.plot([2,3,6,7,10], [1,4,5,8,9], linestye="solid", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestye="dashed", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestye="solid", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestye="dashed", label="PData(km)") """

#solid 픽셀 크기-간격
""" #plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 2)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (10, 1)), label="PData(km)") """

#문자열 색 지정
""" #plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)") """

#선 두께-모양
""" #plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="butt", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=5, solid_capstyle="butt", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, dash_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="round", label="Value(m)" """

#마커 지정
""" #plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "go-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "co--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "kd-.", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)") """

#그래프 영역 채우기
""" xdata = [2, 3, 6, 7, 10]
x1data = [1, 3, 5, 7, 9]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]
plt.plot(xdata, ydata, label="PData(km)")
plt.plot(x1data, y1data, label="Value(m)")

plt.xlabel("x_data")
plt.ylabel("y_data")
plt.legend(ncol=1)
plt.axis([0, 10, 0, 10]) """

#세로 축 채우기
""" #plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], alpha=0.5)
#plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3) """

#가로 축 채우기
#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[:4], xdata[:4], alpha=0.3)

#두 선간 채우기
""" #plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], color="C2", alpha=0.3) """

#특정 범위 지정 채우기 x축/y축
""" #plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.1, 5.1], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 1.4], alpha=0.5) """


#배경 그리드 변경
""" plt.grid()
#plt.grid(axis="x")
#plt.grid(axis="y") """

#그리드 설정
""" #plt.grid(color="g", alpha=0.5, linestyle="-")
#plt.grid(color="g", alpha=0.5, linestyle=".")
plt.grid(color="g", alpha=0.5, linestyle="-.")
#plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
#plt.grid(axis="x", color="r", alpha=0.5, linestyle="-") """

#눈금 표시
""" #plt.xticks()
#plt.yticks()

#plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.xticks([1, 3, 5, 7, 9, 11])
plt.yticks([2, 4, 6, 8, 10, 12]) """

#라벨 지정
""" plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]) """

#눈금 안/밖 지정
""" plt.tick_params(axis="x", direction="in")
plt.tick_params(axis="y", direction="in") """

#막대그래프
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["C5", "lime", "#D09AED"]

#plt.bar(x_years, y_data)

#색 지정
""" #plt.bar(x_years, y_data, color="g")
#plt.bar(x_years, y_data, color="C7")
plt.bar(x_years, y_data, color="#57ADCC") """

#개별 색 지정
""" plt.bar(x_years, y_data, color=clr) """

#너비 설정
""" #plt.bar(x_years, y_data, color=clr, width=2)
#plt.bar(x_years, y_data, color=clr, width=0.5)
plt.bar(x_years, y_data, color=clr, width=0.1) """

#위치 선정
""" #plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", width=0.5) """

#막대 테두리 설정
""" #plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C6", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=2, width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="blue", linewidth=2, width=0.5) """

#축 지표 설정
""" plt.yticks([100, 200, 300, 400, 500, 600, 900]) """

#수평/가로 그래프
""" plt.barh(x_years, y_data) """

#옵션 나열
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()