from pyoxigraph import NamedNode

from pyrdf_prefix.namespace import PredefinedNamespace


class GR(PredefinedNamespace):
    """The GoodRelations Vocabulary for Semantic Web-based E-Commerce"""

    # Conversion-Date: 2024-09-30T10:48+00:00
    # Source: http://www.heppnetz.de/ontologies/goodrelations/v1.owl

    _nsBaseIri = "http://purl.org/goodrelations/v1#"
    _issueWarning = True
    _withContainerMembershipProperty = False
    _nonPyIdentifiers = (
        "Labor-BringIn",
        "N-Ary-Relations",
        "PartsAndLabor-BringIn",
        "PartsAndLabor-PickUp",
        "hasEAN_UCC-13",
        "hasGTIN-14",
        "hasGTIN-8",
    )

    ActualProductOrServiceInstance: NamedNode
    """DEPRECATED - This class is superseded by gr:Individual. Replace all occurrences of gr:ActualProductOrServiceInstance by gr:Individual, if possible."""
    AmericanExpress: NamedNode
    """Payment by credit or debit cards issued by the American Express network."""
    Brand: NamedNode
    """A brand is the identity of a specific product, service, or business. Use foaf:logo for attaching a brand logo and gr:name or rdfs:label for attaching the brand name.	

(Source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Brand)"""
    Business: NamedNode
    """The gr:BusinessEntityType representing such agents that are themselves offering commercial services or products on the market. Usually, businesses are characterized by the fact that they are officially registered with the public administration and strive for profits by their activities."""
    BusinessEntity: NamedNode
    """An instance of this class represents the legal agent making (or seeking) a particular offering. This can be a legal body or a person. A business entity has at least a primary mailing address and contact details. For this, typical address standards (vCard) and location data (geo, WGS84) can be attached. Note that the location of the business entity is not necessarily the location from which the product or service is being available (e.g. the branch or store). Use gr:Location for stores and branches.
		
Example: Siemens Austria AG, Volkswagen Ltd., Peter Miller's Cell phone Shop LLC

Compatibility with schema.org: This class is equivalent to the union of http://schema.org/Person and http://schema.org/Organization.		
"""
    BusinessEntityType: NamedNode
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of a gr:BusinessEntity. From the ontological point of view, business entity types are mostly roles that a business entity has in the market. Business entity types are important for specifying eligible customers, since a gr:Offering is often valid only for business entities of a certain size, legal structure, or role in the value chain. 

Examples: Consumers, Retailers, Wholesalers, or Public Institutions"""
    BusinessFunction: NamedNode
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the gr:BusinessEntity on the gr:ProductOrService through the gr:Offering. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation.

Licenses and other proprietary specifications of access rights are also instances of this class.

Examples: A particular offering made by Miller Rentals Ltd. says that they (1) sell Volkswagen Golf convertibles, (2) lease out a particular Ford pick-up truck, and (3) dispose car wrecks of any make and model."""
    Buy: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity is in general interested in purchasing the specified gr:ProductOrService.
DEPRECATED. Use gr:seeks instead."""
    ByBankTransferInAdvance: NamedNode
    """Payment by bank transfer in advance, i.e., the offering gr:BusinessEntity will inform the buying party about their bank account details and will deliver the goods upon receipt of the due amount.
This is equivalent to payment by wire transfer."""
    ByInvoice: NamedNode
    """Payment by bank transfer after delivery, i.e., the offering gr:BusinessEntity will deliver first, inform the buying party about the due amount and their bank account details, and expect payment shortly after delivery."""
    COD: NamedNode
    """Collect on delivery / Cash on delivery - A payment method where the recipient of goods pays at the time of delivery. Usually, the amount of money is collected by the transportation company handling the goods."""
    Cash: NamedNode
    """Payment by cash upon delivery or pickup."""
    CheckInAdvance: NamedNode
    """Payment by sending a check in advance, i.e., the offering gr:BusinessEntity will deliver the goods upon receipt of a check over the due amount. There are variations in handling payment by check - sometimes, shipment will be upon receipt of the check as a document, sometimes the shipment will take place only upon successful crediting of the check."""
    ConstructionInstallation: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) the construction and/or installation of the specified gr:ProductOrService at the customer's location."""
    DHL: NamedNode
    """Delivery via the parcel service DHL."""
    DayOfWeek: NamedNode
    """The day of the week, used to specify  to which day the opening hours of a gr:OpeningHoursSpecification refer.

Examples: Monday, Tuesday, Wednesday,..."""
    DeliveryChargeSpecification: NamedNode
    """A delivery charge specification is a conceptual entity that specifies the additional costs asked for the delivery of a given gr:Offering using a particular gr:DeliveryMethod by the respective gr:BusinessEntity. A delivery charge specification is characterized by (1) a monetary amount per order, specified as a literal value of type float in combination with a currency, (2) the delivery method, (3) the target country or region, and (4)  whether this charge includes local sales taxes, namely VAT.
A gr:Offering may be linked to multiple gr:DeliveryChargeSpecification nodes that specify alternative charges for disjoint combinations of target countries or regions, and delivery methods.

Examples: Delivery by direct download is free of charge worldwide, delivery by UPS to Germany is 10 Euros per order, delivery by mail within the US is 5 Euros per order.

The total amount of this charge is specified as a float value of the gr:hasCurrencyValue property. The currency is specified via the gr:hasCurrency datatype property. Whether the price includes VAT or not is indicated by the gr:valueAddedTaxIncluded property. The gr:DeliveryMethod to which this charge applies is specified using the gr:appliesToDeliveryMethod object property. The region or regions to which this charge applies is specified using the gr:eligibleRegions property, which uses ISO 3166-1 and ISO 3166-2 codes.

If the price can only be given as a range, use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue for the upper and lower bounds.

Important: When querying for the price, always use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue."""
    DeliveryMethod: NamedNode
    """A delivery method is a standardized procedure for transferring the product or service to the destination of fulfilment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending gr:BusinessEntity (this is important, since the contracted party may subcontract the fulfilment to smaller, regional businesses).

Examples: Delivery by mail, delivery by direct download, delivery by UPS"""
    DeliveryModeDirectDownload: NamedNode
    """Delivery of the goods via direct download from the Internet, i.e., the offering gr:BusinessEntity provides the buying party with details on how to retrieve the goods online. Connection fees and other costs of using the infrastructure are to be carried by the buying party."""
    DeliveryModeFreight: NamedNode
    """Delivery by an unspecified air, sea, or ground freight carrier or cargo company."""
    DeliveryModeMail: NamedNode
    """Delivery via regular mail service (private or public postal services)."""
    DeliveryModeOwnFleet: NamedNode
    """Delivery of the goods by using a fleet of vehicles either owned and operated or subcontracted by the gr:BusinessEntity."""
    DeliveryModeParcelService: NamedNode
    """A private parcel service as the delivery mode available for a certain offering.

Examples: UPS, DHL"""
    DeliveryModePickUp: NamedNode
    """Delivery of the goods by picking them up at one of the stores etc. (gr:Location) during the opening hours as specified by respective instances of gr:OpeningHoursSpecification."""
    DinersClub: NamedNode
    """Payment by credit or debit cards issued by the Diner's Club network."""
    DirectDebit: NamedNode
    """Payment by direct debit, i.e., the buying party will inform the offering gr:BusinessEntity about its bank account details and authorizes the gr:BusinessEntity to collect the agreed amount directly from that account."""
    Discover: NamedNode
    """Payment by credit or debit cards issued by the Discover network."""
    Dispose: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) the acceptance of the specified gr:ProductOrService for proper disposal, recycling, or any other kind of allowed usages, freeing the current owner from all rights and obligations of ownership."""
    Enduser: NamedNode
    """The gr:BusinessEntityType representing such agents that are purchasing the good or service for private consumption, in particular not for resale or for usage within an industrial enterprise. By default, a Business Entity is an Enduser."""
    FederalExpress: NamedNode
    """Delivery via the parcel service Federal Express."""
    Friday: NamedNode
    """Friday as a day of the week."""
    GoogleCheckout: NamedNode
    """Payment via the Google Checkout payment service."""
    Individual: NamedNode
    """A gr:Individual is an actual product or service instance, i.e., a single identifiable object or action that creates some increase in utility (in the economic sense) for the individual possessing or using this very object (product) or for the individual in whose favor this very action is being taken (service). Products or services are types of goods in the economic sense. For an overview of goods and commodities in economics, see Milgate (1987).

