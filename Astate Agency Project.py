#-------------------------------------  کتابخانه ها   --------------------
#region
import tkinter as tk
import mysql.connector
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox,font,scrolledtext
import subprocess
import os
from openpyxl import Workbook
import datetime
from tkinter import filedialog
from docxtpl import DocxTemplate
from tkinter import filedialog
import shutil


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mmmm9905",#   entry  در ادرس ها   تبدیل بهtext شود      entry==>text
        #database="state_agency"
    )
#endregion
#---#----#----#----#----#----------  توابع   ----------#----#----#----#-------------
#-------------------------تابع بستن پروژه-----------------
#region
def close_window():#این تابع بعد از اتصال دیتابیس تکمیل مشود 
    response=messagebox.askyesno("تایید خروج","آیا از خارج شدن اطمینان دارید؟")
    if response:
        root.destroy()
    else:
        return
#endregion
# -------------------------------------تابع فراخوانی ادرس با دکمه-----------
#region
def open_file_folder():
    file_path = filedialog.askopenfilename()
    if file_path:
        folder_path = os.path.dirname(file_path)
        subprocess.run(['explorer', '/select,', file_path])
#endregion
#  ------------------------------------------تابع انتخاب فایل عکس------------
#region
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        os.startfile(file_path)
#endregion
#---------------------------تابع خروجی گزارش اکسل-----------
#region
def show_message(label, text):
    label.config(text=text)
    label.update_idletasks()


def export_excel(sql, sheet_title, file_prefix, label):
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("USE state_agency")
        cursor.execute(sql)

        data = cursor.fetchall()

        if not data:
            show_message(label, "اطلاعاتی برای خروجی وجود ندارد.")
            return
        column_names = [desc[0] for desc in cursor.description]
        workbook = Workbook()
        sheet = workbook.active  # توجه: active نه activess
        sheet.title = sheet_title

        for col_num, title in enumerate(column_names, 1):
            sheet.cell(row=1, column=col_num, value=title)

        for row_num, row in enumerate(data, 2):
            for col_num, value in enumerate(row, 1):
                sheet.cell(row=row_num, column=col_num, value=value)

        file_name = f"{file_prefix}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"

        file_path = filedialog.asksaveasfilename(
            title="ذخیره فایل اکسل",
            initialfile=file_name,
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")]
        )

        if file_path:
            workbook.save(file_path)
            show_message(label, "فایل با موفقیت ذخیره شد.")

        cursor.close()
        db.close()

    except Exception as e:
        show_message(label, f"خطا: {str(e)}")
def excel_gozaresh_maskoni():
    value = gozaresh_file_combo_maskoni.get()

    if value == "گزارش فایل اجاره":
        export_excel(
            "SELECT * FROM sabt_ejareh_maskoni",
            "جدول اجاره مسکونی",
            "گزارش اجاره مسکونی",
            error_label_maskoni
        )

    elif value == "گزارش فایل فروش":
        export_excel(
            "SELECT * FROM sabt_forosh_maskoni",
            "جدول فروش مسکونی",
            "گزارش فروش مسکونی",
            error_label_maskoni
        )

    elif value == "گزارش فایل درخواست اجاره":
        export_excel(
            "SELECT * FROM sabt_darkhast_ejareh_maskoni",
            "جدول درخواست اجاره مسکونی",
            "گزارش درخواست اجاره مسکونی",
            error_label_maskoni
        )

    elif value == "گزارش فایل درخواست خرید":
        export_excel(
            "SELECT * FROM sabt_darkhast_kharid_maskoni",
            "جدول درخواست خرید مسکونی",
            "گزارش درخواست خرید مسکونی",
            error_label_maskoni
        )
def excel_gozaresh_edari_tejari():
    value = gozaresh_file_combo_edari_tejari.get()

    if value == "گزارش فایل اجاره":
        export_excel(
            "SELECT * FROM sabt_ejareh_edari_tejari",
            "جدول اجاره اداری_تجاری",
            "گزارش اجاره اداری_تجاری",
            error_label_edari_tejari
        )

    elif value == "گزارش فایل فروش":
        export_excel(
            "SELECT * FROM sabt_forosh_edari_tejari",
            "جدول فروش اداری_تجاری",
            "گزارش فروش اداری_تجاری",
            error_label_edari_tejari
        )

    elif value == "گزارش فایل درخواست اجاره":
        export_excel(
            "SELECT * FROM sabt_darkhast_ejareh_edari_tejari",
            "جدول درخواست اجاره اداری_تجاری",
            "گزارش درخواست اجاره اداری_تجاری",
            error_label_edari_tejari
        )

    elif value == "گزارش فایل درخواست خرید":
        export_excel(
            "SELECT * FROM sabt_darkhast_kharid_edari_tejari",
            "جدول درخواست خرید اداری_تجاری",
            "گزارش درخواست خرید اداری_تجاری",
            error_label_edari_tejari
        )
def excel_gozaresh_bagh_zamin():
    value = gozaresh_file_combo_bagh_zamin.get()

    if value == "گزارش فایل اجاره باغ":
        export_excel(
            "SELECT * FROM ejareh_bagh",
            "جدول اجاره باغ",
            "گزارش اجاره باغ",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل فروش باغ":
        export_excel(
            "SELECT * FROM forosh_bagh",
            "جدول فروش باغ",
            "گزارش فروش باغ",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل درخواست اجاره باغ":
        export_excel(
            "SELECT * FROM darkhast_ejareh_bagh",
            "جدول درخواست اجاره باغ",
            "گزارش درخواست باغ",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل درخواست خرید باغ":
        export_excel(
            "SELECT * FROM darkhast_kharid_bagh",
            "جدول درخواست خرید باغ",
            "گزارش درخواست خرید باغ",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل اجاره زمین":
        export_excel(
            "SELECT * FROM ejareh_zamin",
            "جدول اجاره زمین",
            "گزارش اجاره زمین",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل فروش زمین":
        export_excel(
            "SELECT * FROM forosh_zamin",
            "جدول فروش زمین",
            "گزارش فروش زمین",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل درخواست اجاره زمین":
        export_excel(
            "SELECT * FROM darkhast_ejareh_zamin",
            "جدول درخواست اجاره زمین",
            "گزارش درخواست زمین",
            error_label_bagh_zamin
        )

    elif value == "گزارش فایل درخواست خرید زمین":
        export_excel(
            "SELECT * FROM darkhast_kharid_zamin",
            "جدول درخواست خرید زمین",
            "گزارش درخواست خرید زمین",
            error_label_bagh_zamin
        )
def excel_gozaresh_kargah():
    value = gozaresh_file_combo_kargah.get()

    if value == "گزارش فایل اجاره":
        export_excel(
            "SELECT * FROM sabt_ejareh_kargah",
            "جدول اجاره کارگاه",
            "گزارش اجاره کارگاه",
            error_label_kargah
        )

    elif value == "گزارش فایل فروش":
        export_excel(
            "SELECT * FROM sabt_forosh_kargah",
            "جدول فروش کارگاه",
            "گزارش فروش کارگاه",
            error_label_kargah
        )

    elif value == "گزارش فایل درخواست اجاره":
        export_excel(
            "SELECT * FROM sabt_darkhast_ejareh_kargah",
            "جدول درخواست اجاره کارگاه",
            "گزارش درخواست اجاره کارگاه",
            error_label_kargah
        )

    elif value == "گزارش فایل درخواست خرید":
        export_excel(
            "SELECT * FROM sabt_darkhast_kharid_kargah",
            "جدول درخواست خرید کارگاه",
            "گزارش درخواست خرید کارگاه",
            error_label_kargah
        )
def gharardadeha():
    pass
#endregion
#------------------------------تابع خروجی فایل ورد قرارداد-----------------
#region
def creat_word_gharardad():
    try:
        property_type = type_melk_gharardad_combo.get()
        contract_type = type_gharardad_combo.get()
        party_one = name_shakhs_aval_gharardad_entry.get()
        party_two = name_shakhs_dovom_gharardad_entry.get()
        description = tozih_gharardad_entry.get("1.0", "end-1c")
        # اعتبارسنجی
        if property_type == "":
            messagebox.showwarning("خطا", "نوع ملک را انتخاب کنید")
            return
        if contract_type == "":
            messagebox.showwarning("خطا", "نوع قرارداد را انتخاب کنید")
            return
        if party_one == "":
            messagebox.showwarning("خطا", "نام طرف اول را وارد کنید")
            return
        if party_two == "":
            messagebox.showwarning("خطا", "نام طرف دوم را وارد کنید")
            return
        # اتصال دیتابیس
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gharardad(
            id INT AUTO_INCREMENT PRIMARY KEY,
            tracking_code VARCHAR(30),
            property_type VARCHAR(40),
            contract_type VARCHAR(40),
            party_one VARCHAR(40),
            party_two VARCHAR(40),
            description VARCHAR(225)
        )
        """)
        # ثبت اولیه قرارداد
        cursor.execute("""
        INSERT INTO gharardad
        (property_type,contract_type,party_one,party_two,description
        )
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            property_type,
            contract_type,
            party_one,
            party_two,
            description
        ))

        db.commit()

        # تولید کد رهگیری

        last_id = cursor.lastrowid
        tracking_code = f"GH-{last_id:06d}"
        cursor.execute("""
        UPDATE gharardad
        SET tracking_code=%s
        WHERE id=%s
        """,
        (
            tracking_code,
            last_id
        ))

        db.commit()

        # ساخت فایل ورد

        if contract_type =="خرید و فروش ":
            template_path = "docx files/قرارداد خام خرید و فروش.docx"

        elif contract_type == "اجاره":
            template_path = "docx files/قرارداد خام اجاره.docx"

        elif contract_type == "مشارکت":
            template_path = "docx files/قرارداد خام مشارکت.docx"

        else:
            messagebox.showerror(
                "خطا",
                "نوع قرارداد نامعتبر است"
            )
            db.close()
            return

        # ساخت فایل ورد

        doc = DocxTemplate(template_path)

        doc.render({
            "tracking_code": tracking_code,
            "property_type": property_type,
            "contract_type": contract_type,
            "party_one": party_one,
            "party_two": party_two,
            "description": description
        })

        # انتخاب محل ذخیره

        file_name = f"{tracking_code}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx"

        file_path = filedialog.asksaveasfilename(
            title="ذخیره فایل قرارداد",
            initialfile=file_name,
            defaultextension=".docx",
            filetypes=[("Word Files", "*.docx")]
        )

        if not file_path:
            db.close()
            return

        # ذخیره فایل

        doc.save(file_path)

        # نمایش کد رهگیری

        for widget in code_frame.winfo_children():
            widget.destroy()

        code_label = tk.Label(
            code_frame,
            text=tracking_code,
            fg="#00BFFF",
            bg="#052340",
            font=("Consolas", 11, "bold")
        )

        code_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        db.close()

        messagebox.showinfo(
            "موفق",
            f"قرارداد با موفقیت ایجاد شد\n\nکد رهگیری: {tracking_code}"
        )

    except Exception as e:

        messagebox.showerror(
            "خطا",
            str(e)
        )
#endregion
#---------تابع پاک کردن فرم اصلی----------------
#region
def delete_root():
    melk_mahdode_gheimat_entry.delete(0,tk.END) 
    metraj_entry.delete(0,tk.END)
    metraj_entry.delete(0,tk.END)
    combo_file_type.set("")
    melk_type_combo.set("")
#endregion
#===================================================
#========================================================
# ------------پنجره اصلی-------------------------------
#region
root = tk.Tk()
root.title("Astate Agency")
root.geometry("1100x700")
#تصاویر پروژه
plus=tk.PhotoImage(file="Images/pluse.png")
elvator_pic=tk.PhotoImage(file="Images/elvator.png")
parking_pic=tk.PhotoImage(file="Images/parking.png")
warehouse_pic=tk.PhotoImage(file="Images/anbari.png")
#--------------------- تصاویر صفحه های اجاره -------------------------------
image_ejareh_maskoni=Image.open("Images/ejareh_maskoni.jpg")
image_ejareh_edari_tajari=Image.open("Images/ejareh_edari_tajari.jpg")
image_ejareh_bagh_zamin=Image.open("Images/ejareh_bagh_zamin.jpg")
image_ejareh_karghah=Image.open("Images/ejareh_karghah.jpg")
#---------------------- تصاویر صفحه های فروش ------------------------------- 
image_forosh_maskoni=Image.open("Images/forosh_maskoni.jpg")
image_forosh_edari_tejari=Image.open("Images/forosh_edari_tejari.jpg")
image_forosh_bagh_zamin=Image.open("Images/forosh_bagh_zamin.jpg")
image_forosh_karghah=Image.open("Images/forosh_karghah.jpg")
#---------------------- تصاویر صفحه های درخواست -------------------------------
image_darkhast_maskoni=Image.open("Images/darkhast_maskoni.jpg")
image_darkhast_edari_tejari=Image.open("Images/darkhast_edari_tejari.jpg")
image_darkhast_bagh_zamin=Image.open("Images/darkhast_bagh_zamin.jpg")
image_darkhast_kargah=Image.open("Images/darkhast_kargah.jpg")
#---------------------- تصاویر صفحه های گزارش ---------------------------------
image_gozaresh_maskoni=Image.open("Images/gozaresh_maskoni.jpg")
image_gozaresh_edari_tejari=Image.open("Images/gozaresh_edari_tejari.jpg")
image_gozaresh_bagh_zamin=Image.open("Images/gozaresh_bagh_zamin.jpg")
image_gozaresh_kargah=Image.open("Images/gozaresh_kargah.jpg")
#--------------------------تصاویر صفحه قراردادها------------
image_gharardad=tk.PhotoImage(file="Images/gharardad.png")
image_massage=tk.PhotoImage(file="Images/massage.png")
image_melk=tk.PhotoImage(file="Images/melk_image.png")
image_person=tk.PhotoImage(file="Images/person.png")
image_type_gharardad=tk.PhotoImage(file="Images/type_gharardad.png")
image_word=tk.PhotoImage(file="Images/word.png")
# root.attributes("-fullscreen", True) <<<-----  App فول اسکرین شدن
root.configure(bg="#052340")
main_frame=tk.Frame(root)
main_frame.pack(fill="both",expand=True)
#endregion
#------------------------فریم هدر --------------
#region
header=tk.Frame(main_frame,bg="#052340",height=60)
header.pack(fill='x')
title_font=font.Font(family="Shabnam",size=22,weight="bold")
title_label=tk.Label(header,text="آژانس املاک",fg="#00BFFF",bg="#052340",font=title_font)
title_label.pack(pady=25)
#endregion
#-----------قسمت منوبار پروژه------------------------
#---------------------فریم منو----------------------
#region
menu_frame=tk.Frame(main_frame,bg="#ffffff", relief="flat",height=1)
menu_frame.pack(padx=2, pady=2, fill="x")
#endregion
# ------------- لیست کشویی فیلد فایل های ثبتی-----------
#region
def darkhast():
    box_darkhast.deiconify()
    box_darkhast.grab_set()

def gozaresh():
    box_gozaresh.deiconify()
    box_gozaresh.grab_set()

def forosh():
    box_forosh.deiconify()
    box_forosh.grab_set()

def rahn():
    box_rehn_ejareh.deiconify()
    box_rehn_ejareh.grab_set()

def mosharecat():
    box_mosharekat.deiconify()
    box_mosharekat.grab_set()
#endregion
#---------------------------توابع باز و بستن کردن امکانات فایل ها---------------------------
#region
def open_option1():
    option_file_frame_ejareh_maskoni.deiconify()
    option_file_frame_ejareh_maskoni.grab_set()

def open_option2():
    option_file_frame_forosh_maskoni.deiconify()
    option_file_frame_forosh_maskoni.grab_set()

def open_option3():
    option_file_frame_ejareh_edari_tajari.deiconify()
    option_file_frame_ejareh_edari_tajari.grab_set()

def open_option4():
    option_file_frame_forosh_edari_tejari.deiconify()
    option_file_frame_forosh_edari_tejari.grab_set()

def open_option5():
    option_file_frame_ejareh_bagh_zamin.deiconify()
    option_file_frame_ejareh_bagh_zamin.grab_set()

def open_option6():
    option_file_frame_forosh_bagh_zamin.deiconify()
    option_file_frame_forosh_bagh_zamin.grab_set()

def open_option7():
    option_file_frame_ejareh_kargah.deiconify()
    option_file_frame_ejareh_kargah.grab_set()

def open_option8():
    option_file_frame_forosh_kargah.deiconify()
    option_file_frame_forosh_kargah.grab_set()

def open_option9():
    option_file_frame_darkhast_maskoni.deiconify()
    option_file_frame_darkhast_maskoni.grab_set()

def open_option10():
    option_file_frame_darkhast_edari_tejari.deiconify()
    option_file_frame_darkhast_edari_tejari.grab_set()

def open_option11():
    option_file_frame_darkhast_bagh_zamin.deiconify()
    option_file_frame_darkhast_bagh_zamin.grab_set()

def open_option12():
    option_file_frame_darkhast_kargah.deiconify()
    option_file_frame_darkhast_kargah.grab_set()

#endregion
#=======================================================
#-----------توابع برگشت صفحات ثبتی به فرم اصلی----------
#region
#-----برگشت از صفحه اجاره مسکونی-------------------------
def back_home_ejareh_maskoni():
    clear_entry_ejareh_maskoni()
    root.deiconify()
    ejareh_rehn_page.withdraw()
    delete_root()
#--------------------------------پاک شدن Entry صفحه اجاره مسکونی--------------------------
def clear_entry_ejareh_maskoni():
    #خالی کردن  باکس های اجاره مسکونی
    sal_sakht_ejareh_maskoni_entry.delete(0,tk.END)
    addrres_ejareh_maskoni_entry.delete(0,tk.END)
    tabaghe_ejareh_maskoni_entry.delete(0,tk.END)
    vahed_ejareh_maskoni_entry.delete(0,tk.END)
    otagh_ejareh_maskoni_entry.delete(0,tk.END)
    gheimat_ejare_ejare_maskoni_entry.delete(0,tk.END)
    gheimat_pish_ejare_maskoni_entry.delete(0,tk.END)
    name_malek_ejareh_maskoni_entry.delete(0,tk.END)
    shomareh_malek_ejareh_maskoni_entry.delete(0,tk.END)
    #پنجره امکانات
    sarmaesh_ejareh_maskoni_combo.set("")
    garmaesh_ejareh_maskoni_combo.set("")
    kaf_ejareh_maskoni_combo.set("")
    toilet_ejareh_maskoni_combo.set("")
    parking_checkbutton_btn_ejareh_maskoni.deselect()
    asansor_checkbutton_btn_ejareh_maskoni.deselect()
    anbari_checkbutton_btn_ejareh_maskoni.deselect()
#-----برگشت از صفحه فروش مسکونی-------------------------
def back_home_forosh_maskoni():
    clear_entry_forosh_maskoni()
    root.deiconify()
    forosh_rehn_page.withdraw()
    delete_root()
#--------------------------------پاک شدن Entry صفحه فروش مسکونی--------------------------
def clear_entry_forosh_maskoni():
    sal_sakht_forosh_maskoni_entry.delete(0, tk.END)
    addrres_forosh_maskoni_entry.delete(0, tk.END)
    tabaghe_forosh_maskoni_entry.delete(0, tk.END)
    vahed_forosh_maskoni_entry.delete(0, tk.END)
    otagh_forosh_maskoni_entry.delete(0, tk.END)
    gheimat_kol_forosh_maskoni_entry.delete(0, tk.END)
    name_malek_forosh_maskoni_entry.delete(0, tk.END)
    shomareh_malek_forosh_maskoni_entry.delete(0, tk.END)
    #پنجره امکانات
    sarmaesh_combo_forosh_maskoni.set("")
    garmaesh_combo_forosh_maskoni.set("")
    kaf_combo_forosh_maskoni.set("")
    toilet_combo_forosh_maskoni.set("")
    parking_ch_btn_forosh_maskoni.deselect()
    asansor_ch_btn_forosh_maskoni.deselect()
    anbari_checkbuton_forosh_maskoni.deselect()
#------------------------برگشت از صفحه اجاره اداری/تجاری---------------------
def back_home_ejareh_edari_tejari():
    clear_entry_ejareh_edari_tejari()
    root.deiconify()
    ejareh_edari_tejari.withdraw()
    delete_root()
#--------------------------------پاک شدن Entry صفحه اجاره اداری/تجاری--------------------------
def clear_entry_ejareh_edari_tejari():
    sal_sakht_ejareh_edari_tejari_entry.delete(0,tk.END)
    metraj_melk_ejareh_edari_tejari_entry.delete(0,tk.END)
    addrres_ejareh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_ejareh_edari_tejari_entry.delete(0,tk.END)
    vahed_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_ejareh_edari_tejari_entry.delete(0,tk.END)
    name_malek_ejareh_edari_tejari_entry.delete(0,tk.END)
    shomareh_malek_ejareh_edari_tejari_entry.delete(0,tk.END)
    #پنجره امکانات
    ab_va_gaz_combo_emkanat_ejareh_edari_tejari.set("")
    sarmayesh_combo_emkanat_ejareh_edari_tejari.set("")
    garmayesh_combo_emkanat_ejareh_edari_tejari.set("")
    parking_ch_btn_ejareh_edari_tejari.deselect()
    anbari_ch_btn_ejareh_edari_tejari.deselect()
    asansor_ch_btn_ejareh_edari_tejari.deselect()
#---------------------------برگشت از صفحه فروش اداری/تجاری--------------------
def back_home_forosh_edari_tejari():
    clear_entry_forosh_edari_tejari()
    root.deiconify()
    forosh_edari_tejari.withdraw()
    delete_root()
#--------------------------پاک شدن Entry صفحه فروش اداری و تجاری------------------------
def clear_entry_forosh_edari_tejari():
    sal_sakht_forosh_edari_tejari_entry.delete(0,tk.END)
    addrres_forosh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_forosh_edari_tejari_entry.delete(0,tk.END)
    vahed_forosh_edari_tejari_entry.delete(0,tk.END)
    gheimat_kol_forosh_edari_tejari_entry.delete(0,tk.END)
    metraj_melk_forosh_edari_tejari_entry.delete(0,tk.END)
    name_malek_forosh_edari_tejari_entry.delete(0,tk.END)
    shomareh_malek_forosh_edari_tejari_entry.delete(0,tk.END)
    #پنجره امکانات
    aab_va_gaz_combo_emkanat_forosh_edari_tejari.set("")
    sarmayesh_combo_emkanat_forosh_edari_tejari.set("")
    garmayesh_combo_emkanat_forosh_edari_tejari.set("")
    asansor_check_btn_forosh_edari_tejari.deselect()
    parking_check_btn_forosh_edari_tejari.deselect()
    anbari_check_btn_forosh_edari_tejari.deselect()
#----------------------------برگشت از صفحه اجاره باغ / زمین------------------
def back_home_ejareh_bagh_zamin():
    clear_entry_ejareh_bagh_zamin()
    ejareh_bagh_zamin.withdraw()
    root.deiconify()
    delete_root()
#--------------------------پاک شدن Entry صفحه اجاره باغ و زمین------------------------
def clear_entry_ejareh_bagh_zamin():
    metraj_zamin_ejareh_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_entry.delete(0,tk.END)
    bagh_gheimat_ejareh_bagh_zamin_entry.delete(0,tk.END)
    bagh_gheimat_har_metr_ejareh_bagh_zamin_entry.delete(0,tk.END)
    bagh_type_combo.set("باغ")
    room_bagh_checkbutton.deselect()
    name_malek_bagh_zamin_entry.delete(0,tk.END)
    number_malek_bagh_zamin_entry.delete(0,tk.END)

    # امکانات فروش باغ و زمین
    type_vila_ejareh_bagh_zamin_combo.set("")
    option_ejareh_bagh_zamin_combo.set("")
    tree_count_entry.delete(0,tk.END)
    metraj_tree_entry.delete(0,tk.END)
    abyari_combo.set("")
    type_tree_combo.set("")
    label_result_add.config(text="")
    label_result2_add.config(text="")
    metraj_vila_bagh_entry.delete(0,tk.END)
    sal_sakht_vila_bagh_entry.delete(0,tk.END)
    type_vila_forosh_bagh_zamin_combo.set("")
    toilet_bagh_combo.set("")
    hamam_bagh_combo.set("")
    sanad_bagh_combo.set("")
    chah_bagh.deselect()
    estakhr_bagh.deselect()
    bargh_bagh.deselect()
    divar_ejareh_bagh_zamin.deselect()
    #تغییر کاربری
    metraj_zamin_ejareh_bagh_zamin_entry2.delete(0,tk.END)
    karbari_ejareh_ejareh_bagh_zamin_combo.set("")
    khak_ejareh_ejareh_bagh_zamin_combo.set("")
    ab_ejareh_ejareh_bagh_zamin_combo.set("")
    metraj_vila_bagh_entry.config(state="disabled")
    sal_sakht_vila_bagh_entry.config(state="disabled")
    type_vila_ejareh_bagh_zamin_combo.config(state="disabled")
    toilet_bagh_combo.config(state="disabled")
    hamam_bagh_combo.config(state="disabled")
    sanad_bagh_combo.config(state="disabled")
    option_ejareh_bagh_zamin_combo.config(state="disabled")
    mojavez_sakht_ejareh_bagh_zamin.config(state="disabled")
    mohavate_ejareh_bagh_zamin.config(state="disabled")
    security_room_zamin_ejareh_bagh_zamin.deselect()
    bargh_tak_faz_zamin_ejareh_bagh_zamin.deselect()
    bargh_se_faz_zamin_ejareh_bagh_zamin.deselect()
    anbar_zamin_ejareh_bagh_zamin.deselect()
    fans_zamin_ejareh_bagh_zamin.deselect()
    mojavaz_chah_zamin_ejareh_bagh_zamin.deselect()
#-----------------------------برگشت از صفحه فروش باغ / زمین------------------
def back_home_forosh_bagh_zamin():
    clear_entry_forosh_bagh_zamin()
    forosh_bagh_zamin.withdraw()
    root.deiconify()    
    delete_root()
#------------------------- پاک شدن Entry صفحه فروش باغ و زمین----------------------------
def clear_entry_forosh_bagh_zamin():
    metraj_zamin_forosh_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_forosh_bagh_zamin_entry.delete(0,tk.END)
    gheimat_har_metr_babagh_zamin_forosh_entry.delete(0,tk.END)
    metraj_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    name_malek_forosh_bagh_entry.delete(0,tk.END)
    number_malek_forosh_bagh_entry.delete(0,tk.END)
    gheimat_kol_forosh_bagh_zamin_entry.delete(0,tk.END)

    # امکانات فروش باغ و زمین
    metraj_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    abyari_forosh_bagh_zamin_combo.set("")
    type_tree_forosh_bagh_zamin_combo.set("")
    label_natige_forosh_bagh_zamin.config(text="")
    metraj_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    type_vila_forosh_bagh_zamin_combo.set("")
    toilet_forosh_bagh_zamin_combo.set("")
    hamam_forosh_bagh_zamin_combo.set("")
    sanad_forosh_bagh_zamin_combo.set("")
    option_forosh_bagh_zamin_combo.set("")
    chah_forosh_bagh_zamin.deselect()
    estakhr_forosh_bagh_zamin.deselect()
    bargh_keshi_forosh_bagh_zamin.deselect()
    gas_keshi_forosh_bagh_zamin.deselect()
    #تغییر کاربری
    metraj_zamin2_forosh_bagh_zamin_entry.delete(0,tk.END)
    karbari_forosh_bagh_zamin_combo.set("")
    khak_forosh_bagh_zamin_combo.set("")
    ab_forosh_bagh_zamin_combo.set("")
    metraj_vila_forosh_bagh_zamin_entry.config(state="disabled")
    sal_sakht_vila_forosh_bagh_zamin_entry.config(state="disabled")
    type_vila_forosh_bagh_zamin_combo.config(state="disabled")
    toilet_forosh_bagh_zamin_combo.config(state="disabled")
    hamam_forosh_bagh_zamin_combo.config(state="disabled")
    sanad_forosh_bagh_zamin_combo.config(state="disabled")
    option_forosh_bagh_zamin_combo.config(state="disabled")
    
    lable_natige_add_forosh_bagh_zamin.config(text="")
    mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="disabled")
    mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="disabled")
    security_zamin_forosh_bagh_zamin.deselect()
    bargh_kesi_zamin_forosh_bagh_zamin.deselect()
    bargh_keshi_zamin_forosh_bagh_zamin2.deselect()
    anbar_zamin_forosh_bagh_zamin.deselect()
    divar_forosh_bagh_zamin.deselect()
    fans_zamin_forosh_bagh_zamin.deselect()
    mojavez_chah_zamin_forosh_bagh_zamin.deselect()
#----------------------- برگشت از صفحه اجاره کارگاه--------------------
def back_home_ejareh_karghah():
    clear_entry_ejareh_karghah()
    ejareh_karghah.withdraw()
    root.deiconify()
    delete_root()
#------------------------- پاک شدن Entry صفحه اجاره کارگاه ----------------------------
def clear_entry_ejareh_karghah():
    metraj_kargah_entry.delete(0,tk.END)
    loctaion_ejareh_kargah_entry.delete(0,tk.END)
    mablagh_ejareh_ejareh_kargah_entry.delete(0,tk.END)
    mablagh_pish_ejareh_kargah_entry.delete(0,tk.END) 
    name_malek_ejareh_kargah_entry.delete(0,tk.END) 
    shomareh_malek_ejareh_kargah_entry.delete(0,tk.END) 
    #پنجره امکانات
    sal_sakht_ejareh_kargah_entry.delete(0,tk.END)
    vaziat_bargh_ejareh_kargah_combo.set("")
    garmayesh_type_ejareh_kargah_combo.set("")
    vaziat_ab_ejareh_kargah_combo.set("")
    abzaar_ejareh_kargah_combo.set("")
    toilet_ejareh_kargah_combo.set("")
    hamam_ejareh_kargah__combo.set("")
    otagh_ejareh_kargah_combo.set("")
    sarmayesh_fan_ejareh_kargah.deselect()
    sarmayesh_panke_ejareh_kargah.deselect()
    sarmayesh_kooler_abi_ejareh_kargah.deselect()
    sarmayesh_kooler_gazi_ejareh_kargah.deselect()
#----------------------- برگشت از صفحه فروش کارگاه--------------------
def back_home_forosh_karghah():
    clear_entry_forosh_kargah()
    forosh_karghah.withdraw()
    root.deiconify()
    delete_root()
#-------------------------- پاک شدن Entry صفحه فروش کارگاه-----------------------
def clear_entry_forosh_kargah():
    loctaion_forosh_kargah_entry.delete(0,tk.END)
    gheimat_kol_forosh_kargah_entry.delete(0,tk.END)
    metraj_forosh_kargah_entry.delete(0,tk.END)
    name_malek_forosh_kargah_entry.delete(0,tk.END)
    shomareh_malek_forosh_kargah_entry.delete(0,tk.END)
    #پنجره امکانات
    sal_sakht_forosh_kargah_entry.delete(0,tk.END)
    vaziat_bargh_forosh_kargah_combo.set("")
    garmayesh_type_forosh_kargah_combo.set("")
    vaziat_ab_forosh_kargah_combo.set("")
    abzar_forosh_kargah_combo.set("")
    toilet_forosh_kargah_combo.set("")
    hamam_forosh_kargah_combo.set("")
    otagh_forosh_kargah_combo.set("")
    sarmayesh_fan_forosh_kargah.deselect()
    sarmayesh_panke_forosh_kargah.deselect()
    sarmayesh_kooler_abi_forosh_kargah.deselect()
    sarmayesh_kooler_gazi_forosh_kargah.deselect()
#----------------------------برگشت از صفحه اجاره کارگاه------------------
def back_to_ejareh_karghah():
    option_file_frame_ejareh_kargah.withdraw()
    ejareh_karghah.deiconify()
#----------------------------برگشت از صفحه درخواست مسکونی-------------------
def back_home_darkhast_maskoni():
    clear_entry_darkhast_maskoni()
    darkhast_maskoni_page.withdraw()
    root.deiconify()
    delete_root()
#-------------------------- پاک شدن Entry صفحه درخواست مسکونی-----------------------
def clear_entry_darkhast_maskoni():
    sal_sakht_darkhast_maskoni_entry.delete(0,tk.END)
    addrres_darkhast_maskoni_entry.delete(0,tk.END)
    tabaghe_darkhast_maskoni_entry.delete(0,tk.END)
    vahed_darkhast_maskoni_entry.delete(0,tk.END)
    otagh_darkhast_maskoni_entry.delete(0,tk.END)
    gheimat_kol_darkhast_maskoni_entry.delete(0,tk.END)
    name_moshtari_darkhast_maskoni_entry.delete(0,tk.END)
    shomareh_moshtari_darkhast_maskoni_entry.delete(0,tk.END)
    mablagh_ejare_darkhast_maskoni_entry.delete(0,tk.END)
    gheimat_pish_darkhast_maskoni_entry.delete(0,tk.END)
    #پنجره امکانات
    sarmaesh_combo_darkhast_maskoni.set("")
    garmaesh_combo_darkhast_maskoni.set("")
    kaf_combo_darkhast_maskoni.set("")
    toilet_combo_darkhast_maskoni.set("")
    parking_ch_btn_darkhast_maskoni.deselect()
    asansor_ch_btn_darkhast_maskoni.deselect()
    anbari_checkbuton_darkhast_maskoni.deselect()
    #---------------------------برگشت از صفحه درخواست اداری/تجاری--------------------
def back_home_darkhast_edari_tejari():
    clear_entry_darkhast_edari_tejari()
    darkhast_edari_tejari.withdraw()
    root.deiconify()
    delete_root()
#-------------------------- پاک شدن Entry صفحه درخواست اداری/تجاری-----------------------
def clear_entry_darkhast_edari_tejari():
    sal_sakht_darkhast_edari_tejari_entry.delete(0,tk.END)
    addrres_darkhast_edari_tejari_entry.delete(0,tk.END)
    tabaghe_darkhast_edari_tejari_entry.delete(0,tk.END)
    vahed_darkhast_edari_tejari_entry.delete(0,tk.END)
    gheimat_kol_darkhast_edari_tejari_entry.delete(0,tk.END)
    metraj_melk_darkhast_edari_tejari_entry.delete(0,tk.END)
    shomareh_moshtari_darkhast_edari_tejari_entry.delete(0,tk.END)
    name_moshtari_darkhast_edari_tejari_entry.delete(0,tk.END)
    mablagh_vadie_darkhast_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejareh_darkhast_edari_tejari_entry.delete(0,tk.END)
    #پنجره امکانات
    aab_va_gaz_combo_emkanat_darkhast_edari_tejari.set("")
    sarmayesh_combo_emkanat_darkhast_edari_tejari.set("")
    garmayesh_combo_emkanat_darkhast_edari_tejari.set("")
    parking_check_btn_darkhast_edari_tejari.deselect()
    asansor_check_btn_darkhast_edari_tejari.deselect()
    anbari_check_btn_darkhast_edari_tejari.deselect()
#-----------------------------برگشت از صفحه درخواست باغ / زمین------------------
def back_home_darkhast_bagh():
    clear_entry_darkhast_bagh_zamin()
    darkhast_bagh_zamin.withdraw()
    root.deiconify()  
    delete_root()
#-------------------------- پاک شدن Entry صفحه درخواست باغ/زمین-----------------------
def clear_entry_darkhast_bagh_zamin():  
    metraj_zamin_darkhast_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_darkhast_bagh_zamin_entry.delete(0,tk.END)
    gheimat_har_metr_bagh_zamin_darkhast_entry.delete(0,tk.END)
    metraj_derakht_darkhast_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_darkhast_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_darkhast_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_darkhast_bagh_zamin_entry.delete(0,tk.END)
    shomareh_moshtari_darkhast_bagh_entry.delete(0,tk.END)
    name_moshtari_darkhast_bagh_entry.delete(0,tk.END)
    gheimat_kol_bagh_zamin_darkhast_entry.delete(0,tk.END)
    gheimat_ejareh_bagh_darkhast_zamin_entry.delete(0,tk.END)
    mablagh_ejareh_mahaneh_darkhast_entry.delete(0,tk.END)
    # امکانات فروش باغ و زمین
    metraj_derakht_darkhast_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_darkhast_bagh_zamin_entry.delete(0,tk.END)
    abyari_darkhast_bagh_zamin_combo.set("")
    type_tree_darkhast_bagh_zamin_combo.set("")
    lable_natige_add_darkhast_bagh_zamin.config(text="")
    label_natige_darkhast_bagh_zamin.config(text="")
    metraj_vila_darkhast_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_darkhast_bagh_zamin_entry.delete(0,tk.END)
    type_vila_darkhast_bagh_zamin_combo.set("")
    toilet_darkhast_bagh_zamin_combo.set("")
    hamam_darkhast_bagh_zamin_combo.set("")
    sanad_darkhast_bagh_zamin_combo.set("")
    option_darkhast_bagh_zamin_combo.set("")
    chah_darkhast_bagh_zamin.deselect()
    estakhr_darkhast_bagh_zamin.deselect()
    bargh_keshi_darkhast_bagh_zamin.deselect()
    #تغییر کاربری
    metraj_zamin2_darkhast_bagh_zamin_entry.delete(0,tk.END)
    karbari_darkhast_bagh_zamin_combo.set("")
    khak_darkhast_bagh_zamin_combo.set("")
    ab_darkhast_bagh_zamin_combo.set("")
    metraj_vila_darkhast_bagh_zamin_entry.config(state="disabled")
    sal_sakht_vila_darkhast_bagh_zamin_entry.config(state="disabled")
    type_vila_darkhast_bagh_zamin_combo.config(state="disabled")
    toilet_darkhast_bagh_zamin_combo.config(state="disabled")
    hamam_darkhast_bagh_zamin_combo.config(state="disabled")
    sanad_darkhast_bagh_zamin_combo.config(state="disabled")
    option_darkhast_bagh_zamin_combo.config(state="disabled")
    mojavez_sakht_check_btn_darkhast_bagh_zamin.config(state="disabled")
    mohavate_sazi_check_btn_darkhast_bagh_zamin.config(state="disabled")
    otagh_check_btn_darkhast_bagh_zamin.deselect()
    security_zamin_darkhast_bagh_zamin.deselect()
    bargh_kesi_zamin_darkhast_bagh_zamin.deselect()
    bargh_keshi_zamin_darkhast_bagh_zamin2.deselect()
    anbar_zamin_darkhast_bagh_zamin.deselect()
    fans_zamin_darkhast_bagh_zamin.deselect()
    mojavez_chah_zamin_darkhast_bagh_zamin.deselect()
    divar_darkhast_bagh_zamin.deselect()
#-----------------------------برگشت از صفحه درخواست کارگاه--------------------
def back_home_darkhast_kargah():
    clear_entry_darkhast_kargah()
    darkhast_kargah.withdraw()   
    root.deiconify()
    delete_root()
#-------------------------- پاک شدن Entry صفحه درخواست کارگاه-----------------------
def clear_entry_darkhast_kargah():
    metraj_darkhast_kargah_entry.delete(0,tk.END)
    loctaion_darkhast_kargah_entry.delete(0,tk.END)
    gheimat_kol_darkhast_kargah_entry.delete(0,tk.END)
    shomareh_moshtari_darkhast_kargah_entry.delete(0,tk.END)
    name_moshtari_darkhast_kargah_entry.delete(0,tk.END)
    mablagh_pish_darkhast_kargah_entry.delete(0,tk.END)
    ejareh_mahaneh_darkhast_kargah_entry.delete(0,tk.END)
    #پنجره امکانات
    sal_sakht_darkhast_kargah_entry.delete(0,tk.END)
    vaziat_bargh_darkhast_kargah_combo.set("")
    garmayesh_type_darkhast_kargah_combo.set("")
    vaziat_ab_darkhast_kargah_combo.set("")
    abzaar_darkhast_kargah_combo.set("")
    toilet_darkhast_kargah_combo.set("")
    hamam_darkhast_kargah__combo.set("")
    otagh_darkhast_kargah_combo.set("")
    sarmayesh_panke_darkhast_kargah.deselect()
    sarmayesh_kooler_abi_darkhast_kargah.deselect()
    sarmayesh_kooler_gazi_darkhast_kargah.deselect()
    sarmayesh_fan_darkhast_kargah.deselect()
#----------------------برگشت از گزارش مسکونی--------
def back_home_gozaresh_maskoni():
    root.deiconify()
    gozaresh_maskoni.withdraw()
    error_label_maskoni.config(text="")
    gozaresh_file_combo_maskoni.set("")
#-----------------------برگشت از صفحه گزارش اداری و تجاری------------------------
def back_home_gozaresh_edari_tejari():
    root.deiconify()
    gozaresh_edari_tejari.withdraw()
    error_label_edari_tejari.config(text="")
    gozaresh_file_combo_edari_tejari.set("")
#--------------------------برگشت از گزارش باغ و زمین----------------------------
def back_home_gozaresh_bagh_zamin():
    root.deiconify()
    gozaresh_bagh_zamin.withdraw()
    error_label_bagh_zamin.config(text="")
    gozaresh_file_combo_bagh_zamin.set("")
#----------------------برگشت از صفحه گزارش کارگاه------------------
def back_home_gozaresh_kargah():
    root.deiconify()
    gozaresh_kargah.withdraw()
    error_label_kargah.config(text="")
    gozaresh_file_combo_kargah.set("")
def back_main_ghararadad():
    root.deiconify()
    gharardad_window.withdraw()
    type_gharardad_combo.set("")
    type_melk_gharardad_combo.set("")
    name_shakhs_aval_gharardad_entry.delete(0,tk.END)
    name_shakhs_dovom_gharardad_entry.delete(0,tk.END)
    tozih_gharardad_entry.delete(0,tk.END)
    code_label.config(text="")
#endregion
#region #توابع تایید اپشن ها 
#==============================
#region
def save_option_forosh_maskoni():
    option_file_frame_forosh_maskoni.withdraw()
    option_file_frame_forosh_maskoni.grab_release()

def save_option_forosh_edari_tejari():
    option_file_frame_forosh_edari_tejari.withdraw()
    option_file_frame_forosh_edari_tejari.grab_release()

def save_option_forosh_bagh_zamin():
    option_file_frame_forosh_bagh_zamin.withdraw()
    option_file_frame_forosh_bagh_zamin.grab_release()

def save_option_forosh_kargah():
    option_file_frame_forosh_kargah.withdraw()
    option_file_frame_forosh_kargah.grab_release()

def save_option_ejareh_maskoni():
    option_file_frame_ejareh_maskoni.withdraw()
    option_file_frame_ejareh_maskoni.grab_release()

def save_option_ejareh_edari_tejari():
    option_file_frame_ejareh_edari_tajari.withdraw()
    option_file_frame_ejareh_edari_tajari.grab_release()

def save_option_ejareh_bagh_zamin():
    option_file_frame_ejareh_bagh_zamin.withdraw()
    option_file_frame_ejareh_bagh_zamin.grab_release()

def save_option_ejareh_kargah():
    option_file_frame_ejareh_kargah.withdraw()
    option_file_frame_ejareh_kargah.grab_release()

def save_option_darkhast_maskoni():
    option_file_frame_darkhast_maskoni.withdraw()
    option_file_frame_darkhast_maskoni.grab_release()

def save_option_darkhast_edari_tejari():
    option_file_frame_darkhast_edari_tejari.withdraw()
    option_file_frame_darkhast_edari_tejari.grab_release()

def save_option_darkhast_bagh_zamin():
    option_file_frame_darkhast_bagh_zamin.withdraw()
    option_file_frame_darkhast_bagh_zamin.grab_release()

def save_option_darkhast_kargah():
    option_file_frame_darkhast_kargah.withdraw()
    option_file_frame_darkhast_kargah.grab_release()
#endregion
#=========================================================
#--------برگشت از امکانات فایل ها به صفحه اصلی ثبتی-------
#region
#-------برگشت اجاره مسکونی------------------
def back_to_ejareh_maskoni():
    option_file_frame_ejareh_maskoni.withdraw()
    option_file_frame_ejareh_maskoni.grab_release()
#--------برگشت اجاره اداری/تجاری----------------- 
def back_to_ejareh_edari_tejari():
    option_file_frame_ejareh_edari_tajari.withdraw()
    option_file_frame_ejareh_edari_tajari.grab_release()
#-------برگشت اجاره باغ و زمین------------------
def back_to_ejareh_bagh_zamin():
    option_file_frame_ejareh_bagh_zamin.withdraw()
    option_file_frame_ejareh_bagh_zamin.grab_release()
#--------------------برگشت اجاره کارگاه------------------------------------------------
def back_to_ejareh_karghah():
     option_file_frame_ejareh_kargah.withdraw()
     option_file_frame_ejareh_kargah.grab_release()
#-------برگشت فروش مسکونی------------------    
def back_to_forosh_maskoni():
    option_file_frame_forosh_maskoni.withdraw()
    option_file_frame_forosh_maskoni.grab_release()
#--------برگشت فروش اداری/تجاری----------------- 
def back_to_forosh_edari_tejari():
    option_file_frame_forosh_edari_tejari.withdraw()
    option_file_frame_forosh_edari_tejari.grab_release()
#--------------------برگشت فروش باغ و زمین------------------------------------------------
def  back_to_forosh_bagh_zamin():
     option_file_frame_forosh_bagh_zamin.withdraw()
     option_file_frame_forosh_bagh_zamin.grab_release()
#--------------------برگشت فروش کارگاه------------------------------------------------
def  back_to_forosh_karghah():
     option_file_frame_forosh_kargah.withdraw()
     option_file_frame_forosh_kargah.grab_release()
#-----------------------------برگشت درخواست مسکونی--------------------------
def back_to_darkhast_maskoni():
    option_file_frame_darkhast_maskoni.withdraw()
    option_file_frame_darkhast_maskoni.grab_release()
#--------برگشت درخواست اداری/تجاری----------------- 
def back_to_darkhast_edari_tejari():
    option_file_frame_darkhast_edari_tejari.withdraw()
    option_file_frame_darkhast_edari_tejari.grab_release()
#--------------------برگشت درخواست باغ و زمین------------------------------------------------
def  back_to_darkhast_bagh_zamin():
     option_file_frame_darkhast_bagh_zamin.withdraw()
     option_file_frame_darkhast_bagh_zamin.grab_release()
#-------------------برگشت درخواست کارگاه---------------------------
def  back_to_darkhast_kargah():
     option_file_frame_darkhast_kargah.withdraw()
     option_file_frame_darkhast_kargah.grab_release()
#----------برگشت باکس ها(نوع ملک)-------------
def back_forosh_exit():
    box_forosh.withdraw()
    box_forosh.grab_release()

def back_rehn_ejareh_exit():
    box_rehn_ejareh.withdraw()
    box_rehn_ejareh.grab_release()

def back_darkhast_exit():
    box_darkhast.withdraw()
    box_darkhast.grab_release()

def back_gozaresh_exit():
    box_gozaresh.withdraw()
    box_gozaresh.grab_release()

def back_mosharekat_exit():
    box_mosharekat.withdraw()
    box_mosharekat.grab_release()
#endregion
#============================================
#--------باز و بسته کردن بین باکس ها----------------
#-----بستن باکس و باز کردن صفحه اجاره مسکونی-----------
def ejareh_rehn_page():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_rehn_page.deiconify()
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره اداری/تجاری-----------
def ejareh_edari_tejari():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_edari_tejari.deiconify() 
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره باغ/زمین---------
def ejareh_bagh_zamin():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_bagh_zamin.deiconify()
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه اجاره کارگاه---------
def ejareh_karghah():
    box_rehn_ejareh.withdraw()
    root.withdraw()
    ejareh_karghah.deiconify() 
    box_rehn_ejareh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش مسکونی-----------
def forosh_rehn_page():
    box_forosh.withdraw()
    root.withdraw()
    forosh_rehn_page.deiconify() 
    box_forosh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش اداری/تجاری-----------
def forosh_edari_tejari():
    box_forosh.withdraw()
    root.withdraw()
    forosh_edari_tejari.deiconify()
    box_forosh.grab_release()
#-----بستن باکس و باز کردن صفحه فروش باغ/زمین---------
def forosh_bagh_zamin():
    box_forosh.withdraw()
    root.withdraw()
    forosh_bagh_zamin.deiconify()
    box_forosh.grab_release()  
#-----بستن باکس و باز کردن صفحه فروش  کارگاه---------
def forosh_karghah():
    box_forosh.withdraw()
    root.withdraw()
    forosh_karghah.deiconify() 
    box_forosh.grab_release()
#--------بستن باکس و باز کردن صفحه درخواست مسکونی--------
def darkhast_maskoni_page():
    box_darkhast.withdraw()
    root.withdraw()
    darkhast_maskoni_page.deiconify() 
    box_darkhast.grab_release()
#-----بستن باکس و باز کردن صفحه درخواست اداری/تجاری-----------
def darkhast_edari_tejari():
    box_darkhast.withdraw()
    root.withdraw()
    darkhast_edari_tejari.deiconify()
    box_darkhast.grab_release()
#-----بستن باکس و باز کردن صفحه درخواست باغ/زمین---------
def darkhast_bagh_zamin():
    box_darkhast.withdraw()
    root.withdraw()
    darkhast_bagh_zamin.deiconify()
    box_darkhast.grab_release()   
#------بستن باکس و باز کردن صفحه درخواست کارگاه-----------
def darkhast_kargah():
    box_darkhast.withdraw()
    root.withdraw()
    darkhast_kargah.deiconify()
    box_darkhast.grab_release()
#-------------------باز و بسته کردن صفحه گزارش مسکونی----------
def gozaresh_maskoni():
    box_gozaresh.withdraw()
    root.withdraw()
    gozaresh_maskoni.deiconify()
    box_gozaresh.grab_release()  
#---------------------باز و بسته کردن صفحه گزارش باغ و زمین-------
def gozaresh_bagh_zamin():
    box_gozaresh.withdraw()
    root.withdraw()
    gozaresh_bagh_zamin.deiconify()
    box_gozaresh.grab_release()  
#-----بستن باکس و باز کردن صفحه گزارش اداری/تجاری-----------
def gozaresh_edari_tejari():
    box_gozaresh.withdraw()
    root.withdraw()
    gozaresh_edari_tejari.deiconify()
    box_gozaresh.grab_release()   
#-------------بستن باکس و باز کردن صفحه گزارش کارگاه------------
def gozaresh_kargah():
    box_gozaresh.withdraw()
    root.withdraw()
    gozaresh_kargah.deiconify()
    box_gozaresh.grab_release()
#------------------------باز و بشته کردن پنجره قرادادها-------- 
def  open_ghrardad():
    root.withdraw()
    gharardad_window.deiconify()
#-------------رادیو باتن باکس-------------------
#تابع رادیو باتن باز و بسته کردن صفحات فروش
def sabt_radio_frosh():
    selected2 = forosh_radio_value.get()

    if selected2==0:
            box_forosh.withdraw()
            root.withdraw()
            forosh_rehn_page.deiconify() 
            box_forosh.grab_release()

    elif selected2==2:
            box_forosh.withdraw()
            root.withdraw()
            forosh_edari_tejari.deiconify()
            box_forosh.grab_release()
        
    elif selected2==4:
         box_forosh.withdraw()
         root.withdraw()
         forosh_bagh_zamin.deiconify()
         box_forosh.grab_release()
        
    elif selected2==6:
        box_forosh.withdraw()
        root.withdraw()
        forosh_karghah.deiconify()
        box_forosh.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات اجاره
def sabt_radio_rehn():
    selected = ejareh_radio_value.get()

    if selected==0:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_rehn_page.deiconify()
            box_rehn_ejareh.grab_release()
        
    elif selected==2:
        box_rehn_ejareh.withdraw()
        root.withdraw()
        ejareh_edari_tejari.deiconify() 
        box_rehn_ejareh.grab_release()

    elif selected==4:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_bagh_zamin.deiconify()
            box_rehn_ejareh.grab_release()

    elif selected==6:
            box_rehn_ejareh.withdraw()
            root.withdraw()
            ejareh_karghah.deiconify()
            box_rehn_ejareh.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات درخواست
def sabt_radio_darkhast():
    selected = darkhast_radio_value.get()

    if selected==0:
            box_darkhast.withdraw()
            root.withdraw()
            darkhast_maskoni_page.deiconify()
            box_darkhast.grab_release()
        
    elif selected==2:
        box_darkhast.withdraw()
        root.withdraw()
        darkhast_edari_tejari.deiconify()
        box_darkhast.grab_release()

    elif selected==4:
        box_darkhast.withdraw()
        root.withdraw()
        darkhast_bagh_zamin.deiconify()
        box_darkhast.grab_release()

    elif selected==6:
        box_darkhast.withdraw()
        root.withdraw()
        darkhast_kargah.deiconify()
        box_darkhast.grab_release()

#تابع رادیو باتن باز و بسته گزارش ها
def sabt_radio_gozaresh():
    selected = gozaresh_radio_value.get()

    if selected==0:
        box_gozaresh.withdraw()
        root.withdraw()
        gozaresh_maskoni.deiconify()
        box_gozaresh.grab_release() 

    elif selected==2:
        box_gozaresh.withdraw()
        root.withdraw()
        gozaresh_edari_tejari.deiconify()
        box_gozaresh.grab_release()

    elif selected==4:
        box_gozaresh.withdraw()
        root.withdraw()
        gozaresh_bagh_zamin.deiconify()
        box_gozaresh.grab_release()

    elif selected==6:
        box_gozaresh.withdraw()
        root.withdraw()
        gozaresh_kargah.deiconify()
        box_gozaresh.grab_release()

#تابع رادیو باتن باز و بسته کردن صفحات مشارکت
def sabt_radio_mosharekat():
    selected = mosharekat_radio_value.get()

    if selected == 0:
        box_mosharekat.withdraw()
        box_mosharekat.grab_release()

        #root.withdraw()
        #mosharecat_window.deiconify()

        #for f in frames:
         #   f.grid_forget()

        #frames[0].grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        
    elif selected==2:
        box_mosharekat.withdraw()
        root.withdraw()
        #pishforosh_page.deiconify()
        box_mosharekat.grab_release()
#endregion        
#=======================================================
#region
#---------------/جابه جایی کاربری باغ و زمین در قسمت های فروش/درخواست/اجاره-------------
def change_bagh_zamin1(event):
    co=bagh_type_combo.get()
    if co=="باغ":
        fram_option_zamin_ejareh_bagh_zamin.place_forget()
        option_frame_options_ejareh_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)
    else:
        option_frame_options_ejareh_bagh_zamin.place_forget()
        fram_option_zamin_ejareh_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)
