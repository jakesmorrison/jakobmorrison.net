from django.shortcuts import render
import json
from .models import Map

# Create your views here.

def index(request):
    mapData = Map.objects.all().values()
    locationDictionary = []
    for x in mapData:
        locationDictionary.append({"lat":x["lat"],"long":x["long"],"label":x["label"],"index":x["index"]})
    context = {
        "locationDictionary":locationDictionary
    }
    return render(request, 'map/index.html', context)


def get_long_lat(request):
    context={
        "locationDictionary": [
            {"location":"7216 Lima Drive Nampa, ID, 83687", "label":"Home"},
            {"location": "3201 W Airport Way, Boise, ID 83705", "label": "Airport: BOI"},
            {"location": "7000 NE Airport Way, Portland, OR 97218", "label": "Airport: PDX"},
            {"location": "San Francisco, CA 94128", "label": "Airport: SFO"},
            {"location": "272 Gonghang-ro, Jung-gu, Incheon, South Korea", "label": "Airport: ICN"},
            {"location": "40 Nonhyeon-ro 155-gil Gangnam-gu, Seoul South Korea", "label": "Airbnb: Gangnam-gu"},
            {"location": "999 หมู่ 1 Nong Prue, Amphoe Bang Phli, Chang Wat Samut Prakan 10540, Thailand", "label": "Airport: BKK"},
            {"location": "118 Soi Songpra Siphraya Road Khwaeng Maha Phruttharam, Khet Bang Rak, Krung Thep Maha Nakhon 10500, Thailand", "label": "Airbnb: iSanook"},
            {"location": "Amphoe Mueang Kamphaeng Phet, Chang Wat Kamphaeng Phet 62000, Thailand", "label": "Spa Resort: Praepimpalai"},
            {"location": "Hang Dong, Hot District, Chiang Mai 50240, Thailand", "label": "Resort: Huen Hug Hod"},
            {"location": "Ratmakka Rd, Tambon Phra Sing, Amphoe Mueang Chiang Mai, Chang Wat Chiang Mai 50100, Thailand", "label": "Elephant Nature Park Office"},
            {"location": "Chang Wat Chiang Mai 50150, Thailand", "label": "Elephant Nature Park"},
            {"location": "Charoenrad road 365, Fha Ham, Chiang Mai, Amphoe Mueang Chiang Mai, Chang Wat Chiang Mai 50000, Thailand", "label": "Guesthouse: Hollanda Montri"},
            {"location": "222 Vibhavadi Rangsit Rd, Khwaeng Sanambin, Khet Don Mueang, Krung Thep Maha Nakhon 10210, Thailand", "label": "Airport: DMK"},
            {"location": "T. Wiang, A. Muang, Tambon Wiang, Amphoe Mueang Chiang Rai, Chang Wat Chiang Rai 57000, Thailand", "label": "Hotel: North Hotel"},
            {"location": "Huay Xai, Laos", "label": "Bus to Huay Xai"},
            {"location": "Pak Beng, Laos", "label": "Slow boat to Pak Beng"},
            {"location": "Joy Guest house, Luang Prabang, Laos", "label": "Guesthouse: Joy's"},
            {"location": "Kuang Si Waterfall, Luang Prabang, Laos", "label": "Kuang Si Waterfall"},
            {"location": "Lao Valhalla Bungalows, Vang Vieng, Laos", "label": "Airbnb: Lao Valhalla Bungalows"},
            {"location": "iHouse-New Hotel Vientiane 01000, Laos", "label": "Airbnb: iHouse"},
            {"location": "Tha Taphao, Mueang Chumphon District, Chumphon 86000, Thailand", "label": "Train from Bangkok to Chumphon"},
            {"location": "Montalay Beach Resort Ko Tao, Ko Pha-ngan District, Surat Thani, Thailand", "label": "Spa Resort: Montalay Beach Resort"},
            {"location": "Blue Immersion Freediving Thailand, Ko Tao, Ko Pha-ngan District, Surat Thani, Thailand", "label": "Blue Immersion Freediving"},
            {"location": "Chum Kho, Pathio District, Chumphon 86160, Thailand", "label": "Airport: CJM"},
            {"location": "Chic Hostel, Khwaeng Talat Noi, Khet Samphanthawong, Krung Thep Maha Nakhon 10100, Thailand", "label": "Hostel: Chic"},
            {"location": "Phuket International Airport, Mai Khao, Thalang District, Phuket, Thailand", "label": "Airport: HKT"},
            {"location": "FIN Hostel Phuket, Karon, Phuket, Thailand", "label": "Hostel: Fin"},
            {"location": "National Highway 6, Krong Siem Reap, Cambodia", "label": "Airport: REP"},
            {"location": "Phú Minh, Sóc Sơn, Hà Nội, Vietnam", "label": "Airport: HAN"},
            {"location": "73 Mã Mây, Hàng Buồm, Hoàn Kiếm, Hà Nội, Vietnam", "label": "Hostel: Funky Jungle"},
            {"location": "Hạ Long Bay Thành phố Hạ Long Quảng Ninh Province Vietnam", "label": "Ha Long Bay"},
            {"location": "Sapa Vietnam, Bản Hồ, Lao Cai, Vietnam", "label": "Sapa"},
            {"location": "Duy Tân, Hòa Thuận Tây, Quận Hải Châu, Đà Nẵng, Vietnam", "label": "Airport: DAD"},
            {"location": "07, Thái Phiên, Cẩm Phô, Tp. Hội An, Quảng Nam, Vietnam", "label": "Airbnb: DUA VIET"},
            {"location": "Airport Blvd, Singapore", "label": "Airport: SIN"},
            {"location": "Grand Hyatt Singapore", "label": "Hotel: Grand Hyatt Singapore"},
            {"location": "No. 9, Hangzhan S Rd, Dayuan District, Taoyuan City, Taiwan 33758", "label": "Airport: TPE"},
            {"location": "Backpack 41 Youth Hostel - Taichung", "label": "Hostel: Backpack 41"},
            {"location": "Itami Airport, Japan", "label": "Airport: ITM"},
        ]
    }
    return render(request, 'map/get_long_lat.html', context)

