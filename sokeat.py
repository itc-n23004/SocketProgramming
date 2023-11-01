import socket

def send_msg(sock, msg):
	total_sent_len = 0
	total_msg_len = len(msg)
	while total_sent_len < total_msg_len:
		sent_len = sock.send(msg[total_send_len:])
		if sent_len == 0:
		raise RuntimeError('socket connection broken')
		total_sent_len += sent_len

def recv_msg(sock, chunk_len=1024):
	while True:
		received_chunk = sock.recv(chunk_len)
		if len(received_chunk) == 0:
			break
#プログラムをストップする
		yield received_chunk

def main(ip_address,port):
    client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))
    request_text = 'GET / HTTP/1.0/r/n/r/n'
    request_bytes = request_text.encode('ASCII')
    send_msg(client_socket, request_bytes)
    received_bytes=b''.join(recv_msg(client_socket))
    received_text =received_bytes.decode('ASCII')
    print(received_text)
    client_socket.close()

if_name_=='_main_':
ip_address, port=input()
main(ip_address, int(port))
