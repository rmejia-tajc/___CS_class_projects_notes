class Animal:
    pass

if __name__ == "__main__":
    #Don't run this when this file is imported
    print(f"Hi! {__name__}")




    def main(sys.argv):
  cal = calendar.TextCalendar(calendar.SUNDAY)
  if len(sys.argv) == 0:
    currentDate = datetime.now()
    print(cal.formatmonth(currentDate.year, currentDate.month))
  elif len(sys.argv) == 1:
    currentDate = datetime.now()
    print(cal.formatmonth(currentDate.year, int(sys.argv[0])))
  elif len(sys.argv) == 2:
    print(cal.formatmonth(int(sys.argv[1]), int(sys.argv[0])))
  else:
    print('Enter a month ( 1- 12 ) in this format: "python 14_cal.py 5"\nOr enter a month ( 1-12 ) and a year ( xxxx ) in this format: "python 14_cal.py 5 2015"')