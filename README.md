# Приложение для отображения профиля, написанное с использованием PyQt6.

## Требования:
- Python 3.6 или выше
- PyQt6 — для графического интерфейса

## Установка:
```bash
# Установка зависимостей
pip install PyQt6
```

## Структура проекта:
├── 📁 images/
│   ├── skyblue.png          # Фоновое изображение
│   ├── profile_image.png          # Изображение для примера
│   └── Kotik.png    # Аватар профиля
├── 📄 code_PyQt6.py       # Основной файл приложения
└── 📄 README.md            # Документация

## Запуск приложения:
```bash
python code_PyQt6.py
```

Используемые библиотеки:
# PyQt6.QtWidgets — Компоненты интерфейса

QApplication	- Главное приложение	- app = QApplication(sys.argv)
QWidget	- Базовое окно	- class MainWindow(QWidget)
QLabel -	Отображение текста и изображений -	user_label = QLabel(self)

# PyQt6.QtGui - Графика и шрифты

QFont	- Настройка шрифтов	- setFont(QFont("Arial", 17))
QPixmap -	Работа с изображениями	- pixmap = QPixmap(image)

# Системные библиотеки

os	- Работа с файловой системой	- os.path.join(),os.path.dirname()
sys -	Системные операции	- sys.argv,sys.exit()

## Основные методы классаMainWindow:
```bash
def initializeUI(self):
    """Настройка основного интерфейса"""
    self.setGeometry(50, 50, 300, 400)
    self.setWindowTitle("Резюме")
```
```bash
def createImageLabels(self):
    """Загрузка и отображение изображений"""
    # Автоматическое определение путей
    # Обработка ошибок загрузки
    # Адаптивное масштабирование
```
```bash
def setUpMainWindow(self):
    """Создание всех элементов интерфейса"""
    # Текстовые метки
    # Настройка шрифтов
    # Позиционирование элементов
```
