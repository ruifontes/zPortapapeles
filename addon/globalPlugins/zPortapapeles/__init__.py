# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

#Idea original de  Peter Vagner <peter.v@datagate.sk>

import globalPluginHandler
import addonHandler
import queueHandler
import ui
import gui
import api
import inputCore
import scriptHandler
import globalVars
import config
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
from gui import guiHelper, nvdaControls
import speech
import watchdog
import core
from keyboardHandler import KeyboardInputGesture
from NVDAObjects.UIA import UIA
# Temporary: test for suggestions list until NVDA 2021.3 requirement is in effect.
import NVDAObjects.UIA
import time
import winsound
import wx
from threading import Thread
import os
from . import ajustes
from . import portapapeles as pt

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)

		if globalVars.appArgs.secure or config.isAppX: return

		ajustes.setup()
		NVDASettingsDialog.categoryClasses.append(PortapapelesPanel)
		self.old = speech.getState()
		self.monitor = None
		ajustes._main = self
		if hasattr(globalVars, 'zPortapapeles'):
			self.postStartupHandler()
		core.postNvdaStartup.register(self.postStartupHandler)
		globalVars.zPortapapeles = None

	def postStartupHandler(self):
		pt.clean()
		if ajustes.historial:
			self.monitor = pt.ClipMonitor(ajustes.tiempoDict.get(ajustes.tiempo), daemon=True)
			self.monitor.start()

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(PortapapelesPanel)
		try:
			self.monitor.kill()
		except:
			pass
		core.postNvdaStartup.unregister(self.postStartupHandler)

	def event_UIA_notification(self, obj, nextHandler, activityId=None, **kwargs):
		# Función para detectar las combinaciones de teclas seleccionar todo,, copiar, pegar y borrar de Word y excel
		if ajustes.voz == False:
			if obj.appModule.appName == 'winword' and activityId in ('AccSN4', 'AccSN3'):
				return
			if obj.appModule.appName == 'excel' and activityId in ('Microsoft.Office.Excel.PrimaryUserActionComplete.CeCopy', 'Microsoft.Office.Excel.PrimaryUserActionComplete.CeCut', 'Microsoft.Office.Excel.PrimaryUserActionComplete.CePaste'):
				return
		nextHandler()

	def audioOn(self, event):
		#Función para capturar la combinación de teclas pulsada y reproducir el audio correspondiente
		fichero = os.path.join(os.path.dirname(__file__), "Sonidos", ajustes.soundsDict.get(ajustes.messagesDict["+".join(event.modifierNames)+"+"+event.mainKeyName]))
		if os.path.exists(fichero):
			winsound.PlaySound(fichero, winsound.SND_ASYNC)
		return

	def script_gestos(self,gesture):
		# Función que simulara la tecla pulsada y actuara ofreciendo la información que el usuario eligiese en opciones
		obj = api.getFocusObject()

		gesture.send()

		if not obj:
			return 
		if obj.windowClassName == 'ConsoleWindowClass':
			return

		globalMapScripts = []
		globalMaps = [inputCore.manager.userGestureMap, inputCore.manager.localeGestureMap]
		for globalMap in globalMaps:
			for identifier in gesture.identifiers:
				globalMapScripts.extend(globalMap.getScriptsForGesture(identifier))

		treeInterceptor = obj.treeInterceptor
		if treeInterceptor and treeInterceptor.isReady:
			func = scriptHandler._getObjScript(treeInterceptor, gesture, globalMapScripts)
			if func and (not treeInterceptor.passThrough or getattr(func,"ignoreTreeInterceptorPassThrough",False)):
				if ajustes.voz == False:
					speech.setSpeechMode(0)
				func(treeInterceptor)
				if ajustes.voz == False:
					speech.setSpeechMode(self.old)

				if ajustes.audio == True:
					self.audioOn(gesture)

		if ajustes.voz == True:
			ui.message(ajustes.messagesDict["+".join(gesture.modifierNames)+"+"+gesture.mainKeyName])

		if ajustes.audio == True:
			self.audioOn(gesture)

	# Translators: Descripción para el dialogo de Gestos de entrada de NVDA
	@scriptHandler.script(gesture=None, description= _("Muestra la ventana de historial del portapapeles"),
		# Translators: Nombre para la categoría en el dialogo Gestos de entrada de NVDA
		category= _("zPortapapeles"))
	def script_Run(self, event):
		# Función para mostrar la ventana del historial. Contempla distintos errores como ventana ya abierta, opción no configurada o no hay nada en el historial.
		if ajustes.historial == True:
			if len(self.monitor.historial) == 0:
				# Translators: Mensaje informativo de que el historial se encuentra vacío
				msg = \
