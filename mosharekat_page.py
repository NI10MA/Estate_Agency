#پنجره مشارکت در ساخت و ساز
#---------------------------------------------------------------
#region
#----------------------------توابع بخش مشارکت------------------------------------------
#----------------------------تابع اپدیت اسلایدر سهم----------
def update_percent(value):
    owner = int(value)
    builder = 100 - owner
    owner_label.config(text=f"مالک: {owner}%")
    builder_label.config(text=f"سازنده: {builder}%")
#------------------------تابع مدیریت فریم های مشارکت--------------
current_step = 0
def show_step(index):
    for f in frames:
        f.grid_forget()
    frames[index].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
def change_frame_melk():
    global current_step
    a = address_melk_moshrecat_entry.get("1.0", "end").strip()
    b = metraj_melk_moshrecat_entry.get().strip()
    c = arzzamin_melk_moshrecat_entry.get().strip()
    if not a or not b or not c:
        error_mosharecat.config(
            text="لطفاً همه فیلدهای مشخصات ملک را کامل کنید",
            fg="red")
        return   
    if current_step < len(frames) - 1:
        current_step += 1
        show_step(current_step)

def change_frame_malek():
    global current_step

    a=name_malek_mosharecat_entry.get("1.0","end").strip()
    b=number_malek_mosharecat_entry.get()
    c=tedad_malek_mosharecat_entry.get()
    d=name_sazandeh_moshrecat_entry.get()
    e=sazandeh_info_mosharecat_entry.get("1.0","end").strip()
    g=number_sazandeh_moshrecat_entry.get()

    if not a or not b or not c or not d or not e or not g:
        error_mosharecat.config(text="لطفاً همه فیلدهای مشخصات ملک را کامل کنید",fg="red")
        return
    else:
        error_mosharecat.config(text='')
    if current_step < len(frames) -1:
        current_step +=1
        show_step(current_step)

def change_frame_sharayet():
    global current_step

    a=mablagh_avaz_moshrecat_entry.get()
    b=tedad_tabaghe_moshrecat_entry.get()
    c=tedad_vahed_moshrecat_entry.get()
    d=sahm_tabaghe_mosharecat_malek_entry.get()
    e=sahm_vahed_moshrecat_malek_entry.get()
    f=sahm_tabaghe_mosharecat_sa_entry.get()
    g=sahm_vahed_moshrecat_sa_entry.get()
    h=tahatar_text_mosharecat_entry.get("1.0","end").strip()
    i=tahatar_value_mosharecat_entry.get()
    if not a or not b or not c or not d or not e or not f or not g or not h or not i:
        error_mosharecat.config(text="لطفاً همه فیلدهای مشخصات ملک را کامل کنید",fg="red")
        return
    else:
        error_mosharecat.config(text="")
    if current_step < len(frames) -1:
        current_step +=1
        show_step(current_step)
def tayid_final_mosharecat():#این تابع حین اتصال دیتا بیس تکمیل میشود
    a=building_time_mosharecat_entry.get()
    b=ending_time_mosharecat_entry.get()
    c=starting_time_mosharecat_entry.get()
    d=fasgh_mosharecat_entry.get()
    e=takhir_mosharecat_entry.get()
    f=end_text_mosharecat_entry.get("1.0","end").strip()
    if not a or not b or not c or not d or not e or not f:
        error_mosharecat.config(text="لطفاً همه فیلدهای مشخصات ملک را کامل کنید",fg="red")
        return
    else:
        error_mosharecat.config(text="")
    if current_step < len(frames) -1:
        current_step +=1
        show_step(current_step)
