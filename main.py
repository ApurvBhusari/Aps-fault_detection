import pymongo
client=pymongo.Mongoclient("mongodb://localhost:27017")
data_file_path="F:\pythonProject3\aps_failure_training_set.csv"
Database_name="aps"
collection_name="sensor"
if __name__=="__main__":
    df=pd.read_csv(data_file_path)
    print(f"Rows and columns:{df.shape}")