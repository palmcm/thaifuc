import brainfuck
import sys
def toThaiNumber(number):
    th = {
  "0": "๐",
  "1": "๑",
  "2": "๒",
  "3": "๓",
  "4": "๔",
  "5": "๕",
  "6": "๖",
  "7": "๗",
  "8": "๘",
  "9": "๙",
}
    m = ""
    for i in str(number):
        m += th[i]
    return m


translate = {
    'ขวา' : 0,
    'ซ้าย' : 1,
    'เพิ่ม' : 2,
    'ลด' : 3,
    'พิมพ์' : 4,
    'ใส่' : 5,
    'ข้ามวนถ้าหากว่าช่่องนี้เป็น๐' : 6,
    'วน' : 7,
}
sym = ['>', '<', '+', '-', '.', ',', '[', ']']
thainum = {'๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙'}
tokens = {
    "๐": "0",
    "๑": "1",
    "๒": "2",
    "๓": "3",
    "๔": "4",
    "๕": "5",
    "๖": "6",
    "๗": "7",
    "๘": "8",
    "๙": "9",
  } 
  
def toArabic(number):
    return int(number)

def checkThainum(number):
    try:
        int(number)
        return True
    except:
        return False

s =  ""
stack = []
def compiler(text):
    global s
    decode = []
    line = 1
    total = 0
    tmps = 0
    message = ""
    iserr = True
    
    def get_token():
        global s
        if (len(s)==0): return ' '
        if (s[0] in thainum):
            inxn = 1
            while (inxn < len(s) and s[inxn] in thainum):
                inxn += 1
            num = s[:inxn]
            s = s[inxn:]
            return num
        
        for word in translate:
            if (s[:len(word)] == word):
                s = s[len(word):]
                return word

        if (s[0] == 'ข'):
            if (s[1] == '้'):
                raise Exception("คำสั่งไม่ถูกต้อง: หรือว่าคุณหมายถึง 'ข้ามวนถ้าหากว่าช่่องนี้เป็น๐' ?")
            else:
                raise Exception("คำสั่งไม่ถูกต้อง: หรือว่าคุณหมายถึง 'ขวา' ?")
        
        for word in translate:
            if (s[0] == word[0]): raise Exception("คำสั่งไม่ถูกต้อง: หรือว่าคุณหมายถึง '"+word+"' ?")

        raise Exception("คำสั่งไม่ถูกต้อง")


    def get_type(token):
        if (checkThainum(token)): return 8
        return translate[token]


    def parser():
        global s
        global stack
        # print(s)
        token = get_token()
        # print(f"token :{token}")
        typ = get_type(token)
        if (typ == 8): raise Exception("ไวยากรณ์ผิดพลาด: คาดหวังคำสั่งนำหน้าตัวเลข")
        n = num()
        decode.append({
            'symbol': sym[typ],
            'rep': n
        })
        if (typ == 6):
            for i in range(n): stack.append(6)
        
        if (typ == 7):
            if (n > len(stack)): raise Exception("ไวยากรณ์ผิดพลาด: มี 'วน' มากเกินไป")
            stack = stack[:-n]

    def num():
        global s
        if (len(s)>0 and checkThainum(s[0])): #lookahead
            token = get_token()
            return toArabic(token)
        return 1
        
    def extract():
        realCode = ""
        for sy in decode: 
            realCode += sy['symbol'] * (sy['rep'])
        return realCode

    try:
        for l in text.split("\n"):
                s = l.strip()
                total = len(s)
                tmps = s
                while(len(s)>0): parser()
                line += 1
        if (len(stack)>0): raise Exception("ไวยากรณ์ผิดพลาด: คาดหวังให้มี 'วน'")
        iserr=False
        message += (extract())
    except Exception as e:
        m = total - len(s)
        message += f"เกิดข้อผิดพลาดที่บรรทัด {toThaiNumber(line)}\n"
        message += ("    " + tmps[max(m-10,0):m+30]+'\n')
        message += ("    " + " "*(min(m,9)) + "^"+'\n')
        message += str(e)+'\n'
        # print(decode)

    return {
        'message': message, 
        'iserr': iserr
    }



try:
    f = open(sys.argv[1])
    res = compiler(f.read())
    if res['iserr']:
        print(res['message'])
    else:
        print(brainfuck.evaluate(res['message']))
except:
    print("ไม่สามามรถหาไฟล์ " + sys.argv[1] + "ได้")
    