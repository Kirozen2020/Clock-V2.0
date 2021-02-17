import turtle
from datetime import datetime

clock = turtle.Turtle()
datt = turtle.Turtle()
win = turtle.Screen()
win.setup(500,500)

current_datetime = datetime.now()#מקסל מידה על השעון

Haur = current_datetime.hour#קבלת שעה
Minute = current_datetime.minute#קבלת דקות
#Haur += 2#מוסיף שעתיים כדי שיתאים לשעון שלנו)(2+)
d1 = current_datetime.strftime("%d/%m/%Y")#קבלת תאריך

clock.goto(0,0)
clock.ht()
datt.pu()
datt.goto(-150,200)
datt.ht()
#בדיקה לכשי שהשעון יפיע בצורה יפה יותר (אם ה0 וכול זה...)
if Haur < 10:
  if Minute < 10 and Minute <= 60:
    clock.write(f"0{Haur}:0{Minute}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
  elif Minute >= 10 and Minute <= 60:
    clock.write(f"0{Haur}:{Minute}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
elif Haur >= 10:
  if Minute < 10 and Minute <= 60:
    clock.write(f"{Haur}:0{Minute}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
  elif Minute >= 10 and Minute <= 60:
    clock.write(f"{Haur}:{Minute}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))

while True:
  #קבלת זמן עכשוית
  time_now = datetime.now()
  Haur2 = time_now.hour
  Minute2 = time_now.minute
  #Haur2 += 2
  if Haur != Haur2 or Minute != Minute2:#בדיקה עם הזמן השתנה
    clock.clear()
    if Haur < 10:#שינוי הזמן על המסך
      if Minute2 < 10 and Minute2 <= 60:
        clock.write(f"0{Haur2}:0{Minute2}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
        print(f"0{Haur2}:0{Minute2}")
      elif Minute2 >= 10 and Minute2 <= 60:
        clock.write(f"0{Haur2}:{Minute2}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
        print(f"0{Haur2}:{Minute2}")
    elif Haur2 >= 10:
      if Minute2 < 10 and Minute2 <= 60:
        clock.write(f"{Haur2}:0{Minute2}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
        print(f"{Haur2}:0{Minute2}")
      elif Minute2 >= 10 and Minute2 <= 60:
        clock.write(f"{Haur2}:{Minute2}", align="center", font=("Comic Sans MS", 40, "normal", "bold"))
        print(f"{Haur2}:{Minute2}")
    #קביעה של הנתונים החדשים כמקוריים
    Haur = Haur2
    Minute = Minute2

  #שינוי התאריך
  d2 = time_now.strftime("%d/%m/%y")
  if d1 != d2:#בדיקה עם התאריך השתנה
    datt.write(f"{d2}", align="center", font=("Comic Sans MS", 20, "normal", "bold"))
    d1 = d2
