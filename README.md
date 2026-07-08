# Class bo'yicha 10 ta vazifa (Junior / Junior-Middle daraja)

## 1-vazifa (Junior) — Oddiy klass
`Person` klassini yarating. `name` va `age` xususiyatlariga ega bo'lsin. `introduce()` metodi orqali "Salom, mening ismim Ali, men 20 yoshdaman" kabi xabar chiqarsin.

## 2-vazifa (Junior) — Konstruktor bilan ishlash
`Book` klassini yarating: `title`, `author`, `price` xususiyatlari bilan. `discount(percent)` metodi narxni foizga kamaytirsin va yangi narxni qaytarsin.

## 3-vazifa (Junior) — `__str__` metodi
`Car` klassi: `brand`, `model`, `year`. `__str__` metodini yozing, shunda `print(car)` chaqirilganda "2020 Toyota Corolla" formatida chiqsin.

## 4-vazifa (Junior) — Metodlar orqali holatni o'zgartirish
`BankAccount` klassi: `balance` (boshlang'ich 0). `deposit(amount)` va `withdraw(amount)` metodlarini yozing. Agar balансdan ko'p pul yechilmoqchi bo'lsa, xatolik xabari chiqsin.

## 5-vazifa (Junior-Middle) — Inheritance (Meros olish)
`Animal` klassini yarating (`name`, `sound()` metodi bilan). Undan `Dog` va `Cat` klasslarini meros oldiring va `sound()` metodini **override** qiling (har biri o'z ovozini chiqarsin).

## 6-vazifa (Junior-Middle) — `super()` bilan ishlash
`Employee` klassi (`name`, `salary`). Undan `Manager` klassini yarating, u qo'shimcha `bonus` xususiyatiga ega bo'lsin. `Manager`ning `__init__` metodida `super().__init__()` orqali ota klass konstruktorini chaqiring.

## 7-vazifa (Junior-Middle) — Encapsulation (Private xususiyatlar)
`Student` klassi yarating, `__grade` (private) xususiyatiga ega bo'lsin. `get_grade()` va `set_grade(value)` metodlari orqali (getter/setter) bahoni o'qish va o'zgartirish imkonini bering. Baho 0-100 oralig'ida bo'lishini tekshiring.

## 8-vazifa (Junior-Middle) — Class va Instance metodlari/xususiyatlari
`Product` klassi yarating. Har bir yangi obyekt yaratilganda `total_products` deb nomlangan **class-level** o'zgaruvchi 1 taga oshsin (nechta mahsulot yaratilganini hisoblash uchun).

## 9-vazifa (Junior-Middle) — Polymorphism (Ko'p qiyofalilik)
`Shape` deb nomlangan bazaviy klass yarating, undan `Circle` va `Rectangle` klasslarini meros oldiring. Har birida `area()` metodi bo'lsin (o'z formulasi bilan). Ro'yxat ichidagi barcha shakllarning yuzasini `for` loop orqali chiqaring.

## 10-vazifa (Junior-Middle) — Abstraction (Abstract class)
`abc` moduli yordamida `PaymentMethod` deb nomlangan **abstract klass** yarating, unda `pay(amount)` abstrakt metodi bo'lsin. Undan `CreditCard` va `CashPayment` klasslarini yarating, har biri `pay()` metodini o'zicha amalga oshirsin.

---

Xohlasangiz, shu vazifalarning **yechimlarini** (kod bilan) ham tayyorlab beray, yoki avval o'zingiz yechib ko'rib, keyin men tekshirib berayinmi?
