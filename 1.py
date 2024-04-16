
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("расчет прихода ЖБО на КТО 15")
root.geometry("500x300")

# Увеличиваем шрифт для всех виджетов
font = ("Arial", 14)

# Создаем 6 окон для ввода цифр и назначаем им переменные и описание
label1 = tk.Label(root, text="уровень емкости вчера", font=font)
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="Уровень емкости сегодня", font=font)
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="привезла вакумка", font=font)
entry3 = tk.Entry(root)

label4 = tk.Label(root, text="сожгли за сутки", font=font)
entry4 = tk.Entry(root)

label5 = tk.Label(root, text="Пятая цифра", font=font)
entry5 = tk.Entry(root)

label6 = tk.Label(root, text="Шестая цифра", font=font)
entry6 = tk.Entry(root)

# Создаем кнопку "Рассчитать"
button = tk.Button(root, text="Рассчитать", font=font)

# Создаем окно для вывода результата
result_label = tk.Label(root, text="Сумма:", font=font)

# Создаем функцию для расчета суммы всех 6 переменных
def calculate_sum():
    # Получаем значения из окон ввода цифр
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num3 = int(entry3.get())
    num4 = int(entry4.get())
    num5 = int(entry5.get())
    num6 = int(entry6.get())

    # Рассчитываем сумму
    sum = (num1 - num2)/ 18 + num3 + num4 + num5 + num6

    # Выводим результат в окно для вывода результата
    result_label.config(text="поступило: " + str(sum))

# Назначаем функцию calculate_sum кнопке "Рассчитать"
button.config(command=calculate_sum)

# Размещаем окна в главном окне в столбик
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)
label4.grid(row=3, column=0)
entry4.grid(row=3, column=1)
label5.grid(row=4, column=0)
entry5.grid(row=4, column=1)
label6.grid(row=5, column=0)
entry6.grid(row=5, column=1)

# Размещаем кнопку "Рассчитать" и окно для вывода результата в нижнем правом углу
button.grid(row=6, column=0, sticky="se")
result_label.grid(row=6, column=1, sticky="se")

# Запускаем главное окно
root.mainloop()
