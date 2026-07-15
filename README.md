---



## 이슈 리포트 템플릿 작성
이슈 리포트 템플릿 작성되었습니다.
깃허브의 이슈는 MD를 통해서 내용 수정과 커스텀이 가능한 상태로, 관련 내역에 대해 수정가능합니다.
[.github/ISSUE_TEMPLATE](https://github.com/rupria/gitproject/tree/main/.github/ISSUE_TEMPLATE)
위 폴더 내
'-적용-영역--이슈를-한줄로-표현-가능하게-작성_튜토리얼용.md' 확인 부탁드립니다.
추가 문의사항은 DM 주시면 아는 선에서 답변드리겠습니다.
피드백 및 개선 환영합니다.
비게임하신분들 많이 도와주세용

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
