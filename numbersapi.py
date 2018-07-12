import requests


params1 = {
    "json" : "true"
}


with open("power.txt", "r") as f, open("out.txt", "w") as ff:
    for line in f:
        line = line.rstrip()

        api_url = "http://numbersapi.com/" + line + "/math"
        res = requests.get(api_url, params=params1)
        print(res.url)
        data = res.json()
        x = data["found"]
        #print(x)
        if x:
            z = "Interesting\n"
        else:
            z = "Boring\n"

        ff.write(z)