def send_long_lat(request):
    locationDictionary = [
        {"location": "7216 Lima Drive Nampa, ID, 83687", "label":"Home"},
        {"location": "3201 W Airport Way, Boise, ID 83705", "label": "Airport: BOI"},
        {"location": "7000 NE Airport Way, Portland, OR 97218", "label": "Airport: PDX"},
        {"location": "San Francisco, CA 94128", "label": "Airport: SFO"},
        {"location": "272 Gonghang-ro, Jung-gu, Incheon, South Korea", "label": "Airport: ICN"},
        {"location": "40 Nonhyeon-ro 155-gil Gangnam-gu, Seoul South Korea", "label": "Airbnb: Gangnam-gu"},
        {"location": "999 หมู่ 1 Nong Prue, Amphoe Bang Phli, Chang Wat Samut Prakan 10540, Thailand", "label": "Airport: BKK"},
        {"location": "118 Soi Songpra Siphraya Road Khwaeng Maha Phruttharam, Khet Bang Rak, Krung Thep Maha Nakhon 10500, Thailand", "label": "Airbnb: iSanook"},
        {"location": "Amphoe Mueang Kamphaeng Phet, Chang Wat Kamphaeng Phet 62000, Thailand", "label": "Spa Resort: Praepimpalai"},
        {"location": "Hang Dong, Hot District, Chiang Mai 50240, Thailand", "label": "Resort: Huen Hug Hod"},
        {"location": "Ratmakka Rd, Tambon Phra Sing, Amphoe Mueang Chiang Mai, Chang Wat Chiang Mai 50100, Thailand", "label": "Elephant Nature Park Office"},
        {"location": "Chang Wat Chiang Mai 50150, Thailand", "label": "Elephant Nature Park"},
        {"location": "Charoenrad road 365, Fha Ham, Chiang Mai, Amphoe Mueang Chiang Mai, Chang Wat Chiang Mai 50000, Thailand", "label": "Guesthouse: Hollanda Montri"},
        {"location": "222 Vibhavadi Rangsit Rd, Khwaeng Sanambin, Khet Don Mueang, Krung Thep Maha Nakhon 10210, Thailand", "label": "Airport: DMK"},
        {"location": "T. Wiang, A. Muang, Tambon Wiang, Amphoe Mueang Chiang Rai, Chang Wat Chiang Rai 57000, Thailand", "label": "Hotel: North Hotel"},
        {"location": "Huay Xai, Laos", "label": "Bus to Huay Xai"},
        {"location": "Pak Beng, Laos", "label": "Slow boat to Pak Beng"},
        {"location": "Joy Guest house, Luang Prabang, Laos", "label": "Guesthouse: Joy's"},
        {"location": "Kuang Si Waterfall, Luang Prabang, Laos", "label": "Kuang Si Waterfall"},
        {"location": "Lao Valhalla Bungalows, Vang Vieng, Laos", "label": "Airbnb: Lao Valhalla Bungalows"},
        {"location": "iHouse-New Hotel Vientiane 01000, Laos", "label": "Airbnb: iHouse"},
        {"location": "Tha Taphao, Mueang Chumphon District, Chumphon 86000, Thailand", "label": "Train from Bangkok to Chumphon"},
        {"location": "Montalay Beach Resort Ko Tao, Ko Pha-ngan District, Surat Thani, Thailand", "label": "Spa Resort: Montalay Beach Resort"},
        {"location": "Blue Immersion Freediving Thailand, Ko Tao, Ko Pha-ngan District, Surat Thani, Thailand", "label": "Blue Immersion Freediving"},
        {"location": "Chum Kho, Pathio District, Chumphon 86160, Thailand", "label": "Airport: CJM"},
        {"location": "Chic Hostel, Khwaeng Talat Noi, Khet Samphanthawong, Krung Thep Maha Nakhon 10100, Thailand", "label": "Hostel: Chic"},
        {"location": "Phuket International Airport, Mai Khao, Thalang District, Phuket, Thailand", "label": "Airport: HKT"},
        {"location": "FIN Hostel Phuket, Karon, Phuket, Thailand", "label": "Hostel: Fin"},
        {"location": "National Highway 6, Krong Siem Reap, Cambodia", "label": "Airport: REP"},
        {"location": "Phú Minh, Sóc Sơn, Hà Nội, Vietnam", "label": "Airport: HAN"},
        {"location": "73 Mã Mây, Hàng Buồm, Hoàn Kiếm, Hà Nội, Vietnam", "label": "Hostel: Funky Jungle"},
        {"location": "Hạ Long Bay Thành phố Hạ Long Quảng Ninh Province Vietnam", "label": "Ha Long Bay"},
        {"location": "Sapa Vietnam, Bản Hồ, Lao Cai, Vietnam", "label": "Sapa"},
        {"location": "Duy Tân, Hòa Thuận Tây, Quận Hải Châu, Đà Nẵng, Vietnam", "label": "Airport: DAD"},
        {"location": "07, Thái Phiên, Cẩm Phô, Tp. Hội An, Quảng Nam, Vietnam", "label": "Airbnb: DUA VIET"},
        {"location": "Airport Blvd, Singapore", "label": "Airport: SIN"},
        {"location": "Grand Hyatt Singapore", "label": "Hotel: Grand Hyatt Singapore"},
        {"location": "No. 9, Hangzhan S Rd, Dayuan District, Taoyuan City, Taiwan 33758", "label": "Airport: TPE"},
        {"location": "Backpack 41 Youth Hostel - Taichung", "label": "Hostel: Backpack 41"},
        {"location": "Itami Airport, Japan","label": "Airport: ITM"},
    ]

    queryDict = request.GET
    data = json.loads(list(dict(queryDict).keys())[0])
    for x in data:
        x["label"] = locationDictionary[x["index"]]["label"]
        m = Map(index=x["index"], address=x["address"], label=x["label"], lat=x["lat"], long=x["long"])
        m.save()
    return render(request, 'map/get_long_lat.html', {})

