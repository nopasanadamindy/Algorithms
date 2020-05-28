import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Python Player'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 5
HOLES = [ [-1, -1], [127, -1], [255, -1], [-1, 128], [127, 128], [255, 128] ]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + 
        str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%f/%f' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData, cnt):
    angle = 104.8
    power = 100
    ball = gameData.balls
    white_ball = ball[0]
    ######################################################################################
    # 주석을 지우고, 이 곳에 주어진 정보를 바탕으로 게임 로직을 구현하여 자동으로 플레이할 수 있도록 구현합니다.
    # 필요한 결괏값은 방향(angle)과 세기(power)로 두 변수의 값이 결정되도록 만들어야 합니다.
    target = ball[1]
    if ball[1] in HOLES:
        if ball[2] in HOLES and ball[3] in HOLES:
            target = ball[4]
        elif ball[2] in HOLES:
            target = ball[3]
        else:
            target = ball[2]

    if white_ball[0] - target[0] == 0 or white_ball[1] - target[1] == 0:
        angle = 91.5
        power = 100  
    else:
        xdelta = target[0] - white_ball[0]
        ydelta = target[1] - white_ball[1] 
        angle = math.atan(ydelta/xdelta) * 180 / math.pi
        if xdelta > 0 and ydelta > 0 :
            power = 90
            if cnt == 2:
                power = 100
                angle = 90-angle + 1.5
            else:
                if cnt == 3:
                    power = 60
            angle = 90-angle

        elif xdelta > 0 and ydelta < 0 :
            power = 80
            angle = 90 - angle     
        elif xdelta < 0 and ydelta < 0 :
            power = 80
            angle = 270 - angle
        elif xdelta < 0 and ydelta > 0 :
            power = 80
            angle = 270 - angle

    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    cnt = 1
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData,cnt)
        cnt = cnt + 1        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
