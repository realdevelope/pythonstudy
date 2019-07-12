'''
print("안녕하세요"[1:3])
print(len("hello"))
print("안녕"*3)
print(5//2, 5/2)    #정수나눗셈, 실수나눗셈
print(type(3.5))    #괄호안의 3.5 의 타입이 무엇인지 출력
print(2**4) # **= 승수!  2x2x2x2 라는 뜻
print()
print("환영합니다.")
a = input("정수>>")
print("덧셈:",int(a) + 100)
print()
input_a = float(input("첫번쨰 숫자>"))
input_b = float(input("두번째 숫자>"))
print()
print("덧셈 결과 :",input_a + input_b)
print("뺄셈 결과 :",input_a - input_b)
print("곱셈 결과 :",input_a * input_b)
print("나눗셈 결과 :",input_a / input_b)
print()


#input() 연습문제3
week = 7
day = 24
a = week * day
print()
print("7일은" + str(a) + "시간입니다")
print()


#input() 연습문제 4~7
height = input()
weight = float(input())#강제형변환(입력받은 후 정수형으로 변환)
a = height+weight
print("키 >",height)
print("몸무게 >",weight)
print("height * weight >",a)


#input() 응용문제 9~11
a = float(input())
b = float(intput())
c = (a**2 + b**2)**0.5
print("피타고라스의 정의 >",c)

#전처리기 impot
import datetime

now = datetime.datetime.now()   #

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

if now.hour <12 :
    print("현재 시간은 {}시로 오전입니다!".format(now.hour))

if now.hour >=12:
    print("현재 시간은 {}시로 오후입니다!".format(now.hour))

else:
    print("현재 시간은 {}시로 오전입니다!".format(now.hour))

if 3<=now.month<=5:
    print("이번달은 {}월로 봄입니다!".format(now.month))
elif 6<=now.month <=8:
    print("이번달은 {}월로 여름입니다!".format(now.month))
elif 9<=now.month <=11:
    print("이번달은 {}월로 가을입니다!".format(now.month))
else:
    print("이번달은 {}월로 겨울입니다!".format(now.month))


x = int(input("정수 >>"))


if 10 < x < 20:
    print("조건에 맞습니다")
else:
    print("조건에 맞지않습니다.")


#연습문제1
a = int(input())

if a%2==0
    print("'짝수'입니다")
else
    print("'홀수'입니다.")


#연습문제 3
a = int(input("점수 :"))

if 90 <= a > 100:
    print("'A'")
elif 80 <= a > 90:
    print("'B'")
elif 70 <= a > 80:
    print("'C'")
elif 60 <= a < 70:
    print("'D'")
else:
    print("'F'")

#삼항연산자
num1 = 1
num2 = 2
num3 = 3

print(num1 if num1 < 3 else 0)
print(num2 if num2> 3 else 'zero')
print('ok' if num3 == 3 else 0)

sum2 =((num1 if num1 > 0 else 0) + (num2 if num2 > 0 else  0) + (num3 if num3 >0 else 0))
print(sum2)

#리스트
list_a = [1,2,3]
list_b = [4,5,6]

print("# 리스트")
print("list_a = ",list_a)
print("list_b = ",list_b)
print()

print("# 리스트 기본연산자")
print("list_a + list_b =",list_a+list_b)
print("list_a *3 =",list_a * 3)
print()

print("# 길이구하기")
print("len(list_a",len(list_a))

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)

#리스트 삭제방법
list_a = [0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거하기")

##제거 방법[1]
del list_a[1]
print("del list_a[1]")

list_a.pop(2)
print("pop(2):",list_a)
print()

#여러개 한꺼번에 제거
list_b = [0,1,2,3,4,5,6]
del list_b[3:6]

#요소 한쪽 전부 제거
list_c =[0,1,2,3,4,5,6]
list_d =[0,1,2,3,4,5,6]

del list_c[:3]      #앞에가비어있으면 0부터 라는뜻 (0~3-1까지)
del list_d[3:]      #뒤에가 비어있으면 앞에 숫자부터 끝까지 (3부터 끝까지)

#리스트 값으로 제거

list_c = [1,2,1,2]
list_c.remove(2)    #동일한게 있으면 가장 앞쪽부터 제거

print("# 값으로 리스트의 요소 제거하기")
print("remove(2):",list_c)

#모두제거

list_c.clear()

print("$ 리스트의 요소 모두 제거하기")
print("clear.list_C:",list_c)

#포문과 리스트
array = [273, 32, 103, 57, 52]

for element in array:
    print(element)

#for문 리스트, 범위 조합 하기 : 몇번쨰 반복인지 확인
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))
    # print("%d 번째 : %d""%(i,arr[i]))  와같음

#반대로 출력하는법 = for i in (reverse(range(len(array))):

#연습문제1 1~10까지으 ㅣ합
a = 0

for i in range(1:11):
a = a+i
print("1~10번까지의 합 :",a)

#연습문제2 - 1~입력한 숫자까지의 합
a = int(input("입력 :"))

for i in range(1,a,]):
    print("1부터 a까지의 합 :",a+1)

#연습문제3 - 입력한 단의 구구단 출력
a = int(input("입력 :"))

for i in range(2,a,1):
    print("입력한 단의 구구단 :",a)

#반복문 내부에서만 사용하는 키워드
#in =

i = 0
while True:
    print("{}번쨰 반복문입니다".format(i))
    i = i +1

    input_text = input("종료하시겠습니까? (y):")
    if input_text in ["y","Y"]:
        print("반복을 종료하시겠습니까? (y):")
        break

#리스트의 함수

list_a = [52, 273, 103, 32, 57]

min_value = min(list_a)
max_value = max(list_a)

print("최소값 : ",min_value)
print("최대값 :",max_value)

#연습문제 4
hap,i = 0,0

for i in range (1,101,1):
    hap += i

    if hap >= 1000:
        break

print("1000이 넘게 하는 숫자 :",i)

#연습문제 5
sum = 0
for i in range(1,101,1):
    if i % 3 ==0:
       sum = sum +i
print("1부터 100까지의 합중 3의 배수는 제외한 합 :",5050 - sum)

#7월2일

ss = '파이썬짱!'

sslen = len(ss)
for i in range(0,sslen) :
    print(ss[i] + '$', end = '')

print()

#연습문제
ss = '파이썬은완전재미있어요'

sslen = len(ss)
for i in range(sslen):
    if i %2 ==0:
        print(ss[i] + '$', end = '')
    else:
        print(ss[i],end='')

#연습문제
instr, outStr = '',''
count, i = 0,0

inStr = input("문자열을 입력하세요 ;")
count = len(instr)

for i in range(0,count):
    outStr += instr[count - (i +1)]

print("내용을 거꾸로 출력 : %s"%outStr)

#연습문제

ss =input("입력 문자열 :")
print("출력 문자열 ==>", end = '')

if ss.startswith('(') == false :
    print("(",end = '')

print(ss,end = '')

if ss.endswith('(') == False :
    print(")",end ='')

#연습문제
    inStr = "한글 python 프로그래밍"
    outStr =""

    for i in range(0, len(inStr)):
        if inStr[i] != '' :
            outStr += inStr[i]


print("원래 문자열 ==>"+'['+inStr + ']')
print("공백 삭제 문자열 ==>"+ '[' + outStr + ']')

#연습문제
list1 =[]
list2 =[]
value = 1
for i in range(0,4) :
    for k in range  (0,5) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0,4) :
    for k in range(0,5) :
        print("%3d" % list2[i][k], end = "")

    print("")

#연습문제

dictionary = {}

print("요소 추가 이전 :", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print("요소 추가 이후 :",dictionary)


del dictionary["head"]
del dictionary["body"]

print("요소 제거 이후 :",dictionary)

#연습문제
foods = {"떡볶이":"오뎅", "짜장면":"단무지","라면":"김치" ,"피자":"피클","맥주":"땅콩","치킨":"치킨무","삼겹살":"상추"};

while True:
    myfood = input(str(list(foods.key())) +"중 좋아하는 음식은?")
    if myfood in foods :
        prine("<%s> 궁합 음식은 <%s> 입니다." % (myfoods, foods.get(myfood)))
    elif myfood == "끝" :
         break
    else:
            print("그런 음식이 없습니다. 확인해보세요.")

#연습문제 1
dictionary = {}

dictionary["국어"] = "80"
dictionary["영어"] = "75"
dictionary["수학"] = "55"

print("과목별 점수 :", dictionary)

a= (80 + 75 + 55)/3

print("평균 :",a)

#연습문제 2
ss = "881120 - 1068234"
ss.split()

#연습문제 3
pin="881120-1068234"
if pin[7] == 1:
    print("남자")
elif pin[7] ==2:
    print("여자")

#연습문제 4
ss = "a:b:c:d"

sslen = len(ss)
for i in range(0,sslen) :
    print(ss[i] + '#', end = '')

#연습문제 5
a = [1,3,5,4,2]
a.sort
a.reverse()
print("원래 : [1, 3, 5, 4, 2]")
print("거꾸로 출력 :",a)

#연습문제 6
ss =['Life','is','too','short']
a =" ".join(ss)
print(a)

#연습문제 7
t1 = (1, 2, 3)
t2 = (4,)
print(t1 + t2)

#연습문제 8
#연습문제 9
#연습문제 10
#연습문제 11
#연습문제 12
list =[]
s = 0

for i in range (0,5):
    a = int(input("정수 : "))
    list.append(a)
    s += list[i]

#컴프리 헨션구성
numList = [num for num in range(1,21) if num %3 == 0]
print(numList)

#함수기본 def<함수 이름>():
         # <문장>
#매개변수 def<함수이름>(<매개변수>,<매개변수>, ...):
        # <문장>
# 매개변수 자동 생성시 n = 2
#재귀함수

def factorial(n):

  if n ==1:
      return 1
  elif n  > 1:
      return n * factorial(n-1)

print("1! :",factorial(1))
print("2! :",factorial(2))
print("3! :",factorial(3))
print("4! :",factorial(4))
print("5! :",factorial(5))

# 5 * fact(4)
# 4 * fact (3)
# 3 * fact(2)
# 2 * fact(1)

#global 예약어 : a 변수를 전역변수로 지정
a=100

def GANGCH():

    global a

    print("",a + 1)
    print("",a + 1)

GANGCH()

#가변이랑 기변 같이 쓸떄 가변 먼저
#연습문제 1
def happyBirhday(a =",dear 홍길동!"):

    print("happy birthday! \n"*2,end='')
    print("happy birthday!",(a))
    print("happy birthday!")

happyBirhday()

#연습문제 2
def kangche(a=int(input("입력 :")),b=int(input("입력 :"))):
    c = a + b
    print("첫 번쨰 정수 :%d"%(a))
    print("두번쨰 정수 :%d"%(b))
    print("정수 10 + 20의 합=%d :"%(c))

kangche()

#연습문제 3
pi = 3.14
radius =5

def circleArea(radius):
    a = radius * radius * pi
    print("반지름이 5인 원의 넓이 : %d"%(a))

def circleRound(radius):
    a = 2*pi*radius
    print("반지름이 5인 원의 둘레 : %d"%(a))

circleArea(radius)
circleRound(radius)

#연습문제 4
a = 20
b = 10

def add(a,b):
    c = a + 10
    print("(20 + 10) = %d"%(c))
add(a,b)

#연습문제 6
def avg_numbers(*args):
    result =0
    for i in args :
        result += i
        return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5,))

#9 연습문제
#hap3 = lambda num1 = 10, num2 =20 : num1 + num2
#print(hap3 ())
#print(hap3(100, 200))

def myRange(start, end, hop =1):
    retVal = srart
    while retVal <= end :
        yield retVal # yield = 양보 ,처리하지않고 넘김
        retVal += hop
hop = 0
for i in myRange(1,5,2):
    hap += i

print(hap)

# map 아니더라도 람다형식은 많이 나옴

#7월 5일
import os

inFp = None
fName, inlist, instr = "",[],""

fName = "C:\data1.txt"

if os.path.exists(fName) :
    inFp = open(fName,"r")

    inlist = inFp.readline()
    for instr in inlist :
        print(instr, end ="")

        inFp.close()
else :
    print("%s 파일이 없습니다."%fName)

#한번에 읽어서 inList에 저장     => inList = inFp.readlines()

outFp = None
outstr = ""

outFp = open("C:\data1.txt","w")

while True :
    outFp = input("내용입력 :")
    if outstr != "" :
       outFp.writelines(outstr + "\n")
    else :
        break

outFp.close()
print("------정상적으로 파일에 씀-------)

#파일복사

inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt","w")

inList = iFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("----------파일이 정상적으로 복사되었음------")

#파일 저장
hp = 280
hit = ""
print("현재 체력은 %d입니다"%hp)
while hit != "save" and hp >0:
    hit = input("데미지를 몇 입었습니까 :")
    if hit == "save":
        f = open('save.txt', 'w')
        f.write(str(hp))
        f.close()
    else:
        hit = int(hit)
        hp = hp - hit
        print("체력이 %d 남았습니다."%hp)

#예외처리 & 파일 입출력

a,b = map(int,input("숫자 2개 입력 :").split())
print("a+b")

# labda 는 한줄 코딩만 가능
#여러줄일시에는 def
#  파이썬에서 세미콜론 쓸때는 명령어 ; 다음명령어 이렇게 쓸떄 세미콜론으로 구분


#6번
f1 = None
f2 = None
f3 = ""

f1 = open("C:\data4.txt","w")
f2 = f1.write("Life is too short")

f2 = open("C:\data4.txt","r")
f3 = f2.read()
print(f3)

f1.close()
f2.close()

#47/8(월)
#메소드 뒤에 self는 무조껀 들어간다 ex) def speed(self,value):
# class.변수 = 클래스 변수
#self,변수 = 인스턴스(객체) 변수
#인스턴스 변수 = 클래스의 맴버변수
#클래스 메소드는 앞에 @ 붙여주고 매개변수 자리에 (cls)를 적어준다
#count() : car count( = 10; - 클래스가 로딩되어질떄
# my car = car() - 메인안에서
#접근제어자중 private 하면 외부접근, 상속x  ex) self.__private    (언더바2개)
#             public 하면 외부접근, 상속0 ex) self.public
#set 설정자  -----  ex) def getAge (self) : self.__age
#get 접근자  -----  ex) def getAge (self) : return self.__age

class car :
    speed =0
    def upspeed(selfself,value):
        self.speed += value
        print("현재 속도(슈퍼클래스) : %d"%self.speed )

class Sedan(car):
    def upSpeed(self, value):
        self.speed += value
        if self.upspped >= 150 :
            self.speed = 150
        print("현재속도(서브클래스) : %d"% self.speed)

    def downSpeed(self, value):
        self.spped =+ value
class Truck(car) :
    pass
Sedan1, truck1 = None, None

truck1 = Truck()
Sedan1 = Sedan()
print("트럭 ==> ",end ="")
truck1.upspeed(200)
print("승용차 -->", end = "")
sedan1.upspeed(200)

#실습 1
class Book:
    title = ""
    author = ""

    def __init__(self, title="", author = ""):
        self.title = title
        self.author = author

    def show(self):
        print("제목 :",self.title)
        print("저자 :",self.author)

a = Book("파이썬","홍길동")
a.show()

#실습 2
class Rect:
    width = ""
    height = ""

    def __init__(self, width="1", height="1"):
        self.width = width
        self.height = height

    def area(self):
        return self.width * height

    def around(self):
        return 2*(self.width + height)

class Dog :
    def __init__(self, name="이쁜이", type ="푸들", age=1):
        self.__name = name
        self.__type = type
        self.__age = age

    def setName(self, name):
        self.__name = nmae

    def getName(self, name):
        return self.__name

a = Dog()
print(a.getName)

#상속
#def super() - 부모메서드에 접근 - 정적라이딩
#def ride(self) - 내꺼(자식)메서드에 접근

class A:
    def __init__(self):
        print("A.__init__()")
        self.message ="HELLO"
class B(A):
    def __init__(self):
        print("B.__init__()")
        super().__init__()
a = B()
a.message

#슈퍼 클래스에서 는 빈껍질의 메서드만 만들어놓고 내용은 pass로 채움
# 오버라이딩 =  자식이 부모를 상속받을떄 부모의 바디가 없는 경우에 바디를 입력
# __add__ = 매직매서드 = 생성자를 만들어주는!! 생성자는 아니고

class Line:
    length = 0
    def __init__(self,length):
        self.length = length
        print(self.length,'길이의 선이 생성되었습니다.')

    def __del__(self):
        print(self.length, '길이의 선이 삭제되었습니다.')
    def __repr__(self):
        return '선의길이 : ' + str(self.length)
    def __add__(self,other):
        return self.length + other.length
    def __lt__(self,other):
        return self.lenth < other.length
    def __eq__(selfself,other):
        return self.length == other.length

myLine1 =Line(100)
myLine2 = Line(200)

print(myLine1)
print('두 선의 길이 합 :',myLine1 + myLine2)
if myLine1 < myLine2 :
      print('선분 2가 더 기네요.')
elif myLine1 == myLine2 :
      print('두 선분이 같네요.')
else : print('모르겠네요')
del(myLine1)

#연습문제 4
class Rect:

    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def around(self):
        return 2*(self.width + self.height)

class vol(Rect) :
    def __init__(self, width =1, height =1, depth =1):
            Rect.__init__(self,width, height)
            self.depth =depth

a= vol()
print("사각형의 넓이 :",a.area())
print("사각형의 둘레 :",a.around())

#연습문제 5
class People :
    name = ""
    telephonenumber =""

    def __init__(self,name, telephonenumber):
        self.name = name
        self.telephonenumber = telephonenumber

    def name(self):
        return self.name

    def getname(self):
        print("")

    def settelephonenumber(self):
        print("")

    def gettelephonenumber(self):
        print("")

class Customer :
    consumernumber = ""
    ml = ""
#protected = 변경은 x

class Hello:
    t = "내가 상속해 줬어"
    def __init__(self):
        self._name ="hong"
        self.show = "결과"+ self.t
    @staticmethod
    def calc_satic(): return Hello()

    @classmethod
    def calc_class(cls): return cls()
    def prin_t(self): print(self.show)

class Hello2(Hello):
    t = "내가 상속 받았어"
    def setName(self,name):
        self._name =name

    def ss(self): print(self._name)

a = Hello2()
a._name = "kim"
a.ss()

a.setName("ym")
a.ss()

a_satic = Hello2.calc_satic()
a_class = Hello2.calc_class()

a_satic.prin_t()
a_class.prin_t()

#다중 상속

class Mother:
     def __init__(self):
        print('mother')

class Father:
    def __init__(self):
        print('father')

class Gentleman(Mother, Father):
    def __init__(self):
        super().__init__()
        Father.__init__(self)
        print('gentleman')

Gentleman()

#그래픽1
import turtle

t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("","이름을 입력하시오 :")
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")

for i in range(4):
    t.right(90)
    t.forward(100)


turtle.exitonclick()

#그래픽2

t= turtle.Turtle()
t.shape("turtle")

radisus = 100

t.circle(radisus)
t.forward(30)
t.circle(radisus)
t.forward(30)
t.circle(radisus)

turtle.exitonclick()

#그래픽 연습
import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = ["Yellow", "red", "blue", "green"]

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()


for i in range(4):
    t.fillcolor(color_list[0])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    if i != 3 : t.forward(50)

turtle.exitonclick()

#그래픽 연습2

import turtle
import random

screen = turtle.Screen()
image1 = "../../img/rabbit.gif"
image2 = "../../img/turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t1.shape(image1)
t1.pensize(5)
t1.penup()
t1.goto(-300,0)

t1 = turtle.Turtle()
t2.shape(image2)
t1.pensize(5)
t1.penup()
t1.goto(-300,-200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

turtle.exitonclick()

#그래픽 연습문제 1

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

turtle.exitonclick()

#그래픽 연습문제 2

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.width(10)

t.forward(100)
t.left(90)
t.forward(100)

turtle.exitonclick()

#그래픽 연습문제 3

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.color("blue")

t.forward(100)

turtle.exitonclick()

#그래픽 연습문제 4

import turtle

t = turtle.Turtle()
t.shape('square')

t.forward(100)

turtle.exitonclick()

#그래픽 연습문제 5

import turtle

t = turtle.Turtle()
t.shape("turtle")

range = 100

t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()

t.fillcolor("green")
t.forward(190)
t.begin_fill()
t.circle(100)
t.end_fill()

t.fillcolor("blue")
t.forward(190)
t.begin_fill()
t.circle(100)
t.end_fill()


t.left(90)
t.forward(50)
t.right(90)

t.fillcolor("yellow")
t.right(180)
t.forward(80)
t.begin_fill()
t.circle(100)
t.end_fill()

t.fillcolor("black")
t.forward(190)
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.exitonclick()

# bg = 배경색 / bd = 테두리 굵기 / front + 글씨체 / cursor = 마우스 올릴ㄹ떄 나타나는 커서모양
from tkinter import *
root = Tk()

label = Label(root, text = "Welcome, please input your name", bg ="beige",font ="arial")
label.pack()

entry = Entry(root, text = "input here", bd =5, cursor ="pirate")
entry.pack()

button = Button(root, text= "확인", fg ="red", cursor = "arrow",height = 10)
button.pack()

root.mainloop()

#예제소스

import tkinter

window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry ("640x400+100+100")
window.resizable(False, False)

b1 = tkinter.Button(window, text = "top")
b1_1 = tkinter.Button(window, text= "top-1")
b2 = tkinter.Button(window, text = "top-1")
b2_1 =tkinter.Button(window, text = "bottom-1")
b3 = tkinter.Button(window, text = "bottom-1")
b3_1 = tkinter.Button(window , text = "left-1")
b4 = tkinter.Button(window, text = "right")
b4_1 = tkinter.Button(window, text = "right-1")
b5 = tkinter.Button(window, text = "center", bg ="red")

b1.pack(side = "top")
b1_1.pack(side = "top", fill="x")
b2.pack(side = "bottom")
b2_1.pack(side = "bottom",anchor="e")
b3.pack(side = "left")
b3_1.pack(side ="left", fill = "y")
b1.pack(side = "top")
b1_1.pack(side = "top", fill ="x")
b2.pack(side = "bottom")
b2_1.pack(side = "bottom", anchor ="e")
b3.pack(side ="left")
b3_1.pack(side = "left", fill ="y")
b4.pack(side = "right")
b4_1.pack(side ="right", anchor ="s")
b5.pack(expand = True, fill = "both")



window.mainloop()

#라디오 버튼
from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc():

    if chk.get() ==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 켜졌어요.")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()

#라디오버튼2
from tkinter import*
window = Tk()

def myFunc():
    if var.get() ==1:
        label1. configure(text = "파이썬")
    elif var.get() ==2:
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")

var = IntVar()
rb1 =Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 =Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 =Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)
label1 = Label(window, text = "선택한 언어 : ", fg = "red")
rb1.pack(); rb2.pack(); rb3.pack()
label1.pack(); window.mainloop()

#grid
from tkinter import*

window = Tk()

l1 = Label(window, text ="화씨")
l2 = Label(window, text ="섭씨")
l1.grid(row =0, column=0)
l2.grid(row =1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row =0, column=1)
e2.grid(row =1, column=1)

b1 = Button(window, text ="화씨->섭씨")
b2 = Button(window, text ="섭씨->화씨")
b1.grid(row =2, column=0)
b2.grid(row =2, column=1, sticky ="W")

window.mainloop()


#place

from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0, y=0)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=20, y=20)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=40, y=40)

window.mainloop()

#배치관리자 pack

from tkinter import*
window = Tk()

btnList = [None]*3

for i in range(0,3) :
    btnList[i] = Button(window, text ="버튼" + str(i+1))

for btn in btnList :
    btn.pack(side = RIGHT)

    window.mainloop()

#event 매개변수를 활용한 마우스 이벤트 처리

from tkinter import *

def clickMouse(event) :
    txt = ""
    if event.num ==1:
        txt += "마우스 왼쪽 버튼이("
    elif event.num ==3:
        txt += "마우스 오른쪽 버튼이("
    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label1.configure(text = txt)

window =Tk()1
label1 = Label(window, text = "이곳이 바뀜")
window.bind("<Button>", clickMouse)
label1.pack(expand = 1, anchor = CENTER)

window.mainloop()

#계산기 만들기

from tkinter import *
window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5,command=process).grid(row=row_index, column=col_index)
    col_index += 1

    if col_index > 4:
        row_index += 1
        col_index = 0

    def click(key):
        if key == "=":
            result = eval(display.get())
            s = str(result)
            display.insert(END, "=" + s)
        elif key == "C":
            display.delete(0,int(display.get().__len__()))
        else:
            display.insert(END, key)

window.mainloop()
#7월 11일

from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
     img = PhotoImage(file ="C://Users/Workspace/untitled/venv/Scripts/rabbit.GIF")
     IbI = Label(image =img)
     IbI.image = img
     IbI.place(x=0, y=0)
root = Tk()
root.title('이미지 보기')
root.geometry('500x400+10+10')
myframe = MyFrame(root)

root.mainloop()

#메뉴와 대화상자

from tkinter import *
from tkinter import messagebox

def fun_open():
    messagebox.showinfo("메뉴선택","열기 메뉴 선택함")
def fun_exit():
    window.quit()
    window.destroy()

window =Tk()
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label ="파일", menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

window.mainloop()

#메뉴처리와 파일처리
from tkinter import *
from tkinter.filedialog import *

def func_open() :
    filname = askopenfilename(parent = window, filetypes =(("GIF파일","*.gif"),("모든파일","*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image =photo

def func_exit():
    window.quit()
    window.destroy()

window =Tk()
window.geometry("400x400")
window.title("명화 감상하기")
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand =1, anchor = CENTER)
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu =Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기 ", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료",command = func_exit)

window .mainloop()

#캔버스 위젯

from tkinter import *
mycolor ="blue"

def paint(event):
    x1, y1 = (event. x-1), (event.y+1)
    x2, y2 = (event.x - 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill = mycolor)

def change_color():
    global mycolor ; mycolor = "red"

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button = Button(window, text = "빨강색", command = change_color)
button.pack()

window.mainloop()'''

#실습 삼각학,사각형,오각형,육각형,팔각형 을 숫자로  입력 받고 -> 거북이로 숫자입력받은 도형 그리기

import turtle
from tkinter import *

def hoon():
    t = turtle.Turtle()
    t.shape("turtle")
    t.width(10)
    t.fillcolor("red")

    n  = 0
    n = int(ent1.get())

    for i in range(n) :
        t.forward(100)
        t.left(360//n)

r = Tk()

r.title("다각형 구하기")
#a = 0


lb1 = Label(r, text = "숫자입력")
ent1 = Entry()
ent1.insert(0, "0")
#ent1.bind("<Return>", sang)
#entry.pack()
btn = Button(r,text ="확인",command = hoon)
btn2 = Button(r,text ="종료",command = quit)

lb1.grid(row=0, column =0)
ent1.grid(row=0, column=1)
btn.grid(row=0, column =2)
btn2.grid(row=0, column =3)

#def sang(event):
#    label.config(text="결과="+str(eval(entry.get())))

#label=tkinter.Label(window)
#label.pack()

r.mainloop()

