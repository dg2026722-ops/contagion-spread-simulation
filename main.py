Web VPython 3.2

import random #아까 불러온 랜덤 모음집에서가져오라는뜻나중에위치정할때사용할거야

balls = []#15개가있어야해리스트에저장해놓자

for i in range(15):#공 15개를 하나하나 코드로 짜면 힘드니까, 컴퓨터한테 공 만드는 코드를 15번 반복 실행하라고!
    # 위치를 -4에서 4 사이로 랜덤하게 지정해놓은거야지정해놓지않으면어디로튈지모름
    rx = random.uniform(-4, 4) #randomx좌표
    ry = random.uniform(-4, 4)
    rz = random.uniform(-4, 4)
    
    # 공 생성 (처음엔 모두 흰색)
    ball = sphere(pos=vector(rx, ry, rz), radius=0.4, color=color.white)
    
    # 컴퓨터가 첫 번째(0번) 공을 만들 때만 빨간색(감염자)으로 지정!
    if i == 0:
        ball.color = color.red
    
    # 속도 지정 (처음 정해진 방향으로만 똑바로 가게 만듦)
    ball.vx = random.uniform(-1, 1)
    ball.vy = random.uniform(-1, 1)
    ball.vz = random.uniform(-1, 1)
    
    balls.append(ball)#추가하다는뜻이야방금만든공들을리스트balls에넣어야해


# 3. 무한 반복하며 움직이기
while True:
    rate(30) # 1초에 30번 화면 움직이기
    
    for ball in balls:
        # [이동] 위치 = 원래 위치 + 속도 
        ball.pos.x += ball.vx * 0.05
        ball.pos.y += ball.vy * 0.05
        ball.pos.z += ball.vz * 0.05
        
        # [벽 충돌 중심에서 거리가 5를 벗어나면 속도의 부호를 반대로 바꿔서 튕겨냄
        if abs(ball.pos.x) > 5: #abs는절대값이라는 의미 따라서거리를나타내는거야
            ball.vx = -ball.vx #그래서 절대값이5보다크면벽에부딪혔다는뜻이야 그래서마이너스를붙혀서다시돌아가게만들어야해
            
        if abs(ball.pos.y) > 5:
            ball.vy = -ball.vy #공간은가로세로옆으로이루어져있어서vx,vy,vz모두설정해줘야해
            
        if abs(ball.pos.z) > 5:
            ball.vz = -ball.vz
            
    for white_ball in balls: #하얀색공을이용하자
       
        if white_ball.color == color.white: #하얀공색을확인해보자정말하얀색인지아닌지
            
            for red_ball in balls: #빨간공이정말빨간공이라면!
                if red_ball.color == color.red: 
                    
                    distance = mag(white_ball.pos - red_ball.pos) #하얀색좌표에서빨간색좌푤를빼면거리가나와 #mag는거리를바로계산해주는거야 #distance에결과값을저장해두기
                    
                    #거리가 1보다 작으면(부딪히면) 빨간색으로 변경!
                    if distance <1:
                        white_ball.color = color.red
                        
        
