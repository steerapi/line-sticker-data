# library to download line sticker data

Quickstart

    import linestickerdata
    linestickerdata.list_available()
    linestickerdata.get_image_paths(folder="data", n=100000, num_workers=64)

To see the list of available data use this command

    linestickerdata.list_available()

    [{'folder': 'dataofficial',
      'category': ['Pop-Up Stickers',
      'Big stickers',
      'BROWN & FRIENDS',
      'Animated Stickers',
      'Humor and Entertainment',
      'Anime',
      'Games',
      'With Voice or Sound',
      'Kids Cartoons',
      'Horoscope',
      'Music sticker',
      'TV Stars',
      'Cartoons',
      'Love and Romance',
      'Manga',
      "Official Creators' Stickers",
      'Disney',
      'Sanrio',
      'Characters',
      'Custom stickers'],
      'total': 2948,
      'count': {'Animated Stickers': 967,
      'With Voice or Sound': 613,
      'Music sticker': 43,
      'Sanrio': 65,
      'Cartoons': 90,
      'Humor and Entertainment': 66,
      'Horoscope': 1,
      'TV Stars': 90,
      'Manga': 142,
      'Pop-Up Stickers': 149,
      'BROWN & FRIENDS': 68,
      'Characters': 241,
      "Official Creators' Stickers": 3,
      'Disney': 145,
      'Big stickers': 12,
      'Games': 36,
      'Kids Cartoons': 54,
      'Anime': 76,
      'Custom stickers': 46,
      'Love and Romance': 41}},
    {'folder': 'dataofficial-th',
      'category': ['ครีเอเตอร์ทางการ',
      'BROWN&FRIENDS',
      'มาสคอต',
      'สติกเกอร์แอนิเมชัน',
      'ความรักและโรแมนติก',
      'สติกเกอร์เติมคำ',
      'การ์ตูนเด็ก',
      'ดารา & คนดัง',
      'ดิสนีย์',
      'อนิเมะ',
      'สติกเกอร์มีเสียง',
      'ดวงชะตาราศี',
      'เกม',
      'สติกเกอร์ป๊อปอัพ',
      'บิ๊กสติกเกอร์',
      'ตลกขบขัน',
      'ซานริโอ้',
      'มังงะ',
      'การ์ตูน',
      'มิวสิคสติกเกอร์'],
      'total': 2922,
      'count': {'บิ๊กสติกเกอร์': 11,
      'ความรักและโรแมนติก': 41,
      'ดารา & คนดัง': 85,
      'ครีเอเตอร์ทางการ': 3,
      'ตลกขบขัน': 66,
      'สติกเกอร์เติมคำ': 41,
      'การ์ตูน': 88,
      'สติกเกอร์แอนิเมชัน': 962,
      'BROWN&FRIENDS': 68,
      'ดิสนีย์': 144,
      'สติกเกอร์มีเสียง': 611,
      'ดวงชะตาราศี': 1,
      'ซานริโอ้': 65,
      'มังงะ': 140,
      'อนิเมะ': 73,
      'การ์ตูนเด็ก': 54,
      'มิวสิคสติกเกอร์': 43,
      'เกม': 36,
      'มาสคอต': 241,
      'สติกเกอร์ป๊อปอัพ': 149}},
    {'folder': 'data',
      'taste': ['Polite Language',
      'Seasonal',
      'Gorgeous',
      'Dialects & Slang',
      'Speech Balloons',
      'Humorous',
      'Greetings',
      'Warm & Fuzzy',
      'Cute',
      'Cool',
      'Wacky'],
      'character': ['Female Characters',
      'Rabbits',
      'Male Characters',
      'Pandas',
      'Birds',
      'Bears',
      'Weird',
      'Families & Couples',
      'Seals',
      'Names',
      'Dogs',
      'Cats',
      'Food',
      'Other'],
      'total': 357361,
      'count': {'Gorgeous': 28127,
      'Food': 23821,
      'Names': 54413,
      'Dogs': 24892,
      'Other': 50951,
      'Rabbits': 23737,
      'Female Characters': 38145,
      'Families & Couples': 29035,
      'Male Characters': 37325,
      'Cats': 30389,
      'Pandas': 7705,
      'Birds': 17307,
      'Seals': 2515,
      'Bears': 17126,
      'Greetings': 28684,
      'Weird': 44552,
      'Polite Language': 16073,
      'Humorous': 47116,
      'Cool': 23471,
      'Dialects & Slang': 27144,
      'Cute': 58422,
      'Seasonal': 13303,
      'Speech Balloons': 14157,
      'Warm & Fuzzy': 56312}},
    {'folder': 'data-th',
      'taste': ['ตลก',
      'เทศกาล',
      'ทักทาย',
      'ภาษาท้องถิ่น, สแลง',
      'น่ารัก',
      'เท่',
      'บอลลูนข้อความ',
      'สวยเริ่ด',
      'อบอุ่น',
      'แปลก',
      'ภาษาสุภาพ'],
      'character': ['หมี',
      'ชื่อ',
      'สุนัข',
      'หญิง',
      'นก',
      'อาหาร',
      'แมว',
      'ครอบครัว, คู่รัก',
      'แมวน้ำ',
      'แพนด้า',
      'กระต่าย',
      'อื่นๆ',
      'ชาย'],
      'total': 245513,
      'count': {'ทักทาย': 28692,
      'แพนด้า': 6525,
      'นก': 14179,
      'สุนัข': 20362,
      'กระต่าย': 16865,
      'หมี': 14256,
      'อาหาร': 17295,
      'อื่นๆ': 31848,
      'ครอบครัว, คู่รัก': 23555,
      'หญิง': 24756,
      'แมวน้ำ': 1868,
      'แมว': 18781,
      'ชาย': 25202,
      'ชื่อ': 30021,
      'น่ารัก': 59032,
      'เท่': 23624,
      'เทศกาล': 13552,
      'ตลก': 47172,
      'อบอุ่น': 57357,
      'สวยเริ่ด': 16084}}]

The data is divided into 4 folders

    data # from line en creator store
    data-th # from line th creator store
    dataofficial # from line en official store
    dataofficial-th # from line th official store

Stickers from the official store is divided into categories.
Stickers from the creator store is divided into tastes and characters. There is a total count and a count per category, taste or character.

Use this command to download and extract stickers

    linestickerdata.get_image_paths(folder="data", n=100000, num_workers=64)

You can specify `folder`, `category`, `taste`, `character` of the stickers you want to download. `n` is the number of stickers to download. You can also specify `location` where you want to file to be stored. This function returns paths to all the sticker images that has been downloaded. `num_workers` specifies the number of workers that use to download the stickers.