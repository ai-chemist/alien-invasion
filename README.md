## Python Crash Course - \[Alien Invasion with pygame] (12 to 14)

---

### Process

|    날짜     |         내역          |                    비고                     |                                  추가                                  |
|:---------:|:-------------------:|:-----------------------------------------:|:--------------------------------------------------------------------:|
|   08/14   | chapter 12 (pygame) |             main part of game             |                                                                      |
| 08/14 - 2 | chapter 12 (pygame) |         separate setting options          |                                                                      |
| 08/14 - 3 | chapter 12 (pygame) |               space_ship.py               |                images/spaceship.bmp 크기 조절 및 배경 지우기 필요                |
|   08/15   | chapter 12 (pygame) |                refactoring                |                    spaceship 이미지 수정, 기타 코드 메서드 화                     |
| 08/15 - 2 | chapter 12 (pygame) |               move_ method                |                      좌우 이동 메서드 작성 및 화면 내부 범위 설정                      |
|   08/16   | chapter 12 (pygame) | key event refactoring and fullscreen mode |                    **추후 창 모드, 전체 화면 변경 기능 추가할 것**                    |
| 08/16 - 2 | chapter 12 (pygame) |           add bullets (Sprite)            | bullet이 위로 올라갈 때 y좌표를 -= 연산하던 이유 (컴퓨터 그래픽스 분야에선 통상 좌표계와 다른 좌표 체계가 존재 |
| 08/16 - 3 | chapter 12 (pygame) |                refactoring                |                         bullet 관련 기능 메서드로 분리                         |
|   08/18   | chapter 13 (pygame) |                make alien                 |                        alien 부분 클래스 및 메서드 작성                         |
| 08/18 - 2 | chapter 13 (pygame) |      game over and players left life      |                        플래그 및 게임 상태 관리용 클래스 작성                        |
| 08/18 - 3 | chapter 14 (pygame) |    game start button and active status    |                  시작 버튼 및 버튼 클래스 작성 / 게임 활성 상태 관리 추가                  |
|   08/19   | chapter 14 (pygame) |           scoreboard and level            |                        레벨 증가, 점수, 최고 점수 등 출력                         |
|   08/19   | book part finished  |                                           |                  free refactoring and make new part                  |
---

#### 추가 사항
1. images/spaceship.bmp - Piskel 통해 직접 제작
2. 컴퓨터 그래픽스 좌표계 : 정확하게는 좌측 최상단의 좌표가 (0, 0) y축은 아래로 증가, x축은 우측으로 증가
3. images/alien.bmp - ~~이미지 새로 제작 필요~~ 제작 완료
---

#### 추후 할 것
- 외계인 부대 랜덤 위치에 나오게
- 플레이어 강화 아이템
- 레벨 및 점수판 디자인
- 플레이어 남은 목숨 -> 아이콘 새로 제작 후 적용
- 탄환 발사 시 사운드 출력
- 

---

*Based on the book by **"Eric Matthes"***