#---------------------------------توابع برگشت مشارکت-----------------------
def back_root_mosharecat():
    a = address_melk_moshrecat_entry.delete("1.0","end")
    b = metraj_melk_moshrecat_entry.delete(0,tk.END)
    c = arzzamin_melk_moshrecat_entry.delete(0,tk.END)
    d=name_malek_mosharecat_entry.delete("1.0","end")
    e=number_malek_mosharecat_entry.delete(0,tk.END)
    f=tedad_malek_mosharecat_entry.delete(0,tk.END)
    g=name_sazandeh_moshrecat_entry.delete(0,tk.END)
    h=sazandeh_info_mosharecat_entry.delete("1.0","end")
    i=number_sazandeh_moshrecat_entry.delete(0,tk.END)
    j=mablagh_avaz_moshrecat_entry.delete(0,tk.END)
    k=tedad_tabaghe_moshrecat_entry.delete(0,tk.END)
    l=tedad_vahed_moshrecat_entry.delete(0,tk.END)
    m=sahm_tabaghe_mosharecat_malek_entry.delete(0,tk.END)
    n=sahm_vahed_moshrecat_malek_entry.delete(0,tk.END)
    o=sahm_tabaghe_mosharecat_sa_entry.delete(0,tk.END)
    p=sahm_vahed_moshrecat_sa_entry.delete(0,tk.END)
    q=tahatar_text_mosharecat_entry.delete("1.0","end")
    r=tahatar_value_mosharecat_entry.delete(0,tk.END) 
    t=building_time_mosharecat_entry.delete(0,tk.END)
    u=ending_time_mosharecat_entry.delete(0,tk.END)
    v=starting_time_mosharecat_entry.delete(0,tk.END)
    w=fasgh_mosharecat_entry.delete(0,tk.END)
    x=takhir_mosharecat_entry.delete(0,tk.END)
    y=end_text_mosharecat_entry.delete("1.0","end")

    mosharecat_window.withdraw()
    root.deiconify()
###################################################
#---------------------------------------------------
#-----------تابع برگشت فریم ih------------------
def back_to_melk():#برگشت فریم مالک به ملک
    global current_step

    if current_step > 0:
        current_step -= 1
        show_step(current_step)
def back_to_malek():#برگشت فریم شرایط به مالک
    global current_step

    if current_step > 0:
        current_step -= 1
        show_step(current_step)
def back_to_sharayet():#برگشت فریم ساخت به شرایط
    global current_step

    if current_step > 0:
        current_step -= 1
        show_step(current_step)
#------------------------------------------------------------------
#######################################################
#---------------------------------تابع سوییچ بین نوع مشارکت---------------------------
def change_type_mosharecat(event):
    combo_value = sharayet_mosharecat_type_combo.get()

    if combo_value == "مشارکت در ساخت":
        mablagh_avaz_moshrecat_entry.config(state="disabled")
        tahatar_text_mosharecat_entry.config(state="disabled")
        tahatar_value_mosharecat_entry.config(state="disabled")

    elif combo_value == "مشارکت با بلاعوض":
         mablagh_avaz_moshrecat_entry.config(state="normal")
         tahatar_text_mosharecat_entry.config(state="disabled")
         tahatar_value_mosharecat_entry.config(state="disabled")

    elif combo_value == "مشارکت + تهاتر":
         mablagh_avaz_moshrecat_entry.config(state="disabled")
         tahatar_text_mosharecat_entry.config(state="normal")
         tahatar_value_mosharecat_entry.config(state="normal")

#region
mosharecat_window=tk.Toplevel(root,background="#021728")
mosharecat_window.geometry("800x680")
mosharecat_window.title("پنجره مشارکت در ساخت و ساز")
mosharecat_window.pack_propagate(False)
mosharecat_window.rowconfigure(0, weight=1)
mosharecat_window.columnconfigure(0, weight=1)
mosharecat_window.withdraw()

#گرید کردن تمام  فریم ها--------------
melk_mosharecat_data=tk.Frame(mosharecat_window,bg="#021728",height=600,width=1000)
malek_mosharecat_frame=tk.Frame(mosharecat_window,bg="#021728",height=600,width=1000)
sharayet_mosharecat_frame=tk.Frame(mosharecat_window,bg="#021728",height=600,width=1000)
bulid_mosharecat_frame=tk.Frame(mosharecat_window,bg="#021728",height=600,width=1000)
frames=[melk_mosharecat_data,malek_mosharecat_frame,sharayet_mosharecat_frame,bulid_mosharecat_frame]
for f in frames:
    f.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

