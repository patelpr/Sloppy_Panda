import requests
import openai
import json
from flask import Flask, jsonify, request

app = Flask(__name__)
printify_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImU5NmQyOGMyMmViYjYxNmI5MzljYzQxYTUyZDlmZGY5MjNlNTEzMmY0NTFmNjgzZGIwOGI2ZDAzZDAxMTFjMjRiNDcwODU1MDU0MjZlNDg2IiwiaWF0IjoxNjkwOTUzNDgzLjkzMjM0MywibmJmIjoxNjkwOTUzNDgzLjkzMjM0NywiZXhwIjoxNzIyNTc1ODgzLjkyNTc2Nywic3ViIjoiMTQwODIwNzciLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.AVeJKC7hKdnBS6qfsd8TBkR8-YYQ-xq-6x5rU37cXDruY8rRdJjpeQNC9WVbdBXxrRElmAxKCXiB7CwXPzw"
openai.api_key = "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"


def pick_product_dims(imageid, tags, title, desc, style, hexcode,shopid):
   product = {
    "1342": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-pu-slide-sandals",
        "variants": [
            102117,
            102124,
            102118,
            102125,
            102119,
            102126,
            102120,
            102127,
            102121,
            102128,
            102122,
            102129,
            102123,
            102130
        ],
        "print_areas": [
            {
                "position": "left_shoe",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_shoe",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1342",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 107
    },
    "1050": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-capri-leggings-aop",
        "variants": [
            82045,
            82047,
            82049,
            82051,
            82053,
            82055
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1050",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "1286": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "girls-swimsuit-crop-top-aop",
        "variants": [
            96428,
            96429,
            96430,
            96431
        ],
        "print_areas": [
            {
                "position": "front_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1286",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1285": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "girls-hipster-swimsuit-bottom-aop",
        "variants": [
            96432,
            96433,
            96434,
            96435
        ],
        "print_areas": [
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1285",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1185": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "kids-leggings-aop",
        "variants": [
            91871,
            91872,
            91873,
            91874,
            91875,
            91876,
            91877
        ],
        "print_areas": [
            {
                "position": "all",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1185",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1097": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "youth-leggings-aop",
        "variants": [
            84654,
            84655,
            84656,
            84657,
            84658,
            84659,
            84660
        ],
        "print_areas": [
            {
                "position": "all",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1097",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1110": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-shorts-aop",
        "variants": [
            86201,
            86202,
            86203,
            86204,
            86205,
            86206
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1110",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "350": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-one-piece-swimsuit-aop",
        "variants": [
            44452,
            44453,
            44449,
            44457,
            44456,
            44458,
            44455,
            44454,
            44451,
            44450,
            44462,
            44463,
            44459,
            44467,
            44466,
            44468,
            44465,
            44464,
            44461,
            44460,
            44472,
            44473,
            44469,
            44477,
            44476,
            44478,
            44475,
            44474,
            44471,
            44470,
            44482,
            44483,
            44479,
            44487,
            44486,
            44488,
            44485,
            44484,
            44481,
            44480,
            44492,
            44493,
            44489,
            44497,
            44496,
            44498,
            44495,
            44494,
            44491,
            44490,
            44502,
            44503,
            44499,
            44507,
            44506,
            44508,
            44505,
            44504,
            44501,
            44500,
            44512,
            44513,
            44509,
            44517,
            44516,
            44518,
            44515,
            44514,
            44511,
            44510
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "strap",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "350",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1241": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "youth-full-length-leggings-aop",
        "variants": [
            94247,
            94248,
            94249,
            94250,
            94251,
            94252
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1241",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1218": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "childrens-hoodie-aop",
        "variants": [
            92328,
            92329,
            92330,
            92331,
            92332,
            92333
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside_label",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1218",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1209": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-basketball-jersey-aop",
        "variants": [
            92054,
            92055,
            92056,
            92057,
            92058,
            92059,
            92060,
            92061
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1209",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "859": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-full-zip-hoodie-aop",
        "variants": [
            77204,
            77205,
            76814,
            76815,
            76816,
            76817,
            76818,
            76819,
            76820,
            76821
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "859",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "783": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-hoodie-dress-aop",
        "variants": [
            74892,
            74893,
            74894,
            74895,
            74896
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "hem",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood_lining",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood_lining",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "783",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "1281": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "loop-tie-side-bikini-bottom-aop",
        "variants": [
            96471,
            96472,
            96473,
            96474,
            96475,
            96476,
            96477,
            96478,
            96479,
            96480,
            96481,
            96482,
            96483,
            96484,
            96485,
            96486,
            96487,
            96488,
            96489,
            96490,
            96491,
            96492,
            96493,
            96494,
            96495,
            96496,
            96497,
            96498,
            96499,
            96500,
            96501,
            96502,
            96503,
            96504,
            96505
        ],
        "print_areas": [
            {
                "position": "front_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1281",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1274": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "fully-lined-padded-sports-bra-aop",
        "variants": [
            96169,
            96170,
            96171,
            96172,
            96173
        ],
        "print_areas": [
            {
                "position": "front_bra",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bra",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband_bra",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1274",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1223": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "yoga-capri-leggings-aop",
        "variants": [
            93609,
            93610,
            93611,
            93612,
            93613,
            93614
        ],
        "print_areas": [
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_waistband_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_waistband_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1223",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1023": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "lightweight-sweatshirt-aop",
        "variants": [
            91089,
            91090,
            91091,
            91092,
            91093,
            91094,
            91095
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1023",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "977": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-elastic-beach-shorts-aop",
        "variants": [
            78755,
            78756,
            78757,
            78758,
            78759,
            78760,
            78761,
            78762
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "977",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "365": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "crew-socks",
        "variants": [
            44904,
            44905,
            44906
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "365",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1290": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-workout-shorts-aop",
        "variants": [
            96680,
            96681,
            96682,
            96683,
            96684
        ],
        "print_areas": [
            {
                "position": "front_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1290",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1263": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-long-sleeve-dance-dress-aop",
        "variants": [
            95198,
            95199,
            95200,
            95201,
            95202
        ],
        "print_areas": [
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1263",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "1260": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "kids-pajama-pants-aop",
        "variants": [
            95117,
            95118,
            95119,
            95120
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1260",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "361": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-vintage-swimsuit-aop",
        "variants": [
            44820,
            44821,
            44817,
            44825,
            44824,
            44826,
            44823,
            44822,
            44819,
            44818,
            44830,
            44831,
            44827,
            44835,
            44834,
            44836,
            44833,
            44832,
            44829,
            44828,
            44840,
            44841,
            44837,
            44845,
            44844,
            44846,
            44843,
            44842,
            44839,
            44838,
            44850,
            44851,
            44847,
            44855,
            44854,
            44856,
            44853,
            44852,
            44849,
            44848,
            44860,
            44861,
            44857,
            44865,
            44864,
            44866,
            44863,
            44862,
            44859,
            44858,
            44870,
            44871,
            44867,
            44875,
            44874,
            44876,
            44873,
            44872,
            44869,
            44868,
            44880,
            44881,
            44877,
            44885,
            44884,
            44886,
            44883,
            44882,
            44879,
            44878
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "361",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1255": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-long-sleeve-v-neck-shirt-aop",
        "variants": [
            94876,
            94877,
            94878,
            94879,
            94880,
            94881,
            94882,
            94883
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1255",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1217": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "youth-joggers-aop",
        "variants": [
            92323,
            92324,
            92325,
            92326,
            92327
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1217",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1174": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "plus-size-leggings-aop",
        "variants": [
            91238,
            91239,
            91240,
            91241,
            91242
        ],
        "print_areas": [
            {
                "position": "front_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside_label",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1174",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "871": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mid-length-socks",
        "variants": [
            77921
        ],
        "print_areas": [
            {
                "position": "left_side",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_side",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "871",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 48
    },
    "702": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-bike-shorts-aop",
        "variants": [
            73149,
            73150,
            73151,
            73152,
            73153,
            73154
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "702",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 51
    },
    "701": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-capri-leggings-aop",
        "variants": [
            73143,
            73144,
            73145,
            73146,
            73147,
            73148
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "701",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 51
    },
    "1343": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-pu-slide-sandals",
        "variants": [
            102131,
            102140,
            102132,
            102141,
            102133,
            102142,
            102134,
            102143,
            102135,
            102144,
            102136,
            102145,
            102137,
            102146,
            102138,
            102147,
            102139,
            102148
        ],
        "print_areas": [
            {
                "position": "left_shoe",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_shoe",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1343",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 107
    },
    "1280": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "strappy-bikini-set-aop",
        "variants": [
            96436,
            96437,
            96438,
            96439,
            96440,
            96441,
            96442,
            96443,
            96444,
            96445,
            96446,
            96447,
            96448,
            96449,
            96450,
            96451,
            96452,
            96453,
            96454,
            96455,
            96456,
            96457,
            96458,
            96459,
            96460,
            96461,
            96462,
            96463,
            96464,
            96465,
            96466,
            96467,
            96468,
            96469,
            96470
        ],
        "print_areas": [
            {
                "position": "right_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1280",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "960": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "girls-sleeveless-sundress-aop",
        "variants": [
            79704,
            79705,
            79706,
            79707,
            79708,
            79709,
            79710,
            79711
        ],
        "print_areas": [
            {
                "position": "front_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "960",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "757": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-jogger-shorts-aop",
        "variants": [
            74413,
            74414,
            74415,
            74416,
            74417
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_welt_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_welt_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_pocket_welt_inner",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_pocket_welt_outer",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_inner_pocket_front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_inner_pocket_back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_inner_pocket_front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_inner_pocket_back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inner_back_pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "757",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 85
    },
    "740": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-pajama-pants-aop",
        "variants": [
            74879,
            74880,
            74881,
            74882,
            74883,
            74884
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "740",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "700": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "sports-bra-aop",
        "variants": [
            73130,
            73136,
            73131,
            73137,
            73132,
            73138,
            73133,
            73139,
            73134,
            73140
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "700",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 51
    },
    "360": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-classic-one-piece-swimsuit-aop",
        "variants": [
            44768,
            44769,
            44770,
            44771,
            44772,
            44773,
            44774,
            44775,
            44776,
            44777,
            44778,
            44779,
            44780,
            44781,
            44747,
            44748,
            44749,
            44750,
            44751,
            44752,
            44753,
            44803,
            44804,
            44805,
            44806,
            44807,
            44808,
            44809,
            44796,
            44797,
            44798,
            44799,
            44800,
            44801,
            44802,
            44810,
            44811,
            44812,
            44813,
            44814,
            44815,
            44816,
            44789,
            44790,
            44791,
            44792,
            44793,
            44794,
            44795,
            44782,
            44783,
            44784,
            44785,
            44786,
            44787,
            44788,
            44761,
            44762,
            44763,
            44764,
            44765,
            44766,
            44767,
            44754,
            44755,
            44756,
            44757,
            44758,
            44759,
            44760
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "360",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1078": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "basketball-rib-shorts-aop",
        "variants": [
            88684,
            88685,
            88686,
            88687,
            88688,
            88689,
            88690,
            88691
        ],
        "print_areas": [
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1078",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1062": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-tank-top-aop",
        "variants": [
            84109,
            84110,
            84111,
            84112,
            84113,
            84114,
            84115,
            84116
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1062",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "925": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-relaxed-shorts-aop",
        "variants": [
            77614,
            77615,
            77616,
            77617,
            77618,
            77619,
            77620,
            77621,
            77622,
            77623,
            77624,
            77625
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "925",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "858": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "apron-aop",
        "variants": [
            76812,
            76813
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "858",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1283": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-sports-shorts-aop",
        "variants": [
            96413,
            96414,
            96415,
            96416,
            96417,
            96418
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1283",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1087": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-football-jersey-aop",
        "variants": [
            91889,
            91890,
            91891,
            91892,
            91893,
            91894,
            91895,
            91896
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1087",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "947": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-casual-leggings-aop",
        "variants": [
            78566,
            78567,
            78568,
            78569,
            78570,
            78571
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "947",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "822": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-baseball-jersey-aop",
        "variants": [
            75690,
            75691,
            75692,
            75693,
            75694,
            75695,
            75696,
            75697,
            75698,
            75699,
            75700,
            75701
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "822",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1289": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-short-sleeve-shirt-aop",
        "variants": [
            96672,
            96673,
            96674,
            96675,
            96676,
            96677,
            96678,
            96679
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1289",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1282": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "strappy-triangle-bikini-top-aop",
        "variants": [
            96506,
            96507,
            96508,
            96509,
            96510,
            96511,
            96512,
            96513,
            96514,
            96515,
            96516,
            96517,
            96518,
            96519,
            96520,
            96521,
            96522,
            96523,
            96524,
            96525,
            96526,
            96527,
            96528,
            96529,
            96530,
            96531,
            96532,
            96533,
            96534,
            96535,
            96536,
            96537,
            96538,
            96539,
            96540
        ],
        "print_areas": [
            {
                "position": "right_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1282",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1222": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "high-waisted-yoga-shorts-aop",
        "variants": [
            93603,
            93604,
            93605,
            93606,
            93607,
            93608
        ],
        "print_areas": [
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_waistband_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_waistband_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1222",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1177": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-casual-shorts-aop",
        "variants": [
            91323,
            91324,
            91325,
            91326,
            91327
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1177",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "1132": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-biker-shorts-aop",
        "variants": [
            86209,
            86210,
            86211,
            86212,
            86213,
            86214
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1132",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "1084": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "athletic-long-shorts-aop",
        "variants": [
            85197,
            85198,
            85199,
            85200,
            85201,
            85202,
            85203,
            85204
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside_label",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_pocket_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1084",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1037": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-satin-pajamas-aop",
        "variants": [
            80074,
            80072,
            80073,
            80071
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1037",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "576": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "baby-beanie-aop",
        "variants": [
            71671
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "576",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 70
    },
    "508": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-mini-skirt-aop",
        "variants": [
            72977,
            72978,
            72979,
            72980,
            72981
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "508",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 48
    },
    "1284": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "girls-two-piece-swimsuit-aop",
        "variants": [
            96424,
            96425,
            96426,
            96427
        ],
        "print_areas": [
            {
                "position": "front_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_outside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1284",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "452": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "recycled-poly-socks",
        "variants": [
            63289
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "452",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 33
    },
    "934": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-puffer-jacket-aop",
        "variants": [
            77828,
            77833,
            77829,
            77834,
            77830,
            77835,
            77831,
            77836,
            77832,
            77837
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "934",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "739": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-pajama-pants-aop",
        "variants": [
            74886,
            74887,
            74888,
            74889,
            74890,
            74891
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "739",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "407": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-briefs-aop",
        "variants": [
            61893,
            61894,
            61895,
            61896,
            61897,
            61898
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "407",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "919": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "apron-aop",
        "variants": [
            77521,
            77522,
            81426,
            81427,
            81428
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "919",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 48
    },
    "828": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-short-pajama-set-aop",
        "variants": [
            75680,
            75681,
            75682,
            75683,
            75684,
            75685,
            75686,
            75687,
            75688,
            75689
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "828",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "1032": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-loose-t-shirt-aop",
        "variants": [
            83516,
            83517,
            83518,
            83519,
            83520,
            83521,
            83522,
            83523,
            83524
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1032",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "856": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-board-shorts-aop",
        "variants": [
            76804,
            76805,
            76806,
            76807,
            76808
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Pocket_lining_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Pocket_lining_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "856",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "1071": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "seamless-sports-bra-aop",
        "variants": [
            87607,
            87608,
            87609,
            87610,
            87611
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1071",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 240
    },
    "1028": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-hoodie-aop",
        "variants": [
            79861,
            79862,
            79863,
            79864,
            79865,
            79866,
            79867
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood_lining",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood_lining",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1028",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "799": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-bomber-jacket-aop",
        "variants": [
            74999,
            75000,
            75001,
            75002,
            75003
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "799",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "509": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-spandex-leggings-aop",
        "variants": [
            72429,
            72430,
            72431,
            72432,
            72433,
            72434
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "509",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 48
    },
    "949": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "basketball-jersey-aop",
        "variants": [
            79386,
            79387,
            79388,
            79389,
            79390,
            79391
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "949",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "948": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "basketball-shorts-aop",
        "variants": [
            79955,
            78572,
            78573,
            78574,
            78575,
            78576
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "948",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1262": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-skater-dress-aop",
        "variants": [
            95203,
            95204,
            95205,
            95206,
            95207,
            95208
        ],
        "print_areas": [
            {
                "position": "front_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1262",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "703": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "stretchy-leggings-aop",
        "variants": [
            73155,
            73156,
            73157,
            73158,
            73159,
            73160
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "703",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 51
    },
    "593": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-baseball-jersey-aop",
        "variants": [
            72387,
            72388,
            72389,
            72390,
            72391
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "593",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1270": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "athletic-hoodie-aop",
        "variants": [
            95868,
            95869,
            95870,
            95871,
            95872,
            95873,
            95874,
            95875
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "inside_label",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1270",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "1254": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-pajama-pants-aop",
        "variants": [
            94861,
            94862,
            94863,
            94864,
            94865,
            94866,
            94867,
            94868
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1254",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "1251": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-pajama-pants-aop",
        "variants": [
            95503,
            94289,
            94290,
            94291,
            94292,
            94293,
            94294,
            94295
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1251",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "997": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-tank-aop",
        "variants": [
            79352,
            79353,
            79354,
            79355,
            79356,
            79357
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "997",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 90
    },
    "832": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-full-zip-hoodie-aop",
        "variants": [
            75714,
            75715,
            75716,
            75717,
            75718,
            75719,
            75720,
            75721,
            75722,
            75723
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "832",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "285": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-pencil-skirt-aop",
        "variants": [
            43187,
            43189,
            43191,
            43193,
            43195,
            43197
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "285",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "923": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "long-sleeve-kimono-robe-aop",
        "variants": [
            77561,
            77562,
            77563,
            77564,
            77565,
            77566,
            77567,
            77568,
            77569,
            77570,
            77571,
            77572
        ],
        "print_areas": [
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "923",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "281": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-cut-and-sew-tee-aop",
        "variants": [
            43100,
            43101,
            43102,
            43103,
            43104,
            43105,
            43106,
            43107,
            43108,
            43109,
            43110,
            43111,
            43112,
            43113,
            43114,
            43115,
            43116,
            43117,
            43118,
            43119,
            43120,
            43121,
            43122,
            43123
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "281",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "376": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "sublimation-socks",
        "variants": [
            45134,
            45133,
            45132
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "376",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 1
    },
    "924": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-hawaiian-shirt-aop",
        "variants": [
            77587,
            77588,
            77589,
            77590,
            77591,
            77592,
            77593,
            77594,
            77595,
            77596,
            77597,
            77598,
            77599,
            77600,
            77601,
            77602
        ],
        "print_areas": [
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_top",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_bottom",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "924",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "433": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-bomber-jacket-aop",
        "variants": [
            62176,
            62177,
            62178,
            62179,
            62180,
            62181,
            62182,
            62183,
            98594
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "433",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "589": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "swim-trunks-aop",
        "variants": [
            72768,
            72769,
            72770,
            72771,
            72772,
            72773,
            72774
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "589",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "574": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "cushioned-crew-socks",
        "variants": [
            71924
        ],
        "print_areas": [
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "574",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 64
    },
    "1242": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-polyester-tee-aop",
        "variants": [
            94253,
            94254,
            94255,
            94256,
            94257,
            94258,
            94259,
            94260
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1242",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "591": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "athletic-joggers-aop",
        "variants": [
            72926,
            72927,
            72928,
            72929,
            72930,
            72931
        ],
        "print_areas": [
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "591",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "831": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-baseball-jersey-aop",
        "variants": [
            75702,
            75703,
            75704,
            75705,
            75706,
            75707,
            75708,
            75709,
            75710,
            75711,
            75712,
            75713
        ],
        "print_areas": [
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "831",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "349": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-bikini-swimsuit-aop",
        "variants": [
            44533,
            44534,
            44530,
            44538,
            44537,
            44539,
            44536,
            44535,
            44532,
            44531,
            44543,
            44544,
            44540,
            44548,
            44547,
            44549,
            44546,
            44545,
            44542,
            44541,
            44553,
            44554,
            44550,
            44558,
            44557,
            44559,
            44556,
            44555,
            44552,
            44551,
            44563,
            44564,
            44560,
            44568,
            44567,
            44569,
            44566,
            44565,
            44562,
            44561,
            44573,
            44574,
            44570,
            44578,
            44577,
            44579,
            44576,
            44575,
            44572,
            44571,
            44583,
            44584,
            44580,
            44588,
            44587,
            44589,
            44586,
            44585,
            44582,
            44581,
            44593,
            44594,
            44590,
            44598,
            44597,
            44599,
            44596,
            44595,
            44592,
            44591,
            44603,
            44604,
            44600,
            44608,
            44607,
            44609,
            44606,
            44605,
            44602,
            44601
        ],
        "print_areas": [
            {
                "position": "right_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cup",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_panties",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "349",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "256": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-cut-and-sew-casual-leggings-aop",
        "variants": [
            45661,
            45663,
            45665,
            45667,
            45669,
            45671
        ],
        "print_areas": [
            {
                "position": "left_side",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_side",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "256",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "279": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-cut-and-sew-tee-aop",
        "variants": [
            43076,
            43077,
            43078,
            43079,
            43080,
            43081,
            43082,
            43083,
            43084,
            43085,
            43086,
            43087,
            43088,
            43089,
            43090,
            43091,
            43092,
            43093,
            43094,
            43095,
            43096,
            43097,
            43098,
            43099
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "279",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "450": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-pullover-hoodie-aop",
        "variants": [
            63240,
            63241,
            63242,
            63243,
            63244,
            63245
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "450",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "449": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-sweatshirt-aop",
        "variants": [
            63219,
            63220,
            63221,
            63222,
            63223,
            63224
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "449",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "978": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-mid-length-swim-shorts-aop",
        "variants": [
            82422,
            82423,
            82424,
            82425,
            82426,
            82427,
            82428,
            82429,
            82430,
            82431
        ],
        "print_areas": [
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "978",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "516": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "high-waisted-yoga-leggings-aop",
        "variants": [
            67982,
            67983,
            67984,
            67985,
            67986,
            67987
        ],
        "print_areas": [
            {
                "position": "front_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back_waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "516",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "286": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-skater-skirt-aop",
        "variants": [
            43199,
            43201,
            43203,
            43205,
            43207,
            43209
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "286",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "592": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "fashion-hoodie-aop",
        "variants": [
            74644,
            74645,
            74646,
            74647,
            74648
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "sleeves",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "592",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 83
    },
    "406": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-boxer-briefs-aop",
        "variants": [
            61879,
            61880,
            61881,
            61882,
            61883,
            61884,
            61885
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left_leg",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "gusset",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "406",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 14
    },
    "627": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "crop-tee-aop",
        "variants": [
            73371,
            73377,
            73372,
            73378,
            73373,
            73379,
            73374,
            73380,
            73375,
            73381,
            73376,
            73382
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "627",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "431": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "t-shirt-dress-aop",
        "variants": [
            62083,
            62084,
            62085,
            62086,
            62087,
            62088
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "431",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "276": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "womens-cut-and-sew-racerback-dress-aop",
        "variants": [
            43001,
            43002,
            43003,
            43004,
            43005,
            43006
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "276",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    },
    "1261": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "mens-long-sleeve-shirt-aop",
        "variants": [
            95121,
            95122,
            95123,
            95124,
            95125,
            95126,
            95127,
            95128
        ],
        "print_areas": [
            {
                "position": "front",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "Collar",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "1261",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 47
    },
    "451": {
        "tags": tags,
        "title": title,
        "shopId": shopid,
        "description": desc + "unisex-zip-hoodie-aop",
        "variants": [
            63246,
            63247,
            63248,
            63249,
            63250,
            63251
        ],
        "print_areas": [
            {
                "position": "back",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_sleeve",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_hood",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "waistband",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "left_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "right_cuff_panel",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "front_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_right",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            },
            {
                "position": "pocket_left",
                "images": [
                    {
                        "x": 0.5,
                        "y": 0.5,
                        "id": imageid,
                        "angle": 0,
                        "scale": 1.25
                    }
                ]
            }
        ],
        "blueprint_id": "451",
        "print_details": {
            "print_on_side": "regular"
        },
        "print_provider_id": 10
    }
}
    return product


def publish_product():
    url = "https://api.printify.com/v1/shops/{shop_id}/products/{product_id}/publish.json"
    payload = json.dumps({
        "title": True,
        "description": True,
        "images": True,
        "variants": True,
        "tags": True,
        "keyFeatures": True,
        "shipping_template": True
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': printify_token
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def upload_product(image_id, tags, title, prompt, style, hexcode):
    url = "https://api.printify.com/v1/shops/10956921/products.json"
    payload = json.dumps(dims)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': printify_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def upload_img(title, image_url):
    url = "https://api.printify.com/v1/uploads/images.json"

    payload = json.dumps({
        "file_name": title,
        # "contents": "url",
        "url": image_url
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': printify_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    return response.json()

def ai_stuff(query):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Return a completed JSON object like: {title:"",detailed_prompt:"", tags:[],hex_color:'000000'} based on the input for image generation."},
            {"role": "user", "content": query}
        ]
    )

    new_json = completion.choices[0].message.content
    json_object = json.loads(new_json)
    print(json_object)
    # prompt = json_object.get("detailed_prompt")
    # tags = json_object.get("tags")
    # title = json_object.get("title")
    # hexcode = json_object.get("hexcode")

    # # Example DALL-E API call

    return json_object


@app.route('/process-form', methods=['POST'])
def process_form():
    try:
        name = request.json.get('Name')
        email = request.json.get('Email')
        designs = request.json.get('Designs') #vector, splash art etc.
        garment = request.json.get('Garment')
        favorites = request.json.get('Favorites') #description box for generator
        query = designs + "," + favorites #concatenates design + description
        # if not query:
        #     return jsonify({'error': 'Invalid form data. Please provide valid data.'}), 400
        # 2nd bubble on make.com shopify pipeline
        data = ai_stuff(query)
        #Get Image
        dalle_response = openai.Image.create(prompt= query, n=1, size="1024x1024")
        image_link = dalle_response.data[0].url
        print(image_link)
        printify_img = upload_img(data.get("title"), image_link)
        dims = pick_product_dims(printify_img.get("image_id"), data.get("tags"), data.get("title"), data.get("detailed_prompt"), garment, data.get("hexcode"), 10956921)
        upload_product(printify_img.ID, tags, title, prompt, garment, hexcode)

        # Do something with the responses from the APIs and construct the final response
        # For simplicity, we'll just return a success message here
        return jsonify({'success': True}), 200

    except Exception as e:
        print('Error processing form:', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500



if __name__ == '__main__':
    app.run(debug=True)
