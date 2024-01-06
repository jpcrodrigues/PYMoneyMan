import csv


def read_file(file_name):
    result_array = []

    with open(file_name, "r") as ficheiro_csv:
        csv_result = csv.reader(ficheiro_csv)
        next(csv_result)
        for line in csv_result:
            result_array.append(line)

    return result_array


def write_record(file_name, record):
    with open(file_name, mode="a") as csv_file:
        csv.writer(csv_file, lineterminator="\n").writerow(record)


def update_record(file_name, record):
    records = []
    with open(file_name, "r") as csv_reader:
        reader = csv.reader(csv_reader)

        for line in reader:
            if line[0] == record[0]:
                records.append(record)
            else:
                records.append(line)

        with open(file_name, "w") as csv_write:
            writer = csv.writer(csv_write, lineterminator="\n")
            writer.writerows(records)


def delete_records_by_ids(file_name, id_list):
    records = []

    with open(file_name, "r") as csv_reader:
        reader = csv.reader(csv_reader)

        for line in reader:
            if line[0] not in id_list:
                records.append(line)

        with open(file_name, "w") as csv_write:
            writer = csv.writer(csv_write, lineterminator="\n")
            writer.writerows(records)