#melk_mosharecat_data=tk.Frame(mosharecat_window,bg="#b2c4ff",height=600,width=1000)
#melk_mosharecat_data.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# ستون‌ها برای گسترش Entry/Combobox
melk_mosharecat_data.columnconfigure(0, weight=1)
melk_mosharecat_data.columnconfigure(1, weight=0)

melk_mosharecat_data.pack_propagate(False)

type_melk_mosharecat=tk.Label(melk_mosharecat_data,text="نوع ملک",bg="#021728" ,fg="#ffffff",font=("Shabnam",11),width=10)
type_melk_mosharecat.grid(padx=5,pady=10,row=0,column=1)

type_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
type_melk_mosharecat_combo["values"]=(' ',"کلنگی","زمین","ویلایی","آپارتمان")
type_melk_mosharecat_combo.set(' ')
type_melk_mosharecat_combo.grid(padx=5,pady=10,row=0,column=0)

address_melk_moshrecat=tk.Label(melk_mosharecat_data,text="آدرس دقیق",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
address_melk_moshrecat.grid(padx=5,pady=10,row=1,column=1)

address_melk_moshrecat_entry=scrolledtext.ScrolledText(melk_mosharecat_data,width=30,height=8)
address_melk_moshrecat_entry.grid(padx=5,pady=2,row=1,column=0)

metraj_melk_moshrecat=tk.Label(melk_mosharecat_data,text="متراژ",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
metraj_melk_moshrecat.grid(padx=5,pady=10,row=2,column=1)

metraj_melk_moshrecat_entry=tk.Entry(melk_mosharecat_data,bg="#ffffff",fg="#000000")
metraj_melk_moshrecat_entry.grid(padx=5,pady=10,row=2,column=0)

arzzamin_melk_moshrecat=tk.Label(melk_mosharecat_data,text="عرض زمین",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
arzzamin_melk_moshrecat.grid(padx=5,pady=10,row=3,column=1)

arzzamin_melk_moshrecat_entry=tk.Entry(melk_mosharecat_data,bg="#ffffff",fg="#000000")
arzzamin_melk_moshrecat_entry.grid(padx=5,pady=10,row=3,column=0)

located_melk_mosharecat=tk.Label(melk_mosharecat_data,text="موقعیت ملک",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
located_melk_mosharecat.grid(padx=5,pady=10,row=4,column=1)

located_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
located_melk_mosharecat_combo["values"]=(' شمالی',"جنوبی","دونبش","سرنبش")
located_melk_mosharecat_combo.set( "شمالی")
located_melk_mosharecat_combo.grid(padx=5,pady=10,row=4,column=0)

karbary_melk_mosharecat=tk.Label(melk_mosharecat_data,text="کاربری",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
karbary_melk_mosharecat.grid(padx=5,pady=10,row=5,column=1)

karbary_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
karbary_melk_mosharecat_combo["values"]=("مسکونی","تجاری","هردو")
karbary_melk_mosharecat_combo.set( "مسکونی")
karbary_melk_mosharecat_combo.grid(padx=5,pady=10,row=5,column=0)

sanad_melk_mosharecat=tk.Label(melk_mosharecat_data,text="وضعیت سند",bg="#021728",fg="#ffffff",font=("Shabnam",11),width=10)
sanad_melk_mosharecat.grid(padx=5,pady=10,row=6,column=1)

sanad_melk_mosharecat_combo=ttk.Combobox(melk_mosharecat_data)
sanad_melk_mosharecat_combo["values"]=("تک برگ","قول نامه","ثبتی","نامشخص")
sanad_melk_mosharecat_combo.set( "تک برگ")
sanad_melk_mosharecat_combo.grid(padx=5,pady=10,row=6,column=0)

edame_moshrecat_melk1=tk.Button(melk_mosharecat_data,text="ادامه",background="#00BFFF",fg="#000000",width=10,height=2,command=change_frame_melk)
edame_moshrecat_melk1.place(x=200,y=500)

back_to_root=tk.Button(melk_mosharecat_data,text="برگشت به صفحه اصلی",command=back_root_mosharecat,background="#00BFFF",fg="#000000",width=17,height=2)
back_to_root.place(x=50,y=500)

#---------------------------------------------------------------------------
#---------------------------- و سازنده فریم دوم مشخصات مالک--------------------------------------
#malek_mosharecat_frame=tk.Frame(mosharecat_window,bg="#b2c4ff",height=600,width=1000)
#malek_mosharecat_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

malek_mosharecat_frame.columnconfigure(0, weight=1)
malek_mosharecat_frame.columnconfigure(1, weight=0)

malek_mosharecat_frame.pack_propagate(False)

name_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="نام مالک/مالکان",bg="#efefef" ,fg="black",width=13)
name_malek_mosharecat.grid(padx=5,pady=10,row=0,column=1)

name_malek_mosharecat_entry=scrolledtext.ScrolledText(malek_mosharecat_frame,width=30,height=5)
name_malek_mosharecat_entry.grid(padx=5,pady=10,row=0,column=0)

number_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="شماره تماس مالک/نماینده ",bg="#efefef" ,fg="black",width=18)
number_malek_mosharecat.grid(padx=5,pady=10,row=1,column=1)

number_malek_mosharecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
number_malek_mosharecat_entry.grid(padx=5,pady=10,row=1,column=0)

tedad_malek_mosharecat=tk.Label(malek_mosharecat_frame,text="تعداد مالک",bg="#efefef" ,fg="black",width=13)
tedad_malek_mosharecat.grid(padx=5,pady=10,row=2,column=1)

tedad_malek_mosharecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
tedad_malek_mosharecat_entry.grid(padx=5,pady=10,row=2,column=0)

type_malekiyat_mosharecat=tk.Label(malek_mosharecat_frame,text="نوع مالکیت",bg="#efefef" ,fg="black",width=13)
type_malekiyat_mosharecat.grid(padx=5,pady=10,row=3,column=1)

type_malekiyat_mosharecat_combo=ttk.Combobox(malek_mosharecat_frame)
type_malekiyat_mosharecat_combo["values"]=("شش دانگ","مشاع")
type_malekiyat_mosharecat_combo.set( "شش دانگ")
type_malekiyat_mosharecat_combo.grid(padx=5,pady=10,row=3,column=0)

#بعد میتوان درصد مشارکت هم اضافه کرد ولی باید به تایید جمع برسه
#-------------قسمت مشخصات سازنده-----------------------
#این فیلدها اجباری نیست چراکه ممکنه هن.ز سازنده تعیین نشده باشه
name_sazandeh_moshrecat=tk.Label(malek_mosharecat_frame,text="نام سازنده/شرکت",bg="#efefef" ,fg="black",width=13)
name_sazandeh_moshrecat.grid(padx=5,pady=10,row=4,column=1)

name_sazandeh_moshrecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
name_sazandeh_moshrecat_entry.grid(padx=5,pady=10,row=4,column=0)

number_sazandeh_moshrecat=tk.Label(malek_mosharecat_frame,text="شماره تماس",bg="#efefef" ,fg="black",width=13)
number_sazandeh_moshrecat.grid(padx=5,pady=10,row=5,column=1)

number_sazandeh_moshrecat_entry=tk.Entry(malek_mosharecat_frame,bg="#e5e5e5",fg="black")
number_sazandeh_moshrecat_entry.grid(padx=5,pady=10,row=5,column=0)

sazandeh_info_moshrecat=tk.Label(malek_mosharecat_frame,text="سابقه کوتاه سازنده",bg="#efefef" ,fg="black",width=15)
sazandeh_info_moshrecat.grid(padx=5,pady=10,row=6,column=1)

sazandeh_info_mosharecat_entry=scrolledtext.ScrolledText(malek_mosharecat_frame,width=30,height=8)
sazandeh_info_mosharecat_entry.grid(padx=5,pady=10,row=6,column=0)

edame_moshrecat_malek=tk.Button(malek_mosharecat_frame,text="ادامه",background="#079BDB",fg="#ffffff",width=8,command=change_frame_malek)
edame_moshrecat_malek.place(x=200,y=500)

back_to_melk_mosharecat=tk.Button(malek_mosharecat_frame,text="برگشت ",command=back_to_melk,background="#079BDB",fg="#ffffff",width=17)
back_to_melk_mosharecat.place(x=50,y=500)
#---------------------------------------------------------------------------
#---------------------------- شرایط مشارکت در ساخت---------------
#sharayet_mosharecat_frame=tk.Frame(mosharecat_window,bg="#b2c4ff",height=750,width=1000)
#sharayet_mosharecat_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

sharayet_mosharecat_frame.columnconfigure(0, weight=1)
sharayet_mosharecat_frame.columnconfigure(1, weight=0)
sharayet_mosharecat_frame.pack_propagate(False)

sharayet_mosharecat_type=tk.Label(sharayet_mosharecat_frame,text="نوع مشارکت",bg="#efefef" ,fg="black",width=13)
sharayet_mosharecat_type.grid(padx=5,pady=10,row=0,column=4)


sharayet_mosharecat_type_combo=ttk.Combobox(sharayet_mosharecat_frame)
sharayet_mosharecat_type_combo["values"]=("مشارکت در ساخت","مشارکت با بلاعوض","مشارکت + تهاتر")
sharayet_mosharecat_type_combo.set( "مشارکت در ساخت")
sharayet_mosharecat_type_combo.grid(padx=10,pady=10,row=0,column=3)
sharayet_mosharecat_type_combo.bind("<<ComboboxSelected>>",change_type_mosharecat)


owner_percent = tk.IntVar(value=50)
owner_slider = tk.Scale(sharayet_mosharecat_frame,from_=0,to=100,orient="horizontal",variable=owner_percent,
    label="درصد سهم مالک",
    length=300)
owner_slider.grid(row=1, column=3, padx=10, pady=10, columnspan=2)

owner_label = tk.Label(sharayet_mosharecat_frame,text="مالک: 50%",fg="black",bg="#efefef")
owner_label.grid(row=1, column=2,padx=10,pady=10)

builder_label = tk.Label(sharayet_mosharecat_frame,text="سازنده: 50%",fg="black",bg="#efefef")
builder_label.grid(row=1, column=1,padx=10,pady=10)

owner_slider.config(command=update_percent)
avardeh_malek_moshrecat=tk.Label(sharayet_mosharecat_frame,text="اورده مالک",fg="black",bg="#efefef")
avardeh_malek_moshrecat.grid(row=2, column=4,padx=10,pady=10)

avardeh_malek_zamin_melk=tk.Checkbutton(sharayet_mosharecat_frame,text="زمین/ملک",fg="black",bg="#efefef")
avardeh_malek_zamin_melk.grid(row=2, column=3,padx=10,pady=10)

parvaneh_malek_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="پروانه ساخت",fg="black",bg="#efefef")
parvaneh_malek_moshrecat.grid(row=2, column=2,padx=10,pady=10)

mony_malek_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="پول نقد",fg="black",bg="#efefef")
mony_malek_moshrecat.grid(row=2,column=1,padx=10,pady=10)

avardeh_sazandeh_moshrecat=tk.Label(sharayet_mosharecat_frame,text="آورده سازنده",fg="black",bg="#efefef")
avardeh_sazandeh_moshrecat.grid(row=3, column=4,padx=10,pady=10)

mojavez_sazandeh_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="اخذ مجوز ها",fg="black",bg="#efefef")
mojavez_sazandeh_moshrecat.grid(row=3, column=3,padx=10,pady=10)

