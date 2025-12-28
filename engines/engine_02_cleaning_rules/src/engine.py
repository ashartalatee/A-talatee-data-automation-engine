import pandas as pd
from clean_missing import clean_missing
from clean_duplicates import remove_duplicates, standardize_columns
from clean_format import validate_dates, validate_numeric
from utils import setup_logger, log_rule, generate_report

class CleaningEngine:
    def __init__(self, df):
        self.df = df
        setup_logger()
    
    def run_missing(self):
        df_before = self.df.copy()
        self.df = clean_missing(self.df)
        log_rule("clean_missing", "Missing values cleaned successfully")
        generate_report(df_before, self.df, "clean_missing")
    
    def run_duplicates(self):
        df_before = self.df.copy()
        self.df = remove_duplicates(self.df)
        self.df = standardize_columns(self.df)
        log_rule("clean_duplicates", "Duplicates removed & columns standardized")
        generate_report(df_before, self.df, "clean_duplicates")
    
    def run_format(self):
        df_before = self.df.copy()
        self.df = validate_dates(self.df)
        self.df = validate_numeric(self.df)
        log_rule("validate_format", "Date & numeric validated")
        generate_report(df_before, self.df, "validate_format")
    
    def run_all(self):
        self.run_missing()
        self.run_duplicates()
        self.run_format()
    
    def get_cleaned_data(self):
        return self.df
