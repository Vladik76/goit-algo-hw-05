import collections,sys

def parse_log_line(line: str) -> dict:
    """
    This function parses line from the log file
    """
    keys=["date","time","level","message"]  #keys for the log parts
    parsed_line = { key:value for key,value in zip(keys,line.split(maxsplit=3))} #Creating dictionary from the raw string.

    return parsed_line

def load_logs(file_path: str) -> list:
    """
    This function loads log file and creates list of dictionaries.
    """

    try:
        with open(file_path,"r",encoding="utf-8") as f:

            loaded_list=[parse_log_line(line.strip()) for line in f] # parsing each line from the log file

            if len(loaded_list) == 0:
                print ("The log file is empty.")
    
        return loaded_list
    
    except FileNotFoundError:
        print("File not found.")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    This function gets list of logs and loggin level (DEBUG INFO ERROR WARNING etc...)
    Returns list of filtered log entries
    """

    filtered_log=filter(lambda x:x.get("level","").upper()==level.upper(),logs)

    return list(filtered_log)

def count_logs_by_level(logs: list) -> dict:
    """
    This function returns a total number of each log by its level
    """

    logs_by_level = collections.Counter([k["level"] for  k in logs])

    return logs_by_level

def display_log_counts(counts: dict):
    """
    This function displays formatted log counts
    """

    print(f'{"Logging Level":^15}|{"Log Entries":^15}')
    print("-"*30)

    for level,number in counts.items():
        print(f'{level:^15}|{number:^15}')

def display_filtered_logs(logs:list):
    """
    This function returns formatted filtered log entries
    """

    if len(logs) > 0:
        print (f"Detailed logs for the level {logs[0].get("level")}: ")

        for item in logs:
            print (f"{item.get("date"):^15}{item.get("time"):^5}{"-":^5}{item.get("message")}")
    

def main():

    if len(sys.argv) > 1:

        loaded_logs = load_logs(sys.argv[1])

        if len(loaded_logs) > 0: #file loaded and parsed
            if len(sys.argv) >= 2:
                display_log_counts(count_logs_by_level(loaded_logs))

            if len(sys.argv) > 2:
                display_filtered_logs(filter_logs_by_level(loaded_logs,sys.argv[2].upper()))
    else:
        print("At least 1 argument should be passed.")



if __name__ == '__main__':
    main() 