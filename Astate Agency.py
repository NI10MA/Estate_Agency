#-------------------------------------  کتابخانه ها-----------------
#region
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox,font,scrolledtext
import subprocess
import os
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
#------------توابع اصلی ذخیره----------------------
#region
def save_rehn_maskkoni():#ذخیره پنجره اجاره مسکونی
    pass
def save_forosh_maskkoni():#ذخیره پنجره فروش مسکونی
    pass
def save_rehn_edari():#ذخیره پنجره اجاره اداری
    pass
def save_forosh_edari():#ذخیره پنجره فروش اداری
    pass
def save_rehn_bagh():#ذخیره پنجره اجاره زمین و باغ
    pass
def save_forosh_bagh():# ذخیره پنجره فروش باغ و زمین 
    pass
def save_ejareh_karghah():# ذخیره پنجره اجاره کارگاه 
    pass
def save_forosh_karghah():# ذخیره پنجره فروش کارگاه 
    pass
def save_kharid_karghah():# ذخیره پنجره خرید کارگاه
    pass
#endregion
#========================================================
# ------------پنجره اصلی-------------------------------
#region
root = tk.Tk()
root.title("Astate Agency")
root.geometry("1100x700")
#تصاویر پروژه
plus=tk.PhotoImage(file="pluse.png")
elvator_pic=tk.PhotoImage(file="elvator.png")
parking_pic=tk.PhotoImage(file="parking.png")
warehouse_pic=tk.PhotoImage(file="anbari.png")
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
menu_frame.pack(padx=2, pady=2, fill="both", expand=True)
#endregion
# ------------- لیست کشویی فیلد فایل های ثبتی-----------
#region
def kharid():
    box_kharid.deiconify()
    box_kharid.grab_set()

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
    option_file_frame_kharid_maskoni.deiconify()
    option_file_frame_kharid_maskoni.grab_set()

def open_option10():
    option_file_frame_kharid_edari_tejari.deiconify()
    option_file_frame_kharid_edari_tejari.grab_set()

def open_option11():
    option_file_frame_kharid_bagh_zamin.deiconify()
    option_file_frame_kharid_bagh_zamin.grab_set()

def open_option12():
    option_file_frame_kharid_kargah.deiconify()
    option_file_frame_kharid_kargah.grab_set()

#endregion
#=======================================================
#-----------توابع برگشت صفحات ثبتی به فرم اصلی----------
#-----برگشت از صفحه اجاره مسکونی-------------------------
#region
def back_home_ejare_maskoni():
    root.deiconify()
    ejareh_rehn_page.withdraw()
    #خالی کردن  باکس های اجاره مسکونی
    sal_sakht_ejareh_maskoni_entry.delete(0,tk.END)
    addrres_ejare_maskoni_entry.delete(0,tk.END)
    tabaghe_ejare_maskoni_entry.delete(0,tk.END)
    vahed_ejare_maskoni_entry.delete(0,tk.END)
    otagh_ejare_maskoni_entry.delete(0,tk.END)
    gheimat_ejare_ejare_maskoni_entry.delete(0,tk.END)
    gheimat_pish_ejare_maskoni_entry.delete(0,tk.END)
    #پنجره امکانات
    sarmaesh_ejare_maskoni_combo.set("")
    garmaesh_ejare_maskoni_combo.set("")
    kaf_ejare_maskoni_combo.set("")
    toilet_ejare_maskoni_combo.set("")
    delete_root()
#endregion
#-----برگشت از صفحه فروش مسکونی-------------------------
#region
def back_home_forosh_maskoni():
    root.deiconify()
    forosh_rehn_page.withdraw()
    sal_sakht_forosh_maskoni_entry.delete(0,tk.END)
    addrres_forosh_maskoni_entry.delete(0,tk.END)
    tabaghe_forosh_maskoni_entry.delete(0,tk.END)
    vahed_forosh_maskoni_entry.delete(0,tk.END)
    otagh_forosh_maskoni_entry.delete(0,tk.END)
    gheimat_forosh_maskoni_entry.delete(0,tk.END)
    #پنجره امکانات
    sarmaesh_combo_forosh_maskoni.set("")
    garmaesh_combo_forosh_maskoni.set("")
    kaf_combo_forosh_maskoni.set("")
    toilet_combo_forosh_maskoni.set("")
    delete_root()
#endregion
#------------------------برگشت از صفحه اجاره اداری/تجاری---------------------
#region
def back_home_ejareh_edari_tejari():
    root.deiconify()
    ejareh_edari_tejari.withdraw()
    sal_sakht_ejareh_edari_tejari_entry.delete(0,tk.END)
    addrres_ejareh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_ejareh_edari_tejari_entry.delete(0,tk.END)
    vahed_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_ejareh_edari_tejari_entry.delete(0,tk.END) 
    #پنجره امکانات
    ab_va_gaz_combo_emkanat_ejareh_edari_tejari.set("")
    sarmayesh_combo_emkanat_ejareh_edari_tejari.set("")
    garmayesh_combo_emkanat_ejareh_edari_tejari.set("")
    delete_root()
#endregion
#---------------------------برگشت از صفحه فروش اداری/تجاری--------------------
def back_home_forosh_edari_tejari():
    root.deiconify()
    forosh_edari_tejari.withdraw()
    sal_sakht_forosh_edari_tejari_entry.delete(0,tk.END)
    addrres_forosh_edari_tejari_entry.delete(0,tk.END)
    tabaghe_forosh_edari_tejari_entry.delete(0,tk.END)
    vahed_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_forosh_edari_tejari_entry.delete(0,tk.END)
    #پنجره امکانات
    aab_va_gaz_combo_emkanat_forosh_edari_tejari.set("")
    sarmayesh_combo_emkanat_forosh_edari_tejari.set("")
    garmayesh_combo_emkanat_forosh_edari_tejari.set("")
    delete_root()
#---------------------------برگشت از صفحه خرید اداری/تجاری--------------------
def back_home_kharid_edari_tejari():
    root.deiconify()
    kharid_edari_tejari.withdraw()
    sal_sakht_kharid_edari_tejari_entry.delete(0,tk.END)
    addrres_kharid_edari_tejari_entry.delete(0,tk.END)
    tabaghe_kharid_edari_tejari_entry.delete(0,tk.END)
    vahed_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_pish_kharid_edari_tejari_entry.delete(0,tk.END)
    #پنجره امکانات
    aab_va_gaz_combo_emkanat_kharid_edari_tejari.set("")
    sarmayesh_combo_emkanat_kharid_edari_tejari.set("")
    garmayesh_combo_emkanat_kharid_edari_tejari.set("")
    delete_root()
#----------------------------برگشت از صفحه اجاره باغ / زمین------------------
def back_home_ejareh_bagh():
    ejareh_bagh_zamin.withdraw()
    root.deiconify()
    metraj_zamin_ejareh_bagh_zamin_entry.delete(0,tk.END)
    mablagh_ejare_ejareh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_ejareh_edari_tejari_entry.delete(0,tk.END)
    # امکانات فروش باغ و زمین
    type_vila_ejareh_bagh_zamin_combo.set("")
    option_ejareh_bagh_zamin_combo.set("")
    karbari_zamin_combo.set("")
    tree_count_entry.delete(0,tk.END)
    metraj_tree_entry.delete(0,tk.END)
    abyari_combo.set("")
    type_tree_combo.set("")
    metraj_vila_bagh_entry.delete(0,tk.END)
    sal_sakht_vila_bagh_entry.delete(0,tk.END)
    type_vila_ejareh_bagh_zamin_combo.set("")
    toilet_bagh_combo.set("")
    hamam_bagh_combo.set("")
    sanad_bagh_combo.set("")
    #تغییر کاربری
    metraj_zamin_ejareh_bagh_zamin_entry2.delete(0,tk.END)
    karbari_ejareh_ejareh_bagh_zamin_combo.set("")
    khak_ejareh_ejareh_bagh_zamin_combo.set("")
    ab_ejareh_ejareh_bagh_zamin_combo.set("")
    zamin_shekl_ejareh_bagh_zamin_combo.set("")
    kesht_ejareh_bagh_zamin_combo.set("")
    kesht_ejareh_bagh_zamin_entry.delete(0,tk.END)
#-----------------------------برگشت از صفحه فروش باغ / زمین------------------
def back_home_forosh_bagh():
    forosh_bagh_zamin.withdraw()
    root.deiconify()    
    metraj_zamin_forosh_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_forosh_bagh_zamin_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_forosh_edari_tejari_entry.delete(0,tk.END)
    metraj_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    # امکانات فروش باغ و زمین
    karbary_zamin_forosh_bagh_zamin_combo.set("")
    metraj_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_forosh_bagh_zamin_entry.delete(0,tk.END)
    abyari_forosh_bagh_zamin_combo.set("")
    type_tree_forosh_bagh_zamin_combo.set("")
    metraj_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_forosh_bagh_zamin_entry.delete(0,tk.END)
    type_vila_forosh_bagh_zamin_combo.set("")
    toilet_forosh_bagh_zamin_combo.set("")
    hamam_forosh_bagh_zamin_combo.set("")
    sanad_forosh_bagh_zamin_combo.set("")
    option_forosh_bagh_zamin_combo.set("")
    #تغییر کاربری
    metraj_zamin2_forosh_bagh_zamin_entry.delete(0,tk.END)
    karbari_forosh_bagh_zamin_combo.set("")
    khak_forosh_bagh_zamin_combo.set("")
    ab_forosh_bagh_zamin_combo.set("")
    zamin_shekl_forosh_bagh_zamin_combo.set("")
    kesht_forosh_bagh_zamin_combo.set("")
    delete_root()
#=========================================================
#----------------------- برگشت از صفحه اجاره کارگاه--------------------
def back_home_ejareh_karghah():
    ejareh_karghah.withdraw()
    root.deiconify()
    metraj_kargah_entry.delete(0,tk.END)
    loctaion_ejareh_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_ejareh_kargah_entry.delete(0,tk.END)
    mablagh_pish_ejareh_kargah_entry.delete(0,tk.END) 
    #پنجره امکانات
    sal_sakht_ejareh_kargah_entry.delete(0,tk.END)
    vaziat_bargh_ejareh_kargah_combo.set("")
    garmayesh_type_ejareh_kargah_combo.set("")
    vaziat_ab_ejareh_kargah_combo.set("")
    abzaar_ejareh_kargah_combo.set("")
    toilet_ejareh_kargah_combo.set("")
    hamam_ejareh_kargah__combo.set("")
    otagh_ejareh_kargah_combo.set("")
    delete_root()
#----------------------- برگشت از صفحه فروش کارگاه--------------------
def back_home_forosh_karghah():
    forosh_karghah.withdraw()
    root.deiconify()
    metraj_kargah_entry.delete(0,tk.END)
    loctaion_forosh_kargah_entry.delete(0,tk.END)
    mablagh_pish_forosh_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_forosh_kargah_entry.delete(0,tk.END) 
    #پنجره امکانات
    sal_sakht_forosh_kargah_entry.delete(0,tk.END)
    vaziat_bargh_forosh_kargah_combo.set("")
    garmayesh_type_forosh_kargah_combo.set("")
    vaziat_ab_forosh_kargah_combo.set("")
    abzarforosh_kargah_combo.set("")
    toilet_forosh_kargah_combo.set("")
    hamam_forosh_kargah_combo.set("")
    otagh_forosh_kargah_combo.set("")
    delete_root()
#----------------------------برگشت از صفحه اجاره کارگاه------------------
def back_to_ejareh_karghah():
    option_file_frame_ejareh_kargah.withdraw()
    ejareh_karghah.deiconify()
#-----------------------------برگشت از صفحه خرید باغ / زمین------------------
def back_home_kharid_bagh():
    kharid_bagh_zamin.withdraw()
    root.deiconify()    
    metraj_zamin_kharid_bagh_zamin_entry.delete(0,tk.END)
    bagh_loctaion_kharid_bagh_zamin_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    mablagh_ejare_kharid_edari_tejari_entry.delete(0,tk.END)
    metraj_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    metraj_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    # امکانات فروش باغ و زمین
    karbary_zamin_kharid_bagh_zamin_combo.set("")
    metraj_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    tedad_derakht_kharid_bagh_zamin_entry.delete(0,tk.END)
    abyari_kharid_bagh_zamin_combo.set("")
    type_tree_kharid_bagh_zamin_combo.set("")
    metraj_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    sal_sakht_vila_kharid_bagh_zamin_entry.delete(0,tk.END)
    type_vila_kharid_bagh_zamin_combo.set("")
    toilet_kharid_bagh_zamin_combo.set("")
    hamam_kharid_bagh_zamin_combo.set("")
    sanad_kharid_bagh_zamin_combo.set("")
    option_kharid_bagh_zamin_combo.set("")
    #تغییر کاربری
    metraj_zamin2_kharid_bagh_zamin_entry.delete(0,tk.END)
    karbari_kharid_bagh_zamin_combo.set("")
    khak_kharid_bagh_zamin_combo.set("")
    ab_kharid_bagh_zamin_combo.set("")
    zamin_shekl_kharid_bagh_zamin_combo.set("")
    kesht_kharid_bagh_zamin_combo.set("")
    delete_root()
#-----------------------------برگشت از صفحه خرید کارگاه--------------------
def back_home_kharid_kargah():
    kharid_kargah.withdraw()   
    root.deiconify()
    metraj_kharid_kargah_entry.delete(0,tk.END)
    loctaion_kharid_kargah_entry.delete(0,tk.END)
    gheimat_har_metr_kharid_kargah_entry.delete(0,tk.END)
    mablagh_pish_kharid_kargah_entry.delete(0,tk.END)
    #پنجره امکانات
    sal_sakht_kharid_kargah_entry.delete(0,tk.END)
    vaziat_bargh_kharid_kargah_combo.set("")
    garmayesh_type_kharid_kargah_combo.set("")
    vaziat_ab_kharid_kargah_combo.set("")
    abzaar_kharid_kargah_combo.set("")
    toilet_kharid_kargah_combo.set("")
    hamam_kharid_kargah__combo.set("")
    otagh_kharid_kargah_combo.set("")
    delete_root()
#----------------------------برگشت از صفحه خرید مسکونی-------------------
def back_home_kharid_maskoni():
    root.deiconify()
    kharid_maskoni_page.withdraw()
    sal_sakht_kharid_maskoni_entry.delete(0,tk.END)
    addrres_kharid_maskoni_entry.delete(0,tk.END)
    tabaghe_kharid_maskoni_entry.delete(0,tk.END)
    vahed_kharid_maskoni_entry.delete(0,tk.END)
    otagh_kharid_maskoni_entry.delete(0,tk.END)
    gheimat_kharid_maskoni_entry.delete(0,tk.END)
    #پنجره امکانات
    sarmaesh_combo_kharid_maskoni.set("")
    garmaesh_combo_kharid_maskoni.set("")
    kaf_combo_kharid_maskoni.set("")
    toilet_combo_kharid_maskoni.set("")
    delete_root()
#=========================================================
#--------برگشت از امکانات فایل ها به صفحه اصلی ثبتی-------
#-------برگشت اجاره مسکونی------------------
def back_to_ejareh_maskoni_page():
    option_file_frame_ejareh_maskoni.withdraw()
    option_file_frame_ejareh_maskoni.grab_release()
