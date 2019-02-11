#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import os;
import Tkinter as tk;
from Tkinter import *;
from tkinter import *;
from PIL import Image, ImageDraw, ImageTk;

global pict;
global vr;
global drawer;
global vrhCount;
vrhCount=1;
global vrhovi;
vrhovi={};
global putevi;
putevi={};
global prviVrh;
prviVrh=False;
global oznaceniVrh;
oznaceniVrh=[];
global oznaceniVrhIme;
oznaceniVrhIme="";
global korakPoKorak;
korakPoKorak="Algoritam jos nije proveden!";
global origSlika;
origSlika=None;

def kliknut(event):
	global vrhCount;
	global vrhovi;
	global prviVrh;
	global oznaceniVrh;
	global oznaceniVrhIme;
	global origSlika;
	global drawer;
	global pict;
	if(origSlika is not None):
		pict=Image.new('RGB',(700,600),"white");
		pict.paste(origSlika,(0,0));
		drawer=ImageDraw.Draw(pict);
	#Na slici su dodane izmjene; Originalne slike vise nema
	origSlika=None;
	#Oznacavanje vrha; vr=1
	if(vr.get()==1):
		Testko=True;
		#Nema preklapanja vrhova
		for vrh in vrhovi:
			if(event.x<vrhovi[vrh][0]+10 and event.x>vrhovi[vrh][0]-10 and event.y<vrhovi[vrh][1]+10 and event.y>vrhovi[vrh][1]-10):
				Testko=False;
				break;
		if(Testko):
			if(len(pocetnivrh.get("1.0",END))==1):
				pocetnivrh.insert("1.0","V1");
			drawer.ellipse((event.x-10,event.y-10,event.x+10,event.y+10),fill=(0,0,0));
			drawer.text((event.x-5,event.y-5),"V"+str(vrhCount),(255,255,255));
			vrhovi["V"+str(vrhCount)]=[event.x,event.y];
			vrhCount+=1;
			imgn=ImageTk.PhotoImage(pict);
			pictCont.configure(image=imgn);
			pictCont.Image=imgn;
	
	#Oznacavanje puta
	elif(vr.get()==2):
		testko=False;
		vrhek=[];
		ime="";
		for vrh in vrhovi:
			if((event.x<=int(vrhovi[vrh][0])+10 and event.x>=int(vrhovi[vrh][0])-10) and (event.y<=int(vrhovi[vrh][1])+10 and event.y>=int(vrhovi[vrh][1])-10)):
				testko=True;
				vrhek=vrhovi[vrh];
				ime=vrh;
				if(oznaceniVrhIme!="" and ime==oznaceniVrhIme):
					testko=False;
				break;
		if(testko):
			if(not prviVrh):
				prviVrh=True;
				oznaceniVrh=vrhek;
				oznaceniVrhIme=ime;
				drawer.ellipse((oznaceniVrh[0]-10,oznaceniVrh[1]-10,oznaceniVrh[0]+10,oznaceniVrh[1]+10),fill=(200,200,0));
				drawer.text((oznaceniVrh[0]-5,oznaceniVrh[1]-5),ime,(255,255,255));
				imgn=ImageTk.PhotoImage(pict);
				pictCont.configure(image=imgn);
				pictCont.Image=imgn;
			else:
				prviVrh=False;
				drawer.ellipse((oznaceniVrh[0]-10,oznaceniVrh[1]-10,oznaceniVrh[0]+10,oznaceniVrh[1]+10),fill=(0,0,0));
				#Svaki put izmedju dva vrha je jedinstven
				if(oznaceniVrhIme+","+ime not in putevi and ime+","+oznaceniVrhIme not in putevi):
					drawer.line((oznaceniVrh[0],oznaceniVrh[1],vrhek[0],vrhek[1]),fill=(0,0,0),width=4);
					checkDuljPuta();
					drawer.text(((oznaceniVrh[0]+vrhek[0])/2 + 5,(oznaceniVrh[1]+vrhek[1])/2 + 5),duljpu.get("1.0",END),(255,0,255));
					drawer.text((vrhek[0]-5,vrhek[1]-5),ime,(255,255,255));
					putevi[oznaceniVrhIme+","+ime]=duljpu.get("1.0",END);
				drawer.text((oznaceniVrh[0]-5,oznaceniVrh[1]-5),oznaceniVrhIme,(255,255,255));
				imgn=ImageTk.PhotoImage(pict);
				pictCont.configure(image=imgn);
				pictCont.Image=imgn;
				oznaceniVrh=[];
				oznaceniVrhIme="";
		#Oznacio vrh pa odustao; kliknuo sa strane
		else:
			if(oznaceniVrhIme!=""):
				drawer.ellipse((oznaceniVrh[0]-10,oznaceniVrh[1]-10,oznaceniVrh[0]+10,oznaceniVrh[1]+10),fill=(0,0,0));
				drawer.text((oznaceniVrh[0]-5,oznaceniVrh[1]-5),oznaceniVrhIme,(255,255,255));
				imgn=ImageTk.PhotoImage(pict);
				pictCont.configure(image=imgn);
				pictCont.Image=imgn;
				oznaceniVrh=[];
				oznaceniVrhIme="";
				prviVrh=False;


