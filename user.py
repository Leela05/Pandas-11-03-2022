import pandas as pd
user = pd.DataFrame(
    [
        ['leela', 'abc nagar', 'female', 'leelarenu05@gmail.com', 'leela05'],
        ['pooja', 'abc nagar', 'female', 'pooja01@gmail.com', 'pooja01'],
        ['jo', 'abc nagar', 'female', 'jo1234@gmail.com', 'jo123'],
        ['proksh', 'abc nagar', 'female', 'proksh0405@gmail.com', 'proksh04'],
        ['pranavi', 'abc nagar', 'female', 'pranavi0105@gmail.com', 'pranavi01']
    ],columns=['name', 'address', 'gender', 'email id', 'username']
)
user.to_csv("user.csv")