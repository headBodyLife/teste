#!/usr/bin/python3
import pyautogui
import time
from collections import deque
from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import *
import sys

##funciona
# time.sleep(4)
# pyautogui.moveTo(525,459)
# pyautogui.moveTo(525,354)
# pyautogui.click(button='left')
# time.sleep(1)
# pyautogui.moveTo(548,300)
# pyautogui.click(button='left')
# ###bbXlib.error.DisplayConnectionError: Can't connect to display ":1": b'No protocol specified\n'
# print(pyautogui.position())
# if pyautogui.keyUp("4"):
# 	print('ola mundo')
# if keyboard.is_pressed('4'):
# 	print('nem quero')


pause = True
running = True
xx_yy = None
xx_yy1= None
cont= 1
mouse_event = mouse.Events()

def mandar_msg_todos():
	get_click_position(5)
	lis = keyboard.Listener(on_press=on_press)
	lis.start()
	cont = 1
	time.sleep(2)
	# print(len(xx_yy)-1)
	msg = input("Qual mensagem:")

	while 1:
		# for i in range(3):

		for i in range(len(xx_yy)):
			
		# pyautogui.moveTo(x=315, y=747)
			print(i)
			pyautogui.moveTo(xx_yy[i])
			time.sleep(1)
			pyautogui.click(button='left')
			if i == len((xx_yy)-2): ##3
				print(i)
				pyautogui.moveTo(xx_yy[i])
				pyautogui.click(button='left')
				pyautogui.typewrite(f'{msg}\n', interval=1)
				time.sleep(1)
				
			
			
		time.sleep(10)	
		# pyautogui.click(button='left'n

		if not lis.running:
			print(xx_yy)
			break
	lis.stop()

def on_click(x, y, button, pressed):

    global xx_yy
    

    if pressed:
    	xx_yy.append(tuple([x,y]))



def get_click_position(clicks):
	global xx_yy
	xx_yy = deque(maxlen=clicks)
	with keyboard.Listener(on_press=on_press) as listener:
		lis = mouse.Listener(on_click=on_click)
		lis.start()
		listener.join()

		lis.stop()
	print('saindo do get_click')
		
def campainha(*args):
	
	print('passou')
	print(xx_yy)

	for click in range(clicks):
		print(xx_yy[0])
		# pyautogui.moveTo(xx_yy[click])
		pyautogui.click(xx_yy[click],button='left')
		pyautogui.PAUSE = 0.100
		time.sleep(0.100)
		if click == 2:
			time.sleep(1)
			pyautogui.click(xx_yy[click],button='left')
			time.sleep(2)
		# time.sleep(7.30) #quando nao for no navegador


def check_position():
	lis = Listener(on_press=on_press)
	lis.start()
	while running:
		print(pyautogui.position())
		position_x,position_y = pyautogui.position()
		if position_x == 0 and position_y == 0:
			print('merda')
# g


		time.sleep(1)
	lis.stop()


def on_press(key):
	global running
	if key == keyboard.Key.f1:
		running = False
		print('fim')
		return False

	
def dance(*args):
	pyautogui.moveTo(xx_yy[0]) # clica na posição
	time.sleep(1)
	pyautogui.click(button='left')
	pyautogui.moveTo(xx_yy[1])
	pyautogui.typewrite('_b\n', interval=0.100)
	time.sleep(1)
	pyautogui.click(button='left')
	# time.sleep(1.70)


def mandar_msg(msg,*args):
	mouse_listener = mouse.Listener(on_click=on_click)
	# print(dir(mouse_listener))

	# lis = Listener(on_press=on_press)
	# lis.start()
	global cont


	pyautogui.moveTo(xx_yy[0])
	pyautogui.click(button='left')
	#vc é menina na real?
	# pyautogui.press('enter')
	# pyautogui.typewrite(f'{cont}\n', interval=0.005)
	pyautogui.typewrite(f'{msg}\n', interval=0.005)

	time.sleep(3)
	pyautogui.moveTo(xx_yy[0])
	pyautogui.click(button='left')
	pyautogui.typewrite(f' ... \n', interval=0.005)
	# pyautogui.typewrite(f'{msg}\n', interval=0.005)
	time.sleep(4)
	cont+=1