_("""No hay nada en el historial de zPortapapeles.""")
				ui.message(msg)
			else:
				if ajustes.winOn == False:
					HiloComplemento(1)
				else:
					# Translators: Mensaje informativo el cual le dice al usuario que no es posible abrir 2 ventanas del historial a la vez
					msg = \
_("""Ya hay una ventana del historial abierta.

No es posible tener dos ventanas a la vez.""")
					ui.message(msg)
		else:
			# Translators: Mensaje informativo que le indica al usuario que el historial no esta activado y como proceder si desea usarlo
			msg = \
_("""El historial del portapapeles no está activado.

Si desea usarlo, actívelo desde las opciones de NVDA en Opciones de zPortapapeles.""")
			ui.message(msg)

	# Translators: Descripción para el dialogo de Gestos de entrada de NVDA
	script_gestos.__doc__ = _("Teclas predefinidas del portapapeles (cambiar solo en distribuciones de portapapeles distinto)")
	# Translators: Nombre para la categoría en el dialogo Gestos de entrada de NVDA
	script_gestos.category = _("zPortapapeles")
	__gestures = {
		"kb:Control+a": "gestos",
		"kb:Control+c": "gestos",
		"kb:Control+e": "gestos",
		"kb:Control+v": "gestos",
		"kb:Control+x": "gestos",
		"kb:Control+z": "gestos",
	}

class PortapapelesPanel(SettingsPanel):

	# Translators: Titulo del panel del complemento en el dialogo de opciones de NVDA
	title = _("Opciones de zPortapapeles")

	def makeSettings(self, sizer):

		helper=guiHelper.BoxSizerHelper(self, sizer=sizer)

		# Translators: Descripción para el checkbox de opciones
		self.vozChk = helper.addItem(wx.CheckBox(self, label=_("Activar o desactivar anuncios hablados del portapapeles")))
		self.vozChk.Value = ajustes.voz
		# Translators: Descripción para el checkbox de opciones
		self.audioChk = helper.addItem(wx.CheckBox(self, label=_("Activar o desactivar sonidos del portapapeles")))
		self.audioChk.Value = ajustes.audio
		# Translators: Descripción para el checkbox de opciones
		self.historialChk = helper.addItem(wx.CheckBox(self, label=_("Activar o desactivar el historial del portapapeles")))
		self.historialChk.Value = ajustes.historial
		self.historialChk.Bind(wx.EVT_CHECKBOX,self.onTimer)
		# Translators: Descripción de la etiqueta del choice de opciones
		self.choiceTimer = helper.addLabeledControl(_("Elija un tiempo para actualizar el monitor del portapapeles"), wx.Choice, choices=ajustes.tiempoChk)
		# Translators: Descripción para el checkbox de opciones
		self.sndHistorialChk = helper.addItem(wx.CheckBox(self, label=_("Notificar con un sonido cada vez que se agregue algo al historial")))
		self.sndHistorialChk.Value = ajustes.sndHistorial
		# Translators: Descripción para el checkbox de opciones
		self.vozCopiadoChk = helper.addItem(wx.CheckBox(self, label=_("Hablar lo copiado al portapapeles y agregado al Historial")))
		self.vozCopiadoChk.Value = ajustes.talkPaste

		if self.historialChk.Value:
			self.choiceTimer.Enable()
			self.sndHistorialChk.Enable()
			self.vozCopiadoChk.Enable()
		else:
			self.choiceTimer.Disable()
			self.sndHistorialChk.Disable()
			self.vozCopiadoChk.Disable()

		self.choiceTimer.Selection = ajustes.tiempo

		self.tempHistorial = ajustes.historial
		self.tempTiempo = ajustes.tiempo

	def onTimer(self, event):
		chk = event.GetEventObject()
		if chk.GetValue():
			self.choiceTimer.Enable()
			self.sndHistorialChk.Enable()
			self.vozCopiadoChk.Enable()
		else:
			self.choiceTimer.Disable()
			self.sndHistorialChk.Disable()
			self.vozCopiadoChk.Disable()

	def onSave(self):
		ajustes.setConfig("voz", self.vozChk.Value)
		ajustes.voz = self.vozChk.Value
		ajustes.setConfig("audio", self.audioChk.Value)
		ajustes.audio = self.audioChk.Value
		ajustes.setConfig("historial", self.historialChk.Value)
		ajustes.historial = self.historialChk.Value
		ajustes.setConfig("tiempo", self.choiceTimer.Selection)
		ajustes.tiempo =self.choiceTimer.Selection
		ajustes.setConfig("sonidoHistorial", self.sndHistorialChk.Value)
		ajustes.sndHistorial = self.sndHistorialChk.Value
		ajustes.setConfig("vozCopiado", self.vozCopiadoChk.Value)
		ajustes.talkPaste = self.vozCopiadoChk.Value

		if self.tempHistorial:
			if ajustes.historial:
				if self.tempTiempo ==ajustes.tiempo:
					return
				else:
					ajustes._main.monitor.SetTimer(ajustes.tiempoDict.get(ajustes.tiempo))
			else:
				ajustes._main.monitor.kill()
		else:
			if ajustes.historial:
				ajustes._main.postStartupHandler()
			else:
				return

	def onPanelActivated(self):
		self.originalProfileName = config.conf.profiles[-1].name
		config.conf.profiles[-1].name = None
		self.Show()

	def onPanelDeactivated(self):
		config.conf.profiles[-1].name = self.originalProfileName
		self.Hide()

