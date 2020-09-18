import pandas as pd
import os.path

from os import path


class UserRepository:

    def __init__(self):
        self.database_path = './userdata.parquet'
        self.user_df = self._load_data()

    def _load_data(self):
        if path.exists(self.database_path):
            return pd.read_parquet(self.database_path)

        return pd.DataFrame(columns=['username', 'title', 'start', 'end', 'startTime', 'endTime', 'color'])        

    def save_data(self):
        self.user_df.to_parquet(self.database_path)

    def add_calendar_event(self, user_event):
        self.user_df = self.user_df.append(user_event, ignore_index=True)

    def get_events(self, username): 
        return self.user_df.loc[self.user_df['username'] == username, :]

    def get_without_user(self, events_list):
        return self.user_df.head().to_dict()
    
    def return_as_json(self, events_list):
        return events_list.to_json()
    def return_correct_format(self, d):
        c = [{k:v for k,v in zip(d,i)} for i in zip(*[d[a].values for a in d])]
        return c