def checkDuljPuta():
	try:
		probavanje=int(duljpu.get("1.0",END));
		if(probavanje<1):
			duljpu.delete("1.0",END);
			duljpu.insert(END,"1");
	except:
		duljpu.delete("1.0",END);
		duljpu.insert(END,"1");
		
def eraser():
	global pict;
	global drawer;
	global vrhCount;
	global vrhovi;
	global putevi;
	global korakPoKorak;
	global origSlika;
	vrhovi={};
	putevi={};
	vrhCount=1;
	pict=Image.new('RGB',(700,600),"white");
	drawer=ImageDraw.Draw(pict);
	imgn=ImageTk.PhotoImage(pict);
	pictCont.configure(image=imgn);
	pictCont.Image=imgn;
	korakPoKorak="Algoritam jos nije proveden!";
	origSlika=None;
	
def pokrAlg():
	global pict;
	global drawer;
	global vrhovi;
	global putevi;
	global korakPoKorak;
	global origSlika;
	if(origSlika is None):
		origSlika=Image.new('RGB',(700,600),"white");
		origSlika.paste(pict,(0,0));
	else:
		pict=Image.new('RGB',(700,600),"white");
		pict.paste(origSlika,(0,0));
		drawer=ImageDraw.Draw(pict);
	korakPoKorak="";
	if(str(pocetnivrh.get("1.0",END))[0:len(str(pocetnivrh.get("1.0",END)))-1] not in vrhovi):
		pocetnivrh.delete("1.0",END);
		pocetnivrh.insert("1.0","V1");
	trenvrh=str(pocetnivrh.get("1.0",END));
	trenvrh=trenvrh[0:len(trenvrh)-1]
	ukuda=0;
	obidjeni={trenvrh:ukuda};
	neobidjeni=dict.fromkeys(vrhovi.keys());
	neobidjeniKeys=neobidjeni.keys();
	neobidjeniKeys.remove(trenvrh);
	trenspoj=dict.fromkeys(neobidjeni);
	koraci=1;
	#Zadnji obidjeni vrh
	zadvrh="";
	safecount=0;
	while(len(neobidjeniKeys)>0 and safecount<len(putevi)):
		safecount+=1;
		korakPoKorak+="Korak "+str(koraci)+".:";
		if(koraci==1):
			korakPoKorak+="\nPozicioniranje u početni vrh: "+trenvrh+" , kojem pripisujemo udaljenost 0.\nSvim ostalim vrhovima pripisujemo udaljenost inf(beskonačno).";
		else:
			korakPoKorak+="\nU skupu \"Neobiđeni_vrhovi\" tražim najmanju udaljenost i pripadni vrh te se u njega pozicioniram.\nREZULTAT: Pozicioniranje u vrh: "+trenvrh;
		if(trenspoj[trenvrh] is not None):
			korakPoKorak+=" preko vrha: "+trenspoj[trenvrh];
		korakPoKorak+="\n\nObiđeni_vrhovi="+str(obidjeni)+"\nNeobiđeni_vrhovi={";
		for neo in neobidjeniKeys:
			korakPoKorak+=neo+":";
			if(neobidjeni[neo] is None):
				korakPoKorak+="inf, ";
			else:
				korakPoKorak+=str(neobidjeni[neo])+", ";
		korakPoKorak=korakPoKorak[:-2];
		korakPoKorak+="}\n\n\n";
		koraci+=1;
		#Provjera ima li promjene u udaljenosti
		doduda=False;
		susvrhovi="";
		korakPoKorak+="Korak "+str(koraci)+".:\nIz vrha: "+trenvrh+" promatram udaljenosti prema susjednim neobiđenim vrhovima i uspoređujem ih sa \nudaljenostima zapisanim u skupu \"Neobiđeni_vrhovi\". Ako su udaljenosti od pozicije (vrh "+trenvrh+") \nmanje od onih u skupu, ažuriram skup.\nREZULTAT: ";
		for key in putevi:
			if(key.split(",")[0]==trenvrh or key.split(",")[1]==trenvrh):
				druvrh=trenvrh;
				if(key.split(",")[0]==trenvrh):
					druvrh=key.split(",")[1];
				else:
					druvrh=key.split(",")[0];
				if(druvrh in neobidjeniKeys):
					if(neobidjeni[druvrh] is None or neobidjeni[druvrh]>ukuda+int(putevi[key])):
						neobidjeni[druvrh]=ukuda+int(putevi[key]);
						trenspoj[druvrh]=trenvrh;
						doduda=True;
						susvrhovi+=druvrh+","
		if(doduda):
			susvrhovi=susvrhovi[:-1];
			ssvrhovi=susvrhovi.split(",");
			#Uzlazno sortiranje
			ssvrhovi.sort();
			susvrhovi="";
			for ss in ssvrhovi:
				susvrhovi+=ss+", "
			susvrhovi=susvrhovi[:-2];
			korakPoKorak+="Ažurirane udaljenosti prema susjednim vrhovima: "+susvrhovi+"\n\nNeobiđeni_vrhovi={";
		else:
			korakPoKorak+="Nema promjene udaljenosti prema niti jednom susjednom vrhu.\n\nNeobiđeni_vrhovi={"
		koraci+=1;
		for neo in neobidjeniKeys:
			korakPoKorak+=neo+":";
			if(neobidjeni[neo] is None):
				korakPoKorak+="inf, ";
			else:
				korakPoKorak+=str(neobidjeni[neo])+", ";
		korakPoKorak=korakPoKorak[:-2];
		korakPoKorak+="}\n\n\n";
		trenuda=0;
		trenvrh1="";
		for key in neobidjeniKeys:
			if(neobidjeni[key] is not None):
				if(trenuda==0 or trenuda>neobidjeni[key]):
					trenuda=neobidjeni[key];
					trenvrh1=key;
		if(trenvrh1!=""):
			ukuda=trenuda;
			obidjeni[trenvrh1]=ukuda;
			neobidjeniKeys.remove(trenvrh1);
			if(len(neobidjeniKeys)==0):
				zadvrh=trenvrh1;
			#Linija
			drawer.line((vrhovi[trenspoj[trenvrh1]][0],vrhovi[trenspoj[trenvrh1]][1],vrhovi[trenvrh1][0],vrhovi[trenvrh1][1]),fill=(0,100,255),width=4);
			drawer.ellipse((vrhovi[trenspoj[trenvrh1]][0]-10,vrhovi[trenspoj[trenvrh1]][1]-10,vrhovi[trenspoj[trenvrh1]][0]+10,vrhovi[trenspoj[trenvrh1]][1]+10),fill=(0,0,0));
			drawer.text((vrhovi[trenspoj[trenvrh1]][0]-5,vrhovi[trenspoj[trenvrh1]][1]-5),trenspoj[trenvrh1],fill=(255,255,255));
			drawer.ellipse((vrhovi[trenvrh1][0]-10,vrhovi[trenvrh1][1]-10,vrhovi[trenvrh1][0]+10,vrhovi[trenvrh1][1]+10),fill=(0,0,0));
			drawer.text((vrhovi[trenvrh1][0]-5,vrhovi[trenvrh1][1]-5),trenvrh1,fill=(255,255,255));
			trenvrh=trenvrh1;
	imgn=ImageTk.PhotoImage(pict);
	pictCont.configure(image=imgn);
	pictCont.Image=imgn;
	try:
		korakPoKorak+="Korak "+str(koraci)+".: Obiđen zadnji neobiđeni vrh: "+zadvrh+" preko vrha: "+trenspoj[zadvrh]+" ; algoritam gotov!\n"
	except:
		korakPoKorak+="Graf nije potpuno povezan pa algoritam nije mogao završiti!";
	