def change_bagh_zamin_forosh_bagh(event):
    co=bagh_type_forosh_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_forosh_bagh_zamin.place_forget()
        option_frame_forosh_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)#فریم باغ
    else:
        option_frame_forosh_bagh_zamin.place_forget()
        option_frame_option2_forosh_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)
def change_bagh_zamin_darkhast_bagh(event):
    co=bagh_type_darkhast_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_darkhast_bagh_zamin.place_forget()
        option_frame_darkhast_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)
    else:
        option_frame_darkhast_bagh_zamin.place_forget()
        option_frame_option2_darkhast_bagh_zamin.place(x=1,y=60,relwidth=1,relheight=1)
#endregion
#=============================================================  
#region    
#---------------------قسمت اضافه کردن اپشن های تفریحی و درختان در قسمت باغ و زمین------------
selected_trees=[]
def add_tree():# برای اضافه کردن درخت به صورت دستی
    t=type_tree_combo.get()
    if t and t not in selected_trees:
        selected_trees.append(t)
        label_result_add.config(text=','.join(selected_trees))
selected_option=[]
def add_option():
    op=option_ejareh_bagh_zamin_combo.get()
    if op and op not in selected_option:
        selected_option.append(op)
        label_result2_add.config(text=','.join(selected_option))

selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        label_natige_forosh_bagh_zamin.config(text=','.join(selected_trees2))
selected_option2=[]
def add_option2():
    op2=option_forosh_bagh_zamin_combo.get()
    if op2 and op2 not in selected_option2:
        selected_option2.append(op2)
        lable_natige_add_forosh_bagh_zamin.config(text=','.join(selected_option2))
selected_trees3=[]
def add_tree3():
    t4=type_tree_darkhast_bagh_zamin_combo.get()
    if t4 and t4 not in selected_trees3:
        selected_trees3.append(t4)
        label_natige_darkhast_bagh_zamin.config(text=','.join(selected_trees3))
selected_option3=[]
def add_option3():
    op3=option_darkhast_bagh_zamin_combo.get()
    if op3 and op3 not in selected_option3:
        selected_option3.append(op3)
        lable_natige_add_darkhast_bagh_zamin.config(text=','.join(selected_option3))
#endregion
#====================================================================================
#=====================================================================================
#region
def home_true_false1(): # برای فعال یا غیر فعال کردن ویجت های خونه باغ در اجاره
    if var0.get()==1:
        metraj_vila_bagh_entry.config(state="normal")
        sal_sakht_vila_bagh_entry.config(state="normal")
        type_vila_ejareh_bagh_zamin_combo.config(state="readonly")
        toilet_bagh_combo.config(state="readonly")
        hamam_bagh_combo.config(state="readonly")
        sanad_bagh_combo.config(state="readonly")
        option_ejareh_bagh_zamin_combo.config(state="readonly")
        mojavez_sakht_ejareh_bagh_zamin.config(state="normal")
        mohavate_ejareh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_bagh_entry.config(state="disabled")
        sal_sakht_vila_bagh_entry.config(state="disabled")
        type_vila_ejareh_bagh_zamin_combo.config(state="disabled")
        toilet_bagh_combo.config(state="disabled")
        hamam_bagh_combo.config(state="disabled")
        sanad_bagh_combo.config(state="disabled")
        option_ejareh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_ejareh_bagh_zamin.config(state="disabled")
        mohavate_ejareh_bagh_zamin.config(state="disabled")
def home_true_false2(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در فروش
    if var0_forosh_bagh_zamin.get()==1:
        metraj_vila_forosh_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="normal")
        type_vila_forosh_bagh_zamin_combo.config(state="readonly")
        toilet_forosh_bagh_zamin_combo.config(state="readonly")
        hamam_forosh_bagh_zamin_combo.config(state="readonly")
        sanad_forosh_bagh_zamin_combo.config(state="readonly")
        option_forosh_bagh_zamin_combo.config(state="readonly")
        divar_forosh_bagh_zamin.config(state="normal")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_forosh_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="disabled")
        type_vila_forosh_bagh_zamin_combo.config(state="disabled")
        toilet_forosh_bagh_zamin_combo.config(state="disabled")
        hamam_forosh_bagh_zamin_combo.config(state="disabled")
        sanad_forosh_bagh_zamin_combo.config(state="disabled")
        option_forosh_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_forosh_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_forosh_bagh_zamin.config(state="disabled")
def home_true_false3(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در درخواست
    if var0_darkhast_bagh_zamin.get()==1:
        metraj_vila_darkhast_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_darkhast_bagh_zamin_entry.config(state="normal")
        type_vila_darkhast_bagh_zamin_combo.config(state="readonly")
        toilet_darkhast_bagh_zamin_combo.config(state="readonly")
        hamam_darkhast_bagh_zamin_combo.config(state="readonly")
        sanad_darkhast_bagh_zamin_combo.config(state="readonly")
        option_darkhast_bagh_zamin_combo.config(state="readonly")
        divar_darkhast_bagh_zamin.config(state="normal")
        mojavez_sakht_check_btn_darkhast_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_darkhast_bagh_zamin.config(state="normal")
    else:
        metraj_vila_darkhast_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_darkhast_bagh_zamin_entry.config(state="disabled")
        type_vila_darkhast_bagh_zamin_combo.config(state="disabled")
        toilet_darkhast_bagh_zamin_combo.config(state="disabled")
        hamam_darkhast_bagh_zamin_combo.config(state="disabled")
        sanad_darkhast_bagh_zamin_combo.config(state="disabled")
        option_darkhast_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_darkhast_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_darkhast_bagh_zamin.config(state="disabled")
selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        label_natige_forosh_bagh_zamin.config(text=' ,'.join(selected_trees2))
#endregion
#=================================DataBase========================
#region *توابع ثبتی دیتابیس*
#--------------------------------------تابع ثبت فروش---------------------------
def sabt_forosh_maskoni():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        # دستور ساده و انگلیسی خالص
        sql_create = """
        CREATE TABLE IF NOT EXISTS sabt_forosh_maskoni (
            id INT AUTO_INCREMENT PRIMARY KEY ,
            type_melk VARCHAR(50) NOT NULL,
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            otagh INT,
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            sarmayesh VARCHAR(20),
            garmayesh VARCHAR(20),
            kaf VARCHAR(20),
            toilet VARCHAR(20),
            name_malek VARCHAR(20),
            shomareh_malek INT,
            gheimat_kol DECIMAL(15,2)

        )
        """
        cursor.execute(sql_create)

        sql_insert = """
        INSERT INTO sabt_forosh_maskoni 
        (type_melk,sal_sakht,address,tabaghe,vahed,otagh,parking,asansor,
        anbari,sarmayesh,garmayesh,kaf,toilet,name_malek,shomareh_malek,gheimat_kol)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            melk_type_forosh_maskoni_entry.get(),
            sal_sakht_forosh_maskoni_entry.get(),
            addrres_forosh_maskoni_entry.get(),
            tabaghe_forosh_maskoni_entry.get(),
            vahed_forosh_maskoni_entry.get(),
            otagh_forosh_maskoni_entry.get(),
            parking_forosh_maskoni_var.get(),
            asansor_forosh_maskoni_var.get(),
            anbari_forosh_maskoni_var.get(),
            sarmaesh_combo_forosh_maskoni.get(),
            garmaesh_combo_forosh_maskoni.get(),
            kaf_combo_forosh_maskoni.get(),
            toilet_combo_forosh_maskoni.get(),
            name_malek_forosh_maskoni_entry.get(),
            shomareh_malek_forosh_maskoni_entry.get(),
            float(gheimat_kol_forosh_maskoni_entry.get())

        )

        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_forosh_maskoni()
            db.close()
#------------------- forosh_edari_tejari database -----------------------------------
def sabt_forosh_edari_tejari():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        sql_create = """
        CREATE TABLE IF NOT EXISTS sabt_forosh_edari_tejari (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            aab_va_gaz VARCHAR(20),
            system_sarmayesh VARCHAR(20),
            system_garmayesh VARCHAR(20),
            name_malek VARCHAR(20),
            shomareh_malek INT,
            gheimat_kol DECIMAL(15,2)

        )
        """
        cursor.execute(sql_create)

        sql_insert = """
        INSERT INTO sabt_forosh_edari_tejari
        (type_melk,metraj_melk,sal_sakht,address,tabaghe,vahed,parking,
        asansor,anbari,aab_va_gaz,system_sarmayesh,system_garmayesh,name_malek,shomareh_malek,gheimat_kol)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            melk_type_forosh_edari_tejari_entry.get(),
            metraj_melk_forosh_edari_tejari_entry.get(),
            sal_sakht_forosh_edari_tejari_entry.get(),
            addrres_forosh_edari_tejari_entry.get(),
            tabaghe_forosh_edari_tejari_entry.get(),
            vahed_forosh_edari_tejari_entry.get(),
            parking_forosh_edari_tejari_var.get(),
            asansor_forosh_edari_tejari_var.get(),
            anbari_forosh_edari_tejari_var.get(),
            aab_va_gaz_combo_emkanat_forosh_edari_tejari.get(),
            sarmayesh_combo_emkanat_forosh_edari_tejari.get(),
            garmayesh_combo_emkanat_forosh_edari_tejari.get(),
            name_malek_forosh_edari_tejari_entry.get(),
            shomareh_malek_forosh_edari_tejari_entry.get(),
            float(gheimat_kol_forosh_edari_tejari_entry.get()))
        
        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_forosh_edari_tejari()
            db.close()
