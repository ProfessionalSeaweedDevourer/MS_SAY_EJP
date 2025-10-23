# 50,000 이내의 물품 가격에 대해 입력한 금액을 냈을 때, 거스름돈을 화폐권 단위로 출력.
# 예: 47200에 대해 50000을 낼 때, 1000원 2개, 500원 1개, 100원 3개

price = int(input("구매하고자 하는 물품 가격: "))
amount_paid = int(input("낸 돈: "))

# '낸 돈'이 '물품 가격'보다 적은 경우
while amount_paid < price:
    print("물품 가격(%d원)보다 돈(%d원)을 적게 낼 수 없습니다." % (price, amount_paid))

    is_price_wrong = input("물품 가격을 다시 입력하겠습니까? (Y/N): ").upper()

    if is_price_wrong == "Y":
        price = int(input("구매하고자 하는 물품 가격: "))
        amount_paid = int(input("낸 돈을 다시 입력하십시오: "))
        
    elif is_price_wrong == "N":
        amount_paid = int(input("낸 돈을 다시 입력하십시오: "))
        
    else:
        print("Y 또는 N으로만 응답해 주십시오.")

left_amount = amount_paid - price
print("거스름돈 총액: %d" % left_amount)

count = left_amount // 50000
print("5만원: %d" % count)
left_amount -= (count * 50000)

count = left_amount // 10000
print("만원: %d" % count)
left_amount -= (count * 10000)

count = left_amount // 5000
print("5천원: %d" % count)
left_amount -= (count * 5000)

count = left_amount // 1000
print("천원: %d" % count)
left_amount -= (count * 1000)

count = left_amount // 500
print("500원: %d" % count)
left_amount -= (count * 500)

count = left_amount // 100
print("100원: %d" % count)
left_amount -= (count * 100)

count = left_amount // 50
print("50원: %d" % count)
left_amount -= (count * 50)

count = left_amount // 10
print("10원: %d" % count)
left_amount -= (count * 10)

print("잔액: %d" % left_amount)

# # 모범 답안
# def calculate_change(amount):
#     currency_units = [
#         (50000, "5만원"), (10000, "만원"), (5000, "5천원"), (1000, "천원"),
#         (500, "500원"), (100, "100원"), (50, "50원"), (10, "10원")
#     ]
#     change_details = {}

#     for unit, name in currency_units:
#         count = amount // unit

#         if count > 0:
#             change_details[name] = count

#         amount %= unit

#     return change_details, amount

# price = int(input("구매하고자 하는 물품 가격: "))
# amount_paid = int(input("낸 돈: "))

# while amount_paid < price:
#     print(f"\n 물품 가격({price}원)보다 돈({amount_paid}원)을 적게 낼 수 없습니다.")

#     is_price_wrong = input("물품 가격을 다시 입력하겠습니까? (Y/N): ").upper()

#     if is_price_wrong == "Y":
#         price = int(input("구매하고자 하는 물품 가격: "))
#         amount_paid = int(input("낸 돈을 다시 입력하십시오: "))

#     elif is_price_wrong == "N":
#         amount_paid = int(input("낸 돈을 다시 입력하십시오: "))

#     else:
#         print("⚠ Y 또는 N으로만 응답해 주십시오.")

# left_amount = amount_paid - price

# print(f"\n 지불이 확인되었습니다. 거스름돈 총액: {left_amount}원")

# change_details, final_remaining = calculate_change(left_amount)

# print("\n--- 거스름돈 내역 ---")
# if left_amount == 0:
#     print("거스름돈이 없습니다.")
# else:
#     for name, count in change_details.items():
#         print(f"{name}: {count}개")

# print(f"잔액: {final_remaining} (0이면 정상)")