class HistorialDialogo(wx.Dialog):
	def _calculatePosition(self, width, height):
		w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
		h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
		# Centre of the screen
		x = w / 2
		y = h / 2
		# Minus application offset
		x -= (width / 2)
		y -= (height / 2)
		return (x, y)

	def __init__(self, parent):

		WIDTH = 800
		HEIGHT = 600
		pos = self._calculatePosition(WIDTH, HEIGHT)

		# Translators: Titulo de la ventana de dialogo del Historial
		super(HistorialDialogo, self).__init__(parent, -1, title=_("Historial del Portapapeles"),pos = pos, size = (WIDTH, HEIGHT))

		ajustes.winOn = True
		self.listaTemporal = ajustes._main.monitor.historial
		self.panel_1 = wx.Panel(self, wx.ID_ANY)

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		# Translators: Etiqueta para el listbox con atajo de tecla Alt+H
		label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("&Historial:"))
		sizer_1.Add(label_1, 0, wx.EXPAND, 0)

		self.listbox = wx.ListBox(self.panel_1, 1, choices=self.listaTemporal)
		self.listbox.SetSelection(0)
		sizer_1.Add(self.listbox, 1, wx.ALL | wx.EXPAND, 0)

		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

		# Translators: Nombre del botón con tecla de atajo Alt+B
		self.borrarBTN = wx.Button(self.panel_1, 101, _("&Borrar"))
		sizer_2.Add(self.borrarBTN, 0, wx.ALIGN_BOTTOM, 0)

		# Translators: Nombre del botón con tecla de atajo Alt+T
		self.borrarAllBTN = wx.Button(self.panel_1, 102, _("Borrar &todo"))
		sizer_2.Add(self.borrarAllBTN, 0, wx.BOTTOM, 0)

		# Translators: Nombre del botón con tecla de atajo Alt+R
		self.refrescarBTN = wx.Button(self.panel_1, 103, _("&Refrescar"))
		sizer_2.Add(self.refrescarBTN, 0, wx.BOTTOM, 0)

		# Translators: Nombre del botón con tecla de atajo Alt+C
		self.cerrarBTN = wx.Button(self.panel_1, wx.ID_CANCEL, _("&Cerrar"))
		sizer_2.Add(self.cerrarBTN, 0, wx.BOTTOM, 0)

		self.panel_1.SetSizer(sizer_1)

		self.Layout()
		self.CenterOnScreen()

		self.cargaEventos()

	def cargaEventos(self):
		# Función para tener todas las definiciones juntas
		self.Bind(wx.EVT_BUTTON,self.onBotones)
		self.Bind(wx.EVT_BUTTON, self.onSalir, id=wx.ID_CANCEL)
		self.Bind(wx.EVT_CLOSE, self.onSalir)
		self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyEvent)

	def SetClipboardTextTime(self, text):
		# Función utilizada para copiar al portapapeles después de ocultar la ventana del historial
		pt.clean()
		self.SetClipboardText(text)

	def SetClipboardText(self, text):
		# Función utilizada para copiar al portapapeles
		pt.put(text)

	def GetClipboardText(self):
		# Función utilizada para pegar del portapapeles
		return pt.get()

	def onRefrescar(self):
		# Función utilizada para refrescar el listbox del historial
		if len(ajustes._main.monitor.historial) == 0:
			self.onSalir(None)
		else:
			self.listbox.Clear()
			self.listaTemporal = ajustes._main.monitor.historial
			self.listbox.Append(self.listaTemporal)
			self.listbox.SetSelection(0)
			self.listbox.SetFocus()

	def onBorrar(self):
		# Función utilizada para borrar el item seleccionado del historial
		total = len(ajustes._main.monitor.historial)
		totalTemporal = self.listbox.GetCount()
		indice = self.listbox.GetSelection()
		if total == totalTemporal:
			ajustes._main.monitor.borrar(indice)
			self.onRefrescar()
		else:
			ajustes._main.monitor.borrar(total - totalTemporal + indice)
			self.onRefrescar()

	def onBotones(self, event):
		# Función para manejar los botones del cuadro de dialogo del historial
		botonID = event.GetEventObject().GetId()
		if botonID == 101:
			self.onBorrar()
		elif botonID == 102:
			ajustes._main.monitor.borrarTodo()
			self.onRefrescar()
		elif botonID == 103:
			self.onRefrescar()

	def onPegar(self, event):
		# Función que pegara al foco el item que tengamos seleccionado en el listbox del historial
		ajustes._main.monitor.pausar()
		self.Hide()
		event.Skip()
		paste = self.listbox.GetString(self.listbox.GetSelection()) 
		# Source code taken from: frequentText add-on for NVDA. Written by Rui Fontes and Ângelo Abrantes
		try:
			clipboardBackup = self.GetClipboardText()
		except:
			clipboardBackup = None
		self.SetClipboardText(paste)
		time.sleep(0.1)
		api.processPendingEvents(False)
		focus = api.getFocusObject()
		if focus.windowClassName == "ConsoleWindowClass":
			# Windows console window - Control+V doesn't work here, so using an alternative method here
			WM_COMMAND = 0x0111
			watchdog.cancellableSendMessage(focus.windowHandle, WM_COMMAND, 0xfff1, 0)
		else:
			if ajustes.voz:
				# Translators: Mensaje informativo de pegado al foco
				ui.message(_("Pegado al foco."))
			KeyboardInputGesture.fromName("Control+v").send()

		try:
			core.callLater(300, lambda: self.SetClipboardTextTime(clipboardBackup))
		except:
			pass
		core.callLater(375, lambda: ajustes._main.monitor.reanudar())
		self.onSalir(None)

	def OnKeyEvent(self, event):
		# Función de control del teclado
		foco = wx.Window.FindFocus().GetId()
		if event.GetUnicodeKey() in [wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER]:
			if foco == 1:
				wx.CallAfter(self.onPegar, event)
				event.Skip()
		elif event.GetUnicodeKey() == wx.WXK_ESCAPE:
			self.onSalir(None)
		else:
			event.Skip()

	def onSalir(self, event):
		# Función para cerrar correctamente el dialogo del historial
		ajustes.winOn = False
		self.Destroy()
		gui.mainFrame.postPopup()

class HiloComplemento(Thread):
#Clase que manejara la visualización del dialogo del historial en un hilo separado de NVDA
	def __init__(self, opcion):
		super(HiloComplemento, self).__init__()

		self.opcion = opcion
		self.daemon = True
		self.start()

	def run(self):
		def HistorialDLG():
			self._MainWindows = HistorialDialogo(gui.mainFrame)
			gui.mainFrame.prePopup()
			self._MainWindows.Show()

		if self.opcion == 1:
			wx.CallAfter(HistorialDLG)
