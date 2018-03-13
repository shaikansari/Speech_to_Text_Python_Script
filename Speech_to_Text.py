from speech_recognition import *

'''
Recognizer() -- class used to recognize your voice:
	We used two methods
	listen() --listen voice
	recognize_google()--process our voice in google API

Microphone() -- class used to capture our voice through system mic
'''

running =True

def speech_to_text():

	global running
	r = Recognizer()

	with Microphone() as voice:
		print('I am listening you, say something.....')
		audio = r.listen(voice)

	try:
		command = r.recognize_google(audio)
		print('Bro you said '+ command)
	except UnknownValueError:
	    print("Bro, could not understand your audio")
	except RequestError as e:
	    print("Could not process your request {0}".format(e))

	if command =='stop' or command =='cancel':
		running = False

while running:
	speech_to_text()
