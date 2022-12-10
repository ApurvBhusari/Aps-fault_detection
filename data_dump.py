import pymongo
import pandas as pd
import json
client=pymongo.MongoClient("mongodb://localhost:27017")
data_file_path="F:\pythonProject3/aps_failure_training_set.csv"
Database_name="aps"
collection_name="sensor"
if __name__=="__main__":
    df=pd.read_csv(data_file_path)
    print(f"Rows and columns:{df.shape}")
    #convert the dataframe into json so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[Database_name][collection_name].insert_many(json_record)
