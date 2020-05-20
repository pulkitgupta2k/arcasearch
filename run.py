import requests

add_nulls = lambda number, zero_count : "{0:0{1}d}".format(number, zero_count)


def download_file(link, name):
    name = "downloads/"+ name
    headers = {'User-agent': 'Mozilla/5.0'}
    d_file = requests.get(link, headers = headers)
    if not d_file.status_code==404: 
        open(name, "wb").write(d_file.content)
    return d_file.status_code

def driver():
    # link = "http://gov.arcasearch.com/uswyprkcn/PDFs/tir/uswyprk-tir-050-000-0000-000_00259-001.pdF"
    link = "http://gov.arcasearch.com/uswyprkcn/PDFs/tir/uswyprk-tir"
    number_1 = 0
    number_2 = 0
    number_3 = 0
    number_4 = 0
    number_5 = 1
    number_6 = 1
    for number_1 in range(50,56):
        # for number_2 in range(999):
        #     for number_3 in range(9999):
                # for number_4 in range(999):
        for number_5 in range(1,99999):
            flag = 0
            for number_6 in range(1,999):
                d_link = "{}-{}-{}-{}-{}_{}-{}.pdf".format(link, add_nulls(number_1, 3), add_nulls(number_2, 3), add_nulls(number_3, 4), add_nulls(number_4, 3), add_nulls(number_5, 5), add_nulls(number_6, 3))
                name = "{}-{}-{}-{}_{}-{}.pdf".format(str(number_1), str(number_2), str(number_3), str(number_4), str(number_5), str(number_6))
                status = download_file(d_link, name)
                if status == 404:
                    if number_6 == 1:
                        flag = 1
                    break
                print(d_link)
            if flag == 1:
                break


if __name__ == "__main__":
    # download_file("http://gov.arcasearch.com/uswyprkcn/PDFs/tir/uswyprk-tir-050-000-0000-000_00259-001.pdF", "xyz.pdf")
    driver()
