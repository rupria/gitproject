---
name: Custom issue template
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

## 요약 :
> git 프로젝트 변경 시 신규 계정의 git push 불가 현상<br>
 > 기존 : rupria.sk / rupria.sk@gmail.com
 >  변경 :  rupria.jjn / rupria.jjn@gmai

## 설명

    [현재 상황]
 rupria.jjn / rupria.jjn@gmail 를 계정 사용자로 등록 시 push 기능이 작동하지 않는 현상입니다.

    [기대 상황]
상기 계정 사용 시에도 git 기능이 정상적으로 작동해야 합니다.

    [재현 방법]
    1.  git bash 를 통해 해당 폴더 내 git 이동
    2.  git 계정 이름, 사용자 등록 
         git config -- global user.name rupria.jjb
         git config -- global user.email rurpa.jjb@gmail.com
    3. 아래 코드를 통해 유저 등록 확인 
          git config --global --unset user.name
          git config --global--unset user.email
    4. 계정 등록 정상 확인.
    5. git commit 후 push 진행
    6. 보안관련 오류 메시지 노출 및 push 불가 확인