cust_sazandeh_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="هزینه ساخت ",fg="black",bg="#efefef")
cust_sazandeh_moshrecat.grid(row=3, column=2,padx=10,pady=10)

control_sazandeh_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="مدیریت پروژه",fg="black",bg="#efefef")
control_sazandeh_moshrecat.grid(row=3, column=1,padx=10,pady=10)

tajhiz_sazandeh_moshrecat=tk.Checkbutton(sharayet_mosharecat_frame,text="تجهیز پروژه",fg="black",bg="#efefef")
tajhiz_sazandeh_moshrecat.grid(row=3, column=0,padx=10,pady=10)

mablagh_avaz_moshrecat=tk.Label(sharayet_mosharecat_frame,text="مبلغ بلاعوض",fg="black",bg="#efefef")
mablagh_avaz_moshrecat.grid(row=4, column=4,padx=10,pady=10)

mablagh_avaz_moshrecat_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="white",width=13)
mablagh_avaz_moshrecat_entry.grid(row=4, column=3,padx=10,pady=10)

time_mablagh_mosharecat=tk.Label(sharayet_mosharecat_frame,text="زمان پرداخت",fg="black",bg="#efefef")
time_mablagh_mosharecat.grid(row=5, column=4,padx=10,pady=10)

time_mablagh_mosharecat_combo=ttk.Combobox(sharayet_mosharecat_frame)
time_mablagh_mosharecat_combo["values"]=( "حین عقد قرار داد","مرحله ای")
time_mablagh_mosharecat_combo.set( "حین عقد قرار داد")
time_mablagh_mosharecat_combo.grid(padx=10,pady=10,row=5,column=3)

