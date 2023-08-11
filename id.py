import requests
import json

product_ids = [
    {
        "name": "Men's PU Slide Sandals",
        "id": "1343",
        "price": 3358
    },
    {
        "name": "Women's PU Slide Sandals",
        "id": "1342",
        "price": 3358
    },
    {
        "name": "Women’s Capri Leggings (AOP)",
        "id": "1050",
        "price": 2287
    },
    {
        "name": "Girls' Swimsuit Crop Top (AOP)",
        "id": "1286",
        "price": 2388
    },
    {
        "name": "Girls' Hipster Swimsuit Bottom (AOP)",
        "id": "1285",
        "price": 1940
    },
    {
        "name": "Kids Leggings (AOP)",
        "id": "1185",
        "price": 1642
    },
    {
        "name": "Youth Leggings (AOP)",
        "id": "1097",
        "price": 1791
    },
    {
        "name": "Girls Two Piece Swimsuit (AOP)",
        "id": "1284",
        "price": 3731
    },
    {
        "name": "Women's Shorts (AOP)",
        "id": "1110",
        "price": 1734
    },
    {
        "name": "Women's One-piece Swimsuit (AOP)",
        "id": "350",
        "price": 1724
    },
    {
        "name": "Youth Full-Length Leggings (AOP)",
        "id": "1241",
        "price": 2388
    },
    {
        "name": "Children's Hoodie (AOP)",
        "id": "1218",
        "price": 2612
    },
    {
        "name": "Unisex Basketball Jersey (AOP)",
        "id": "1209",
        "price": 1940
    },
    {
        "name": "Women’s Full-Zip Hoodie (AOP)",
        "id": "859",
        "price": 3970
    },
    {
        "name": "Women's Hoodie Dress (AOP)",
        "id": "783",
        "price": 2687
    },
    {
        "name": "Loop Tie Side Bikini Bottom (AOP)",
        "id": "1281",
        "price": 2090
    },
    {
        "name": "Fully Lined, Padded Sports Bra (AOP)",
        "id": "1274",
        "price": 2836
    },
    {
        "name": "Yoga Capri Leggings (AOP)",
        "id": "1223",
        "price": 2985
    },
    {
        "name": "Lightweight Sweatshirt (AOP)",
        "id": "1023",
        "price": 1940
    },
    {
        "name": "Men's Elastic Beach Shorts (AOP)",
        "id": "977",
        "price": 2985
    },
    {
        "name": "Crew Socks",
        "id": "365",
        "price": 1045
    },
    {
        "name": "Women's Workout Shorts (AOP)",
        "id": "1290",
        "price": 2276
    },
    {
        "name": "Women's Long Sleeve Dance Dress (AOP)",
        "id": "1263",
        "price": 1940
    },
    {
        "name": "Kids Pajama Pants (AOP)",
        "id": "1260",
        "price": 2313
    },
    {
        "name": "Women's Vintage Swimsuit (AOP)",
        "id": "361",
        "price": 2164
    },
    {
        "name": "Women's Long Sleeve V-neck Shirt (AOP)",
        "id": "1255",
        "price": 2687
    },
    {
        "name": "Youth Joggers (AOP)",
        "id": "1217",
        "price": 2276
    },
    {
        "name": "Plus Size Leggings (AOP)",
        "id": "1174",
        "price": 2388
    },
    {
        "name": "Mid-length Socks",
        "id": "871",
        "price": 1579
    },
    {
        "name": "Women's Bike Shorts (AOP)",
        "id": "702",
        "price": 2090
    },
    {
        "name": "Women's Capri Leggings (AOP)",
        "id": "701",
        "price": 2164
    },
    {
        "name": "Long Sleeve Kimono Robe (AOP)",
        "id": "923",
        "price": 3209
    },
    {
        "name": "Strappy Bikini Set (AOP)",
        "id": "1280",
        "price": 3582
    },
    {
        "name": "Girls' Sleeveless Sundress (AOP)",
        "id": "960",
        "price": 2328
    },
    {
        "name": "Apron (AOP)",
        "id": "858",
        "price": 1701
    },
    {
        "name": "Men's Jogger Shorts (AOP)",
        "id": "757",
        "price": 3657
    },
    {
        "name": "Men's Pajama Pants (AOP)",
        "id": "740",
        "price": 3119
    },
    {
        "name": "Sports Bra (AOP)",
        "id": "700",
        "price": 2351
    },
    {
        "name": "Women's Classic One-Piece Swimsuit (AOP)",
        "id": "360",
        "price": 1940
    },
    {
        "name": "Basketball Rib Shorts (AOP)",
        "id": "1078",
        "price": 2687
    },
    {
        "name": "Unisex Tank Top (AOP)",
        "id": "1062",
        "price": 1746
    },
    {
        "name": "Women's Relaxed Shorts (AOP)",
        "id": "925",
        "price": 2433
    },
    {
        "name": "Men’s Sports Shorts (AOP)",
        "id": "1283",
        "price": 2313
    },
    {
        "name": "Unisex Football Jersey (AOP)",
        "id": "1087",
        "price": 2537
    },
    {
        "name": "Women's Casual Leggings (AOP)",
        "id": "947",
        "price": 2463
    },
    {
        "name": "Women's Baseball Jersey (AOP)",
        "id": "822",
        "price": 2463
    },
    {
        "name": "Women's Short Sleeve Shirt (AOP)",
        "id": "1289",
        "price": 1679
    },
    {
        "name": "Strappy Triangle Bikini Top (AOP)",
        "id": "1282",
        "price": 2090
    },
    {
        "name": "High Waisted Yoga Shorts (AOP)",
        "id": "1222",
        "price": 2836
    },
    {
        "name": "Women's Casual Shorts (AOP)",
        "id": "1177",
        "price": 1493
    },
    {
        "name": "Women's Biker Shorts (AOP)",
        "id": "1132",
        "price": 1870
    },
    {
        "name": "Athletic Long Shorts (AOP)",
        "id": "1084",
        "price": 2425
    },
    {
        "name": "Women's Satin Pajamas (AOP)",
        "id": "1037",
        "price": 5597
    },
    {
        "name": "Baby Beanie (AOP)",
        "id": "576",
        "price": 1269
    },
    {
        "name": "Women's Mini Skirt (AOP)",
        "id": "508",
        "price": 2537
    },
    {
        "name": "Recycled Poly Socks",
        "id": "452",
        "price": 1045
    },
    {
        "name": "Men's Puffer Jacket (AOP)",
        "id": "934",
        "price": 5672
    },
    {
        "name": "Women's Pajama Pants (AOP)",
        "id": "739",
        "price": 2937
    },
    {
        "name": "Women's Briefs (AOP)",
        "id": "407",
        "price": 1940
    },
    {
        "name": "Apron (AOP)",
        "id": "919",
        "price": 1940
    },
    {
        "name": "Sublimation Crew Socks (EU)",
        "id": "496",
        "price": 1015
    },
    {
        "name": "Women's Short Pajama Set (AOP)",
        "id": "828",
        "price": 2687
    },
    {
        "name": "Men's Loose T-shirt (AOP)",
        "id": "1032",
        "price": 1343
    },
    {
        "name": "Men's Board Shorts (AOP)",
        "id": "856",
        "price": 1791
    },
    {
        "name": "Seamless Sports Bra (AOP)",
        "id": "1071",
        "price": 2537
    },
    {
        "name": "Men's Hoodie (AOP)",
        "id": "1028",
        "price": 3284
    },
    {
        "name": "Women's Bomber Jacket (AOP)",
        "id": "799",
        "price": 2239
    },
    {
        "name": "Women's Spandex Leggings (AOP)",
        "id": "509",
        "price": 2864
    },
    {
        "name": "Basketball Jersey (AOP)",
        "id": "949",
        "price": 2313
    },
    {
        "name": "Basketball Shorts (AOP)",
        "id": "948",
        "price": 2313
    },
    {
        "name": "Women's Skater Dress (AOP)",
        "id": "1262",
        "price": 2761
    },
    {
        "name": "Stretchy Leggings (AOP)",
        "id": "703",
        "price": 2164
    },
    {
        "name": "Men's Baseball Jersey (AOP)",
        "id": "593",
        "price": 2612
    },
    {
        "name": "Athletic Hoodie (AOP)",
        "id": "1270",
        "price": 2687
    },
    {
        "name": "Men's Pajama Pants (AOP)",
        "id": "1254",
        "price": 2761
    },
    {
        "name": "Women's Pajama Pants (AOP)",
        "id": "1251",
        "price": 2761
    },
    {
        "name": "Men's Tank (AOP)",
        "id": "997",
        "price": 1269
    },
    {
        "name": "Men's Full-Zip Hoodie (AOP)",
        "id": "832",
        "price": 3881
    },
    {
        "name": "Women's Pencil Skirt (AOP)",
        "id": "285",
        "price": 1506
    },
    {
        "name": "Unisex Cut & Sew Tee (AOP)",
        "id": "281",
        "price": 2081
    },
    {
        "name": "Sublimation Socks",
        "id": "376",
        "price": 769
    },
    {
        "name": "Men's Hawaiian Shirt (AOP)",
        "id": "924",
        "price": 3821
    },
    {
        "name": "Men's Bomber Jacket (AOP)",
        "id": "433",
        "price": 5567
    },
    {
        "name": "Swim Trunks (AOP)",
        "id": "589",
        "price": 2239
    },
    {
        "name": "Cushioned Crew Socks",
        "id": "574",
        "price": 945
    },
    {
        "name": "Men's Polyester Tee (AOP)",
        "id": "1242",
        "price": 2060
    },
    {
        "name": "Athletic Joggers (AOP)",
        "id": "591",
        "price": 2836
    },
    {
        "name": "Men's Baseball Jersey (AOP)",
        "id": "831",
        "price": 2806
    },
    {
        "name": "Women's Bikini Swimsuit (AOP)",
        "id": "349",
        "price": 1866
    },
    {
        "name": "Women's Cut & Sew Casual Leggings (AOP)",
        "id": "256",
        "price": 2155
    },
    {
        "name": "Women's Cut & Sew Tee (AOP)",
        "id": "279",
        "price": 1863
    },
    {
        "name": "Unisex Pullover Hoodie (AOP)",
        "id": "450",
        "price": 4996
    },
    {
        "name": "Unisex Sweatshirt (AOP)",
        "id": "449",
        "price": 3149
    },
    {
        "name": "Men's Mid-Length Swim Shorts (AOP)",
        "id": "978",
        "price": 2507
    },
    {
        "name": "High Waisted Yoga Leggings (AOP)",
        "id": "516",
        "price": 3209
    },
    {
        "name": "Women's Skater Skirt (AOP)",
        "id": "286",
        "price": 2264
    },
    {
        "name": "Fashion Hoodie (AOP)",
        "id": "592",
        "price": 3060
    },
    {
        "name": "Men's Boxer Briefs (AOP)",
        "id": "406",
        "price": 2313
    },
    {
        "name": "Crop Tee (AOP)",
        "id": "627",
        "price": 2163
    },
    {
        "name": "T-Shirt Dress (AOP)",
        "id": "431",
        "price": 2618
    },
    {
        "name": "Women's Cut & Sew Racerback Dress (AOP)",
        "id": "276",
        "price": 2087
    },
    {
        "name": "Men's Long Sleeve Shirt (AOP)",
        "id": "1261",
        "price": 2612
    },
    {
        "name": "Unisex Zip Hoodie (AOP)",
        "id": "451",
        "price": 5385
    }
]


