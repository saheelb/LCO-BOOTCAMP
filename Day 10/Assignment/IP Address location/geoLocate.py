from random import randint, choice
import requests as rq
import json, os, csv
from tqdm import tqdm


class IP_Generator:
    
    @staticmethod
    def generate_public_IP(count=1):
        public_ip_ranges = [[(1, 9), (0, 255), (0, 255), (0, 255)],
                            [(11, 126), (255, 255), (255, 255), (255, 255)],
                            [(128, 168), (0, 255), (0, 255), (0, 255)],
                            [(169, 169), (0, 253), (0, 255), (0, 255)],
                            [(169, 169), (255, 255), (0, 255), (0, 255)],
                            [(170, 171), (0, 255), (0, 255), (0, 255)],
                            [(172, 172), (0, 15), (0, 255), (0, 255)],
                            [(172, 172), (32, 255), (0, 255), (0, 255)],
                            [(173, 191), (0, 255), (0, 255), (0, 255)],
                            [(192, 192), (0, 167), (0, 255), (0, 255)],
                            [(193, 223), (0, 255), (0, 255), (0, 255)]
                        ]

        IP_set = set()
        while len(IP_set) < count:
            ch = choice(public_ip_ranges)
            ip = ".".join([str(randint(*ch[0])),
                        str(randint(*ch[1])),
                        str(randint(*ch[2])),
                        str(randint(*ch[3])) ])

            IP_set.add(ip)

        return list(IP_set)

    @staticmethod
    def generate_any_IP(count=1):
        IP_set = set()
        while len(IP_set) < count:
            ip = ".".join([str(randint(1, 255)),
                        str(randint(0, 255)),
                        str(randint(0, 255)),
                        str(randint(0, 255)) ])

            IP_set.add(ip)

        return list(IP_set)


class IP_locator:
    def __init__(self, IP_list, *args):
        self.IP_list = IP_list
        self.fields = args

    def get_location(self):
        location_info = []
        
        access_key = "<Your API key here>"
        request_url = "http://api.ipstack.com/{}?access_key="+access_key
        
        if len(self.fields):
            request_url += "&fields=" + ",".join(self.fields)

        for ip in tqdm(self.IP_list):
            data = json.loads(rq.get(request_url.format(ip)).text)
            data['ip_address'] = ip
            location_info.append(data)

        return location_info


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def log_csv(self, data_list):
        extension = ".csv"
        try:
            if not os.path.exists(self.file_name+extension):
                with open(self.file_name + extension, "a+") as file:
                    fields = []
                    fields.extend(data_list[0].keys())
                    print(fields)

                    csv_file = csv.writer(file, delimiter=",")
                    csv_file.writerow(fields)

            with open(self.file_name + extension, "a+") as file:
                csv_file = csv.writer(file, delimiter=",")

                for i in data_list:
                    row = []
                    row.extend(i.values())
                    csv_file.writerow(row)
            return True

        except Exception as e:
            return False

    def log_txt(self, data_list):
        extension = ".txt"
        try:
            with open(self.file_name + extension, "a+") as txt_file:
                for record in data_list:
                    data_line = json.dumps(record) + "\n\n"
                    txt_file.write(data_line)
            return True

        except Exception as e:
            return False


    def read_data(self):
        pass

        
def main():
    count = 3
    IP_list = IP_Generator.generate_public_IP(count=count)
    
    print("\nGetting Geolocations of "+str(count)+" IP(s)...\n")

    locator = IP_locator(IP_list, "country_name","region_name","city")
    location_data = locator.get_location()
    

    print("\n\nLogging data to files...")

    logger_obj = Logger("IP_locations")
    if logger_obj.log_csv(location_data):
        print("CSV File Done!")
    else :
        print("Some Problem Occured while Logging CSV File!")
    if logger_obj.log_txt(location_data):
        print("Text File Done!")
    else :
        print("Some Problem Occured while Logging Txt File!")



if __name__ == "__main__":
    main()
