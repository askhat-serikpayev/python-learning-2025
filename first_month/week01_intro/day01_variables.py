# 📌 Примеры всех основных типов данных в Python

# 🔢 int — Целые числа
age = 29
count = -5
zero = 0
print("int примеры:", age, count, zero)

# 🌊 float — Числа с плавающей точкой
height = 1.75
pi = 3.14159
exp = 1.2e3  # 1200.0
print("float примеры:", height, pi, exp)

# 🧵 str — Строки
name = "Асхат"
greeting = 'Привет'
multiline = """Первая строка\nВторая строка"""
print("str примеры:", name, greeting)
print("str многострочная:", multiline)

# 💡 bool — Логические значения
is_happy = True
is_tired = False
print("bool примеры:", is_happy, is_tired)

# 🧺 list — Списки
numbers = [1, 2, 3, 4]
mixed = [1, "два", 3.0, True]
print("list примеры:", numbers, mixed)

# 🔗 tuple — Кортежи
coords = (10, 20)
pair = ("ключ", "значение")
print("tuple примеры:", coords, pair)

# 🗺️ dict — Словари
user = {
    "name": "Асхат",
    "age": 29,
    "is_admin": True
}
config = {
    "host": "localhost",
    "port": 8080
}
print("dict примеры:", user, config)

# 🔤 set — Множества
unique_numbers = {1, 2, 3, 1, 2}
print("set пример:", unique_numbers)

# ❌ NoneType — Отсутствие значения
result = None
print("NoneType пример:", result)

# ✅ Проверка типов
print("Тип переменной name:", type(name))
print("Тип переменной height:", type(height))
print("Тип переменной user:", type(user))
