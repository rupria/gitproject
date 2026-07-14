---


-title:str    #접근제어자(상속불가)
-author:str   
-page:int    
   

Book(title=None:str, author=None:str, page=None:int)  
+setter & getter  #퍼블릭(상속 가능)
+toString():str 

변수 A 는 - 를 통해 A 값을 상속 불가로 함
        + B는 상속 가능 상태

그런데 변수 B 는 그럼 A 가 상속된 상태일 때
B 에서 B 만 상속받게 하려면 A에 - 를 써야하나?


---



animal = Animal('동물') # Animal을 animal로 바꿔서 부모 Animal 의 make_sound 를 가져옴 > 가져오고 다른 요소도 추가해도 괜찮나?
print(animal.make_sound())

dog = Dog('강아지')
print(dog.make_sound())

cat = Cat('고양이')
print(cat.make_sound())
