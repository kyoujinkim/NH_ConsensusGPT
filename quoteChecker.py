import re
import unicodedata

def change_quote_num(txt, addnum):
  txtNumStrList = re.findall(r'\(\*\d+', txt)
  for txtNumStr in txtNumStrList:
    txtNum = [x for x in txtNumStr if x.isdigit()]
    txtNum = int(''.join(txtNum))
    txt = txt.replace(txtNumStr, f'(*{txtNum+addnum}')
  return txt

def print_quote(rearr_context_doc, docs):
  txtNumStrList = re.findall(r'\*\d+', rearr_context_doc.page_content)
  txtNumList = []
  for txtNumStr in txtNumStrList:
    txtNum = [x for x in txtNumStr if x.isdigit()]
    txtNum = int(''.join(txtNum))
    txtNumList.append(txtNum)
  txtNumList = list(set(txtNumList))

  '''주석 표시'''
  quoteList = []
  for txtNum in txtNumList:
    doc = docs[txtNum-1]
    quote = f"(*{txtNum}){unicodedata.normalize('NFC',doc.metadata['source'].replace('/',''))}. {int(doc.metadata['page'])+1}pg"
    quoteList.append(quote)
  print('출처: ', '; '.join(quoteList))