Examples: MyThinkpad T60, the pint of beer standing in front of me, my Volkswagen Golf, the haircut that I received or will be receiving at a given date and time.

Note 1: In many cases, product or service instances are not explicitly exposed on the Web but only claimed to exist (i.e. existentially quantified). In this case, use gr:SomeItems.
Note 2: This class is the new, shorter form of the former gr:ActualProductOrServiceInstance.

Compatibility with schema.org: This class is a subclass of http://schema.org/Product."""
    JCB: NamedNode
    """Payment by credit or debit cards issued by the JCB network."""
    LeaseOut: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) the temporary right to use the specified gr:ProductOrService."""
    License: NamedNode
    """A license is the specification of a bundle of rights that determines the type of activity or access offered by the gr:BusinessEntity on the gr:ProductOrService through the gr:Offering.
	
Licenses can be standardized (e.g. LPGL, Creative Commons, ...), vendor-specific, or individually defined for a single offer or product. Whether there is a fee for obtaining the license is specified using the gr:UnitPriceSpecification attached to the gr:Offering. Use foaf:page for linking to a document containing the license, e.g. in PDF or HTML."""
    Location: NamedNode
    """A location is a point or area of interest from which a particular product or service is available, e.g. a store, a bus stop, a gas station, or a ticket booth. The difference to gr:BusinessEntity is that the gr:BusinessEntity is the legal entity (e.g. a person or corporation) making the offer, while gr:Location is the store, office, or place. A chain restaurant will e.g. have one legal entity but multiple restaurant locations. Locations are characterized by an address or geographical position and a set of opening hour specifications for various days of the week.
		
Example: A rental car company may offer the Business Function Lease Out of cars from two locations, one in Fort Myers, Florida, and one in Boston, Massachussetts. Both stations are open 7:00 - 23:00 Mondays through Saturdays.

Note: Typical address standards (vcard) and location data (geo, WGC84) should be attached to a gr:Location node. Since there already exist established vocabularies for this, the GoodRelations ontology does not provide respective attributes. Instead, the use of respective vocabularies is recommended. However, the gr:hasGlobalLocationNumber property is  provided for linking to public identifiers for business locations.
		
Compatibility with schema.org: This class is equivalent to http://schema.org/Place."""
    LocationOfSalesOrServiceProvisioning: NamedNode
    """DEPRECATED - This class is superseded by gr:Location. Replace all occurrences of gr:LocationOfSalesOrServiceProvisioning by gr:Location, if possible."""
    Maintain: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) typical maintenance tasks for the specified gr:ProductOrService. Maintenance tasks are actions that undo or compensate for wear or other deterioriation caused by regular usage, in order to restore the originally intended function of the product, or to prevent outage or malfunction."""
    MasterCard: NamedNode
    """Payment by credit or debit cards issued by the MasterCard network."""
    Monday: NamedNode
    """Monday as a day of the week."""
    Offering: NamedNode
    """An offering represents the public, not necessarily binding, not necessarily exclusive, announcement by a gr:BusinessEntity to provide (or seek) a certain gr:BusinessFunction for a certain gr:ProductOrService to a specified target audience. An offering is specified by the type of product or service or bundle it refers to, what business function is being offered (sales, rental, ...), and a set of commercial properties. It can either refer to 
(1) a clearly specified instance (gr:Individual),
(2) to a set of anonymous instances of a given type (gr:SomeItems),
(3) a product model specification (gr:ProductOrServiceModel), see also section 3.3.3 of the GoodRelations Technical Report. 

An offering may be constrained in terms of the eligible type of business partner, countries, quantities, and other commercial properties. The definition of the commercial properties, the type of product offered, and the business function are explained in other parts of this vocabulary in more detail.

Example: Peter Miller offers to repair TV sets made by Siemens, Volkswagen Innsbruck sells a particular instance of a Volkswagen Golf at $10,000.

Compatibility with schema.org: This class is a superclass to http://schema.org/Offer, since gr:Offering can also represent demand."""
    OpeningHoursSpecification: NamedNode
    """This is a conceptual entity that holds together all information about the opening hours on a given day (gr:DayOfWeek)."""
    PayPal: NamedNode
    """Payment via the PayPal payment service."""
    PaySwarm: NamedNode
    """Payment via the PaySwarm distributed micropayment service."""
    PaymentChargeSpecification: NamedNode
    """A payment charge specification is a conceptual entity that specifies the additional costs asked for settling the payment after accepting a given gr:Offering using a particular gr:PaymentMethod. A payment charge specification is characterized by (1) a monetary amount per order specified as a literal value of type float in combination with a Currency, (2) the payment method, and (3) a whether this charge includes local sales taxes, namely VAT.
A gr:Offering may be linked to multiple payment charge specifications that specify alternative charges for various payment methods.

Examples: Payment by VISA or Mastercard costs a fee of 3 Euros including VAT, payment by bank transfer in advance is free of charge.

The total amount of this surcharge is specified as a float value of the gr:hasCurrencyValue property. The currency is specified via the gr:hasCurrency datatype property. Whether the price includes VAT or not is indicated by the gr:valueAddedTaxIncluded datatype property. The gr:PaymentMethod to which this charge applies is specified using the gr:appliesToPaymentMethod object property.

If the price can only be given as a range, use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue for the upper and lower bounds.

Important: When querying for the price, always use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue."""
    PaymentMethod: NamedNode
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction. This element is mostly used for specifying the types of payment accepted by a gr:BusinessEntity.

