run-script:
	python3 ${CONTINENT}/$(REGION)/$(COUNTRY).py

canada:
	make run-script CONTINENT=America REGION=NorthAmerica COUNTRY=Canada

colombia:
	make run-script CONTINENT=America REGION=SouthAmerica COUNTRY=Colombia

japan:
	make run-script CONTINENT=Asia REGION=EastAsia COUNTRY=Japan
south-korea:
	make run-script CONTINENT=Asia REGION=EastAsia COUNTRY=SouthKorea
thailand:
	make run-script CONTINENT=Asia REGION=EastAsia COUNTRY=Thailand

israel:
	make run-script CONTINENT=Asia REGION=MiddleEast COUNTRY=Israel

armenia:
	make run-script CONTINENT=Eurasia REGION=Caucasus COUNTRY=Armenia
georgia:
	make run-script CONTINENT=Eurasia REGION=Caucasus COUNTRY=Georgia

moldova:
	make run-script CONTINENT=Eurasia REGION=EasternEurope COUNTRY=Moldova
russia:
	make run-script CONTINENT=Eurasia REGION=EasternEurope COUNTRY=Russia
ukraine:
	make run-script CONTINENT=Eurasia REGION=EasternEurope COUNTRY=Ukraine

turkey:
	make run-script CONTINENT=Eurasia REGION=Turkey COUNTRY=Turkey

czech-republic:
	make run-script CONTINENT=Europe REGION=CentralEurope COUNTRY=CzechRepublic
hungary:
	make run-script CONTINENT=Europe REGION=CentralEurope COUNTRY=Hungary
poland:
	make run-script CONTINENT=Europe REGION=CentralEurope COUNTRY=Poland
slovakia:
	make run-script CONTINENT=Europe REGION=CentralEurope COUNTRY=Slovakia

denmark:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Denmark
estonia:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Estonia
finland:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Finland
iceland:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Iceland
ireland:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Ireland
latvia:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Latvia
lithuania:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Lithuania
norway:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Norway
sweden:
	make run-script CONTINENT=Europe REGION=NorthEurope COUNTRY=Sweden

andorra:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Andorra
bulgaria:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Bulgaria
croatia:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Croatia
cyprus:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Cyprus
greece:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Greece
italy:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Italy
malta:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Malta
montenegro:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Montenegro
portugal:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Portugal
romania:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Romania
serbia:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Serbia
slovenia:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Slovenia
spain:
	make run-script CONTINENT=Europe REGION=SouthEurope COUNTRY=Spain

makerfield:
	make run-script CONTINENT=Europe REGION=UK COUNTRY=Makerfield
scotland:
	make run-script CONTINENT=Europe REGION=UK COUNTRY=Scotland
uk:
	make run-script CONTINENT=Europe REGION=UK COUNTRY=UK
wales:
	make run-script CONTINENT=Europe REGION=UK COUNTRY=Wales

austria:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Austria
belgium:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Belgium
european-union:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=EuropeanUnion
flanders:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Flanders
france:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=France
germany:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Germany
luxembourg:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Luxembourg
netherlands:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Netherlands
netherlands-seats:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=NetherlandsSeats
switzerland:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Switzerland
wallonia:
	make run-script CONTINENT=Europe REGION=WestEurope COUNTRY=Wallonia

australia:
	make run-script CONTINENT=Oceania REGION=Asia-Pacific COUNTRY=Australia
new-zealand:
	make run-script CONTINENT=Oceania REGION=Asia-Pacific COUNTRY=NewZealand