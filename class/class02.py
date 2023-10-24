# 객체 (object)

# 객체는 ㅣㅅㄹ제로 존재하는 모든 것들이다 
# 객체는 함수와 변수(데이터)를 함께 묶는 방법의 하나이다  
# 프로그래밍 용어로 파이썬은 객체지향적(object-oriented)라고 표현합니다. 이는 파이썬 내에서 객체를 사용하는 것이 가능하다는 뜻이다.

# 속성(ATTRIBUTE): 객체의 특징 또는 객체에 관해 알고 있는 사항, 숫자, 문자열 등과 같은 정보로 구성되어 있다. 즉 속성은 객체 안에 포함된 변수(데이처)이다.

# method: 파이썬에서 행동 또는 객체에 대해, 객체를 통해 할 수 있는것 , 어떤 일을 하기 위해 호출(call)할 수 있는 코드 덩어리이다. 즉 메서드는 객체 안에 포함된 함수 

# 객체 = 속성(변수) + 메소드(함수): 그러므로 객체를 통해 할수 있는것, 어떤 일을 하기 위해 호출(call)할 수 있는 코드 덩어리이다

# 객체 지향 프로그래밍(Object-Oriented Programming OOP)은 컴퓨터 프로그래임의 패러다임 중 하나입니다. 
# 객체 지향 프로그래밍은 컴퓨터프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.

# 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다. 또한 프로그래밍은 프로그램을 더 배우기 쉽게 하고 소프트웨워 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있다. 그러나 지나친 프로그램의 객체화 경향은 실제 세계의 모습을 그대로 반영하지 못한다는 비판을 받기도 한다.

# <기본 구성 요소>

# 클래스(Class) - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user defined data type)이라고 할 수 있다
# 객체(Object) - 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있습니다. 
# 메소드(Method), 메시지(Message) - 클래스로부터 생성된 객체를 사용하는 방법으로서 객체에 명령을 내리는 메시지라 할 수 있다.

# 객체와 클래스 
# 하나의 붕어빵 틀에 반죽과 여러 가지 앙금을 넣어 가공하면 팥은 넣은 팥붕 슈크림을 넣은 슈붕 붕어빵을 넣은 붕붕을 만들 수 있습니다. 
# 이 붕어빵처럼 모양이나 개념으로 존재하는 것을 객체라고 하고 하고 붕어빵 틀처럼 객체를 만들때 사용하는 것을 클래스라고 한다 

# step 1 : class를 만들어 설계하기 

# 클래스 구성요소: 클래스 이름, 클래스 메서드(함수)
# step 1: class에 클래스 이름 지정 보통 대문자로 시작 
# def 메서드 작성 메서드의 첫 번째 매개변수는 보통 self를 지정 

class Dog:
    def bark(self):
        print("멍")

# 인스턴스
myDog = Dog()

# 클래스 Dod헤 myDog(객체)이라는 이름을 할당하였는데 이 myDog이 Dog의 인스턴스가 된다 


myDog.name = "백구"
myDog.color = "white"
myDog.size = "Big"

# 객체의 속성 출력 
print(myDog.name)
print(myDog.color)
print(myDog.size)
print()

#메서드 사용하기 
myDog.bark()


class Lamp:
    def onOff(self):
        if self.light == "on":
            self.light = "off"

myLamp = Lamp()
myLamp.color = "orange"
myLamp.size = "small"           
myLamp.light = "on"

print("i just created a lamp.")
print("my lamp is",myLamp.color)
print('My lamp is ',myLamp.size)
print('My lamp is ',myLamp.light)
print("Now im going to turn off my lamp")
print()
myLamp.onOff()

print("Now my lamp is ",myLamp.light)

# self는 인스터스 자기 자신을 의미한다. 보통 메서드의 첫 번째 매개변수는 self로 지정해야 한다.
