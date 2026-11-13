import random

def number_guessing_game():
    # تولید یک عدد تصادفی بین ۱ تا ۱۰۰
    secret_number = random.randint(1, 100)
    max_attempts = 10
    
    print("--- به بازی حدس عدد خوش آمدید! ---")
    print(f"من یک عدد بین ۱ تا ۱۰۰ در نظر گرفته‌ام. شما {max_attempts} بار فرصت دارید آن را حدس بزنید.\n")
    
    for attempt in range(1, max_attempts + 1):
        try:
            # دریافت حدس کاربر
            guess = int(input(f"تلاش شماره {attempt}: عدد خود را وارد کنید: "))
        except ValueError:
            print("خطا: لطفاً فقط عدد صحیح وارد کنید.")
            continue
            
        # بررسی حدس کاربر
        if guess == secret_number:
            print(f"\n تبریک! شما برنده شدید! عدد درست {secret_number} بود و آن را در تلاش {attempt}م حدس زدید.")
            return
        elif guess < secret_number:
            print("کم است! عدد مورد نظر **بزرگ‌تر** است. ⬆️")
        else:
            print("زیاد است! عدد مورد نظر **کوچک‌تر** است. ⬇️")
            
        print(f"فرصت‌های باقیمانده: {max_attempts - attempt}\n")
            
    # اگر بعد از ۱۰ تلاش کاربر درست حدس نزده باشد
    print(f"\n❌ متأسفانه فرصت‌های شما به پایان رسید و باختید! عدد صحیح همان {secret_number} بود.")

# اجرای بازی
if __name__ == "__main__":
    number_guessing_game()