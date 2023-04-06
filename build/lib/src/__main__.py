import pandas as pandas
import os
from dotenv import load_dotenv

load_dotenv()

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


def main():
  df = pandas.DataFrame(data)
  name = os.getenv("Name")
  print(f"My name is {name}")
  print(df)

if __name__ == "__main__":
  #load data into a DataFrame object:
  main()