def post_it():
	print('escolha o lugar')
	get_click_position(4)
	lis = keyboard.Listener(on_press=on_press)
	lis.start()
	cont = 1
	time.sleep(2)

	while 1:

		# pyautogui.moveTo(x=315, y=747)
		pyautogui.moveTo(xx_yy[0])
		pyautogui.click(button='left')
		# pyautogui.click(button='left'n

		pyautogui.moveTo(x=425, y=463)
		pyautogui.moveTo(xx_yy[1])

		pyautogui.click(button='left',clicks=2)
		# pyautogui.moveTo(x=796, y=327)
		pyautogui.moveTo(xx_yy[2])

		pyautogui.click(button='left')
		# pyautogui.moveTo(x=333, y=212)
		pyautogui.moveTo(xx_yy[3])

		time.sleep(0.3)
		pyautogui.click(button='left')
		if not lis.running:
			print(xx_yy)
			break
	lis.stop()
		# cont +=1

		# time.sleep(2)
		# print(pyautogui.position())

def zueira_never_end():
	def i_impar():
		for i in range(1,10,2):
			yield i,i+2
	def i_par():
		for i in range(2,10,2):
			yield i,i+2

	g = i_impar()
	h = i_par()

	for i,l in zip(g,h):
		pyautogui.typewrite(f':sign {i[0]}\n',interval=0.0500)
		pyautogui.typewrite(f':sign {i[1]}\n',interval=0.0500)
		pyautogui.typewrite(f':sign {l[0]}\n',interval=0.0500)
		pyautogui.typewrite(f':sign {l[1]}\n',interval=0.0500)

def andar_dormindo():
	mouse_event.start()
	# print(help(mouse.Events()))
	# time.sleep(0.009)
	# print(dir(Listener()))
	# mouse = Controller()
	# if mouse.press(Button.left):
	# 	print('ok')

	for event in mouse_event:
		if running:
			if isinstance(event,mouse.Events.Click):
				if not event.pressed:
					pyautogui.typewrite(':idle\n',interval=0.009)
		else:
			time.sleep(1)
			return False
			

def placas():
	# placas = [x for x in range(1,11,2)]
	placas = [x for x in range(1,11)]
	# for placa in range(1,len(placas)+1):
	for placa in placas:
		# pyautogui.typewrite(':sit\n', interval=0.100)
		pyautogui.typewrite(f':sign {placa}\n',interval=0.0500)
		# pyautogui.typewrite(f':sign {placas[-placa]}\n',interval=0.0500)
		# pyautogui.typewrite(':stand\n', interval=0.100)
	for placa in placas[1:]:
		# pyautogui.typewrite(':sit\n', interval=0.100)
		pyautogui.typewrite(f':sign {placas[-placa]}\n',interval=0.0500)
	# 	# pyautogui.typewrite(':stand\n', interval=0.100)