#-------برگشت فروش مسکونی------------------    
def back_to_forosh_maskoni_page():
    option_file_frame_forosh_maskoni.withdraw()
    option_file_frame_forosh_maskoni.grab_release()
#--------برگشت اجاره اداری/تجاری----------------- 
def back_to_ejareh_edari_tejari():
    option_file_frame_ejareh_edari_tajari.withdraw()
    option_file_frame_ejareh_edari_tajari.grab_release()
#--------برگشت فروش اداری/تجاری----------------- 
def back_to_forosh_edari_tejari():
    option_file_frame_forosh_edari_tejari.withdraw()
    option_file_frame_forosh_edari_tejari.grab_release()
#-------برگشت اجاره باغ و زمین------------------
def back_to_ejareh_bagh_zamin():
    option_file_frame_ejareh_bagh_zamin.withdraw()
    option_file_frame_ejareh_bagh_zamin.grab_release()
#--------------------برگشت فروش باغ و زمین------------------------------------------------
def  back_to_forosh_bagh_zamin():
     option_file_frame_forosh_bagh_zamin.withdraw()
     option_file_frame_forosh_bagh_zamin.grab_release()
#--------------------برگشت اجاره کارگاه------------------------------------------------
def  back_to_ejareh_karghah():
     option_file_frame_ejareh_kargah.withdraw()
     option_file_frame_ejareh_kargah.grab_release()
#--------------------برگشت فروش کارگاه------------------------------------------------
def  back_to_forosh_karghah():
     option_file_frame_forosh_kargah.withdraw()
     option_file_frame_forosh_kargah.grab_release()
#-----------------------------برگشت خرید مسکونی--------------------------
def back_to_kharid_maskoni_page():
    option_file_frame_kharid_maskoni.withdraw()
    option_file_frame_kharid_maskoni.grab_release()
#--------برگشت خرید اداری/تجاری----------------- 
def back_to_kharid_edari_tejari():
    option_file_frame_kharid_edari_tejari.withdraw()
    option_file_frame_kharid_edari_tejari.grab_release()
#--------------------برگشت خرید باغ و زمین------------------------------------------------
def  back_to_kharid_bagh_zamin():
     option_file_frame_kharid_bagh_zamin.withdraw()
     option_file_frame_kharid_bagh_zamin.grab_release()
#-------------------برگشت خرید کارگاه---------------------------
def  back_to_kharid_kargah():
     option_file_frame_kharid_kargah.withdraw()
     option_file_frame_kharid_kargah.grab_release()
#----------برگشت باکس ها(نوع ملک)-------------
def back_forosh_exit():
    box_forosh.withdraw()
    box_forosh.grab_release()

def back_rehn_ejareh_exit():
    box_rehn_ejareh.withdraw()
    box_rehn_ejareh.grab_release()

def back_kharid_exit():
    box_kharid.withdraw()
    box_kharid.grab_release()

def back_mosharekat_exit():
    box_mosharekat.withdraw()
    box_mosharekat.grab_release()

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
def ejarebagh_zamin():
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
#--------بستن باکس و باز کردن صفحه خرید مسکونی--------
def kharid_maskoni_page():
    box_kharid.withdraw()
    root.withdraw()
    kharid_maskoni_page.deiconify() 
    box_kharid.grab_release()
#-----بستن باکس و باز کردن صفحه خرید اداری/تجاری-----------
def kharid_edari_tejari():
    box_kharid.withdraw()
    root.withdraw()
    kharid_edari_tejari.deiconify()
    box_kharid.grab_release()
#-----بستن باکس و باز کردن صفحه خرید باغ/زمین---------
def kharid_bagh_zamin():
    box_kharid.withdraw()
    root.withdraw()
    kharid_bagh_zamin.deiconify()
    box_kharid.grab_release()   
#------بستن باکس و باز کردن صفحه خرید کارگاه-----------
def kharid_kargah():
    box_kharid.withdraw()
    root.withdraw()
    kharid_kargah.deiconify()
    box_kharid.grab_release()   

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

#تابع رادیو باتن باز و بسته کردن صفحات خرید
def sabt_radio_kharid():
    selected = kharid_radio_value.get()

    if selected==0:
            box_kharid.withdraw()
            root.withdraw()
            kharid_maskoni_page.deiconify()
            box_kharid.grab_release()
        
    elif selected==2:
        box_kharid.withdraw()
        root.withdraw()
        kharid_edari_tejari.deiconify()
        box_kharid.grab_release()

    elif selected==4:
        box_kharid.withdraw()
        root.withdraw()
        kharid_bagh_zamin.deiconify()
        box_kharid.grab_release()

    elif selected==6:
        box_kharid.withdraw()
        root.withdraw()
        kharid_kargah.deiconify()
        box_kharid.grab_release()

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
            
#=======================================================
#---------------/جابه جایی کاربری باغ و زمین در قسمت های فروش/خرید/اجاره-------------
def change_bagh_zamin1(event):
    co=karbari_zamin_combo.get()
    if co=="باغ":
        fram_option_zamin_ejareh_bagh_zamin.place_forget()
        option_frame_options_ejareh_bagh_zamin.place(x=60,y=60)
    else:
        option_frame_options_ejareh_bagh_zamin.place_forget()
        fram_option_zamin_ejareh_bagh_zamin.place(x=60,y=60)
def change_bagh_zamin_forosh_bagh(event):
    co=karbary_zamin_forosh_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_forosh_bagh_zamin.place_forget()
        option_frame_forosh_bagh_zamin.place(x=60,y=60)#فریم باغ
    else:
        option_frame_forosh_bagh_zamin.place_forget()
        option_frame_option2_forosh_bagh_zamin.place(x=60,y=60)
def change_bagh_zamin_kharid_bagh(event):
    co=karbary_zamin_kharid_bagh_zamin_combo.get()
    if co=="باغ":
        option_frame_option2_kharid_bagh_zamin.place_forget()
        option_frame_kharid_bagh_zamin.place(x=60,y=60)
    else:
        option_frame_kharid_bagh_zamin.place_forget()
        option_frame_option2_kharid_bagh_zamin.place(x=60,y=60)
#=============================================================      
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
selected_topo1=[]
def add_topo1():
    topo=zamin_shekl_ejareh_bagh_zamin_combo.get()
    if topo and topo not in selected_topo1:
        selected_topo1.append(topo)
        label_natige_topo_add_ejareh_bagh_zamin.config(text=','.join(selected_topo1))
selected_topo2=[]
def add_topo2():
    topo2=zamin_shekl_forosh_bagh_zamin_combo.get()
    if topo2 and topo2 not in selected_topo2:
        selected_topo2.append(topo2)
        lable_natige_add_forosh_bagh_zamin.config(text=','.join(selected_topo2))
selected_topo3=[]
def add_topo3():
    topo3=zamin_shekl_kharid_bagh_zamin_combo.get()
    if topo3 and topo3 not in selected_topo3:
        selected_topo3.append(topo3)
        label_natige_topo_add_kharid_bagh_zamin.config(text=','.join(selected_topo3))
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
    if var0.get()==1:
        metraj_vila_forosh_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_forosh_bagh_zamin_entry.config(state="normal")
        type_vila_forosh_bagh_zamin_combo.config(state="readonly")
        toilet_forosh_bagh_zamin_combo.config(state="readonly")
        hamam_forosh_bagh_zamin_combo.config(state="readonly")
        sanad_forosh_bagh_zamin_combo.config(state="readonly")
        option_forosh_bagh_zamin_combo.config(state="readonly")
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
def choos_kesht(event):
    a=kesht_ejareh_bagh_zamin_combo.get()
    if a=="بدون کشت":
        kesht_ejareh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_ejareh_bagh_zamin_entry.config(state="normal")
def choos_kesht2(event):
    b=kesht_forosh_bagh_zamin_combo.get()
    if b=="بدون کشت":
        kesht_forosh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_forosh_bagh_zamin_entry.config(state="normal")
def choos_kesht3(event):
    c=kesht_kharid_bagh_zamin_combo.get()
    if c=="بدون کشت":
        kesht_kharid_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_kharid_bagh_zamin_entry.config(state="normal")
selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        type_tree_forosh_btn.config(text=','.join(selected_trees2))
selected_option2=[]
def add_option2():
    op2=option_forosh_bagh_zamin_combo.get()
    if op2 and op2 not in selected_option2:
        selected_option2.append(op2)
        lable_natige_add_forosh_bagh_zamin.config(text=','.join(selected_option2))
selected_trees3=[]
def add_tree3():
    t4=type_tree_kharid_bagh_zamin_combo.get()
    if t4 and t4 not in selected_trees3:
        selected_trees3.append(t4)
        type_tree_kharid_btn.config(text=','.join(selected_trees3))
selected_option3=[]
def add_option3():
    op3=option_kharid_bagh_zamin_combo.get()
    if op3 and op3 not in selected_option3:
        selected_option3.append(op3)
        lable_natige_add_kharid_bagh_zamin.config(text=','.join(selected_option3))
#====================================================================================
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
selected_topo1=[]
def add_topo1():
    topo=zamin_shekl_ejareh_bagh_zamin_combo.get()
    if topo and topo not in selected_topo1:
        selected_topo1.append(topo)
        label_natige_topo_add_ejareh_bagh_zamin.config(text=','.join(selected_topo1))
selected_topo2=[]
def add_topo2():
    topo2=zamin_shekl_forosh_bagh_zamin_combo.get()
    if topo2 and topo2 not in selected_topo2:

        selected_topo2.append(topo2)
        add_topo2_button_forosh_bagh_zamin.config(text=','.join(selected_topo2))
#=====================================================================================
def home_true_false1(): # برای فعال یا غیر فعال کردن ویجت های خونه باغ در اجاره
    if var0.get()==1:
        metraj_vila_bagh_entry.config(state="normal")
        sal_sakht_vila_bagh_entry.config(state="normal")
        type_vila_ejareh_bagh_zamin_combo.config(state="readonly")
        toilet_bagh_combo.config(state="readonly")
        hamam_bagh_combo.config(state="readonly")
        sanad_bagh_combo.config(state="readonly")
        option_forosh_bagh_zamin_combo.config(state="readonly")
        mojavez_sakht_ejareh_bagh_zamin.config(state="normal")
        mohavate_ejareh_bagh_zamin.config(state="normal")
    else:
        metraj_vila_bagh_entry.config(state="disabled")
        sal_sakht_vila_bagh_entry.config(state="disabled")
        type_vila_ejareh_bagh_zamin_combo.config(state="disabled")
        toilet_bagh_combo.config(state="disabled")
        hamam_bagh_combo.config(state="disabled")
        sanad_bagh_combo.config(state="disabled")
        option_forosh_bagh_zamin_combo.config(state="disabled")
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
def home_true_false3(): #برای فعال یا غیر فعال کردن ویجت های خونه باغ در خرید
    if var0_kharid_bagh_zamin.get()==1:
        metraj_vila_kharid_bagh_zamin_entry.config(state="normal")
        sal_sakht_vila_kharid_bagh_zamin_entry.config(state="normal")
        type_vila_kharid_bagh_zamin_combo.config(state="readonly")
        toilet_kharid_bagh_zamin_combo.config(state="readonly")
        hamam_kharid_bagh_zamin_combo.config(state="readonly")
        sanad_kharid_bagh_zamin_combo.config(state="readonly")
        option_kharid_bagh_zamin_combo.config(state="readonly")
        divar_kharid_bagh_zamin.config(state="normal")
        mojavez_sakht_check_btn_kharid_bagh_zamin.config(state="normal")
        mohavate_sazi_check_btn_kharid_bagh_zamin.config(state="normal")
    else:
        metraj_vila_kharid_bagh_zamin_entry.config(state="disabled")
        sal_sakht_vila_kharid_bagh_zamin_entry.config(state="disabled")
        type_vila_kharid_bagh_zamin_combo.config(state="disabled")
        toilet_kharid_bagh_zamin_combo.config(state="disabled")
        hamam_kharid_bagh_zamin_combo.config(state="disabled")
        sanad_kharid_bagh_zamin_combo.config(state="disabled")
        option_kharid_bagh_zamin_combo.config(state="disabled")
        mojavez_sakht_check_btn_kharid_bagh_zamin.config(state="disabled")
        mohavate_sazi_check_btn_kharid_bagh_zamin.config(state="disabled")
def choos_kesht(event):
    a=kesht_ejareh_bagh_zamin_combo.get()
    if a=="بدون کشت":
        kesht_ejareh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_ejareh_bagh_zamin_entry.config(state="readonly")
def choos_kesht2(event):
    b=kesht_forosh_bagh_zamin_combo.get()
    if b=="بدون کشت":
        kesht_forosh_bagh_zamin_entry.config(state="disabled")
    else:
        kesht_forosh_bagh_zamin_entry.config(state="readonly")
selected_trees2=[]
def add_tree2():
    t3=type_tree_forosh_bagh_zamin_combo.get()
    if t3 and t3 not in selected_trees2:
        selected_trees2.append(t3)
        type_tree_forosh_btn.config(text=','.join(selected_trees2))
selected_option2=[]
def add_option2():
    op2=option_forosh_bagh_zamin_combo.get()
    if op2 and op2 not in selected_option2:
        selected_option2.append(op2)
        add_option_button_forosh_bagh_zamin.config(text=','.join(selected_option2))
#endregion
#---#----#----#----#----#----------  گرافیک   ----------#----#----#----#-----#-----------
# ---------دکمه فایل با منوی کشویی ------------------
#region 
menubar = tk.Menu(root, font=("Shabnam", 10))
# ایجاد منوی "ثبت فایل ها"
file_menu_sabt_file = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_sabt_file.add_command(label="خرید", command=kharid)
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
file_menu_gharardad.add_command(label="خرید", command=None)
file_menu_gharardad.add_command(label="فروش", command=None)
file_menu_gharardad.add_command(label="رهن/اجاره", command=None)
file_menu_gharardad.add_command(label="مشارکت", command=None)

# اضافه کردن منوی قرار دادها به منوبار
menubar.add_cascade(label="قراردادها", menu=file_menu_gharardad)
#endregion
#----------------دکمه گزارش ها با منوی کشویی ------------------------
#region
# ----------لیست کشویی فیلد گزارش ها-----------------
file_menu_gozaresh = tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_gozaresh.add_command(label="خروجی اکسل", command=None)
file_menu_gozaresh.add_command(label="قراردادها", command=None)
# اضافه کردن منوی گزارش ها به منوبار
menubar.add_cascade(label="گزارش ها", menu=file_menu_gozaresh)
#endregion
#--------------------------تابع های خروجی اکسل و قرار دادها------------
def excel():
    pass
def gharardadeha():
    pass
# ----------------------اضافه کردن فیلد درخواست ها-------
#region
file_menu_darkhast= tk.Menu(menubar, tearoff=0, font=("Shabnam", 10))
file_menu_darkhast.add_command(label="", command=None)
file_menu_darkhast.add_command(label="", command=None)

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
frame_jostojo_melk_left= tk.LabelFrame(root, text="جستجوی ملک", width=200, bg="#052340",fg="#00BFFF", font=("Shabnam", 16))
frame_jostojo_melk_left.pack(side="left", fill="y", padx=6, pady=15)

box_jostojo_malk1= tk.Frame(frame_jostojo_melk_left,bg="#052340")
box_jostojo_malk1.pack(padx=6, pady=15)

