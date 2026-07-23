---
name: dbIssue
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

name: Database 오류
description: DB 연결, SQL 실행, 테이블 및 데이터 관련 오류를 등록합니다.
title: "[DB] "
labels:
  - bug
  - database
body:
  - type: dropdown
    id: error-type
    attributes:
      label: 오류 유형
      options:
        - DB 연결 오류
        - 데이터베이스 선택 오류
        - SQL 문법 오류
        - 테이블 생성 오류
        - 제약조건 오류
        - 데이터 입력 오류
        - 기타
    validations:
      required: true

  - type: textarea
    id: summary
    attributes:
      label: 오류 개요
      description: 발생한 문제를 간단히 설명해 주세요.
      placeholder: MySQL에서 myxedb 데이터베이스를 찾지 못해 SQL 실행이 실패했습니다.
    validations:
      required: true

  - type: textarea
    id: environment
    attributes:
      label: 실행 환경
      value: |
        - OS:
        - DBMS 및 버전:
        - DB 접속 도구:
        - Host:
        - Port:
        - Database:
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: 재현 절차
      placeholder: |
        1. DBeaver를 실행합니다.
        2. MySQL 연결을 선택합니다.
        3. SQL 파일을 실행합니다.
        4. 오류가 발생합니다.
    validations:
      required: true

  - type: textarea
    id: error-message
    attributes:
      label: 오류 메시지
      render: shell
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: 기대 결과
    validations:
      required: true

  - type: textarea
    id: actual
    attributes:
      label: 실제 결과
    validations:
      required: true

  - type: textarea
    id: sql
    attributes:
      label: 관련 SQL
      render: sql

  - type: textarea
    id: cause
    attributes:
      label: 추정 원인 또는 확인된 원인

  - type: textarea
    id: resolution
    attributes:
      label: 해결 방법 및 검증 결과

  - type: checkboxes
    id: security
    attributes:
      label: 첨부 정보 확인
      options:
        - label: 비밀번호, 접속 토큰 등 민감한 정보가 포함되지 않았습니다.
          required: true