#---------------------------forosh_bagh/zamin Database-------------------------
#region
#تابع مادر 
selected_option2=[]
selected_trees2=[]
#endregion
def sabt_forosh_bagh_zamin_main():
    db = None
    
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

                # ========== دریافت مقادیر ==========
        karbari = bagh_type_forosh_bagh_zamin_combo.get()
        gheimat_str = gheimat_har_metr_babagh_zamin_forosh_entry.get()
        if not gheimat_str or gheimat_str == "":
            gheimat_str = "0"
        gheimat_value = float(gheimat_str)
        
        if karbari == "باغ": 
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS forosh_bagh(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_metri DECIMAL(15,2),
                name_malek VARCHAR(50),
                shomareh_malek VARCHAR(30),
                gheimat_kol DECIMAL(15,2),
                metraj_derakht VARCHAR(10),
                tedad_derakht VARCHAR(10),
                type_derakht TEXT,
                system_ab VARCHAR(25),
                chah VARCHAR(10),
                estakhr VARCHAR(10),
                divar VARCHAR(10),
                sazeh VARCHAR(10),
                metraj_sazeh VARCHAR(10),
                sal_sakht VARCHAR(10),
                type_sazeh VARCHAR(20),
                emkanat TEXT,
                WC VARCHAR(10),
                hamam VARCHAR(10),
                javaz_sakht VARCHAR(10),
                sanad VARCHAR(20),
                mohavate VARCHAR(10),
                bargh VARCHAR (10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """) 
            type_derakht_value = ",".join(selected_trees2) if selected_trees2 else ""
            tedad_derakht_value = str(len(selected_trees2)) if selected_trees2 else "0"
            emkanat_value = ",".join(selected_option2) if selected_option2 else ""
            
            sql_bagh = """
                INSERT INTO forosh_bagh(
                    type_melk,metraj,karbari,address,mablagh_metri,name_malek,shomareh_malek,gheimat_kol,
                    metraj_derakht, tedad_derakht, type_derakht,
                    system_ab, chah, estakhr, divar,sazeh, metraj_sazeh,
                    sal_sakht, type_sazeh, emkanat, WC, hamam,
                    javaz_sakht, sanad, mohavate,bargh
                )
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s
                ,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            
            values_bagh = (
                melk_type_forosh_bagh_zamin_entry.get(),
                metraj_zamin_forosh_bagh_zamin_entry.get(),
                bagh_type_forosh_bagh_zamin_combo.get(),
                bagh_loctaion_forosh_bagh_zamin_entry.get(),
                gheimat_har_metr_babagh_zamin_forosh_entry.get(),
                name_malek_forosh_bagh_entry.get(),
                number_malek_forosh_bagh_entry.get(),
                gheimat_kol_forosh_bagh_zamin_entry.get(),
                metraj_derakht_forosh_bagh_zamin_entry.get(),
                tedad_derakht_value,
                type_derakht_value,
                abyari_forosh_bagh_zamin_combo.get(),
                chah_forosh_bagh_var.get(),
                estakhr_forosh_bagh_var.get(),
                divar_forosh_bagh_var.get(),
                var0_forosh_bagh_zamin.get(),
                metraj_vila_forosh_bagh_zamin_entry.get(),
                sal_sakht_vila_forosh_bagh_zamin_entry.get(),
                type_vila_forosh_bagh_zamin_combo.get(),
                emkanat_value,
                toilet_forosh_bagh_zamin_combo.get(),
                hamam_forosh_bagh_zamin_combo.get(),
                mojavez_sakht_forosh_bagh_var.get(),
                sanad_forosh_bagh_zamin_combo.get(),
                mohavate_forosh_bagh_var.get(),
                bargh_keshi_forosh_bagh_var.get()
            )
            cursor.execute(sql_bagh, values_bagh)

            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return
        elif karbari == "زمین کشاورزی":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS forosh_zamin(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_metri DECIMAL(15,2),
                name_malek VARCHAR(50),
                shomareh_malek VARCHAR(30),
                gheimat_kol DECIMAL(15,2),
                metraj_zamin VARCHAR(30),
                karbari_zamin VARCHAR(50),
                type_khak VARCHAR(20),
                manba_ab VARCHAR(20),
                negahbani VARCHAR(20),
                bargh_takfaz VARCHAR(20),
                bargh_sefaz VARCHAR(20),
                anbar VARCHAR(20),
                fans VARCHAR(20),
                chah VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
            )
        """)

            sql_zamin = """
                INSERT INTO forosh_zamin(
                    type_melk,metraj,karbari,address,mablagh_metri,name_malek,shomareh_malek,gheimat_kol,
                    metraj_zamin, karbari_zamin,type_khak,
                    manba_ab, negahbani, bargh_takfaz, bargh_sefaz,
                    anbar, fans, chah
                )
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            
            values_zamin = (
                melk_type_forosh_bagh_zamin_entry.get(),
                metraj_zamin_forosh_bagh_zamin_entry.get(),
                bagh_type_forosh_bagh_zamin_combo.get(),
                bagh_loctaion_forosh_bagh_zamin_entry.get(),
                gheimat_har_metr_babagh_zamin_forosh_entry.get(),
                name_malek_forosh_bagh_entry.get(),
                number_malek_forosh_bagh_entry.get(),
                gheimat_kol_forosh_bagh_zamin_entry.get(),
                metraj_zamin2_forosh_bagh_zamin_entry.get(),
                bagh_type_forosh_bagh_zamin_combo.get(),
                khak_forosh_bagh_zamin_combo.get(),
                ab_forosh_bagh_zamin_combo.get(),
                security_zamin_forosh_zamin_var.get(),
                bargh_kesi_zamin_forosh_zamin_var.get(),
                bargh_kesi_zamin_forosh_zamin2_var.get(),
                anbar_zamin_forosh_zamin_var.get(),
                fans_zamin_forosh_zamin_var.get(),
                javaz_chah_zamin_forosh_zamin_var.get()
            )
            cursor.execute(sql_zamin, values_zamin)
            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return
        
        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")      
        
    except Exception as e:
        messagebox.showerror("Error", f"خطا در ثبت داده: {e}")
        
    finally:
        if db and db.is_connected():
            clear_entry_forosh_bagh_zamin()
            db.close()
#---------------------------- forosh_karghah Database ------------------------
def sabt_forosh_kargah():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        
        cursor.execute("USE state_agency")

        sql_create = """
        CREATE TABLE IF NOT EXISTS sabt_forosh_kargah (
            id INT AUTO_INCREMENT PRIMARY KEY,
            karbari_zamin VARCHAR(50) NOT NULL,
            metraj VARCHAR(20),
            address VARCHAR(225),
            sal_sakht VARCHAR(20),
            vaziat_bargh VARCHAR(20),
            garmayesh VARCHAR(20),
            fan VARCHAR(20),
            panke VARCHAR(20),
            kooler_abi VARCHAR(20),
            kooler_gazi VARCHAR(20),
            vaziat_ab VARCHAR(30),
            abzar VARCHAR(30),
            toilet VARCHAR(20),
            hamam VARCHAR(20),
            otagh VARCHAR(20),
            name_malek VARCHAR(20),
            shomareh_malek INT,
            gheimat_kol DECIMAL(15,2)
        )
        """
        cursor.execute(sql_create)
        sql_insert = """
        INSERT INTO sabt_forosh_kargah
        (karbari_zamin,metraj,address,sal_sakht,
        vaziat_bargh,garmayesh,fan,panke,kooler_abi,kooler_gazi,vaziat_ab,abzar,toilet,hamam,otagh,name_malek,shomareh_malek,gheimat_kol)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            karbari_forosh_kargah_entry.get(),
            metraj_forosh_kargah_entry.get(),
            loctaion_forosh_kargah_entry.get(),
            sal_sakht_forosh_kargah_entry.get(),
            vaziat_bargh_forosh_kargah_combo.get(),
            garmayesh_type_forosh_kargah_combo.get(),
            fan_forosh_kargah_var.get(),
            panke_forosh_kargah_var.get(),
            kooler_abi_forosh_kargah_var.get(),
            kooler_gazi_forosh_kargah_var.get(),
            vaziat_ab_forosh_kargah_combo.get(),
            abzar_forosh_kargah_combo.get(),
            toilet_forosh_kargah_combo.get(),
            hamam_forosh_kargah_combo.get(),
            otagh_forosh_kargah_combo.get(),
            name_malek_forosh_kargah_entry.get(),
            shomareh_malek_forosh_kargah_entry.get(),
            float(gheimat_kol_forosh_kargah_entry.get())
        )
        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_forosh_kargah()
            db.close()
#------------------------------------پایان ثبت فروش-----------------------------
#----------------------------تابع ثبت اجاره----------------------------------
#----------------------- ejareh_maskoni Database -------------------------------
def sabt_ejareh_maskoni():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        sql_create = """
            CREATE TABLE IF NOT EXISTS sabt_ejareh_maskoni (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            otagh INT,
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            sarmayesh VARCHAR(20),
            garmayesh VARCHAR(20),
            kaf VARCHAR(20),
            toilet VARCHAR(20),
            ejareh VARCHAR(20),
            pish VARCHAR(20),
            name_malek VARCHAR(20),
            shomareh_malek INT
        )
        """

        cursor.execute(sql_create)

        sql_insert = """
        INSERT INTO sabt_ejareh_maskoni 
        (type_melk,sal_sakht,address,tabaghe,vahed,otagh,parking,
        asansor,anbari,sarmayesh,garmayesh,kaf,toilet,ejareh,pish,name_malwk,shomareh_malek)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            melk_type_ejareh_maskoni_entry.get(),
            sal_sakht_ejareh_maskoni_entry.get(),
            addrres_ejareh_maskoni_entry.get(),
            tabaghe_ejareh_maskoni_entry.get(),
            vahed_ejareh_maskoni_entry.get(),
            otagh_ejareh_maskoni_entry.get(),
            parking_ejareh_maskoni_var.get(),
            asansor_ejareh_maskoni_var.get(),
            anbari_ejareh_maskoni_var.get(),
            sarmaesh_ejareh_maskoni_combo.get(),
            garmaesh_ejareh_maskoni_combo.get(),
            kaf_ejareh_maskoni_combo.get(),
            toilet_ejareh_maskoni_combo.get(),
            float(gheimat_ejare_ejare_maskoni_entry.get()),
            float(gheimat_pish_ejare_maskoni_entry.get()),
            name_malek_ejareh_maskoni_entry.get(),
            shomareh_malek_ejareh_maskoni_entry.get()

        )

        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_ejareh_maskoni()
            db.close()
#---------------------ejareh_edari/tejari Database------------------------------
def sabt_ejareh_edari_tejari():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        sql_create = """
        CREATE TABLE IF NOT EXISTS sabt_ejareh_edari_tejari (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            aab_va_gaz VARCHAR(20),
            system_sarmayesh VARCHAR(20),
            system_garmayesh VARCHAR(20),
            gheimat_vadie DECIMAL(15,2),
            gheimat_ejareh DECIMAL(15,2),
            name_malek VARCHAR(20),
            shomareh_malek INT
        )
        """
        cursor.execute(sql_create)

        sql_insert = """
        INSERT INTO sabt_ejareh_edari_tejari
        (type_melk,metraj_melk,sal_sakht,address,tabaghe,vahed,parking,asansor,
        anbari,aab_va_gaz,system_sarmayesh,system_garmayesh,
        gheimat_vadie,gheimat_ejareh,name_malek,shomareh_malek)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            melk_type_ejareh_edari_tejari_entry.get(),
            metraj_melk_ejareh_edari_tejari_entry.get(),
            sal_sakht_ejareh_edari_tejari_entry.get(),
            addrres_ejareh_edari_tejari_entry.get(),
            tabaghe_ejareh_edari_tejari_entry.get(),
            vahed_ejareh_edari_tejari_entry.get(),
            parking_ejareh_edari_tejari_var.get(),
            asansor_ejareh_edari_tejari_var.get(),
            anbari_ejareh_edari_tejari_var.get(),
            ab_va_gaz_combo_emkanat_ejareh_edari_tejari.get(),
            sarmayesh_combo_emkanat_ejareh_edari_tejari.get(),
            garmayesh_combo_emkanat_ejareh_edari_tejari.get(),
            float(mablagh_pish_ejareh_edari_tejari_entry.get()),
            float(mablagh_ejare_ejareh_edari_tejari_entry.get()),
            name_malek_ejareh_edari_tejari_entry.get(),
            shomareh_malek_ejareh_edari_tejari_entry.get()


        )
        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_ejareh_edari_tejari()
            db.close()
#-----------------ejareh_bagh/zamin Database------------------------------------
selected_option=[]
selected_trees=[]
def sabt_ejareh_bagh_zamin():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")
        karbari = bagh_type_combo.get()
        gheimat_str =bagh_gheimat_har_metr_ejareh_bagh_zamin_entry.get()
        if not gheimat_str or gheimat_str == "":
            gheimat_str = "0"
        gheimat_value = float(gheimat_str)
        # ========== ساخت جدول اصلی ==========
        if karbari == "باغ":  
            type_derakht_value = ",".join(selected_trees) if selected_trees else ""
            tedad_derakht_value = str(len(selected_trees)) if selected_trees else "0"
            emkanat_value = ",".join(selected_option) if selected_option else ""

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ejareh_bagh(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_pish VARCHAR(20),
                mablagh_ejareh DECIMAL(15,2),
                zaman_ejareh VARCHAR(30),
                name_malek VARCHAR(50),
                shomareh_malek VARCHAR(50),
                metraj_derakht VARCHAR(10),
                tedad_derakht VARCHAR(10),
                type_derakht TEXT,
                system_ab VARCHAR(25),
                chah VARCHAR(10),
                estakhr VARCHAR(10),
                divar VARCHAR(10),
                bargh VARCHAR(10),
                sazeh VARCHAR(10),
                metraj_sazeh VARCHAR(10),
                sal_sakht VARCHAR(10),
                type_sazeh VARCHAR(20),
                emkanat TEXT,
                WC VARCHAR(10),
                hamam VARCHAR(10),
                javaz_sakht VARCHAR(10),
                sanad VARCHAR(20),
                mohavate VARCHAR(10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
            
            sql_bagh = """
                INSERT INTO ejareh_bagh(type_melk, metraj, karbari, address,mablagh_pish,
                    mablagh_ejareh,zaman_ejareh,name_malek,shomareh_malek,
                    metraj_derakht,tedad_derakht, type_derakht,
                    system_ab, chah, estakhr, divar,sazeh, metraj_sazeh,
                    sal_sakht, type_sazeh, emkanat, WC, hamam,
                    javaz_sakht, sanad, mohavate,bargh
                )
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s)
            """
            
            values_bagh = (
                melk_type_ejareh_bagh_zamin_entry.get(),
                metraj_zamin_ejareh_bagh_zamin_entry.get(),
                karbari,
                bagh_loctaion_entry.get(),
                bagh_gheimat_ejareh_bagh_zamin_entry.get(),
                gheimat_value,
                bagh_time_combo.get(),
                name_malek_bagh_zamin_entry.get(),
                number_malek_bagh_zamin_entry.get(),
                metraj_tree_entry.get(),
                tedad_derakht_value,
                type_derakht_value,
                abyari_combo.get(),
                chah_bagh_ejareh_var.get(),
                estakhr_bagh_var.get(),
                divar_ejareh_bagh_var.get(),
                var0.get(),
                metraj_vila_bagh_entry.get(),
                sal_sakht_vila_bagh_entry.get(),
                type_vila_ejareh_bagh_zamin_combo.get(),
                emkanat_value,
                toilet_bagh_combo.get(),
                hamam_bagh_combo.get(),
                mojavez_sakht_ejareh_bagh_var.get(),
                sanad_bagh_combo.get(),
                mohavate_ejareh_bagh_var.get(),
                bargh_bagh_var.get()
            )
            cursor.execute(sql_bagh, values_bagh)
            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
               messagebox.showerror("Error", "خطا: ثبت در جدول اصلی انجام نشد")
               return
            
        elif karbari == "زمین کشاورزی": 
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ejareh_zamin(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_pish VARCHAR(20),
                mablagh_metri DECIMAL(15,2),
                zaman_ejareh VARCHAR(30),
                name_malek VARCHAR(50),
                shomareh_malek VARCHAR(30),
                metraj_zamin VARCHAR(30),
                karbari_zamin VARCHAR(50),
                type_khak VARCHAR(20),
                manba_ab VARCHAR(20),
                negahbani VARCHAR(20),
                bargh_takfaz VARCHAR(20),
                bargh_sefaz VARCHAR(20),
                anbar VARCHAR(20),
                fans VARCHAR(20),
                chah VARCHAR(20),
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """) 
            sql_zamin = """
                INSERT INTO ejareh_zamin(type_melk, metraj, karbari, address,mablagh_pish,
                    mablagh_metri,zaman_ejareh,name_malek,shomareh_malek,
                    metraj_zamin, karbari_zamin, type_khak,
                    manba_ab, negahbani, bargh_takfaz, bargh_sefaz,
                    anbar, fans, chah
                )
                VALUES(%s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        # ========== ساخت جدول زمین (بدون hagh_bardasht) ==========

            values_zamin = (
                melk_type_ejareh_bagh_zamin_entry.get(),
                metraj_zamin_ejareh_bagh_zamin_entry.get(),
                karbari,
                bagh_loctaion_entry.get(),
                bagh_gheimat_ejareh_bagh_zamin_entry.get(),
                gheimat_value,
                bagh_time_combo.get(),
                name_malek_bagh_zamin_entry.get(),
                number_malek_bagh_zamin_entry.get(),
                metraj_zamin_ejareh_bagh_zamin_entry2.get(),
                karbari_ejareh_ejareh_bagh_zamin_combo.get(),
                khak_ejareh_ejareh_bagh_zamin_combo.get(),
                ab_ejareh_ejareh_bagh_zamin_combo.get(),
                security_zamin_ejareh_var.get(),
                bargh_tak_ejareh_zamin_var.get(),
                bargh_se_faz_ejareh_zamin_var.get(),
                anbar_ejareh_zamin_var.get(),
                fans_ejareh_zamin_var.get(),
                mojavaz_chah_ejareh_zamin_var.get()
            )
            cursor.execute(sql_zamin, values_zamin)
            last_id = cursor.lastrowid
        
            if last_id is None or last_id == 0:
               messagebox.showerror("Error", "خطا: ثبت در جدول اصلی انجام نشد")
               return
            
        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد")
 
    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_ejareh_bagh_zamin()
            db.close()
#-----------------ejareh_kargah Database----------------------------------------
def sabt_ejareh_kargah():
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        
        cursor.execute("USE state_agency")

        sql_create = """
        CREATE TABLE IF NOT EXISTS sabt_ejareh_kargah (
            id INT AUTO_INCREMENT PRIMARY KEY,
            karbari_zamin VARCHAR(50) NOT NULL,
            metraj VARCHAR(20),
            loctaion_and_address VARCHAR(225),
            gheimat_vadie DECIMAL(15,2),
            mablagh_ejareh DECIMAL(15,2),
            time_ejare VARCHAR(20),
            sal_sakht VARCHAR(20),
            vaziat_bargh VARCHAR(30),
            garmayesh VARCHAR(20),
            fan VARCHAR(20),
            panke VARCHAR(20),
            kooler_abi VARCHAR(20),
            kooler_gazi VARCHAR(20),
            vaziat_ab VARCHAR(30),
            abzar VARCHAR(30),
            toilet VARCHAR(20),
            hamam VARCHAR(20),
            otagh VARCHAR(20),
            name_malek VARCHAR(20),
            shomareh_malek INT

        )
        """
        cursor.execute(sql_create)
        sql_insert = """
        INSERT INTO sabt_ejareh_kargah
        (karbari_zamin,metraj,loctaion_and_address,
        gheimat_vadie,mablagh_ejareh,time_ejare,sal_sakht,vaziat_bargh,
        garmayesh,fan,panke,kooler_abi,kooler_gazi,vaziat_ab,abzar,toilet,hamam,otagh,name_malek,shomareh_malek)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            karbari_ejareh_kargah_entry.get(),
            metraj_kargah_entry.get(),
            loctaion_ejareh_kargah_entry.get(),
            float(mablagh_pish_ejareh_kargah_entry.get()),
            float(mablagh_ejareh_ejareh_kargah_entry.get()),
            time_ejare_ejareh_kargah_combo.get(),
            sal_sakht_ejareh_kargah_entry.get(),
            vaziat_bargh_ejareh_kargah_combo.get(),
            garmayesh_type_ejareh_kargah_combo.get(),
            sarmayesh_fan_ejareh_kargah_var.get(),
            sarmayesh_panke_ejareh_kargah_var.get(),
            sarmayesh_kooler_abi_ejareh_kargah_var.get(),
            sarmayesh_kooler_gazi_ejareh_kargah_var.get(),
            vaziat_ab_ejareh_kargah_combo.get(),
            abzaar_ejareh_kargah_combo.get(),
            toilet_ejareh_kargah_combo.get(),
            hamam_ejareh_kargah__combo.get(),
            otagh_ejareh_kargah_combo.get(),
            name_malek_ejareh_kargah_entry.get(),
            shomareh_malek_ejareh_kargah_entry.get()
        )
        cursor.execute(sql_insert, values)
        last_id = cursor.lastrowid
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")
        db.commit()

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")
    finally:
        if db and db.is_connected():
            clear_entry_ejareh_karghah()
            db.close()
#------------------------پایان تابع اجاره-----------------------------------
#endregion
#----------------------تابع ثبت درخواست--------------------------------
#region
#---------------darkhast_maskoni Database------------------------
skip_save=False
def sabt_darkhast_maskoni(event=None):
    global skip_save
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        change_type= melk_type_darkhast_maskoni_entry.get()
        #فیلد های خرید
        gheimat_kol_darkhast_maskoni_lable.place_forget()
        gheimat_kol_darkhast_maskoni_entry.place_forget()
        #فیلد های اجاره
        mablagh_ejare_darkhast_maskoni_lable.place_forget()
        mablagh_ejare_darkhast_maskoni_entry.place_forget()
        gheimat_pish_darkhast_maskoni_lable.place_forget()
        gheimat_pish_darkhast_maskoni_entry.place_forget()
        # فیلد های مشترک
        name_moshtari_darkhast_maskoni_lable.place_forget()
        name_moshtari_darkhast_maskoni_entry.place_forget()
        shomareh_moshtari_darkhast_maskoni_lable.place_forget()
        shomareh_moshtari_darkhast_maskoni_entry.place_forget()
        
        if change_type=="درخواست خرید مسکونی":

            gheimat_kol_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 445, anchor="e")
            gheimat_kol_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 430, width=150, height=25)
            name_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 340,anchor="e")
            name_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)
            shomareh_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 390,anchor="e")
            shomareh_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)

        elif change_type=="درخواست اجاره مسکونی":
           
           mablagh_ejare_darkhast_maskoni_lable.place(x=start_x + 130, y=start_y + 340, anchor="e")
           mablagh_ejare_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 370, width=150, height=25)
           gheimat_pish_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 340, anchor="e")
           gheimat_pish_darkhast_maskoni_entry.place(x=start_x + 190, y=start_y + 370, width=150, height=25)
           name_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 442,anchor="e")
           name_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 430, width=150, height=25)
           shomareh_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 486,anchor="e")
           shomareh_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 475, width=150, height=25)
        if event is not None:#خیلی مهم 
           return
        
        if change_type=="درخواست خرید مسکونی":
            cursor.execute( """
            CREATE TABLE IF NOT EXISTS sabt_darkhast_kharid_maskoni (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            otagh INT,
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            sarmayesh VARCHAR(20),
            garmayesh VARCHAR(20),
            kaf VARCHAR(20),
            toilet VARCHAR(20),
            gheimat_kol VARCHAR(20),
            name_moshtari VARCHAR(20),
            shomareh_moshtari INT
            )
            """)

            sql_kharid = """
            INSERT INTO sabt_darkhast_kharid_maskoni 
            (type_melk,sal_sakht,address,tabaghe,vahed,otagh,parking,asansor,
            anbari,sarmayesh,garmayesh,kaf,toilet,gheimat_kol,name_moshtari,shomareh_moshtari)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values_darkhast_kharid_maskoni = (
            melk_type_darkhast_maskoni_entry.get(),
            sal_sakht_darkhast_maskoni_entry.get(),
            addrres_darkhast_maskoni_entry.get(),
            tabaghe_darkhast_maskoni_entry.get(),
            vahed_darkhast_maskoni_entry.get(),
            otagh_darkhast_maskoni_entry.get(),
            parking_darkhast_maskoni_var.get(),
            asansor_darkhast_maskoni_var.get(),
            anbari_darkhast_maskoni_var.get(),
            sarmaesh_combo_darkhast_maskoni.get(),
            garmaesh_combo_darkhast_maskoni.get(),
            kaf_combo_darkhast_maskoni.get(),
            toilet_combo_darkhast_maskoni.get(),
            gheimat_kol_darkhast_maskoni_entry.get(),
            name_moshtari_darkhast_maskoni_entry.get(),
            shomareh_moshtari_darkhast_maskoni_entry.get()     
            )

            cursor.execute(sql_kharid, values_darkhast_kharid_maskoni)
        
            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return

        elif change_type=="درخواست اجاره مسکونی":

            cursor.execute( """
            CREATE TABLE IF NOT EXISTS sabt_darkhast_ejareh_maskoni (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            otagh INT,
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            sarmayesh VARCHAR(20),
            garmayesh VARCHAR(20),
            kaf VARCHAR(20),
            toilet VARCHAR(20),
            ejareh VARCHAR(20),
            pish VARCHAR(20),
            name_moshtari VARCHAR(20),
            shomareh_moshtari INT
            )
             """)

            sql_ejareh = """
            INSERT INTO sabt_darkhast_ejareh_maskoni 
            (type_melk,sal_sakht,address,tabaghe,vahed,otagh,parking,
            asansor,anbari,sarmayesh,garmayesh,kaf,toilet,ejareh,pish,name_moshtari,shomareh_moshtari)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values_darkhast_ejareh_maskoni= (
            melk_type_darkhast_maskoni_entry.get(),
            sal_sakht_darkhast_maskoni_entry.get(),
            addrres_darkhast_maskoni_entry.get(),
            tabaghe_darkhast_maskoni_entry.get(),
            vahed_darkhast_maskoni_entry.get(),
            otagh_darkhast_maskoni_entry.get(),
            parking_darkhast_maskoni_var.get(),
            asansor_darkhast_maskoni_var.get(),
            anbari_darkhast_maskoni_var.get(),
            sarmaesh_combo_darkhast_maskoni.get(),
            garmaesh_combo_darkhast_maskoni.get(),
            kaf_combo_darkhast_maskoni.get(),
            toilet_combo_darkhast_maskoni.get(),
            mablagh_ejare_darkhast_maskoni_entry.get(),
            gheimat_pish_darkhast_maskoni_entry.get(),
            name_moshtari_darkhast_maskoni_entry.get(),
            shomareh_moshtari_darkhast_maskoni_entry.get()
            )

            cursor.execute(sql_ejareh, values_darkhast_ejareh_maskoni)
            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return


        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")      
    except Exception as e:
        messagebox.showerror("Error", f"خطا در ثبت داده: {e}")
        
    finally:
        if db and db.is_connected():
            clear_entry_darkhast_maskoni()
            db.close()

#---------------darkhast_edari/tejari Database--------------------
skip_save=False
def sabt_darkhast_edari_tejari(event=None):
    global skip_save
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        change_type= combo_darkhast_edari_tejari_entry.get()
        #فیلد های خرید
        gheimat_kol_darkhast_edari_tejari_lable.place_forget()
        gheimat_kol_darkhast_edari_tejari_entry.place_forget()
        #فیلد های اجاره
        mablagh_vadie_darkhast_edari_tejari_lable.place_forget()
        mablagh_vadie_darkhast_edari_tejari_entry.place_forget()
        mablagh_ejareh_darkhast_edari_tejari_lable.place_forget()
        mablagh_ejareh_darkhast_edari_tejari_entry.place_forget()
        # فیلد های مشترک
        name_moshtari_darkhast_edari_tejari_lable.place_forget()
        name_moshtari_darkhast_edari_tejari_entry.place_forget()
        shomareh_moshtari_darkhast_edari_tejari_lable.place_forget()
        shomareh_moshtari_darkhast_edari_tejari_entry.place_forget()

        if change_type=="درخواست خرید اداری/تجاری":

            gheimat_kol_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")
            gheimat_kol_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 425, width=150, height=25)
            name_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")
            name_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)
            shomareh_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")
            shomareh_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

        elif change_type=="درخواست اجاره اداری/تجاری":
           
           mablagh_vadie_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")
           mablagh_vadie_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)
           mablagh_ejareh_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")
           mablagh_ejareh_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)
           name_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 438, anchor="e")
           name_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 425, width=150, height=25)
           shomareh_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 487, anchor="e")
           shomareh_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 475, width=150, height=25)
        if event is not None:#خیلی مهم 
           return
        
        if change_type=="درخواست خرید اداری/تجاری":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sabt_darkhast_kharid_edari_tejari (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            aab_va_gaz VARCHAR(20),
            system_sarmayesh VARCHAR(20),
            system_garmayesh VARCHAR(20),
            mablagh_kharid VARCHAR(20),
            name_moshtari VARCHAR(20),
            shomareh_moshtari INT
            )
            """)

            sql_kharid = """
            INSERT INTO sabt_darkhast_kharid_edari_tejari
            (type_melk,metraj_melk,sal_sakht,address,tabaghe,vahed,parking,
            asansor,anbari,aab_va_gaz,system_sarmayesh,system_garmayesh,mablagh_kharid,name_moshtari,shomareh_moshtari)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values_darkhast_kharid_edari_tejari = (
            combo_darkhast_edari_tejari_entry.get(),
            metraj_melk_darkhast_edari_tejari_entry.get(),
            sal_sakht_darkhast_edari_tejari_entry.get(),
            addrres_darkhast_edari_tejari_entry.get(),
            tabaghe_darkhast_edari_tejari_entry.get(),
            vahed_darkhast_edari_tejari_entry.get(),
            parking_darkhast_edari_tejari_var.get(),
            asansor_darkhast_edari_tejari_var.get(),
            anbari_darkhast_edari_tejari_var.get(),
            aab_va_gaz_combo_emkanat_darkhast_edari_tejari.get(),
            sarmayesh_combo_emkanat_darkhast_edari_tejari.get(),
            garmayesh_combo_emkanat_darkhast_edari_tejari.get(),
            gheimat_kol_darkhast_edari_tejari_entry.get(),
            name_moshtari_darkhast_edari_tejari_entry.get(),
            shomareh_moshtari_darkhast_edari_tejari_entry.get()
            )
            
            cursor.execute(sql_kharid,values_darkhast_kharid_edari_tejari)

            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return
            
        elif change_type=="درخواست اجاره اداری/تجاری":
            cursor.execute( """
            CREATE TABLE IF NOT EXISTS sabt_darkhast_ejareh_edari_tejari (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            sal_sakht VARCHAR(20),
            address VARCHAR(225),
            tabaghe VARCHAR(10),
            vahed VARCHAR(20),
            parking VARCHAR(20),
            asansor VARCHAR(20),
            anbari VARCHAR(20),
            aab_va_gaz VARCHAR(20),
            system_sarmayesh VARCHAR(20),
            system_garmayesh VARCHAR(20),
            mablagh_vadie VARCHAR(20),
            mablagh_ejareh VARCHAR(20),
            name_moshtari VARCHAR(20),
            shomareh_moshtari INT
            )
            """)

            sql_ejareh = """
            INSERT INTO sabt_darkhast_ejareh_edari_tejari
            (type_melk,metraj_melk,sal_sakht,address,tabaghe,vahed,parking,asansor,
            anbari,aab_va_gaz,system_sarmayesh,system_garmayesh,
            mablagh_vadie,mablagh_ejareh,name_moshtari,shomareh_moshtari)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values_darkhast_ejareh_edari_tejari = (
            combo_darkhast_edari_tejari_entry.get(),
            metraj_melk_darkhast_edari_tejari_entry.get(),
            sal_sakht_darkhast_edari_tejari_entry.get(),
            addrres_darkhast_edari_tejari_entry.get(),
            tabaghe_darkhast_edari_tejari_entry.get(),
            vahed_darkhast_edari_tejari_entry.get(),
            parking_darkhast_edari_tejari_var.get(),
            asansor_darkhast_edari_tejari_var.get(),
            anbari_darkhast_edari_tejari_var.get(),
            aab_va_gaz_combo_emkanat_darkhast_edari_tejari.get(),
            sarmayesh_combo_emkanat_darkhast_edari_tejari.get(),
            garmayesh_combo_emkanat_darkhast_edari_tejari.get(),
            mablagh_vadie_darkhast_edari_tejari_entry.get(),
            mablagh_ejareh_darkhast_edari_tejari_entry.get(),
            name_moshtari_darkhast_edari_tejari_entry.get(),
            shomareh_moshtari_darkhast_edari_tejari_entry.get()
            )
            
            cursor.execute(sql_ejareh,values_darkhast_ejareh_edari_tejari)

            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return

        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")      
    except Exception as e:
        messagebox.showerror("Error", f"خطا در ثبت داده: {e}")
        
    finally:
        if db and db.is_connected():
            clear_entry_darkhast_edari_tejari()
            db.close()

#--------------darkhast_bagh/zamin Database-----------------------
selected_option3=[]
selected_trees3=[]
skip_save=False
def sabt_darkhast_bagh_zamin(event=None):
    global skip_save
    db = None
    
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")
        change_type=melk_type_darkhast_bagh_zamin_entry.get()
        karbari = bagh_type_darkhast_bagh_zamin_combo.get()
        gheimat_str =gheimat_har_metr_bagh_zamin_darkhast_entry.get()
        if not gheimat_str or gheimat_str == "":
            gheimat_str = "0"
        gheimat_value = float(gheimat_str)
        gheimat_har_matr_bagh_zamin_darkhast_lable.place_forget()
        gheimat_har_metr_bagh_zamin_darkhast_entry.place_forget()
        gheimat_kol_bagh_zamin_darkhast_lable.place_forget()
        gheimat_kol_bagh_zamin_darkhast_entry.place_forget()
        time_ejareh_bagh_darkhast_zamin_lable.place_forget()
        bagh_time_darkhast_combo.place_forget()
        gheimat_ejareh_bagh_darkhast_zamin_lable.place_forget()
        gheimat_ejareh_bagh_darkhast_zamin_entry.place_forget()
        mablagh_ejareh_mahaneh_darkhast_lable.place_forget()
        mablagh_ejareh_mahaneh_darkhast_entry.place_forget()
        mablagh_ejareh_mahaneh_darkhast_lable.place_forget()
        mablagh_ejareh_mahaneh_darkhast_entry.place_forget()
        gheimat_ejareh_bagh_darkhast_zamin_lable.place_forget()#ودیعه
        gheimat_ejareh_bagh_darkhast_zamin_entry.place_forget()#ودیعه
        gheimat_har_matr_bagh_zamin_darkhast_lable.place_forget()
        gheimat_har_metr_bagh_zamin_darkhast_entry.place_forget()
        gheimat_kol_bagh_zamin_darkhast_lable.place_forget()#قیمت کل
        gheimat_kol_bagh_zamin_darkhast_entry.place_forget()#قیمت کل
        time_ejareh_bagh_darkhast_zamin_lable.place_forget()
        bagh_time_darkhast_combo.place_forget()   
        if change_type=="درخواست خرید باغ زمین":
            gheimat_har_matr_bagh_zamin_darkhast_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")
            gheimat_har_metr_bagh_zamin_darkhast_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)
            gheimat_kol_bagh_zamin_darkhast_lable.place(x=start_x + 325, y=start_y + 390, anchor="e")
            gheimat_kol_bagh_zamin_darkhast_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)
        elif change_type=="درخواست اجاره باغ زمین":
           mablagh_ejareh_mahaneh_darkhast_lable.place(x=start_x + 225, y=start_y + 420, width=100, height=25)
           mablagh_ejareh_mahaneh_darkhast_entry.place(x=start_x + 10, y=start_y + 419, width=150, height=25)
           gheimat_ejareh_bagh_darkhast_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")#ودیعه
           gheimat_ejareh_bagh_darkhast_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)#ودیعه
           time_ejareh_bagh_darkhast_zamin_lable.place(x=start_x + 320, y=start_y +390, anchor="e")
           bagh_time_darkhast_combo.place(x=start_x + 10, y=start_y + 375, width=150, height=25)
        if event is not None:#خیلی مهم 
           return
        

        if change_type=="درخواست خرید باغ زمین":
            if karbari=="باغ":
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS darkhast_kharid_bagh(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_metri DECIMAL(15,2),
                gheimat_kol VARCHAR(30),
                name_malek VARCHAR(50),
                shomareh_malek VARCHAR(30),
                metraj_derakht VARCHAR(10),
                tedad_derakht VARCHAR(10),
                type_derakht TEXT,
                system_ab VARCHAR(25),
                chah VARCHAR(10),
                estakhr VARCHAR(10),
                divar VARCHAR(10),
                sazeh VARCHAR(10),
                metraj_sazeh VARCHAR(10),
                sal_sakht VARCHAR(10),
                type_sazeh VARCHAR(20),
                emkanat TEXT,
                WC VARCHAR(10),
                hamam VARCHAR(10),
                javaz_sakht VARCHAR(10),
                sanad VARCHAR(20),
                mohavate VARCHAR(10),
                bargh VARCHAR (10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
               """) 
                type_derakht_value = ",".join(selected_trees3) if selected_trees3 else ""
                tedad_derakht_value = str(len(selected_trees3)) if selected_trees3 else "0"
                emkanat_value = ",".join(selected_option3) if selected_option3 else ""
            
                sql_bagh = """
                INSERT INTO darkhast_kharid_bagh(
                    type_melk,metraj,karbari,address,mablagh_metri,gheimat_kol,name_malek,shomareh_malek,
                    metraj_derakht, tedad_derakht, type_derakht,
                    system_ab, chah, estakhr, divar,sazeh, metraj_sazeh,
                    sal_sakht, type_sazeh, emkanat, WC, hamam,
                    javaz_sakht, sanad, mohavate,bargh
                )
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s
                ,%s,%s,%s,%s,%s,%s,%s,%s)
                 """
                values_kharid=(
                melk_type_darkhast_bagh_zamin_entry.get(),
                metraj_zamin_darkhast_bagh_zamin_entry.get(),
                karbari,
                bagh_loctaion_darkhast_bagh_zamin_entry.get(),
                gheimat_value,
                name_moshtari_darkhast_bagh_entry.get(),
                shomareh_moshtari_darkhast_bagh_entry.get(),
                gheimat_kol_bagh_zamin_darkhast_entry.get(),
                metraj_derakht_darkhast_bagh_zamin_entry.get(),
                tedad_derakht_darkhast_bagh_zamin_entry.get(),
                type_tree_darkhast_bagh_zamin_combo.get(),
                abyari_darkhast_bagh_zamin_combo.get(),
                chah_darkhast_bagh_zamin_var.get(),
                estakhr_darkhast_bagh_zamin_var.get(),
                divar_darkhast_bagh_zamin_var.get(),
                var0_darkhast_bagh_zamin.get(),
                metraj_vila_darkhast_bagh_zamin_entry.get(),
                sal_sakht_vila_darkhast_bagh_zamin_entry.get(),
                type_vila_darkhast_bagh_zamin_combo.get(),
                toilet_darkhast_bagh_zamin_combo.get(),
                hamam_darkhast_bagh_zamin_combo.get(),
                sanad_darkhast_bagh_zamin_combo.get(),
                option_darkhast_bagh_zamin_combo.get(),
                mojavez_sakht_darkhast_bagh_zamin_var.get(),
                mohavate_sazi_darkhast_bagh_zamin_var.get(),
                bargh_keshi_darkhast_bagh_zamin_var.get()
                )
                cursor.execute(sql_bagh, values_kharid)

                last_id = cursor.lastrowid
                if last_id is None or last_id == 0:
                       messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                       return
            elif karbari=="زمین کشاورزی":
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS darkhast_kharid_zamin(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_metri DECIMAL(15,2),
                name_moshtari VARCHAR(50),
                shomareh_moshtari VARCHAR(30),
                metraj_zamin VARCHAR(30),
                karbari_zamin VARCHAR(50),
                type_khak VARCHAR(20),
                manba_ab VARCHAR(20),
                negahbani VARCHAR(20),
                bargh_takfaz VARCHAR(20),
                bargh_sefaz VARCHAR(20),
                anbar VARCHAR(20),
                fans VARCHAR(20),
                chah VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
                )
                """)

                sql_zamin = """
                INSERT INTO darkhast_kharid_zamin(
                    type_melk,metraj,karbari,address,mablagh_metri,name_moshtari,shomareh_moshtari,
                    metraj_zamin, karbari_zamin,type_khak,
                    manba_ab, negahbani, bargh_takfaz, bargh_sefaz,
                    anbar, fans, chah
                 )
                 VALUES( %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s)
                 """
                values_kharid_zamin=(
                   change_type,
                   metraj_zamin_darkhast_bagh_zamin_entry.get(),
                   karbari,
                   bagh_loctaion_darkhast_bagh_zamin_entry.get(),
                   gheimat_value,
                   name_moshtari_darkhast_bagh_entry.get(),
                   shomareh_moshtari_darkhast_bagh_entry.get(),
                   metraj_zamin2_darkhast_bagh_zamin_entry.get(),
                   karbari_darkhast_bagh_zamin_combo.get(),
                   khak_darkhast_bagh_zamin_combo.get(),
                   ab_darkhast_bagh_zamin_combo.get(),
                   security_zamin_darkhast_bagh_zamin_var.get(),
                   bargh_kesi_zamin_darkhast_bagh_zamin_var.get(),
                   bargh_zamin_darkhast_bagh_zamin2_var.get(),
                   anbar_zamin_darkhast_bagh_zamin_var.get(),
                   fans_zamin_darkhast_bagh_zamin_var.get(),
                   mojavez_chah_zamin_darkhast_bagh_zamin_var.get())
                   
                cursor.execute(sql_zamin,values_kharid_zamin)
                last_id = cursor.lastrowid
                if last_id is None or last_id == 0:
                        messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                        return
            
        
        elif change_type=="درخواست اجاره باغ زمین":
            if karbari=="باغ":
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS darkhast_ejareh_bagh(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                name_moshtari VARCHAR(50),
                shomareh_moshtari VARCHAR(30),
                zaman_ejareh VARCHAR(40),
                mablagh_pish VARCHAR(30),
                mablagh_ejareh VARCHAR(30),
                metraj_derakht VARCHAR(10),
                tedad_derakht VARCHAR(10),
                type_derakht TEXT,
                system_ab VARCHAR(25),
                chah VARCHAR(10),
                estakhr VARCHAR(10),
                divar VARCHAR(10),
                sazeh VARCHAR(10),
                metraj_sazeh VARCHAR(10),
                sal_sakht VARCHAR(10),
                type_sazeh VARCHAR(20),
                emkanat TEXT,
                WC VARCHAR(10),
                hamam VARCHAR(10),
                javaz_sakht VARCHAR(10),
                sanad VARCHAR(20),
                mohavate VARCHAR(10),
                bargh VARCHAR (10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
               """) 
                type_derakht_value = ",".join(selected_trees3) if selected_trees3 else ""
                tedad_derakht_value = str(len(selected_trees3)) if selected_trees3 else "0"
                emkanat_value = ",".join(selected_option3) if selected_option3 else ""
            
                sql_bagh = """
                INSERT INTO darkhast_ejareh_bagh(
                    type_melk,metraj,karbari,address,name_moshtari,shomareh_moshtari,
                    zaman_ejareh,mablagh_pish,mablagh_ejareh,
                    metraj_derakht, tedad_derakht, type_derakht,
                    system_ab, chah, estakhr, divar,sazeh, metraj_sazeh,
                    sal_sakht, type_sazeh, emkanat, WC, hamam,
                    javaz_sakht, sanad, mohavate,bargh
                )
                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s,%s
                ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                 """
                values_ejareh=(
                melk_type_darkhast_bagh_zamin_entry.get(),
                metraj_zamin_darkhast_bagh_zamin_entry.get(),
                karbari,
                bagh_loctaion_darkhast_bagh_zamin_entry.get(),
                name_moshtari_darkhast_bagh_entry.get(),
                shomareh_moshtari_darkhast_bagh_entry.get(),
                bagh_time_darkhast_combo.get(),
                gheimat_ejareh_bagh_darkhast_zamin_entry.get(),
                mablagh_ejareh_mahaneh_darkhast_entry.get(),
                metraj_derakht_darkhast_bagh_zamin_entry.get(),
                tedad_derakht_darkhast_bagh_zamin_entry.get(),
                type_tree_darkhast_bagh_zamin_combo.get(),
                abyari_darkhast_bagh_zamin_combo.get(),
                chah_darkhast_bagh_zamin_var.get(),
                estakhr_darkhast_bagh_zamin_var.get(),
                divar_darkhast_bagh_zamin_var.get(),
                var0_darkhast_bagh_zamin.get(),
                metraj_vila_darkhast_bagh_zamin_entry.get(),
                sal_sakht_vila_darkhast_bagh_zamin_entry.get(),
                type_vila_darkhast_bagh_zamin_combo.get(),
                toilet_darkhast_bagh_zamin_combo.get(),
                hamam_darkhast_bagh_zamin_combo.get(),
                sanad_darkhast_bagh_zamin_combo.get(),
                option_darkhast_bagh_zamin_combo.get(),
                mojavez_sakht_darkhast_bagh_zamin_var.get(),
                mohavate_sazi_darkhast_bagh_zamin_var.get(),
                bargh_keshi_darkhast_bagh_zamin_var.get()
                )
                cursor.execute(sql_bagh, values_ejareh)

                last_id = cursor.lastrowid
                if last_id is None or last_id == 0:
                       messagebox.showerror("Error", "خطا: ثبت در جدول")
                       return
            elif karbari=="زمین کشاورزی":
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS darkhast_ejareh_zamin(
                id INT AUTO_INCREMENT PRIMARY KEY,
                type_melk VARCHAR(50) NOT NULL,
                metraj VARCHAR(20),
                karbari VARCHAR(20),
                address VARCHAR(255),
                mablagh_pish VARCHAR(30),
                mablagh_ejareh VARCHAR(30),
                zaman_ejareh VARCHAR(40),
                name_moshtari VARCHAR(50),
                shomareh_moshtari VARCHAR(30),
                metraj_zamin VARCHAR(30),
                karbari_zamin VARCHAR(50),
                type_khak VARCHAR(20),
                manba_ab VARCHAR(20),
                negahbani VARCHAR(20),
                bargh_takfaz VARCHAR(20),
                bargh_sefaz VARCHAR(20),
                anbar VARCHAR(20),
                fans VARCHAR(20),
                chah VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
                )
              """)

                sql_zamin = """
                INSERT INTO darkhast_ejareh_zamin(
                    type_melk,metraj,karbari,address,mablagh_pish,mablagh_ejareh,zaman_ejareh,name_moshtari,shomareh_moshtari,
                    metraj_zamin, karbari_zamin,type_khak,
                    manba_ab,negahbani,bargh_takfaz,bargh_sefaz,
                    anbar,fans,chah
                 )
                VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                values_ejareh_zamin=(
                   change_type,
                   metraj_zamin_darkhast_bagh_zamin_entry.get(),
                   karbari,
                   bagh_loctaion_darkhast_bagh_zamin_entry.get(),
                   gheimat_ejareh_bagh_darkhast_zamin_entry.get(),
                   mablagh_ejareh_mahaneh_darkhast_entry.get(),
                   bagh_time_darkhast_combo.get(),
                   name_moshtari_darkhast_bagh_entry.get(),
                   shomareh_moshtari_darkhast_bagh_entry.get(),
                   metraj_zamin2_darkhast_bagh_zamin_entry.get(),
                   karbari_darkhast_bagh_zamin_combo.get(),
                   khak_darkhast_bagh_zamin_combo.get(),
                   ab_darkhast_bagh_zamin_combo.get(),
                   security_zamin_darkhast_bagh_zamin_var.get(),
                   bargh_kesi_zamin_darkhast_bagh_zamin_var.get(),
                   bargh_zamin_darkhast_bagh_zamin2_var.get(),
                   anbar_zamin_darkhast_bagh_zamin_var.get(),
                   fans_zamin_darkhast_bagh_zamin_var.get(),
                   mojavez_chah_zamin_darkhast_bagh_zamin_var.get())
            
                cursor.execute(sql_zamin,values_ejareh_zamin)
                last_id = cursor.lastrowid
                if last_id is None or last_id == 0:
                       messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                       return    
                        
        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")      
    except Exception as e:
        messagebox.showerror("Error", f"خطا در ثبت داده: {e}")
        
    finally:
        if db and db.is_connected():
            clear_entry_darkhast_bagh_zamin()
            db.close()
                
