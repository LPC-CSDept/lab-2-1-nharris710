def main():
   ##################################################
   # Comlete your code here
   ##################################################

    original_price = int(input())
    rate = int(input())
    discount_amount = (rate/100 * original_price)
    print('Regular Price: :', original_price)
    print('discount_amount: ', rate * original_price)
    print('The final price:', original_price - discount_amount)


if __name__ == '__main__':
    main()