file_type = tk.Label(box_jostojo_malk1,text="نوع فایل",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
file_type.pack(padx=15,pady=10, side="right")
combo_file_type= ttk.Combobox(box_jostojo_malk1)
combo_file_type["values"] = ("رهن/اجاره","خرید","فروش","مشارکت",)
combo_file_type["state"]=["readonly"]
combo_file_type.pack(padx=10, pady=10) 

box_jostojo_malk2= tk.Frame(frame_jostojo_melk_left,bg="#052340")
box_jostojo_malk2.pack(padx=6, pady=15)

melk_type_lable = tk.Label(box_jostojo_malk2,text="نوع ملک",bg="#052340", fg="#FFFFFF",font=("Shabnam", 13))
melk_type_lable.pack(padx=15,pady=10, side="right")
melk_type_combo= ttk.Combobox(box_jostojo_malk2)
melk_type_combo["values"] = ("مسکونی","مغازه/ تجاری"," باغ / زمین","کارگاه")
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
search_btn = tk.Button(frame_jostojo_melk_left, text="    جستجو    " , bg="#00BFFF", fg="#000000", font=("Shabnam", 13), command=open_file)
search_btn.pack(pady=10)
#=====================================================
#endregion
# ---------------------------باکس وسط - نمایش جستجوی --------------
#region
frame_list_amlack_centre = tk.LabelFrame(root, text="لیست املاک", bg="#052340",fg="#00BFFF", font=("Shabnam", 13))
frame_list_amlack_centre.pack(side="left", fill="both", expand=True, padx=4, pady=15)

columns = ["آدرس", "قیمت ", "نوع ملک ", "متراژ"]
tree = ttk.Treeview(frame_list_amlack_centre, columns=columns, show="headings")
for textt in columns:
    tree.heading(textt,text=textt)
    tree.column(textt, width=100)
tree.pack(fill="both", expand=True)
#===================================================
#endregion
# --------------------باکس سمت راست - نمایش جزئیات فایل های موجود املاک---------------
#region
frame_joziat_amlack = tk.LabelFrame(root, text="جزئیات ملک", width=200, bg="#052340",fg="#00BFFF", font=("Shabnam", 13))
frame_joziat_amlack.pack(side="right", fill="y", padx=6, pady=15)

photo_melk_lbl = tk.Label(frame_joziat_amlack, text="[تصویر ملک]", bg="#FFFFFF", width=20, height=10)
photo_melk_lbl.pack(pady=10)

malek = tk.Label(frame_joziat_amlack,text="مالک ",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
malek.pack(padx=6,pady=4)

entry_malek = tk.Entry(frame_joziat_amlack,bg="#FFFFFF", fg="#000000",font=("Shabnam", 13))
entry_malek.pack(padx=20,pady=4)

malek_phone_number = tk.Label(frame_joziat_amlack,text="شماره تماس مالک ",bg="#052340", fg="#F7F7FA",font=("Shabnam", 13))
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

forosh_edari_radio = tk.Radiobutton(box_forosh, value=2, text="ثبت فایل اداری/تجاری",
bg="#052340",fg="#00BFFF", variable=forosh_radio_value, font=("Shabnam",11))
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
#----------------------------------نوع انتخاب ثبتی فایل برای پنجره های خرید-----------------
#region
box_kharid=tk.Toplevel(root)
box_kharid.title("انتخاب نوع ملک خرید")
box_kharid.geometry("500x270")
box_kharid.withdraw()
box_kharid.configure(bg="#052340")

# یک متغیر مشترک برای همه رادیوباتن‌ها
kharid_radio_value = tk.IntVar(value=0)  # مقدار پیش‌فرض -1 یعنی هیچکدام انتخاب نشده

kharid_maskoni_radio = tk.Radiobutton(box_kharid, value=0, text="ثبت فایل مسکونی", background="#052340",fg="#00BFFF", variable=kharid_radio_value, font=("Shabnam",11))
kharid_maskoni_radio.place(x=330,y=50)

kharid_edari_radio = tk.Radiobutton(box_kharid, value=2, text="ثبت فایل اداری/تجاری",
bg="#052340",fg="#00BFFF", variable=kharid_radio_value, font=("Shabnam",11))
kharid_edari_radio.place(x=330,y=90)

kharid_bagh_radio = tk.Radiobutton(box_kharid, value=4, text="ثبت فایل باغ/زمین",bg="#052340",fg="#00BFFF", variable=kharid_radio_value, font=("Shabnam",11))
kharid_bagh_radio.place(x=330,y=130)

kharid_kargah_radio = tk.Radiobutton(box_kharid, value=6, text="ثبت فایل کارگاه",bg="#052340",fg="#00BFFF", variable=kharid_radio_value, font=("Shabnam",11))
kharid_kargah_radio.place(x=330,y=170)


back_to_home_box_kharid=tk.Button(box_kharid,text="بازگشت",bg="#00BFFF",fg="#000000",width=12,height=2,command=back_kharid_exit)
back_to_home_box_kharid.place(x=190,y=210)

zakhire_radio_box_kharid=tk.Button(box_kharid,text="ادامه",bg="#00BFFF",fg="#000000",width=12,height=2,command=sabt_radio_kharid)
zakhire_radio_box_kharid.place(x=50,y=210)

box_kharid.protocol("WM_DELETE_WINDOW", lambda: None)
box_kharid.resizable(False, False)
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
bg_image = Image.open("large_a94eba63-7081-44d1-9491-d81113e6c266.jpg")
bg_image = bg_image.resize((800, 600))
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

addrres_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
addrres_ejare_maskoni_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

# ردیف 4: طبقه
tabaghe_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="طبقه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
tabaghe_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

tabaghe_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
tabaghe_ejare_maskoni_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

# ردیف 5: واحد
vahed_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="واحد", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
vahed_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

vahed_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
vahed_ejare_maskoni_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

# ردیف 6: اتاق
otagh_ejare_maskoni_lable = tk.Label(ejareh_rehn_page, text="اتاق", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
otagh_ejare_maskoni_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

otagh_ejare_maskoni_entry = tk.Entry(ejareh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
otagh_ejare_maskoni_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

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

back_to_home_ejareh_maskoni=tk.Button(ejareh_rehn_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_ejare_maskoni)
back_to_home_ejareh_maskoni.place(x=270,y=520)

save_button_ejareh_maskooni=tk.Button(ejareh_rehn_page,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_rehn_maskkoni)
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
option_frame_ejare_maskoni.place(x=525,y=500)

add_option_frame_ejare_maskoni=tk.Label(option_frame_ejare_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
add_option_frame_ejare_maskoni.pack(side="right",padx=1)

plus_button_ejare_maskoni=tk.Button(option_frame_ejare_maskoni,image=plus,command=open_option1,border=0)
plus_button_ejare_maskoni.pack()

bg_image = Image.open("large_a94eba63-7081-44d1-9491-d81113e6c266.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_maskoni, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# --- چک‌باکس‌ها (پارکینگ، آسانسور، انباری) ---
# چیدمان افقی در بالای فرم
parking_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=parking_pic, bg="#052340")
parking_checkbutton_btn_ejareh_maskoni.place(x=140, y=50)

asansor_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=elvator_pic, bg="#052340")
asansor_checkbutton_btn_ejareh_maskoni.place(x=240, y=50)

anbari_checkbutton_btn_ejareh_maskoni = tk.Checkbutton(option_file_frame_ejareh_maskoni, image=warehouse_pic, bg="#052340")
anbari_checkbutton_btn_ejareh_maskoni.place(x=340, y=50)

# 1. سرمایش
sarmaesh_ejare_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="سرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
sarmaesh_ejare_maskoni.place(x=320, y=110)
sarmaesh_ejare_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
sarmaesh_ejare_maskoni_combo["values"] = ("ندارد", "پنکه سقفی", "کولر ابی", "کولر گازی ", "ابی/گازی")
sarmaesh_ejare_maskoni_combo["state"] = "readonly"
sarmaesh_ejare_maskoni_combo.place(x=120, y=110)

# 2. گرمایش
garmaesh_ejare_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="گرمایش", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
garmaesh_ejare_maskoni.place(x=320, y=150)
garmaesh_ejare_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
garmaesh_ejare_maskoni_combo["values"] = ("ندارد", "بخاری", " شوفاژ", "گرمایش از کف ")
garmaesh_ejare_maskoni_combo["state"] = "readonly"
garmaesh_ejare_maskoni_combo.place(x=120, y=150)

# 3. کف
kaf_ejare_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="کف", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
kaf_ejare_maskoni.place(x=320, y=190)
kaf_ejare_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
kaf_ejare_maskoni_combo["values"] = ("سرامیک", "موزاییک", "پارکت")
kaf_ejare_maskoni_combo["state"] = "readonly"
kaf_ejare_maskoni_combo.place(x=120, y=190)

# 4. سرویس بهداشتی
toilet_ejare_maskoni = tk.Label(option_file_frame_ejareh_maskoni, text="سرویس بهداشتی", bg="#052340", fg="#ffffff", font=("Shabnam", 11))
toilet_ejare_maskoni.place(x=320, y=230)
toilet_ejare_maskoni_combo = ttk.Combobox(option_file_frame_ejareh_maskoni, width=15)
toilet_ejare_maskoni_combo["values"] = ("ایرانی", "فرنگی", "هردو")
toilet_ejare_maskoni_combo["state"] = "readonly"
toilet_ejare_maskoni_combo.place(x=120, y=230)


# --- دکمه‌های پایین صفحه ---
save_optoin_ejareh_maskoni = tk.Button(option_file_frame_ejareh_maskoni, text="ذخیره", command=None, bg="#00BFFF", fg="#000000", width=10, height=1)
save_optoin_ejareh_maskoni.place(x=95, y=320)

back_to_ejare_maskoni = tk.Button(option_file_frame_ejareh_maskoni, text="بازگشت", command=back_to_ejareh_maskoni_page, bg="#00BFFF", fg="#000000", width=10, height=1)
back_to_ejare_maskoni.place(x=215, y=320)

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
bg_image = Image.open("singapore-skyscrapers-marina-bay-sands-evening-4k-es-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

melk_type_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari, text=" متراژ ملک", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
melk_type_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

melk_type_ejareh_edari_tejari_entry=tk.Entry(ejareh_edari_tejari, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
melk_type_ejareh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

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

rahn_kamel_ejareh_edari_tejari_lable=tk.Label(ejareh_edari_tejari,text=" رهن کامل؟ ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
rahn_kamel_ejareh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")

rahn_kamel_checkbutton_ejareh_edari_tejari=tk.Checkbutton(ejareh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
rahn_kamel_checkbutton_ejareh_edari_tejari.place(x=start_x + 10, y=start_y + 425)

back_to_home_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_ejareh_edari_tejari)
back_to_home_ejareh_edari_tejari.place(x=280,y=520)

zakhire_ejareh_edari_tejari=tk.Button(ejareh_edari_tejari,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=save_rehn_edari)
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
option_frame_ejareh_edari_tejari.place(x=250,y=373)

option_label_ejareh_edari_tejari=tk.Label(option_frame_ejareh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_ejareh_edari_tejari.pack(side="right",padx=1)

plus_button_ejareh_edari_tejari=tk.Button(option_frame_ejareh_edari_tejari,image=plus,command=open_option3,border=0)
plus_button_ejareh_edari_tejari.pack(side="right",padx=1)

bg_image = Image.open("singapore-skyscrapers-marina-bay-sands-evening-4k-es-1920x1200.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_edari_tajari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,image=parking_pic,background="#052340")
parking_ch_btn_ejareh_edari_tejari.place(x=140, y=50)

elvator_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,image=elvator_pic,background="#052340")
elvator_ch_btn_ejareh_edari_tejari.place(x=240, y=50)

warehouse_ch_btn_ejareh_edari_tejari=tk.Checkbutton(option_file_frame_ejareh_edari_tajari,image=warehouse_pic,background="#052340")
warehouse_ch_btn_ejareh_edari_tejari.place(x=340, y=50)

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

save_optoin_ejareh_maskoni=tk.Button(option_file_frame_ejareh_edari_tajari,text="ذخیره",command=None,background="#00BFFF",fg="#000000",width=10,height=1)
save_optoin_ejareh_maskoni.place(x=95,y=320)

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

bg_image = Image.open("empire-state-building-night-5k-oa-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(ejareh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------------کادر اجاره باغ و زمین---------------------#
frame_ejareh_bagh_zamin= tk.Frame(ejareh_bagh_zamin,bd=0,highlightthickness=0)
frame_ejareh_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(ejareh_bagh_zamin,text="اجاره باغ و زمین",bg="#000000",fg="#00BFFF",font=("Shabnam", 15))
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

bagh_loctaion_lable=tk.Label(ejareh_bagh_zamin, text=" منطقه و آدرس ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_loctaion_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_loctaion_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

bagh_gheimat_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="ودیعه", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_gheimat_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

bagh_gheimat_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_gheimat_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

bagh_gheimat_har_metr_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin, text="قیمت هر متر", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
bagh_gheimat_har_metr_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

bagh_gheimat_ejareh_bagh_zamin_entry=tk.Entry(ejareh_bagh_zamin, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
bagh_gheimat_ejareh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

time_bagh_ejareh_bagh_zamin_lable=tk.Label(ejareh_bagh_zamin,text="مدت اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
time_bagh_ejareh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

bagh_time_combo=ttk.Combobox(ejareh_bagh_zamin,state="readonly")
bagh_time_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
bagh_time_combo.set("فصلی")
bagh_time_combo.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

photo_lbl2_ejareh_bagh_zamin = tk.Label(ejareh_bagh_zamin, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15)
photo_lbl2_ejareh_bagh_zamin.place(x=60, y=85)


add_img_btn_ejareh_bagh_zamin = tk.Button(ejareh_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_ejareh_bagh_zamin.place(x=60, y=370)

back_to_home_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_ejareh_bagh)
back_to_home_ejareh_bagh_zamin.place(x=290,y=520)

zakhire_ejareh_bagh_zamin=tk.Button(ejareh_bagh_zamin,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=save_rehn_bagh)
zakhire_ejareh_bagh_zamin.place(x=140,y=520)

ejareh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_bagh_zamin.resizable(False, False)

#endregion
#---------------------امکانات اجاره باغ/زمین---------------------
#region
option_frame_ejareh_bagh_zamin=tk.Frame(ejareh_bagh_zamin,width=300,height=30,background="#052340")
option_frame_ejareh_bagh_zamin.place(x=525,y=450)

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

bg_image = Image.open("empire-state-building-night-5k-oa-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_ejareh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

karbari_zamin_ejareh_bagh_zamin_lable=tk.Label(option_file_frame_ejareh_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",9),width=9)
karbari_zamin_ejareh_bagh_zamin_lable.place(x=463, y=40)

karbari_zamin_combo=ttk.Combobox(option_file_frame_ejareh_bagh_zamin,state="readonly")
karbari_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbari_zamin_combo.set("باغ")
karbari_zamin_combo.place(x=273, y=40)

karbari_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin1)

metraj_tree=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_tree.place(x=450, y=70)

metraj_tree_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_tree_entry.place(x=305, y=70)

tree_count=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tree_count.place(x=460, y=100)

tree_count_entry=tk.Entry(option_file_frame_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tree_count_entry.place(x=305, y=100)

abyari=tk.Label(option_file_frame_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع ابیاری")
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
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_combo["state"]=["readonly"]
type_tree_combo.set("گردو")
type_tree_combo.place(x=273, y=160)

add_tree_button=tk.Button(option_file_frame_ejareh_bagh_zamin,text="افزودن درخت",font=("Shabnam",9),command=add_tree,bg="#00BFFF",width=10,height=1)
add_tree_button.place(x=460, y=190)

label_result_add=tk.Label(option_file_frame_ejareh_bagh_zamin,text="")
label_result_add.place(x=305, y=190)

chah_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="چاه",font=("Shabnam",9),background="#052340",fg="#00BFFF")
chah_bagh.place(x=480, y=220)

estakhr_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="استخر",font=("Shabnam",9),background="#052340",fg="#00BFFF")
estakhr_bagh.place(x=380, y=220)

loleh_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="اب لوله کشی",font=("Shabnam",9),background="#052340",fg="#00BFFF")
loleh_bagh.place(x=280, y=220)

bargh_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="برق کشی",font=("Shabnam",9),background="#052340",fg="#00BFFF")
bargh_bagh.place(x=180, y=220)

gas_bagh=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="گاز کشی",font=("Shabnam",9),background="#052340",fg="#00BFFF")
gas_bagh.place(x=80, y=220)

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

mojavez_sakht_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_ejareh_bagh_zamin.place(x=450, y=510)

mohavate_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_ejareh_bagh_zamin.place(x=320, y=510)

divar_ejareh_bagh_zamin=tk.Checkbutton(option_file_frame_ejareh_bagh_zamin,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_ejareh_bagh_zamin.place(x=180, y=510)

zakhire_option_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_option_ejareh_bagh_zamin.place(x=95,y=580)

back_to_ejareh_bagh_zamin=tk.Button(option_file_frame_ejareh_bagh_zamin,text="بازگشت",command=back_to_ejareh_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_ejareh_bagh_zamin.place(x=215,y=580)

option_file_frame_ejareh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_ejareh_bagh_zamin.resizable(False, False)

#endregion
#-------------------تعویض کاربری به زمین در قسمت اجاره باغ/زمین--------------
#region
fram_option_zamin_ejareh_bagh_zamin=tk.Frame(option_file_frame_ejareh_bagh_zamin,width=445,height=290,background="#052340")
fram_option_zamin_ejareh_bagh_zamin.place_forget()

metraj_zamin_ejareh_bagh_zamin2=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin_ejareh_bagh_zamin2.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin_ejareh_bagh_zamin_entry2=tk.Entry(fram_option_zamin_ejareh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin_ejareh_bagh_zamin_entry2.grid(padx=10,pady=5,row=0,column=3)

karbari_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=1,column=4)

karbari_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
karbari_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")     
karbari_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                        
karbari_ejareh_ejareh_bagh_zamin_combo.set(" ")
karbari_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
khak_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")
khak_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                              
khak_ejareh_ejareh_bagh_zamin_combo.set(" ")
khak_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_ejareh_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع اب")
ab_ejareh_ejareh_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_ejareh_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
ab_ejareh_ejareh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر") 
ab_ejareh_ejareh_bagh_zamin_combo["state"]=["readonly"]                             
ab_ejareh_ejareh_bagh_zamin_combo.set(" ")
ab_ejareh_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="توپوگرافی")
zamin_shekl_ejareh_bagh_zamin.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
zamin_shekl_ejareh_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")         
zamin_shekl_ejareh_bagh_zamin_combo["state"]=["readonly"]                     
zamin_shekl_ejareh_bagh_zamin_combo.set(" ")
zamin_shekl_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo_button=tk.Button(fram_option_zamin_ejareh_bagh_zamin,text=" مورد دلخواه",command=add_topo1,bg="#00BFFF",font=("Shabnam",9),width=10,height=1)
add_topo_button.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,text="")
label_natige_topo_add_ejareh_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_ejareh_bagh_zamin=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="سطح زیر کشت")
kesht_ejareh_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_ejareh_bagh_zamin_combo=ttk.Combobox(fram_option_zamin_ejareh_bagh_zamin)
kesht_ejareh_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_ejareh_bagh_zamin_combo.set("بدون کشت ")
kesht_ejareh_bagh_zamin_combo["state"]=["readonly"] 
kesht_ejareh_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_ejareh_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht)

kesht_ejareh_bagh_zamin_label=tk.Label(fram_option_zamin_ejareh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=11,text="محصول زیرکشت")
kesht_ejareh_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_ejareh_bagh_zamin_entry=tk.Entry(fram_option_zamin_ejareh_bagh_zamin,width=10,bg="#00BFFF",fg="#ffffff",state="disabled")
kesht_ejareh_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_room_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_room_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_tak_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_tak_faz_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_se_faz_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_se_faz_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه ساخت گلخانه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_golkhane_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavaz_chah_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavaz_chah_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="حق برداشت ",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bardasht_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_ejareh_bagh_zamin=tk.Checkbutton(fram_option_zamin_ejareh_bagh_zamin,text="اجازه ورود دام",background="#052340",fg="#00BFFF",font=("Shabnam",9))
dam_zamin_ejareh_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)

#=======================================================================
#endregion
#-------------------پنجره اجاره کارگاه------------------------
#region
ejareh_karghah = tk.Toplevel(root)
ejareh_karghah.title(" اجاره کارگاه")
ejareh_karghah.geometry("800x600")
ejareh_karghah.withdraw()

bg_image = Image.open("yokohama-at-night-noen-city-4k-00-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

gheimat_har_metr_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="قیمت هر متر", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_har_metr_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_har_metr_ejareh_kargah_entry=tk.Entry(ejareh_karghah, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_har_metr_ejareh_kargah_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)


time_ejate_ejareh_kargah_lable=tk.Label(ejareh_karghah, text="مدت اجاره", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
time_ejate_ejareh_kargah_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

time_ejare_ejareh_kargah_combo=ttk.Combobox(ejareh_karghah,state="readonly")
time_ejare_ejareh_kargah_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
time_ejare_ejareh_kargah_combo.set("فصلی")
time_ejare_ejareh_kargah_combo.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

photo_lbl2_ejareh_kargah = tk.Label(ejareh_karghah, text="[تصویر ملک]", bg="#FFFFFF", width=50, height=15)
photo_lbl2_ejareh_kargah.place(x=60, y=85)

add_img_btn_ejareh_kargah = tk.Button(ejareh_karghah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_ejareh_kargah.place(x=60, y=370)

back_to_home_ejareh_kargah=tk.Button(ejareh_karghah,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_ejareh_karghah)
back_to_home_ejareh_kargah.place(x=290,y=520)

zakhire_ejareh_kargah=tk.Button(ejareh_karghah,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_ejareh_karghah)
zakhire_ejareh_kargah.place(x=140,y=520)

ejareh_karghah.protocol("WM_DELETE_WINDOW", lambda: None)
ejareh_karghah.resizable(False, False)
#endregion
#---------------------پنجره امکانات اجاره کارگاه---------------------
#region
option_frame_ejareh_kargah=tk.Frame(ejareh_karghah,width=300,height=30,background="#052340")
option_frame_ejareh_kargah.place(x=525,y=450)

option_frame_ejareh_kargah_lable=tk.Label(option_frame_ejareh_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_ejareh_kargah_lable.pack(side="right",padx=1)

plus_button_ejareh_kargah=tk.Button(option_frame_ejareh_kargah,image=plus,command=open_option7,border=0)
plus_button_ejareh_kargah.pack()

option_file_frame_ejareh_kargah=tk.Toplevel(ejareh_karghah)
option_file_frame_ejareh_kargah.title(" امکانات اجاره کارگاه")
option_file_frame_ejareh_kargah.geometry("500x500")
option_file_frame_ejareh_kargah.pack_propagate(False)
option_file_frame_ejareh_kargah.withdraw()

bg_image = Image.open("yokohama-at-night-noen-city-4k-00-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
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
vaziat_bargh_ejareh_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_ejareh_kargah_combo.set("برق شهری")
vaziat_bargh_ejareh_kargah_combo["state"]=["readonly"]
vaziat_bargh_ejareh_kargah_combo.place(x=70, y=80)

garmayesh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_ejareh_kargah.place(x=295, y=110)

garmayesh_type_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
garmayesh_type_ejareh_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_ejareh_kargah_combo.set(" بخاری")
garmayesh_type_ejareh_kargah_combo["state"]=["readonly"]
garmayesh_type_ejareh_kargah_combo.place(x=70, y=110)

sarmayesh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_ejareh_kargah.place(x=295, y=140)

sarmayesh_fan_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="تهویه(فن)",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_ejareh_kargah.place(x=295, y=170)

sarmayesh_panke_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="پنکه سقفی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_ejareh_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="کولر آبی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_ejareh_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_ejareh_kargah=tk.Checkbutton(option_file_frame_ejareh_kargah,text="کولر گازی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_ejareh_kargah.place(x=84, y=200)

vaziat_ab_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",width=13,text=" وضعیت آب",font=("Shabnam", 9))
vaziat_ab_ejareh_kargah.place(x=303, y=230)

vaziat_ab_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah,width=35)
vaziat_ab_ejareh_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_ejareh_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_ejareh_kargah_combo["state"]=["readonly"]
vaziat_ab_ejareh_kargah_combo.place(x=30, y=230)

abzar_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_ejareh_kargah.place(x=298, y=260)

abzaar_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah,width=23)
abzaar_ejareh_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzaar_ejareh_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzaar_ejareh_kargah_combo["state"]=["readonly"]
abzaar_ejareh_kargah_combo.place(x=58, y=260)

toilet_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_ejareh_kargah.place(x=298, y=290)

toilet_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
toilet_ejareh_kargah_combo["values"]=("دارد","ندارد")
toilet_ejareh_kargah_combo.set("دارد")
toilet_ejareh_kargah_combo["state"]=["readonly"]
toilet_ejareh_kargah_combo.place(x=70, y=290)

hamam_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_ejareh_kargah.place(x=303, y=320)

hamam_ejareh_kargah__combo=ttk.Combobox(option_file_frame_ejareh_kargah)
hamam_ejareh_kargah__combo["values"]=("ندارد","دارد")
hamam_ejareh_kargah__combo.set("ندارد")
hamam_ejareh_kargah__combo["state"]=["readonly"]
hamam_ejareh_kargah__combo.place(x=70, y=320)

otagh_ejareh_kargah=tk.Label(option_file_frame_ejareh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_ejareh_kargah.place(x=294, y=350)

otagh_ejareh_kargah_combo=ttk.Combobox(option_file_frame_ejareh_kargah)
otagh_ejareh_kargah_combo["values"]=("ندارد","دارد")
otagh_ejareh_kargah_combo.set("ندارد")
otagh_ejareh_kargah_combo["state"]=["readonly"]
otagh_ejareh_kargah_combo.place(x=70, y=350)

zakhire_options_ejareh_kargah=tk.Button(option_file_frame_ejareh_kargah,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
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
bg_image = Image.open("singapore-city-skyline-5k-kb-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

title_lbl = tk.Label(forosh_rehn_page,text="فروش مسکونی",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
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

gheimat_forosh_maskoni=tk.Label(forosh_rehn_page, text=" قیمت ", bg="#052340", fg="#ffffff", font=("Shabnam", 12), width=9)
gheimat_forosh_maskoni.place(x=start_x + 320, y=start_y + 340, anchor="e")

gheimat_forosh_maskoni_entry=tk.Entry(forosh_rehn_page, bg="#FFFFFF", fg="#000000", font=("Shabnam", 10))
gheimat_forosh_maskoni_entry.place(x=start_x + 10, y=start_y + 328, width=150, height=25)


back_to_home_forosh_maskoni=tk.Button(forosh_rehn_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_maskoni)
back_to_home_forosh_maskoni.place(x=270,y=520)

zakhire_forosh_maskoni=tk.Button(forosh_rehn_page,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_forosh_maskkoni)
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
option_frame_options_forosh_maskoni.place(x=520,y=460)

option_label_forosh_maskoni=tk.Label(option_frame_options_forosh_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_forosh_maskoni.pack(side="right",padx=1)

plus_button_forosh_maskoni=tk.Button(option_frame_options_forosh_maskoni,image=plus,command=open_option2,border=0)
plus_button_forosh_maskoni.pack()

bg_image = Image.open("singapore-city-skyline-5k-kb-1920x1200.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_maskoni, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


parking_ch_btn_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni, image=parking_pic, bg="#052340")
parking_ch_btn_forosh_maskoni.place(x=140, y=50)

asansor_ch_btn_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni,image=elvator_pic,background="#052340")
asansor_ch_btn_forosh_maskoni.place(x=240, y=50)

anbari_checkbuton_forosh_maskoni=tk.Checkbutton(option_file_frame_forosh_maskoni,image=warehouse_pic,background="#052340")
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

zakhire_options_forosh_maskini=tk.Button(option_file_frame_forosh_maskoni,text="ذخیره",command=None,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_forosh_maskini.place(x=95, y=320)

back_to_home_forosh_maskoni=tk.Button(option_file_frame_forosh_maskoni,text="بازگشت",command=back_to_forosh_maskoni_page,background="#00BFFF",fg="#000000",width=10,height=1)
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

bg_image = Image.open("aesthetic-city-night-lights-5s-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

melk_type_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="متراژ ملک ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

melk_type_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
melk_type_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

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


mablagh_pish_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text="مبلغ ودیعه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_pish_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

mablagh_pish_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_pish_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

mablagh_ejare_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text=" مبلغ اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_ejare_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

mablagh_ejare_forosh_edari_tejari_entry=tk.Entry(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10),)
mablagh_ejare_forosh_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

rahn_kamel_forosh_edari_tejari_lable=tk.Label(forosh_edari_tejari,text=" رهن کامل؟ ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
rahn_kamel_forosh_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")

rahn_kamel_check_btn_forosh_edari_tejari=tk.Checkbutton(forosh_edari_tejari,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
rahn_kamel_check_btn_forosh_edari_tejari.place(x=start_x + 10, y=start_y + 425)


back_to_home_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_edari_tejari)
back_to_home_forosh_edari_tejari.place(x=280,y=520)

zakhire_forosh_edari_tejari=tk.Button(forosh_edari_tejari,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_forosh_edari)
zakhire_forosh_edari_tejari.place(x=130,y=520)

photo_lbl2_forosh_edari_tejari = tk.Label(forosh_edari_tejari, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_forosh_edari_tejari.place(x=60, y=85)

add_img_btn_forosh_edari_tejari = tk.Button(forosh_edari_tejari, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_edari_tejari.place(x=60, y=370)

forosh_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_edari_tejari.resizable(False, False)
#endregion
#---------------امکانات فروش اداری/تجاری-------------------
#region
option_frame_options_forosh_edari_tejari=tk.Frame(forosh_edari_tejari,width=300,height=30,background="#052340")
option_frame_options_forosh_edari_tejari.place(x=250,y=373)

option_label_forosh_edari_tejari=tk.Label(option_frame_options_forosh_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_forosh_edari_tejari.pack(side="right",padx=1)

plus_button_forosh_eedari_tejari=tk.Button(option_frame_options_forosh_edari_tejari,image=plus,command=open_option4,border=0)
plus_button_forosh_eedari_tejari.pack()

bg_image = Image.open("aesthetic-city-night-lights-5s-1920x1200.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_edari_tejari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,image=parking_pic,background="#052340")
parking_check_btn_forosh_edari_tejari.place(x=140, y=50)

asansor_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,image=elvator_pic,background="#052340")
asansor_check_btn_forosh_edari_tejari.place(x=240, y=50)

anbari_check_btn_forosh_edari_tejari=tk.Checkbutton(option_file_frame_forosh_edari_tejari,image=warehouse_pic,background="#052340")
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

zakhire_options_forosh_edari_tejari=tk.Button(option_file_frame_forosh_edari_tejari,text="ذخیره",command=None,background="#00BFFF",fg="#000000",width=10,height=1)
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

bg_image = Image.open("santa-monica-pier-5k-8m-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

bagh_loctaion_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text="منطقه و ادرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
bagh_loctaion_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#FFFFFF", fg="#000000",font=("Shabnam", 10))
bagh_loctaion_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

gheimat_bagh_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text='ودیعه',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_bagh_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_bagh_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_bagh_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable=tk.Label(forosh_bagh_zamin,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_har_matr_babagh_zamin_forosh_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

gheimat_har_metr_babagh_zamin_forosh_bagh_zamin_entry=tk.Entry(forosh_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_babagh_zamin_forosh_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

#time_bagh_forosh_bagh_zamin=tk.Label(frame_asli_forosh_bagh_zamin,text="مدت اجاره",bg="#052340",fg="#ffffff",width=10)
#time_bagh_forosh_bagh.grid(padx=8,pady=15,sticky="e",row=5,column=1)

#bagh_time_forosh_bagh_combo=ttk.Combobox(frame_asli_forosh_bagh_zamin,state="readonly")
#bagh_time_forosh_bagh_zamin_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
#.set("فصلی")
#bagh_time_forosh_bagh_zamin_combo.grid(padx=8,pady=15,sticky="w",row=5,column=0)

photo_forosh_bagh_zamin_lable= tk.Label(forosh_bagh_zamin, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_forosh_bagh_zamin_lable.place(x=60, y=85)
add_img_btn_forosh_bagh_zamin = tk.Button(forosh_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_bagh_zamin.place(x=60, y=370)

back_to_home_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_bagh)
back_to_home_forosh_bagh_zamin.place(x=290,y=520)

zakhire_forosh_bagh_zamin=tk.Button(forosh_bagh_zamin,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_forosh_bagh)
zakhire_forosh_bagh_zamin.place(x=140,y=520)

forosh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_bagh_zamin.resizable(False, False)
#endregion
#-----------------------پنجره امکانات فروش باغ/زمین-------------------
#region
option_frame_options_forosh_bagh_zamin=tk.Frame(forosh_bagh_zamin,width=300,height=30,background="#052340")
option_frame_options_forosh_bagh_zamin.place(x=525,y=450)

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

bg_image = Image.open("santa-monica-pier-5k-8m-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_forosh_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

karbary_zamin_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10)
karbary_zamin_forosh_bagh_zamin.place(x=463, y=40)

karbary_zamin_forosh_bagh_zamin_combo=ttk.Combobox(option_file_frame_forosh_bagh_zamin,state="readonly")
karbary_zamin_forosh_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbary_zamin_forosh_bagh_zamin_combo.set("باغ")
karbary_zamin_forosh_bagh_zamin_combo["state"]=["readonly"]
karbary_zamin_forosh_bagh_zamin_combo.place(x=273, y=40)

karbary_zamin_forosh_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_forosh_bagh)

metraj_derakht_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_derakht_forosh_bagh_zamin_lable.place(x=450, y=70)

metraj_derakht_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_derakht_forosh_bagh_zamin_entry.place(x=305, y=70)

tedad_derakht_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tedad_derakht_forosh_bagh_zamin_lable.place(x=460, y=100)

tedad_derakht_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tedad_derakht_forosh_bagh_zamin_entry.place(x=305, y=100)

abyari_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع ابیاری")
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
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_forosh_bagh_zamin_combo["state"]=["readonly"]
type_tree_forosh_bagh_zamin_combo.set("گردو")
type_tree_forosh_bagh_zamin_combo.place(x=273, y=160)

type_tree_forosh_btn=tk.Button(option_file_frame_forosh_bagh_zamin,text="افزودن درخت",command=add_tree2,bg="#00BFFF",font=("Shabnam",9),width=10)
type_tree_forosh_btn.place(x=460, y=190)

label_natige_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,text="")
label_natige_forosh_bagh_zamin.place(x=305, y=190)

chah_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
chah_forosh_bagh_zamin.place(x=480, y=220)

estakhr_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="استخر",background="#052340",fg="#00BFFF",font=("Shabnam",9))
estakhr_forosh_bagh_zamin.place(x=380, y=220)

loleh_keshi_ab_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="اب لوله کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
loleh_keshi_ab_forosh_bagh_zamin.place(x=280, y=220)

bargh_keshi_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="برق کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_forosh_bagh_zamin.place(x=180, y=220)

gas_keshi_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="گاز کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
gas_keshi_forosh_bagh_zamin.place(x=80, y=220)


var0_forosh_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

otagh_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,variable=var0,image=warehouse_pic,background="#052340",text="ساختمان",command=home_true_false2)
otagh_check_btn_forosh_bagh_zamin.place(x=470, y=250)

metraj_vila_forosh_bagh_zamin=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ سازه")
metraj_vila_forosh_bagh_zamin.place(x=450, y=300)

metraj_vila_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000",state="disabled")
metraj_vila_forosh_bagh_zamin_entry.place(x=305, y=300)

sal_sakht_vila_forosh_bagh_zamin_lable=tk.Label(option_file_frame_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سال ساخت")
sal_sakht_vila_forosh_bagh_zamin_lable.place(x=450, y=330)

sal_sakht_vila_forosh_bagh_zamin_entry=tk.Entry(option_file_frame_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000",state="disabled")
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

mojavez_sakht_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_check_btn_forosh_bagh_zamin.place(x=450, y=510)

mohavate_sazi_check_btn_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_sazi_check_btn_forosh_bagh_zamin.place(x=320, y=510)

divar_forosh_bagh_zamin=tk.Checkbutton(option_file_frame_forosh_bagh_zamin,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_forosh_bagh_zamin.place(x=180, y=510)

zakhire_options_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_forosh_bagh_zamin.place(x=95,y=580)

back_to_forosh_bagh_zamin=tk.Button(option_file_frame_forosh_bagh_zamin,text="بازگشت",command=back_to_forosh_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_forosh_bagh_zamin.place(x=215,y=580)

option_file_frame_forosh_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_bagh_zamin.resizable(False, False)
#endregion
#-------------------------تعویض کاربری به زمین در قسمت فروش باغ/زمین-------------
#region
option_frame_option2_forosh_bagh_zamin=tk.Frame(option_file_frame_forosh_bagh_zamin,width=445,height=290,background="#052340")
option_frame_option2_forosh_bagh_zamin.place_forget()

metraj_zamin2_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin2_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin2_forosh_bagh_zamin_entry=tk.Entry(option_frame_option2_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin2_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

karbari_forosh_bagh_zamin_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_forosh_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

karbari_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
karbari_forosh_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")        
karbari_forosh_bagh_zamin_combo["state"]=["readonly"]                        
karbari_forosh_bagh_zamin_combo.set(" ")
karbari_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_forosh_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
khak_forosh_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")       
khak_forosh_bagh_zamin_combo["state"]=["readonly"]                         
khak_forosh_bagh_zamin_combo.set(" ")
khak_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع اب")
ab_forosh_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
ab_forosh_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")    
ab_forosh_bagh_zamin_combo["state"]=["readonly"]                            
ab_forosh_bagh_zamin_combo.set(" ")
ab_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_forosh_bagh_zamin_forosh_lable=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="توپوگرافی")
zamin_shekl_forosh_bagh_zamin_forosh_lable.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
zamin_shekl_forosh_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")   
zamin_shekl_forosh_bagh_zamin_combo["state"]=["readonly"]                          
zamin_shekl_forosh_bagh_zamin_combo.set(" ")
zamin_shekl_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo2_button_forosh_bagh_zamin=tk.Button(option_frame_option2_forosh_bagh_zamin,text=" مورد دلخواه",command=add_topo2,bg="#00BFFF",font=("Shabnam",9),width=10)
add_topo2_button_forosh_bagh_zamin.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,text="")
label_natige_topo_add_forosh_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_forosh_bagh_zamin=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="سطح زیر کشت")
kesht_forosh_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_forosh_bagh_zamin_combo=ttk.Combobox(option_frame_option2_forosh_bagh_zamin)
kesht_forosh_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_forosh_bagh_zamin_combo.set("بدون کشت ")
kesht_forosh_bagh_zamin_combo["state"]=["readonly"]   
kesht_forosh_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_forosh_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht2)

kesht_forosh_bagh_zamin_label=tk.Label(option_frame_option2_forosh_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=11,text="محصول زیرکشت")
kesht_forosh_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_forosh_bagh_zamin_entry=tk.Entry(option_frame_option2_forosh_bagh_zamin,width=10,bg="#746f6f",fg="#000000",state="disabled")
kesht_forosh_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_kesi_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_kesi_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_keshi_zamin_forosh_bagh_zamin2=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_zamin_forosh_bagh_zamin2.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه ساخت گلخانه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_golkhane_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavez_chah_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_chah_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="حق برداشت ",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bardasht_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_forosh_bagh_zamin=tk.Checkbutton(option_frame_option2_forosh_bagh_zamin,text="اجازه ورود دام",background="#052340",fg="#00BFFF",font=("Shabnam",9))
dam_zamin_forosh_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)
#endregion
#-------------------پنجره فروش کارگاه------------------------
#region
forosh_karghah = tk.Toplevel(root)
forosh_karghah.title(" فروش کارگاه")
forosh_karghah.geometry("800x600")
forosh_karghah.withdraw()

bg_image = Image.open("dubai-cityscape-buildings-lights-8k-ar-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
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

lable_forosh_kargah=tk.Label(forosh_karghah,text=" کارگاه ",bg="#ffffff",fg="#000000",font=("Shabnam", 10),width=20)
lable_forosh_kargah.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

metraj_forosh_kargah=tk.Label(forosh_karghah,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
metraj_forosh_kargah.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

loctaion_forosh_kargah=tk.Label(forosh_karghah,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=10)
loctaion_forosh_kargah.place(x=start_x + 320, y=start_y + 135, anchor="e")

loctaion_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
loctaion_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

mablagh_pish_forosh_kargah=tk.Label(forosh_karghah,text='ودیعه',bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
mablagh_pish_forosh_kargah.place(x=start_x + 320, y=start_y + 185, anchor="e")

mablagh_pish_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
mablagh_pish_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

gheimat_har_metr_forosh_kargah=tk.Label(forosh_karghah,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
gheimat_har_metr_forosh_kargah.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_har_metr_forosh_kargah_entry=tk.Entry(forosh_karghah,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_forosh_kargah_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

time_ejare_forosh_kargah=tk.Label(forosh_karghah,text="مدت اجاره",bg="#052340",fg="#ffffff",font=("Shabnam", 12),width=9)
time_ejare_forosh_kargah.place(x=start_x + 320, y=start_y + 285, anchor="e")

time_ejare_forosh_kargah_combo=ttk.Combobox(forosh_karghah,state="readonly")
time_ejare_forosh_kargah_combo["values"]=("بلندمدت","کوتاه مدت","فصلی","سالانه")
time_ejare_forosh_kargah_combo.set("فصلی")
time_ejare_forosh_kargah_combo.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

photo_lbl2_forosh_kargah = tk.Label(forosh_karghah, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_forosh_kargah.place(x=60, y=85)

add_img_btn_forosh_kargah = tk.Button(forosh_karghah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_forosh_kargah.place(x=60, y=370)

back_to_home_forosh_kargah=tk.Button(forosh_karghah,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_forosh_karghah)
back_to_home_forosh_kargah.place(x=290,y=520)

zakhire_forosh_kargah=tk.Button(forosh_karghah,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=save_forosh_karghah)
zakhire_forosh_kargah.place(x=140,y=520)

forosh_karghah.protocol("WM_DELETE_WINDOW", lambda: None)
forosh_karghah.resizable(False, False)
#endregion
#---------------------پنجره امکانات فروش کارگاه---------------------
#region
option_frame_forosh_kargah=tk.Frame(forosh_karghah,width=300,height=30,background="#052340")
option_frame_forosh_kargah.place(x=550,y=450)

option_frame_lable_forosh_kargah=tk.Label(option_frame_forosh_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_lable_forosh_kargah.pack(side="right",padx=1)

plus_button_forosh_kargah=tk.Button(option_frame_forosh_kargah,image=plus,command=open_option8,border=0)
plus_button_forosh_kargah.pack()

option_file_frame_forosh_kargah=tk.Toplevel(forosh_karghah,background="#052340")
option_file_frame_forosh_kargah.title(" امکانات فروش کارگاه")
option_file_frame_forosh_kargah.geometry("500x500")
option_file_frame_forosh_kargah.pack_propagate(False)
option_file_frame_forosh_kargah.withdraw()

bg_image = Image.open("dubai-cityscape-buildings-lights-8k-ar-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
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
vaziat_bargh_forosh_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_forosh_kargah_combo.set("برق شهری")
vaziat_bargh_forosh_kargah_combo["state"]=["readonly"]
vaziat_bargh_forosh_kargah_combo.place(x=70, y=80)

garmayesh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_forosh_kargah.place(x=295, y=110)

garmayesh_type_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
garmayesh_type_forosh_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_forosh_kargah_combo.set(" بخاری")
garmayesh_type_forosh_kargah_combo["state"]=["readonly"]
garmayesh_type_forosh_kargah_combo.place(x=70, y=110)

sarmayesh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_forosh_kargah.place(x=295, y=140)

sarmayesh_fan_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="تهویه(فن)",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_forosh_kargah.place(x=295, y=170)

sarmayesh_panke_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="پنکه سقفی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_forosh_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="کولر آبی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_forosh_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_forosh_kargah=tk.Checkbutton(option_file_frame_forosh_kargah,text="کولر گازی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_forosh_kargah.place(x=84, y=200)

vaziat_ab_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text=" وضعیت آب")
vaziat_ab_forosh_kargah.place(x=303, y=230)

vaziat_ab_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah,width=35)
vaziat_ab_forosh_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_forosh_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_forosh_kargah_combo["state"]=["readonly"]
vaziat_ab_forosh_kargah_combo.place(x=30, y=230)

abzar_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_forosh_kargah.place(x=298, y=260)

abzarforosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah,width=23)
abzarforosh_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzarforosh_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzarforosh_kargah_combo["state"]=["readonly"]
abzarforosh_kargah_combo.place(x=58, y=260)

toilet_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_forosh_kargah.place(x=298, y=290)

toilet_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
toilet_forosh_kargah_combo["values"]=("دارد","ندارد")
toilet_forosh_kargah_combo.set("دارد")
toilet_forosh_kargah_combo["state"]=["readonly"]
toilet_forosh_kargah_combo.place(x=70, y=290)

hamam_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_forosh_kargah.place(x=303, y=320)

hamam_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
hamam_forosh_kargah_combo["values"]=("ندارد","دارد")
hamam_forosh_kargah_combo.set("ندارد")
hamam_forosh_kargah_combo["state"]=["readonly"]
hamam_forosh_kargah_combo.place(x=70, y=320)

otagh_forosh_kargah=tk.Label(option_file_frame_forosh_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_forosh_kargah.place(x=294, y=350)

otagh_forosh_kargah_combo=ttk.Combobox(option_file_frame_forosh_kargah)
otagh_forosh_kargah_combo["values"]=("ندارد","دارد")
otagh_forosh_kargah_combo.set("ندارد")
otagh_forosh_kargah_combo["state"]=["readonly"]
otagh_forosh_kargah_combo.place(x=70, y=350)

zakhire_options_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_forosh_kargah.place(x=50,y=450)

back_to_forosh_kargah=tk.Button(option_file_frame_forosh_kargah,text="بازگشت",command=back_to_forosh_karghah,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_forosh_kargah.place(x=170,y=450)

option_file_frame_forosh_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_forosh_kargah.resizable(False, False)
#endregion
#--------------------پنجره های ثبتی بخش خرید-----------------------
#----------------------پنجره خرید مسکونی--------------------------
#region
kharid_maskoni_page = tk.Toplevel(root)
kharid_maskoni_page.title("خرید مسکونی")
kharid_maskoni_page.geometry("800x600")
kharid_maskoni_page.withdraw()

bg_image = Image.open("evening-houses-skyscrapers-qatar-5k-g2-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(kharid_maskoni_page, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#---------------------پنجره امکانات خرید مسکونی----------------------
option_file_frame_kharid_maskoni=tk.Toplevel(kharid_maskoni_page)
option_file_frame_kharid_maskoni.title(" امکانات خرید مسکونی")
option_file_frame_kharid_maskoni.geometry("500x370")
option_file_frame_kharid_maskoni.pack_propagate(False)
option_file_frame_kharid_maskoni.withdraw()

#------------------کادر خرید مسکونی-----------------------------#
frame_kharid_maskoni= tk.Frame(kharid_maskoni_page,bd=0,highlightthickness=0)
frame_kharid_maskoni.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(kharid_maskoni_page,text="خرید مسکونی",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)   

# تعیین نقطه شروع (جایی که فریم قبلی قرار داشت)
start_x = 450
start_y = 40

melk_type_kharid_maskoni=tk.Label(kharid_maskoni_page,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_kharid_maskoni.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,text="خرید مسکونی",bg="#C2C2C2", fg="#180202",font=("Shabnam", 10),justify="center")
melk_type_kharid_maskoni_entry.insert(0,"خرید مسکونی")
melk_type_kharid_maskoni_entry.config(state="disable")
melk_type_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

sal_sakht_kharid_maskoni=tk.Label(kharid_maskoni_page,text="سال ساخت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
sal_sakht_kharid_maskoni.place(x=start_x + 320, y=start_y + 85, anchor="e")

sal_sakht_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
sal_sakht_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

addrres_kharid_maskoni=tk.Label(kharid_maskoni_page,text="آدرس",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
addrres_kharid_maskoni.place(x=start_x + 320, y=start_y + 135, anchor="e")

addrres_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
addrres_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

tabaghe_kharid_maskoni=tk.Label(kharid_maskoni_page,text="طبقه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
tabaghe_kharid_maskoni.place(x=start_x + 320, y=start_y + 185, anchor="e")

tabaghe_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
tabaghe_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

vahed_kharid_maskoni=tk.Label(kharid_maskoni_page,text="واحد",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
vahed_kharid_maskoni.place(x=start_x + 320, y=start_y + 235, anchor="e")

vahed_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
vahed_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

otagh_kharid_maskoni=tk.Label(kharid_maskoni_page,text="اتاق",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
otagh_kharid_maskoni.place(x=start_x + 320, y=start_y + 285, anchor="e")

otagh_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
otagh_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

gheimat_kharid_maskoni=tk.Label(kharid_maskoni_page,text="قیمت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
gheimat_kharid_maskoni.place(x=start_x + 320, y=start_y + 340, anchor="e")

gheimat_kharid_maskoni_entry=tk.Entry(kharid_maskoni_page,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
gheimat_kharid_maskoni_entry.place(x=start_x + 10, y=start_y + 330, width=150, height=25)

back_to_home_kharid_maskoni=tk.Button(kharid_maskoni_page,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_kharid_maskoni)
back_to_home_kharid_maskoni.place(x=270,y=520)

zakhire_kharid_maskoni=tk.Button(kharid_maskoni_page,text="ذخیره",bg="#00BFFF",fg="black",width=10,height=2,command=save_forosh_maskkoni)
zakhire_kharid_maskoni.place(x=120,y=520)

photo_lbl2_kharid_maskoni = tk.Label(kharid_maskoni_page, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_kharid_maskoni.place(x=60, y=85)

add_img_btn_kharid_maskoni = tk.Button(kharid_maskoni_page, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_kharid_maskoni.place(x=60, y=370)

kharid_maskoni_page.protocol("WM_DELETE_WINDOW", lambda: None)
kharid_maskoni_page.resizable(False, False)
#endregion
#------------------------امکانات خرید مسکونی--------------------
#region
option_frame_options_kharid_maskoni=tk.Frame(kharid_maskoni_page,width=300,height=30,background="#052340")
option_frame_options_kharid_maskoni.place(x=520,y=460)

option_label_kharid_maskoni=tk.Label(option_frame_options_kharid_maskoni,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_kharid_maskoni.pack(side="right",padx=1)

plus_button_kharid_maskoni=tk.Button(option_frame_options_kharid_maskoni,image=plus,command=open_option9,border=0)
plus_button_kharid_maskoni.pack()

bg_image = Image.open("evening-houses-skyscrapers-qatar-5k-g2-1920x1200.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_kharid_maskoni, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_ch_btn_kharid_maskoni=tk.Checkbutton(option_file_frame_kharid_maskoni,image=parking_pic,background="#052340")
parking_ch_btn_kharid_maskoni.place(x=140, y=50)

asansor_ch_btn_kharid_maskoni=tk.Checkbutton(option_file_frame_kharid_maskoni,image=elvator_pic,background="#052340")
asansor_ch_btn_kharid_maskoni.place(x=240, y=50)

anbari_checkbuton_kharid_maskoni=tk.Checkbutton(option_file_frame_kharid_maskoni,image=warehouse_pic,background="#052340")
anbari_checkbuton_kharid_maskoni.place(x=340, y=50)

sarmaesh_kharid_maskoni=tk.Label(option_file_frame_kharid_maskoni,text="سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
sarmaesh_kharid_maskoni.place(x=320, y=110)

sarmaesh_combo_kharid_maskoni=ttk.Combobox(option_file_frame_kharid_maskoni)
sarmaesh_combo_kharid_maskoni["values"] = ("ندارد","پنکه سقفی","کولر ابی","کولر گازی ","ابی/گازی")
sarmaesh_combo_kharid_maskoni["state"]=["readonly"]
sarmaesh_combo_kharid_maskoni.place(x=120, y=110)

garmaesh_kharid_maskoni=tk.Label(option_file_frame_kharid_maskoni,text="گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11))
garmaesh_kharid_maskoni.place(x=320, y=150)

garmaesh_combo_kharid_maskoni=ttk.Combobox(option_file_frame_kharid_maskoni)
garmaesh_combo_kharid_maskoni["values"] = ("ندارد","بخاری"," شوفاژ","گرمایش از کف ")
garmaesh_combo_kharid_maskoni["state"]=["readonly"]
garmaesh_combo_kharid_maskoni.place(x=120, y=150)

kaf_kharid_maskoni=tk.Label(option_file_frame_kharid_maskoni,text="کف",background="#052340",fg="#ffffff",font=("Shabnam",11))
kaf_kharid_maskoni.place(x=320, y=190)

kaf_combo_kharid_maskoni=ttk.Combobox(option_file_frame_kharid_maskoni)
kaf_combo_kharid_maskoni["state"]=["readonly"]
kaf_combo_kharid_maskoni["values"] = ("سرامیک","موزاییک","پارکت")
kaf_combo_kharid_maskoni.place(x=120, y=190)

toilet_kharid_maskoni=tk.Label(option_file_frame_kharid_maskoni,text="سرویس بهداشتی",background="#052340",fg="#ffffff",font=("Shabnam",11))
toilet_kharid_maskoni.place(x=320, y=230)

toilet_combo_kharid_maskoni=ttk.Combobox(option_file_frame_kharid_maskoni)
toilet_combo_kharid_maskoni["state"]=["readonly"]
toilet_combo_kharid_maskoni["values"] = ("ایرانی","فرنگی","هردو")
toilet_combo_kharid_maskoni.place(x=120, y=230)

zakhire_options_kharid_maskini=tk.Button(option_file_frame_kharid_maskoni,text="ذخیره",command=None,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_kharid_maskini.place(x=95, y=320)

back_to_home_kharid_maskoni=tk.Button(option_file_frame_kharid_maskoni,text="بازگشت",command=back_to_kharid_maskoni_page,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_kharid_maskoni.place(x=215, y=320)

option_file_frame_kharid_maskoni.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_kharid_maskoni.resizable(False, False)
#endregion
#-----------------پنجره خرید اداری/تجاری-------------------
#region
kharid_edari_tejari = tk.Toplevel(root)
kharid_edari_tejari.title(" خرید اداری / تجاری")
kharid_edari_tejari.geometry("800x600")
kharid_edari_tejari.withdraw()

bg_image = Image.open("paris-beautiful-city-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

# لیبل پس‌زمینه
bg_label = tk.Label(kharid_edari_tejari, image=bg_photo)
bg_label.image = bg_photo  # خیلی مهم: جلوگیری از پاک شدن عکس
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------پنجره امکانات خرید اداری/تجاری----------------

option_file_frame_kharid_edari_tejari=tk.Toplevel(kharid_edari_tejari,background="#052340" )
option_file_frame_kharid_edari_tejari.title(" امکانات خرید اداری/تجاری")
option_file_frame_kharid_edari_tejari.geometry("500x370")
option_file_frame_kharid_edari_tejari.pack_propagate(False)
option_file_frame_kharid_edari_tejari.withdraw()

#----------------------کادر خرید اداری و تجاری------------------#
frame_kharid_edari_tejari= tk.Frame(kharid_edari_tejari,bd=0,highlightthickness=0)
frame_kharid_edari_tejari.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(kharid_edari_tejari,text="خرید اداری و تجاری",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

melk_type_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),justify="center")
melk_type_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_kharid_edari_tejari_entry.insert(0,"اجاره اداری و تجاری")
melk_type_kharid_edari_tejari_entry.config(state="disable")

melk_type_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="متراژ ملک ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
melk_type_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

melk_type_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
melk_type_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

sal_sakht_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="سال ساخت",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
sal_sakht_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

sal_sakht_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
sal_sakht_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

addrres_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="آدرس",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
addrres_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

addrres_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
addrres_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

tabaghe_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="طبقه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
tabaghe_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

tabaghe_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
tabaghe_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

vahed_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="واحد",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
vahed_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

vahed_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
vahed_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)


mablagh_pish_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text="مبلغ ودیعه",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_pish_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 335, anchor="e")

mablagh_pish_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
mablagh_pish_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 325, width=150, height=25)

mablagh_ejare_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text=" مبلغ اجاره",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
mablagh_ejare_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 385, anchor="e")

mablagh_ejare_kharid_edari_tejari_entry=tk.Entry(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10),)
mablagh_ejare_kharid_edari_tejari_entry.place(x=start_x + 10, y=start_y + 375, width=150, height=25)

rahn_kamel_kharid_edari_tejari_lable=tk.Label(kharid_edari_tejari,text=" رهن کامل؟ ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=9)
rahn_kamel_kharid_edari_tejari_lable.place(x=start_x + 320, y=start_y + 435, anchor="e")

rahn_kamel_check_btn_kharid_edari_tejari=tk.Checkbutton(kharid_edari_tejari,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
rahn_kamel_check_btn_kharid_edari_tejari.place(x=start_x + 10, y=start_y + 425)

back_to_home_kharid_edari_tejari=tk.Button(kharid_edari_tejari,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_kharid_edari_tejari)
back_to_home_kharid_edari_tejari.place(x=280,y=520)

zakhire_kharid_edari_tejari=tk.Button(kharid_edari_tejari,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=None)
zakhire_kharid_edari_tejari.place(x=130,y=520)

photo_lbl2_kharid_edari_tejari = tk.Label(kharid_edari_tejari, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_kharid_edari_tejari.place(x=60, y=85)

add_img_btn_kharid_edari_tejari = tk.Button(kharid_edari_tejari, text="افزودن تصویر", bg="#00BFFF", fg="#000000",command=open_file,height=2,width=13)
add_img_btn_kharid_edari_tejari.place(x=60, y=370)

kharid_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
kharid_edari_tejari.resizable(False, False)
#endregion
#---------------امکانات خرید اداری/تجاری-------------------
#region
option_frame_options_kharid_edari_tejari=tk.Frame(kharid_edari_tejari,width=300,height=30,background="#052340")
option_frame_options_kharid_edari_tejari.place(x=250,y=373)

option_label_kharid_edari_tejari=tk.Label(option_frame_options_kharid_edari_tejari,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_kharid_edari_tejari.pack(side="right",padx=1)

plus_button_kharid_eedari_tejari=tk.Button(option_frame_options_kharid_edari_tejari,image=plus,command=open_option10,border=0)
plus_button_kharid_eedari_tejari.pack()

bg_image = Image.open("paris-beautiful-city-1920x1200.jpg")
bg_image = bg_image.resize((800, 380))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_kharid_edari_tejari, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

parking_check_btn_kharid_edari_tejari=tk.Checkbutton(option_file_frame_kharid_edari_tejari,image=parking_pic,background="#052340")
parking_check_btn_kharid_edari_tejari.place(x=140, y=50)

asansor_check_btn_kharid_edari_tejari=tk.Checkbutton(option_file_frame_kharid_edari_tejari,image=elvator_pic,background="#052340")
asansor_check_btn_kharid_edari_tejari.place(x=240, y=50)

anbari_check_btn_kharid_edari_tejari=tk.Checkbutton(option_file_frame_kharid_edari_tejari,image=warehouse_pic,background="#052340")
anbari_check_btn_kharid_edari_tejari.place(x=340, y=50)

aab_va_gaz_emkanat_kharid_edari_tejari=tk.Label(option_file_frame_kharid_edari_tejari,text="وضعیت آب و گاز",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
aab_va_gaz_emkanat_kharid_edari_tejari.place(x=320, y=110)

aab_va_gaz_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_file_frame_kharid_edari_tejari)
aab_va_gaz_combo_emkanat_kharid_edari_tejari["values"] = ("فقط گاز دارد","فقط آب دارد","آب و گاز دارد")
aab_va_gaz_combo_emkanat_kharid_edari_tejari["state"]=["readonly"]
aab_va_gaz_combo_emkanat_kharid_edari_tejari.place(x=120, y=110)

sarmayesh_emkanat_kharid_edari_tejari=tk.Label(option_file_frame_kharid_edari_tejari,text="سیستم سرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
sarmayesh_emkanat_kharid_edari_tejari.place(x=320, y=150)

sarmayesh_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_file_frame_kharid_edari_tejari)
sarmayesh_combo_emkanat_kharid_edari_tejari["values"] = (" کولر گازی"," کولرآبی","پنکه سقفی","ندارد")
sarmayesh_combo_emkanat_kharid_edari_tejari["state"]=["readonly"]
sarmayesh_combo_emkanat_kharid_edari_tejari.place(x=120, y=150)

garmayesh_emkanat_kharid_edari_tejari=tk.Label(option_file_frame_kharid_edari_tejari,text="سیستم گرمایش",background="#052340",fg="#ffffff",font=("Shabnam",11),width=17)
garmayesh_emkanat_kharid_edari_tejari.place(x=320, y=190)

garmayesh_combo_emkanat_kharid_edari_tejari=ttk.Combobox(option_file_frame_kharid_edari_tejari)
garmayesh_combo_emkanat_kharid_edari_tejari["values"] = (" شوفاژ"," بخاری","ندارد")
garmayesh_combo_emkanat_kharid_edari_tejari["state"]=["readonly"]
garmayesh_combo_emkanat_kharid_edari_tejari.place(x=120, y=190)

zakhire_options_kharid_edari_tejari=tk.Button(option_file_frame_kharid_edari_tejari,text="ذخیره",command=None,background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_kharid_edari_tejari.place(x=95,y=320)

back_to_home_kharid_edari_tejari=tk.Button(option_file_frame_kharid_edari_tejari,text="بازگشت",command=back_to_kharid_edari_tejari,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_home_kharid_edari_tejari.place(x=215,y=320)

option_file_frame_kharid_edari_tejari.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_kharid_edari_tejari.resizable(False, False)
#endregion
#--------------------پنجره خرید باغ/زمین-----------------------
#region
kharid_bagh_zamin = tk.Toplevel(root)
kharid_bagh_zamin.title("خرید باغ و زمین")
kharid_bagh_zamin.geometry("800x600")
kharid_bagh_zamin.withdraw()

bg_image = Image.open("vilnius-cityscape-4k-el-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(kharid_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#---------------------کادر خرید باغ و زمین---------------------#
frame_kharid_bagh_zamin= tk.Frame(kharid_bagh_zamin,bd=0,highlightthickness=0)
frame_kharid_bagh_zamin.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(kharid_bagh_zamin,text="خرید باغ و زمین",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40


melk_type_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text="نوع ملک",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
melk_type_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 35, anchor="e")

melk_type_kharid_bagh_zamin_entry=tk.Entry(kharid_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10),justify="center")
melk_type_kharid_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 25, width=150, height=25)
melk_type_kharid_bagh_zamin_entry.insert(0,"خرید باغ و زمین")
melk_type_kharid_bagh_zamin_entry.config(state="disable")

metraj_zamin_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
metraj_zamin_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_zamin_kharid_bagh_zamin_entry=tk.Entry(kharid_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_zamin_kharid_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

bagh_type_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
bagh_type_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

bagh_type_kharid_bagh_zamin_combo=ttk.Combobox(kharid_bagh_zamin,state="readonly")
bagh_type_kharid_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
bagh_type_kharid_bagh_zamin_combo.set("باغ")
bagh_type_kharid_bagh_zamin_combo.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

bagh_loctaion_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
bagh_loctaion_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

bagh_loctaion_kharid_bagh_zamin_entry=tk.Entry(kharid_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
bagh_loctaion_kharid_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

gheimat_bagh_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text='قیمت کل',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_bagh_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_bagh_kharid_bagh_zamin_entry=tk.Entry(kharid_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_bagh_kharid_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

gheimat_har_matr_babagh_zamin_kharid_bagh_zamin_lable=tk.Label(kharid_bagh_zamin,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_har_matr_babagh_zamin_kharid_bagh_zamin_lable.place(x=start_x + 320, y=start_y + 285, anchor="e")

gheimat_har_metr_babagh_zamin_kharid_bagh_zamin_entry=tk.Entry(kharid_bagh_zamin,bg="#ffffff", fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_babagh_zamin_kharid_bagh_zamin_entry.place(x=start_x + 10, y=start_y + 275, width=150, height=25)

photo_kharid_bagh_zamin_lable= tk.Label(kharid_bagh_zamin, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_kharid_bagh_zamin_lable.place(x=60, y=85)
add_img_btn_kharid_bagh_zamin = tk.Button(kharid_bagh_zamin, text="افزودن تصویر", bg="#00BFFF", fg="#000000",command=open_file,height=2,width=13)
add_img_btn_kharid_bagh_zamin.place(x=60, y=370)

back_to_home_kharid_bagh_zamin=tk.Button(kharid_bagh_zamin,text="بازگشت",bg="#00BFFF", fg="#000000",width=10,height=2,command=back_home_kharid_bagh)
back_to_home_kharid_bagh_zamin.place(x=290,y=520)

zakhire_kharid_bagh_zamin=tk.Button(kharid_bagh_zamin,text="ذخیره",bg="#00BFFF", fg="#000000",width=10,height=2,command=None)
zakhire_kharid_bagh_zamin.place(x=140,y=520)

kharid_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
kharid_bagh_zamin.resizable(False, False)
#endregion
#-----------------------پنجره امکانات خرید باغ/زمین-------------------
#region
option_frame_options_kharid_bagh_zamin=tk.Frame(kharid_bagh_zamin,width=300,height=30,background="#052340")
option_frame_options_kharid_bagh_zamin.place(x=525,y=450)

option_label_kharid_bagh_zamin=tk.Label(option_frame_options_kharid_bagh_zamin,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_label_kharid_bagh_zamin.pack(side="right",padx=1)

plus_button_kharid_bagh_zamin=tk.Button(option_frame_options_kharid_bagh_zamin,image=plus,command=open_option11,border=0)
plus_button_kharid_bagh_zamin.pack()

option_file_frame_kharid_bagh_zamin=tk.Toplevel(kharid_bagh_zamin)
option_file_frame_kharid_bagh_zamin.title(" امکانات خرید باغ/زمین")
option_file_frame_kharid_bagh_zamin.geometry("690x630")
option_file_frame_kharid_bagh_zamin.pack_propagate(False)
option_file_frame_kharid_bagh_zamin.withdraw()

option_frame_kharid_bagh_zamin=tk.Frame(option_file_frame_kharid_bagh_zamin)
option_frame_kharid_bagh_zamin.place(x=50,y=50)

bg_image = Image.open("vilnius-cityscape-4k-el-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_kharid_bagh_zamin, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

karbary_zamin_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10)
karbary_zamin_kharid_bagh_zamin.place(x=463, y=40)

karbary_zamin_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="readonly")
karbary_zamin_kharid_bagh_zamin_combo["values"]=("باغ","زمین کشاورزی")
karbary_zamin_kharid_bagh_zamin_combo.set("باغ")
karbary_zamin_kharid_bagh_zamin_combo.place(x=273, y=40)

karbary_zamin_kharid_bagh_zamin_combo.bind("<<ComboboxSelected>>",change_bagh_zamin_kharid_bagh)

metraj_derakht_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ درخت کاری")
metraj_derakht_kharid_bagh_zamin_lable.place(x=450, y=70)

metraj_derakht_kharid_bagh_zamin_entry=tk.Entry(option_file_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_derakht_kharid_bagh_zamin_entry.place(x=305, y=70)

tedad_derakht_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="تعداد درخت")
tedad_derakht_kharid_bagh_zamin_lable.place(x=460, y=100)

tedad_derakht_kharid_bagh_zamin_entry=tk.Entry(option_file_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
tedad_derakht_kharid_bagh_zamin_entry.place(x=305, y=100)

abyari_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع ابیاری")
abyari_kharid_bagh_zamin_lable.place(x=460, y=130)

abyari_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin)
abyari_kharid_bagh_zamin_combo["values"]=("سطحی","بارانی","قطره ای","تحت فشار")
abyari_kharid_bagh_zamin_combo["state"]=["readonly"]
abyari_kharid_bagh_zamin_combo.set("سطحی")
abyari_kharid_bagh_zamin_combo.place(x=273, y=130)

type_tree_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع درخت")
type_tree_kharid_bagh_zamin_lable.place(x=460, y=160)

type_tree_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin)
type_tree_kharid_bagh_zamin_combo["values"]=(" ","پسته","بادام","گردو","شلیل","هلو","سیب","انگور"
                           ,"انجیر","زردالو","گیلاس","البالو")
type_tree_kharid_bagh_zamin_combo.set("گردو")
type_tree_kharid_bagh_zamin_combo["state"]=["readonly"]
type_tree_kharid_bagh_zamin_combo.place(x=273, y=160)

type_tree_kharid_btn=tk.Button(option_file_frame_kharid_bagh_zamin,text="افزودن درخت",command=add_tree3,bg="#00BFFF",font=("Shabnam",9),width=10)
type_tree_kharid_btn.place(x=460, y=190)

label_natige_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,text="")
label_natige_kharid_bagh_zamin.place(x=305, y=190)

chah_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
chah_kharid_bagh_zamin.place(x=480, y=220)

estakhr_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="استخر",background="#052340",fg="#00BFFF",font=("Shabnam",9))
estakhr_kharid_bagh_zamin.place(x=380, y=220)

loleh_keshi_ab_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="اب لوله کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
loleh_keshi_ab_kharid_bagh_zamin.place(x=280, y=220)

bargh_keshi_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="برق کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_kharid_bagh_zamin.place(x=180, y=220)

gas_keshi_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="گاز کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
gas_keshi_kharid_bagh_zamin.place(x=80, y=220)

var0_kharid_bagh_zamin=tk.IntVar(value=0)#چک باتن پیش فرض تیک نخورده باشه

otagh_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,variable=var0,image=warehouse_pic,background="#052340",text="ساختمان",command=home_true_false3)
otagh_check_btn_kharid_bagh_zamin.place(x=470, y=250)

metraj_vila_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ سازه")
metraj_vila_kharid_bagh_zamin.place(x=450, y=300)

metraj_vila_kharid_bagh_zamin_entry=tk.Entry(option_file_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
metraj_vila_kharid_bagh_zamin_entry.place(x=305, y=300)

sal_sakht_vila_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سال ساخت")
sal_sakht_vila_kharid_bagh_zamin_lable.place(x=450, y=330)

sal_sakht_vila_kharid_bagh_zamin_entry=tk.Entry(option_file_frame_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#ffffff",state="disabled")
sal_sakht_vila_kharid_bagh_zamin_entry.place(x=305, y=330)

type_vila_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="نوع سازه")
type_vila_kharid_bagh_zamin.place(x=450, y=360)

type_vila_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="disabled")
type_vila_kharid_bagh_zamin_combo["values"]=("آجری","بلوکی","کانکس","چوبی")
type_vila_kharid_bagh_zamin_combo.set("آجری")
type_vila_kharid_bagh_zamin_combo.place(x=273, y=360)

toilet_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سرویس بهداشتی")
toilet_kharid_bagh_zamin_lable.place(x=450, y=390)

toilet_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="disabled")
toilet_kharid_bagh_zamin_combo["values"]=(" ","ندارد","فرنگی","ایرانی","هردو")
toilet_kharid_bagh_zamin_combo.set("")
toilet_kharid_bagh_zamin_combo.place(x=273, y=390)

hamam_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="حمام")
hamam_kharid_bagh_zamin.place(x=450, y=420)

hamam_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="disabled")
hamam_kharid_bagh_zamin_combo["values"]=(" ","ندارد","دارد")
hamam_kharid_bagh_zamin_combo.set(" ")
hamam_kharid_bagh_zamin_combo.place(x=273, y=420)

sanad_kharid_bagh_zamin_lable=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="سند")
sanad_kharid_bagh_zamin_lable.place(x=450, y=450)

sanad_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="disabled")
sanad_kharid_bagh_zamin_combo["values"]=(" ","ندارد","تک برگ","قولنامه ای","مشاع")
sanad_kharid_bagh_zamin_combo.set(" ")
sanad_kharid_bagh_zamin_combo.place(x=273, y=450)

option_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="امکانات تفریحی")
option_kharid_bagh_zamin.place(x=450, y=480)

option_kharid_bagh_zamin_combo=ttk.Combobox(option_file_frame_kharid_bagh_zamin,state="disabled")
option_kharid_bagh_zamin_combo["values"]=(" ","استخر","جکوزی","باربیکیو")
option_kharid_bagh_zamin_combo.set(" ")
option_kharid_bagh_zamin_combo.place(x=273, y=480)

add_option_button_kharid_bagh_zamin=tk.Button(option_file_frame_kharid_bagh_zamin,text="افزودن امکانات",command=add_option3,bg="#00BFFF",font=("Shabnam",9),width=10)
add_option_button_kharid_bagh_zamin.place(x=180, y=480)

lable_natige_add_kharid_bagh_zamin=tk.Label(option_file_frame_kharid_bagh_zamin,text="")
lable_natige_add_kharid_bagh_zamin.place(x=100, y=480)

mojavez_sakht_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="مجوز ساختن",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mojavez_sakht_check_btn_kharid_bagh_zamin.place(x=450, y=510)

mohavate_sazi_check_btn_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="محوطه سازی",background="#052340",fg="#00BFFF",font=("Shabnam",9),state="disabled")
mohavate_sazi_check_btn_kharid_bagh_zamin.place(x=320, y=510)

divar_kharid_bagh_zamin=tk.Checkbutton(option_file_frame_kharid_bagh_zamin,text="دیوار کشی",background="#052340",fg="#00BFFF",font=("Shabnam",9))
divar_kharid_bagh_zamin.place(x=180, y=510)

zakhire_options_kharid_bagh_zamin=tk.Button(option_file_frame_kharid_bagh_zamin,command=None,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_kharid_bagh_zamin.place(x=95,y=580)

back_to_kharid_bagh_zamin=tk.Button(option_file_frame_kharid_bagh_zamin,text="بازگشت",command=back_to_kharid_bagh_zamin,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_kharid_bagh_zamin.place(x=215,y=580)

option_file_frame_kharid_bagh_zamin.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_kharid_bagh_zamin.resizable(False, False)
#endregion
#-------------------------تعویض کاربری به زمین در قسمت خرید باغ/زمین-------------
#region
option_frame_option2_kharid_bagh_zamin=tk.Frame(option_file_frame_kharid_bagh_zamin,width=445,height=290,background="#052340")
option_frame_option2_kharid_bagh_zamin.place_forget()

metraj_zamin2_kharid_bagh_zamin_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=13,text="متراژ زمین")
metraj_zamin2_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=0,column=4)

metraj_zamin2_kharid_bagh_zamin_entry=tk.Entry(option_frame_option2_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#000000")
metraj_zamin2_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=0,column=3)

karbari_kharid_bagh_zamin_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع کاربری")
karbari_kharid_bagh_zamin_lable.grid(padx=10,pady=5,row=1,column=4)

karbari_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
karbari_kharid_bagh_zamin_combo["values"]=(" ","زراعی","باغی","گلخانه ای","دامداری ","مرغداری",
                               "دامداری و مرغداری","آیش")           
karbari_kharid_bagh_zamin_combo["state"]=["readonly"]                  
karbari_kharid_bagh_zamin_combo.set(" ")
karbari_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=1,column=3)

khak_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="نوع خاک")
khak_kharid_bagh_zamin.grid(padx=10,pady=5,row=2,column=4)

khak_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
khak_kharid_bagh_zamin_combo["values"]=(" ","رسی","شنی","لومی","رسی_شنی","شنی_لومی",
                               "رسی_لومی")        
khak_kharid_bagh_zamin_combo["state"]=["readonly"]                     
khak_kharid_bagh_zamin_combo.set(" ")
khak_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=2,column=3)

ab_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="منبع اب")
ab_kharid_bagh_zamin.grid(padx=10,pady=5,row=3,column=4)

ab_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
ab_kharid_bagh_zamin_combo["values"]=(" ","چاه","قنات","رودخانه","کانال ابیاری","چشمه",
                               "آب لوله کشی کشاورزی","تانکر","استخر")  
ab_kharid_bagh_zamin_combo["state"]=["readonly"]
ab_kharid_bagh_zamin_combo.set(" ")
ab_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=3,column=3)

zamin_shekl_kharid_bagh_zamin_kharid_lable=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="توپوگرافی")
zamin_shekl_kharid_bagh_zamin_kharid_lable.grid(padx=10,pady=5,row=4,column=4)

zamin_shekl_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
zamin_shekl_kharid_bagh_zamin_combo["values"]=(" "," صاف و یکدست"," شیب دار"," باتلاقی","سنگی ")     
zamin_shekl_kharid_bagh_zamin_combo["state"]=["readonly"]                        
zamin_shekl_kharid_bagh_zamin_combo.set(" ")
zamin_shekl_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=4,column=3)

add_topo2_button_kharid_bagh_zamin=tk.Button(option_frame_option2_kharid_bagh_zamin,text=" مورد دلخواه",command=add_topo3,bg="#00BFFF",font=("Shabnam",9),width=10)
add_topo2_button_kharid_bagh_zamin.grid(padx=10,pady=5,row=4,column=2)
label_natige_topo_add_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,text="")
label_natige_topo_add_kharid_bagh_zamin.grid(padx=10,pady=5,row=4,column=1)

kesht_kharid_bagh_zamin=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=10,text="سطح زیر کشت")
kesht_kharid_bagh_zamin.grid(padx=10,pady=5,row=5,column=4)

kesht_kharid_bagh_zamin_combo=ttk.Combobox(option_frame_option2_kharid_bagh_zamin)
kesht_kharid_bagh_zamin_combo["values"]=("بدون کشت"," زیر کشت")                             
kesht_kharid_bagh_zamin_combo.set("بدون کشت ")
kesht_kharid_bagh_zamin_combo["state"]=["readonly"]
kesht_kharid_bagh_zamin_combo.grid(padx=10,pady=5,row=5,column=3)
kesht_kharid_bagh_zamin_combo.bind("<<ComboboxSelected>>",choos_kesht3)

kesht_kharid_bagh_zamin_label=tk.Label(option_frame_option2_kharid_bagh_zamin,bg="#052340",fg="#ffffff",font=("Shabnam",9),width=11,text="محصول زیرکشت")
kesht_kharid_bagh_zamin_label.grid(padx=10,pady=5,row=5,column=2)

kesht_kharid_bagh_zamin_entry=tk.Entry(option_frame_option2_kharid_bagh_zamin,width=10,bg="#746f6f",fg="#000000",state="disabled")
kesht_kharid_bagh_zamin_entry.grid(padx=10,pady=5,row=5,column=1)

security_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اتاق نگهبان",background="#052340",fg="#00BFFF",font=("Shabnam",9))
security_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=0)

bargh_kesi_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="برق تک فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_kesi_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=1)

bargh_keshi_zamin_kharid_bagh_zamin2=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="برق سه فاز",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bargh_keshi_zamin_kharid_bagh_zamin2.grid(padx=10,pady=6,row=6,column=2)

anbar_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="انبار/سوله",background="#052340",fg="#00BFFF",font=("Shabnam",9))
anbar_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=3)

fans_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="فنس/دیوار",background="#052340",fg="#00BFFF",font=("Shabnam",9))
fans_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=6,column=4)

mojavez_golkhane_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه ساخت گلخانه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_golkhane_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=0)

mojavez_chah_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه حفر چاه",background="#052340",fg="#00BFFF",font=("Shabnam",9))
mojavez_chah_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=1)

bardasht_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="حق برداشت ",background="#052340",fg="#00BFFF",font=("Shabnam",9))
bardasht_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=2)

dam_zamin_kharid_bagh_zamin=tk.Checkbutton(option_frame_option2_kharid_bagh_zamin,text="اجازه ورود دام",background="#052340",fg="#00BFFF",font=("Shabnam",9))
dam_zamin_kharid_bagh_zamin.grid(padx=10,pady=6,row=7,column=3)
#endregion
#-------------------پنجره خرید کارگاه------------------------
#region
kharid_kargah= tk.Toplevel(root)
kharid_kargah.title("خرید کارگاه")
kharid_kargah.geometry("800x600")
kharid_kargah.withdraw()

bg_image = Image.open("monaco-purple-clouds-sunset-1920x1200.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(kharid_kargah, image=bg_photo)
bg_label.image = bg_photo  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#----------------------کادر خرید کارگاه-----------------------#
frame_kharid_kargah=tk.Frame(kharid_kargah,bd=0,highlightthickness=0)
frame_kharid_kargah.pack(side="left", fill="y", padx=6, pady=15)

title_lbl = tk.Label(kharid_kargah,text="خرید کارگاه",bg="#052340",fg="#00BFFF",font=("Shabnam", 15))
title_lbl.place(x=60, y=25)

start_x = 450
start_y = 40

karbari_zamin_kharid_kargah=tk.Label(kharid_kargah,text="کاربری زمین",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
karbari_zamin_kharid_kargah.place(x=start_x + 320, y=start_y + 35, anchor="e")

kharid_kargah_lable=tk.Label(kharid_kargah,text=" کارگاه ",bg="#ffffff",fg="#000000",width=20)
kharid_kargah_lable.place(x=start_x + 10, y=start_y + 25, width=150, height=25)

kharid_kargah_lable=tk.Label(kharid_kargah,text="متراژ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
kharid_kargah_lable.place(x=start_x + 320, y=start_y + 85, anchor="e")

metraj_kharid_kargah_entry=tk.Entry(kharid_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10),textvariable="متر مربع")
metraj_kharid_kargah_entry.place(x=start_x + 10, y=start_y + 75, width=150, height=25)

loctaion_kharid_kargah_lable=tk.Label(kharid_kargah,text="منطقه و آدرس ",bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
loctaion_kharid_kargah_lable.place(x=start_x + 320, y=start_y + 135, anchor="e")

loctaion_kharid_kargah_entry=tk.Entry(kharid_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
loctaion_kharid_kargah_entry.place(x=start_x + 10, y=start_y + 125, width=150, height=25)

mablagh_pish_kharid_kargah_lable=tk.Label(kharid_kargah,text='ودیعه',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
mablagh_pish_kharid_kargah_lable.place(x=start_x + 320, y=start_y + 185, anchor="e")

mablagh_pish_kharid_kargah_entry=tk.Entry(kharid_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
mablagh_pish_kharid_kargah_entry.place(x=start_x + 10, y=start_y + 175, width=150, height=25)

gheimat_har_metr_kharid_kargah_lable=tk.Label(kharid_kargah,text='قیمت هر متر',bg="#052340",fg="#ffffff",font=("Shabnam",12),width=10)
gheimat_har_metr_kharid_kargah_lable.place(x=start_x + 320, y=start_y + 235, anchor="e")

gheimat_har_metr_kharid_kargah_entry=tk.Entry(kharid_kargah,bg="#ffffff",fg="#000000",font=("Shabnam", 10))
gheimat_har_metr_kharid_kargah_entry.place(x=start_x + 10, y=start_y + 225, width=150, height=25)

photo_lbl2_kharid_kargah = tk.Label(kharid_kargah, text="[تصویر ملک]", bg="#ffffff", width=50, height=15)
photo_lbl2_kharid_kargah.place(x=60, y=85)

add_img_btn_kharid_kargah = tk.Button(kharid_kargah, text="افزودن تصویر", bg="#00BFFF", fg="black",command=open_file,height=2,width=13)
add_img_btn_kharid_kargah.place(x=60, y=370)

back_to_home_kharid_kargah=tk.Button(kharid_kargah,text="بازگشت",bg="#00BFFF",fg="#000000",width=10,height=2,command=back_home_kharid_kargah)
back_to_home_kharid_kargah.place(x=290,y=520)

zakhire_kharid_kargah=tk.Button(kharid_kargah,text="ذخیره",bg="#00BFFF",fg="#000000",width=10,height=2,command=save_kharid_karghah)
zakhire_kharid_kargah.place(x=140,y=520)

kharid_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
kharid_kargah.resizable(False, False)
#endregion
#---------------------پنجره امکانات خرید کارگاه---------------------
#region
option_frame_kharid_kargah=tk.Frame(kharid_kargah,width=300,height=30,background="#052340")
option_frame_kharid_kargah.place(x=550,y=450)

option_frame_kharid_kargah_lable=tk.Label(option_frame_kharid_kargah,text='افزودن امکانات فایل',font=("Shabnam",12,"bold"),background="#052340",fg="#00BFFF")
option_frame_kharid_kargah_lable.pack(side="right",padx=1)

plus_button_kharid_kargah=tk.Button(option_frame_kharid_kargah,image=plus,command=open_option12,border=0)
plus_button_kharid_kargah.pack()

option_file_frame_kharid_kargah=tk.Toplevel(kharid_kargah)
option_file_frame_kharid_kargah.title(" امکانات خرید کارگاه")
option_file_frame_kharid_kargah.geometry("500x500")
option_file_frame_kharid_kargah.pack_propagate(False)
option_file_frame_kharid_kargah.withdraw()

option_frame_asli_kharid_kargah=tk.Frame(option_file_frame_kharid_kargah)
option_frame_asli_kharid_kargah.place(x=50,y=50)

bg_image = Image.open("monaco-purple-clouds-sunset-1920x1200.jpg")
bg_image = bg_image.resize((800, 650))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(option_file_frame_kharid_kargah, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


sal_sakht_kharid_kargah_lable=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="سال ساخت")
sal_sakht_kharid_kargah_lable.place(x=302, y=50)

sal_sakht_kharid_kargah_entry=tk.Entry(option_file_frame_kharid_kargah,width=10,bg="#ffffff",fg="#000000")
sal_sakht_kharid_kargah_entry.place(x=108, y=50)

vaziat_bagh_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="وضعیت برق")
vaziat_bagh_kharid_kargah.place(x=295, y=80)

vaziat_bargh_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah)
vaziat_bargh_kharid_kargah_combo["values"]=("برق شهری","سه فاز","تک فاز")
vaziat_bargh_kharid_kargah_combo.set("برق شهری")
vaziat_bargh_kharid_kargah_combo["state"]=["readonly"]
vaziat_bargh_kharid_kargah_combo.place(x=70, y=80)

garmayesh_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم گرمایش")
garmayesh_kharid_kargah.place(x=295, y=110)

garmayesh_type_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah)
garmayesh_type_kharid_kargah_combo["values"]=("بخاری ","شوفاژ ","فن کوئل(گرما) ")
garmayesh_type_kharid_kargah_combo.set(" بخاری")
garmayesh_type_kharid_kargah_combo["state"]=["readonly"]
garmayesh_type_kharid_kargah_combo.place(x=70, y=110)

sarmayesh_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سیستم سرمایش ")
sarmayesh_kharid_kargah.place(x=295, y=140)

sarmayesh_fan_kharid_kargah=tk.Checkbutton(option_file_frame_kharid_kargah,text="تهویه(فن)",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_fan_kharid_kargah.place(x=295, y=170)

sarmayesh_panke_kharid_kargah=tk.Checkbutton(option_file_frame_kharid_kargah,text="پنکه سقفی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_panke_kharid_kargah.place(x=80, y=170)

sarmayesh_kooler_abi_kharid_kargah=tk.Checkbutton(option_file_frame_kharid_kargah,text="کولر آبی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_abi_kharid_kargah.place(x=299, y=200)

sarmayesh_kooler_gazi_kharid_kargah=tk.Checkbutton(option_file_frame_kharid_kargah,text="کولر گازی",background="#052340",fg="#00BFFF",font=("Shabnam", 9))
sarmayesh_kooler_gazi_kharid_kargah.place(x=84, y=200)

vaziat_ab_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",width=13,text=" وضعیت آب",font=("Shabnam", 9))
vaziat_ab_kharid_kargah.place(x=303, y=230)

vaziat_ab_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah,width=35)
vaziat_ab_kharid_kargah_combo["values"]=(" آب مستقیم لوله کشی (بدون فشار) " ," آب مستقیم لوله کشی (همراه موتور فشار) ","دارای منبع(همراه موتور فشار)","دارای منبع(بدون فشار)")
vaziat_ab_kharid_kargah_combo.set(" آب مستقیم لوله کشی (بدون فشار) ")
vaziat_ab_kharid_kargah_combo["state"]=["readonly"]
vaziat_ab_kharid_kargah_combo.place(x=30, y=230)

abzar_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text=" ابزار صنعتی ")
abzar_kharid_kargah.place(x=298, y=260)

abzaar_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah,width=23)
abzaar_kharid_kargah_combo["values"]=("(کارگاه خالی) بدون دستگاه ","دارای دستگاه های تولیدی")
abzaar_kharid_kargah_combo.set("(کارگاه خالی) بدون دستگاه ")
abzaar_kharid_kargah_combo["state"]=["readonly"]
abzaar_kharid_kargah_combo.place(x=58, y=260)

toilet_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=15,text="سرویس بهداشتی")
toilet_kharid_kargah.place(x=298, y=290)

toilet_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah)
toilet_kharid_kargah_combo["values"]=("دارد","ندارد")
toilet_kharid_kargah_combo.set("دارد")
toilet_kharid_kargah_combo["state"]=["readonly"]
toilet_kharid_kargah_combo.place(x=70, y=290)

hamam_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=13,text="حمام")
hamam_kharid_kargah.place(x=303, y=320)

hamam_kharid_kargah__combo=ttk.Combobox(option_file_frame_kharid_kargah)
hamam_kharid_kargah__combo["values"]=("ندارد","دارد")
hamam_kharid_kargah__combo.set("ندارد")
hamam_kharid_kargah__combo["state"]=["readonly"]
hamam_kharid_kargah__combo.place(x=70, y=320)

otagh_kharid_kargah=tk.Label(option_file_frame_kharid_kargah,bg="#052340",fg="#ffffff",font=("Shabnam", 9),width=17,text="اتاق رخت کن و استراحت")
otagh_kharid_kargah.place(x=294, y=350)

otagh_kharid_kargah_combo=ttk.Combobox(option_file_frame_kharid_kargah)
otagh_kharid_kargah_combo["values"]=("ندارد","دارد")
otagh_kharid_kargah_combo.set("ندارد")
otagh_kharid_kargah_combo["state"]=["readonly"]
otagh_kharid_kargah_combo.place(x=70, y=350)

zakhire_options_kharid_kargah=tk.Button(option_file_frame_kharid_kargah,text="ذخیره",background="#00BFFF",fg="#000000",width=10,height=1)
zakhire_options_kharid_kargah.place(x=50,y=450)

back_to_kharid_kargah=tk.Button(option_file_frame_kharid_kargah,text="بازگشت",command=back_to_kharid_kargah,background="#00BFFF",fg="#000000",width=10,height=1)
back_to_kharid_kargah.place(x=170,y=450)

option_file_frame_kharid_kargah.protocol("WM_DELETE_WINDOW", lambda: None)
option_file_frame_kharid_kargah.resizable(False, False)
#endregion
#############################################################################
# ----------------------اجرای برنامه-------------------
#region
root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()
#endregion