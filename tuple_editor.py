import tkinter as tk
from tkinter.messagebox import showerror


def _pop(kort, index):
    return tuple(elem for i, elem in enumerate(kort) if i != index)


def _del(kort, elem):
    return tuple(x for x in kort if x != elem)


def _remove_element(is_min=True):
    global kor
    if not kor:
        showerror('Ошибка', 'Кортеж не задан')
        return

    sorted_kor = sorted(kor)
    kor = tuple(sorted_kor[1:] if is_min else sorted_kor[:-1])
    lbl['text'] = kor


def _min():
    _remove_element(is_min=True)


def _max():
    _remove_element(is_min=False)


def zadan():
    top = tk.Toplevel(win)
    tk.Label(top, text='Введите кортеж').grid(row=0, column=0)
    ent = tk.Entry(top, width=20)
    ent.grid(row=0, column=1)
    tk.Button(top, text='Считать', command=lambda: _get(ent, top)).grid(row=1, columnspan=2)


def _get(entry, window):
    global kor
    try:
        kor = tuple(int(i) for i in entry.get().split())
        lbl['text'] = kor
        window.destroy()
    except ValueError:
        showerror('Ошибка', 'Введите только числа, разделенные пробелами')


win = tk.Tk()
kor = ()

tk.Button(win, text='Задать кортеж', command=zadan).grid(row=0, columnspan=2)
tk.Label(win, text='Кортеж:').grid(row=1, column=0)
lbl = tk.Label(win, width=40)
lbl.grid(row=1, column=1)

tk.Button(win, text='Удалить минимальный элемент', command=_min).grid(row=2, column=0)
tk.Button(win, text='Удалить максимальный элемент', command=_max).grid(row=2, column=1)

win.mainloop()