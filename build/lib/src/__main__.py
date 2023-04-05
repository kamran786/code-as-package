import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


def main():
  df = pd.DataFrame(data)

  print(df)

if __name__ == "__main__":
  #load data into a DataFrame object:
  main()