import requests
import json
import logging
from fake_headers import Headers
from bs4 import BeautifulSoup
from main_3 import logger

logging.basicConfig(level=logging.INFO)


@logger("log_1.log")
def gen_fake_headers():
    headers_gen = Headers(os="win", browser="chrome").generate()
    return headers_gen


@logger("log_2.log")
def extract_vacancies(query_list: list):
    vacancies = {}
    query_join = '+'.join(query_list)
    url = f"https://spb.hh.ru/search/vacancy?text={query_join}&area=1&area=2"  # 1-Москва, 2-Санкт-Петербург
    # print(url)

    response = requests.get(url=url, headers=gen_fake_headers())

    if response.status_code != 200:
        logging.error("Failed to fetch the page!")
        return

    soup = BeautifulSoup(response.content, "lxml")
    vacancies_list_tag = soup.find("div", class_="bloko-column bloko-column_xs-4 bloko-column_s-8 "
                                                 "bloko-column_m-8 bloko-column_l-12")
    vacancy_tag = vacancies_list_tag.find_all("div", class_="vacancy-serp-item-body")
    for tag in vacancy_tag:
        title = tag.find("span", class_="serp-item__title").text
        # print(title)
        link = tag.find("a", class_="bloko-link")["href"]
        # print(link)
        company_tag = tag.find("div", class_="vacancy-serp-item__meta-info-company")
        company = " ".join(company_tag.text.split('\xa0'))
        # print(company)
        city_tag = tag.find_all("div", class_="bloko-text")
        city = " ".join(city_tag[1].text.split('\xa0'))
        # print(city)
        salary_tag = tag.find("span", class_="bloko-header-section-2")
        if salary_tag is not None:
            salary = " ".join(salary_tag.text.split('\u202f'))
            # print(salary)
        else:
            salary = "Не указана"

        vacancies.setdefault(title, {"link": link, "company": company, "city": city, "salary": salary})
        # print(vacancies)

    json_obj = json.dumps(vacancies, ensure_ascii=False, indent=4)
    with open("vacancies.json", "w", encoding="utf-8") as file:
        file.write(json_obj)

    logging.info("Парсинг завершен. Результаты сохранены в файле vacancies.json.")
    print(f"Добавлено {len(vacancies)} вакансий.")


if __name__ == "__main__":
    extract_vacancies(['python', 'django', 'flask'])
