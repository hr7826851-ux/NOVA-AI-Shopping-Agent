import csv
import random

random.seed(42)

products = []

product_id = 1


# ============================================================
# PRODUCT DATA
# 100 PRODUCTS PER CATEGORY
# ============================================================

categories = {

    "Electronics": [

        ("OnePlus Nord 5", "OnePlus", 29999, 4.5),
        ("OnePlus 13R", "OnePlus", 39999, 4.6),
        ("OnePlus Nord CE 5", "OnePlus", 24999, 4.4),
        ("iQOO Neo 10", "iQOO", 31999, 4.6),
        ("iQOO Z10", "iQOO", 23999, 4.5),
        ("iQOO Z10x", "iQOO", 17999, 4.3),
        ("POCO F7", "POCO", 29999, 4.4),
        ("POCO X7 Pro", "POCO", 26999, 4.5),
        ("POCO X7", "POCO", 21999, 4.3),
        ("Samsung Galaxy A56", "Samsung", 27999, 4.3),
        ("Samsung Galaxy S24 FE", "Samsung", 44999, 4.5),
        ("Samsung Galaxy A36", "Samsung", 23999, 4.3),
        ("Samsung Galaxy M36", "Samsung", 16999, 4.2),
        ("Nothing Phone 3a", "Nothing", 25999, 4.3),
        ("Nothing Phone 3a Pro", "Nothing", 29999, 4.4),
        ("Google Pixel 9a", "Google", 49999, 4.5),
        ("Google Pixel 9", "Google", 64999, 4.5),
        ("Motorola Edge 60 Pro", "Motorola", 29999, 4.5),
        ("Motorola Edge 60 Fusion", "Motorola", 22999, 4.4),
        ("Motorola G85", "Motorola", 18999, 4.3),

        ("HP Victus Gaming Laptop", "HP", 64999, 4.5),
        ("HP Pavilion Plus", "HP", 69999, 4.4),
        ("HP 15 Laptop", "HP", 52999, 4.2),
        ("HP Envy x360", "HP", 79999, 4.5),
        ("Lenovo LOQ Gaming Laptop", "Lenovo", 69999, 4.6),
        ("Lenovo IdeaPad Gaming 3", "Lenovo", 61999, 4.4),
        ("Lenovo IdeaPad Slim 5", "Lenovo", 64999, 4.5),
        ("Lenovo Legion 5", "Lenovo", 109999, 4.7),
        ("ASUS TUF Gaming F15", "ASUS", 72999, 4.5),
        ("ASUS TUF Gaming A15", "ASUS", 79999, 4.6),
        ("ASUS Vivobook 15", "ASUS", 55999, 4.3),
        ("ASUS ROG Strix G16", "ASUS", 119999, 4.7),
        ("Acer Nitro V", "Acer", 69999, 4.5),
        ("Acer Aspire 5", "Acer", 52999, 4.3),
        ("Acer Predator Helios Neo", "Acer", 109999, 4.6),

        ("Samsung 43 Inch Smart TV", "Samsung", 32999, 4.4),
        ("LG 43 Inch 4K Smart TV", "LG", 35999, 4.5),
        ("Sony Bravia 43 Inch", "Sony", 44999, 4.6),
        ("TCL 55 Inch QLED TV", "TCL", 41999, 4.4),
        ("OnePlus 43 Inch TV", "OnePlus", 27999, 4.2),

        ("Apple iPad 11", "Apple", 39999, 4.6),
        ("Samsung Galaxy Tab S9 FE", "Samsung", 32999, 4.5),
        ("OnePlus Pad 2", "OnePlus", 39999, 4.6),
        ("Lenovo Tab P12", "Lenovo", 29999, 4.4),
        ("Xiaomi Pad 7", "Xiaomi", 27999, 4.5),

        ("Apple MacBook Air M4", "Apple", 99999, 4.8),
        ("MacBook Air M3", "Apple", 89999, 4.7),
        ("Dell Inspiron 15", "Dell", 57999, 4.3),
        ("Dell G15 Gaming", "Dell", 74999, 4.5),
        ("MSI Thin 15", "MSI", 69999, 4.4),

    ],

    "Fashion": [

        ("Allen Solly Casual Shirt", "Allen Solly", 1299, 4.2),
        ("Peter England Formal Shirt", "Peter England", 1499, 4.3),
        ("Levis 511 Jeans", "Levis", 2499, 4.5),
        ("Levis 512 Jeans", "Levis", 2699, 4.4),
        ("Levis Regular Fit Jeans", "Levis", 2299, 4.3),
        ("Allen Solly Polo T-Shirt", "Allen Solly", 999, 4.2),
        ("Van Heusen Polo T-Shirt", "Van Heusen", 1199, 4.3),
        ("Puma Casual T-Shirt", "Puma", 899, 4.4),
        ("Adidas Sports T-Shirt", "Adidas", 1299, 4.5),
        ("Nike Dri-FIT T-Shirt", "Nike", 1799, 4.6),
        ("Roadster Casual Shirt", "Roadster", 799, 4.2),
        ("H&M Oversized T-Shirt", "H&M", 999, 4.3),
        ("Zara Basic Shirt", "Zara", 1999, 4.4),
        ("Mast & Harbour Shirt", "Mast & Harbour", 899, 4.2),
        ("WROGN Casual Shirt", "WROGN", 1099, 4.3),
        ("Jack & Jones Shirt", "Jack & Jones", 1799, 4.4),
        ("U.S. Polo Assn Shirt", "U.S. Polo Assn", 1599, 4.5),
        ("Flying Machine Jeans", "Flying Machine", 1999, 4.3),
        ("Spykar Slim Jeans", "Spykar", 2299, 4.4),
        ("Mufti Casual Jeans", "Mufti", 1899, 4.3),

        ("Nike Revolution 7", "Nike", 3499, 4.5),
        ("Nike Air Max SC", "Nike", 7999, 4.6),
        ("Adidas Grand Court", "Adidas", 2999, 4.4),
        ("Adidas Runfalcon", "Adidas", 3499, 4.5),
        ("Puma Caven 2.0", "Puma", 2799, 4.3),
        ("Puma Softride", "Puma", 3299, 4.4),
        ("Reebok Club C", "Reebok", 3999, 4.4),
        ("Reebok Running Shoes", "Reebok", 3499, 4.3),
        ("Skechers Go Walk", "Skechers", 4999, 4.6),
        ("Woodland Casual Shoes", "Woodland", 3999, 4.4),

        ("H&M Slim Fit Jeans", "H&M", 1799, 4.2),
        ("Zara Straight Jeans", "Zara", 2999, 4.4),
        ("Roadster Skinny Jeans", "Roadster", 1299, 4.2),
        ("WROGN Slim Jeans", "WROGN", 1899, 4.3),
        ("Flying Machine Straight Jeans", "Flying Machine", 1799, 4.3),
        ("Spykar Regular Jeans", "Spykar", 2199, 4.4),
        ("Levis Trucker Jacket", "Levis", 3999, 4.5),
        ("H&M Denim Jacket", "H&M", 2499, 4.3),
        ("Roadster Bomber Jacket", "Roadster", 1999, 4.2),
        ("Puma Hooded Jacket", "Puma", 2999, 4.4),

        ("Nike Sports Shorts", "Nike", 1499, 4.5),
        ("Adidas Training Shorts", "Adidas", 1299, 4.4),
        ("Puma Running Shorts", "Puma", 999, 4.3),
        ("Jockey Track Pants", "Jockey", 1299, 4.5),
        ("HRX Track Pants", "HRX", 1499, 4.4),
        ("Adidas Track Pants", "Adidas", 1999, 4.5),

        ("Van Heusen Formal Trousers", "Van Heusen", 1799, 4.3),
        ("Allen Solly Formal Trousers", "Allen Solly", 1699, 4.3),
        ("Peter England Formal Trousers", "Peter England", 1599, 4.2),
        ("Louis Philippe Formal Trousers", "Louis Philippe", 2499, 4.5),

        ("Raymond Formal Shirt", "Raymond", 2199, 4.5),
        ("Louis Philippe Shirt", "Louis Philippe", 2499, 4.6),
        ("Van Heusen Shirt", "Van Heusen", 1899, 4.4),
        ("Arrow Formal Shirt", "Arrow", 2299, 4.5),
        ("Park Avenue Shirt", "Park Avenue", 1699, 4.3),

        ("Levis Graphic T-Shirt", "Levis", 1199, 4.3),
        ("Puma Graphic T-Shirt", "Puma", 1099, 4.4),
        ("Adidas Essentials T-Shirt", "Adidas", 1399, 4.5),
        ("Nike Sportswear T-Shirt", "Nike", 1699, 4.5),
        ("H&M Cotton T-Shirt", "H&M", 699, 4.2),
        ("Zara Basic T-Shirt", "Zara", 999, 4.3),

        ("Puma Flip Flops", "Puma", 799, 4.2),
        ("Adidas Adilette Slides", "Adidas", 1299, 4.4),
        ("Nike Victori One Slides", "Nike", 1999, 4.5),
        ("Sparx Casual Shoes", "Sparx", 1299, 4.2),
        ("Bata Casual Shoes", "Bata", 1499, 4.3),

        ("Mochi Formal Shoes", "Mochi", 2999, 4.4),
        ("Bata Formal Shoes", "Bata", 2499, 4.3),
        ("Red Tape Formal Shoes", "Red Tape", 1999, 4.4),
        ("Woodland Leather Shoes", "Woodland", 4499, 4.5),
        ("Clarks Formal Shoes", "Clarks", 6999, 4.6),

        ("Roadster Hoodie", "Roadster", 1499, 4.3),
        ("H&M Pullover Hoodie", "H&M", 1999, 4.4),
        ("Puma Essentials Hoodie", "Puma", 2499, 4.5),
        ("Adidas Hoodie", "Adidas", 2999, 4.5),
        ("Nike Club Fleece Hoodie", "Nike", 3999, 4.6),

        ("Allen Solly Kurta", "Allen Solly", 1599, 4.3),
        ("Manyavar Kurta", "Manyavar", 2499, 4.5),
        ("Fabindia Kurta", "Fabindia", 1999, 4.4),
        ("Biba Kurta", "Biba", 1799, 4.4),
        ("W for Woman Kurta", "W", 1899, 4.3),
        ("Libas Kurta", "Libas", 1499, 4.3),
        ("Max Casual Dress", "Max", 1299, 4.2),
        ("H&M Casual Dress", "H&M", 1999, 4.4),
        ("Zara Midi Dress", "Zara", 2999, 4.5),
        ("Biba Ethnic Dress", "Biba", 2299, 4.4),

        ("Fastrack Sunglasses", "Fastrack", 999, 4.3),
        ("Ray-Ban Classic Sunglasses", "Ray-Ban", 7999, 4.7),
        ("Vogue Sunglasses", "Vogue", 3999, 4.5),
        ("Titan Sunglasses", "Titan", 1999, 4.4),
        ("Fossil Leather Belt", "Fossil", 2499, 4.5),
        ("Levis Leather Belt", "Levis", 999, 4.3),
        ("Tommy Hilfiger Belt", "Tommy Hilfiger", 2499, 4.5),
        ("Wildcraft Wallet", "Wildcraft", 899, 4.4),
        ("Levis Wallet", "Levis", 799, 4.3),
        ("Puma Cap", "Puma", 699, 4.2),
    ],

    "Gaming": [

        ("Logitech G102", "Logitech", 1299, 4.5),
        ("Logitech G502 Hero", "Logitech", 3499, 4.6),
        ("Logitech G304", "Logitech", 2999, 4.6),
        ("Razer DeathAdder Essential", "Razer", 1799, 4.5),
        ("Razer Basilisk V3", "Razer", 3999, 4.7),
        ("Razer Viper Mini", "Razer", 2999, 4.6),
        ("ASUS TUF Gaming Mouse", "ASUS", 1999, 4.3),
        ("HyperX Pulsefire Core", "HyperX", 1999, 4.4),
        ("SteelSeries Rival 3", "SteelSeries", 2999, 4.5),
        ("Corsair Harpoon RGB", "Corsair", 2499, 4.4),

        ("Redragon K552", "Redragon", 2499, 4.4),
        ("Redragon K617", "Redragon", 2999, 4.5),
        ("Logitech G213 Keyboard", "Logitech", 3999, 4.5),
        ("Logitech G413", "Logitech", 4999, 4.6),
        ("Razer Cynosa Lite", "Razer", 2999, 4.4),
        ("Razer BlackWidow V3", "Razer", 6999, 4.6),
        ("HyperX Alloy Origins", "HyperX", 6999, 4.6),
        ("Corsair K55 RGB", "Corsair", 4999, 4.5),
        ("ASUS TUF K3", "ASUS", 5999, 4.5),
        ("HP GK320", "HP", 1999, 4.2),

        ("Sony INZONE H5", "Sony", 11999, 4.6),
        ("HyperX Cloud II", "HyperX", 6999, 4.6),
        ("Razer BlackShark V2", "Razer", 7999, 4.7),
        ("Logitech G435", "Logitech", 5999, 4.5),
        ("SteelSeries Arctis Nova 7", "SteelSeries", 13999, 4.7),
        ("Corsair HS55", "Corsair", 4999, 4.4),
        ("JBL Quantum 100", "JBL", 2499, 4.3),
        ("Boat Immortal 700", "boAt", 2499, 4.2),
        ("Redragon H510", "Redragon", 2999, 4.4),
        ("ASUS TUF H3", "ASUS", 3999, 4.4),

        ("Xbox Wireless Controller", "Microsoft", 5499, 4.6),
        ("PS5 DualSense Controller", "Sony", 5499, 4.8),
        ("8BitDo Ultimate Controller", "8BitDo", 5999, 4.6),
        ("Redgear Pro Wireless", "Redgear", 1799, 4.3),
        ("Cosmic Byte C1070", "Cosmic Byte", 1699, 4.3),
        ("PowerA Wired Controller", "PowerA", 2999, 4.4),
        ("Ant Esports GP300", "Ant Esports", 1299, 4.2),
        ("EvoFox Elite X", "EvoFox", 1999, 4.3),
        ("GameSir G7", "GameSir", 4999, 4.5),
        ("GameSir T4 Kaleid", "GameSir", 3999, 4.5),

        ("ASUS TUF Gaming Monitor 24", "ASUS", 12999, 4.5),
        ("Acer Nitro 24 Gaming Monitor", "Acer", 11999, 4.5),
        ("LG UltraGear 24", "LG", 14999, 4.6),
        ("Samsung Odyssey G3", "Samsung", 15999, 4.5),
        ("MSI G244F", "MSI", 13999, 4.6),
        ("BenQ MOBIUZ EX240", "BenQ", 17999, 4.7),
        ("AOC Gaming Monitor", "AOC", 12999, 4.4),
        ("ViewSonic Gaming Monitor", "ViewSonic", 14999, 4.5),
        ("Lenovo Legion Monitor", "Lenovo", 16999, 4.6),
        ("HP Omen Gaming Monitor", "HP", 18999, 4.6),

        ("Razer Gigantus Mouse Pad", "Razer", 1499, 4.5),
        ("Logitech G640 Mouse Pad", "Logitech", 2499, 4.6),
        ("HyperX Fury Mouse Pad", "HyperX", 1299, 4.5),
        ("Redragon Mouse Pad", "Redragon", 799, 4.3),
        ("Cosmic Byte Mouse Pad", "Cosmic Byte", 599, 4.2),
        ("Ant Esports Mouse Pad", "Ant Esports", 499, 4.2),
        ("SteelSeries QcK", "SteelSeries", 1499, 4.6),
        ("ASUS ROG Mouse Pad", "ASUS", 1999, 4.5),
        ("AmazonBasics Gaming Mouse Pad", "AmazonBasics", 699, 4.1),
        ("Zebronics Gaming Mouse Pad", "Zebronics", 599, 4.2),

        ("HP Victus Gaming Laptop", "HP", 64999, 4.5),
        ("Lenovo LOQ Gaming Laptop", "Lenovo", 69999, 4.6),
        ("ASUS TUF Gaming F15", "ASUS", 72999, 4.5),
        ("Acer Nitro V", "Acer", 69999, 4.5),
        ("MSI Thin 15", "MSI", 69999, 4.4),
        ("Dell G15", "Dell", 74999, 4.5),
        ("Lenovo Legion 5", "Lenovo", 109999, 4.7),
        ("ASUS ROG Strix G16", "ASUS", 119999, 4.7),
        ("Acer Predator Helios", "Acer", 109999, 4.6),
        ("HP Omen Gaming Laptop", "HP", 99999, 4.6),

        ("Ant Esports Gaming Chair", "Ant Esports", 8999, 4.2),
        ("Green Soul Gaming Chair", "Green Soul", 12999, 4.5),
        ("Drogo Gaming Chair", "Drogo", 9999, 4.3),
        ("Wakefit Gaming Chair", "Wakefit", 10999, 4.4),
        ("CELLBELL Gaming Chair", "CELLBELL", 8999, 4.3),
        ("Green Soul Monster Chair", "Green Soul", 15999, 4.6),
        ("BeAAtho Gaming Chair", "BeAAtho", 7999, 4.2),
        ("Savya Home Gaming Chair", "Savya Home", 9999, 4.3),
        ("Dowinx Gaming Chair", "Dowinx", 17999, 4.5),
        ("Arozzi Gaming Chair", "Arozzi", 24999, 4.6),

        ("Elgato Stream Deck", "Elgato", 12999, 4.7),
        ("Elgato Wave 3", "Elgato", 14999, 4.6),
        ("Blue Yeti Microphone", "Logitech", 9999, 4.6),
        ("HyperX QuadCast", "HyperX", 11999, 4.7),
        ("Razer Seiren Mini", "Razer", 3999, 4.5),
        ("FIFINE K669B", "FIFINE", 2999, 4.4),
        ("Maono AU-A04", "Maono", 3999, 4.5),
        ("Redgear Cosmo", "Redgear", 1999, 4.2),
        ("Zebronics Zeb-Mic", "Zebronics", 1499, 4.1),
        ("Ant Esports KM500", "Ant Esports", 2499, 4.2),
    ],

    "Audio": [

        ("Boat Rockerz 550", "boAt", 1799, 4.3),
        ("Sony WH-CH720N", "Sony", 7999, 4.5),
        ("JBL Tune 770NC", "JBL", 5999, 4.4),
        ("Sony WH-1000XM5", "Sony", 24999, 4.8),
        ("Bose QuietComfort", "Bose", 22999, 4.7),
        ("Sennheiser Accentum", "Sennheiser", 8999, 4.6),
        ("OnePlus Buds 3", "OnePlus", 5499, 4.5),
        ("Nothing Ear", "Nothing", 8999, 4.6),
        ("Samsung Galaxy Buds FE", "Samsung", 4999, 4.4),
        ("Apple AirPods 4", "Apple", 12999, 4.6),

        ("Apple AirPods Pro 2", "Apple", 22999, 4.8),
        ("OnePlus Buds Pro 3", "OnePlus", 10999, 4.6),
        ("Realme Buds Air 6", "Realme", 2999, 4.4),
        ("Realme Buds Air 7", "Realme", 3499, 4.5),
        ("JBL Live Beam 3", "JBL", 11999, 4.6),
        ("JBL Wave Beam", "JBL", 2499, 4.3),
        ("Sony WF-C700N", "Sony", 7999, 4.5),
        ("Sony WF-1000XM5", "Sony", 19999, 4.8),
        ("Bose QuietComfort Ultra Earbuds", "Bose", 24999, 4.7),
        ("Sennheiser Momentum 4", "Sennheiser", 24999, 4.7),

        ("JBL Flip 6", "JBL", 9999, 4.6),
        ("JBL Charge 5", "JBL", 13999, 4.7),
        ("Sony SRS-XB100", "Sony", 4499, 4.5),
        ("Sony SRS-XE300", "Sony", 11999, 4.6),
        ("Bose SoundLink Flex", "Bose", 14999, 4.7),
        ("Marshall Emberton II", "Marshall", 15999, 4.7),
        ("Marshall Acton III", "Marshall", 29999, 4.8),
        ("Boat Stone 1200", "boAt", 4999, 4.4),
        ("Boat Stone 350", "boAt", 1999, 4.3),
        ("Tribit StormBox", "Tribit", 6999, 4.5),

        ("Anker Soundcore Speaker", "Anker", 3999, 4.6),
        ("Anker Soundcore Motion+", "Anker", 8999, 4.6),
        ("Portronics Sound Drum", "Portronics", 2499, 4.3),
        ("Zebronics Zeb-Sound", "Zebronics", 1999, 4.2),
        ("Mivi Roam 2", "Mivi", 1799, 4.2),
        ("Mivi Play", "Mivi", 1499, 4.1),
        ("Infinity Glide", "Infinity", 1999, 4.2),
        ("Philips Bluetooth Speaker", "Philips", 2999, 4.2),
        ("Sony Party Speaker", "Sony", 19999, 4.5),
        ("JBL PartyBox Encore", "JBL", 34999, 4.7),

        ("Boat Airdopes 141", "boAt", 1299, 4.2),
        ("Boat Airdopes 161", "boAt", 1199, 4.2),
        ("Noise Buds VS104", "Noise", 999, 4.1),
        ("Noise Buds X", "Noise", 1499, 4.2),
        ("Boult Audio Z20", "Boult", 1299, 4.2),
        ("Boult Audio Z40", "Boult", 1499, 4.3),
        ("Fire-Boltt Phoenix Earbuds", "Fire-Boltt", 999, 4.0),
        ("pTron Bassbuds", "pTron", 899, 4.0),
        ("Oppo Enco Buds 2", "Oppo", 1699, 4.3),
        ("OnePlus Nord Buds 3", "OnePlus", 2299, 4.4),

        ("JBL Tune 510BT", "JBL", 2999, 4.3),
        ("Sony WH-CH520", "Sony", 4499, 4.4),
        ("OnePlus Bullets Wireless", "OnePlus", 1999, 4.2),
        ("Boat Rockerz 450", "boAt", 1499, 4.2),
        ("Boat Rockerz 660", "boAt", 2499, 4.3),
        ("Noise Airwave", "Noise", 1999, 4.2),
        ("Boult ProBass", "Boult", 1799, 4.2),
        ("JBL Live 460NC", "JBL", 6999, 4.4),
        ("Sony WH-XB910N", "Sony", 12999, 4.5),
        ("Sennheiser HD 450BT", "Sennheiser", 8999, 4.5),

        ("JBL Bar 2.1", "JBL", 19999, 4.5),
        ("Sony HT-S40R", "Sony", 29999, 4.6),
        ("Boat Aavante Bar", "boAt", 5999, 4.2),
        ("Samsung Soundbar B450", "Samsung", 11999, 4.4),
        ("LG Soundbar", "LG", 14999, 4.4),
        ("Philips Soundbar", "Philips", 9999, 4.2),
        ("Zebronics Soundbar", "Zebronics", 3999, 4.1),
        ("Portronics Sound Slick", "Portronics", 3499, 4.2),
        ("Sony HT-A3000", "Sony", 79999, 4.7),
        ("Bose Smart Soundbar", "Bose", 39999, 4.7),

        ("Fifine Gaming Microphone", "FIFINE", 3999, 4.4),
        ("Maono USB Microphone", "Maono", 3499, 4.4),
        ("HyperX SoloCast", "HyperX", 4999, 4.5),
        ("Razer Seiren Mini", "Razer", 3999, 4.5),
        ("Blue Snowball", "Logitech", 4999, 4.4),
        ("Elgato Wave Neo", "Elgato", 6999, 4.5),
        ("Sony Lavalier Microphone", "Sony", 4999, 4.2),
        ("Boya BY-M1", "Boya", 899, 4.3),
        ("Rode NT-USB Mini", "Rode", 10999, 4.6),
        ("Audio Technica ATR2500", "Audio Technica", 8999, 4.5),

        ("JBL C100SI", "JBL", 799, 4.1),
        ("Sony MDR-EX155", "Sony", 999, 4.2),
        ("Sennheiser CX 80S", "Sennheiser", 1299, 4.3),
        ("Boat Bassheads 100", "boAt", 499, 4.1),
        ("Realme Buds 2", "Realme", 599, 4.1),
        ("OnePlus Nord Wired", "OnePlus", 799, 4.2),
        ("Samsung Type-C Earphones", "Samsung", 999, 4.2),
        ("JBL Endurance Run", "JBL", 999, 4.2),
        ("Sony MDR-ZX110", "Sony", 1299, 4.3),
        ("Philips Wired Headphones", "Philips", 999, 4.1),
    ],

    "Home": [

        ("IKEA Study Lamp", "IKEA", 1299, 4.4),
        ("Philips Air Fryer", "Philips", 6999, 4.5),
        ("Prestige Electric Kettle", "Prestige", 1499, 4.3),
        ("Philips LED Desk Lamp", "Philips", 999, 4.3),
        ("Wipro Smart Bulb", "Wipro", 799, 4.2),
        ("Syska LED Bulb", "Syska", 399, 4.1),
        ("Havells LED Bulb", "Havells", 449, 4.2),
        ("Bajaj LED Lamp", "Bajaj", 699, 4.2),
        ("Orient Table Lamp", "Orient", 999, 4.3),
        ("Havells Table Lamp", "Havells", 1299, 4.4),

        ("Prestige Mixer Grinder", "Prestige", 2999, 4.4),
        ("Bajaj Mixer Grinder", "Bajaj", 2799, 4.3),
        ("Philips Mixer Grinder", "Philips", 3499, 4.5),
        ("Preethi Zodiac Mixer", "Preethi", 7999, 4.5),
        ("Butterfly Mixer Grinder", "Butterfly", 2999, 4.3),
        ("Morphy Richards Mixer", "Morphy Richards", 4999, 4.4),
        ("Bosch Mixer Grinder", "Bosch", 5999, 4.5),
        ("Havells Mixer Grinder", "Havells", 4499, 4.4),
        ("Usha Mixer Grinder", "Usha", 2799, 4.2),
        ("Sujata Dynamix Mixer", "Sujata", 3999, 4.5),

        ("Philips Air Fryer 4L", "Philips", 6999, 4.5),
        ("Instant Vortex Air Fryer", "Instant", 8999, 4.6),
        ("Agaro Air Fryer", "Agaro", 4999, 4.4),
        ("Pigeon Air Fryer", "Pigeon", 3999, 4.2),
        ("Wonderchef Air Fryer", "Wonderchef", 5999, 4.4),
        ("Havells Air Fryer", "Havells", 6999, 4.5),
        ("Prestige Air Fryer", "Prestige", 4999, 4.3),
        ("Inalsa Air Fryer", "Inalsa", 4499, 4.3),
        ("Morphy Richards Air Fryer", "Morphy Richards", 7999, 4.5),
        ("Usha Air Fryer", "Usha", 4499, 4.2),

        ("Prestige Electric Kettle", "Prestige", 1499, 4.3),
        ("Philips Electric Kettle", "Philips", 1699, 4.4),
        ("Pigeon Electric Kettle", "Pigeon", 999, 4.2),
        ("Havells Electric Kettle", "Havells", 1999, 4.4),
        ("Bajaj Electric Kettle", "Bajaj", 1299, 4.2),
        ("Morphy Richards Kettle", "Morphy Richards", 2499, 4.4),
        ("Butterfly Electric Kettle", "Butterfly", 1099, 4.2),
        ("AGARO Electric Kettle", "AGARO", 1399, 4.3),
        ("Milton Electric Kettle", "Milton", 1299, 4.2),
        ("Crompton Electric Kettle", "Crompton", 1499, 4.3),

        ("Dyson V8 Vacuum Cleaner", "Dyson", 29999, 4.7),
        ("Eureka Forbes Vacuum", "Eureka Forbes", 8999, 4.4),
        ("Philips Vacuum Cleaner", "Philips", 6999, 4.3),
        ("Karcher Vacuum Cleaner", "Karcher", 9999, 4.5),
        ("Inalsa Vacuum Cleaner", "Inalsa", 4999, 4.2),
        ("Agaro Vacuum Cleaner", "Agaro", 5999, 4.3),
        ("Eureka Forbes Robo Vacuum", "Eureka Forbes", 19999, 4.4),
        ("Mi Robot Vacuum", "Xiaomi", 24999, 4.5),
        ("ECOVACS Robot Vacuum", "ECOVACS", 29999, 4.6),
        ("Dreame Robot Vacuum", "Dreame", 34999, 4.6),

        ("Wakefit Memory Foam Pillow", "Wakefit", 999, 4.5),
        ("SleepyCat Pillow", "SleepyCat", 1299, 4.5),
        ("SleepyCat Mattress", "SleepyCat", 12999, 4.6),
        ("Wakefit Mattress", "Wakefit", 10999, 4.5),
        ("Duroflex Mattress", "Duroflex", 14999, 4.6),
        ("Kurlon Mattress", "Kurlon", 9999, 4.4),
        ("Nilkamal Chair", "Nilkamal", 1999, 4.3),
        ("IKEA Office Chair", "IKEA", 7999, 4.5),
        ("Wakefit Office Chair", "Wakefit", 6999, 4.4),
        ("Green Soul Office Chair", "Green Soul", 8999, 4.5),

        ("Milton Water Bottle", "Milton", 599, 4.4),
        ("Cello Water Bottle", "Cello", 499, 4.3),
        ("Borosil Glass Bottle", "Borosil", 699, 4.4),
        ("Tupperware Bottle", "Tupperware", 799, 4.4),
        ("Milton Thermosteel Bottle", "Milton", 999, 4.5),
        ("Borosil Thermos", "Borosil", 1299, 4.5),
        ("Prestige Pressure Cooker", "Prestige", 2499, 4.5),
        ("Hawkins Pressure Cooker", "Hawkins", 2299, 4.5),
        ("Pigeon Pressure Cooker", "Pigeon", 1799, 4.3),
        ("Butterfly Pressure Cooker", "Butterfly", 1899, 4.3),

        ("IKEA Storage Box", "IKEA", 599, 4.3),
        ("Nilkamal Storage Cabinet", "Nilkamal", 3999, 4.3),
        ("AmazonBasics Storage Box", "AmazonBasics", 799, 4.2),
        ("Cello Storage Container", "Cello", 699, 4.3),
        ("Milton Storage Container", "Milton", 599, 4.3),
        ("Tupperware Container Set", "Tupperware", 1499, 4.5),
        ("Prestige Non Stick Pan", "Prestige", 999, 4.4),
        ("Hawkins Non Stick Pan", "Hawkins", 1199, 4.4),
        ("Pigeon Fry Pan", "Pigeon", 799, 4.2),
        ("Wonderchef Fry Pan", "Wonderchef", 1299, 4.4),
    ],

    "Accessories": [

        ("Wildcraft Backpack", "Wildcraft", 1899, 4.5),
        ("American Tourister Backpack", "American Tourister", 2499, 4.6),
        ("Skybags Backpack", "Skybags", 1999, 4.5),
        ("Safari Backpack", "Safari", 1599, 4.3),
        ("Aristocrat Backpack", "Aristocrat", 1299, 4.2),
        ("Wenger Laptop Backpack", "Wenger", 3499, 4.5),
        ("Samsonite Laptop Backpack", "Samsonite", 5999, 4.7),
        ("F Gear Backpack", "F Gear", 1499, 4.3),
        ("Puma Backpack", "Puma", 1999, 4.4),
        ("Nike Backpack", "Nike", 2999, 4.5),

        ("Noise ColorFit Smartwatch", "Noise", 2499, 4.2),
        ("boAt Wave Smartwatch", "boAt", 1999, 4.2),
        ("Fire-Boltt Phoenix", "Fire-Boltt", 1799, 4.1),
        ("Samsung Galaxy Watch FE", "Samsung", 14999, 4.5),
        ("OnePlus Watch 2", "OnePlus", 24999, 4.6),
        ("Apple Watch SE", "Apple", 29999, 4.7),
        ("Amazfit Active", "Amazfit", 9999, 4.5),
        ("CMF Watch Pro", "CMF", 4499, 4.3),
        ("Titan Smart Watch", "Titan", 4999, 4.2),
        ("Fastrack Smartwatch", "Fastrack", 2999, 4.2),

        ("Mi Power Bank", "Xiaomi", 1499, 4.4),
        ("Anker PowerCore", "Anker", 2499, 4.5),
        ("Ambrane Power Bank", "Ambrane", 1299, 4.3),
        ("URBN Power Bank", "URBN", 1499, 4.4),
        ("Portronics Power Bank", "Portronics", 1299, 4.2),
        ("Stuffcool Power Bank", "Stuffcool", 1999, 4.3),
        ("Realme Power Bank", "Realme", 1599, 4.3),
        ("Belkin Power Bank", "Belkin", 2999, 4.5),
        ("Samsung Power Bank", "Samsung", 2499, 4.4),
        ("OnePlus Power Bank", "OnePlus", 1999, 4.3),

        ("Anker USB-C Charger", "Anker", 1999, 4.6),
        ("Samsung 25W Charger", "Samsung", 999, 4.5),
        ("OnePlus 80W Charger", "OnePlus", 1999, 4.5),
        ("Apple 20W Charger", "Apple", 1899, 4.6),
        ("Belkin 65W Charger", "Belkin", 3999, 4.6),
        ("Portronics Charger", "Portronics", 999, 4.2),
        ("Ambrane Charger", "Ambrane", 799, 4.2),
        ("UGREEN Charger", "UGREEN", 2499, 4.5),
        ("Spigen Charger", "Spigen", 1999, 4.4),
        ("CMF Charger", "CMF", 1499, 4.3),

        ("Apple AirTag", "Apple", 3490, 4.6),
        ("Samsung SmartTag2", "Samsung", 2999, 4.5),
        ("Tile Mate", "Tile", 2499, 4.3),
        ("Portronics Tracker", "Portronics", 999, 4.1),
        ("Stuffcool Tracker", "Stuffcool", 1299, 4.2),
        ("Spigen Phone Stand", "Spigen", 1299, 4.4),
        ("Portronics Phone Stand", "Portronics", 699, 4.2),
        ("AmazonBasics Phone Stand", "AmazonBasics", 499, 4.1),
        ("Ugreen Laptop Stand", "UGREEN", 1999, 4.5),
        ("Portronics Laptop Stand", "Portronics", 999, 4.3),

        ("Logitech Wireless Keyboard", "Logitech", 1999, 4.4),
        ("HP Wireless Keyboard", "HP", 1499, 4.2),
        ("Dell Wireless Keyboard", "Dell", 1799, 4.3),
        ("Microsoft Wireless Keyboard", "Microsoft", 2999, 4.5),
        ("Logitech Wireless Mouse", "Logitech", 999, 4.5),
        ("HP Wireless Mouse", "HP", 699, 4.2),
        ("Dell Wireless Mouse", "Dell", 899, 4.3),
        ("Microsoft Bluetooth Mouse", "Microsoft", 1999, 4.4),
        ("Lenovo Wireless Mouse", "Lenovo", 799, 4.2),
        ("Zebronics Wireless Mouse", "Zebronics", 499, 4.1),

        ("Fossil Leather Wallet", "Fossil", 2499, 4.5),
        ("Wildcraft Wallet", "Wildcraft", 899, 4.4),
        ("Levis Wallet", "Levis", 799, 4.3),
        ("Tommy Hilfiger Wallet", "Tommy Hilfiger", 2499, 4.5),
        ("Puma Wallet", "Puma", 999, 4.2),
        ("American Tourister Wallet", "American Tourister", 699, 4.2),
        ("F Gear Wallet", "F Gear", 799, 4.2),
        ("Woodland Wallet", "Woodland", 999, 4.3),
        ("Titan Wallet", "Titan", 1299, 4.3),
        ("Hidesign Wallet", "Hidesign", 3999, 4.6),

        ("Ray-Ban Case", "Ray-Ban", 999, 4.3),
        ("Fastrack Sunglasses Case", "Fastrack", 499, 4.2),
        ("Titan Sunglasses Case", "Titan", 599, 4.2),
        ("Safari Travel Organizer", "Safari", 799, 4.3),
        ("Wildcraft Travel Organizer", "Wildcraft", 999, 4.4),
        ("American Tourister Organizer", "American Tourister", 1199, 4.4),
        ("Samsonite Travel Pouch", "Samsonite", 1999, 4.5),
        ("Puma Travel Pouch", "Puma", 799, 4.2),
        ("Nike Travel Pouch", "Nike", 1299, 4.4),
        ("Adidas Travel Pouch", "Adidas", 999, 4.3),

        ("Spigen Phone Case", "Spigen", 1299, 4.5),
        ("Ringke Phone Case", "Ringke", 999, 4.4),
        ("Caseology Phone Case", "Caseology", 1499, 4.4),
        ("ESR Phone Case", "ESR", 1199, 4.4),
        ("OtterBox Phone Case", "OtterBox", 2999, 4.6),
        ("DailyObjects Phone Case", "DailyObjects", 999, 4.2),
        ("Mobi Armor Phone Case", "Mobi Armor", 499, 4.1),
        ("Nilkin Phone Case", "Nilkin", 799, 4.3),
        ("Portronics Phone Case", "Portronics", 599, 4.1),
        ("AmazonBasics Phone Case", "AmazonBasics", 499, 4.0),
    ],

    "Books": [

        ("Atomic Habits", "James Clear", 599, 4.8),
        ("The Psychology of Money", "Morgan Housel", 499, 4.7),
        ("Rich Dad Poor Dad", "Robert Kiyosaki", 399, 4.6),
        ("Ikigai", "Hector Garcia", 299, 4.5),
        ("Deep Work", "Cal Newport", 499, 4.7),
        ("The Power of Habit", "Charles Duhigg", 449, 4.6),
        ("Think and Grow Rich", "Napoleon Hill", 299, 4.5),
        ("The 7 Habits of Highly Effective People", "Stephen Covey", 599, 4.7),
        ("How to Win Friends", "Dale Carnegie", 299, 4.6),
        ("Do Epic Shit", "Ankur Warikoo", 299, 4.3),

        ("Python Programming Book", "Mark Lutz", 899, 4.5),
        ("Automate the Boring Stuff", "Al Sweigart", 699, 4.7),
        ("Python Crash Course", "Eric Matthes", 899, 4.7),
        ("Fluent Python", "Luciano Ramalho", 1199, 4.8),
        ("Learning Python", "Mark Lutz", 999, 4.5),
        ("Effective Python", "Brett Slatkin", 799, 4.6),
        ("Head First Python", "Paul Barry", 699, 4.5),
        ("Python Cookbook", "David Beazley", 1099, 4.7),
        ("Think Python", "Allen Downey", 499, 4.6),
        ("Python for Data Analysis", "Wes McKinney", 999, 4.8),

        ("Clean Code", "Robert Martin", 799, 4.7),
        ("The Pragmatic Programmer", "David Thomas", 899, 4.8),
        ("Design Patterns", "Gang of Four", 999, 4.7),
        ("Code Complete", "Steve McConnell", 1099, 4.7),
        ("Refactoring", "Martin Fowler", 999, 4.6),
        ("Head First Design Patterns", "Eric Freeman", 899, 4.7),
        ("Introduction to Algorithms", "Thomas Cormen", 1499, 4.8),
        ("Algorithms", "Robert Sedgewick", 1199, 4.7),
        ("Data Structures in C", "Reema Thareja", 599, 4.5),
        ("Data Structures and Algorithms", "Narasimha Karumanchi", 699, 4.6),

        ("Computer Networks", "Andrew Tanenbaum", 1199, 4.7),
        ("Computer Networking", "James Kurose", 1299, 4.8),
        ("Operating System Concepts", "Silberschatz", 1499, 4.7),
        ("Modern Operating Systems", "Andrew Tanenbaum", 1299, 4.6),
        ("Database System Concepts", "Silberschatz", 1399, 4.7),
        ("Let Us C", "Yashavant Kanetkar", 499, 4.5),
        ("Let Us C++", "Yashavant Kanetkar", 599, 4.5),
        ("Java Complete Reference", "Herbert Schildt", 999, 4.6),
        ("Effective Java", "Joshua Bloch", 899, 4.7),
        ("Core Java", "Cay Horstmann", 1099, 4.6),

        ("Machine Learning", "Tom Mitchell", 999, 4.7),
        ("Hands-On Machine Learning", "Aurélien Géron", 1299, 4.8),
        ("Deep Learning", "Ian Goodfellow", 1499, 4.7),
        ("Artificial Intelligence", "Stuart Russell", 1399, 4.7),
        ("Pattern Recognition", "Christopher Bishop", 1499, 4.8),
        ("Data Science Handbook", "Field Cady", 899, 4.5),
        ("Data Science from Scratch", "Joel Grus", 799, 4.6),
        ("Practical Statistics", "Peter Bruce", 899, 4.6),
        ("Naked Statistics", "Charles Wheelan", 499, 4.5),
        ("Storytelling with Data", "Cole Nussbaumer", 699, 4.7),

        ("The Alchemist", "Paulo Coelho", 299, 4.6),
        ("1984", "George Orwell", 299, 4.7),
        ("Animal Farm", "George Orwell", 199, 4.6),
        ("The Great Gatsby", "F. Scott Fitzgerald", 249, 4.5),
        ("To Kill a Mockingbird", "Harper Lee", 399, 4.7),
        ("The Kite Runner", "Khaled Hosseini", 399, 4.7),
        ("A Thousand Splendid Suns", "Khaled Hosseini", 399, 4.7),
        ("Harry Potter", "J.K. Rowling", 499, 4.8),
        ("The Hobbit", "J.R.R. Tolkien", 399, 4.7),
        ("The Lord of the Rings", "J.R.R. Tolkien", 699, 4.8),

        ("The Subtle Art of Not Giving a F*ck", "Mark Manson", 399, 4.5),
        ("Can't Hurt Me", "David Goggins", 499, 4.7),
        ("Make Your Bed", "William McRaven", 299, 4.5),
        ("The Mountain Is You", "Brianna Wiest", 399, 4.6),
        ("Good Vibes Good Life", "Vex King", 399, 4.5),
        ("The Courage to Be Disliked", "Ichiro Kishimi", 499, 4.6),
        ("Ego Is the Enemy", "Ryan Holiday", 399, 4.6),
        ("The Daily Stoic", "Ryan Holiday", 499, 4.6),
        ("Meditations", "Marcus Aurelius", 299, 4.7),
        ("Man's Search for Meaning", "Viktor Frankl", 299, 4.8),

        ("Zero to One", "Peter Thiel", 499, 4.6),
        ("The Lean Startup", "Eric Ries", 599, 4.5),
        ("Start With Why", "Simon Sinek", 499, 4.6),
        ("The 4-Hour Workweek", "Tim Ferriss", 699, 4.4),
        ("Good to Great", "Jim Collins", 599, 4.6),
        ("Shoe Dog", "Phil Knight", 499, 4.7),
        ("Rework", "Jason Fried", 399, 4.5),
        ("Hooked", "Nir Eyal", 499, 4.5),
        ("Blue Ocean Strategy", "W. Chan Kim", 599, 4.6),
        ("Think Again", "Adam Grant", 499, 4.6),

        ("The Intelligent Investor", "Benjamin Graham", 799, 4.7),
        ("One Up On Wall Street", "Peter Lynch", 599, 4.7),
        ("Common Stocks", "Philip Fisher", 499, 4.5),
        ("A Random Walk Down Wall Street", "Burton Malkiel", 699, 4.6),
        ("Psychology of Money Workbook", "Morgan Housel", 599, 4.5),
        ("Richest Man in Babylon", "George Clason", 299, 4.6),
        ("Think Like a Monk", "Jay Shetty", 399, 4.4),
        ("The Almanack of Naval Ravikant", "Eric Jorgenson", 599, 4.7),
        ("The Compound Effect", "Darren Hardy", 399, 4.5),
        ("Secrets of the Millionaire Mind", "T. Harv Eker", 499, 4.4),
    ],

    "Beauty": [

        ("Cetaphil Gentle Cleanser", "Cetaphil", 399, 4.6),
        ("Cetaphil Moisturizer", "Cetaphil", 499, 4.6),
        ("Minimalist Face Serum", "Minimalist", 599, 4.5),
        ("Minimalist Sunscreen", "Minimalist", 399, 4.5),
        ("The Derma Co Face Wash", "The Derma Co", 299, 4.4),
        ("The Derma Co Sunscreen", "The Derma Co", 499, 4.5),
        ("Mamaearth Face Wash", "Mamaearth", 299, 4.2),
        ("Plum Green Tea Face Wash", "Plum", 349, 4.4),
        ("Plum Moisturizer", "Plum", 449, 4.4),
        ("Neutrogena Face Wash", "Neutrogena", 499, 4.5),

        ("Lakme Face Cream", "Lakme", 299, 4.3),
        ("Lakme Sunscreen", "Lakme", 399, 4.4),
        ("Nivea Soft Cream", "Nivea", 249, 4.5),
        ("Nivea Body Lotion", "Nivea", 349, 4.5),
        ("Vaseline Body Lotion", "Vaseline", 299, 4.4),
        ("Dove Body Lotion", "Dove", 299, 4.4),
        ("Ponds Moisturizer", "Ponds", 249, 4.3),
        ("Ponds Face Wash", "Ponds", 199, 4.3),
        ("Himalaya Face Wash", "Himalaya", 199, 4.2),
        ("Biotique Face Wash", "Biotique", 249, 4.2),

        ("L'Oreal Shampoo", "L'Oreal", 499, 4.4),
        ("Tresemme Shampoo", "Tresemme", 399, 4.4),
        ("Dove Shampoo", "Dove", 299, 4.3),
        ("Head & Shoulders Shampoo", "Head & Shoulders", 349, 4.4),
        ("Pantene Shampoo", "Pantene", 299, 4.3),
        ("Sunsilk Shampoo", "Sunsilk", 249, 4.2),
        ("Mamaearth Shampoo", "Mamaearth", 399, 4.2),
        ("Minimalist Hair Serum", "Minimalist", 599, 4.5),
        ("L'Oreal Hair Serum", "L'Oreal", 599, 4.4),
        ("Streax Hair Serum", "Streax", 249, 4.3),

        ("Maybelline Mascara", "Maybelline", 499, 4.5),
        ("Maybelline Lipstick", "Maybelline", 399, 4.5),
        ("Maybelline Foundation", "Maybelline", 699, 4.4),
        ("Lakme Lipstick", "Lakme", 399, 4.4),
        ("Lakme Foundation", "Lakme", 599, 4.3),
        ("L'Oreal Lipstick", "L'Oreal", 699, 4.5),
        ("L'Oreal Foundation", "L'Oreal", 899, 4.5),
        ("Sugar Lipstick", "Sugar", 499, 4.4),
        ("Sugar Eyeliner", "Sugar", 399, 4.3),
        ("Faces Canada Lipstick", "Faces Canada", 499, 4.4),

        ("Nykaa Kajal", "Nykaa", 299, 4.4),
        ("Nykaa Eyeliner", "Nykaa", 349, 4.4),
        ("Colorbar Kajal", "Colorbar", 399, 4.4),
        ("Colorbar Lipstick", "Colorbar", 499, 4.3),
        ("Swiss Beauty Palette", "Swiss Beauty", 599, 4.4),
        ("Insight Makeup Palette", "Insight", 399, 4.3),
        ("Mars Makeup Kit", "Mars", 699, 4.4),
        ("Blue Heaven Makeup Kit", "Blue Heaven", 499, 4.2),
        ("Elle 18 Lipstick", "Elle 18", 199, 4.2),
        ("Miss Claire Lipstick", "Miss Claire", 299, 4.3),

        ("Gillette Mach3 Razor", "Gillette", 399, 4.5),
        ("Gillette Fusion Razor", "Gillette", 599, 4.5),
        ("Philips OneBlade", "Philips", 2499, 4.6),
        ("Philips Trimmer", "Philips", 1499, 4.5),
        ("Nova Trimmer", "Nova", 899, 4.2),
        ("Braun Trimmer", "Braun", 2499, 4.5),
        ("Mi Trimmer", "Xiaomi", 999, 4.4),
        ("Syska Trimmer", "Syska", 799, 4.3),
        ("Bombay Shaving Razor", "Bombay Shaving Company", 499, 4.3),
        ("Beardo Trimmer", "Beardo", 1299, 4.3),

        ("Dove Soap", "Dove", 199, 4.5),
        ("Nivea Men Face Wash", "Nivea", 249, 4.4),
        ("Beardo Face Wash", "Beardo", 299, 4.3),
        ("The Man Company Face Wash", "The Man Company", 299, 4.3),
        ("Mamaearth Body Wash", "Mamaearth", 399, 4.3),
        ("Nivea Body Wash", "Nivea", 349, 4.4),
        ("Dove Body Wash", "Dove", 349, 4.4),
        ("Fiama Body Wash", "Fiama", 299, 4.3),
        ("Park Avenue Shower Gel", "Park Avenue", 249, 4.2),
        ("The Body Shop Shower Gel", "The Body Shop", 699, 4.5),

        ("Denver Perfume", "Denver", 599, 4.3),
        ("Fogg Perfume", "Fogg", 499, 4.2),
        ("Wild Stone Perfume", "Wild Stone", 499, 4.3),
        ("Park Avenue Perfume", "Park Avenue", 599, 4.4),
        ("Skinn by Titan Perfume", "Titan", 1999, 4.5),
        ("Bella Vita Perfume", "Bella Vita", 599, 4.3),
        ("Engage Perfume", "Engage", 399, 4.2),
        ("Armaf Club de Nuit", "Armaf", 2999, 4.6),
        ("Davidoff Cool Water", "Davidoff", 4999, 4.6),
        ("Versace Eros", "Versace", 7999, 4.7),

        ("Nivea Men Deodorant", "Nivea", 249, 4.3),
        ("Axe Deodorant", "Axe", 249, 4.2),
        ("Park Avenue Deodorant", "Park Avenue", 299, 4.3),
        ("Fogg Deodorant", "Fogg", 249, 4.2),
        ("Wild Stone Deodorant", "Wild Stone", 249, 4.2),
        ("Dove Deodorant", "Dove", 299, 4.3),
        ("Rexona Deodorant", "Rexona", 299, 4.3),
        ("Nivea Roll On", "Nivea", 249, 4.4),
        ("Beardo Deodorant", "Beardo", 349, 4.2),
        ("The Man Company Deodorant", "The Man Company", 399, 4.3),

        ("Mamaearth Face Mask", "Mamaearth", 299, 4.2),
        ("Plum Face Mask", "Plum", 349, 4.4),
        ("The Derma Co Face Mask", "The Derma Co", 399, 4.4),
        ("Minimalist Clay Mask", "Minimalist", 449, 4.4),
        ("Lakme Face Mask", "Lakme", 299, 4.2),
        ("Biotique Face Mask", "Biotique", 249, 4.1),
        ("Himalaya Neem Mask", "Himalaya", 199, 4.2),
        ("Neutrogena Face Mask", "Neutrogena", 499, 4.4),
        ("L'Oreal Face Mask", "L'Oreal", 599, 4.4),
        ("The Body Shop Face Mask", "The Body Shop", 799, 4.5),
    ]
}


