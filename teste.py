import pynput
import pyautogui
import time
from pynput import mouse
from pynput import keyboard


running = True
mouse_event = mouse.Events()

def on_press(key):
	global running
	if key == keyboard.Key.f1:
		running = False
		print('fim')
		return False
def msg():
	mouse_event.start()


	for event in mouse_event:
		if running:
			if isinstance(event,mouse.Events.Click):
				if not event.pressed:
					pyautogui.typewrite('hello world\n',interval=0.009)
		else:
			time.sleep(1)
			print('teste1')
			return False


# with mouse.Events(vai_meu) as listener:
# 	if running:
# 		msg()
		
	# elif not listener.running:
		
	# 	time.sleep(2)
	# 	break
while 1:
	print("Escolha a opção desejada")
	print("1. Mensagem")
	option = int(input("Opção:"))
	if option == 1:

			running = True
			print("Pressione f1 para sair.")
			with keyboard.Listener(on_press=on_press) as listener:
				if running:
					msg()
					
				elif not listener.running:
					
					time.sleep(2)
					break