#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

from Da import BdApi
import PlayerView

class GUI :

	def __init__ (self) :
		self.winTitle = 'Config'
		self.save = ''

	def show (self, data) :
		self.slave = Tkinter.Toplevel()
		self.slave.title(self.winTitle)
		self.slave.resizable(width = 'false', height = 'false')
		self.slave.geometry('280x280+200+200')

		mainFrame = Tkinter.Frame(self.slave, bd = 0, bg="#444")
		mainFrame.pack(expand = True, fill = 'both')

		pathLabel = Tkinter.Label(mainFrame, text="网盘存放路径", fg = '#ddd', bg="#444", anchor = 'center')
		pathLabel.grid(row = 0, column = 1, pady = 5)

		self.path = Tkinter.Entry(mainFrame, width = 25, bd = 0, bg = "#222", fg = "#ddd", highlightthickness = 1, highlightcolor="#111", highlightbackground = '#111', selectbackground = '#116cd6', justify='center')
		self.path.grid(row = 1, column = 1, pady = 5)
		self.path.insert('end', data['path'])

		AriaRpclabel = Tkinter.Label(mainFrame, text="Aria2 Json-RPC路径", fg = '#ddd', bg="#444", anchor = 'center')
		AriaRpclabel.grid(row = 2, column = 1)

		self.ariarpc = Tkinter.Entry(mainFrame, width = 25, bd = 0, bg = "#222", fg = "#ddd", highlightthickness = 1, highlightcolor="#111", highlightbackground = '#111', selectbackground = '#116cd6', justify='center')
		self.ariarpc.grid(row = 3, column = 1, pady = 5)
		self.ariarpc.insert('end', data['ariarpc'])

		AriaPathlabel = Tkinter.Label(mainFrame, text="Aria2 Json-RPC路径", fg = '#ddd', bg="#444", anchor = 'center')
		AriaPathlabel.grid(row = 4, column = 1)

		self.ariapath = Tkinter.Entry(mainFrame, width = 25, bd = 0, bg = "#222", fg = "#ddd", highlightthickness = 1, highlightcolor="#111", highlightbackground = '#111', selectbackground = '#116cd6', justify='center')
		self.ariapath.grid(row = 5, column = 1, pady = 5)
		self.ariapath.insert('end', data['ariapath'])

		updateTimelabel = Tkinter.Label(mainFrame, text="自动检测更新", fg = '#ddd', bg="#444", anchor = 'center')
		updateTimelabel.grid(row = 6, column = 1)

		utFrame = Tkinter.Frame(mainFrame, bd = 0, bg="#444")
		utFrame.grid(row = 7, column = 1, pady = 5)

		self.chkUpdateTime = Tkinter.IntVar()
		self.chkUpdateTime.set(int(data['udrate']))
		r1 = Tkinter.Radiobutton(utFrame, text="每天", fg = '#ddd', bg="#444", variable=self.chkUpdateTime, value=1)
		r1.grid(row = 0, column = 0, sticky = 'e')
		r2 = Tkinter.Radiobutton(utFrame, text="每周", fg = '#ddd', bg="#444", variable=self.chkUpdateTime, value=2)
		r2.grid(row = 0, column = 1, sticky = 'e')
		r3 = Tkinter.Radiobutton(utFrame, text="每月", fg = '#ddd', bg="#444", variable=self.chkUpdateTime, value=3)
		r3.grid(row = 0, column = 2, sticky = 'e')

		if data['bdc'] == '' :
			bdLoginBtn = Tkinter.Button(mainFrame, text = '百度云登录', width = 10, fg = '#222', highlightbackground = '#444', command = lambda cb = BdApi.BdApi().saveLogin : PlayerView.GUI().showLoginWindow(cb))
			bdLoginBtn.grid(row = 8, column = 1, pady = 5)
		else :
			bdLoginBtn = Tkinter.Button(mainFrame, text = '百度云已登录', width = 10, fg = '#222', highlightbackground = '#444', command = None)
			bdLoginBtn.grid(row = 8, column = 1, pady = 5)			

		cfgBtn = Tkinter.Button(mainFrame, text = '保存配置', width = 20, fg = '#222', highlightbackground = '#444', command = self.saveCfg)
		cfgBtn.grid(row = 9, column = 1, pady = 5)

		mainFrame.grid_columnconfigure(0, weight=1)
		mainFrame.grid_columnconfigure(2, weight=1)

	def saveCfg (self) :
		data = {
			'path' : self.path.get(),
			'ariarpc' : self.ariarpc.get(),
			'ariapath' : self.ariapath.get(),
			'udrate' : self.chkUpdateTime.get()
		}

		result = self.save(data)

		if result['stat'] == 1 :
			self.slave.withdraw()
			tkMessageBox.showinfo('Success', '更新成功')
		else :
			tkMessageBox.showinfo('Error', result['msg'])
