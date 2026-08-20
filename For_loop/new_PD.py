
import pandas as pd

data = {
    'Name': ['Aarav Mehta', 'Isha Reddy', 'Kabir Shah'],
    'Age': [17, 17, 18],
    'Roll_no': ['201', '89', '90'],
    'Subject': ['Python', 'SQL', 'C##']
}

df = pd.DataFrame(data)

print(df)
type(df)