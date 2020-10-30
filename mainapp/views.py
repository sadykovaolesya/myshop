import datetime

from django.shortcuts import render


def main(request):
    title = "home"
    products = [
        {
            "name": "ASSASIN’S CREED: Rogue",
            "image_src":"assassin.jpg",
            "image_href":"/product/1/",
            "alt":"product 1",
        },
        {
            "name": "TOMB RAIDER",
            "image_src":"tomb.png",
            "image_href":"/product/2/",
            "alt":"product 2",
        },
        {
            "name": "RYSE: Son Of Rome",
            "image_src":"ryse.png",
            "image_href":"/product/3/",
            "alt":"product 3",
        },
        {
            "name": "WORLD OF WARCRAFT:Wrath Of The Linch King",
            "image_src":"warcraft.png",
            "image_href":"/product/4/",
            "alt":"product 4",
        },
    ]

    team = [
        {
            "name": "Mary Jane",
            "position": "Vestibulum",
            "image_src":"t1.jpg",
        },
        {
            "name": "Peter Parker",
            "position": "Vestibulum",
            "image_src":"t2.jpg",
        },
        {
            "name": "John Watson",
            "position": "Vestibulum",
            "image_src":"t3.jpg",
        },
        {
            "name": "Steven Wilson",
            "position": "Vestibulum",
            "image_src":"t4.jpg",
        },
    ]

    content = {"title": title, "products":products, "team":team}
    return render(request, "mainapp/index.html", content)

def catalog(request):
    title = "catalog"

    catalog_products = [
        {
            "name": "BATTLEFIELD 1",
            "image_src":"1.jpg",
            "image_href":"/product/1/",
            "alt":"product 1",
        },
        {
            "name": "STAR WARS",
            "image_src":"2.jpg",
            "image_href":"/product/2/",
            "alt":"product 2",
        },
        {
            "name": "BATTLEFIELD 4",
            "image_src":"3.jpg",
            "image_href":"/product/3/",
            "alt":"product 3",
        },
        {
            "name": "WORLD OF TANKS",
            "image_src":"4.jpg",
            "image_href":"/product/4/",
            "alt":"product 4",
        },
        {
            "name": "ASSASIN’S CREED: Rogue",
            "image_src":"5.jpg",
            "image_href":"/product/5/",
            "alt":"product 5",
        },
        {
            "name": "FOR HONOR",
            "image_src":"6.jpg",
            "image_href":"/product/6/",
            "alt":"product 6",
        },
        {
            "name": "WORLD OF WARSHIPS",
            "image_src":"7.jpg",
            "image_href":"/product/7/",
            "alt":"product 7",
        },
        {
            "name": "CALL OF DUTY",
            "image_src":"8.jpg",
            "image_href":"/product/8/",
            "alt":"product 8",
        },
    ]

    discounts = [
        {
            "name": "CALL OF DUTY",
            "div_class":"banner-left",
            "image_href":"/product/1/",
            "old_price":"$28.90",
            "new_price":"$14.44",
        },
        {
            "name": "MEDAL OF HONOR",
            "div_class":"banner-right",
            "image_href":"/product/2/",
            "old_price":"$29.90",
            "new_price":"$15.96",
        },


    ]
    content = {"title": title, "catalog_products":catalog_products, "discounts":discounts}
    return render(request, "mainapp/catalog.html", content)


def product(request):
    title = "product"
    content = {"title" : title}
    return render(request, "mainapp/product.html", content)


def contacts(request):
    title = "Contact Us"
    visit_date = datetime.datetime.now()
    locations = [
        {
            "citi": "MOSCOW 125167, Russia",
            "fax": "+1 888 888 4444",
            "email": "mail@example.com",
            "adress":"Leningradsky AVE 39, BLDG 79",
        }
    ]
    content = {"title": title, "visit_date": visit_date, "locations":locations}
    return render(request, "mainapp/contacts.html", content)