taraf_mablagh_mosharecat=tk.Label(sharayet_mosharecat_frame,text=":پرداخت به",fg="black",bg="#efefef")
taraf_mablagh_mosharecat.grid(row=5, column=2,padx=10,pady=10)

taraf_mablagh_mosharecat_combo=ttk.Combobox(sharayet_mosharecat_frame)
taraf_mablagh_mosharecat_combo["values"]=( "مالک","مالکین")
taraf_mablagh_mosharecat_combo.set( "مالک")
taraf_mablagh_mosharecat_combo.grid(padx=10,pady=10,row=5,column=1)

tedad_tabaghe_mosharecat=tk.Label(sharayet_mosharecat_frame,text="تعداد طبقات قابل ساخت",fg="black",bg="#efefef",width=18)
tedad_tabaghe_mosharecat.grid(row=6, column=4,padx=10,pady=10)

tedad_tabaghe_moshrecat_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
tedad_tabaghe_moshrecat_entry.grid(row=6, column=3,padx=10,pady=10)

tedad_vahed_mosharecat=tk.Label(sharayet_mosharecat_frame,text="تعداد واحد",fg="black",bg="#efefef",width=18)
tedad_vahed_mosharecat.grid(row=6, column=2,padx=10,pady=10)

tedad_vahed_moshrecat_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
tedad_vahed_moshrecat_entry.grid(row=6, column=1,padx=10,pady=10)