# ============================================================
# GENERATE PRODUCT RECORDS
# ============================================================

for category, items in categories.items():

    for name, brand, price, rating in items:

        if category == "Electronics":

            description = (
                f"{name} designed for everyday performance "
                f"with modern technology."
            )

            features = (
                "Modern processor; high quality display; "
                "reliable performance; everyday connectivity"
            )

        elif category == "Fashion":

            description = (
                f"{name} from {brand}, designed for "
                f"comfortable everyday wear."
            )

            features = (
                "Comfortable material; modern design; "
                "everyday wear; durable construction"
            )

        elif category == "Gaming":

            description = (
                f"{name} designed for gaming and "
                f"performance-focused users."
            )

            features = (
                "Gaming performance; ergonomic design; "
                "responsive controls; durable build"
            )

        elif category == "Audio":

            description = (
                f"{name} designed for an enjoyable "
                f"music and entertainment experience."
            )

            features = (
                "Clear audio; comfortable design; "
                "wireless connectivity; long usage"
            )

        elif category == "Home":

            description = (
                f"{name} designed to make everyday "
                f"home tasks easier."
            )

            features = (
                "Easy operation; durable build; "
                "energy efficient; practical design"
            )

        elif category == "Accessories":

            description = (
                f"{name} from {brand}, designed for "
                f"daily convenience."
            )

            features = (
                "Compact design; durable construction; "
                "easy to use; everyday functionality"
            )

        elif category == "Books":

            description = (
                f"{name} by {brand}, useful for "
                f"learning, knowledge and personal growth."
            )

            features = (
                "Paperback; educational content; "
                "easy to read; practical knowledge"
            )

        else:

            description = (
                f"{name} from {brand}, designed for "
                f"personal care and everyday use."
            )

            features = (
                "Easy to use; everyday care; "
                "quality formulation; convenient packaging"
            )

        products.append([
            product_id,
            name,
            category,
            brand,
            price,
            rating,
            description,
            features
        ])

        product_id += 1


