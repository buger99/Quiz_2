환율표 = {"달러":1320, "엔":950, "위안":182}

print(환율표)

a = [13, 200, 13]

b = 환율표["달러"] * a[0] + 환율표["엔"] * a[1] + 환율표["위안"] * a[2]
print(b)

print("철수가 가지고 있는 돈의 원화 가치는", b, "원 입니다.")