#------------darkhast_kargah Database--------------------------
skip_save=False
def sabt_darkhast_kargah(event=None):
    global skip_save
    db = None
    try:
        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency")
        cursor.execute("USE state_agency")

        change_type= combo_darkhast_kargah.get()
        #فیلد های خرید
        mablagh_pish_darkhast_kargah_lable.place_forget()
        mablagh_pish_darkhast_kargah_entry.place_forget()
        #فیلد های اجاره
        mablagh_pish_darkhast_kargah_lable.place_forget()
        mablagh_pish_darkhast_kargah_entry.place_forget()
        gheimat_kol_darkhast_kargah_lable.place_forget()
        gheimat_kol_darkhast_kargah_entry.place_forget()
        ejareh_mahaneh_darkhast_kargah_lable.place_forget()
        ejareh_mahaneh_darkhast_kargah_entry.place_forget()
        # فیلد های مشترک
        name_moshtari_darkhast_kargah_lable.place_forget()
        name_moshtari_darkhast_kargah_entry.place_forget()
        shomareh_moshtari_darkhast_kargah_lable.place_forget()
        shomareh_moshtari_darkhast_kargah_entry.place_forget()

        if change_type=="درخواست خرید کارگاه":
            gheimat_kol_darkhast_kargah_lable.place(x=start_x + 320, y=start_y +274,anchor="e")
            gheimat_kol_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 218,width=150, height=25)
            name_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 180, anchor="e")
            name_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 170, width=150, height=25)
            shomareh_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 230, anchor="e")
            shomareh_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 260, width=150, height=25)

        elif change_type=="درخواست اجاره کارگاه":
           
            mablagh_pish_darkhast_kargah_lable.place(x=start_x + 320, y=start_y +180,anchor="e")
            mablagh_pish_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 170,width=150, height=25)
            name_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 230, anchor="e")
            name_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 218, width=150, height=25)
            shomareh_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 274, anchor="e")
            shomareh_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 260, width=150, height=25)
            ejareh_mahaneh_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 320, anchor="e")
            ejareh_mahaneh_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 310, width=150, height=25)


        if event is not None:#خیلی مهم 
           return
        
        if change_type=="درخواست خرید کارگاه":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sabt_darkhast_kharid_kargah(
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            address VARCHAR(225),
            name_moshtari VARCHAR(30),
            shomareh_moshtari INT, 
            gheimat_kol VARCHAR(20),              
            sal_sakht VARCHAR(20),
            vaziat_bargh VARCHAR(20),
            garmayesh VARCHAR(20),
            sarmayesh_fan VARCHAR(20),
            sarmayesh_panke VARCHAR(20),
            sarmayesh_kooler_abi VARCHAR(20),
            sarmayesh_kooler_gazi VARCHAR(20),
            vaziat_ab VARCHAR(100),
            abzar VARCHAR(100),
            toilet VARCHAR(20),
            hamam VARCHAR(20),
            otagh VARCHAR(20)
            )
            """)

            sql_kharid = """
            INSERT INTO sabt_darkhast_kharid_kargah
            (type_melk,metraj_melk,address,name_moshtari,shomareh_moshtari,gheimat_kol,sal_sakht,
            vaziat_bargh,garmayesh,sarmayesh_fan,
            sarmayesh_panke,sarmayesh_kooler_abi,sarmayesh_kooler_gazi,vaziat_ab,
            abzar,toilet,hamam,otagh)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values_darkhast_kharid_kargah = (
            combo_darkhast_kargah.get(),
            metraj_darkhast_kargah_entry.get(),
            loctaion_darkhast_kargah_entry.get(),
            name_moshtari_darkhast_kargah_entry.get(),
            shomareh_moshtari_darkhast_kargah_entry.get(),
            gheimat_kol_darkhast_kargah_entry.get(),
            sal_sakht_darkhast_kargah_entry.get(),
            vaziat_bargh_darkhast_kargah_combo.get(),
            garmayesh_type_darkhast_kargah_combo.get(),
            sarmayesh_fan_darkhast_kargah_var.get(),
            sarmayesh_panke_darkhast_kargah_var.get(),
            sarmayesh_kooler_abi_darkhast_kargah_var.get(),
            sarmayesh_kooler_gazi_darkhast_kargah_var.get(),
            vaziat_ab_darkhast_kargah_combo.get(),
            abzaar_darkhast_kargah_combo.get(),
            toilet_darkhast_kargah_combo.get(),
            hamam_darkhast_kargah__combo.get(),
            otagh_darkhast_kargah_combo.get()
            )
            
            cursor.execute(sql_kharid,values_darkhast_kharid_kargah)

            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return
            
        elif change_type=="درخواست اجاره کارگاه":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sabt_darkhast_ejareh_kargah(
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_melk VARCHAR(50) NOT NULL,
            metraj_melk VARCHAR(20),
            address VARCHAR(225),
            mablagh_pish VARCHAR(20),
            name_moshtari VARCHAR(30),
            shomareh_moshtari INT,
            ejareh_mahaneh VARCHAR(20),
            sal_sakht VARCHAR(20),
            vaziat_bargh VARCHAR(20),
            garmayesh VARCHAR(20),
            sarmayesh_fan VARCHAR(40),
            sarmayesh_panke VARCHAR(40),
            sarmayesh_kooler_abi VARCHAR(40),
            sarmayesh_kooler_gazi VARCHAR(40),
            vaziat_ab VARCHAR(100),
            abzar VARCHAR(100),
            toilet VARCHAR(20),
            hamam VARCHAR(20),
            otagh VARCHAR(20)
            )
            """)

            sql_ejareh = """
            INSERT INTO sabt_darkhast_ejareh_kargah
            (type_melk,metraj_melk,address,mablagh_pish,name_moshtari,shomareh_moshtari,
            ejareh_mahaneh,sal_sakht,vaziat_bargh,garmayesh,sarmayesh_fan,
            sarmayesh_panke,sarmayesh_kooler_abi,sarmayesh_kooler_gazi,vaziat_ab,
            abzar,toilet,hamam,otagh)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values_darkhast_ejareh_kargah = (
            combo_darkhast_kargah.get(),
            metraj_darkhast_kargah_entry.get(),
            loctaion_darkhast_kargah_entry.get(),
            mablagh_pish_darkhast_kargah_entry.get(),
            name_moshtari_darkhast_kargah_entry.get(),
            shomareh_moshtari_darkhast_kargah_entry.get(),
            ejareh_mahaneh_darkhast_kargah_entry.get(),
            sal_sakht_darkhast_kargah_entry.get(),
            vaziat_bargh_darkhast_kargah_combo.get(),
            garmayesh_type_darkhast_kargah_combo.get(),
            sarmayesh_fan_darkhast_kargah_var.get(),
            sarmayesh_panke_darkhast_kargah_var.get(),
            sarmayesh_kooler_abi_darkhast_kargah_var.get(),
            sarmayesh_kooler_gazi_darkhast_kargah_var.get(),
            vaziat_ab_darkhast_kargah_combo.get(),
            abzaar_darkhast_kargah_combo.get(),
            toilet_darkhast_kargah_combo.get(),
            hamam_darkhast_kargah__combo.get(),
            otagh_darkhast_kargah_combo.get()
            )
            
            cursor.execute(sql_ejareh,values_darkhast_ejareh_kargah)

            last_id = cursor.lastrowid
            if last_id is None or last_id == 0:
                messagebox.showerror("Error", "خطا: ثبت در جدول  انجام نشد")
                return

        db.commit()
        user_idcode = f"ID-{last_id}"
        messagebox.showinfo("Success", f"ثبت با کد {user_idcode} انجام شد.")      
    except Exception as e:
        messagebox.showerror("Error", f"خطا در ثبت داده: {e}")
        
    finally:
        if db and db.is_connected():
            clear_entry_darkhast_kargah()
            db.close()
#--------------------پایان تابع ثبت درخواست----------------
#endregion
#----------------------------سیو تصاویر--------------------------
#===================سیو تصاویر در پنجره فروش اداری و تجاری================
#region
def open_file_forosh_edari_tejari():

    global selected_images_forosh_edari_tejari
    global photo_refs_forosh_edari_tejari

    file_paths = filedialog.askopenfilenames(
        title="انتخاب تصاویر ملک",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")
        ]
    )

    # حداکثر 4 تصویر
    file_paths = list(file_paths[:4])

    # ساخت پوشه روی دسکتاپ
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    save_folder = os.path.join(desktop_path, "Forosh_Edari_Tejari")

    os.makedirs(save_folder, exist_ok=True)

    new_paths = []

    # کپی تصاویر به پوشه پروژه
    for path in file_paths:

        filename = os.path.basename(path)

        destination = os.path.join(save_folder, filename)

        shutil.copy2(path, destination)

        new_paths.append(destination)

    # ذخیره مسیرهای جدید
    selected_images_forosh_edari_tejari = new_paths

    # پاک کردن تصاویر قبلی
    for widget in image_frame_forosh_edari_tejari.winfo_children():
        widget.destroy()

    photo_refs_forosh_edari_tejari.clear()

    # نمایش تصاویر
    for i, path in enumerate(selected_images_forosh_edari_tejari):

        try:

            img = Image.open(path)

            img.thumbnail((150, 110))

            photo = ImageTk.PhotoImage(img)

            photo_refs_forosh_edari_tejari.append(photo)

            lbl = tk.Label(image_frame_forosh_edari_tejari,image=photo,bg="white",bd=1,relief="solid")

            lbl.grid(row=i // 2,column=i % 2,padx=5,pady=5)

        except Exception as e:
            print("خطا در بارگذاری تصویر:", e)
#endregion
#------------------------توابع سرچ--------------------
#regoin
def search():
    file = combo_file_type.get()
    melk = melk_type_combo.get()

    db = get_connection()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS state_agency") 
    cursor.execute("USE state_agency")

    try:
        if file == "فروش":

            if melk == "مسکونی":
                cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_forosh_maskoni
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))

            elif melk == "مغازه_تجاری":
                cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_forosh_edari_tejari
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))

            elif melk == "زمین":
                cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM forosh_zamin
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))

            elif melk == "باغ":
                cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM forosh_bagh
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))

            elif melk == "کارگاه":
                cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_forosh_kargah
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
        elif file=="رهن_اجاره":
            if melk=="مسکونی":
                    cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_ejareh_maskoni
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
            elif melk == "مغازه_تجاری":
                    cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_ejareh_edari_tejari
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
            elif melk == "زمین":
                    cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM ejareh_zamin
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
            elif melk == "باغ":
                    cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM ejareh_bagh
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
            elif melk == "کارگاه":
                    cursor.execute("""
                    SELECT address, gheimat_kol, type_melk, name_malek
                    FROM sabt_forosh_kargah
                    WHERE address LIKE %s
                """, (f"%{address_entry.get().strip()}%",))
        elif file=="درخواستی":
            pass






        else:
            messagebox.showerror("خطا", "نوع ملک نامعتبر است")
            return

        results = cursor.fetchall()

        # پاک کردن نتایج قبلی
        for item in tree.get_children():
            tree.delete(item)

        if results:
            for row in results:
                tree.insert("", "end", values=row)
        else:
           messagebox.showinfo("یافت نشد", "هیچ موردی پیدا نشد")

    except Exception as e:
        messagebox.showerror("Error", f"خطا: {e}")

    finally:
        cursor.close()
        db.close()
#endregion
#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------
# ---------دکمه فایل با منوی کشویی ------------------
#region 
menubar = tk.Menu(root, font=("Shabnam", 10))
# ایجاد منوی "ثبت فایل ها"
file_menu_sabt_file = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_sabt_file.add_command(label="فروش", command=forosh)
file_menu_sabt_file.add_command(label="رهن/اجاره", command=rahn)
file_menu_sabt_file.add_command(label="مشارکت", command=mosharecat)

# اضافه کردن منوی "ثبت فایل ها" به منوبار
menubar.add_cascade(label="ثبت فایل ها", menu=file_menu_sabt_file)

# اتصال منوبار به پنجره
root.config(menu=menubar)
#endregion
# ---------------اضافه کردن فیلد قرارداد ---------------
#region
file_menu_gharardad= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_gharardad.add_command(label="ثبت قراردادها", command=open_ghrardad)
# اضافه کردن منوی قرار دادها به منوبار
menubar.add_cascade(label="قراردادها", menu=file_menu_gharardad)
#endregion
#----------------دکمه گزارش ها با منوی کشویی ------------------------
#region
# ----------لیست کشویی فیلد گزارش ها-----------------
file_menu_gozaresh = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_gozaresh.add_command(label="خروجی اکسل", command=gozaresh)
file_menu_gozaresh.add_command(label="قراردادها", command=None)
# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="گزارش ها", menu=file_menu_gozaresh)
#endregion
# ----------------------اضافه کردن فیلد درخواست ها-------
#region
file_menu_darkhast= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_darkhast.add_command(label="درخواست خرید و اجاره", command=darkhast)

# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="درخواست ها", menu=file_menu_darkhast)
#endregion
#-------------------------اضافه کردن فیلد کاربران---------
#region
file_menu_karbaran= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_karbaran.add_command(label="", command=None)
file_menu_karbaran.add_command(label="", command=None)

# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="کاربران", menu=file_menu_karbaran)
#endregion
#========================================================
# -----------باکس سمت چپ - جستجو در فایل های ملک----------
#region
contant_frame=tk.Frame(root)
contant_frame.pack(fill="both",expand=True)
frame_jostojo_melk_left= tk.LabelFrame(contant_frame, text="جستجوی ملک", width=200, bg="#052340",fg="#00BFFF", font=("Shabnam", 16))
frame_jostojo_melk_left.pack(side="left", fill="both",expand=True, padx=6, pady=15)

box_jostojo_malk1= tk.Frame(frame_jostojo_melk_left,bg="#052340")
box_jostojo_malk1.pack(padx=6, pady=15)

