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

# Lista con idiomas para las traducciones
langLST = [_("Alemán"), _("Árabe"), _("Croata"), _("Español"), _("Francés"), _("Inglés"), _("Italiano"), _("Polaco"), _("Portugués"), _("Ruso"), _("Turco"), _("Ucraniano")]
# Diccionario con las abreviaturas de idioma
langDict = {
	0:"de",
	1:"ar",
	2:"hr",
	3:"es",
	4:"fr",
	5:"en",
	6:"it",
	7:"pl",
	8:"pt",
	9:"ru",
	10:"tr",
	11:"uk",
}

_main = None
audio = None
voz = None
historial = None
tiempo = None
sndHistorial = None
talkPaste = None
isGame = None
isActivo = None
tiempoLang = None
langTrans = None
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
		"game": "boolean(default=False)",
		"tiempoLang": "integer(default=1, min=0, max=5)",
		"langTrans": "integer(default=5, min=0, max=11)",
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
	global voz, audio, historial, tiempo, sndHistorial, talkPaste, isGame, isActivo, tiempoLang, langTrans
	initConfiguration()
	voz = getConfig("voz")
	audio = getConfig("audio")
	historial = getConfig("historial")
	tiempo = getConfig("tiempo")
	sndHistorial = getConfig("sonidoHistorial")
	talkPaste = getConfig("vozCopiado")
	isGame = getConfig("game")
	isActivo = getConfig("activado")
	tiempoLang = getConfig("tiempoLang")
	langTrans = getConfig("langTrans")