sahm_tabaghe_mosharecat_malek=tk.Label(sharayet_mosharecat_frame,text="سهم طبقه مالک",fg="black",bg="#efefef",width=18)
sahm_tabaghe_mosharecat_malek.grid(row=7, column=4,padx=10,pady=10)

sahm_tabaghe_mosharecat_malek_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
sahm_tabaghe_mosharecat_malek_entry.grid(row=7, column=3,padx=10,pady=10)

sahm_vahed_mosharecat_malek=tk.Label(sharayet_mosharecat_frame,text="سهم واحد مالک",fg="black",bg="#efefef",width=18)
sahm_vahed_mosharecat_malek.grid(row=7, column=2,padx=10,pady=10)

sahm_vahed_moshrecat_malek_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
sahm_vahed_moshrecat_malek_entry.grid(row=7, column=1,padx=10,pady=10)

sahm_tabaghe_mosharecat_sa=tk.Label(sharayet_mosharecat_frame,text="سهم طبقه سازنده",fg="black",bg="#efefef",width=18)
sahm_tabaghe_mosharecat_sa.grid(row=8, column=4,padx=10,pady=10)

sahm_tabaghe_mosharecat_sa_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
sahm_tabaghe_mosharecat_sa_entry.grid(row=8, column=3,padx=10,pady=10)

sahm_vahed_mosharecat_sa=tk.Label(sharayet_mosharecat_frame,text="سهم واحد سازنده",fg="black",bg="#efefef",width=18)
sahm_vahed_mosharecat_sa.grid(row=8, column=2,padx=10,pady=10)

sahm_vahed_moshrecat_sa_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="#efefef",width=13)
sahm_vahed_moshrecat_sa_entry.grid(row=8, column=1,padx=10,pady=10)

tahatar_text_mosharecat=tk.Label(sharayet_mosharecat_frame,text="توضیح تهاتر",fg="black",bg="#efefef",width=18)
tahatar_text_mosharecat.grid(row=9, column=4,padx=10,pady=10)

