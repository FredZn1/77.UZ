# Onlayn Savdo Platformasi

Ushbu loyiha **onlayn marketplace** bo‘lib, foydalanuvchilar mahsulot qo‘shish, sotish va xarid qilishlari mumkin.  
Tizimda uchta asosiy rol mavjud: **super admin**, **admin** va **sotuvchi**. Har birining vakolatlari aniq belgilangan.  

Platforma keng auditoriyaga mo‘ljallangan bo‘lib, **o‘zbek (lotin)** va **rus** tillarini qo‘llab-quvvatlaydi.

---

## Xususiyatlar
- 🔑 Autentifikatsiya (JWT login, ro‘yxatdan o‘tish, profil tahriri)  
- 👤 Rol asosida huquqlar: super admin, admin, sotuvchi  
- 🛒 Mahsulot boshqaruvi (kategoriya, e’lon, sevimlilar, qidiruv)  
- 🌍 Ikki tilli qo‘llab-quvvatlash (o‘zbekcha, ruscha)  
- 📊 Admin panel orqali boshqaruv  
- 📱 API (pagination, qidiruv, filterlash)  

---

## Talablar
O‘rnatilgan bo‘lishi kerak:
- Python 3.10+
- pip
- virtualenv (ixtiyoriy, lekin tavsiya etiladi)
- PostgreSQL yoki SQLite

---

## O‘rnatish

1. Reponi yuklab oling:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