file_type = tk.Label(box_jostojo_malk1,text="نوع فایل",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
file_type.pack(padx=15,pady=10, side="right")
combo_file_type= ttk.Combobox(box_jostojo_malk1)
combo_file_type["values"] = ("رهن_اجاره","درخواستی","فروش","مشارکت",)
combo_file_type["state"]=["readonly"]
combo_file_type.pack(padx=10, pady=10) 

box_jostojo_malk2= tk.Frame(frame_jostojo_melk_left,bg="#052340")
box_jostojo_malk2.pack(padx=6, pady=15)

melk_type_lable = tk.Label(box_jostojo_malk2,text="نوع ملک",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
melk_type_lable.pack(padx=15,pady=10, side="right")
melk_type_combo= ttk.Combobox(box_jostojo_malk2)
melk_type_combo["values"] = ("مسکونی","مغازه_تجاری","زمین","کارگاه","باغ")
melk_type_combo["state"]=["readonly"]
melk_type_combo.pack(padx=10, pady=10) 

box_jostojo_malk3 = tk.Frame(frame_jostojo_melk_left,bg="#052340")
box_jostojo_malk3.pack(padx=6, pady=5)

melk_mahdode_gheimat_lable = tk.Label(box_jostojo_malk3,text="محدوده قیمت",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
melk_mahdode_gheimat_lable.pack(padx=5, pady=1)

melk_mahdode_gheimat_entry = tk.Entry(box_jostojo_malk3,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
melk_mahdode_gheimat_entry.pack(padx=20,pady=10)


mahdode_ta_lable = tk.Label(box_jostojo_malk3,text="تا",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
mahdode_ta_lable.pack(padx=5, pady=1)

mahdode_ta_entry = tk.Entry(box_jostojo_malk3,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
mahdode_ta_entry.pack(padx=20,pady=10)


metraj_lable = tk.Label(box_jostojo_malk3,text=" متراژ",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
metraj_lable.pack(padx=5, pady=1)
metraj_entry = tk.Entry(box_jostojo_malk3,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
metraj_entry.pack(padx=20,pady=10)

address_lable = tk.Label(box_jostojo_malk3,text=" منطقه / آدرس",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
address_lable.pack(padx=5, pady=1)
address_entry = tk.Entry(box_jostojo_malk3,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
address_entry.pack(padx=20,pady=10)

# ---------------------دکمه جستجوی ملک-----------------
search_btn = tk.Button(frame_jostojo_melk_left, text="    جستجو    " , bg="#00BFFF", fg="#000000", font=("Shabnam", 13), command=search)
search_btn.pack(pady=10)
#=====================================================
#endregion
# ---------------------------باکس وسط - نمایش جستجوی --------------
#region
frame_list_amlack_centre = tk.LabelFrame(contant_frame, text="لیست املاک", bg="#052340",fg="#00BFFF", font=("Shabnam", 13))
frame_list_amlack_centre.pack(side="left", fill="both", expand=True, padx=4, pady=15)

columns = ["آدرس", "قیمت ", "نوع ملک ", "نام مالک"]
tree = ttk.Treeview(frame_list_amlack_centre, columns=columns, show="headings")
for textt in columns:
    tree.heading(textt,text=textt)
    tree.column(textt, width=100)
tree.pack(fill="both", expand=True)

lable_list_amlack_centre = tk.Label(frame_list_amlack_centre,text="تمامی حقوق قانونی این نرم افزار متعلق به گروه نیواد است",bg="#052340", fg="white",font=("Shabnam", 10))
lable_list_amlack_centre.pack(padx=10)
#===================================================
#endregion
# --------------------باکس سمت راست - نمایش جزئیات فایل های موجود املاک---------------
#region
frame_joziat_amlack = tk.LabelFrame(contant_frame, text="جزئیات ملک", width=200, bg="#052340",fg="#00BFFF", font=("Shabnam", 13))
frame_joziat_amlack.pack(side="right", fill="both",expand=True, padx=6, pady=15)

photo_melk_lbl = tk.Label(frame_joziat_amlack, text="[تصویر ملک]", bg="#FFFFFF", width=20, height=10)
photo_melk_lbl.pack(pady=10)

malek = tk.Label(frame_joziat_amlack,text="نام مالک",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
malek.pack(padx=6,pady=4)

entry_malek = tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
entry_malek.pack(padx=20,pady=4)

malek_phone_number = tk.Label(frame_joziat_amlack,text="شماره مالک",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
malek_phone_number.pack(padx=6,pady=4)

entry_malek_phone_number = tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
entry_malek_phone_number.pack(padx=20,pady=4)

metraj_lable_right= tk.Label(frame_joziat_amlack,text="متراژ ",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
metraj_lable_right.pack(padx=6,pady=4)

metraj_lable_right_entry = tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
metraj_lable_right_entry.pack(padx=20,pady=4)

gheimat_melk_right_lable = tk.Label(frame_joziat_amlack,text="قیمت ",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
gheimat_melk_right_lable.pack(padx=6,pady=4)

gheimat_melk_right_entry= tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
gheimat_melk_right_entry.pack(padx=20,pady=4)

tozihat_right_lable = tk.Label(frame_joziat_amlack,text="توضیحات ",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
tozihat_right_lable.pack(padx=6,pady=4)

tozihat_right_entry = tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
tozihat_right_entry.pack(padx=20,pady=4)
#=======================================================
#endregion
#-------------------------باکس های نوع ثبتی فایل ها----------------------
#-------------------نوع انتخاب ثبتی فایل برای پنجره های رهن و اجاره--------------
#region
box_rehn_ejareh=tk.Toplevel(root)
box_rehn_ejareh.title("انتخاب نوع ملک رهن و اجاره")
box_rehn_ejareh.geometry("500x270")
box_rehn_ejareh.withdraw()
box_rehn_ejareh.configure(bg="#052340")

ejareh_radio_value = tk.IntVar(value=0)

ejareh_maskoni_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل مسکونی",background="#052340",fg="#00BFFF",variable=ejareh_radio_value,value=0,font=("Shabnam", 11))
ejareh_maskoni_radio.place(x=330, y=50)

ejareh_edari_radio = tk.Radiobutton( box_rehn_ejareh,text="ثبت فایل اداری/تجاری",
    bg="#052340",fg="#00BFFF",
    variable=ejareh_radio_value,
    value=2,
    font=("Shabnam", 11))
ejareh_edari_radio.place(x=330, y=90)

ejareh_bagh_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل باغ/زمین",bg="#052340",fg="#00BFFF",
    variable=ejareh_radio_value,
    value=4,
    font=("Shabnam", 11))
ejareh_bagh_radio.place(x=330, y=130)

ejareh_kargah_radio = tk.Radiobutton(box_rehn_ejareh,text="ثبت فایل کارگاه",bg="#052340",fg="#00BFFF",variable=ejareh_radio_value,value=6,
    font=("Shabnam", 11))
ejareh_kargah_radio.place(x=330, y=170)

back_to_home_box_ejareh=tk.Button(box_rehn_ejareh,text="بازگشت",bg="#00BFFF",fg="#000000",width=12,height=2,command=back_rehn_ejareh_exit)
back_to_home_box_ejareh.place(x=190,y=210)


zakhire_radio_box_ejareh=tk.Button(box_rehn_ejareh,text="ادامه",bg="#00BFFF",fg="#000000",width=12,height=2,command=sabt_radio_rehn)
zakhire_radio_box_ejareh.place(x=50,y=210)

box_rehn_ejareh.protocol("WM_DELETE_WINDOW", lambda: None)
box_rehn_ejareh.resizable(False, False) 

#=====================================================================
#endregion
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های فروش-----------------
#region
box_forosh=tk.Toplevel(root)
box_forosh.title("انتخاب نوع ملک فروش")
box_forosh.geometry("500x270")
box_forosh.withdraw()
box_forosh.configure(bg="#052340")

# یک متغیر مشترک برای همه رادیوباتن‌ها
forosh_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

forosh_maskoni_radio = tk.Radiobutton(box_forosh, value=0, text="ثبت فایل مسکونی", background="#052340",fg="#00BFFF", variable=forosh_radio_value, font=("Shabnam",11))
forosh_maskoni_radio.place(x=330,y=50)

forosh_edari_radio = tk.Radiobutton(box_forosh, value=2, text="ثبت فایل اداری/تجاری",bg="#052340",fg="#00BFFF", variable=forosh_radio_value, font=("Shabnam",11))
forosh_edari_radio.place(x=330,y=90)

forosh_bagh_radio = tk.Radiobutton(box_forosh, value=4, text="ثبت فایل باغ/زمین",bg="#052340",fg="#00BFFF", variable=forosh_radio_value, font=("Shabnam",11))
forosh_bagh_radio.place(x=330,y=130)

forosh_kargah_radio = tk.Radiobutton(box_forosh, value=6, text="ثبت فایل کارگاه",bg="#052340",fg="#00BFFF", variable=forosh_radio_value, font=("Shabnam",11))
forosh_kargah_radio.place(x=330,y=170)


back_to_home_box_forosh=tk.Button(box_forosh,text="بازگشت",bg="#00BFFF",fg="#000000",width=12,height=2,command=back_forosh_exit)
back_to_home_box_forosh.place(x=190,y=210)

zakhire_radio_box_forosh=tk.Button(box_forosh,text="ادامه",bg="#00BFFF",fg="#000000",width=12,height=2,command=sabt_radio_frosh)
zakhire_radio_box_forosh.place(x=50,y=210)

box_forosh.protocol("WM_DELETE_WINDOW", lambda: None)
box_forosh.resizable(False, False) 




#======================================================================
#endregion
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های درخواستی-----------------
#region
box_darkhast=tk.Toplevel(root)
box_darkhast.title("انتخاب نوع ملک درخواستی")
box_darkhast.geometry("500x270")
box_darkhast.withdraw()
box_darkhast.configure(bg="#052340")

# یک متغیر مشترک برای همه رادیوباتن‌ها
darkhast_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

darkhast_maskoni_radio = tk.Radiobutton(box_darkhast, value=0, text="ثبت درخواست مسکونی", background="#052340",fg="#00BFFF", variable=darkhast_radio_value, font=("Shabnam",11))
darkhast_maskoni_radio.place(x=295,y=50)

darkhast_edari_radio = tk.Radiobutton(box_darkhast, value=2, text="ثبت درخواست اداری/تجاری",bg="#052340",fg="#00BFFF", variable=darkhast_radio_value, font=("Shabnam",11))
darkhast_edari_radio.place(x=295,y=90)

darkhast_bagh_radio = tk.Radiobutton(box_darkhast, value=4, text="ثبت درخواست باغ/زمین",bg="#052340",fg="#00BFFF", variable=darkhast_radio_value, font=("Shabnam",11))
darkhast_bagh_radio.place(x=295,y=130)

darkhast_kargah_radio = tk.Radiobutton(box_darkhast, value=6, text="ثبت درخواست کارگاه",bg="#052340",fg="#00BFFF", variable=darkhast_radio_value, font=("Shabnam",11))
darkhast_kargah_radio.place(x=295,y=170)


back_to_home_box_darkhast=tk.Button(box_darkhast,text="بازگشت",bg="#00BFFF",fg="#000000",width=12,height=2,command=back_darkhast_exit)
back_to_home_box_darkhast.place(x=190,y=210)

zakhire_radio_box_darkhast=tk.Button(box_darkhast,text="ادامه",bg="#00BFFF",fg="#000000",width=12,height=2,command=sabt_radio_darkhast)
zakhire_radio_box_darkhast.place(x=50,y=210)

box_darkhast.protocol("WM_DELETE_WINDOW", lambda: None)
box_darkhast.resizable(False, False)
#endregion 
#---------------------------------نوع انتخاب ثبتی فایل برای  پنجره خروجی گزارش------------
#region
box_gozaresh=tk.Toplevel(root)
box_gozaresh.title("انتخاب نوع ملکی گزارش")
box_gozaresh.geometry("500x270")
box_gozaresh.withdraw()
box_gozaresh.configure(bg="#052340")

# یک متغیر مشترک برای همه رادیوباتن‌ها
gozaresh_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

gozaresh_maskoni_radio = tk.Radiobutton(box_gozaresh, value=0, text="گزارش مسکونی", background="#052340",fg="#00BFFF", variable=gozaresh_radio_value, font=("Shabnam",11))
gozaresh_maskoni_radio.place(x=295,y=50)

gozaresh_edari_radio = tk.Radiobutton(box_gozaresh, value=2, text="گزارش اداری/تجاری",bg="#052340",fg="#00BFFF", variable=gozaresh_radio_value, font=("Shabnam",11))
gozaresh_edari_radio.place(x=295,y=90)

gozaresh_bagh_radio = tk.Radiobutton(box_gozaresh, value=4, text="گزارش باغ/زمین",bg="#052340",fg="#00BFFF", variable=gozaresh_radio_value, font=("Shabnam",11))
gozaresh_bagh_radio.place(x=295,y=130)

gozaresh_kargah_radio = tk.Radiobutton(box_gozaresh, value=6, text="گزارش کارگاه",bg="#052340",fg="#00BFFF", variable=gozaresh_radio_value, font=("Shabnam",11))
gozaresh_kargah_radio.place(x=295,y=170)


back_to_home_box_gozaresh=tk.Button(box_gozaresh,text="بازگشت",bg="#00BFFF",fg="#000000",width=12,height=2,command=back_gozaresh_exit)
back_to_home_box_gozaresh.place(x=190,y=210)

zakhire_radio_box_gozaresh=tk.Button(box_gozaresh,text="ادامه",bg="#00BFFF",fg="#000000",width=12,height=2,command=sabt_radio_gozaresh)
zakhire_radio_box_gozaresh.place(x=50,y=210)

box_gozaresh.protocol("WM_DELETE_WINDOW", lambda: None)
box_gozaresh.resizable(False, False)
#endregion
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های مشارکت-----------------
#region
box_mosharekat=tk.Toplevel(root)
box_mosharekat.title("انتخاب نوع ملک مشارکت")
box_mosharekat.geometry("350x300")
box_mosharekat.withdraw()
box_mosharekat.configure(bg="#052340")

# یک متغیر مشترک برای همه رادیوباتن‌ها
mosharekat_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

mosharekat_sakht_radio = tk.Radiobutton(box_mosharekat, value=0, text="مشارکت در ساخت", background="#052340",fg="#00BFFF", variable=mosharekat_radio_value, font=("Shabnam",11))
mosharekat_sakht_radio.place(x=200,y=50)

mosharekat_pishforosh_radio = tk.Radiobutton(box_mosharekat, value=2, text="پیش فروش",
bg="#052340",fg="#00BFFF", variable=mosharekat_radio_value, font=("Shabnam",11))
mosharekat_pishforosh_radio.place(x=200,y=90)

back_to_home_box_mosharekat=tk.Button(box_mosharekat,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_mosharekat_exit)
back_to_home_box_mosharekat.place(x=190,y=210)

zakhire_radio_box_mosharekat=tk.Button(box_mosharekat,text="ادامه",bg="#00BFFF",fg="#000000",width=10,height=2,command=sabt_radio_mosharekat)
zakhire_radio_box_mosharekat.place(x=50,y=210)

box_mosharekat.protocol("WM_DELETE_WINDOW", lambda: None)
box_mosharekat.resizable(False, False)
#endregion
#-----------------پنجره های ثبتی بخش رهن و اجاره----------------------------
#--------------------------پنجره اجاره مسکونی----------------
#region
ejareh_rehn_page = tk.Toplevel(root)
ejareh_rehn_page.title("رهن و اجاره مسکونی")
ejareh_rehn_page.geometry("800x600")
ejareh_rehn_page.withdraw()

# بارگذاری تصویر
bg_image = image_ejareh_maskoni
bg_image = image_ejareh_maskoni.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(ejareh_rehn_page, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

 
#----------------------پنجره امکانات اجاره مسکونی-----------------------------
option_file_frame_ejareh_maskoni=tk.Toplevel(ejareh_rehn_page)
option_file_frame_ejareh_maskoni.title("امکانات اجاره مسکونی ")
option_file_frame_ejareh_maskoni.geometry("500x370")
option_file_frame_ejareh_maskoni.pack_propagate(False)
option_file_frame_ejareh_maskoni.withdraw()

#------------------کادر اجاره مسکونی------------#

frame_rehn_ejareh_maskoni = tk.Frame(ejareh_rehn_page,bd=0,highlightthickness=0)
frame_rehn_ejareh_maskoni.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(ejareh_rehn_page,text="رهن و اجاره مسکونی",bg="#000000",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)   

# تعیین نقطه شروع (جایی که فریم قبلی قرار داشت)
start_x = 450
start_y = 40

# ----------------------------  ویجت‌ها مستقیماً روی عکس ----------------------------

# ردیف 1: نوع ملک
melk_type_ejareh_maskoni_lable = tk.Label(ejareh_rehn_page, text="نوع ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
# قرار دادن لیبل در سمت راست (x حدود 830)
melk_type_ejareh_maskoni_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")
# قرار دادن اینتری در سمت چپ (x حدود 460)
melk_type_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_ejareh_maskoni_entry.insert(0, "اجاره مسکونی")
melk_type_ejareh_maskoni_entry.config(state="disabled")

# ردیف 2: سال ساخت
sal_sakht_ejareh_maskoni_lable = tk.Label(ejareh_rehn_page, text="سال ساخت", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
sal_sakht_ejareh_maskoni_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

sal_sakht_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
sal_sakht_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

# ردیف 3: آدرس
addrres_ejareh_maskoni_lable = tk.Label(ejareh_rehn_page, text="آدرس", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
addrres_ejareh_maskoni_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

addrres_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
addrres_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

# ردیف 4: طبقه
tabaghe_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="طبقه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
tabaghe_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

tabaghe_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
tabaghe_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

# ردیف 5: واحد
vahed_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="واحد", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
vahed_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

vahed_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
vahed_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

# ردیف 6: اتاق
otagh_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="اتاق", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
otagh_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

otagh_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
otagh_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

# ردیف 7: قیمت اجاره و پیش (دو ستون کنار هم)
# مبلغ اجاره
gheimat_ejare_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="مبلغ اجاره", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_ejare_ejare_maskoni_lable.place(x=start_x + 130, y=start_y + 340, anchor="e")

gheimat_ejare_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_ejare_ejare_maskoni_entry.place(x=start_x + 10, y=start_y + 370, width=150, height=25)

# مبلغ پیش
gheimat_pish_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="مبلغ پیش", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_pish_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 340, anchor="e")

gheimat_pish_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_pish_ejare_maskoni_entry.place(x=start_x + 190, y=start_y + 370, width=150, height=25)


name_malek_ejareh_maskoni_lable = tk.Label(ejareh_rehn_page, text="نام مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_malek_ejareh_maskoni_lable.place(x=start_x + 320, y=start_y + 442,anchor="e")

name_malek_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_malek_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 430, width=150, height=25)

shomareh_malek_ejareh_maskoni_lable = tk.Label(ejareh_rehn_page, text="شماره مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_malek_ejareh_maskoni_lable.place(x=start_x + 320, y=start_y + 486,anchor="e")

shomareh_malek_ejareh_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_malek_ejareh_maskoni_entry.place(x=start_x + 10, y=start_y + 475, width=150, height=25)

back_to_home_ejareh_maskoni=tk.Button(ejareh_rehn_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_ejareh_maskoni)
back_to_home_ejareh_maskoni.place(x=270,y=520)

save_button_ejareh_maskooni=tk.Button(ejareh_rehn_page,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_ejareh_maskoni)
save_button_ejareh_maskooni.place(x=120,y=520)

# 1. لیبل نگهدارنده تصویر
photo_lbl2_ejare_maskoni = tk.Label(ejareh_rehn_page, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15,relief="solid", bd=1)
photo_lbl2_ejare_maskoni.place(x=60, y=85)

# 2. دکمه افزودن تصویر
add_img_btn_ejare_maskoni = tk.Button(ejareh_rehn_page, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file, height=2,width=13)
add_img_btn_ejare_maskoni.place(x=60, y=370)

ejareh_rehn_page.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_rehn_page.resizable(False, False)

#endregion
#------------------ساخت امکانات اجاره مسکونی------------------------
#region
option_frame_ejare_maskoni=tk.Frame(ejareh_rehn_page,width=300,height=30,background="#052340")
option_frame_ejare_maskoni.place(x=225,y=370)

add_option_frame_ejare_maskoni=tk.Label(option_frame_ejare_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
add_option_frame_ejare_maskoni.pack(side="right",padx=1)

plus_button_ejare_maskoni=tk.Button(option_frame_ejare_maskoni,image=plus,command=open_option1,border=0)
plus_button_ejare_maskoni.pack()

bg_image = image_ejareh_maskoni
bg_image = image_ejareh_maskoni.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_maskoni, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# --- چک‌باکس‌ها (پارکینگ، آسانسور، انباری) ---
# چیدمان افقی در بالای فرم

parking_ejareh_maskoni_var=tk.IntVar(value=0)
anbari_ejareh_maskoni_var=tk.IntVar(value=0)
asansor_ejareh_maskoni_var=tk.IntVar(value=0)


parking_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=parking_pic,variable=parking_ejareh_maskoni_var,bg="#052340")
parking_checkbutton_btn_ejareh_maskoni.place(x=140, y=50)

asansor_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=elvator_pic,variable=asansor_ejareh_maskoni_var, bg="#052340")
asansor_checkbutton_btn_ejareh_maskoni.place(x=240, y=50)

anbari_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=warehouse_pic,variable=anbari_ejareh_maskoni_var,bg="#052340")
anbari_checkbutton_btn_ejareh_maskoni.place(x=340, y=50)

# 1. سرمایش
sarmaesh_ejareh_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="سرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
sarmaesh_ejareh_maskoni.place(x=320, y=110)
sarmaesh_ejareh_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
sarmaesh_ejareh_maskoni_combo["values"] = ("ندارد", "پنکه سقفی", "کولر ابی", "کولر گازی ", "ابی/گازی")
sarmaesh_ejareh_maskoni_combo["state"] = "readonly"
sarmaesh_ejareh_maskoni_combo.place(x=120, y=110)

# 2. گرمایش
garmaesh_ejareh_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="گرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
garmaesh_ejareh_maskoni.place(x=320, y=150)
garmaesh_ejareh_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
garmaesh_ejareh_maskoni_combo["values"] = ("ندارد", "بخاری", " شوفاژ", "گرمایش از کف ")
garmaesh_ejareh_maskoni_combo["state"] = "readonly"
garmaesh_ejareh_maskoni_combo.place(x=120, y=150)

# 3. کف
kaf_ejareh_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="کف", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
kaf_ejareh_maskoni.place(x=320, y=190)
kaf_ejareh_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
kaf_ejareh_maskoni_combo["values"] = ("سرامیک", "موزاییک", "پارکت")
kaf_ejareh_maskoni_combo["state"] = "readonly"
kaf_ejareh_maskoni_combo.place(x=120, y=190)

# 4. سرویس بهداشتی
toilet_ejareh_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="سرویس بهداشتی", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
toilet_ejareh_maskoni.place(x=320, y=230)
toilet_ejareh_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
toilet_ejareh_maskoni_combo["values"] = ("ایرانی", "فرنگی", "هردو")
toilet_ejareh_maskoni_combo["state"] = "readonly"
toilet_ejareh_maskoni_combo.place(x=120, y=230)


# --- دکمه‌های پایین صفحه ---
save_optoin_ejareh_maskoni = tk.Button(option_file_frame_ejareh_maskoni, text="تایید", command=save_option_ejareh_maskoni, bg="#00BFFF", fg="#000000", width=10, height=1)
save_optoin_ejareh_maskoni.place(x=95, y=320)

back_to_ejareh_maskoni = tk.Button(option_file_frame_ejareh_maskoni, text="بازگشت", command=back_to_ejareh_maskoni, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_ejareh_maskoni.place(x=215, y=320)

option_file_frame_ejareh_maskoni.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_ejareh_maskoni.resizable(False, False)

#endregion
#------------------------پنجره اجاره اداری/تجاری--------------------
#region
ejareh_edari_tejari = tk.Toplevel(root)
ejareh_edari_tejari.title("رهن و اجاره اداری / تجاری")
ejareh_edari_tejari.geometry("800x600")
ejareh_edari_tejari.withdraw()

# بارگذاری تصویر
bg_image = image_ejareh_edari_tajari
bg_image = image_ejareh_edari_tajari.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(ejareh_edari_tejari, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#--------------------پنجره امکانات اجاره اداری/تجاری----------------------
option_file_frame_ejareh_edari_tajari=tk.Toplevel(ejareh_edari_tejari)
option_file_frame_ejareh_edari_tajari.title("امکانات اجاره اداری/تجاری ")
option_file_frame_ejareh_edari_tajari.geometry("500x370")
option_file_frame_ejareh_edari_tajari.pack_propagate(False)
option_file_frame_ejareh_edari_tajari.withdraw()

#----------------------کادر اجاره اداری و تجاری------------------#
frame_ejareh_edari_tejari= tk.Frame(ejareh_edari_tejari,bd=0,highlightthickness=0)
frame_ejareh_edari_tejari.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(ejareh_edari_tejari,text="اجاره اداری و تجاری",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25) 

start_x = 450
start_y = 40

melk_type_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text="نوع ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)

melk_type_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")

melk_type_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25) 
melk_type_ejareh_edari_tejari_entry.insert(0,"اجاره اداری و تجاری")
melk_type_ejareh_edari_tejari_entry.config(state="disable")

metraj_melk_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text=" متراژ ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
metraj_melk_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_melk_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
metraj_melk_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

sal_sakht_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text="سال ساخت", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
sal_sakht_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

sal_sakht_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
sal_sakht_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

addrres_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text="آدرس", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
addrres_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

addrres_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
addrres_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

tabaghe_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text="طبقه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
tabaghe_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

tabaghe_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
tabaghe_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

vahed_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text="واحد", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
vahed_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")


vahed_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
vahed_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)


mablagh_pish_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari,text="مبلغ ودیعه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_pish_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

mablagh_pish_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_pish_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

mablagh_ejare_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari,text="مبلغ اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_ejare_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

mablagh_ejare_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_ejare_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

name_malek_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari,text="نام مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
name_malek_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 438, anchor="e")

name_malek_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
name_malek_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 425, width=150, height=25)

shomareh_malek_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari,text="شماره مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
shomareh_malek_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 487, anchor="e")

shomareh_malek_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
shomareh_malek_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 475, width=150, height=25)

back_to_home_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_ejareh_edari_tejari)
back_to_home_ejareh_edari_tejari.place(x=280,y=520)

zakhire_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=sabt_ejareh_edari_tejari)
zakhire_ejareh_edari_tejari.place(x=130,y=520)

photo_lbl2_ejareh_edari_tejari = tk.Label(ejareh_edari_tejari, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15)
photo_lbl2_ejareh_edari_tejari.place(x=60, y=85)

add_img_btn_ejareh_edari_tejari = tk.Button(ejareh_edari_tejari, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_ejareh_edari_tejari.place(x=60, y=370)

ejareh_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_edari_tejari.resizable(False, False)
#endregion
#----------------------ساخت امکانات اجاره اداری/تجاری---------------------
#region
option_frame_ejareh_edari_tejari=tk.Frame(ejareh_edari_tejari,width=300,height=30,background="#052340")
option_frame_ejareh_edari_tejari.place(x=225,y=370)

option_label_ejareh_edari_tejari=tk.Label(option_frame_ejareh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_ejareh_edari_tejari.pack(side="right",padx=1)

plus_button_ejareh_edari_tejari=tk.Button(option_frame_ejareh_edari_tejari,image=plus,command=open_option3,border=0)
plus_button_ejareh_edari_tejari.pack(side="right",padx=1)

bg_image = image_ejareh_edari_tajari
bg_image = image_ejareh_edari_tajari.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_edari_tajari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_ejareh_edari_tejari_var=tk.IntVar(value=0)
anbari_ejareh_edari_tejari_var=tk.IntVar(value=0)
asansor_ejareh_edari_tejari_var=tk.IntVar(value=0)

parking_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,variable=parking_ejareh_edari_tejari_var,image=parking_pic,background="#052340")
parking_ch_btn_ejareh_edari_tejari.place(x=140, y=50)

asansor_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,variable=asansor_ejareh_edari_tejari_var,image=elvator_pic,background="#052340")
asansor_ch_btn_ejareh_edari_tejari.place(x=240, y=50)

anbari_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,variable=anbari_ejareh_edari_tejari_var,image=warehouse_pic,background="#052340")
anbari_ch_btn_ejareh_edari_tejari.place(x=340, y=50)

ab_va_gaz_emkanat_ejareh_edari_tejari=tk.Label(option_file_frame_ejareh_edari_tajari,text="وضعیت آب و گاز",background="#052340",fg="#ffffff",font=("Shabnam",11))
ab_va_gaz_emkanat_ejareh_edari_tejari.place(x=320, y=110)

ab_va_gaz_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_file_frame_ejareh_edari_tajari)
ab_va_gaz_combo_emkanat_ejareh_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
ab_va_gaz_combo_emkanat_ejareh_edari_tejari["state"]=["readonly"]
ab_va_gaz_combo_emkanat_ejareh_edari_tejari.place(x=120, y=110)

sarmayesh_emkanat_ejareh_edari_tejari=tk.Label(option_file_frame_ejareh_edari_tajari,text="سیستم سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
sarmayesh_emkanat_ejareh_edari_tejari.place(x=320, y=150)

sarmayesh_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_file_frame_ejareh_edari_tajari)
sarmayesh_combo_emkanat_ejareh_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_ejareh_edari_tejari["state"]=["readonly"]
sarmayesh_combo_emkanat_ejareh_edari_tejari.place(x=120, y=150)

garmayesh_emkanat_ejareh_edari_tejari=tk.Label(option_file_frame_ejareh_edari_tajari,text="سیستم گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
garmayesh_emkanat_ejareh_edari_tejari.place(x=320, y=190)

garmayesh_combo_emkanat_ejareh_edari_tejari=ttk.Combobox(option_file_frame_ejareh_edari_tajari)
garmayesh_combo_emkanat_ejareh_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_ejareh_edari_tejari["state"]=["readonly"]
garmayesh_combo_emkanat_ejareh_edari_tejari.place(x=120, y=190)

save_optoin_ejareh_edari_tejari=tk.Button(option_file_frame_ejareh_edari_tajari,text="تایید",command=save_option_ejareh_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
save_optoin_ejareh_edari_tejari.place(x=95,y=320)

back_to_home_ejareh_edari_tejari=tk.Button(option_file_frame_ejareh_edari_tajari,text="بازگشت",command=back_to_ejareh_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_ejareh_edari_tejari.place(x=215,y=320)

option_file_frame_ejareh_edari_tajari.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_ejareh_edari_tajari.resizable(False, False)

#endregion
#-------------------پنجره اجاره باغ/زمین------------------------
#region
ejareh_bagh_zamin = tk.Toplevel(root)
ejareh_bagh_zamin.title(" اجاره باغ و زمین")
ejareh_bagh_zamin.geometry("800x600")
ejareh_bagh_zamin.withdraw()

bg_image = image_ejareh_bagh_zamin
bg_image = image_ejareh_bagh_zamin.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(ejareh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------------کادر اجاره باغ و زمین---------------------#
frame_ejareh_bagh_zamin= tk.Frame(ejareh_bagh_zamin,bd=0,highlightthickness=0)
frame_ejareh_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(ejareh_bagh_zamin,text="اجاره باغ و زمین",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

melk_type_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="نوع ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
melk_type_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")
melk_type_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_ejareh_bagh_zamin_entry.insert(0,"اجاره باغ و زمین")
melk_type_ejareh_bagh_zamin_entry.config(state="disable")

metraj_zamin_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="متراژ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
metraj_zamin_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_zamin_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
metraj_zamin_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

bagh_type_lable=tk.Label(ejareh_bagh_zamin, text="کاربری زمین", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_type_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")


bagh_type_combo=ttk.Combobox(ejareh_bagh_zamin,state="readonly")
bagh_type_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_combo.set("باغ")
bagh_type_combo.place(x=start_x + 10, y=start_y + 125, width=150, height=25)
bagh_type_combo.bind("<<ComboboxSelected>>",change_bagh_zamin1)

bagh_loctaion_lable=tk.Label(ejareh_bagh_zamin, text=" منطقه و آدرس ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_loctaion_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_loctaion_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

bagh_gheimat_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="ودیعه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_gheimat_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

bagh_gheimat_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_gheimat_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

bagh_gheimat_har_metr_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="اجاره ماهانه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_gheimat_har_metr_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

bagh_gheimat_har_metr_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_gheimat_har_metr_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

time_bagh_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin,text="مدت اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
time_bagh_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

bagh_time_combo=ttk.Combobox(ejareh_bagh_zamin,state="readonly")
bagh_time_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_combo.set("فصلی")
bagh_time_combo.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

name_malek_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="نام مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_malek_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

name_malek_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_malek_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

number_malek_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="شماره مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
number_malek_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 430, anchor="e")

number_malek_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
number_malek_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 420, width=150, height=25)


photo_lbl2_ejareh_bagh_zamin = tk.Label(ejareh_bagh_zamin, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15)
photo_lbl2_ejareh_bagh_zamin.place(x=60, y=85)


add_img_btn_ejareh_bagh_zamin = tk.Button(ejareh_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_ejareh_bagh_zamin.place(x=60, y=370)

back_to_home_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_ejareh_bagh_zamin)
back_to_home_ejareh_bagh_zamin.place(x=290,y=520)

zakhire_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=sabt_ejareh_bagh_zamin)
zakhire_ejareh_bagh_zamin.place(x=140,y=520)

ejareh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_bagh_zamin.resizable(False, False)

#endregion
#---------------------امکانات اجاره باغ/زمین---------------------
#region
option_frame_ejareh_bagh_zamin=tk.Frame(ejareh_bagh_zamin,width=300,height=30,background="#052340")
option_frame_ejareh_bagh_zamin.place(x=225,y=370)

option_label_ejareh_bagh_zamin=tk.Label(option_frame_ejareh_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_ejareh_bagh_zamin.pack(side="right",padx=1)

plus_button_ejareh_bagh_zamin=tk.Button(option_frame_ejareh_bagh_zamin,image=plus,command=open_option5,border=0)
plus_button_ejareh_bagh_zamin.pack()

option_file_frame_ejareh_bagh_zamin=tk.Toplevel(ejareh_bagh_zamin,background="#052340")
option_file_frame_ejareh_bagh_zamin.title(" امکانات اجاره باغ/زمین")
option_file_frame_ejareh_bagh_zamin.geometry("690x630")
option_file_frame_ejareh_bagh_zamin.pack_propagate(False)
option_file_frame_ejareh_bagh_zamin.withdraw()

option_frame_options_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin)
option_frame_options_ejareh_bagh_zamin.place(x=50,y=50)

bg_image = image_ejareh_bagh_zamin
bg_image = image_ejareh_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



metraj_tree=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_tree.place(x=450, y=70)

metraj_tree_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_tree_entry.place(x=305, y=70)

tree_count=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tree_count.place(x=460, y=100)

tree_count_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tree_count_entry.place(x=305, y=100)

abyari=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع آبیاری")
abyari.place(x=460, y=130)

abyari_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin)
abyari_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_combo.set("سطحی")
abyari_combo["state"]=["readonly"]
abyari_combo.place(x=273, y=130)

type_tree=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع درخت")
type_tree.place(x=460, y=160)

type_tree_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin)
type_tree_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","آلبالو")
type_tree_combo["state"]=["readonly"]
type_tree_combo.set("گردو")
type_tree_combo.place(x=273, y=160)

add_tree_button=tk.Button(option_file_frame_ejareh_bagh_zamin,text="افزودن درخت",font=("Shabnam",9),command=add_tree,bg="#00BFFF",width=10,height=1)
add_tree_button.place(x=460, y=190)

label_result_add=tk.Label(option_file_frame_ejareh_bagh_zamin,text="")
label_result_add.place(x=305, y=190)

chah_bagh_ejareh_var= tk.IntVar(value=0)
chah_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=chah_bagh_ejareh_var,text="چاه",font=("Shabnam",9),background="#052340",fg="#00BFFF")
chah_bagh.place(x=480, y=220)

estakhr_bagh_var=tk.IntVar(value=0)
estakhr_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=estakhr_bagh_var,text="استخر",font=("Shabnam",9),background="#052340",fg="#00BFFF")
estakhr_bagh.place(x=380, y=220)

bargh_bagh_var=tk.IntVar(value=0)
bargh_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=bargh_bagh_var,text="برق کشی",font=("Shabnam",9),background="#052340",fg="#00BFFF")
bargh_bagh.place(x=280, y=220)

divar_ejareh_bagh_var=tk.IntVar(value=0)
divar_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=divar_ejareh_bagh_var,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_ejareh_bagh_zamin.place(x=180, y=220)


var0=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

room_bagh_checkbutton=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=var0,image=warehouse_pic,background="#052340",text="ساختمان",command=home_true_false1)
room_bagh_checkbutton.place(x=470, y=250)

metraj_vila_bagh_lable=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ سازه")
metraj_vila_bagh_lable.place(x=450, y=300)

metraj_vila_bagh_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#00BFFF",fg="#000000",state="disabled")
metraj_vila_bagh_entry.place(x=305, y=300)

sal_sakht_vila_bagh_lable=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سال ساخت")
sal_sakht_vila_bagh_lable.place(x=450, y=330)

sal_sakht_vila_bagh_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#00BFFF",fg="#000000",state="disabled")
sal_sakht_vila_bagh_entry.place(x=305, y=330)

type_vila_ejareh_bagh_zamin=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="نوع سازه")
type_vila_ejareh_bagh_zamin.place(x=450, y=360)

type_vila_ejareh_bagh_zamin_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="disabled")
type_vila_ejareh_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_ejareh_bagh_zamin_combo.set("آجری")
type_vila_ejareh_bagh_zamin_combo.place(x=273, y=360)

toilet_bagh=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سرویس بهداشتی")
toilet_bagh.place(x=450, y=390)

toilet_bagh_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="disabled")
toilet_bagh_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_bagh_combo.set("")
toilet_bagh_combo.place(x=273, y=390)

hamam_bagh=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="حمام")
hamam_bagh.place(x=450, y=420)

hamam_bagh_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="disabled")
hamam_bagh_combo["values"]=(" ","ندارد","دارد")
hamam_bagh_combo.set(" ")
hamam_bagh_combo.place(x=273, y=420)

sanad_bagh=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سند")
sanad_bagh.place(x=450, y=450)

sanad_bagh_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="disabled")
sanad_bagh_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_bagh_combo.set(" ")
sanad_bagh_combo.place(x=273, y=450)

option_ejareh_bagh_zamin=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="امکانات تفریحی")
option_ejareh_bagh_zamin.place(x=450, y=480)

option_ejareh_bagh_zamin_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="disabled")
option_ejareh_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_ejareh_bagh_zamin_combo.set(" ")
option_ejareh_bagh_zamin_combo.place(x=273, y=480)

add_option_button=tk.Button(option_file_frame_ejareh_bagh_zamin,text="افزودن امکانات",command=add_option,bg="#00BFFF",font=("Shabnam",9),width=10,height=1)
add_option_button.place(x=180, y=480)

label_result2_add=tk.Label(option_file_frame_ejareh_bagh_zamin,text="")
label_result2_add.place(x=100, y=480)

mojavez_sakht_ejareh_bagh_var=tk.IntVar(value=0)
mojavez_sakht_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=mojavez_sakht_ejareh_bagh_var,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_ejareh_bagh_zamin.place(x=450, y=510)

mohavate_ejareh_bagh_var=tk.IntVar(value=0)
mohavate_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,variable=mohavate_ejareh_bagh_var,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_ejareh_bagh_zamin.place(x=320, y=510)


#endregion
#-------------------تعویض کاربری به زمین در قسمت اجاره باغ/زمین--------------
#region
fram_option_zamin_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin)
fram_option_zamin_ejareh_bagh_zamin.place_forget()