tahatar_text_mosharecat_entry=scrolledtext.ScrolledText(sharayet_mosharecat_frame,width=30,height=5)
tahatar_text_mosharecat_entry.grid(padx=11,pady=10,row=9,column=3)

tahatar_value_mosharecat=tk.Label(sharayet_mosharecat_frame,text="ارزش تقریبی تهاتر",fg="black",bg="#efefef",width=18)
tahatar_value_mosharecat.grid(row=9, column=2,padx=10,pady=10)

tahatar_value_mosharecat_entry=tk.Entry(sharayet_mosharecat_frame,fg="black",bg="white",width=13)
tahatar_value_mosharecat_entry.grid(row=9, column=1,padx=10,pady=10)

edame_moshrecat_sharayet=tk.Button(sharayet_mosharecat_frame,text="ادامه",background="#079BDB",fg="#ffffff",width=8,command=change_frame_sharayet)
edame_moshrecat_sharayet.grid(row=10, column=2,padx=10,pady=10)

back_to_malek_mosharecat=tk.Button(sharayet_mosharecat_frame,text="برگشت ",command=back_to_malek,background="#079BDB",fg="#ffffff",width=17)
back_to_malek_mosharecat.grid(row=10, column=1,padx=10,pady=10)
change_type_mosharecat(None)
#--------------------------------------------------------------------------------
#------------------------------فریم ساخت---------------------------------------
#bulid_mosharecat_frame=tk.Frame(mosharecat_window,bg="#b2c4ff",height=750,width=1000)
#bulid_mosharecat_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

bulid_mosharecat_frame.columnconfigure(0, weight=1)
bulid_mosharecat_frame.columnconfigure(1, weight=0)
bulid_mosharecat_frame.pack_propagate(False)

level_bulid_mosharecat=tk.Label(bulid_mosharecat_frame,text="کیفیت ساخت",fg="black",bg="#efefef",width=18)
level_bulid_mosharecat.grid(row=0, column=3,padx=10,pady=10)

level_bulid_mosharecat_combo=ttk.Combobox(bulid_mosharecat_frame)
level_bulid_mosharecat_combo["value"]=("معمولی","خوب","لوکس")
level_bulid_mosharecat_combo.set("معمولی")
level_bulid_mosharecat_combo.grid(row=0, column=2,padx=10,pady=10)

scelet_bulid_mosharecat=tk.Label(bulid_mosharecat_frame,text="نوع اسکلت",fg="black",bg="#efefef",width=18)
scelet_bulid_mosharecat.grid(row=0, column=1,padx=10,pady=10)

scelet_bulid_mosharecat_combo=ttk.Combobox(bulid_mosharecat_frame)
scelet_bulid_mosharecat_combo["value"]=("بتنی","فلزی")
scelet_bulid_mosharecat_combo.set("فلزی")
scelet_bulid_mosharecat_combo.grid(row=0, column=0,padx=10,pady=10)

nama_bulid_mosharecat=tk.Label(bulid_mosharecat_frame,text="نوع نما",fg="black",bg="#efefef",width=18)
nama_bulid_mosharecat.grid(row=1, column=3,padx=10,pady=10)

nama_bulid_mosharecat_combo=ttk.Combobox(bulid_mosharecat_frame)
nama_bulid_mosharecat_combo["value"]=("سنگی","شیشه","ترکیبی")
nama_bulid_mosharecat_combo.set("سنگی")
nama_bulid_mosharecat_combo.grid(row=1, column=2,padx=10,pady=10)

number_parking_mosharecat=tk.Label(bulid_mosharecat_frame,text="تعداد پارکینگ",fg="black",bg="#efefef",width=18)
number_parking_mosharecat.grid(row=1, column=1,padx=10,pady=10)

number_parking_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
number_parking_mosharecat_entry.grid(row=1, column=0,padx=10,pady=10)

anbari_build_mosharecat=tk.Checkbutton(bulid_mosharecat_frame,text="انباری",image=warehouse_pic)
anbari_build_mosharecat.grid(row=2, column=3,padx=10,pady=10)

