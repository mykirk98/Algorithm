"""
문제
장난꾸러기 혁주는 어렸을 때부터 가위를 아주 잘 다루었다. 그래서 그는 색종이를 가위로 아무렇게나 자르는 것을 좋아한다. 혁주는 오늘 친구에게 원 모양의 색종이를 생일 선물로 받았다. 그가 색종이를 자르려는 순간, 어떤 친구가 "가위로 자를 때는 정확한 직선으로 자르면 더 깔끔해!"라고 했다. 그래서 혁주는 가위로 정확히 직선으로 두 번을 자르기로 했다. 예를 들어, 혁주는 아래와 같이 색종이를 자른다. (단, 한 번 자른 뒤, 색종이를 움직이지 않고 다시 한 번 자른다.)



이때, 영역 a와 b를 구분하는 선분의 길이를 pab, b와 c를 구분하는 선분의 길이를 pbc, c와 d를 구분하는 선분의 길이를 pcd라고 한다. pab, pbc, pcd의 값이 주어지면, 영역 d와 a를 구분하는 선분의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 pab, pbc, pcd의 값이 사이에 공백을 한 개씩 두고 차례대로 주어진다. 주어지는 모든 값들은 10,000 이하의 양의 정수이다.

출력
첫째 줄에 영역 d와 a를 구분하는 선분의 길이를 출력한다. 절대/상대 오차는 10-6 까지 허용한다.
"""

ab, bc, cd = map(int, input().split())

da = ab / bc * cd

print(da)