def isps():
	global korakPoKorak;
	wdow=Tk();
	wdow.title("Prikaz algoritma korak po korak");
	contner=Listbox(wdow);
	contner.pack(side=LEFT,expand=True, fill=BOTH);
	sbar=Scrollbar(wdow);
	sbar.pack(side=RIGHT,fill=Y);
	for ix in korakPoKorak.split("\n"):
		contner.insert(END,ix);
	contner.config(yscrollcommand=sbar.set);
	contner.config(width=0);
	sbar.config(command=contner.yview);
	wdow.mainloop();	
			
window=Tk();

window.geometry("800x600");
window.title("Djikstra draw");
commandContainer=Frame(window);
commandContainer.pack(side=RIGHT,anchor='n');
pict=Image.new('RGB',(700,600),"white");
global drawer;
drawer=ImageDraw.Draw(pict);
img=ImageTk.PhotoImage(pict);
pictCont=tk.Label(window,image=img);
pictCont.bind("<Button-1>",kliknut);
pictCont.pack(side="left",expand="yes");
tx=Label(commandContainer,text="-Za postavljanje vrhova grafa \nodaberite opciju \'Točka\' i \nkliknite bilo gdje na sliku.\n\n-Za povezivanje bilo koja\ndva vrha, odaberite opciju\n\'Put\' i odaberite bilo koja dva\nvrha klikom na njih.\n;Ukoliko ste odabrali krivi vrh,\nkliknite bilo gdje na sliku,\nosim na neki od vrhova\n\n-Za pokretanje algoritma \nkliknite na \'Pokreni algoritam\'\n\n-Za brisanje slike kliknite na \n\'Izbriši\'\n\n",width=22);
tx.pack(anchor="w");

