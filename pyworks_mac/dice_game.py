import dice

num = input('4, 6, 8, 12, 20 중 어느 주사위로 시합하겠습니까? : ')  # input 함수로 값을 받아들임
num = int(num)                     # 문자열을 정수로 변환
my_dice = dice.Dice(num)           # 사용자용 주사위
cpu_dice = dice.Dice(num)          # 컴퓨터용 주사위

my_pip = my_dice.shoot()           # pip는 주사위의 눈을 의미함
cpu_pip = cpu_dice.shoot()         # 컴퓨터용 주사위의 눈

# 나온 눈을 화면에 출력, 숫자는 str 함수를 사용해 문자열로 변경
print('CPU : {} / 당신 : {}'.format(cpu_pip, my_pip))
# 상황에 따라 메시지를 변경함
if my_pip > cpu_pip:
    print('축하합니다. 당신의 승리입니다!')
elif my_pip < cpu_pip:
    print('안 됐네요! 당신의 패배입니다.')
else:
    print('비겼습니다')