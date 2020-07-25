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

        return pd.DataFrame(columns=['title', 'start', 'end', 'daysOfWeek', 'startTime', 'endTime', 'startRecur', 'endRecur', 'editable', 'backgroundColor', 'borderColor', 'textColor'])        

    def save_data(self):
        self.user_df.to_parquet(self.database_path)

    def add_calendar_event(self, user_event):
        self.user_df = self.user_df.append(user_event, ignore_index=True)

    def get_events(self, username):
        
        return self.user_df.loc[self.user_df['username'] == username, :]