bg_image = image_ejareh_bagh_zamin
bg_image = image_ejareh_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(fram_option_zamin_ejareh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

metraj_zamin_ejareh_bagh_zamin2=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin_ejareh_bagh_zamin2.place(x=448, y=10)

metraj_zamin_ejareh_bagh_zamin_entry2=tk.Entry(fram_option_zamin_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin_ejareh_bagh_zamin_entry2.place(x=312, y=13)

karbari_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_ejareh_ejareh_bagh_zamin.place(x=458, y=45)

karbari_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
karbari_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")     
karbari_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                        
karbari_ejareh_ejareh_bagh_zamin_combo.set(" ")
karbari_ejareh_ejareh_bagh_zamin_combo.place(x=273, y=45)

khak_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_ejareh_ejareh_bagh_zamin.place(x=458, y=80)

khak_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
khak_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")
khak_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                              
khak_ejareh_ejareh_bagh_zamin_combo.set(" ")
khak_ejareh_ejareh_bagh_zamin_combo.place(x=273, y=80)

ab_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع آب")
ab_ejareh_ejareh_bagh_zamin.place(x=458, y=115)

ab_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
ab_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال آبیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر") 
ab_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                             
ab_ejareh_ejareh_bagh_zamin_combo.set(" ")
ab_ejareh_ejareh_bagh_zamin_combo.place(x=273, y=115)



security_zamin_ejareh_var=tk.IntVar(value=0)
security_room_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=security_zamin_ejareh_var,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_room_zamin_ejareh_bagh_zamin.place(x=450, y=230)


bargh_tak_ejareh_zamin_var=tk.IntVar(value=0)
bargh_tak_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=bargh_tak_ejareh_zamin_var,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_tak_faz_zamin_ejareh_bagh_zamin.place(x=350, y=230)

bargh_se_faz_ejareh_zamin_var=tk.IntVar(value=0)
bargh_se_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=bargh_se_faz_ejareh_zamin_var,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_se_faz_zamin_ejareh_bagh_zamin.place(x=250, y=230)

anbar_ejareh_zamin_var=tk.IntVar(value=0)
anbar_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=anbar_ejareh_zamin_var,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_ejareh_bagh_zamin.place(x=150, y=230)

fans_ejareh_zamin_var=tk.IntVar(value=0)
fans_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=fans_ejareh_zamin_var,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_ejareh_bagh_zamin.place(x=60, y=230)


mojavaz_chah_ejareh_zamin_var=tk.IntVar(value=0)
mojavaz_chah_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,variable=mojavaz_chah_ejareh_zamin_var,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavaz_chah_zamin_ejareh_bagh_zamin.place(x=300, y=280)


zakhire_option_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="تایید",background="#00BFFF",fg="#000000",width=10,height=1,command=save_option_ejareh_bagh_zamin)
zakhire_option_ejareh_bagh_zamin.place(x=95,y=580)

back_to_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="بازگشت",command=back_to_ejareh_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_ejareh_bagh_zamin.place(x=215,y=580)

option_file_frame_ejareh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_ejareh_bagh_zamin.resizable(False, False)

#=======================================================================
#endregion
#-------------------پنجره اجاره کارگاه------------------------
#region
ejareh_karghah = tk.Toplevel(root)
ejareh_karghah.title(" اجاره کارگاه")
ejareh_karghah.geometry("800x600")
ejareh_karghah.withdraw()

bg_image = image_ejareh_karghah
bg_image = image_ejareh_karghah.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(ejareh_karghah, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#----------------------کادر اجاره کارگاه-----------------------#
ejareh_kargah_frame= tk.Frame(ejareh_karghah,bd=0,highlightthickness=0)
ejareh_kargah_frame.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(ejareh_karghah,text="اجاره کارگاه",bg="#000000",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

karbari_zamin_ejareh_kargah=tk.Label(ejareh_karghah, text="کاربری زمین", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
karbari_zamin_ejareh_kargah.place(x=start_x + 320, y=start_y + 35, anchor="e")

karbari_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")
karbari_ejareh_kargah_entry.insert(0,"کارگاه")
karbari_ejareh_kargah_entry.config(state="disable")
karbari_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

ejareh_kargah_lable=tk.Label(ejareh_karghah,text=" کارگاه ",bg="#ffffff",fg="#000000",width=20)
ejareh_kargah_lable.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

metraj_kargah_lable=tk.Label(ejareh_karghah, text=" متراژ ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
metraj_kargah_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
metraj_kargah_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

loctaion_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="منطقه و آدرس", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
loctaion_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

loctaion_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
loctaion_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

mablagh_pish_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="ودیعه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
mablagh_pish_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")


mablagh_pish_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
mablagh_pish_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

mablagh_ejareh_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="مبلغ اجاره", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
mablagh_ejareh_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

mablagh_ejareh_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
mablagh_ejareh_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)


time_ejate_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="مدت اجاره", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
time_ejate_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

time_ejare_ejareh_kargah_combo=ttk.Combobox(ejareh_karghah,state="readonly")
time_ejare_ejareh_kargah_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
time_ejare_ejareh_kargah_combo.set("فصلی")
time_ejare_ejareh_kargah_combo.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

name_malek_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="نام مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_malek_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 345, anchor="e")

name_malek_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_malek_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 335, width=150, height=25)

shomareh_malek_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="شماره مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_malek_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 395, anchor="e")

shomareh_malek_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_malek_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 385, width=150, height=25)

photo_lbl2_ejareh_kargah = tk.Label(ejareh_karghah, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15)
photo_lbl2_ejareh_kargah.place(x=60, y=85)

add_img_btn_ejareh_kargah = tk.Button(ejareh_karghah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_ejareh_kargah.place(x=60, y=370)

back_to_home_ejareh_kargah=tk.Button(ejareh_karghah,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_ejareh_karghah)
back_to_home_ejareh_kargah.place(x=290,y=520)

zakhire_ejareh_kargah=tk.Button(ejareh_karghah,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_ejareh_kargah)
zakhire_ejareh_kargah.place(x=140,y=520)

ejareh_karghah.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_karghah.resizable(False, False)
#endregion
#---------------------پنجره امکانات اجاره کارگاه---------------------
#region
option_frame_ejareh_kargah=tk.Frame(ejareh_karghah,width=300,height=30,background="#052340")
option_frame_ejareh_kargah.place(x=225,y=370)

option_frame_ejareh_kargah_lable=tk.Label(option_frame_ejareh_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_ejareh_kargah_lable.pack(side="right",padx=1)

plus_button_ejareh_kargah=tk.Button(option_frame_ejareh_kargah,image=plus,command=open_option7,border=0)
plus_button_ejareh_kargah.pack()

option_file_frame_ejareh_kargah=tk.Toplevel(ejareh_karghah)
option_file_frame_ejareh_kargah.title(" امکانات اجاره کارگاه")
option_file_frame_ejareh_kargah.geometry("500x500")
option_file_frame_ejareh_kargah.pack_propagate(False)
option_file_frame_ejareh_kargah.withdraw()

bg_image = image_ejareh_karghah
bg_image = image_ejareh_karghah.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_kargah, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


sal_sakht_ejareh_kargah_lable=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="سال ساخت")
sal_sakht_ejareh_kargah_lable.place(x=302, y=50)

sal_sakht_ejareh_kargah_entry=tk.Entry(option_file_frame_ejareh_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_ejareh_kargah_entry.place(x=108, y=50)

vaziat_bagh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="وضعیت برق")
vaziat_bagh_ejareh_kargah.place(x=295, y=80)

vaziat_bargh_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
vaziat_bargh_ejareh_kargah_combo["values"]=("","برق شهری","سه فاز","تک فاز")
vaziat_bargh_ejareh_kargah_combo.set("")
vaziat_bargh_ejareh_kargah_combo["state"]=["readonly"]
vaziat_bargh_ejareh_kargah_combo.place(x=70, y=80)

garmayesh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_ejareh_kargah.place(x=295, y=110)

garmayesh_type_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
garmayesh_type_ejareh_kargah_combo["values"]=("","بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_ejareh_kargah_combo.set("")
garmayesh_type_ejareh_kargah_combo["state"]=["readonly"]
garmayesh_type_ejareh_kargah_combo.place(x=70, y=110)

sarmayesh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_ejareh_kargah.place(x=295, y=140)

sarmayesh_kooler_abi_ejareh_kargah_var=tk.IntVar(value=0)
sarmayesh_panke_ejareh_kargah_var=tk.IntVar(value=0)
sarmayesh_fan_ejareh_kargah_var=tk.IntVar(value=0)
sarmayesh_kooler_gazi_ejareh_kargah_var=tk.IntVar(value=0)

sarmayesh_fan_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="تهویه(فن)",variable=sarmayesh_fan_ejareh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_ejareh_kargah.place(x=295, y=170)

sarmayesh_panke_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="پنکه سقفی",variable=sarmayesh_panke_ejareh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_ejareh_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="کولر آبی",variable=sarmayesh_kooler_abi_ejareh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_ejareh_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="کولر گازی",variable=sarmayesh_kooler_gazi_ejareh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_ejareh_kargah.place(x=84, y=200)

vaziat_ab_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",width=13,text=" وضعیت آب",font=("Shabnam", 9))
vaziat_ab_ejareh_kargah.place(x=303, y=230)

vaziat_ab_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah,width=35)
vaziat_ab_ejareh_kargah_combo["values"]=(""," آب  لوله کشی (بدون فشار) " ," آب لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_ejareh_kargah_combo.set("")
vaziat_ab_ejareh_kargah_combo["state"]=["readonly"]
vaziat_ab_ejareh_kargah_combo.place(x=30, y=230)

abzar_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_ejareh_kargah.place(x=298, y=260)

abzaar_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah,width=23)
abzaar_ejareh_kargah_combo["values"]=("","(کارگاه خالی) بدون دستگاه ","دارای دستگاه")
abzaar_ejareh_kargah_combo.set("")
abzaar_ejareh_kargah_combo["state"]=["readonly"]
abzaar_ejareh_kargah_combo.place(x=58, y=260)

toilet_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_ejareh_kargah.place(x=298, y=290)

toilet_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
toilet_ejareh_kargah_combo["values"]=("","دارد","ندارد")
toilet_ejareh_kargah_combo.set("")
toilet_ejareh_kargah_combo["state"]=["readonly"]
toilet_ejareh_kargah_combo.place(x=70, y=290)

hamam_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_ejareh_kargah.place(x=303, y=320)

hamam_ejareh_kargah__combo=ttk.Combobox(option_file_frame_ejareh_kargah)
hamam_ejareh_kargah__combo["values"]=("","ندارد","دارد")
hamam_ejareh_kargah__combo.set("")
hamam_ejareh_kargah__combo["state"]=["readonly"]
hamam_ejareh_kargah__combo.place(x=70, y=320)

otagh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_ejareh_kargah.place(x=294, y=350)

otagh_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
otagh_ejareh_kargah_combo["values"]=("","ندارد","دارد")
otagh_ejareh_kargah_combo.set("")
otagh_ejareh_kargah_combo["state"]=["readonly"]
otagh_ejareh_kargah_combo.place(x=70, y=350)

zakhire_options_ejareh_kargah=tk.Button(option_file_frame_ejareh_kargah,text="تایید",command=save_option_ejareh_kargah,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_ejareh_kargah.place(x=50,y=450)

back_to_ejareh_kargah=tk.Button(option_file_frame_ejareh_kargah,text="بازگشت",command=back_to_ejareh_karghah,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_ejareh_kargah.place(x=170,y=450)

option_file_frame_ejareh_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_ejareh_kargah.resizable(False, False)

#endregion
#---------------------------پنجره های ثبتی بخش فروش--------------------
#-------------------پنجره فروش مسکونی----------------------
#region
forosh_rehn_page = tk.Toplevel(root)
forosh_rehn_page.title("فروش مسکونی")
forosh_rehn_page.geometry("800x600")
forosh_rehn_page.withdraw()

# بارگذاری تصویر
bg_image = image_forosh_maskoni
bg_image = image_forosh_maskoni.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(forosh_rehn_page, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


option_file_frame_forosh_maskoni=tk.Toplevel(forosh_rehn_page)
option_file_frame_forosh_maskoni.title(" امکانات فروش مسکونی")
option_file_frame_forosh_maskoni.geometry("500x370")
option_file_frame_forosh_maskoni.pack_propagate(False)
option_file_frame_forosh_maskoni.withdraw()

#------------------کادر فروش مسکونی-----------------------------#
frame_forosh_maskoni= tk.Frame(forosh_rehn_page,bd=0,highlightthickness=0)
frame_forosh_maskoni.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(forosh_rehn_page,text="فروش مسکونی",bg="#000000",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)   

# تعیین نقطه شروع (جایی که فریم قبلی قرار داشت)
start_x = 450
start_y = 40

melk_type_forosh_maskoni_lable = tk.Label(forosh_rehn_page, text="نوع ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
melk_type_forosh_maskoni_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")


melk_type_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")
melk_type_forosh_maskoni_entry.insert(0,"فروش مسکونی")
melk_type_forosh_maskoni_entry.config(state="disable")
melk_type_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

sal_sakht_forosh_maskoni=tk.Label(forosh_rehn_page, text="سال ساخت", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
sal_sakht_forosh_maskoni.place(x=start_x + 320, y=start_y + 85, anchor="e")

sal_sakht_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
sal_sakht_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

addrres_forosh_maskoni=tk.Label(forosh_rehn_page, text="آدرس", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
addrres_forosh_maskoni.place(x=start_x + 320, y=start_y + 135, anchor="e")


addrres_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
addrres_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)


tabaghe_forosh_maskoni= tk.Label(forosh_rehn_page, text="طبقه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
tabaghe_forosh_maskoni.place(x=start_x + 320, y=start_y + 185, anchor="e")

tabaghe_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
tabaghe_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)


vahed_forosh_maskoni=tk.Label(forosh_rehn_page, text="واحد", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
vahed_forosh_maskoni.place(x=start_x + 320, y=start_y + 235, anchor="e")

vahed_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
vahed_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)


otagh_forosh_maskoni= tk.Label(forosh_rehn_page, text="اتاق", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
otagh_forosh_maskoni.place(x=start_x + 320, y=start_y + 285, anchor="e")

otagh_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
otagh_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

name_malek_forosh_maskoni_lable = tk.Label(forosh_rehn_page, text="نام مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_malek_forosh_maskoni_lable.place(x=start_x + 320, y=start_y + 340,anchor="e")

name_malek_forosh_maskoni_entry = tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_malek_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)

shomareh_malek_forosh_maskoni_lable = tk.Label(forosh_rehn_page, text="شماره مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_malek_forosh_maskoni_lable.place(x=start_x + 320, y=start_y + 390,anchor="e")

shomareh_malek_forosh_maskoni_entry = tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_malek_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)

gheimat_kol_forosh_maskoni=tk.Label(forosh_rehn_page, text=" قیمت کل ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_kol_forosh_maskoni.place(x=start_x + 320, y=start_y + 445, anchor="e")

gheimat_kol_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_kol_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 430, width=150, height=25)

back_to_home_forosh_maskoni=tk.Button(forosh_rehn_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_maskoni)
back_to_home_forosh_maskoni.place(x=270,y=520)

zakhire_forosh_maskoni=tk.Button(forosh_rehn_page,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_forosh_maskoni)
zakhire_forosh_maskoni.place(x=120,y=520)

photo_lbl2_forosh_maskoni = tk.Label(forosh_rehn_page, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_forosh_maskoni.place(x=60, y=85)

add_img_btn_forosh_maskoni = tk.Button(forosh_rehn_page, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_maskoni.place(x=60, y=370)

forosh_rehn_page.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_rehn_page.resizable(False, False)
#endregion
#------------------------امکانات فروش مسکونی--------------------
#region
option_frame_options_forosh_maskoni=tk.Frame(forosh_rehn_page,width=300,height=30,background="#052340")
option_frame_options_forosh_maskoni.place(x=225,y=370)

option_label_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_forosh_maskoni.pack(side="right",padx=1)

plus_button_forosh_maskoni=tk.Button(option_frame_options_forosh_maskoni,image=plus,command=open_option2,border=0)
plus_button_forosh_maskoni.pack()

bg_image = image_forosh_maskoni
bg_image = image_forosh_maskoni.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_maskoni, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_forosh_maskoni_var=tk.IntVar(value=0)
anbari_forosh_maskoni_var=tk.IntVar(value=0)
asansor_forosh_maskoni_var=tk.IntVar(value=0)

parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni,variable=parking_forosh_maskoni_var,image=parking_pic, bg="#052340")
parking_ch_btn_forosh_maskoni.place(x=140, y=50)

asansor_ch_btn_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni,variable=asansor_forosh_maskoni_var,image=elvator_pic,background="#052340")
asansor_ch_btn_forosh_maskoni.place(x=240, y=50)

anbari_checkbuton_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni,variable=anbari_forosh_maskoni_var,image=warehouse_pic,background="#052340")
anbari_checkbuton_forosh_maskoni.place(x=340, y=50)

sarmaesh_forosh_maskoni=tk.Label(option_file_frame_forosh_maskoni, text="سرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
sarmaesh_forosh_maskoni.place(x=320, y=110)

sarmaesh_combo_forosh_maskoni=ttk.Combobox(option_file_frame_forosh_maskoni)
sarmaesh_combo_forosh_maskoni["state"]=["readonly"]
sarmaesh_combo_forosh_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_forosh_maskoni.place(x=120, y=110)

garmaesh_forosh_maskoni=tk.Label(option_file_frame_forosh_maskoni, text="گرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
garmaesh_forosh_maskoni.place(x=320, y=150)


garmaesh_combo_forosh_maskoni=ttk.Combobox(option_file_frame_forosh_maskoni)
garmaesh_combo_forosh_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_forosh_maskoni["state"]=["readonly"]
garmaesh_combo_forosh_maskoni.place(x=120, y=150)

kaf_forosh_maskoni= tk.Label(option_file_frame_forosh_maskoni, text="کف", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
kaf_forosh_maskoni.place(x=320, y=190)

kaf_combo_forosh_maskoni=ttk.Combobox(option_file_frame_forosh_maskoni)
kaf_combo_forosh_maskoni["state"]=["readonly"]
kaf_combo_forosh_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_forosh_maskoni.place(x=120, y=190)

toilet_forosh_maskoni=tk.Label(option_file_frame_forosh_maskoni,text="سرویس بهداشتی",background="#052340",fg="#ffffff",font=("Shabnam",11))
toilet_forosh_maskoni.place(x=320, y=230)

toilet_combo_forosh_maskoni=ttk.Combobox(option_file_frame_forosh_maskoni)
toilet_combo_forosh_maskoni["state"]=["readonly"]
toilet_combo_forosh_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_forosh_maskoni.place(x=120, y=230)

zakhire_options_forosh_maskoni=tk.Button(option_file_frame_forosh_maskoni,text="تایید",command=save_option_forosh_maskoni,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_forosh_maskoni.place(x=95, y=320)

back_to_home_forosh_maskoni=tk.Button(option_file_frame_forosh_maskoni,text="بازگشت",command=back_to_forosh_maskoni,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_forosh_maskoni.place(x=215, y=320)

option_file_frame_forosh_maskoni.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_maskoni.resizable(False, False)
#endregion
#-----------------پنجره فروش اداری/تجاری-------------------
#region
forosh_edari_tejari = tk.Toplevel(root)
forosh_edari_tejari.title(" فروش اداری / تجاری")
forosh_edari_tejari.geometry("800x600")
forosh_edari_tejari.withdraw()

bg_image = image_forosh_edari_tejari
bg_image = image_forosh_edari_tejari.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(forosh_edari_tejari, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------پنجره امکانات فروش اداری/تجاری----------------

option_file_frame_forosh_edari_tejari=tk.Toplevel(forosh_edari_tejari)
option_file_frame_forosh_edari_tejari.title(" امکانات فروش اداری/تجاری")
option_file_frame_forosh_edari_tejari.geometry("500x370")
option_file_frame_forosh_edari_tejari.pack_propagate(False)
option_file_frame_forosh_edari_tejari.withdraw()

#----------------------کادر فروش اداری و تجاری------------------#
frame_forosh_edari_tejari= tk.Frame(forosh_edari_tejari,bd=0,highlightthickness=0)
frame_forosh_edari_tejari.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(forosh_edari_tejari,text="فروش اداری و تجاری",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40


melk_type_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),justify="center")
melk_type_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_forosh_edari_tejari_entry.insert(0,"فروش اداری و تجاری")
melk_type_forosh_edari_tejari_entry.config(state="disable")

metraj_melk_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="متراژ ملک ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
metraj_melk_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_melk_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
metraj_melk_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

sal_sakht_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="سال ساخت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
sal_sakht_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

sal_sakht_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
sal_sakht_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

addrres_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="آدرس",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
addrres_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

addrres_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
addrres_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

tabaghe_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="طبقه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
tabaghe_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

tabaghe_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
tabaghe_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

vahed_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="واحد",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
vahed_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

vahed_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
vahed_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

name_malek_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="نام مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
name_malek_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

name_malek_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
name_malek_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

shomareh_malek_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="شماره مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
shomareh_malek_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

shomareh_malek_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
shomareh_malek_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

gheimat_kol_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="قیمت کل",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_kol_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")

gheimat_kol_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
gheimat_kol_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 425, width=150, height=25)

back_to_home_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_edari_tejari)
back_to_home_forosh_edari_tejari.place(x=280,y=520)

zakhire_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_forosh_edari_tejari)
zakhire_forosh_edari_tejari.place(x=130,y=520)

selected_images_forosh_edari_tejari = []
photo_refs_forosh_edari_tejari = []

image_frame_forosh_edari_tejari = tk.Frame(forosh_edari_tejari,bg="white",width=350,height=250)
image_frame_forosh_edari_tejari.place(x=60, y=85)
image_frame_forosh_edari_tejari.pack_propagate(False)

add_img_btn_forosh_edari_tejari = tk.Button(forosh_edari_tejari, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file_forosh_edari_tejari,height=2,width=13)
add_img_btn_forosh_edari_tejari.place(x=60, y=370)

forosh_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_edari_tejari.resizable(False, False)
#endregion
#---------------امکانات فروش اداری/تجاری-------------------
#region
option_frame_options_forosh_edari_tejari=tk.Frame(forosh_edari_tejari,width=300,height=30,background="#052340")
option_frame_options_forosh_edari_tejari.place(x=225,y=370)

option_label_forosh_edari_tejari=tk.Label(option_frame_options_forosh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_forosh_edari_tejari.pack(side="right",padx=1)

plus_button_forosh_eedari_tejari=tk.Button(option_frame_options_forosh_edari_tejari,image=plus,command=open_option4,border=0)
plus_button_forosh_eedari_tejari.pack()

bg_image = image_forosh_edari_tejari
bg_image = image_forosh_edari_tejari.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_edari_tejari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_forosh_edari_tejari_var=tk.IntVar(value=0)
anbari_forosh_edari_tejari_var=tk.IntVar(value=0)
asansor_forosh_edari_tejari_var=tk.IntVar(value=0)

parking_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,variable=parking_forosh_edari_tejari_var,image=parking_pic,background="#052340")
parking_check_btn_forosh_edari_tejari.place(x=140, y=50)

asansor_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,variable=asansor_forosh_edari_tejari_var,image=elvator_pic,background="#052340")
asansor_check_btn_forosh_edari_tejari.place(x=240, y=50)

anbari_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,variable=anbari_forosh_edari_tejari_var,image=warehouse_pic,background="#052340")
anbari_check_btn_forosh_edari_tejari.place(x=340, y=50)

aab_va_gaz_emkanat_forosh_edari_tejari=tk.Label(option_file_frame_forosh_edari_tejari,text="وضعیت آب و گاز",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
aab_va_gaz_emkanat_forosh_edari_tejari.place(x=320, y=110)

aab_va_gaz_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_file_frame_forosh_edari_tejari)
aab_va_gaz_combo_emkanat_forosh_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_forosh_edari_tejari["state"]=["readonly"]
aab_va_gaz_combo_emkanat_forosh_edari_tejari.place(x=120, y=110)

sarmayesh_emkanat_forosh_edari_tejari=tk.Label(option_file_frame_forosh_edari_tejari,text="سیستم سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
sarmayesh_emkanat_forosh_edari_tejari.place(x=320, y=150)

sarmayesh_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_file_frame_forosh_edari_tejari)
sarmayesh_combo_emkanat_forosh_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_forosh_edari_tejari["state"]=["readonly"]
sarmayesh_combo_emkanat_forosh_edari_tejari.place(x=120, y=150)

garmayesh_emkanat_forosh_edari_tejari=tk.Label(option_file_frame_forosh_edari_tejari,text="سیستم گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
garmayesh_emkanat_forosh_edari_tejari.place(x=320, y=190)

garmayesh_combo_emkanat_forosh_edari_tejari=ttk.Combobox(option_file_frame_forosh_edari_tejari)
garmayesh_combo_emkanat_forosh_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_forosh_edari_tejari["state"]=["readonly"]
garmayesh_combo_emkanat_forosh_edari_tejari.place(x=120, y=190)

zakhire_options_forosh_edari_tejari=tk.Button(option_file_frame_forosh_edari_tejari,text="تایید",command=save_option_forosh_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_forosh_edari_tejari.place(x=95,y=320)

back_to_home_forosh_edari_tejari=tk.Button(option_file_frame_forosh_edari_tejari,text="بازگشت",command=back_to_forosh_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_forosh_edari_tejari.place(x=215,y=320)

option_file_frame_forosh_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_edari_tejari.resizable(False, False)
#endregion
#--------------------پنجره فروش باغ/زمین-----------------------
#region
forosh_bagh_zamin = tk.Toplevel(root)
forosh_bagh_zamin.title("فروش باغ و زمین")
forosh_bagh_zamin.geometry("800x600")
forosh_bagh_zamin.withdraw()

bg_image = image_forosh_bagh_zamin
bg_image = image_forosh_bagh_zamin.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(forosh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#---------------------کادر فروش باغ و زمین---------------------#
frame_forosh_bagh_zamin= tk.Frame(forosh_bagh_zamin,bd=0,highlightthickness=0)
frame_forosh_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(forosh_bagh_zamin,text="فروش باغ و زمین",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40


melk_type_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),justify="center")
melk_type_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_forosh_bagh_zamin_entry.insert(0,"فروش باغ و زمین")
melk_type_forosh_bagh_zamin_entry.config(state="disable")

metraj_zamin_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
metraj_zamin_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_zamin_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

bagh_type_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
bagh_type_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

bagh_type_forosh_bagh_zamin_combo=ttk.Combobox(forosh_bagh_zamin,state="readonly")
bagh_type_forosh_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_forosh_bagh_zamin_combo.set("باغ")
bagh_type_forosh_bagh_zamin_combo["state"]=["readonly"]
bagh_type_forosh_bagh_zamin_combo.place(x=start_x + 10, y=start_y + 125, width=150, height=25)
bagh_type_forosh_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_forosh_bagh)


bagh_loctaion_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text="منطقه و ادرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
bagh_loctaion_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
bagh_loctaion_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")


gheimat_har_metr_babagh_zamin_forosh_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_babagh_zamin_forosh_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

name_malek_forosh_bagh_lable=tk.Label(forosh_bagh_zamin,text="نام مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
name_malek_forosh_bagh_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

name_malek_forosh_bagh_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
name_malek_forosh_bagh_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

number_malek_forosh_bagh_lable=tk.Label(forosh_bagh_zamin,text="شماره مالک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
number_malek_forosh_bagh_lable.place(x=start_x + 320, y=start_y + 340, anchor="e")

number_malek_forosh_bagh_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
number_malek_forosh_bagh_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)

gheimat_kol_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text='قیمت کل',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_kol_forosh_bagh_zamin_lable.place(x=start_x + 325, y=start_y + 390, anchor="e")

gheimat_kol_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_kol_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)

photo_forosh_bagh_zamin_lable= tk.Label(forosh_bagh_zamin, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_forosh_bagh_zamin_lable.place(x=60, y=85)
add_img_btn_forosh_bagh_zamin = tk.Button(forosh_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_bagh_zamin.place(x=60, y=370)

back_to_home_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_bagh_zamin)
back_to_home_forosh_bagh_zamin.place(x=290,y=520)

zakhire_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_forosh_bagh_zamin_main)
zakhire_forosh_bagh_zamin.place(x=140,y=520)

forosh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_bagh_zamin.resizable(False, False)
#endregion
#-----------------------پنجره امکانات فروش باغ/زمین-------------------
#region
option_frame_options_forosh_bagh_zamin=tk.Frame(forosh_bagh_zamin,width=300,height=30,background="#052340")
option_frame_options_forosh_bagh_zamin.place(x=225,y=370)

option_label_forosh_bagh_zamin=tk.Label(option_frame_options_forosh_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_forosh_bagh_zamin.pack(side="right",padx=1)

plus_button_forosh_bagh_zamin=tk.Button(option_frame_options_forosh_bagh_zamin,image=plus,command=open_option6,border=0)
plus_button_forosh_bagh_zamin.pack()

option_file_frame_forosh_bagh_zamin=tk.Toplevel(forosh_bagh_zamin)
option_file_frame_forosh_bagh_zamin.title(" امکانات فروش باغ/زمین")
option_file_frame_forosh_bagh_zamin.geometry("690x630")
option_file_frame_forosh_bagh_zamin.pack_propagate(False)
option_file_frame_forosh_bagh_zamin.withdraw()

option_frame_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin)
option_frame_forosh_bagh_zamin.place(x=50,y=50)

bg_image = image_forosh_bagh_zamin
bg_image = image_forosh_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


metraj_derakht_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_derakht_forosh_bagh_zamin_lable.place(x=450, y=70)

metraj_derakht_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_derakht_forosh_bagh_zamin_entry.place(x=305, y=70)

tedad_derakht_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tedad_derakht_forosh_bagh_zamin_lable.place(x=460, y=100)

tedad_derakht_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tedad_derakht_forosh_bagh_zamin_entry.place(x=305, y=100)

abyari_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع آبیاری")
abyari_forosh_bagh_zamin_lable.place(x=460, y=130)

abyari_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin)
abyari_forosh_bagh_zamin_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_forosh_bagh_zamin_combo["state"]=["readonly"]
abyari_forosh_bagh_zamin_combo.set("سطحی")
abyari_forosh_bagh_zamin_combo.place(x=273, y=130)

type_tree_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع درخت")
type_tree_forosh_bagh_zamin_lable.place(x=460, y=160)

type_tree_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin)
type_tree_forosh_bagh_zamin_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","آلبالو")
type_tree_forosh_bagh_zamin_combo["state"]=["readonly"]
type_tree_forosh_bagh_zamin_combo.set("گردو")
type_tree_forosh_bagh_zamin_combo.place(x=273, y=160)

type_tree_forosh_btn=tk.Button(option_file_frame_forosh_bagh_zamin,text="افزودن درخت",command=add_tree2,bg="#00BFFF",font=("Shabnam",9),width=10)
type_tree_forosh_btn.place(x=460, y=190)

label_natige_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,text="")
label_natige_forosh_bagh_zamin.place(x=305, y=190)

chah_forosh_bagh_var=tk.IntVar(value=0)
chah_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=chah_forosh_bagh_var,text="چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
chah_forosh_bagh_zamin.place(x=480, y=220)

estakhr_forosh_bagh_var=tk.IntVar(value=0)
estakhr_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=estakhr_forosh_bagh_var,text="استخر",background="#052340",fg="#00BFFF",font=("Shabnam",9))
estakhr_forosh_bagh_zamin.place(x=380, y=220)

bargh_keshi_forosh_bagh_var=tk.IntVar(value=0)
bargh_keshi_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=bargh_keshi_forosh_bagh_var,text="برق کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_forosh_bagh_zamin.place(x=280, y=220)

gas_keshi_forosh_bagh_var=tk.IntVar(value=0)
gas_keshi_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=gas_keshi_forosh_bagh_var,text="گاز کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
gas_keshi_forosh_bagh_zamin.place(x=180, y=220)


var0_forosh_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

otagh_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=var0_forosh_bagh_zamin,image=warehouse_pic,background="#052340",text="ساختمان",command=home_true_false2)
otagh_check_btn_forosh_bagh_zamin.place(x=470, y=250)

metraj_vila_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ سازه")
metraj_vila_forosh_bagh_zamin.place(x=450, y=300)

metraj_vila_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#00BFFF",fg="#000000",state="disabled")
metraj_vila_forosh_bagh_zamin_entry.place(x=305, y=300)

sal_sakht_vila_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سال ساخت")
sal_sakht_vila_forosh_bagh_zamin_lable.place(x=450, y=330)

sal_sakht_vila_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#00BFFF",fg="#000000",state="disabled")
sal_sakht_vila_forosh_bagh_zamin_entry.place(x=305, y=330)

type_vila_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="نوع سازه")
type_vila_forosh_bagh_zamin.place(x=450, y=360)

type_vila_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="disabled")
type_vila_forosh_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_forosh_bagh_zamin_combo.set("آجری")
type_vila_forosh_bagh_zamin_combo["state"]=["readonly"]
type_vila_forosh_bagh_zamin_combo.place(x=273, y=360)

toilet_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سرویس بهداشتی")
toilet_forosh_bagh_zamin_lable.place(x=450, y=390)

toilet_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="disabled")
toilet_forosh_bagh_zamin_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_forosh_bagh_zamin_combo.set("")
toilet_forosh_bagh_zamin_combo["state"]=["readonly"]
toilet_forosh_bagh_zamin_combo.place(x=273, y=390)

hamam_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="حمام")
hamam_forosh_bagh_zamin.place(x=450, y=420)

hamam_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="disabled")
hamam_forosh_bagh_zamin_combo["values"]=(" ","ندارد","دارد")
hamam_forosh_bagh_zamin_combo.set(" ")
hamam_forosh_bagh_zamin_combo["state"]=["readonly"]
hamam_forosh_bagh_zamin_combo.place(x=273, y=420)

sanad_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سند")
sanad_forosh_bagh_zamin_lable.place(x=450, y=450)

sanad_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="disabled")
sanad_forosh_bagh_zamin_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_forosh_bagh_zamin_combo.set(" ")
type_tree_forosh_bagh_zamin_combo["state"]=["readonly"]
sanad_forosh_bagh_zamin_combo.place(x=273, y=450)

option_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="امکانات تفریحی")
option_forosh_bagh_zamin.place(x=450, y=480)

option_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="disabled")
option_forosh_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_forosh_bagh_zamin_combo.set(" ")
option_forosh_bagh_zamin_combo["state"]=["readonly"]
option_forosh_bagh_zamin_combo.place(x=273, y=480)

add_option_button_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="افزودن امکانات",command=add_option2,bg="#00BFFF",font=("Shabnam",9),width=10)
add_option_button_forosh_bagh_zamin.place(x=180, y=480)

lable_natige_add_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,text="")
lable_natige_add_forosh_bagh_zamin.place(x=100, y=480)

mojavez_sakht_forosh_bagh_var=tk.IntVar(value=0)
mojavez_sakht_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=mojavez_sakht_forosh_bagh_var,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_check_btn_forosh_bagh_zamin.place(x=450, y=510)

mohavate_forosh_bagh_var=tk.IntVar(value=0)
mohavate_sazi_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=mohavate_forosh_bagh_var,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_sazi_check_btn_forosh_bagh_zamin.place(x=320, y=510)

divar_forosh_bagh_var=tk.IntVar(value=0)
divar_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=divar_forosh_bagh_var,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_forosh_bagh_zamin.place(x=180, y=220)
#endregion
#-------------------------تعویض کاربری به زمین در قسمت فروش باغ/زمین-------------
#region
option_frame_option2_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin)
option_frame_option2_forosh_bagh_zamin.place_forget()

bg_image = image_forosh_bagh_zamin
bg_image = image_forosh_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_frame_option2_forosh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

metraj_zamin2_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin2_forosh_bagh_zamin_lable.place(x=448, y=10)

metraj_zamin2_forosh_bagh_zamin_entry=tk.Entry(option_frame_option2_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin2_forosh_bagh_zamin_entry.place(x=312, y=13)

karbari_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_forosh_bagh_zamin_lable.place(x=458, y=45)

karbari_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
karbari_forosh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")        
karbari_forosh_bagh_zamin_combo["state"]=["readonly"]                        
karbari_forosh_bagh_zamin_combo.set(" ")
karbari_forosh_bagh_zamin_combo.place(x=273, y=45)

khak_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_forosh_bagh_zamin.place(x=458, y=80)

khak_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
khak_forosh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")       
khak_forosh_bagh_zamin_combo["state"]=["readonly"]                         
khak_forosh_bagh_zamin_combo.set(" ")
khak_forosh_bagh_zamin_combo.place(x=273, y=80)

ab_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع آب")
ab_forosh_bagh_zamin.place(x=458, y=115)

ab_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
ab_forosh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال آبیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")    
ab_forosh_bagh_zamin_combo["state"]=["readonly"]                            
ab_forosh_bagh_zamin_combo.set(" ")
ab_forosh_bagh_zamin_combo.place(x=273, y=115)



security_zamin_forosh_zamin_var=tk.IntVar(value=0)
security_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=security_zamin_forosh_zamin_var,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_zamin_forosh_bagh_zamin.place(x=450, y=230)


bargh_kesi_zamin_forosh_zamin_var=tk.IntVar(value=0)
bargh_kesi_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=bargh_kesi_zamin_forosh_zamin_var,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_kesi_zamin_forosh_bagh_zamin.place(x=350, y=230)

bargh_kesi_zamin_forosh_zamin2_var=tk.IntVar(value=0)
bargh_keshi_zamin_forosh_bagh_zamin2=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=bargh_kesi_zamin_forosh_zamin2_var,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_zamin_forosh_bagh_zamin2.place(x=250, y=230)


anbar_zamin_forosh_zamin_var=tk.IntVar(value=0)
anbar_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=anbar_zamin_forosh_zamin_var,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_forosh_bagh_zamin.place(x=150, y=230)


fans_zamin_forosh_zamin_var=tk.IntVar(value=0)
fans_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=fans_zamin_forosh_zamin_var,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_forosh_bagh_zamin.place(x=60, y=230)


javaz_chah_zamin_forosh_zamin_var=tk.IntVar(value=0)
mojavez_chah_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,variable=javaz_chah_zamin_forosh_zamin_var,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_chah_zamin_forosh_bagh_zamin.place(x=300, y=280)

zakhire_options_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="تایید",background="#00BFFF",fg="#000000",width=10,height=1,command=save_option_forosh_bagh_zamin)
zakhire_options_forosh_bagh_zamin.place(x=95,y=580)

back_to_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="بازگشت",command=back_to_forosh_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_forosh_bagh_zamin.place(x=215,y=580)

option_file_frame_forosh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_bagh_zamin.resizable(False, False)
#endregion
#-------------------پنجره فروش کارگاه------------------------
#region
forosh_karghah = tk.Toplevel(root)
forosh_karghah.title(" فروش کارگاه")
forosh_karghah.geometry("800x600")
forosh_karghah.withdraw()

