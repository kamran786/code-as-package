import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

if __name__ == "__main__":
  #load data into a DataFrame object:
  df = pd.DataFrame(data)

  print(df)