objection = []
for bid in product_ids:

    url = "https://api.printify.com/v1/catalog/blueprints/" + bid["id"] + "/print_providers.json"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImU5NmQyOGMyMmViYjYxNmI5MzljYzQxYTUyZDlmZGY5MjNlNTEzMmY0NTFmNjgzZGIwOGI2ZDAzZDAxMTFjMjRiNDcwODU1MDU0MjZlNDg2IiwiaWF0IjoxNjkwOTUzNDgzLjkzMjM0MywibmJmIjoxNjkwOTUzNDgzLjkzMjM0NywiZXhwIjoxNzIyNTc1ODgzLjkyNTc2Nywic3ViIjoiMTQwODIwNzciLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.AVeJKC7hKdnBS6qfsd8TBkR8-YYQ-xq-6x5rU37cXDruY8rRdJjpeQNC9WVbdBXxrRElmAxKCXiB7CwXPzw'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response content to JSON
        print(data)
        objection.append({
            "id": bid["id"],
            "name":bid["name"],
            "provider_id": data[0]["id"],
            "provider_name": data[0]["title"],
            "price": bid["price"]
        })
    else:
        print("Failed to fetch data from the API")
        print(response.text)

with open("outputid.json", "w") as json_file:
    json.dump(objection, json_file, indent=4)  # Write JSON data to the file with indentation
