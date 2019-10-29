import socketio
import time

sio = socketio.Client()

ip = input('IP주소를 입력해주세요.')
port = input('PORT를 입력해주세요.')

ip = '115.145.114.112'
port = '5060'

sio.connect(f'http://{ip}:{port}')
sio.emit('submit', {
    'name' : '윤용선',
    'score' : {
    'a' : True,
    'b' : False
    }})
print('submission completed')
time.sleep(3)
sio.disconnect()
