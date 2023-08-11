import requests
import json

products = [
    {
        "id": "1342",
        "name": "womens-pu-slide-sandals",
        "provider": [
            {
                "id": 107,
                "title": "Deco Slides"
            }
        ]
    },
    {
        "id": "1050",
        "name": "womens-capri-leggings-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "1286",
        "name": "girls-swimsuit-crop-top-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1285",
        "name": "girls-hipster-swimsuit-bottom-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1185",
        "name": "kids-leggings-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1097",
        "name": "youth-leggings-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1110",
        "name": "womens-shorts-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "350",
        "name": "womens-one-piece-swimsuit-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1241",
        "name": "youth-full-length-leggings-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1218",
        "name": "childrens-hoodie-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1209",
        "name": "unisex-basketball-jersey-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "859",
        "name": "womens-full-zip-hoodie-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "783",
        "name": "womens-hoodie-dress-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "1281",
        "name": "loop-tie-side-bikini-bottom-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1274",
        "name": "fully-lined-padded-sports-bra-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1223",
        "name": "yoga-capri-leggings-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1023",
        "name": "lightweight-sweatshirt-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "977",
        "name": "mens-elastic-beach-shorts-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "365",
        "name": "crew-socks",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1290",
        "name": "womens-workout-shorts-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1263",
        "name": "womens-long-sleeve-dance-dress-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "1260",
        "name": "kids-pajama-pants-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "361",
        "name": "womens-vintage-swimsuit-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1255",
        "name": "womens-long-sleeve-v-neck-shirt-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1217",
        "name": "youth-joggers-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1174",
        "name": "plus-size-leggings-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "871",
        "name": "mid-length-socks",
        "provider": [
            {
                "id": 48,
                "title": "Colorway"
            }
        ]
    },
    {
        "id": "702",
        "name": "womens-bike-shorts-aop",
        "provider": [
            {
                "id": 51,
                "title": "FYBY"
            }
        ]
    },
    {
        "id": "701",
        "name": "womens-capri-leggings-aop",
        "provider": [
            {
                "id": 51,
                "title": "FYBY"
            }
        ]
    },
    {
        "id": "1343",
        "name": "mens-pu-slide-sandals",
        "provider": [
            {
                "id": 107,
                "title": "Deco Slides"
            }
        ]
    },
    {
        "id": "1280",
        "name": "strappy-bikini-set-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "960",
        "name": "girls-sleeveless-sundress-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "757",
        "name": "mens-jogger-shorts-aop",
        "provider": [
            {
                "id": 85,
                "title": "Custom Luxe"
            }
        ]
    },
    {
        "id": "740",
        "name": "mens-pajama-pants-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "700",
        "name": "sports-bra-aop",
        "provider": [
            {
                "id": 51,
                "title": "FYBY"
            }
        ]
    },
    {
        "id": "360",
        "name": "womens-classic-one-piece-swimsuit-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1078",
        "name": "basketball-rib-shorts-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1062",
        "name": "unisex-tank-top-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "925",
        "name": "womens-relaxed-shorts-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "858",
        "name": "apron-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1283",
        "name": "mens-sports-shorts-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1087",
        "name": "unisex-football-jersey-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "947",
        "name": "womens-casual-leggings-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "822",
        "name": "womens-baseball-jersey-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1289",
        "name": "womens-short-sleeve-shirt-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1282",
        "name": "strappy-triangle-bikini-top-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1222",
        "name": "high-waisted-yoga-shorts-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1177",
        "name": "womens-casual-shorts-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "1132",
        "name": "womens-biker-shorts-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "1084",
        "name": "athletic-long-shorts-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1037",
        "name": "womens-satin-pajamas-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "576",
        "name": "baby-beanie-aop",
        "provider": [
            {
                "id": 70,
                "title": "Printed Mint"
            }
        ]
    },
    {
        "id": "508",
        "name": "womens-mini-skirt-aop",
        "provider": [
            {
                "id": 48,
                "title": "Colorway"
            }
        ]
    },
    {
        "id": "1284",
        "name": "girls-two-piece-swimsuit-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "452",
        "name": "recycled-poly-socks",
        "provider": [
            {
                "id": 33,
                "title": "Tribe Socks"
            }
        ]
    },
    {
        "id": "934",
        "name": "mens-puffer-jacket-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "739",
        "name": "womens-pajama-pants-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "407",
        "name": "womens-briefs-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "919",
        "name": "apron-aop",
        "provider": [
            {
                "id": 48,
                "title": "Colorway"
            }
        ]
    },
    {
        "id": "828",
        "name": "womens-short-pajama-set-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "1032",
        "name": "mens-loose-t-shirt-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "856",
        "name": "mens-board-shorts-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "1071",
        "name": "seamless-sports-bra-aop",
        "provider": [
            {
                "id": 240,
                "title": "PCM"
            }
        ]
    },
    {
        "id": "1028",
        "name": "mens-hoodie-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "799",
        "name": "womens-bomber-jacket-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "509",
        "name": "womens-spandex-leggings-aop",
        "provider": [
            {
                "id": 48,
                "title": "Colorway"
            }
        ]
    },
    {
        "id": "949",
        "name": "basketball-jersey-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "948",
        "name": "basketball-shorts-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1262",
        "name": "womens-skater-dress-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "703",
        "name": "stretchy-leggings-aop",
        "provider": [
            {
                "id": 51,
                "title": "FYBY"
            }
        ]
    },
    {
        "id": "593",
        "name": "mens-baseball-jersey-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1270",
        "name": "athletic-hoodie-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "1254",
        "name": "mens-pajama-pants-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "1251",
        "name": "womens-pajama-pants-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "997",
        "name": "mens-tank-aop",
        "provider": [
            {
                "id": 90,
                "title": "Smart Printee"
            }
        ]
    },
    {
        "id": "832",
        "name": "mens-full-zip-hoodie-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "285",
        "name": "womens-pencil-skirt-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "923",
        "name": "long-sleeve-kimono-robe-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "281",
        "name": "unisex-cut-and-sew-tee-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "376",
        "name": "sublimation-socks",
        "provider": [
            {
                "id": 1,
                "title": "SPOKE Custom Products"
            }
        ]
    },
    {
        "id": "924",
        "name": "mens-hawaiian-shirt-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "433",
        "name": "mens-bomber-jacket-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "589",
        "name": "swim-trunks-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "574",
        "name": "cushioned-crew-socks",
        "provider": [
            {
                "id": 64,
                "title": "ThreadStudio"
            }
        ]
    },
    {
        "id": "1242",
        "name": "mens-polyester-tee-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "591",
        "name": "athletic-joggers-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "831",
        "name": "mens-baseball-jersey-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "349",
        "name": "womens-bikini-swimsuit-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "256",
        "name": "womens-cut-and-sew-casual-leggings-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "279",
        "name": "womens-cut-and-sew-tee-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "450",
        "name": "unisex-pullover-hoodie-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "449",
        "name": "unisex-sweatshirt-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "978",
        "name": "mens-mid-length-swim-shorts-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "516",
        "name": "high-waisted-yoga-leggings-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "286",
        "name": "womens-skater-skirt-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "592",
        "name": "fashion-hoodie-aop",
        "provider": [
            {
                "id": 83,
                "title": "Subliminator"
            }
        ]
    },
    {
        "id": "406",
        "name": "mens-boxer-briefs-aop",
        "provider": [
            {
                "id": 14,
                "title": "ArtsAdd"
            }
        ]
    },
    {
        "id": "627",
        "name": "crop-tee-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "431",
        "name": "t-shirt-dress-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "276",
        "name": "womens-cut-and-sew-racerback-dress-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    },
    {
        "id": "1261",
        "name": "mens-long-sleeve-shirt-aop",
        "provider": [
            {
                "id": 47,
                "title": "Miami Sublimation"
            }
        ]
    },
    {
        "id": "451",
        "name": "unisex-zip-hoodie-aop",
        "provider": [
            {
                "id": 10,
                "title": "MWW On Demand"
            }
        ]
    }
]



objection = []
for prod in products:
    url = "https://api.printify.com/v1/catalog/blueprints/" + str(prod["id"]) + "/print_providers/" + str(prod["provider"][0]["id"]) + "/variants.json?show-out-of-stock =0"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'
                         '.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImU5NmQyOGMyMmViYjYxNmI5MzljYzQxYTUyZDlmZGY5MjNlNTEzMmY0NTFmNjgzZGIwOGI2ZDAzZDAxMTFjMjRiNDcwODU1MDU0MjZlNDg2IiwiaWF0IjoxNjkwOTUzNDgzLjkzMjM0MywibmJmIjoxNjkwOTUzNDgzLjkzMjM0NywiZXhwIjoxNzIyNTc1ODgzLjkyNTc2Nywic3ViIjoiMTQwODIwNzciLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.AVeJKC7hKdnBS6qfsd8TBkR8-YYQ-xq-6x5rU37cXDruY8rRdJjpeQNC9WVbdBXxrRElmAxKCXiB7CwXPzw'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response content to JSON
        data["blueprint_id"]=prod["id"]
        data["blueprint_name"] = prod["name"]
        objection.append(data)
    else:
        print("Failed to fetch data from the API")
        print(response.text)

with open("output.json", "w") as json_file:
    json.dump(objection, json_file, indent=4)  # Write JSON data to the file with indentation
