# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import addonHandler
import config

addonHandler.initTranslation()

messagesDict = {
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+e":_("Seleccionar todo"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+a":_("Seleccionar todo"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+x":_("Cortar"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+c":_("Copiar"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+v":_("Pegar"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+y":_("Rehacer"),
	# Translators: Mensaje que informa de la acción de la combinación de tecla pulsada por el usuario
	"control+z":_("Deshacer")
}

soundsDict = {
	_("Copiar"):"copiar.wav",
	_("Cortar"):"cortar.wav",
	_("Pegar"):"pegar.wav",
	_("Seleccionar todo"):"todo.wav",
	_("Rehacer"):"rehacer.wav",
	_("Deshacer"):"desacer.wav",
}

tiempoDict = {
	0:0.1,
	1:0.2,
	2:0.3,
	3:0.4,
	4:0.5,
	5:1,
}

tiempoChk = [
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("1 décima de segundo"),
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("2 décimas de segundo"),
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("3 décimas de segundo"),
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("4 décimas de segundo"),
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("5 décimas de segundo"),
	# Translators: Descripción de item para el choice del tiempo de opciones
	_("1 segundo")
]

_main = None
audio = None
voz = None
historial = None
tiempo = None
sndHistorial = None
talkPaste = None
isActivo = None
winOn = False

def initConfiguration():
	confspec = {
		"voz": "boolean(default=True)",
		"audio": "boolean(default=False)",
		"historial": "boolean(default=False)",
		"tiempo": "integer(default=1, min=0, max=5)",
		"sonidoHistorial": "boolean(default=False)",
		"vozCopiado": "boolean(default=False)",
		"activado": "boolean(default=True)",
	}
	config.conf.spec['zPortapapeles'] = confspec

def getConfig(key):
	value = config.conf["zPortapapeles"][key]
	return value

def setConfig(key, value):
	try:
		config.conf.profiles[0]["zPortapapeles"][key] = value
	except:
		config.conf["zPortapapeles"][key] = value

def setup():
	global voz, audio, historial, tiempo, sndHistorial, talkPaste, isActivo
	initConfiguration()
	voz = getConfig("voz")
	audio = getConfig("audio")
	historial = getConfig("historial")
	tiempo = getConfig("tiempo")
	sndHistorial = getConfig("sonidoHistorial")
	talkPaste = getConfig("vozCopiado")
	isActivo = getConfig("activado")
