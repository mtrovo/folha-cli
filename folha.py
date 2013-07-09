#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from time import strftime
from termcolor import cprint, colored
from googl import Googl
import os

from sys import argv

SHORT_TIME='%d/%m %H:%M'
FEEDS={
  "emcimadahora":{"href":"http://feeds.folha.uol.com.br/emcimadahora/rss091.xml", "title":"Em cima da hora"},
  "opiniao":{"href":"http://feeds.folha.uol.com.br/opiniao/rss091.xml", "title":"Opinião"},
  "poder":{"href":"http://feeds.folha.uol.com.br/poder/rss091.xml", "title":"Poder"},
  "mundo":{"href":"http://feeds.folha.uol.com.br/mundo/rss091.xml", "title":"Mundo"},
  "mercado":{"href":"http://feeds.folha.uol.com.br/mercado/rss091.xml", "title":"Mercado"},
  "cotidiano":{"href":"http://feeds.folha.uol.com.br/cotidiano/rss091.xml", "title":"Cotidiano"},
  "educacao":{"href":"http://feeds.folha.uol.com.br/educacao/rss091.xml", "title":"Educação"},
  "esporte":{"href":"http://feeds.folha.uol.com.br/esporte/rss091.xml", "title":"Esporte"},
  "ilustrada":{"href":"http://feeds.folha.uol.com.br/ilustrada/rss091.xml", "title":"Ilustrada"},
  "folhateen":{"href":"http://feeds.folha.uol.com.br/folhateen/rss091.xml", "title":"Folhateen"},
  "ilustrissima":{"href":"http://feeds.folha.uol.com.br/ilustrissima/rss091.xml", "title":"Ilustríssima"},
  "ciencia":{"href":"http://feeds.folha.uol.com.br/ciencia/rss091.xml", "title":"Ciência"},
  "ambiente":{"href":"http://feeds.folha.uol.com.br/ambiente/rss091.xml", "title":"Ambiente"},
  "tec":{"href":"http://feeds.folha.uol.com.br/tec/rss091.xml", "title":"Tec"},
  "comida":{"href":"http://feeds.folha.uol.com.br/comida/rss091.xml", "title":"Comida"},
  "equilibrioesaude":{"href":"http://feeds.folha.uol.com.br/equilibrioesaude/rss091.xml", "title":"Equilíbrio"},
  "folhinha":{"href":"http://feeds.folha.uol.com.br/folhinha/rss091.xml", "title":"Folhinha"},
  "turismo":{"href":"http://feeds.folha.uol.com.br/turismo/rss091.xml", "title":"Turismo"}
  }

def main(feedstr):
  printheader()
  g=Googl()
  feed=feedparser.parse(feedstr['href'])
  items=map(lambda e: dict(date=strftime(SHORT_TIME,e.published_parsed),title=e.title,href=e.link), feed.entries)

  for item in items:
    cprint(item['date'], 'green', end=" ")
    cprint(u"\u26a1", 'yellow', end=" ")
    cprint(item['title'], 'white', end=" ")
    cprint('<%s>'%g.shorten(item['href'])['id'], 'blue')

def printheader():
  _, columns = map(int, os.popen('stty size', 'r').read().split())
  FOLHA=map(lambda e: e.rstrip(), """
tttttttt                                     
 LEE   E  ;EEGEE  EEEEL  EEEE EEEE    EE      
 LEE     EEL   EE  EEt    EE,  EE,    EEE    
 LEE  E  EE:   EEf EEt    EE,  EE,   jEEE    
 LEE,,E  EE    EEE EEt    EE,  EE,   EGEE    
 LEE  E  EE    EEE EEt    EEEEEEE,   E EEE   
 LEE  E  EE    EEE EEt    EE,  EE,  .E EEE   
 LEE     EE    EEL EEt    EE,  EE,  EEEEEE.  
 LEE     EEE   EE  EEt .E EE,  EE,  E   EEE  
LEEEEE     fEEf   LEEEEEE EEf tEEt.EEt ,EEEt""".strip().split('\n'))
  maxwidth=max(map(len, FOLHA))
  for line in FOLHA:
    print ' '*((columns - maxwidth)/2),
    print line
  print ' '*10,
  print '='*(columns - 20)
  
def printhelp():
  print 'uso:', argv[0], '[caderno]'
  print "Onde o parâmetro caderno pode ser um dos seguintes:"
  for f in sorted(FEEDS.keys()):
    print "- %s: %s" % (f, FEEDS[f]['title'])


if __name__=='__main__':
  feed='emcimadahora'
  if len(argv) == 2:
    if argv[1] == '-h':
      printhelp()
    else:
      if argv[1] not in FEEDS:
        print colored("Não foi possível achar feed:", 'red'), colored(argv[1],'red')
        printhelp()
        exit()
      else: feed=argv[1]

  main(FEEDS[feed])
