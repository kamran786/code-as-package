import pandas
import os
from dotenv import load_dotenv

load_dotenv()

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


# def main():
#   print("name-kamran")
#   df = pandas.DataFrame(data)
#   name = os.getenv("Name")
#   print(f"My name is {name}")
#   print(df)

def my_main():
  print("I'm in my_main name-kamran-test-2")
  df = pandas.DataFrame(data)
  name = os.getenv("Name")
  print(f"My name is {name}")
  print(df)

if __name__ == "__main__":
  #load data into a DataFrame object:
  my_main()