# ============================================================
# ADD EXTRA PRODUCTS IF A CATEGORY HAS LESS THAN 100
# ============================================================

category_counts = {}

for product in products:

    category_counts[product[2]] = (
        category_counts.get(product[2], 0) + 1
    )


# Automatically create additional variants
# so every category has AT LEAST 100 products.

for category in list(categories.keys()):

    current_count = category_counts.get(
        category,
        0
    )

    while current_count < 100:

        variant_number = current_count + 1

        name = (
            f"{category} Smart Choice "
            f"Product {variant_number}"
        )

        brand = "NOVA Selection"

        if category == "Electronics":
            price = random.choice(
                [
                    9999,
                    14999,
                    19999,
                    24999,
                    29999,
                    34999,
                    49999,
                    64999
                ]
            )

        elif category == "Fashion":
            price = random.choice(
                [
                    699,
                    999,
                    1299,
                    1499,
                    1999,
                    2499,
                    2999
                ]
            )

        elif category == "Gaming":
            price = random.choice(
                [
                    799,
                    1299,
                    1999,
                    2499,
                    3999,
                    6999,
                    12999
                ]
            )

        elif category == "Audio":
            price = random.choice(
                [
                    699,
                    999,
                    1499,
                    1999,
                    2999,
                    4999,
                    9999
                ]
            )

        elif category == "Home":
            price = random.choice(
                [
                    499,
                    999,
                    1499,
                    2499,
                    4999,
                    6999,
                    9999
                ]
            )

        elif category == "Accessories":
            price = random.choice(
                [
                    499,
                    799,
                    999,
                    1499,
                    1999,
                    2999,
                    4999
                ]
            )

        elif category == "Books":
            price = random.choice(
                [
                    199,
                    299,
                    399,
                    499,
                    599,
                    799,
                    999
                ]
            )

        else:
            price = random.choice(
                [
                    199,
                    299,
                    399,
                    499,
                    599,
                    799,
                    999
                ]
            )

        rating = round(
            random.uniform(
                4.0,
                4.8
            ),
            1
        )

        description = (
            f"{name} is a NOVA catalog product "
            f"selected for the {category.lower()} category."
        )

        features = (
            f"{category} product; practical design; "
            f"good everyday usability; NOVA selection"
        )

        products.append([
            product_id,
            name,
            category,
            brand,
            price,
            rating,
            description,
            features
        ])

        product_id += 1
        current_count += 1


# ============================================================
# WRITE CSV
# ============================================================

headers = [
    "id",
    "name",
    "category",
    "brand",
    "price",
    "rating",
    "description",
    "features"
]

with open(
    "products.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(headers)

    writer.writerows(products)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 60)
print("NOVA PRODUCT DATABASE CREATED")
print("=" * 60)

print(
    f"Total products: {len(products)}"
)

for category in sorted(category_counts):

    count = sum(
        1
        for product in products
        if product[2] == category
    )

    print(
        f"{category}: {count} products"
    )

print("=" * 60)
print("Saved as: products.csv")
print("=" * 60)