elavator_build_mosharecat=tk.Checkbutton(bulid_mosharecat_frame,text="آسانسور",image=elvator_pic)
elavator_build_mosharecat.grid(row=2, column=2,padx=10,pady=10)

building_time_mosharecat=tk.Label(bulid_mosharecat_frame,text="زمان ساخت به ماه",fg="black",bg="#efefef",width=18)
building_time_mosharecat.grid(row=3, column=3,padx=10,pady=10)

building_time_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
building_time_mosharecat_entry.grid(row=3, column=2,padx=10,pady=10)

starting_time_mosharecat=tk.Label(bulid_mosharecat_frame,text="زمان شروع",fg="black",bg="#efefef",width=18)
starting_time_mosharecat.grid(row=3, column=1,padx=10,pady=10)

starting_time_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
starting_time_mosharecat_entry.grid(row=3, column=0,padx=10,pady=10)

ending_time_mosharecat=tk.Label(bulid_mosharecat_frame,text="زمان پایان تقریبی",fg="black",bg="#efefef",width=18)
ending_time_mosharecat.grid(row=4, column=3,padx=10,pady=10)

ending_time_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
ending_time_mosharecat_entry.grid(row=4, column=2,padx=10,pady=10)

takhir_mosharecat=tk.Label(bulid_mosharecat_frame,text="جریمه تاخیر",fg="black",bg="#efefef",width=18)
takhir_mosharecat.grid(row=4, column=1,padx=10,pady=10)

takhir_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
takhir_mosharecat_entry.grid(row=4, column=0,padx=10,pady=10)

fasgh_mosharecat=tk.Label(bulid_mosharecat_frame,text="جریمه فسخ",fg="black",bg="#efefef",width=18)
fasgh_mosharecat.grid(row=5, column=3,padx=10,pady=10)

fasgh_mosharecat_entry=tk.Entry(bulid_mosharecat_frame,fg="black",bg="#efefef",width=13)
fasgh_mosharecat_entry.grid(row=5, column=2,padx=10,pady=10)

davari_mosharecat=tk.Label(bulid_mosharecat_frame,text="داوری و حل اختلاف",fg="black",bg="#efefef",width=20)
davari_mosharecat.grid(row=5, column=1,padx=10,pady=10)

davari_mosharecat_combo=ttk.Combobox(bulid_mosharecat_frame)
davari_mosharecat_combo["value"]=("داوری","دادگاه")
davari_mosharecat_combo.set("دادگاه")
davari_mosharecat_combo.grid(row=5, column=0,padx=10,pady=10)

mozakereh_mosharecat=tk.Label(bulid_mosharecat_frame,text="شرایط مذاکره",fg="black",bg="#efefef",width=20)
mozakereh_mosharecat.grid(row=6, column=3,padx=10,pady=10)

mozakereh_mosharecat_combo=ttk.Combobox(bulid_mosharecat_frame)
mozakereh_mosharecat_combo["value"]=("دارد","ندارد")
mozakereh_mosharecat_combo.set("دارد")
mozakereh_mosharecat_combo.grid(row=6, column=2,padx=10,pady=10)

end_text_mosharecat=tk.Label(bulid_mosharecat_frame,text="توضیحات تکمیلی",fg="black",bg="#efefef",width=20)
end_text_mosharecat.grid(row=7, column=3,padx=10,pady=10)

end_text_mosharecat_entry=scrolledtext.ScrolledText(bulid_mosharecat_frame,width=35,height=10)
end_text_mosharecat_entry.grid(padx=10,pady=10,row=7,column=2)

tayied_mosharecat=tk.Button(bulid_mosharecat_frame,text="ثبت نهایی",background="#079BDB",fg="#ffffff",width=8,command=tayid_final_mosharecat)
tayied_mosharecat.grid(row=8, column=2,padx=10,pady=10)

back_to_sharayet_mosharecat=tk.Button(bulid_mosharecat_frame,text="برگشت ",command=back_to_sharayet,background="#079BDB",fg="#ffffff",width=17)
back_to_sharayet_mosharecat.grid(row=8, column=1,padx=10,pady=10)

error_mosharecat=tk.Label(mosharecat_window,fg="red",font=("Arial",14))
error_mosharecat.pack()

#endregion