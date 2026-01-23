from clients import clients

"""
Pentru a fi mai usor de aplicat si de inteles singurele modificari pe care le am facut de cerinta sunt:
    in loc de 72 de ore am limitat timpul la 10 secunde

    in json uri la timp, 1 sec este echivalenta cu o ora

    clientii care stau mai putin sau egal cu 3 secunde sunt cei care stau "sub 2 ore" in parcare:
        timp <=3 sec => 2 hr

    clientii care stau intre 3 si 7 secunde sunt cei care "depasesc 2 ore":
        3 sec < timp < 7 sec => 2+ ore

    clientii care stau peste 7 secunde sunt cei care stau "3 zile":
        7 sec <= timp => 3 zile

    clientii care au depasit 7 secunde a.k.a. "3 zile" li se va schimba pariah din False in True

In rest totul este exact ca si in cerinta de la proiect (sper)
Avem deja 10 clienti gata sortati, daca dam run la main, acest va mai adauga 10 si ii va sorta
La final vom avea 20 de clienti toti dortati frumos la locul lor

Am incercat sa explic cat mai bine tot ce am facut
Sper ca o sa intelegeti, nu sunt cel mai bun la limba romana :)

In drafts sunt toate ciornele mele, nothing important
"""

if __name__ == "__main__":
    clients(
        "data/clients.json",
        "Frank",
        "Fleming",
        "(810) 011-4394",
        "Port Huron, MI",
    )
    clients(
        "data/clients.json",
        "Keith",
        "Wood",
        "(475) 651-6147",
        "Bridgeport, CT",
    )
    clients(
        "data/clients.json",
        "Marty",
        "Koch",
        "(681) 518-7418",
        "Charleston, WV",
    )
    clients(
        "data/clients.json",
        "Billie",
        "Forbes",
        "(570) 542-1228",
        "Scranton, PA",
    )
    clients(
        "data/clients.json",
        "Deloris",
        "White",
        "(386) 167-3182",
        "Palm Coast, FL",
    )
    clients(
        "data/clients.json",
        "Sherwood",
        "Holder",
        "(574) 347-8989",
        "Elkhart, IN",
    )
    clients(
        "data/clients.json",
        "Tobias",
        "Snyder",
        "(502) 947-8597",
        "Louisville, KY",
    )
    clients(
        "data/clients.json",
        "Mattie",
        "Garcia",
        "(270) 921-6744",
        "Henderson, KY",
    )
    clients(
        "data/clients.json",
        "Hugh",
        "Maxwell",
        "(530) 532-3263",
        "Davis, CA",
    )
    clients(
        "data/clients.json",
        "Diana",
        "Acosta",
        "(724) 410-6441",
        "Mccandless, PA",
    )