bg_image = image_forosh_karghah
bg_image = image_forosh_karghah.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(forosh_karghah, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#----------------------کادر فروش کارگاه-----------------------#
frame_forosh_karghah= tk.Frame(forosh_karghah,bd=0,highlightthickness=0)
frame_forosh_karghah.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(forosh_karghah,text="فروش کارگاه",bg="#000000",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40


karbari_forosh_kargah=tk.Label(forosh_karghah,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
karbari_forosh_kargah.place(x=start_x + 320, y=start_y + 35, anchor="e")

karbari_forosh_kargah_entry=tk.Entry(forosh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10), justify="center")
karbari_forosh_kargah_entry.insert(0,"کارگاه")
karbari_forosh_kargah_entry.config(state="disable")
karbari_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

metraj_forosh_kargah=tk.Label(forosh_karghah,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
metraj_forosh_kargah.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

loctaion_forosh_kargah=tk.Label(forosh_karghah,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=10)
loctaion_forosh_kargah.place(x=start_x + 320, y=start_y + 135, anchor="e")

loctaion_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
loctaion_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

name_malek_forosh_kargah_lable=tk.Label(forosh_karghah, text="نام مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_malek_forosh_kargah_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

name_malek_forosh_kargah_entry=tk.Entry(forosh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_malek_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

shomareh_malek_forosh_kargah_lable=tk.Label(forosh_karghah, text="شماره مالک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_malek_forosh_kargah_lable.place(x=start_x + 320, y=start_y + 230, anchor="e")

shomareh_malek_forosh_kargah_entry=tk.Entry(forosh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_malek_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 220, width=150, height=25)

gheimat_kol_forosh_kargah_lable=tk.Label(forosh_karghah,text="قیمت کل ",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
gheimat_kol_forosh_kargah_lable.place(x=start_x + 320, y=start_y + 280, anchor="e")

gheimat_kol_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_kol_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 265, width=150, height=25)

photo_lbl2_forosh_kargah = tk.Label(forosh_karghah, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_forosh_kargah.place(x=60, y=85)

add_img_btn_forosh_kargah = tk.Button(forosh_karghah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_kargah.place(x=60, y=370)

back_to_home_forosh_kargah=tk.Button(forosh_karghah,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_karghah)
back_to_home_forosh_kargah.place(x=290,y=520)

zakhire_forosh_kargah=tk.Button(forosh_karghah,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_forosh_kargah)
zakhire_forosh_kargah.place(x=140,y=520)

forosh_karghah.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_karghah.resizable(False, False)
#endregion
#---------------------پنجره امکانات فروش کارگاه---------------------
#region
option_frame_forosh_kargah=tk.Frame(forosh_karghah,width=300,height=30,background="#052340")
option_frame_forosh_kargah.place(x=225,y=370)

option_frame_lable_forosh_kargah=tk.Label(option_frame_forosh_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_lable_forosh_kargah.pack(side="right",padx=1)

plus_button_forosh_kargah=tk.Button(option_frame_forosh_kargah,image=plus,command=open_option8,border=0)
plus_button_forosh_kargah.pack()

option_file_frame_forosh_kargah=tk.Toplevel(forosh_karghah,background="#052340")
option_file_frame_forosh_kargah.title(" امکانات فروش کارگاه")
option_file_frame_forosh_kargah.geometry("500x500")
option_file_frame_forosh_kargah.pack_propagate(False)
option_file_frame_forosh_kargah.withdraw()

bg_image = image_forosh_karghah
bg_image = image_forosh_karghah.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_kargah, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


sal_sakht_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="سال ساخت")
sal_sakht_forosh_kargah.place(x=302, y=50)

sal_sakht_forosh_kargah_entry=tk.Entry(option_file_frame_forosh_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_forosh_kargah_entry.place(x=108, y=50)

vaziat_bargh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="وضعیت برق")
vaziat_bargh_forosh_kargah.place(x=295, y=80)

vaziat_bargh_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
vaziat_bargh_forosh_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز","")
vaziat_bargh_forosh_kargah_combo.set("")
vaziat_bargh_forosh_kargah_combo["state"]=["readonly"]
vaziat_bargh_forosh_kargah_combo.place(x=70, y=80)

garmayesh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_forosh_kargah.place(x=295, y=110)

garmayesh_type_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
garmayesh_type_forosh_kargah_combo["values"]=("","بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_forosh_kargah_combo.set("")
garmayesh_type_forosh_kargah_combo["state"]=["readonly"]
garmayesh_type_forosh_kargah_combo.place(x=70, y=110)

sarmayesh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_forosh_kargah.place(x=295, y=140)

fan_forosh_kargah_var=tk.IntVar(value=0)
panke_forosh_kargah_var=tk.IntVar(value=0)
kooler_abi_forosh_kargah_var=tk.IntVar(value=0)
kooler_gazi_forosh_kargah_var=tk.IntVar(value=0)

sarmayesh_fan_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="تهویه(فن)",variable=fan_forosh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_forosh_kargah.place(x=295, y=170)

sarmayesh_panke_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="پنکه سقفی",variable=panke_forosh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_forosh_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="کولر آبی",variable=kooler_abi_forosh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_forosh_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="کولر گازی",variable=kooler_gazi_forosh_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_forosh_kargah.place(x=84, y=200)

vaziat_ab_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text=" وضعیت آب")
vaziat_ab_forosh_kargah.place(x=303, y=230)

vaziat_ab_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah,width=35)
vaziat_ab_forosh_kargah_combo["values"]=(""," آب لوله کشی(بدون فشار) " ," آب لوله کشی(همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_forosh_kargah_combo.set("")
vaziat_ab_forosh_kargah_combo["state"]=["readonly"]
vaziat_ab_forosh_kargah_combo.place(x=30, y=230)

abzar_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_forosh_kargah.place(x=298, y=260)

abzar_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah,width=23)
abzar_forosh_kargah_combo["values"]=("کارگاه خالی ","دارای دستگاه ","")
abzar_forosh_kargah_combo.set("")
abzar_forosh_kargah_combo["state"]=["readonly"]
abzar_forosh_kargah_combo.place(x=58, y=260)

toilet_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_forosh_kargah.place(x=298, y=290)

toilet_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
toilet_forosh_kargah_combo["values"]=("دارد","ندارد","")
toilet_forosh_kargah_combo.set("")
toilet_forosh_kargah_combo["state"]=["readonly"]
toilet_forosh_kargah_combo.place(x=70, y=290)

hamam_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_forosh_kargah.place(x=303, y=320)

hamam_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
hamam_forosh_kargah_combo["values"]=("ندارد","دارد","")
hamam_forosh_kargah_combo.set("")
hamam_forosh_kargah_combo["state"]=["readonly"]
hamam_forosh_kargah_combo.place(x=70, y=320)

otagh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_forosh_kargah.place(x=294, y=350)

otagh_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
otagh_forosh_kargah_combo["values"]=("ندارد","دارد","")
otagh_forosh_kargah_combo.set("")
otagh_forosh_kargah_combo["state"]=["readonly"]
otagh_forosh_kargah_combo.place(x=70, y=350)

zakhire_options_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="تایید",background="#00BFFF",fg="#000000",width=10,height=1,command=save_option_forosh_kargah)
zakhire_options_forosh_kargah.place(x=50,y=450)

back_to_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="بازگشت",command=back_to_forosh_karghah,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_forosh_kargah.place(x=170,y=450)

option_file_frame_forosh_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_kargah.resizable(False, False)
#endregion
#--------------------پنجره های ثبتی بخش درخواست-----------------------
#----------------------پنجره درخواست مسکونی--------------------------
#region
darkhast_maskoni_page = tk.Toplevel(root)
darkhast_maskoni_page.title("درخواست مسکونی")
darkhast_maskoni_page.geometry("800x600")
darkhast_maskoni_page.withdraw()

bg_image = image_darkhast_maskoni
bg_image = image_darkhast_maskoni.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(darkhast_maskoni_page, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#---------------------پنجره امکانات درخواست مسکونی----------------------
option_file_frame_darkhast_maskoni=tk.Toplevel(darkhast_maskoni_page)
option_file_frame_darkhast_maskoni.title(" امکانات درخواست مسکونی")
option_file_frame_darkhast_maskoni.geometry("500x370")
option_file_frame_darkhast_maskoni.pack_propagate(False)
option_file_frame_darkhast_maskoni.withdraw()

#------------------کادر درخواست مسکونی-----------------------------#
frame_darkhast_maskoni= tk.Frame(darkhast_maskoni_page,bd=0,highlightthickness=0)
frame_darkhast_maskoni.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(darkhast_maskoni_page,text="درخواست مسکونی",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)   

# تعیین نقطه شروع (جایی که فریم قبلی قرار داشت)
start_x = 450
start_y = 40

melk_type_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_darkhast_maskoni.place(x=start_x + 320, y=start_y + 35, anchor="e")


melk_type_darkhast_maskoni_entry=ttk.Combobox(darkhast_maskoni_page,state="readonly")
melk_type_darkhast_maskoni_entry["values"] = ("درخواست خرید مسکونی","درخواست اجاره مسکونی")
melk_type_darkhast_maskoni_entry.set("درخواست خرید مسکونی")
melk_type_darkhast_maskoni_entry.bind("<<ComboboxSelected>>",sabt_darkhast_maskoni)
melk_type_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

sal_sakht_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="سال ساخت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
sal_sakht_darkhast_maskoni.place(x=start_x + 320, y=start_y + 85, anchor="e")

sal_sakht_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
sal_sakht_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

addrres_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="آدرس",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
addrres_darkhast_maskoni.place(x=start_x + 320, y=start_y + 135, anchor="e")

addrres_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
addrres_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

tabaghe_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="طبقه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
tabaghe_darkhast_maskoni.place(x=start_x + 320, y=start_y + 185, anchor="e")

tabaghe_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
tabaghe_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

vahed_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="واحد",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
vahed_darkhast_maskoni.place(x=start_x + 320, y=start_y + 235, anchor="e")

vahed_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
vahed_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

otagh_darkhast_maskoni=tk.Label(darkhast_maskoni_page,text="اتاق",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
otagh_darkhast_maskoni.place(x=start_x + 320, y=start_y + 285, anchor="e")

otagh_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
otagh_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

mablagh_ejare_darkhast_maskoni_lable = tk.Label(darkhast_maskoni_page, text="مبلغ اجاره", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
mablagh_ejare_darkhast_maskoni_lable.place_forget()

mablagh_ejare_darkhast_maskoni_entry = tk.Entry(darkhast_maskoni_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
mablagh_ejare_darkhast_maskoni_entry.place_forget()

gheimat_pish_darkhast_maskoni_lable = tk.Label(darkhast_maskoni_page, text="مبلغ پیش", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_pish_darkhast_maskoni_lable.place_forget()

gheimat_pish_darkhast_maskoni_entry = tk.Entry(darkhast_maskoni_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_pish_darkhast_maskoni_entry.place_forget()

ejareh_mahane_darkhast_maskoni_lable = tk.Label(darkhast_maskoni_page, text="اجاره ماهانه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
ejareh_mahane_darkhast_maskoni_lable.place_forget()

ejareh_mahane_darkhast_maskoni_entry = tk.Entry(darkhast_maskoni_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
ejareh_mahane_darkhast_maskoni_entry.place_forget()

name_moshtari_darkhast_maskoni_lable = tk.Label(darkhast_maskoni_page, text="نام مشتری", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 340,anchor="e")

name_moshtari_darkhast_maskoni_entry = tk.Entry(darkhast_maskoni_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)

shomareh_moshtari_darkhast_maskoni_lable = tk.Label(darkhast_maskoni_page, text="شماره مشتری", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_moshtari_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 390,anchor="e")

shomareh_moshtari_darkhast_maskoni_entry = tk.Entry(darkhast_maskoni_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_moshtari_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)

gheimat_kol_darkhast_maskoni_lable=tk.Label(darkhast_maskoni_page,text="قیمت کل",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_kol_darkhast_maskoni_lable.place(x=start_x + 320, y=start_y + 445, anchor="e")

gheimat_kol_darkhast_maskoni_entry=tk.Entry(darkhast_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_kol_darkhast_maskoni_entry.place(x=start_x + 10, y=start_y + 430, width=150, height=25)

back_to_home_darkhast_maskoni=tk.Button(darkhast_maskoni_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_darkhast_maskoni)
back_to_home_darkhast_maskoni.place(x=270,y=520)

zakhire_darkhast_maskoni=tk.Button(darkhast_maskoni_page,text="ذخیره",bg="#00BFFF",fg="black",width=10,height=2,command=sabt_darkhast_maskoni)
zakhire_darkhast_maskoni.place(x=120,y=520)

photo_lbl2_darkhast_maskoni = tk.Label(darkhast_maskoni_page, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_darkhast_maskoni.place(x=60, y=85)

add_img_btn_darkhast_maskoni = tk.Button(darkhast_maskoni_page, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_darkhast_maskoni.place(x=60, y=370)

darkhast_maskoni_page.protocol("WM_DELETE_WINDOW", lambda: None)
darkhast_maskoni_page.resizable(False, False)
#endregion
#------------------------امکانات درخواست مسکونی--------------------
#region
option_frame_options_darkhast_maskoni=tk.Frame(darkhast_maskoni_page,width=300,height=30,background="#052340")
option_frame_options_darkhast_maskoni.place(x=225,y=370)

option_label_darkhast_maskoni=tk.Label(option_frame_options_darkhast_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_darkhast_maskoni.pack(side="right",padx=1)

plus_button_darkhast_maskoni=tk.Button(option_frame_options_darkhast_maskoni,image=plus,command=open_option9,border=0)
plus_button_darkhast_maskoni.pack()

bg_image = image_darkhast_maskoni
bg_image = image_darkhast_maskoni.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_darkhast_maskoni, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_darkhast_maskoni_var=tk.IntVar(value=0)
anbari_darkhast_maskoni_var=tk.IntVar(value=0)
asansor_darkhast_maskoni_var=tk.IntVar(value=0)

parking_ch_btn_darkhast_maskoni=tk.Checkbutton(option_file_frame_darkhast_maskoni,variable=parking_darkhast_maskoni_var,image=parking_pic,background="#052340")
parking_ch_btn_darkhast_maskoni.place(x=140, y=50)

asansor_ch_btn_darkhast_maskoni=tk.Checkbutton(option_file_frame_darkhast_maskoni,variable=asansor_darkhast_maskoni_var,image=elvator_pic,background="#052340")
asansor_ch_btn_darkhast_maskoni.place(x=240, y=50)

anbari_checkbuton_darkhast_maskoni=tk.Checkbutton(option_file_frame_darkhast_maskoni,variable=anbari_darkhast_maskoni_var,image=warehouse_pic,background="#052340")
anbari_checkbuton_darkhast_maskoni.place(x=340, y=50)

sarmaesh_darkhast_maskoni=tk.Label(option_file_frame_darkhast_maskoni,text="سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
sarmaesh_darkhast_maskoni.place(x=320, y=110)

sarmaesh_combo_darkhast_maskoni=ttk.Combobox(option_file_frame_darkhast_maskoni)
sarmaesh_combo_darkhast_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_darkhast_maskoni["state"]=["readonly"]
sarmaesh_combo_darkhast_maskoni.place(x=120, y=110)

garmaesh_darkhast_maskoni=tk.Label(option_file_frame_darkhast_maskoni,text="گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
garmaesh_darkhast_maskoni.place(x=320, y=150)

garmaesh_combo_darkhast_maskoni=ttk.Combobox(option_file_frame_darkhast_maskoni)
garmaesh_combo_darkhast_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_darkhast_maskoni["state"]=["readonly"]
garmaesh_combo_darkhast_maskoni.place(x=120, y=150)

kaf_darkhast_maskoni=tk.Label(option_file_frame_darkhast_maskoni,text="کف",background="#052340",fg="#ffffff",font=("Shabnam",11))
kaf_darkhast_maskoni.place(x=320, y=190)

kaf_combo_darkhast_maskoni=ttk.Combobox(option_file_frame_darkhast_maskoni)
kaf_combo_darkhast_maskoni["state"]=["readonly"]
kaf_combo_darkhast_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_darkhast_maskoni.place(x=120, y=190)

toilet_darkhast_maskoni=tk.Label(option_file_frame_darkhast_maskoni,text="سرویس بهداشتی",background="#052340",fg="#ffffff",font=("Shabnam",11))
toilet_darkhast_maskoni.place(x=320, y=230)

toilet_combo_darkhast_maskoni=ttk.Combobox(option_file_frame_darkhast_maskoni)
toilet_combo_darkhast_maskoni["state"]=["readonly"]
toilet_combo_darkhast_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_darkhast_maskoni.place(x=120, y=230)

zakhire_options_darkhast_maskoni=tk.Button(option_file_frame_darkhast_maskoni,text="تایید",command=save_option_darkhast_maskoni,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_darkhast_maskoni.place(x=95, y=320)

back_to_home_darkhast_maskoni=tk.Button(option_file_frame_darkhast_maskoni,text="بازگشت",command=back_to_darkhast_maskoni,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_darkhast_maskoni.place(x=215, y=320)

option_file_frame_darkhast_maskoni.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_darkhast_maskoni.resizable(False, False)
#endregion
#-----------------پنجره درخواست اداری/تجاری-------------------
#region
darkhast_edari_tejari = tk.Toplevel(root)
darkhast_edari_tejari.title(" درخواست اداری / تجاری")
darkhast_edari_tejari.geometry("800x600")
darkhast_edari_tejari.withdraw()

bg_image = image_darkhast_edari_tejari
bg_image = image_darkhast_edari_tejari.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(darkhast_edari_tejari, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------پنجره امکانات درخواست اداری/تجاری----------------

option_file_frame_darkhast_edari_tejari=tk.Toplevel(darkhast_edari_tejari,background="#052340" )
option_file_frame_darkhast_edari_tejari.title(" امکانات درخواست اداری/تجاری")
option_file_frame_darkhast_edari_tejari.geometry("500x370")
option_file_frame_darkhast_edari_tejari.pack_propagate(False)
option_file_frame_darkhast_edari_tejari.withdraw()

#----------------------کادر درخواست اداری و تجاری------------------#
frame_darkhast_edari_tejari= tk.Frame(darkhast_edari_tejari,bd=0,highlightthickness=0)
frame_darkhast_edari_tejari.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(darkhast_edari_tejari,text="درخواست اداری و تجاری",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

melk_type_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")


combo_darkhast_edari_tejari_entry=ttk.Combobox(darkhast_edari_tejari,state="readonly")
combo_darkhast_edari_tejari_entry["values"] = ("درخواست اجاره اداری/تجاری","درخواست خرید اداری/تجاری")
combo_darkhast_edari_tejari_entry.set("درخواست خرید اداری/تجاری")
combo_darkhast_edari_tejari_entry.bind("<<ComboboxSelected>>",sabt_darkhast_edari_tejari)
combo_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 25, width=170, height=25)

metraj_melk_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="متراژ ملک ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
metraj_melk_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_melk_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
metraj_melk_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

sal_sakht_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="سال ساخت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
sal_sakht_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

sal_sakht_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
sal_sakht_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

addrres_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="آدرس",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
addrres_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

addrres_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
addrres_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

tabaghe_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="طبقه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
tabaghe_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

tabaghe_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
tabaghe_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

vahed_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="واحد",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
vahed_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

vahed_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
vahed_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

gheimat_kol_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text= "قیمت کل",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_kol_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")

gheimat_kol_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
gheimat_kol_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 425, width=150, height=25)

mablagh_vadie_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="مبلغ ودیعه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_vadie_darkhast_edari_tejari_lable.place_forget()

mablagh_vadie_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_vadie_darkhast_edari_tejari_entry.place_forget()

mablagh_ejareh_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="مبلغ اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_ejareh_darkhast_edari_tejari_lable.place_forget()

mablagh_ejareh_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_ejareh_darkhast_edari_tejari_entry.place_forget()

name_moshtari_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="نام مشتری",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
name_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

name_moshtari_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
name_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

shomareh_moshtari_darkhast_edari_tejari_lable=tk.Label(darkhast_edari_tejari,text="شماره مشتری",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
shomareh_moshtari_darkhast_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

shomareh_moshtari_darkhast_edari_tejari_entry=tk.Entry(darkhast_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
shomareh_moshtari_darkhast_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

back_to_home_darkhast_edari_tejari=tk.Button(darkhast_edari_tejari,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_darkhast_edari_tejari)
back_to_home_darkhast_edari_tejari.place(x=280,y=520)

zakhire_darkhast_edari_tejari=tk.Button(darkhast_edari_tejari,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_darkhast_edari_tejari)
zakhire_darkhast_edari_tejari.place(x=130,y=520)

photo_lbl2_darkhast_edari_tejari = tk.Label(darkhast_edari_tejari, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_darkhast_edari_tejari.place(x=60, y=85)

add_img_btn_darkhast_edari_tejari = tk.Button(darkhast_edari_tejari, text="افزودن تصویر", bg="#00BFFF", fg="#000000",command=open_file,height=2,width=13)
add_img_btn_darkhast_edari_tejari.place(x=60, y=370)

darkhast_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
darkhast_edari_tejari.resizable(False, False)
#endregion
#---------------امکانات درخواست اداری/تجاری-------------------
#region
option_frame_options_darkhast_edari_tejari=tk.Frame(darkhast_edari_tejari,width=300,height=30,background="#052340")
option_frame_options_darkhast_edari_tejari.place(x=225,y=370)

option_label_darkhast_edari_tejari=tk.Label(option_frame_options_darkhast_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_darkhast_edari_tejari.pack(side="right",padx=1)

plus_button_darkhast_edari_tejari=tk.Button(option_frame_options_darkhast_edari_tejari,image=plus,command=open_option10,border=0)
plus_button_darkhast_edari_tejari.pack()

bg_image = image_darkhast_edari_tejari
bg_image = image_darkhast_edari_tejari.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_darkhast_edari_tejari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_darkhast_edari_tejari_var=tk.IntVar(value=0)
anbari_darkhast_edari_tejari_var=tk.IntVar(value=0)
asansor_darkhast_edari_tejari_var=tk.IntVar(value=0)

parking_check_btn_darkhast_edari_tejari=tk.Checkbutton(option_file_frame_darkhast_edari_tejari,variable=parking_darkhast_edari_tejari_var,image=parking_pic,background="#052340")
parking_check_btn_darkhast_edari_tejari.place(x=140, y=50)

asansor_check_btn_darkhast_edari_tejari=tk.Checkbutton(option_file_frame_darkhast_edari_tejari,variable=asansor_darkhast_edari_tejari_var,image=elvator_pic,background="#052340")
asansor_check_btn_darkhast_edari_tejari.place(x=240, y=50)

anbari_check_btn_darkhast_edari_tejari=tk.Checkbutton(option_file_frame_darkhast_edari_tejari,variable=anbari_darkhast_edari_tejari_var,image=warehouse_pic,background="#052340")
anbari_check_btn_darkhast_edari_tejari.place(x=340, y=50)

aab_va_gaz_emkanat_darkhast_edari_tejari=tk.Label(option_file_frame_darkhast_edari_tejari,text="وضعیت آب و گاز",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
aab_va_gaz_emkanat_darkhast_edari_tejari.place(x=320, y=110)

aab_va_gaz_combo_emkanat_darkhast_edari_tejari=ttk.Combobox(option_file_frame_darkhast_edari_tejari)
aab_va_gaz_combo_emkanat_darkhast_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_darkhast_edari_tejari["state"]=["readonly"]
aab_va_gaz_combo_emkanat_darkhast_edari_tejari.place(x=120, y=110)

sarmayesh_emkanat_darkhast_edari_tejari=tk.Label(option_file_frame_darkhast_edari_tejari,text="سیستم سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
sarmayesh_emkanat_darkhast_edari_tejari.place(x=320, y=150)

sarmayesh_combo_emkanat_darkhast_edari_tejari=ttk.Combobox(option_file_frame_darkhast_edari_tejari)
sarmayesh_combo_emkanat_darkhast_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_darkhast_edari_tejari["state"]=["readonly"]
sarmayesh_combo_emkanat_darkhast_edari_tejari.place(x=120, y=150)

garmayesh_emkanat_darkhast_edari_tejari=tk.Label(option_file_frame_darkhast_edari_tejari,text="سیستم گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
garmayesh_emkanat_darkhast_edari_tejari.place(x=320, y=190)

garmayesh_combo_emkanat_darkhast_edari_tejari=ttk.Combobox(option_file_frame_darkhast_edari_tejari)
garmayesh_combo_emkanat_darkhast_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_darkhast_edari_tejari["state"]=["readonly"]
garmayesh_combo_emkanat_darkhast_edari_tejari.place(x=120, y=190)

zakhire_options_darkhast_edari_tejari=tk.Button(option_file_frame_darkhast_edari_tejari,text="تایید",command=save_option_darkhast_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_darkhast_edari_tejari.place(x=95,y=320)

back_to_home_darkhast_edari_tejari=tk.Button(option_file_frame_darkhast_edari_tejari,text="بازگشت",command=back_to_darkhast_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_darkhast_edari_tejari.place(x=215,y=320)

option_file_frame_darkhast_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_darkhast_edari_tejari.resizable(False, False)
#endregion
#--------------------پنجره درخواست باغ/زمین-----------------------
#region
darkhast_bagh_zamin = tk.Toplevel(root)
darkhast_bagh_zamin.title("درخواست باغ و زمین")
darkhast_bagh_zamin.geometry("800x600")
darkhast_bagh_zamin.withdraw()

bg_image = image_darkhast_bagh_zamin
bg_image = image_darkhast_bagh_zamin.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(darkhast_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------------کادر درخواست باغ و زمین---------------------#
frame_darkhast_bagh_zamin= tk.Frame(darkhast_bagh_zamin,bd=0,highlightthickness=0)
frame_darkhast_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(darkhast_bagh_zamin,text="درخواست باغ و زمین",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40


melk_type_darkhast_bagh_zamin_lable=tk.Label(darkhast_bagh_zamin,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
melk_type_darkhast_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_darkhast_bagh_zamin_entry=ttk.Combobox(darkhast_bagh_zamin,font=("Shabnam", 10),justify="center",state="readonly")
melk_type_darkhast_bagh_zamin_entry["values"]=("درخواست خرید باغ زمین","درخواست اجاره باغ زمین")
melk_type_darkhast_bagh_zamin_entry.set("درخواست خرید باغ زمین")
melk_type_darkhast_bagh_zamin_entry.bind("<<ComboboxSelected>>",sabt_darkhast_bagh_zamin)
melk_type_darkhast_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)


metraj_zamin_darkhast_bagh_zamin_lable=tk.Label(darkhast_bagh_zamin,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
metraj_zamin_darkhast_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_zamin_darkhast_bagh_zamin_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_darkhast_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

bagh_type_darkhast_bagh_zamin_lable=tk.Label(darkhast_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
bagh_type_darkhast_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

bagh_type_darkhast_bagh_zamin_combo=ttk.Combobox(darkhast_bagh_zamin,state="readonly")
bagh_type_darkhast_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_darkhast_bagh_zamin_combo.set("باغ")
bagh_type_darkhast_bagh_zamin_combo.place(x=start_x + 10, y=start_y + 125, width=150, height=25)
bagh_type_darkhast_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_darkhast_bagh)

bagh_loctaion_darkhast_bagh_zamin_lable=tk.Label(darkhast_bagh_zamin,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
bagh_loctaion_darkhast_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_darkhast_bagh_zamin_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
bagh_loctaion_darkhast_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

#gheimat_darkhast_bagh_zamin_lable=tk.Label(darkhast_bagh_zamin,text='قیمت کل',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
#gheimat_darkhast_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

#gheimat_darkhast_bagh_zamin_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
#gheimat_darkhast_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

gheimat_ejareh_bagh_darkhast_zamin_lable=tk.Label(darkhast_bagh_zamin, text="ودیعه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_ejareh_bagh_darkhast_zamin_lable.place_forget()

gheimat_ejareh_bagh_darkhast_zamin_entry=tk.Entry(darkhast_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_ejareh_bagh_darkhast_zamin_entry.place_forget()

gheimat_har_matr_bagh_zamin_darkhast_lable=tk.Label(darkhast_bagh_zamin,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_har_matr_bagh_zamin_darkhast_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_har_metr_bagh_zamin_darkhast_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_bagh_zamin_darkhast_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

mablagh_ejareh_mahaneh_darkhast_lable=tk.Label(darkhast_bagh_zamin,text='اجاره ماهانه',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
mablagh_ejareh_mahaneh_darkhast_lable.place_forget()

mablagh_ejareh_mahaneh_darkhast_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
mablagh_ejareh_mahaneh_darkhast_entry.place_forget()

time_ejareh_bagh_darkhast_zamin_lable=tk.Label(darkhast_bagh_zamin,text="مدت اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
time_ejareh_bagh_darkhast_zamin_lable.place_forget()

bagh_time_darkhast_combo=ttk.Combobox(darkhast_bagh_zamin,state="readonly")
bagh_time_darkhast_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_darkhast_combo.set("فصلی")
bagh_time_darkhast_combo.place_forget()


name_moshtari_darkhast_bagh_lable=tk.Label(darkhast_bagh_zamin,text="نام مشتری",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
name_moshtari_darkhast_bagh_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

name_moshtari_darkhast_bagh_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
name_moshtari_darkhast_bagh_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

shomareh_moshtari_darkhast_bagh_lable=tk.Label(darkhast_bagh_zamin,text="شماره مشتری",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
shomareh_moshtari_darkhast_bagh_lable.place(x=start_x + 320, y=start_y + 340, anchor="e")

shomareh_moshtari_darkhast_bagh_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
shomareh_moshtari_darkhast_bagh_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)

gheimat_kol_bagh_zamin_darkhast_lable=tk.Label(darkhast_bagh_zamin,text='قیمت کل',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_kol_bagh_zamin_darkhast_lable.place(x=start_x + 325, y=start_y + 390, anchor="e")

gheimat_kol_bagh_zamin_darkhast_entry=tk.Entry(darkhast_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_kol_bagh_zamin_darkhast_entry.place(x=start_x + 10, y=start_y + 380, width=150, height=25)

photo_darkhast_bagh_zamin_lable= tk.Label(darkhast_bagh_zamin, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_darkhast_bagh_zamin_lable.place(x=60, y=85)

add_img_btn_darkhast_bagh_zamin = tk.Button(darkhast_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="#000000",command=open_file,height=2,width=13)
add_img_btn_darkhast_bagh_zamin.place(x=60, y=370)

back_to_home_darkhast_bagh_zamin=tk.Button(darkhast_bagh_zamin,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_darkhast_bagh)
back_to_home_darkhast_bagh_zamin.place(x=290,y=520)

zakhire_darkhast_bagh_zamin=tk.Button(darkhast_bagh_zamin,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=sabt_darkhast_bagh_zamin)
zakhire_darkhast_bagh_zamin.place(x=140,y=520)

darkhast_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
darkhast_bagh_zamin.resizable(False, False)
#endregion
#-----------------------پنجره امکانات درخواست باغ/زمین-------------------
#region
option_frame_options_darkhast_bagh_zamin=tk.Frame(darkhast_bagh_zamin,width=300,height=30,background="#052340")
option_frame_options_darkhast_bagh_zamin.place(x=225,y=370)

option_label_darkhast_bagh_zamin=tk.Label(option_frame_options_darkhast_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_darkhast_bagh_zamin.pack(side="right",padx=1)

plus_button_darkhast_bagh_zamin=tk.Button(option_frame_options_darkhast_bagh_zamin,image=plus,command=open_option11,border=0)
plus_button_darkhast_bagh_zamin.pack()

option_file_frame_darkhast_bagh_zamin=tk.Toplevel(darkhast_bagh_zamin)
option_file_frame_darkhast_bagh_zamin.title(" امکانات درخواست باغ/زمین")
option_file_frame_darkhast_bagh_zamin.geometry("690x630")
option_file_frame_darkhast_bagh_zamin.pack_propagate(False)
option_file_frame_darkhast_bagh_zamin.withdraw()

option_frame_darkhast_bagh_zamin=tk.Frame(option_file_frame_darkhast_bagh_zamin)
option_frame_darkhast_bagh_zamin.place(x=50,y=50)

bg_image = image_darkhast_bagh_zamin
bg_image = image_darkhast_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_darkhast_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



metraj_derakht_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_derakht_darkhast_bagh_zamin_lable.place(x=450, y=70)

metraj_derakht_darkhast_bagh_zamin_entry=tk.Entry(option_file_frame_darkhast_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_derakht_darkhast_bagh_zamin_entry.place(x=305, y=70)

tedad_derakht_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tedad_derakht_darkhast_bagh_zamin_lable.place(x=460, y=100)

tedad_derakht_darkhast_bagh_zamin_entry=tk.Entry(option_file_frame_darkhast_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tedad_derakht_darkhast_bagh_zamin_entry.place(x=305, y=100)

abyari_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع آبیاری")
abyari_darkhast_bagh_zamin_lable.place(x=460, y=130)

abyari_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin)
abyari_darkhast_bagh_zamin_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_darkhast_bagh_zamin_combo["state"]=["readonly"]
abyari_darkhast_bagh_zamin_combo.set("سطحی")
abyari_darkhast_bagh_zamin_combo.place(x=273, y=130)

type_tree_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع درخت")
type_tree_darkhast_bagh_zamin_lable.place(x=460, y=160)

type_tree_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin)
type_tree_darkhast_bagh_zamin_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","آلبالو")
type_tree_darkhast_bagh_zamin_combo.set("گردو")
type_tree_darkhast_bagh_zamin_combo["state"]=["readonly"]
type_tree_darkhast_bagh_zamin_combo.place(x=273, y=160)

type_tree_darkhast_btn=tk.Button(option_file_frame_darkhast_bagh_zamin,text="افزودن درخت",command=add_tree3,bg="#00BFFF",font=("Shabnam",9),width=10)
type_tree_darkhast_btn.place(x=460, y=190)

label_natige_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,text="")
label_natige_darkhast_bagh_zamin.place(x=305, y=190)

chah_darkhast_bagh_zamin_var=tk.IntVar(value=0)
chah_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=chah_darkhast_bagh_zamin_var,text="چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
chah_darkhast_bagh_zamin.place(x=480, y=220)

estakhr_darkhast_bagh_zamin_var=tk.IntVar(value=0)
estakhr_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=estakhr_darkhast_bagh_zamin_var,text="استخر",background="#052340",fg="#00BFFF",font=("Shabnam",9))
estakhr_darkhast_bagh_zamin.place(x=380, y=220)

divar_darkhast_bagh_zamin_var=tk.IntVar(value=0)
divar_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=divar_darkhast_bagh_zamin_var,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_darkhast_bagh_zamin.place(x=280, y=220)

bargh_keshi_darkhast_bagh_zamin_var=tk.IntVar(value=0)
bargh_keshi_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=bargh_keshi_darkhast_bagh_zamin_var,text="برق کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_darkhast_bagh_zamin.place(x=180, y=220)



var0_darkhast_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه


otagh_check_btn_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=var0_darkhast_bagh_zamin,image=warehouse_pic,background="#052340",text="ساختمان",command=home_true_false3)
otagh_check_btn_darkhast_bagh_zamin.place(x=470, y=250)

metraj_vila_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ سازه")
metraj_vila_darkhast_bagh_zamin.place(x=450, y=300)

metraj_vila_darkhast_bagh_zamin_entry=tk.Entry(option_file_frame_darkhast_bagh_zamin,width=10,bg="#00BFFF",fg="#ffffff",state="disabled")
metraj_vila_darkhast_bagh_zamin_entry.place(x=305, y=300)

sal_sakht_vila_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سال ساخت")
sal_sakht_vila_darkhast_bagh_zamin_lable.place(x=450, y=330)

sal_sakht_vila_darkhast_bagh_zamin_entry=tk.Entry(option_file_frame_darkhast_bagh_zamin,width=10,bg="#00BFFF",fg="#ffffff",state="disabled")
sal_sakht_vila_darkhast_bagh_zamin_entry.place(x=305, y=330)

type_vila_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="نوع سازه")
type_vila_darkhast_bagh_zamin.place(x=450, y=360)

type_vila_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin,state="disabled")
type_vila_darkhast_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_darkhast_bagh_zamin_combo.set("آجری")
type_vila_darkhast_bagh_zamin_combo.place(x=273, y=360)

toilet_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سرویس بهداشتی")
toilet_darkhast_bagh_zamin_lable.place(x=450, y=390)

toilet_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin,state="disabled")
toilet_darkhast_bagh_zamin_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_darkhast_bagh_zamin_combo.set("")
toilet_darkhast_bagh_zamin_combo.place(x=273, y=390)

hamam_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="حمام")
hamam_darkhast_bagh_zamin.place(x=450, y=420)

hamam_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin,state="disabled")
hamam_darkhast_bagh_zamin_combo["values"]=(" ","ندارد","دارد")
hamam_darkhast_bagh_zamin_combo.set(" ")
hamam_darkhast_bagh_zamin_combo.place(x=273, y=420)

sanad_darkhast_bagh_zamin_lable=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سند")
sanad_darkhast_bagh_zamin_lable.place(x=450, y=450)

sanad_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin,state="disabled")
sanad_darkhast_bagh_zamin_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_darkhast_bagh_zamin_combo.set(" ")
sanad_darkhast_bagh_zamin_combo.place(x=273, y=450)

option_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="امکانات تفریحی")
option_darkhast_bagh_zamin.place(x=450, y=480)

option_darkhast_bagh_zamin_combo=ttk.Combobox(option_file_frame_darkhast_bagh_zamin,state="disabled")
option_darkhast_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_darkhast_bagh_zamin_combo.set(" ")
option_darkhast_bagh_zamin_combo.place(x=273, y=480)

add_option_button_darkhast_bagh_zamin=tk.Button(option_file_frame_darkhast_bagh_zamin,text="افزودن امکانات",command=add_option3,bg="#00BFFF",font=("Shabnam",9),width=10)
add_option_button_darkhast_bagh_zamin.place(x=180, y=480)

lable_natige_add_darkhast_bagh_zamin=tk.Label(option_file_frame_darkhast_bagh_zamin,text="")
lable_natige_add_darkhast_bagh_zamin.place(x=100, y=480)

mojavez_sakht_darkhast_bagh_zamin_var=tk.IntVar(value=0)
mojavez_sakht_check_btn_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=mojavez_sakht_darkhast_bagh_zamin_var,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_check_btn_darkhast_bagh_zamin.place(x=450, y=510)

mohavate_sazi_darkhast_bagh_zamin_var=tk.IntVar(value=0)
mohavate_sazi_check_btn_darkhast_bagh_zamin=tk.Checkbutton(option_file_frame_darkhast_bagh_zamin,variable=mohavate_sazi_darkhast_bagh_zamin_var,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_sazi_check_btn_darkhast_bagh_zamin.place(x=320, y=510)


#endregion
#-------------------------تعویض کاربری به زمین در قسمت درخواست باغ/زمین-------------
#region
option_frame_option2_darkhast_bagh_zamin=tk.Frame(option_file_frame_darkhast_bagh_zamin)
option_frame_option2_darkhast_bagh_zamin.place_forget()

bg_image = image_darkhast_bagh_zamin
bg_image = image_darkhast_bagh_zamin.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_frame_option2_darkhast_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

metraj_zamin2_darkhast_bagh_zamin_lable=tk.Label(option_frame_option2_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin2_darkhast_bagh_zamin_lable.place(x=448, y=10)

metraj_zamin2_darkhast_bagh_zamin_entry=tk.Entry(option_frame_option2_darkhast_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin2_darkhast_bagh_zamin_entry.place(x=312, y=13)

karbari_darkhast_bagh_zamin_lable=tk.Label(option_frame_option2_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_darkhast_bagh_zamin_lable.place(x=458, y=45)

karbari_darkhast_bagh_zamin_combo=ttk.Combobox(option_frame_option2_darkhast_bagh_zamin)
karbari_darkhast_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")           
karbari_darkhast_bagh_zamin_combo["state"]=["readonly"]                  
karbari_darkhast_bagh_zamin_combo.set(" ")
karbari_darkhast_bagh_zamin_combo.place(x=273, y=45)

khak_darkhast_bagh_zamin=tk.Label(option_frame_option2_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_darkhast_bagh_zamin.place(x=458, y=80)

khak_darkhast_bagh_zamin_combo=ttk.Combobox(option_frame_option2_darkhast_bagh_zamin)
khak_darkhast_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")        
khak_darkhast_bagh_zamin_combo["state"]=["readonly"]                     
khak_darkhast_bagh_zamin_combo.set(" ")
khak_darkhast_bagh_zamin_combo.place(x=273, y=80)

ab_darkhast_bagh_zamin=tk.Label(option_frame_option2_darkhast_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع آب")
ab_darkhast_bagh_zamin.place(x=458, y=115)

ab_darkhast_bagh_zamin_combo=ttk.Combobox(option_frame_option2_darkhast_bagh_zamin)
ab_darkhast_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال آبیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")  
ab_darkhast_bagh_zamin_combo["state"]=["readonly"]
ab_darkhast_bagh_zamin_combo.set(" ")
ab_darkhast_bagh_zamin_combo.place(x=273, y=115)

security_zamin_darkhast_bagh_zamin_var=tk.IntVar(value=0)
security_zamin_darkhast_bagh_zamin=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=security_zamin_darkhast_bagh_zamin_var,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_zamin_darkhast_bagh_zamin.place(x=450, y=230)

bargh_kesi_zamin_darkhast_bagh_zamin_var=tk.IntVar(value=0)
bargh_kesi_zamin_darkhast_bagh_zamin=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=bargh_kesi_zamin_darkhast_bagh_zamin_var,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_kesi_zamin_darkhast_bagh_zamin.place(x=350, y=230)


bargh_zamin_darkhast_bagh_zamin2_var=tk.IntVar(value=0)
bargh_keshi_zamin_darkhast_bagh_zamin2=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=bargh_zamin_darkhast_bagh_zamin2_var,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_zamin_darkhast_bagh_zamin2.place(x=250, y=230)

anbar_zamin_darkhast_bagh_zamin_var=tk.IntVar(value=0)
anbar_zamin_darkhast_bagh_zamin=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=anbar_zamin_darkhast_bagh_zamin_var,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_darkhast_bagh_zamin.place(x=150, y=230)

fans_zamin_darkhast_bagh_zamin_var=tk.IntVar(value=0)
fans_zamin_darkhast_bagh_zamin=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=fans_zamin_darkhast_bagh_zamin_var,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_darkhast_bagh_zamin.place(x=60, y=230)

mojavez_chah_zamin_darkhast_bagh_zamin_var=tk.IntVar(value=0)
mojavez_chah_zamin_darkhast_bagh_zamin=tk.Checkbutton(option_frame_option2_darkhast_bagh_zamin,variable=mojavez_chah_zamin_darkhast_bagh_zamin_var,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_chah_zamin_darkhast_bagh_zamin.place(x=300, y=280)



zakhire_options_darkhast_bagh_zamin=tk.Button(option_file_frame_darkhast_bagh_zamin,command=save_option_darkhast_bagh_zamin,text="تایید",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_darkhast_bagh_zamin.place(x=95,y=580)

back_to_darkhast_bagh_zamin=tk.Button(option_file_frame_darkhast_bagh_zamin,text="بازگشت",command=back_to_darkhast_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_darkhast_bagh_zamin.place(x=215,y=580)

option_file_frame_darkhast_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_darkhast_bagh_zamin.resizable(False, False)
#endregion
#-------------------پنجره درخواست کارگاه------------------------
#region
darkhast_kargah= tk.Toplevel(root)
darkhast_kargah.title("درخواست کارگاه")
darkhast_kargah.geometry("800x600")
darkhast_kargah.withdraw()

bg_image = image_darkhast_kargah
bg_image = image_darkhast_kargah.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(darkhast_kargah, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#----------------------کادر درخواست کارگاه-----------------------#
frame_darkhast_kargah=tk.Frame(darkhast_kargah,bd=0,highlightthickness=0)
frame_darkhast_kargah.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(darkhast_kargah,text="درخواست کارگاه",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

karbari_zamin_darkhast_kargah=tk.Label(darkhast_kargah,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
karbari_zamin_darkhast_kargah.place(x=start_x + 320, y=start_y + 35, anchor="e")

combo_darkhast_kargah=ttk.Combobox(darkhast_kargah)
combo_darkhast_kargah["values"] = ("درخواست اجاره کارگاه","درخواست خرید کارگاه")
combo_darkhast_kargah["state"]=["readonly"]
combo_darkhast_kargah.set("درخواست خرید کارگاه")
combo_darkhast_kargah.bind("<<ComboboxSelected>>",sabt_darkhast_kargah)
combo_darkhast_kargah.place(x=start_x + 10, y=start_y + 25)


darkhast_kargah_lable=tk.Label(darkhast_kargah,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_darkhast_kargah_entry=tk.Entry(darkhast_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

loctaion_darkhast_kargah_lable=tk.Label(darkhast_kargah,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
loctaion_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

loctaion_darkhast_kargah_entry=tk.Entry(darkhast_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
loctaion_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

mablagh_pish_darkhast_kargah_lable=tk.Label(darkhast_kargah,text='ودیعه',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
mablagh_pish_darkhast_kargah_lable.place_forget()

mablagh_pish_darkhast_kargah_entry=tk.Entry(darkhast_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
mablagh_pish_darkhast_kargah_entry.place_forget()

gheimat_kol_darkhast_kargah_lable=tk.Label(darkhast_kargah,text='قیمت کل',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_kol_darkhast_kargah_lable.place(x=start_x + 320, y=start_y +274,anchor="e")

gheimat_kol_darkhast_kargah_entry=tk.Entry(darkhast_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
gheimat_kol_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 218,width=150, height=25)

name_moshtari_darkhast_kargah_lable=tk.Label(darkhast_kargah, text="نام مشتری", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
name_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 180, anchor="e")

name_moshtari_darkhast_kargah_entry=tk.Entry(darkhast_kargah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
name_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 170, width=150, height=25)

shomareh_moshtari_darkhast_kargah_lable=tk.Label(darkhast_kargah, text="شماره مشتری", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
shomareh_moshtari_darkhast_kargah_lable.place(x=start_x + 320, y=start_y + 230, anchor="e")

shomareh_moshtari_darkhast_kargah_entry=tk.Entry(darkhast_kargah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
shomareh_moshtari_darkhast_kargah_entry.place(x=start_x + 10, y=start_y + 260, width=150, height=25)

ejareh_mahaneh_darkhast_kargah_lable=tk.Label(darkhast_kargah, text=" اجاره ماهانه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
ejareh_mahaneh_darkhast_kargah_lable.place_forget()

ejareh_mahaneh_darkhast_kargah_entry=tk.Entry(darkhast_kargah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
ejareh_mahaneh_darkhast_kargah_entry.place_forget()

photo_lbl2_darkhast_kargah = tk.Label(darkhast_kargah, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_darkhast_kargah.place(x=60, y=85)

add_img_btn_darkhast_kargah = tk.Button(darkhast_kargah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_darkhast_kargah.place(x=60, y=370)

back_to_home_darkhast_kargah=tk.Button(darkhast_kargah,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_darkhast_kargah)
back_to_home_darkhast_kargah.place(x=290,y=520)

zakhire_darkhast_kargah=tk.Button(darkhast_kargah,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=sabt_darkhast_kargah)
zakhire_darkhast_kargah.place(x=140,y=520)

darkhast_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
darkhast_kargah.resizable(False, False)
#endregion
#---------------------پنجره امکانات درخواست کارگاه---------------------
#region
option_frame_darkhast_kargah=tk.Frame(darkhast_kargah,width=300,height=30,background="#052340")
option_frame_darkhast_kargah.place(x=225,y=370)

option_frame_darkhast_kargah_lable=tk.Label(option_frame_darkhast_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_darkhast_kargah_lable.pack(side="right",padx=1)

plus_button_darkhast_kargah=tk.Button(option_frame_darkhast_kargah,image=plus,command=open_option12,border=0)
plus_button_darkhast_kargah.pack()

option_file_frame_darkhast_kargah=tk.Toplevel(darkhast_kargah)
option_file_frame_darkhast_kargah.title(" امکانات درخواست کارگاه")
option_file_frame_darkhast_kargah.geometry("500x500")
option_file_frame_darkhast_kargah.pack_propagate(False)
option_file_frame_darkhast_kargah.withdraw()

option_frame_asli_darkhast_kargah=tk.Frame(option_file_frame_darkhast_kargah)
option_frame_asli_darkhast_kargah.place(x=50,y=50)

bg_image = image_darkhast_kargah
bg_image = image_darkhast_kargah.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_darkhast_kargah, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


sal_sakht_darkhast_kargah_lable=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="سال ساخت")
sal_sakht_darkhast_kargah_lable.place(x=302, y=50)

sal_sakht_darkhast_kargah_entry=tk.Entry(option_file_frame_darkhast_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_darkhast_kargah_entry.place(x=108, y=50)

vaziat_bagh_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="وضعیت برق")
vaziat_bagh_darkhast_kargah.place(x=295, y=80)

vaziat_bargh_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah)
vaziat_bargh_darkhast_kargah_combo["values"]=("","برق شهری","سه فاز","تک فاز")
vaziat_bargh_darkhast_kargah_combo.set("")
vaziat_bargh_darkhast_kargah_combo["state"]=["readonly"]
vaziat_bargh_darkhast_kargah_combo.place(x=70, y=80)

garmayesh_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_darkhast_kargah.place(x=295, y=110)

garmayesh_type_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah)
garmayesh_type_darkhast_kargah_combo["values"]=("","بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_darkhast_kargah_combo.set("")
garmayesh_type_darkhast_kargah_combo["state"]=["readonly"]
garmayesh_type_darkhast_kargah_combo.place(x=70, y=110)


sarmayesh_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_darkhast_kargah.place(x=295, y=140)

sarmayesh_kooler_gazi_darkhast_kargah_var=tk.IntVar(value=0)
sarmayesh_fan_darkhast_kargah_var=tk.IntVar(value=0)
sarmayesh_panke_darkhast_kargah_var=tk.IntVar(value=0)
sarmayesh_kooler_abi_darkhast_kargah_var=tk.IntVar(value=0)

sarmayesh_fan_darkhast_kargah=tk.Checkbutton(option_file_frame_darkhast_kargah,text="تهویه(فن)",variable=sarmayesh_fan_darkhast_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_darkhast_kargah.place(x=295, y=170)

sarmayesh_panke_darkhast_kargah=tk.Checkbutton(option_file_frame_darkhast_kargah,text="پنکه سقفی",variable=sarmayesh_panke_darkhast_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_darkhast_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_darkhast_kargah=tk.Checkbutton(option_file_frame_darkhast_kargah,text="کولر آبی",variable=sarmayesh_kooler_abi_darkhast_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_darkhast_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_darkhast_kargah=tk.Checkbutton(option_file_frame_darkhast_kargah,text="کولر گازی",variable=sarmayesh_kooler_gazi_darkhast_kargah_var,background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_darkhast_kargah.place(x=84, y=200)

vaziat_ab_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",width=13,text=" وضعیت آب",font=("Shabnam", 9))
vaziat_ab_darkhast_kargah.place(x=303, y=230)

vaziat_ab_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah,width=35)
vaziat_ab_darkhast_kargah_combo["values"]=(""," آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_darkhast_kargah_combo.set("")
vaziat_ab_darkhast_kargah_combo["state"]=["readonly"]
vaziat_ab_darkhast_kargah_combo.place(x=30, y=230)

abzar_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_darkhast_kargah.place(x=298, y=260)

abzaar_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah,width=23)
abzaar_darkhast_kargah_combo["values"]=("","(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzaar_darkhast_kargah_combo.set("")
abzaar_darkhast_kargah_combo["state"]=["readonly"]
abzaar_darkhast_kargah_combo.place(x=58, y=260)

toilet_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_darkhast_kargah.place(x=298, y=290)

toilet_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah)
toilet_darkhast_kargah_combo["values"]=("","دارد","ندارد")
toilet_darkhast_kargah_combo.set("")
toilet_darkhast_kargah_combo["state"]=["readonly"]
toilet_darkhast_kargah_combo.place(x=70, y=290)

hamam_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_darkhast_kargah.place(x=303, y=320)

hamam_darkhast_kargah__combo=ttk.Combobox(option_file_frame_darkhast_kargah)
hamam_darkhast_kargah__combo["values"]=("","ندارد","دارد")
hamam_darkhast_kargah__combo.set("")
hamam_darkhast_kargah__combo["state"]=["readonly"]
hamam_darkhast_kargah__combo.place(x=70, y=320)

otagh_darkhast_kargah=tk.Label(option_file_frame_darkhast_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_darkhast_kargah.place(x=294, y=350)

otagh_darkhast_kargah_combo=ttk.Combobox(option_file_frame_darkhast_kargah)
otagh_darkhast_kargah_combo["values"]=("","ندارد","دارد")
otagh_darkhast_kargah_combo.set("")
otagh_darkhast_kargah_combo["state"]=["readonly"]
otagh_darkhast_kargah_combo.place(x=70, y=350)

zakhire_options_darkhast_kargah=tk.Button(option_file_frame_darkhast_kargah,command=save_option_darkhast_kargah,text="تایید",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_darkhast_kargah.place(x=50,y=450)

back_to_darkhast_kargah=tk.Button(option_file_frame_darkhast_kargah,text="بازگشت",command=back_to_darkhast_kargah,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_darkhast_kargah.place(x=170,y=450)

option_file_frame_darkhast_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_darkhast_kargah.resizable(False, False)
#endregion
#=============================== پنجره گزارشات ===============================
#--------------------------پنجره گزارش های مسکونی------------------------------
#region
gozaresh_maskoni = tk.Toplevel(root)
gozaresh_maskoni.title("گزارش مسکونی")
gozaresh_maskoni.geometry("600x380")
gozaresh_maskoni.withdraw()

bg_image = image_gozaresh_maskoni
bg_image = image_gozaresh_maskoni.resize((600, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(gozaresh_maskoni, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_gozaresh_maskoni= tk.Frame(gozaresh_maskoni,bd=0,highlightthickness=0)
frame_gozaresh_maskoni.pack(side="left", fill="y", padx=6, pady=15)

title_lbl_gozaresh_maskoni = tk.Label(gozaresh_maskoni,text="گزارش مسکونی",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl_gozaresh_maskoni.place(x=40, y=25)

noe_gozaresh_maskoni=tk.Label(gozaresh_maskoni,text=" نوع گزارش ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
noe_gozaresh_maskoni.place(x=470, y=76)

error_label_maskoni=tk.Label(gozaresh_maskoni,text='',font=("Shabnam",10),fg="#E91414",bg="#FFFFFF")
error_label_maskoni.place(x=190,y=230,width=260,height=25)

gozaresh_file_combo_maskoni=ttk.Combobox(gozaresh_maskoni)
gozaresh_file_combo_maskoni["values"] = ("گزارش فایل اجاره","گزارش فایل فروش","گزارش فایل درخواست اجاره","گزارش فایل درخواست خرید")
gozaresh_file_combo_maskoni["state"]=["readonly"]
gozaresh_file_combo_maskoni.config(width=40)
gozaresh_file_combo_maskoni.configure(justify="center")
gozaresh_file_combo_maskoni.place(x=190, y=80)

save_gozaresh_maskoni = tk.Button(gozaresh_maskoni, text="تایید", command=excel_gozaresh_maskoni, bg="#00BFFF", fg="#000000", width=10, height=1)
save_gozaresh_maskoni.place(x=95, y=320)

back_to_home_gozaresh_maskoni = tk.Button(gozaresh_maskoni, text="بازگشت", command=back_home_gozaresh_maskoni, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_home_gozaresh_maskoni.place(x=215, y=320)

gozaresh_maskoni.protocol("WM_DELETE_WINDOW", lambda: None)
gozaresh_maskoni.resizable(False, False)
#endregion
#------------------------------پنجره گزارش اداری/تجاری------------------------------
#region
gozaresh_edari_tejari = tk.Toplevel(root)
gozaresh_edari_tejari.title("گزارش اداری / تجاری")
gozaresh_edari_tejari.geometry("600x380")
gozaresh_edari_tejari.withdraw()

bg_image = image_gozaresh_edari_tejari
bg_image = image_gozaresh_edari_tejari.resize((600, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(gozaresh_edari_tejari, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_gozaresh_edari_tejari= tk.Frame(gozaresh_edari_tejari,bd=0,highlightthickness=0)
frame_gozaresh_edari_tejari.pack(side="left", fill="y", padx=6, pady=15)

title_lbl_gozaresh_edari_tejari = tk.Label(gozaresh_edari_tejari,text="گزارش اداری/تجاری",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl_gozaresh_edari_tejari.place(x=40, y=25)

noe_gozaresh_edari_tejari=tk.Label(gozaresh_edari_tejari,text=" نوع گزارش ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
noe_gozaresh_edari_tejari.place(x=470, y=76)

error_label_edari_tejari=tk.Label(gozaresh_edari_tejari,text='',font=("Shabnam",10),fg="#E91414",bg="#FFFFFF")
error_label_edari_tejari.place(x=190,y=230,width=260,height=25)

gozaresh_file_combo_edari_tejari=ttk.Combobox(gozaresh_edari_tejari)
gozaresh_file_combo_edari_tejari["values"] = ("گزارش فایل اجاره","گزارش فایل فروش","گزارش فایل درخواست اجاره","گزارش فایل درخواست خرید")
gozaresh_file_combo_edari_tejari["state"]=["readonly"]
gozaresh_file_combo_edari_tejari.config(width=40)
gozaresh_file_combo_edari_tejari.configure(justify="center")
gozaresh_file_combo_edari_tejari.place(x=190, y=80)

save_gozaresh_edari_tejari = tk.Button(gozaresh_edari_tejari,text="تایید", command=excel_gozaresh_edari_tejari, bg="#00BFFF", fg="#000000", width=10, height=1)
save_gozaresh_edari_tejari.place(x=95, y=320)

back_to_home_gozaresh_edari_tejari = tk.Button(gozaresh_edari_tejari, text="بازگشت", command=back_home_gozaresh_edari_tejari, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_home_gozaresh_edari_tejari.place(x=215, y=320)

gozaresh_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
gozaresh_edari_tejari.resizable(False, False)
#endregion
#---------------------------------پنجره گزارش های باغ/زمین-------------------------
#region
gozaresh_bagh_zamin = tk.Toplevel(root)
gozaresh_bagh_zamin.title("گزارش باغ/زمین")
gozaresh_bagh_zamin.geometry("600x380")
gozaresh_bagh_zamin.withdraw()

bg_image = image_gozaresh_bagh_zamin
bg_image = image_gozaresh_bagh_zamin.resize((600, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(gozaresh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_gozaresh_bagh_zamin= tk.Frame(gozaresh_bagh_zamin,bd=0,highlightthickness=0)
frame_gozaresh_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl_gozaresh_bagh_zamin = tk.Label(gozaresh_bagh_zamin,text="گزارش باغ/زمین",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl_gozaresh_bagh_zamin.place(x=40, y=25)

noe_gozaresh_bagh_zamin=tk.Label(gozaresh_bagh_zamin,text=" نوع گزارش ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
noe_gozaresh_bagh_zamin.place(x=470, y=76)

error_label_bagh_zamin=tk.Label(gozaresh_bagh_zamin,text='',font=("Shabnam",10),fg="#E91414",bg="#FFFFFF")
error_label_bagh_zamin.place(x=60,y=230,width=390,height=25)

gozaresh_file_combo_bagh_zamin=ttk.Combobox(gozaresh_bagh_zamin)
gozaresh_file_combo_bagh_zamin["values"] = ("گزارش فایل اجاره باغ","گزارش فایل فروش باغ","گزارش فایل درخواست اجاره باغ","گزارش فایل درخواست خرید باغ",
                                            "گزارش فایل اجاره زمین","گزارش فایل فروش زمین","گزارش فایل درخواست اجاره زمین","گزارش فایل درخواست خرید زمین")
gozaresh_file_combo_bagh_zamin["state"]=["readonly"]
gozaresh_file_combo_bagh_zamin.config(width=60)
gozaresh_file_combo_bagh_zamin.configure(justify="center")
gozaresh_file_combo_bagh_zamin.place(x=60 ,y=80)

save_gozaresh_bagh_zamin = tk.Button(gozaresh_bagh_zamin, text="تایید", command=excel_gozaresh_bagh_zamin, bg="#00BFFF", fg="#000000", width=10, height=1)
save_gozaresh_bagh_zamin.place(x=95, y=320)

back_to_home_gozaresh_bagh_zamin = tk.Button(gozaresh_bagh_zamin, text="بازگشت", command=back_home_gozaresh_bagh_zamin, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_home_gozaresh_bagh_zamin.place(x=215, y=320)

gozaresh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
gozaresh_bagh_zamin.resizable(False, False)
#endregion
#---------------------------------پنجره گزارش های کارگاه---------------------------
#region
gozaresh_kargah = tk.Toplevel(root)
gozaresh_kargah.title("گزارش  کارگاه")
gozaresh_kargah.geometry("600x380")
gozaresh_kargah.withdraw()

bg_image = image_gozaresh_kargah
bg_image = image_gozaresh_kargah.resize((600, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(gozaresh_kargah, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_gozaresh_kargah= tk.Frame(gozaresh_kargah,bd=0,highlightthickness=0)
frame_gozaresh_kargah.pack(side="left", fill="y", padx=6, pady=15)

title_lbl_gozaresh_kargah = tk.Label(gozaresh_kargah,text="گزارش کارگاه",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl_gozaresh_kargah.place(x=40, y=25)

type_gozaresh_kargah=tk.Label(gozaresh_kargah,text=" نوع گزارش ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
type_gozaresh_kargah.place(x=470, y=76)

error_label_kargah=tk.Label(gozaresh_kargah,text='',font=("Shabnam",10),fg="#E91414",bg="#FFFFFF")
error_label_kargah.place(x=190,y=230,width=260,height=25)

gozaresh_file_combo_kargah=ttk.Combobox(gozaresh_kargah)
gozaresh_file_combo_kargah["values"] = ("گزارش فایل اجاره","گزارش فایل فروش","گزارش فایل درخواست اجاره","گزارش فایل درخواست خرید")
gozaresh_file_combo_kargah["state"]=["readonly"]
gozaresh_file_combo_kargah.config(width=40)
gozaresh_file_combo_kargah.configure(justify="center")
gozaresh_file_combo_kargah.place(x=190, y=80)

save_gozaresh_edari_kargah = tk.Button(gozaresh_kargah, text="تایید", command=excel_gozaresh_kargah, bg="#00BFFF", fg="#000000", width=10, height=1)
save_gozaresh_edari_kargah.place(x=95, y=320)

back_to_home_gozaresh_kargah = tk.Button(gozaresh_kargah, text="بازگشت", command=back_home_gozaresh_kargah, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_home_gozaresh_kargah.place(x=215, y=320)

gozaresh_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
gozaresh_kargah.resizable(False, False)

#endregion
#-------------------------------------پنجره قرارداد ------------------------------
#region
gharardad_window = tk.Toplevel(root)
gharardad_window.title("قراردادها")
gharardad_window.geometry("600x770")
gharardad_window.configure(bg="#052340")
gharardad_window.withdraw()


titr_window=tk.Label(gharardad_window,text="قراردادها",fg="#00BFFF",bg="#052340",font=("Shabnam",15))
titr_window.place(x=250,y=10)

titr_aval_page=tk.Label(gharardad_window,text="در این بخش میتوانید فایل قرارداد مورد نظر خود را ایجاد و دریافت کنید",fg="#FFFFFF",bg="#052340",font=("Shabnam",8))
titr_aval_page.place(x=130,y=40)

main_frame=tk.Frame(gharardad_window,highlightbackground="#00BFFF",
highlightthickness=1,width=520,height=570)
main_frame.configure(bg="#052340")
main_frame.place(x=40,y=62)

text_label1=tk.Label(main_frame,text="ایجاد قراردادها",font=("Shabnam",11),bg="#052340",fg="#00BFFF",bd=1)
text_label1.place(x=240,y=20)

khat_up_1=tk.Frame(main_frame, bg="#3A6EA5",height=1)
khat_up_1.place(x=40,y=30,width=130)

khat_up_2=tk.Frame(main_frame, bg="#3A6EA5",height=1)
khat_up_2.place(x=340,y=30,width=130)

ghararadad_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_gharardad)
ghararadad_image.place(x=180,y=6)

melk_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_melk)
melk_image.place(x=440,y=60)

type_gharardad_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_type_gharardad)
type_gharardad_image.place(x=440,y=160)

shakhs_aval_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_person)
shakhs_aval_image.place(x=440,y=230)

shakhs_dovom_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_gharardad)
shakhs_dovom_image.place(x=440,y=320)

tozihat_image=tk.Label(main_frame,bg="#052340",fg="#00BFFF",image=image_massage)
tozihat_image.place(x=440,y=410)

type_melk_gharardad=tk.Label(main_frame,text="نوع ملک",bg="#052340",fg="#FFFFFF",font=("Shabnam",8))
type_melk_gharardad.place(x=350,y=80)
type_melk_gharardad_combo=ttk.Combobox(main_frame)
type_melk_gharardad_combo["values"]=("مسکونی","اداری_تجاری","باغ","زمین","کارگاه")
type_melk_gharardad_combo["state"]=["readonly"]
type_melk_gharardad_combo.config(width=40)
type_melk_gharardad_combo.configure(justify="center")
type_melk_gharardad_combo.set("")
type_melk_gharardad_combo.place(x=25,y=80)

type_gharardad=tk.Label(main_frame,text="نوع قرارداد",bg="#052340",fg="#FFFFFF",font=("Shabnam",8))
type_gharardad.place(x=350,y=165)
type_gharardad_combo=ttk.Combobox(main_frame)
type_gharardad_combo["values"]=("خرید و فروش ","اجاره","مشارکت")
type_gharardad_combo["state"]=["readonly"]
type_gharardad_combo.config(width=40)
type_gharardad_combo.configure(justify="center")
type_gharardad_combo.set("")
type_gharardad_combo.place(x=25,y=165)


name_shakhs_aval_gharardad=tk.Label(main_frame,text="نام طرف اول قرارداد",bg="#052340",fg="#FFFFFF",font=("Shabnam",8))
name_shakhs_aval_gharardad.place(x=300,y=250)
name_shakhs_aval_gharardad_entry=tk.Entry(main_frame,bg="#ffffff",font=("Shabnam",10),fg='black')
name_shakhs_aval_gharardad_entry.place(x=25,y=250,width=260)

name_shakhs_dovom_gharardad=tk.Label(main_frame,text="نام طرف دوم قرارداد",bg="#052340",fg="#FFFFFF",font=("Shabnam",8))
name_shakhs_dovom_gharardad.place(x=296,y=340)
name_shakhs_dovom_gharardad_entry=tk.Entry(main_frame,bg="#ffffff",font=("Shabnam",10),fg='black')
name_shakhs_dovom_gharardad_entry.place(x=25,y=340,width=260)

tozih_gharardad=tk.Label(main_frame,text="توضیحات(اختیاری)",bg="#052340",fg="#FFFFFF",font=("Shabnam",8))
tozih_gharardad.place(x=310,y=430)
tozih_gharardad_entry=tk.Text(main_frame,bg="#ffffff",font=("Shabnam",10),fg='black')
tozih_gharardad_entry.place(x=25,y=425,width=260,height=45)

khat_vasat=tk.Frame(main_frame, bg="#3A6EA5",height=1)
khat_vasat.place(x=25,y=490,width=480)

word_btn=tk.Button(main_frame,bg="#0096D6",text="دریافت فایل ورد قرارداد",fg="#ffffff",image=image_word,compound="left",command=creat_word_gharardad)
word_btn.place(x=140,y=497,width=200)
label_titr_vasat1 = tk.Label(main_frame,text="با کلیک بر دکمه بالا، فایل قرارداد مورد نظر در قالب",fg="white",bg="#052340",font=("Shabnam", 8))
label_titr_vasat1.place(x=230, y=547)

label_titr_vasat2 = tk.Label(main_frame,text="Word",fg="#00B7EB",bg="#052340",font=("Shabnam", 8, "bold"))
label_titr_vasat2.place(x=200, y=547)

label_titr_vasat3= tk.Label(main_frame,text="در دسکتاپ ذخیره میشود",fg="white",bg="#052340",font=("Shabnam", 8))
label_titr_vasat3.place(x=80, y=547)

seconde_frame=tk.Frame(gharardad_window,highlightbackground="#00BFFF",
highlightthickness=1,width=520,height=80)
seconde_frame.configure(bg="#052340")
seconde_frame.place(x=40,y=640)

label_titr_rahgiri= tk.Label(seconde_frame,text="اخرین کد رهگیری تولید شده",fg="#ffffff",bg="#052340",font=("Shabnam", 8))
label_titr_rahgiri.place(x=195, y=2)
code_frame=tk.Frame(seconde_frame,highlightbackground="#00BFFF",highlightthickness=1,width=200,height=35)
code_frame.configure(bg="#052340")
code_frame.place(x=160,y=24)

code_label= tk.Label(code_frame,text=" ",fg="#ffffff",bg="#052340",font=("Shabnam", 8))
code_label.place(x=160,y=24)


label_titr_akhar= tk.Label(seconde_frame,text="این کد برای پیگیری قرارداد در بخش گزارش استفاده میشود",fg="#ffffff",bg="#052340",font=("Shabnam", 7))
label_titr_akhar.place(x=167, y=60)


back_to_main=tk.Button(gharardad_window,text="بازگشت",fg="#ffffff",bg="#052340",command=back_main_ghararadad)
back_to_main.place(x=230,y=730,width=140)
#endregion
#############################################################################
# ----------------------اجرای برنامه-------------------
#region
root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()
#endregion