Examples: VISA, MasterCard, Diners, cash, or bank transfer in advance."""
    PaymentMethodCreditCard: NamedNode
    """The subclass of gr:PaymentMethod represents all variants and brands of credit or debit cards as a standardized procedure for transferring the monetary amount for a purchase. It is mostly used for specifying the types of payment accepted by a gr:Business Entity.

Examples: VISA, MasterCard, or American Express."""
    PriceSpecification: NamedNode
    """The superclass of all price specifications."""
    ProductOrService: NamedNode
    """The superclass of all classes describing products or services types, either by nature or purpose. Examples for such subclasses are "TV set", "vacuum cleaner", etc. An instance of this class can be either an actual product or service (gr:Individual), a placeholder instance for unknown instances of a mass-produced commodity (gr:SomeItems), or a model / prototype specification (gr:ProductOrServiceModel). When in doubt, use gr:SomeItems.

Examples: 
a) MyCellphone123, i.e. my personal, tangible cell phone (gr:Individual)
b) Siemens1234, i.e. the Siemens cell phone make and model 1234 (gr:ProductOrServiceModel)
c) dummyCellPhone123 as a placeholder for actual instances of a certain kind of cell phones (gr:SomeItems)
	
Note: Your first choice for specializations of gr:ProductOrService should be http://www.productontology.org.

Compatibility with schema.org: This class is (approximately) equivalent to http://schema.org/Product."""
    ProductOrServiceModel: NamedNode
    """A product or service model is a intangible entity that specifies some characteristics of a group of similar, usually mass-produced products, in the sense of a prototype. In case of mass-produced products, there exists a relation gr:hasMakeAndModel between the actual product or service (gr:Individual or gr:SomeItems) and the prototype (gr:ProductOrServiceModel). GoodRelations treats product or service models as "prototypes" instead of a completely separate kind of entities, because this allows using the same domain-specific properties (e.g. gr:weight) for describing makes and models and for describing actual products.

Examples: Ford T, Volkswagen Golf, Sony Ericsson W123 cell phone

Note: An actual product or service (gr:Individual) by default shares the features of its model (e.g. the weight). However, this requires non-standard reasoning. See http://wiki.goodrelations-vocabulary.org/Axioms for respective rule sets.
	
Compatibility with schema.org: This class is (approximately) a subclass of http://schema.org/Product."""
    ProductOrServicesSomeInstancesPlaceholder: NamedNode
    """DEPRECATED - This class is superseded by gr:SomeItems. Replace all occurrences of gr:ProductOrServicesSomeInstancesPlaceholder by gr:SomeItems, if possible."""
    ProvideService: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) the respective type of service.

Note: Maintain and Repair are also types of Services. However, products and services ontologies often provide classes for tangible products as well as for types of services. The business function gr:ProvideService is to be used with such goods that are services, while gr:Maintain and gr:Repair can be used with goods for which only the class of product exists in the ontology, but not the respective type of service.

Example: Car maintenance could be expressed both as "provide the service car maintenance" or "maintain cars"."""
    PublicHolidays: NamedNode
    """A placeholder for all official public holidays at the gr:Location. This allows specifying the opening hours on public holidays. If a given day is a public holiday, this specification supersedes the opening hours for the respective day of the week."""
    PublicInstitution: NamedNode
    """The gr:BusinessEntityType representing such agents that are part of the adminstration or owned by the public."""
    QualitativeValue: NamedNode
    """A qualitative value is a predefined value for a product characteristic. 
	
Examples: the color "green" or the power cord plug type "US"; the garment sizes "S", "M", "L", and "XL".
	
Note: Value sets are supported by creating subclasses of this class. Ordinal relations between values (gr:greater, gr:lesser, ...) are provided directly by GoodRelations.

Compatibility with schema.org: This class is equivalent to http://schema.org/Enumeration."""
    QuantitativeValue: NamedNode
    """A quantitative value is a numerical interval that represents the range of a certain gr:quantitativeProductOrServiceProperty in terms of the lower and upper bounds for a particular gr:ProductOrService. It is to be interpreted in combination with the respective unit of measurement. Most quantitative values are intervals even if they are in practice often treated as a single point value.
	
Example: a weight between 10 and 25 kilogramms, a length between 10 and 15 milimeters.

Compatibility with schema.org: This class is equivalent to http://schema.org/Quantity."""
    QuantitativeValueFloat: NamedNode
    """An instance of this class is an actual float value for a quantitative property of a product. This instance is usually characterized by a minimal value, a maximal value, and a unit of measurement.

Examples: The intervals "between 10.0  and 25.4 kilogramms" or "10.2 and 15.5 milimeters".

Compatibility with schema.org: This class is a subclass of http://schema.org/Quantity."""
    QuantitativeValueInteger: NamedNode
    """An instance of this class is an actual integer value for a quantitative property of a product. This instance is usually characterized by a minimal value, a maximal value, and a unit of measurement. 

Example: A seating capacity between 1 and 8 persons.

Note: Users must keep in mind that ranges in here mean that ALL possible values in this interval are covered. (Sometimes, the actual commitment may be less than that: "We sell cars from 2 - 12 seats" does often not really mean that they have cars with 2,3,4,...12 seats.). Someone renting out two types of rowing boats, one that fits for 1 or 2 people, and another that must be operated by 4 people cannot claim to rent boats with a seating capacity between 1 and 4 people. He or she is offering two boat types for 1-2 and 4 persons.
		
Compatibility with schema.org: This class is a subclass of http://schema.org/Quantity."""
    Repair: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers (or seeks) the evaluation of the chances for repairing, and, if positive, repair of the specified gr:ProductOrService. Repairing means actions that restore the originally intended function of a product that suffers from outage or malfunction."""
    Reseller: NamedNode
    """The gr:BusinessEntityType representing such agents that are purchasing the scope of products included in the gr:Offering for resale on the market. Resellers are also businesses, i.e., they are officially registered with the public administration and strive for profits by their activities."""
    Saturday: NamedNode
    """Saturday as a day of the week."""
    Sell: NamedNode
    """This gr:BusinessFunction indicates that the gr:BusinessEntity offers to permanently transfer all property rights on the specified gr:ProductOrService."""
    SomeItems: NamedNode
    """A placeholder instance for unknown instances of a mass-produced commodity. This is used as a computationally cheap work-around for such instances that are not individually exposed on the Web but just stated to exist (i.e., which are existentially quantified).

Example: An instance of this class can represent an anonymous set of green Siemens1234 phones. It is different from the gr:ProductOrServiceModel Siemens1234, since this refers to the make and model, and it is different from a particular instance of this make and model (e.g. my individual phone) since the latter can be sold only once.

Note: This class is the new, shorter form of the former gr:ProductOrServicesSomeInstancesPlaceholder.
		