vr=tk.IntVar(None,1);
rb1=Radiobutton(commandContainer,text="Točka",variable=vr,value=1);
rb1.pack(anchor='w');
rb2=Radiobutton(commandContainer,text="Put",variable=vr,value=2);
rb2.pack(anchor='w');
btn1=Button(commandContainer,text="Pokreni algoritam", command=pokrAlg);
btn1.pack(anchor='w');
btn2=Button(commandContainer,text="Izbriši", command=eraser);
btn2.pack(anchor="w")
btn3=Button(commandContainer,text="Prikaz algoritma korak po korak", command=isps);
btn3.pack(anchor="w");
duljp=Label(commandContainer,text="Duljina puta");
duljp.pack(anchor="w");
duljpu=Text(commandContainer);
duljpu.config(width=10,height=2);
duljpu.insert(END,"1");
duljpu.pack(anchor="w");
pocetvrh=Label(commandContainer,text="Početni vrh za algoritam:");
pocetvrh.pack(anchor="w");
pocetnivrh=Text(commandContainer);
pocetnivrh.config(width=10,height=2);
pocetnivrh.pack(anchor="w");
about=Label(commandContainer,text="Created by:\nFuzzy\n(Ivan Mihaljević)\n2018.");
about.pack(anchor="s");

window.mainloop();