def all_action(*args):
	print(*args)
	actions = [':idle','_b',':sign 11','o/',':sit','_b',':sign 12','o/',':yyxxabxa',':stand',':sign 16','o/',':yyxxabxa']
	# actions = [':idle','_b',':sign 11','o/',':sit','_b',':sign 12','o/',':stand',':sign 16','o/']
	# pyautogui.typewrite(':kiss\n',interval=0.00000000000000000000000000000999)
	# pyautogui.typewrite(':sit\n',interval=0.0999)
	# pyautogui.typewrite('o/\n',interval=0.0999)
	# pyautogui.typewrite('_b\n',interval=0.0999)
	# pyautogui.typewrite('o/\n',interval=0.0999)
	# pyautogui.typewrite(':stand\n',interval=0.0999)
	# pyautogui.typewrite('_b\n',interval=0.0999)
	# pyautogui.typewrite(':sign 11\n',interval=0.0999)
	# pyautogui.typewrite('o/\n',interval=0.0999)
	# pyautogui.typewrite(':sit\n',interval=0.0999)
	# pyautogui.typewrite('_b\n',interval=0.0000000000000000000000000000000999)
	# pyautogui.typewrite('o/\n',interval=0.0000000000000000000000000000000999)
	# # pyautogui.typewrite(' \n',interval=0.0999)
	# # time.sleep(200)
	# pyautogui.typewrite(':stand\n',interval=0.0000000000000000000000000000000000001)
	pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)
		# 

	# pyautogui.typewrite('_b\n:idle\n:kiss\n',interval=0.00000000000000000000000000000000000001)
	# pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)

	# time.sleep(1)
	# # pyautogui.typewrite(':sit\n',interval=0.0999)
	pyautogui.typewrite('_b\n',interval=0.00000000000000000000000000000000000001)
	# pyautogui.typewrite(':stand\n',interval=0.0999)
	# time.sleep(1)
	# pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)

	# pyautogui.typewrite('_b\n',interval=0.00000000000000000000000000000000000001)
	# pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)

	# pyautogui.typewrite('_b\n',interval=0.00000000000000000000000000000000000001)
	# pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)

	# pyautogui.typewrite('_b\n',interval=0.00000000000000000000000000000000000001)
	# pyautogui.typewrite(':idle\n',interval=0.0000000000000000000000000000000000001)
	# pyautogui.typewrite(':stand\n',interval=0.0999)
	# pyautogui.typewrite(':stand\n',interval=0.0999)
	# for action in actions:
	# 	pyautogui.typewrite(f'{action}\n',interval=0.140)
	print('saindo do all_action')

# keyboard_listener = keyboard.Listener(on_press=on_press)	


if __name__ == "__main__":
	# with mouse.Listener(on_click=on_click) as listener:
	# 	print(listener.join())

	while 1:
		# post_it()
		print("O que deseja fazer:")
		print("1. Fazer várias coisas ao mesmo tempo.")
		print("2. Tocar campainha")
		print("3. Mandar Mensagem")
		print("4. Levantar Placas")
		print("5. Andar dormindo")
		print("6. Colocar post-it")
		print("7. Mandar mensagem para todos")
		ask = int(input("Opção:"))
		if ask == 1:
			print("Aperte no seu personagem e depois dançar")
			get_click_position(2)
			time.sleep(2)
			with keyboard.Listener(on_press=on_press) as listener:
				while 1:
					all_action()
					# time.sleep(1)
					# dance(xx_yy)
					# time.sleep(1.70)
					if not listener.running:
						break
		elif ask == 2:
			print("Toque a campainha")
			clicks = int(input("Quantos clicks\n"))
			get_click_position(clicks)
			with keyboard.Listener(on_press=on_press) as listener:
				while 1:
					campainha(xx_yy)
					# time.sleep(3)

					if not listener.running:
						break
		elif ask == 3:
			print("Escolha a  posição da caixa de texto:")
			get_click_position(1)
			msg = input("Qual mensagem:")
			with keyboard.Listener(on_press=on_press) as listener:

				while 1:
					# print(msg)
					mandar_msg(msg,xx_yy)
					# time.sleep(1)
					if not listener.running:
						break


		elif ask == 4:

			print("Levantando placas.")
			time.sleep(2)
			with keyboard.Listener(on_press=on_press) as listener:
				while 1:
					# zueira_never_end()
					placas()
					if not listener.running:
						time.sleep(1)
						break
		elif ask == 5:
			# mouse_listener.start()
			# keyboard_listener.start()
			running = True

			with keyboard.Listener(on_press=on_press) as listener:
				print(listener.is_alive())
				if running:
					andar_dormindo()
					print(listener.is_alive())
				elif not listener.running:
					print(listener.is_alive())
					time.sleep(2)
					listener.stop()
		elif ask ==  6:
			post_it()

		elif ask == 7:
			mandar_msg_todos()