Compatibility with schema.org: This class is (approximately) a subclass of http://schema.org/Product."""
    Sunday: NamedNode
    """Sunday as a day of the week."""
    Thursday: NamedNode
    """Thursday as a day of the week."""
    Tuesday: NamedNode
    """Tuesday as a day of the week."""
    TypeAndQuantityNode: NamedNode
    """This class collates all the information about a gr:ProductOrService included in a bundle. If a gr:Offering contains just one item, you can directly link from the gr:Offering to the gr:ProductOrService using gr:includes. If the offering contains multiple items, use an instance of this class for each component to indicate the quantity, unit of measurement, and type of product, and link from the gr:Offering via gr:includesObject.

Example: An offering may include of 100g of Butter and 1 kg of potatoes, or 1 cell phone and 2 headsets."""
    UPS: NamedNode
    """Delivery via the parcel service UPS."""
    UnitPriceSpecification: NamedNode
    """A unit price specification is a conceptual entity that specifies the price asked for a given gr:Offering by the respective gr:Business Entity. An offering may be linked to multiple unit price specifications that specify alternative prices for non-overlapping sets of conditions (e.g. quantities or sales regions) or with differing validity periods. 

A unit price specification is characterized by (1) the lower and upper limits and the unit of measurement of the eligible quantity, (2) by a monetary amount per unit of the product or service, and (3)  whether this prices includes local sales taxes, namely VAT.
	
Example: The price, including VAT, for 1 kg of a given material is 5 Euros per kg for 0 - 5 kg and 4 Euros for quantities above 5 kg.

The eligible quantity interval for a given price is specified using the object property gr:hasEligibleQuantity, which points to an instance of gr:QuantitativeValue. The currency is specified using the gr:hasCurrency property, which points to an ISO 4217 currency code. The unit of measurement for the eligible quantity is specified using the gr:hasUnitOfMeasurement datatype property, which points to an UN/CEFACT Common Code (3 characters).
	
In most cases, the appropriate unit of measurement is the UN/CEFACT Common Code "C62" for "Unit or piece", since a gr:Offering is defined by the quantity and unit of measurement of all items included (e.g. "1 kg of bananas plus a 2 kg of apples"). As long at the offering consists of only one item, it is also possible to use an unit of measurement of choice for specifying the price per unit. For bundles, however, only  "C62" for "Unit or piece" is a valid unit of measurement.

You can assume that the price is given per unit or piece if there is no gr:hasUnitOfMeasurement property attached to the price.
	
Whether VAT and sales taxes are included in this price is specified using the property gr:valueAddedTaxIncluded (xsd:boolean).
	
The price per unit of measurement is specified as a float value of the gr:hasCurrencyValue property. The currency is specified via the gr:hasCurrency datatype property. Whether the price includes VAT or not is indicated by the gr:valueAddedTaxIncluded datatype property.

The property priceType can be used to indicate that the price is a retail price recommendation only (i.e. a list price). 

If the price can only be given as a range, use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue for the upper and lower bounds.

Important: When querying for the price, always use gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue.

Note 1: Due to the complexity of pricing scenarios in various industries, it may be necessary to create extensions of this fundamental model of price specifications. Such can be done easily by importing and refining the GoodRelations ontology.

Note 2: For Google, attaching a gr:validThrough statement to a gr:UnitPriceSpecification is mandatory. 
"""
    VISA: NamedNode
    """Payment by credit or debit cards issued by the VISA network."""
    WarrantyPromise: NamedNode
    """This is a conceptual entity that holds together all aspects of the n-ary relation gr:hasWarrantyPromise.

A Warranty promise is an entity representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of the gr:ProductOrService. A warranty promise is characterized by its temporal duration (usually starting with the date of purchase) and its gr:WarrantyScope. The warranty scope represents the types of services provided (e.g. labor and parts, just parts) of the warranty included in an gr:Offering. The actual services may be provided by the gr:BusinessEntity making the offering, by the manufacturer of the product, or by a third party. There may be multiple warranty promises associated with a particular offering, which differ in duration and scope (e.g. pick-up service during the first 12 months, just parts and labor for 36 months).

Examples: 12 months parts and labor, 36 months parts"""
    WarrantyScope: NamedNode
    """The warranty scope represents types of services that will be provided free of charge by the vendor or manufacturer in the case of a defect (e.g. labor and parts, just parts), as part of the warranty included in an gr:Offering. The actual services may be provided by the gr:BusinessEntity making the offering, by the manufacturer of the product, or by a third party. 

Examples: Parts and Labor, Parts"""
    Wednesday: NamedNode
    """Wednesday as a day of the week."""
    acceptedPaymentMethods: NamedNode
    """The gr:PaymentMethod or methods accepted by the gr:BusinessEntity for the given gr:Offering."""
    addOn: NamedNode
    """This property points from a gr:Offering to additional offerings that can only be obtained in combination with the first offering. This can be used to model supplements and extensions that are available for a surcharge. Any gr:PriceSpecification attached to the secondary offering is to be understood as an additional charge."""
    advanceBookingRequirement: NamedNode
    """The minimal and maximal amount of time that is required between accepting the gr:Offering and the actual usage of the resource or service. This is mostly relevant for offers regarding hotel rooms, the rental of objects, or the provisioning of services. The duration is specified relatively to the beginning of the usage of the contracted object. It is represented by attaching an instance of the class gr:QuantitativeValueInteger. The lower and upper boundaries are specified using the properties gr:hasMinValueInteger and gr:hasMaxValueInteger to that instance. The unit of measurement is specified using the property gr:hasUnitOfMeasurement with a string holding a UN/CEFACT code suitable for durations, e.g. MON (months), DAY (days), HUR (hours), or MIN (minutes).

The difference to the gr:validFrom and gr:validThrough properties is that those specify the interval during which the gr:Offering is valid, while gr:advanceBookingRequirement specifies the acceptable relative amount of time between accepting the offer and the fulfilment or usage."""
    amountOfThisGood: NamedNode
    """This property specifies the quantity of the goods included in the gr:Offering via this gr:TypeAndQuantityNode. The quantity is given in the unit of measurement attached to the gr:TypeAndQuantityNode."""
    appliesToDeliveryMethod: NamedNode
    """This property specifies the gr:DeliveryMethod to which the gr:DeliveryChargeSpecification applies."""
    appliesToPaymentMethod: NamedNode
    """This property specifies the gr:PaymentMethod to which the gr:PaymentChargeSpecification applies."""
    availabilityEnds: NamedNode
    """This property specifies the end of the availability of the gr:ProductOrService included in the gr:Offering.
The difference to the properties gr:validFrom and gr:validThrough is that those specify the period of time during which the offer is valid and can be accepted.

Example: I offer to lease my boat for the period of August 1 - August 31, 2010, but you must accept by offer no later than July 15.

A time-zone should be specified. For a time in GMT/UTC, simply add a "Z" following the time:

2008-05-30T09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

2008-05-30T09:30:10-09:00

or

2008-05-30T09:30:10+09:00.

Note: There is another property gr:availableAtOrFrom, which is used to indicate the gr:Location (e.g. store or shop) from which the goods would be available."""
    availabilityStarts: NamedNode
    """This property specifies the beginning of the availability of the gr:ProductOrService included in the gr:Offering.
The difference to the properties gr:validFrom and gr:validThrough is that those specify the period of time during which the offer is valid and can be accepted.

Example: I offer to lease my boat for the period of August 1 - August 31, 2010, but you must accept by offer no later than July 15.

A time-zone should be specified. For a time in GMT/UTC, simply add a "Z" following the time:

2008-05-30T09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

2008-05-30T09:30:10-09:00

or

2008-05-30T09:30:10+09:00.

Note: There is another property gr:availableAtOrFrom, which is used to indicate the gr:Location (e.g. store or shop) from which the goods would be available."""
    availableAtOrFrom: NamedNode
    """This states that a particular gr:Offering is available at or from the given gr:Location (e.g. shop or branch)."""
    availableDeliveryMethods: NamedNode
    """This specifies the gr:DeliveryMethod or methods available for a given gr:Offering."""
    billingIncrement: NamedNode
    """This property specifies the minimal quantity and rounding increment that will be the basis for the billing. 
The unit of measurement is specified by the UN/CEFACT code attached to the gr:UnitPriceSpecification via the gr:hasUnitOfMeasurement property.

Examples: 
- The price for gasoline is 4 USD per gallon at the pump, but you will be charged in units of 0.1 gallons.
- The price for legal consulting is 100 USD per hour, but you will be charged in units of 15 minutes.

This property makes sense only for instances of gr:Offering that include not more than one type of good or service."""
    category: NamedNode
    """The name of a category to which this gr:ProductOrService, gr:Offering, gr:BusinessEntity, or gr:Location belongs.
	
Note 1: For products, it is better to add an rdf:type statement referring to a GoodRelations-compliant ontology for vertical industries instead, but if you just have a short text label, gr:category is simpler.
Note 2: You can use greater signs or slashes to informally indicate a category hierarchy, e.g. "restaurants/asian_restaurants" or "cables > usb_cables"
"""
    closes: NamedNode
    """The closing  hour of the gr:Location on the given gr:DayOfWeek.
If no time-zone suffix is included, the time is given in the local time valid at the gr:Location.

For a time in GMT/UTC, simply add a "Z" following the time:

09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

09:30:10-09:00

09:30:10+09:00.

Note 1: Use 00:00:00 for the first second of the respective day and 23:59:59 for the last second of that day.
Note 2: If a store opens at 17:00 on Saturdays and closes at 03:00:00 a.m. next morning, use two instances of this class, one with 17:00:00 - 23:59:59 for Saturday and another one with 00:00:00 - 03:00:00 for Sunday.
Note 3: If the shop re-opens on the same day of the week or set of days of the week, you must create a second instance of gr:OpeningHoursSpecification."""
    color: NamedNode
    """The color of the product."""
    condition: NamedNode
    """A textual description of the condition of the product or service, or the products or services included in the offer (when attached to a gr:Offering)"""
    datatypeProductOrServiceProperty: NamedNode
    """This property is the super property for all pure datatype properties that can be used to describe a gr:ProductOrService.

In products and services ontologies, only such properties that are no quantitative properties and that have no predefined gr:QualitativeValue instances are subproperties of this property. In practice, this refers to a few integer properties for which the integer value represents qualitative aspects, for string datatypes (as long as no predefined values exist), for boolean datatype properties, and for dates and times."""
    deliveryLeadTime: NamedNode
    """This property can be used to indicate the promised delay between the receipt of the order and the goods leaving the warehouse.

The duration is specified by attaching an instance of gr:QuantitativeValueInteger. The lower and upper boundaries are specified using the properties gr:hasMinValueInteger and gr:hasMaxValueInteger to that instance. A point value can be modeled with the gr:hasValueInteger property. The unit of measurement is specified using the property gr:hasUnitOfMeasurement with a string holding a UN/CEFACT code suitable for durations, e.g. MON (months), DAY (days), HUR (hours), or MIN (minutes)."""
    depth: NamedNode
    """The depth of the product.
Typical unit code(s): CMT for centimeters, INH for inches"""
    description: NamedNode
    """A short textual description of the resource. 

This property is semantically equivalent to rdfs:comment and just meant as a handy shortcut for marking up data."""
    displayPosition: NamedNode
    """The position at which the option or element should be listed in a menu or user dialog, lower numbers come first.

The main usage of this property are the days of the week (gr:DayOfWeek), but it is also possible to apply it e.g. to product features or any other conceptual element.
Note: Rely on this property only for data originating from a single RDF graph; otherwise, unpredictable results are possible."""
    durationOfWarrantyInMonths: NamedNode
    """This property specifies the duration of the gr:WarrantyPromise in months."""
    eligibleCustomerTypes: NamedNode
    """The types of customers (gr:BusinessEntityType) for which the given gr:Offering is valid."""
    eligibleDuration: NamedNode
    """The minimal and maximal duration for which the given gr:Offering or gr:License is valid. This is mostly used for offers regarding accommodation, the rental of objects, or software licenses. The duration is specified by attaching an instance of gr:QuantitativeValue. The lower and upper boundaries are specified using the properties gr:hasMinValue and gr:hasMaxValue to that instance. If they are the same, use the gr:hasValue property. The unit of measurement is specified using the property gr:hasUnitOfMeasurement with a string holding a UN/CEFACT code suitable for durations, e.g. MON (months), DAY (days), HUR (hours), or MIN (minutes).

The difference to the gr:validFrom and gr:validThrough properties is that those specify the absiolute interval during which the gr:Offering or gr:License is valid, while gr:eligibleDuration specifies the acceptable duration of the contract or usage."""
    eligibleRegions: NamedNode
    """This property specifies the geo-political region or regions for which the gr:Offering, gr:License, or gr:DeliveryChargeSpecification is valid using the two-character version of ISO 3166-1 (ISO 3166-1 alpha-2)  for regions or ISO 3166-2 , which breaks down the countries from ISO 3166-1 into administrative subdivisions.

Important: Do NOT use 3-letter ISO 3166-1 codes!"""
    eligibleTransactionVolume: NamedNode
    """This property can be used to indicate the transaction volume, in a monetary unit, for which the gr:Offering or gr:PriceSpecification is valid. This is mostly used to specify a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases above a certain amount.

The object is a gr:PriceSpecification that uses the properties gr:hasMaxCurrencyValue and gr:hasMinCurrencyValue to indicate the lower and upper boundaries and gr:hasCurrency to indicate the currency using the ISO 4217 standard (3 characters)."""
    equal: NamedNode
    """This ordering relation for qualitative values indicates that the subject is equal to the object."""
    greater: NamedNode
    """This ordering relation for qualitative values indicates that the subject is greater than the object."""
    greaterOrEqual: NamedNode
    """This ordering relation for qualitative values indicates that the subject is greater than or equal to the object."""
    hasBrand: NamedNode
    """This specifies the brand or brands (gr:Brand) associated with a gr:ProductOrService, or the brand or brands maintained by a gr:BusinessEntity."""
    hasBusinessFunction: NamedNode
    """This specifies the business function of the gr:Offering, i.e. whether the gr:BusinessEntity is offering to sell, to lease, or to repair the particular type of product. In the case of bundles, it is also possible to attach individual business functions to each gr:TypeAndQuantityNode. The business function of the main gr:Offering determines the business function for all included objects or services, unless a business function attached to a gr:TypeAndQuantityNode overrides it.
	
Note: While it is possible that an entity is offering multiple types of business functions for the same set of objects (e.g. rental and sales), this should usually not be stated by attaching multiple business functions to the same gr:Offering, since the gr:UnitPriceSpecification for the varying business functions will typically be very different."""
    hasCurrency: NamedNode
    """The currency for all prices in the gr:PriceSpecification given using the ISO 4217 standard (3 characters)."""
    hasCurrencyValue: NamedNode
    """This property specifies the amount of money for a price per unit, shipping charges, or payment charges. The currency and other relevant details are attached to the respective gr:PriceSpecification etc.

For a gr:UnitPriceSpecification, this is the price for one unit or bundle (as specified in the unit of measurement of the unit price specification) of the respective gr:ProductOrService. For a gr:DeliveryChargeSpecification or a gr:PaymentChargeSpecification, it is the price per delivery or payment.

GoodRelations also supports giving price information as intervals only. If this is needed, use gr:hasMaxCurrencyValue for the upper bound and gr:hasMinCurrencyValue for the lower bound. 

Using gr:hasCurrencyValue sets the upper and lower bounds to the same given value, i.e., x gr:hasCurrencyValue y implies x gr:hasMinCurrencyValue y, x gr:hasMaxCurrencyValue y."""
    hasDUNS: NamedNode
    """The Dun & Bradstreet DUNS number for identifying a gr:BusinessEntity. The Dun & Bradstreet DUNS is a nine-digit number used to identify legal entities (but usually not branches or locations of logistical importance only)."""
    hasEligibleQuantity: NamedNode
    """This specifies the interval and unit of measurement of ordering quantities for which the gr:Offering or gr:PriceSpecification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
Note that if an offering is a bundle, i.e. it consists of more than one unit of a single type of good, or if the unit of measurement for the good is different from unit (Common Code C62), then gr:hasEligibleQuantity refers to units of this bundle. In other words, "C62" for "Units or pieces" is usually the appropriate unit of measurement."""
    hasGlobalLocationNumber: NamedNode
    """The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective gr:BusinessEntity or gr:Location.
The Global Location Number is a thirteen-digit number used to identify parties and physical locations."""
    hasISICv4: NamedNode
    """The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular gr:BusinessEntity or gr:Location. See http://unstats.un.org/unsd/cr/registry/isic-4.asp for more information.

Note: While ISIC codes are sometimes misused for classifying products or services, they are designed and suited only for classifying business establishments."""
    hasInventoryLevel: NamedNode
    """This property specifies the current approximate inventory level for gr:SomeItems. The unit of measurement and the point value or interval are indicated using the attached gr:QuantitativeValueFloat instance.

This property can also be attached to a gr:Offering in cases where the included products are not modeled in more detail."""
    hasMPN: NamedNode
    """The Manufacturer Part Number or MPN is a unique identifier for a product, service, or bundle from the perspective of a particular manufacturer. MPNs can be assigned to products or product datasheets, or bundles. Accordingly, the domain of this property is the union of gr:ProductOrService (the common superclass of goods and datasheets), and gr:Offering.

Important: Be careful when assuming two products or services instances or offering instances to be identical based on the MPN. Since MPNs are unique only for the same gr:BusinessEntity, this holds only when the two MPN values refer to the same gr:BusinessEntity. Such can be done by taking into account the provenance of the data. 

Usually, the properties gr:hasEAN_UCC-13 and gr:hasGTIN-14 are much more reliable identifiers, because they are globally unique.

See also http://en.wikipedia.org/wiki/Part_number"""
    hasMakeAndModel: NamedNode
    """This states that an actual product instance (gr:Individual) or a placeholder instance for multiple, unidentified such instances (gr:SomeItems) is one occurence of a particular gr:ProductOrServiceModel.

Example: myFordT hasMakeAndModel FordT."""
    hasManufacturer: NamedNode
    """This object property links a gr:ProductOrService to the gr:BusinessEntity that produces it. Mostly used with gr:ProductOrServiceModel."""
    hasMaxCurrencyValue: NamedNode
    """This property specifies the UPPER BOUND of the amount of money for a price RANGE per unit, shipping charges, or payment charges. The currency and other relevant details are attached to the respective gr:PriceSpecification etc.
For a gr:UnitPriceSpecification, this is the UPPER BOUND for the price for one unit or bundle (as specified in the unit of measurement of the unit price specification) of the respective gr:ProductOrService. For a gr:DeliveryChargeSpecification or a gr:PaymentChargeSpecification, it is the UPPER BOUND of the price per delivery or payment.

Using gr:hasCurrencyValue sets the upper and lower bounds to the same given value, i.e., x gr:hasCurrencyValue y implies x gr:hasMinCurrencyValue y, x gr:hasMaxCurrencyValue y."""
    hasMaxValue: NamedNode
    """This property captures the upper limit of a gr:QuantitativeValue instance."""
    hasMaxValueFloat: NamedNode
    """This property captures the upper limit of a gr:QuantitativeValueFloat instance."""
    hasMaxValueInteger: NamedNode
    """This property captures the upper limit of a gr:QuantitativeValueInteger instance."""
    hasMinCurrencyValue: NamedNode
    """This property specifies the LOWER BOUND of the amount of money for a price RANGE per unit, shipping charges, or payment charges. The currency and other relevant details are attached to the respective gr:PriceSpecification etc.
For a gr:UnitPriceSpecification, this is the LOWER BOUND for the price for one unit or bundle (as specified in the unit of measurement of the unit price specification) of the respective gr:ProductOrService. For a gr:DeliveryChargeSpecification or a gr:PaymentChargeSpecification, it is the LOWER BOUND of the price per delivery or payment.

Using gr:hasCurrencyValue sets the upper and lower bounds to the same given value, i.e., x gr:hasCurrencyValue y implies x gr:hasMinCurrencyValue y, x gr:hasMaxCurrencyValue y."""
    hasMinValue: NamedNode
    """This property captures the lower limit of a gr:QuantitativeValue instance."""
    hasMinValueFloat: NamedNode
    """This property captures the lower limit of a gr:QuantitativeValueFloat instance."""
    hasMinValueInteger: NamedNode
    """This property captures the lower limit of a gr:QuantitativeValueInteger instance."""
    hasNAICS: NamedNode
    """The North American Industry Classification System (NAICS) code for a particular gr:BusinessEntity.
See http://www.census.gov/eos/www/naics/ for more details.

Note: While NAICS codes are sometimes misused for classifying products or services, they are designed and suited only for classifying business establishments."""
    hasNext: NamedNode
    """This ordering relation for gr:DayOfWeek indicates that the subject is directly followed by the object.

Example: Monday hasNext Tuesday

Since days of the week are a cycle, this property is not transitive."""
    hasOpeningHoursDayOfWeek: NamedNode
    """This specifies the gr:DayOfWeek to which the gr:OpeningHoursSpecification is related.

Note: Use multiple instances of gr:OpeningHoursSpecification for specifying the opening hours for multiple days if the opening hours differ."""
    hasOpeningHoursSpecification: NamedNode
    """This property links a gr:Location to a gr:OpeningHoursSpecification."""
    hasPOS: NamedNode
    """This property states that the respective gr:Location is a point of sale for the respective gr:BusinessEntity. It allows linking those two types of entities without the need for a particular gr:Offering."""
    hasPrevious: NamedNode
    """This ordering relation for gr:DayOfWeek indicates that the subject is directly preceeded by the object.

Example: Tuesday hasPrevious Monday

Since days of the week are a cycle, this property is not transitive."""
    hasPriceSpecification: NamedNode
    """This links a gr:Offering to a gr:PriceSpecification or specifications. There can be unit price specifications, payment charge specifications, and delivery charge specifications. For each type, multiple specifications for the same gr:Offering are possible, e.g. for different quantity ranges or for different currencies, or for different combinations of gr:DeliveryMethod and target destinations.

Recommended retail prices etc. can be marked by the gr:priceType property of the gr:UnitPriceSpecification."""
    hasStockKeepingUnit: NamedNode
    """The Stock Keeping Unit, or SKU is a unique identifier for a product, service, or bundle from the perspective of a particular supplier, i.e. SKUs are mostly assigned and serialized at the merchant level. 
Examples of SKUs are the ordering or parts numbers used by a particular Web shop or catalog.

Consequently, the domain of gr:hasStockKeepingUnit is the union of the classes gr:Offering and gr:ProductOrService. 
If attached to a gr:Offering, the SKU will usually reflect a merchant-specific identifier, i.e. one valid only for that particular retailer or shop. 
If attached to a gr:ProductOrServiceModel, the SKU can reflect either the identifier used by the merchant or the part number used by the official manufacturer of that part. For the latter, gr:hasMPN is a better choice.

Important: Be careful when assuming two products or services instances or offering instances to be identical based on the SKU. Since SKUs are unique only for the same gr:BusinessEntity, this can be assumed only when you are sure that the two SKU values refer to the same business entity. Such can be done by taking into account the provenance of the data. As long as instances of gr:Offering are concerned, you can also check that the offerings are being offered by the same gr:Business Entity.

Usually, the properties gr:hasEAN_UCC-13 and gr:hasGTIN-14 are much more reliable identifiers, because they are globally unique.

See also http://en.wikipedia.org/wiki/Stock_Keeping_Unit."""
    hasUnitOfMeasurement: NamedNode
    """The unit of measurement for a gr:QuantitativeValue, a gr:UnitPriceSpecification, or a gr:TypeAndQuantityNode given using the UN/CEFACT Common Code (3 characters)."""
    hasValue: NamedNode
    """This subproperty specifies that the upper and lower limit of the given gr:QuantitativeValue are identical and have the respective value. It is a shortcut for such cases where a quantitative property is (at least practically) a single point value and not an interval."""
    hasValueFloat: NamedNode
    """This subproperty specifies that the upper and lower limit of the given gr:QuantitativeValueFloat are identical and have the respective float value. It is a shortcut for such cases where a quantitative property is (at least practically) a single point value and not an interval."""
    hasValueInteger: NamedNode
    """This subproperty specifies that the upper and lower limit of the given gr:QuantitativeValueInteger are identical and have the respective integer value. It is a shortcut for such cases where a quantitative property is (at least practically) a single point value and not an interval."""
    hasWarrantyPromise: NamedNode
    """This specifies the gr:WarrantyPromise made by the gr:BusinessEntity for the given gr:Offering."""
    hasWarrantyScope: NamedNode
    """This states the gr:WarrantyScope of a given gr:WarrantyPromise."""
    height: NamedNode
    """The height of the product.
Typical unit code(s): CMT for centimeters, INH for inches"""
    includes: NamedNode
    """This object property is a shortcut for the original gr:includesObject property for the common case of having exactly one single gr:ProductOrService instance included in an Offering. 

When linking to an instance of gr:SomeItems or gr:Individual, it is equivalent to using a gr:TypeAndQuantityNode with gr:hasUnitOfMeasurement="C62"^^xsd:string and gr:amountOfThisGood="1.0"^^xsd:float for that good.

When linking to a gr:ProductOrServiceModel, it is equivalent to 
1. defining an blank node for a gr:SomeItems
2. linking that blank node via gr:hasMakeAndModel to the gr:ProductOrServiceModel, and
3. linking from the gr:Offering to that blank node using another blank node of type gr:TypeAndQuantityNode with gr:hasUnitOfMeasurement="C62"^^xsd:string and gr:amountOfThisGood="1.0"^^xsd:float for that good."""
    includesObject: NamedNode
    """This object property links a gr:Offering to one or multiple gr:TypeAndQuantityNode or nodes that specify the components that are included in the respective offer."""
    isAccessoryOrSparePartFor: NamedNode
    """This states that a particular gr:ProductOrService is an accessory or spare part for another product or service."""
    isConsumableFor: NamedNode
    """This states that a particular gr:ProductOrService is a consumable for another product or service."""
    isListPrice: NamedNode
    """This boolean attribute indicates whether a gr:UnitPriceSpecification is a list price (usually a vendor recommendation) or not. "true"  indicates it is a list price, "false" indicates it is not.
DEPRECATED. Use the gr:priceType property instead."""
    isSimilarTo: NamedNode
    """This states that a given gr:ProductOrService is similar to another product or service. Of course, this is a subjective statement; when interpreting it, the trust in the origin of the statement should be taken into account."""
    isVariantOf: NamedNode
    """This states that a particular gr:ProductOrServiceModel is a variant of another product or service model. It is pretty safe to infer that the variant inherits all gr:quantitativeProductOrServiceProperty, gr:qualitativeProductOrServiceProperty, and gr:datatypeProductOrServiceProperty values that are defined for the first gr:ProductOrServiceModel.

Example:
foo:Red_Ford_T_Model gr:isVariantOf foo:Ford_T_Model"""
    legalName: NamedNode
    """The legal name of the gr:BusinessEntity."""
    lesser: NamedNode
    """This ordering relation for gr:QualitativeValue pairs indicates that the subject is lesser than the object."""
    lesserOrEqual: NamedNode
    """This ordering relation for gr:QualitativeValue pairs indicates that the subject is lesser than or equal to the object."""
    name: NamedNode
    """A short text describing the respective resource.

This property is semantically equivalent to dcterms:title and rdfs:label and just meant as a handy shortcut for marking up data."""
    nonEqual: NamedNode
    """This ordering relation for gr:QualitativeValue pairs indicates that the subject is not equal to the object."""
    offers: NamedNode
    """This links a gr:BusinessEntity to the offers (gr:Offering) it makes. If you want to express interest in receiving offers, use gr:seeks instead."""
    opens: NamedNode
    """The opening hour of the gr:Location on the given gr:DayOfWeek.
If no time-zone suffix is included, the time is given in the local time valid at the gr:Location.

For a time in GMT/UTC, simply add a "Z" following the time:

09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

09:30:10-09:00

or

09:30:10+09:00.

Note 1: Use 00:00:00 for the first second of the respective day and 23:59:59 for the last second of that day.
Note 2: If a store opens at 17:00 on Saturdays and closes at 03:00:00 a.m. next morning, use 17:00:00 - 23:59:59 for Saturday and 00:00:00 - 03:00:00 for Sunday.
Note 3: If the shop re-opens on the same day of the week or set of days of the week, you must create a second instance of gr:OpeningHoursSpecification."""
    owns: NamedNode
    """This property indicates that a particular person or business owns a particular product. It can be used to expose the products in one's posession in order to empower recommender systems to suggest matching offers.

Note that the product must be an instance of the class gr:Individual.

This property can also be safely applied to foaf:Agent instances."""
    predecessorOf: NamedNode
    """This property indicates that the subject is a previous, often discontinued variant of the gr:ProductOrServiceModel used as the object.

Example: Golf III predecessorOf Golf IV

This relation is transitive."""
    priceType: NamedNode
    """This attribute can be used to distinguish multiple different price specifications for the same gr:Offering. It supersedes the former gr:isListPrice property. The following values are recommended:

The absence of this property marks the actual sales price.

SRP: "suggested retail price" - applicable for all sorts of a non-binding retail price recommendations, e.g. such published by the manufacturer or the distributor. This value replaces the former gr:isListPrice property.

INVOICE: The invoice price, mostly used in the car industry - this is the price a dealer pays to the manufacturer, excluding rebates and charges."""
    qualitativeProductOrServiceProperty: NamedNode
    """This is the super property of all qualitative properties for products and services. All properties in product or service ontologies for which gr:QualitativeValue instances are specified are subproperties of this property."""
    quantitativeProductOrServiceProperty: NamedNode
    """This is the super property of all quantitative  properties for products and services. All properties in product or service ontologies that specify quantitative characteristics, for which an interval is at least theoretically an appropriate value, are subproperties of this property."""
    relatedWebService: NamedNode
    """The URI of a SOAP or REST Web Service from which additional information about the gr:BusinessEntity, gr:Offering, gr:PriceSpecification, or gr:ProductOrService, or any other element,  can be obtained. The recommended range is xsd:anyURI i.e., the URI of a SOAP or REST Web Service.

In principle, any existing or upcoming vocabulary for Web Services can be used in combination with GoodRelations, because the association between (a) the service description and (b) the GoodRelations description can be found via the Web Service URI value used with this gr:relatedWebService property."""
    seeks: NamedNode
    """This links a gr:BusinessEntity to gr:Offering nodes that describe what the business entity is interested in (i.e., the buy side). If you want to express interest in offering something, use gr:offers instead. Note that this substitutes the former gr:BusinessFunction gr:Buy, which is now deprecated."""
    serialNumber: NamedNode
    """The serial number or any alphanumeric identifier of a particular product. Note that serial number are unique only for the same brand or the same model, so you cannot infer from two occurrences of the same serial number that the objects to which they are attached are identical.

This property can also be attached to a gr:Offering in cases where the included products are not modeled in more detail."""
    successorOf: NamedNode
    """This property indicates that the subject is a newer, often updated or improved variant of the gr:ProductOrServiceModel used as the object.

Example: Golf III successorOf Golf II

This relation is transitive."""
    taxID: NamedNode
    """The Tax / Fiscal ID of the gr:BusinessEntity, e.g. the TIN in the US or the CIF/NIF in Spain. It is usually assigned by the country of residence"""
    typeOfGood: NamedNode
    """This specifies the gr:ProductOrService that the gr:TypeAndQuantityNode is referring to."""
    validFrom: NamedNode
    """This property specifies the beginning of the validity of the gr:Offering, gr:PriceSpecification, gr:License, or gr:OpeningHoursSpecification.
A time-zone should be specified. For a time in GMT/UTC, simply add a "Z" following the time:

2008-05-30T09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

2008-05-30T09:30:10-09:00

or

2008-05-30T09:30:10+09:00.

Note: If multiple contradicting instances of a gr:Offering, gr:PriceSpecification, or gr:OpeningHoursSpecification exist, it is a good heuristics to assume that
1. Information with validity information for the respective period of time ranks higher than information without validity information.
2. Among conflicting nodes both having validity information, the one with the shorter validity span ranks higher."""
    validThrough: NamedNode
    """This property specifies the end of the validity of the gr:Offering, gr:PriceSpecification, gr:License, or gr:OpeningHoursSpecification.
A time-zone should be specified. For a time in GMT/UTC, simply add a "Z" following the time:

2008-05-30T09:30:10Z.

Alternatively, you can specify an offset from the UTC time by adding a positive or negative time following the time:

2008-05-30T09:30:10-09:00

or
2008-05-30T09:30:10+09:00.

Note 1: If multiple contradicting instances of a gr:Offering, gr:PriceSpecification, or gr:OpeningHoursSpecification exist, it is a good heuristics to assume that
1. Information with validity information for the respective period of time ranks higher than information without validity information.
2. Among conflicting nodes both having validity information, the one with the shorter validity span ranks higher.
Note 2: For Google, attaching a gr:validThrough statement to a gr:UnitPriceSpecification is mandatory. 
"""
    valueAddedTaxIncluded: NamedNode
    """This property specifies whether the applicable value-added tax (VAT)  is included in the price of the gr:PriceSpecification or not.

Note: This is a simple representation which may not properly reflect all details of local taxation."""
    valueReference: NamedNode
    """The superclass of properties that link a gr:QuantitativeValue or a gr:QualitativeValue to a second gr:QuantitativeValue or a gr:QualitativeValue that provides additional information on the original value. A good modeling practice is to define specializations of this property (e.g. foo:referenceTemperature) for your particular domain."""
    vatID: NamedNode
    """The Value-added Tax ID of the gr:BusinessEntity. See http://en.wikipedia.org/wiki/Value_added_tax_identification_number for details."""
    weight: NamedNode
    """The weight of the gr:ProductOrService.
Typical unit code(s): GRM for gram, KGM for kilogram, LBR for pound"""
    width: NamedNode
    """The width of the gr:ProductOrService.
Typical unit code(s): CMT for centimeters, INH for inches"""
