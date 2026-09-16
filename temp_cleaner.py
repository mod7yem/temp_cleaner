import os
import shutil
import tkinter as tk
from tkinter import messagebox
import getpass

# الحصول على اسم المستخدم الحالي
user = getpass.getuser()

# المسارات المطلوب تنظيفها
TEMP_FOLDERS = [
    fr"C:\Users\{user}\AppData\Local\Temp",
    r"C:\Windows\Temp"
]

def delete_temp_files():
    total_deleted = 0
    for folder in TEMP_FOLDERS:
        try:
            if not os.path.exists(folder):
                continue

            files = os.listdir(folder)
            for filename in files:
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)
                        total_deleted += 1
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path, ignore_errors=True)
                        total_deleted += 1
                except Exception:
                    continue  # تجاهل الأخطاء
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ في {folder}:\n{e}")
    
    if total_deleted == 0:
        messagebox.showinfo("معلومات", "لم يتم العثور على ملفات لحذفها أو تم حذفها مسبقًا.")
    else:
        messagebox.showinfo("نجاح", f"تم حذف {total_deleted} ملف/مجلد من المسارات المحددة.")

# إنشاء نافذة الواجهة
root = tk.Tk()
root.title("منظف الملفات المؤقتة")
root.geometry("300x250")

# زر الحذف
btn_delete = tk.Button(root, text="حذف الملفات المؤقتة", command=delete_temp_files, font=("Arial", 15))
btn_delete.pack(pady=10)

# زر الخروج باستخدام destroy
btn_exit = tk.Button(root, text="الخروج", command=root.destroy, font=("Arial", 15))
btn_exit.pack(pady=2)

label = tk.Label(root, text="....................................\n (Mohammed_Shammakh)جميع الحقوق محفوظة لدى \n للتواصل:781025592\n....................................",font=("Arial",10))
label.pack(pady=20)

# تشغيل الواجهة
root.mainloop()
