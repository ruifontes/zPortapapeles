# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import api
import ui
import wx
import nvwave
from tones import beep
from threading import Thread, Lock
from time import sleep
import os
import ctypes
from ctypes.wintypes import BOOL, HWND, HANDLE, HGLOBAL, UINT, LPVOID
from ctypes import c_size_t as SIZE_T
from typing import (Any, Callable, Dict, List, Iterable, Tuple) 
from . import ajustes

class ClipboardFormat:
    CF_TEXT = 1
    CF_BITMAP = 2
    CF_METAFILEPICT = 3
    CF_SYLK = 4
    CF_DIF = 5
    CF_TIFF = 6
    CF_OEMTEXT = 7
    CF_DIB = 8
    CF_PALETTE = 9
    CF_PENDATA = 10
    CF_RIFF = 11
    CF_WAVE = 12
    CF_UNICODETEXT = 13
    CF_ENHMETAFILE = 14
    CF_HDROP = 15
    CF_LOCALE = 16
    CF_DIBV5 = 17
    CF_MAX = 18
    CF_HTML = ctypes.windll.user32.RegisterClipboardFormatW("HTML Format")

# Solución extraida de https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard
# Me gusta más esta forma que la interna de NVDA o la de wxpython para manejar el portapapeles, es mas directa con el sistema.

OpenClipboard = ctypes.windll.user32.OpenClipboard
OpenClipboard.argtypes = HWND,
OpenClipboard.restype = BOOL
EmptyClipboard = ctypes.windll.user32.EmptyClipboard
EmptyClipboard.restype = BOOL
GetClipboardData = ctypes.windll.user32.GetClipboardData
GetClipboardData.argtypes = UINT,
GetClipboardData.restype = HANDLE
SetClipboardData = ctypes.windll.user32.SetClipboardData
SetClipboardData.argtypes = UINT, HANDLE
SetClipboardData.restype = HANDLE
CloseClipboard = ctypes.windll.user32.CloseClipboard
CloseClipboard.restype = BOOL
CF_UNICODETEXT = 13

GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc
GlobalAlloc.argtypes = UINT, SIZE_T
GlobalAlloc.restype = HGLOBAL
GlobalLock = ctypes.windll.kernel32.GlobalLock
GlobalLock.argtypes = HGLOBAL,
GlobalLock.restype = LPVOID
GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = HGLOBAL,
GlobalSize = ctypes.windll.kernel32.GlobalSize
GlobalSize.argtypes = HGLOBAL,
GlobalSize.restype = SIZE_T

GMEM_MOVEABLE = 0x0002
GMEM_ZEROINIT = 0x0040

unicode_type = type(u'')

def clean():
	# Función para borrar el portapapeles
	OpenClipboard(None)
	EmptyClipboard()
	CloseClipboard()

def get():
	# Función para obtener el contenido del portapapeles
	text = None
	OpenClipboard(None)
	handle = GetClipboardData(CF_UNICODETEXT)
	pcontents = GlobalLock(handle)
	size = GlobalSize(handle)
	if pcontents and size:
		raw_data = ctypes.create_string_buffer(size)
		ctypes.memmove(raw_data, pcontents, size)
		text = raw_data.raw.decode('utf-16le').rstrip(u'\0')
	GlobalUnlock(handle)
	CloseClipboard()
	return text

def put(text):
	# Función para pegar contenido al portapapeles
	if not isinstance(text, unicode_type):
		text = text.decode('mbcs')
	data = text.encode('utf-16le')
	OpenClipboard(None)
	EmptyClipboard()
	handle = GlobalAlloc(GMEM_MOVEABLE | GMEM_ZEROINIT, len(data) + 2)
	pcontents = GlobalLock(handle)
	ctypes.memmove(pcontents, data, len(data))
	GlobalUnlock(handle)
	SetClipboardData(CF_UNICODETEXT, handle)
	CloseClipboard()

def GetDictKeyName(theDict: Dict, theValue: Any, start: str = None) -> str:
	for key, value in theDict.items():
		if theValue == value and ((start and key.startswith(start)) or True):
			return key
	return ''

def detect() -> Dict[int, str]:
	formats = {}
	if OpenClipboard(None):
		formatType = 0
		arrayType = ctypes.c_wchar * 64
		while True:
			formatType = ctypes.windll.user32.EnumClipboardFormats(formatType)
			if formatType == 0:
				break
			values = arrayType()
			ctypes.windll.user32.GetClipboardFormatNameW(formatType, values, len(values))
			formatName = values.value
			if not formatName:
				formatName = GetDictKeyName(ClipboardFormat.__dict__, formatType, 'CF_')
			formats[formatType] = formatName
		CloseClipboard()
	if len(formats) == 0:
		return False
	else:
#		return formats
		if 'CF_UNICODETEXT' in formats.values():
			return True
		else:
			return False

def talk(text):
	# Función para mandar mensaje de lo copiado fuera del hilo de tiempo
	ui.message(text)

class ClipMonitor(Thread):
# Clase de hilo con tiempo para monitorizar el contenido del portapapeles y actuar en consecuencia
	def __init__(self, tiempo, *args, **kwargs):
		Thread.__init__(self, *args, **kwargs)

		self.tiempo = tiempo
		self.__borrado = ""
		self.__historial = []
		self.__flag = True
		self.pausa = False
		self.__candado = Lock()
		self.fichero = os.path.join(os.path.dirname(__file__), "Sonidos", "historial.wav")
		self.banderaHabla = False
		self.ultimoClipboard = ""
		self.clipTemp = ""

	def run(self):
		while self.__flag:
			try:
				clip = get()
				total = len(self.__historial)
				self.__candado.acquire() # Cerramos el candado para evitar que un hilo intente leer al mismo tiempo que otro está escribiendo
				if self.pausa == False: # Si no hay pausa continuamos
					if clip is not None: # Si no hay nada en el portapapeles continuamos
						if self.exist(self.__historial, clip) == False: # Si no se encuentra en la lista
							if total == 0: # Comprobamos si la lista tiene entradas == 0
								if clip == self.__borrado: # Comprobamos si es igual que lo ultimo borrado
									pass
								else: # Si no es igual que lo ultimo borrado
									if clip == self.clipTemp:
										pass
									else:
										self.__borrado = ""
										self.__historial.insert(0, clip)
										if ajustes.talkPaste:
											self.banderaHabla = True
											self.ultimoClipboard = clip
											wx.CallAfter(self.onTalk)
										if ajustes.sndHistorial: # Si tenemos True sonido
											if os.path.exists(self.fichero):
												nvwave.playWaveFile(self.fichero)
											else:
												beep(1000,50)
							else: # La lista si tiene entradas
								if self.__historial[0] == clip: # Comprobamos si la ultima entrada es igual que portapapeles
									pass
								else: # No es igual que la ultima entrada
									if clip ==self.__borrado:
										pass
									else:
										if clip == self.clipTemp:
											pass
										else:
											self.__borrado = ""
											self.__historial.insert(0, clip)
											if ajustes.sndHistorial: # Si tenemos True sonido
												if os.path.exists(self.fichero):
													nvwave.playWaveFile(self.fichero)
												else:
													beep(1000,50)
						else:
							if not self.clipTemp == clip:
								self.clipTemp = clip
								if not self.banderaHabla:
									if ajustes.talkPaste:
										self.banderaHabla = True
										self.ultimoClipboard = clip
										wx.CallAfter(self.onTalk)

				self.__candado.release() # Abrimos el candado
				sleep(self.tiempo) # Hacemos una pausa de un segundo. Puede ser más o menos pero una mínima pausa hay que hacer si no probablemente se bloquearía.
			except OSError: # Se ha copiado un objeto que no es texto
				pass

	def onTalk(self):
		if self.banderaHabla:
			talk(self.ultimoClipboard)
			self.banderaHabla = False

	def exist(self, listado, buscar):
		if not buscar in listado:
			return False
		return True

	@property # Esto es un getter. Sirve para acceder a la variable __historial que es interna y a la que no se puede acceder desde fuera del objeto. Se invoca con clipMonitor.historial
	def historial(self):
		self.__candado.acquire()
		h = self.__historial
		self.__candado.release()
		return h

	def borrar(self, valor):
		self.__candado.acquire()
		self.__borrado = self.__historial[valor]
		del self.__historial[valor]
		self.__candado.release()

	def borrarTodo(self):
		self.__candado.acquire()
		self.__borrado = self.__historial[0]
		del self.__historial[:]
		self.__candado.release()

	def pausar(self):
		self.pausa = True

	def reanudar(self):
		self.pausa = False

	def SetTimer(self, valor):
		self.__candado.acquire()
		self.tiempo = valor
		self.__candado.release()

	def kill(self):
		self.__flag = False
