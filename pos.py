from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
import xlwt
import xlrd
import re
import datetime
from kivy.uix.popup import Popup
from xlutils.copy import copy
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
data=0
scandata=0
rows=1
cols=0
gender=''
JumlahUser=1
screen_manager = ScreenManager()
waktu=datetime.datetime.now()
simpanwaktu= waktu.strftime("%d-%m-%Y %H:%M:%S")
class setNamePopup(Popup):
    def FadePopup(self):
        #self.manager.current='login'#program untuk pindah ke layout yang lain berdasarkan name window
        self.dismiss()
        print('keluar')
class WelcomeBack(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username=[]
        self.password=[]
    def loginreset(self):
        self.ids.username_field.text=''
        self.ids.pwd_field.text=''
        self.ids.money_field.text=''
        self.ids.info.text=''
    def validate_userwelcome(self):
        loc = ("data.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        for row in range(1,sheet.nrows):
            print(sheet.cell_value(row,5))
            print('\n')
            print(sheet.cell_value(row,6))
            self.username.append(sheet.cell_value(row, 5))
            self.password.append(sheet.cell_value(row,6))
            print(self.username)
            print(self.password)

        #parameter untuk mengecheck nilai pada array
        UserData=-1
        user= self.ids.username_field
        pwd= self.ids.pwd_field
        kembalian= self.ids.money_field
        info= self.ids.info

        uname=user.text
        passw=pwd.text
        UangKembalian=kembalian.text
        #Parameter untuk mengecheck format yang dimasukkan untuk uang kembalian
        xparamUangKembalian=re.findall("[a-zA-Z]",UangKembalian)
        xparamUangKembalian2= UangKembalian.startswith('0')
        if uname== '' or passw=='' or UangKembalian=='' :
            info.text='[color=#FF0000]Username ,Password,and Change  required[/color]'
        elif xparamUangKembalian or xparamUangKembalian2:
            info.text='[color=#FF0000]Masukkan jumlah uang dengan format yang benar[/color]'
        else:
            for i,c in enumerate(self.username):
                if c == uname:
                    UserData=i
            if UserData>=0:
                if uname==self.username[UserData] and passw==self.password[UserData]:
                    info.text='[color=#1764ff]Logged In Successfully!!![/color]'
                    self.manager.current='Home_Win'#program untuk pindah ke layout yang lain berdasarkan name window
                    self.ids.username_field.text=''
                    self.ids.pwd_field.text=''
                    self.ids.money_field.text=''
                    self.ids.info.text=''
                else:
                    info.text='[color=#1764ff]Invalid Username or Password!!![/color]'
                    self.ids.pwd_field.text=''
                    self.ids.money_field.text=''

            else:
                info.text='[color=#FF0000]Username and Password not registered[/color]'
                self.ids.username_field.text=''
                self.ids.pwd_field.text=''
                self.ids.money_field.text=''
        self.username=[]
        self.password=[]
class HomeWindow(Screen):
    def setName(self,*args):
        setNamePopup().open()
    def __init__(self, **kwargs):
        global d1
        super().__init__(**kwargs)
        self.JumlahProduct=[]
        self.codeItem=[]
        self.HargaBarang=[]
        #self.waktu.text=d1
        #waktuSaatIni= Label(text=d1,color=(.06,.45,.45,1))

        #self.waktu.text = time.asctime()   
           
    def barang1(self):
        global scandata
        scandata=1234
        self.list_data()
    def barang2(self):
        global scandata
        scandata=2345
        self.list_data()
    def list_data(self):
        global data
        global scandata
   
        if scandata== 0:
            scanproduct = self.ids.qty_inp_scan.text
        else:
            scanproduct=str(scandata)
        #scandata=scanproduct
        if scanproduct == '1234' or scanproduct =='2345':
            """detail_item= BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
            product_list.add_widget(detail_item) 
            if scanproduct== '1':
                simpandata=data+1
                data=simpandata
                product= Label(text='Apel',size_hint_x=.3,color=(.06,.45,.45,1))
                price= Label(text='12000',size_hint_x=.2,color=(.06,.45,.45,1))
                jumlah_barang= Label (text=str(simpandata),size_hint_x=.1,color=(.06,.45,.45,1),id="check")
                subtotal= Label(text='1',size_hint_x=.3,color=(.06,.45,.45,1))   
                detail_item.add_widget(product) 
                detail_item.add_widget(price)
                detail_item.add_widget(jumlah_barang)
                detail_item.add_widget(subtotal)
            elif scanproduct== '2':
                product= Label(text='Durian',size_hint_x=.3,color=(.06,.45,.45,1))
                price= Label(text='6000',size_hint_x=.2,color=(.06,.45,.45,1))
                jumlah_barang= Label (text='1',size_hint_x=.1,color=(.06,.45,.45,1))
                subtotal= Label(text='1',size_hint_x=.3,color=(.06,.45,.45,1))   
                detail_item.add_widget(product) 
                detail_item.add_widget(price)
                detail_item.add_widget(jumlah_barang)
                detail_item.add_widget(subtotal)"""
            if scanproduct == '1234':
                pname ="Product One"
                pprice = '3500'
                pqty = str(1)
                subtotal=3500
            elif scanproduct == '2345':
                pname ="Product Two"
                pprice = '2000'
                pqty = str(1)
                subtotal=2000
            preview = self.ids.list_item
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]
            ptarget = -1

            for i,c in enumerate(self.codeItem):
                if c == scanproduct:
                    ptarget=i
            if ptarget >=0 :
                pqty= self.JumlahProduct[ptarget]+1
                self.JumlahProduct[ptarget]=pqty
                if scanproduct=='1234':
                    subtotal=self.HargaBarang[ptarget]+3500
                    self.HargaBarang[ptarget]=subtotal
                elif scanproduct=='2345':
                    subtotal=self.HargaBarang[ptarget]+2000
                    self.HargaBarang[ptarget]=subtotal
                #regexPython berdasarkan rexpr
                #\d+ = untuk mengganti suatu digit jika + maka 1 atau lebih digit dibelakangnya
                expr ='%s\t\t\t\t%s\t\t\tx\d+\t\t\d+'%(pname,pprice)
                #regex
                rexpr = pname+'\t\t\t\t'+str(pprice)+'\t\t\tx'+str(pqty)+'\t\t'+str(subtotal)
                nu_text = re.sub(expr,rexpr,prev_text)
                #expr1 ='%s\t\t%s\t\tx\d\t\d'%(pname,pprice)
                #New_text = re.sub(expr1,rexpr,nu_text)
                #nu_text = re.sub('%s\t\t%s\t\tx\d\t\d+'%(pname,pprice), '', prev_text, 4)
                preview.text = nu_text
            else:
                self.codeItem.append(scanproduct)
                self.HargaBarang.append(subtotal)
                self.JumlahProduct.append(1)
                nu_preview = '\n'.join([prev_text,pname+'\t\t\t\t'+str(pprice)+'\t\t\tx'+pqty+'\t\t'+str(subtotal)+'\t`'])
                preview.text = nu_preview
        print(self.JumlahProduct)
        self.ids.qty_inp_scan.text=""
        #nilai scancode di nolkan kembali agar tidak mempegaruhi button sebelah scan
        scandata=0
  
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username=[]
        self.password=[]
    def loginreset(self):
        self.ids.username_field.text=''
        self.ids.pwd_field.text=''
        self.ids.money_field.text=''
        self.ids.info.text=''
    def validate_user(self):
        loc = ("data.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        for row in range(1,sheet.nrows):
            print(sheet.cell_value(row,5))
            print('\n')
            print(sheet.cell_value(row,6))
            self.username.append(sheet.cell_value(row, 5))
            self.password.append(sheet.cell_value(row,6))
            print(self.username)
            print(self.password)

        #parameter untuk mengecheck nilai pada array
        UserData=-1
        user= self.ids.username_field
        pwd= self.ids.pwd_field
        kembalian= self.ids.money_field
        info= self.ids.info

        uname=user.text
        passw=pwd.text
        UangKembalian=kembalian.text
        xparamUangKembalian=re.findall("[a-zA-Z]",UangKembalian)
        xparamUangKembalian2=1
        panjangChange=len(UangKembalian)
        if UangKembalian < '0' :
            xparamUangKembalian2=0
        elif panjangChange>1:
            if UangKembalian.startswith('0'):
                xparamUangKembalian2=0
            else:
                xparamUangKembalian2=1
        #xparamUangKembaliancond3= UangKembalian.startswith('[0][0-9]')
        if uname== '' or passw=='' or UangKembalian=='' :
            info.text='[color=#FF0000]Username ,Password,and Change  required[/color]'
        elif xparamUangKembalian or xparamUangKembalian2==0 :
            info.text='[color=#FF0000]Masukkan jumlah uang dengan format yang benar[/color]'
            self.ids.money_field.text=''
        else:
            for i,c in enumerate(self.username):
                if c == uname:
                    UserData=i
            if UserData>=0:
                if uname==self.username[UserData] and passw==self.password[UserData] and xparamUangKembalian2==1:
                    info.text='[color=#1764ff]Logged In Successfully!!![/color]'
                    self.manager.current='Home_Win'#program untuk pindah ke layout yang lain berdasarkan name window
                    self.ids.username_field.text=''
                    self.ids.pwd_field.text=''
                    self.ids.money_field.text=''
                    self.ids.info.text=''
                else:
                    info.text='[color=#1764ff]Invalid Username or Password!!![/color]'
                    self.ids.pwd_field.text=''
                    self.ids.money_field.text=''

            else:
                info.text='[color=#FF0000]Username and Password not registered[/color]'
                self.ids.username_field.text=''
                self.ids.pwd_field.text=''
                self.ids.money_field.text=''
        self.username=[]
        self.password=[]
#Register
   
class RegistWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username=[]
        self.nomorHand=[]
    def reset(self):
        self.usernameku.text=''
        self.namaAwal.text=''
        self.namaAkhir.text=''
        self.nomorTelp.text=''
        self.passwrd.text=''
        self.address.text=''
        self.confpasswr.text=''
        self.ids.info_regist.text=''
    def regist(self):
        global rows
        global cols
        global gender
        global simpanwaktu
        global JumlahUser
        info= self.ids.info_regist
        # create a workbook and add a worksheet 
        #write some data headers
        rb = xlrd.open_workbook('data.xls')
        wb = copy(rb)
        sheet = rb.sheet_by_index(0)
        w_sheet = wb.get_sheet(0)
        for row in range(1,sheet.nrows):
            print(sheet.cell_value(row,5))
            print('\n')
            print(sheet.cell_value(row,3))
            self.username.append(sheet.cell_value(row, 5))
            self.nomorHand.append(sheet.cell_value(row,3))
            #Mengecheck jumlah user account yang terdaftar
            JumlahUser+=1
            print(self.username)
            print(self.nomorHand)
        print(JumlahUser)
        emaildata= self.usernameku.text
        dataFirstName = self.namaAwal.text
        dataLastName = self.namaAkhir.text
        nomorHP = self.nomorTelp.text
        passw = self.passwrd.text
        addr = self.address.text
        confPass=self.confpasswr.text
        #check username atau nomorHP yang sama
        UserData=-1
        xparamPhoneFront=1
        for i,c in enumerate(self.username):
                if c == emaildata:
                    UserData=i
        namalengkap=dataFirstName+' '+dataLastName
        xparamname=re.findall("\d",namalengkap)
        #parameter untuk memasukkan digit nomor telp pada array
        temp = re.findall('\d', nomorHP)
        res=list(map(int,temp))
        #parameter untuk mengecheck format pada nomortelp
        if temp:
            if res[0]== 0:
                xparamPhoneFront=0
            else:
                print('tidak')
        xparamPhoneNumber=re.findall("[a-zA-Z]",nomorHP)
        xparamPasswNumber=re.findall("\d",passw)
        xparamPasswType=re.findall("[a-zA-Z]",passw)
        LengthPass=len(passw)
        lengthNumberP=len(nomorHP)
        print(xparamPhoneFront)
        if emaildata=='' or dataFirstName=='' or dataLastName=='' or gender=='' or nomorHP=='' or passw=='' or confPass=='':
            print('Harap Lengkapi Data Diri Anda')
            info.text='[color=#FF0000]Harap Lengkapi Data Diri Anda[/color]'
        elif xparamname:
            info.text='[color=#FF0000]tulis nama dengan format yang benar[/color]'
        elif lengthNumberP<10 or lengthNumberP>12:
            info.text='[color=#FF0000]jumlah digit nomor telepon anda tidak sesuai [/color]'
        elif xparamPhoneNumber:
            info.text='[color=#FF0000]Masukkan Nomor Telepon berupa angka saja[/color]'
        elif xparamPhoneFront == 1 :
            info.text='[color=#FF0000]invalid Phone Number[/color]'
        #elif xparamPasswNumber == None or xparamPasswType == None:
            #print('Password harus terdiri dari huruf dan angka')
        elif UserData >= 0:
            if emaildata==self.username[UserData]:
                info.text='[color=#FF0000]Username Telah Digunakan[/color]'
            elif nomorHP==self.nomorHand[UserData]:
                info.text='[color=#FF0000]Nomor Handphone ini telah terdaftar[/color]'
        elif confPass!= passw:
            print('ulangi password yang anda masukkan')
            info.text='[color=#FF0000]Ulangi Password Yang Anda Masukkan[/color]'
            self.passwrd.text=''
            self.confpasswr.text=''
        elif xparamPasswNumber and xparamPasswType and xparamPhoneFront==0:
            if LengthPass<8:
                print('Minimal terdapat 8 karakter')
                info.text='[color=#FF0000]password minimal terdapat 8 karakter[/color]'
            else:
                #mengecheck jumlah user yang terdaftar
                rows=JumlahUser
                w_sheet = wb.get_sheet(0)
                w_sheet.write(rows,0,simpanwaktu)
                w_sheet.write(rows,1,namalengkap)
                w_sheet.write(rows,2,addr)
                w_sheet.write(rows,3,nomorHP)
                w_sheet.write(rows,4,gender)
                w_sheet.write(rows,5,emaildata)
                w_sheet.write(rows,6,confPass)
                rows+=1
                wb.save('data.xls')
                info.text='[color=#1764ff]Success Registered!!![/color]'
                print(namalengkap+' '+addr+' '+nomorHP+' '+emaildata+' '+confPass)
                self.usernameku.text=''
                self.namaAwal.text=''
                self.namaAkhir.text=''
                self.nomorTelp.text=''
                self.passwrd.text=''
                self.address.text=''
                self.confpasswr.text=''
                self.ids.info_regist.text=''
                self.manager.current='welcome'#program untuk pindah ke layout yang lain berdasarkan name window
        else:
            print('password anda harus terdiri dari huruf dan angka')
            self.passwrd.text=''
            self.confpasswr.text=''
            info.text='[color=#FF0000]password anda harus terdiri dari huruf dan angka[/color]'
        self.username=[]
        self.nomorHand=[]
        JumlahUser=1
        #print(res)
    def checkboxMale(self,instance,value):
        global gender
        if value is True:
            gender='Male'
        else:
            gender=''
    def checkboxFemale(self,instance,value):
        global gender
        if value is True:
            gender='female'
        else:
            gender=''
    
presentation=Builder.load_file("designpos.kv")
class ForcaPOSApp(App):
    def build(self):
        return presentation
if __name__ == "__main__":
    ForcaPOSApp().run()