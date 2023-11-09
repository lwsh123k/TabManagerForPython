import socketio

# 创建Socket.IO客户端
sio = socketio.Client()

# 连接到服务器
sio.connect('http://localhost:3000')

# 定义消息处理函数
@sio.on('open a new tab')
def open_new_tab(data):
    print(data)

# 等待连接并监听消息
sio.wait()