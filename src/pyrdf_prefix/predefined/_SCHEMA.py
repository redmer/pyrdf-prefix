from pyoxigraph import NamedNode

from pyrdf_prefix.namespace import PredefinedNamespace


class SCHEMA(PredefinedNamespace):
    """Schema.org"""

    # Conversion-Date: 2024-09-30T10:48+00:00
    # Source: https://schema.org/version/latest/schemaorg-all-https.nt

    _nsBaseIri = "https://schema.org/"
    _issueWarning = True
    _withContainerMembershipProperty = False
    _nonPyIdentifiers = ("3DModel", "False", "True", "yield")

    AMRadioChannel: NamedNode
    """A radio channel that uses AM."""
    APIReference: NamedNode
    """Reference documentation for application programming interfaces (APIs)."""
    Abdomen: NamedNode
    """Abdomen clinical examination."""
    AboutPage: NamedNode
    """Web page type: About page."""
    AcceptAction: NamedNode
    """The act of committing to/adopting an object.\n\nRelated actions:\n\n* [[RejectAction]]: The antonym of AcceptAction."""
    Accommodation: NamedNode
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
For more specific types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    AccountingService: NamedNode
    """Accountancy business.\n\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]'(s).
      """
    AchieveAction: NamedNode
    """The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process."""
    Action: NamedNode
    """An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.\n\nSee also [blog post](http://blog.schema.org/2014/04/announcing-schemaorg-actions.html) and [Actions overview document](https://schema.org/docs/actions.html)."""
    ActionAccessSpecification: NamedNode
    """A set of requirements that must be fulfilled in order to perform an Action."""
    ActionStatusType: NamedNode
    """The status of an Action."""
    ActivateAction: NamedNode
    """The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight)."""
    ActivationFee: NamedNode
    """Represents the activation fee part of the total price for an offered product, for example a cellphone contract."""
    ActiveActionStatus: NamedNode
    """An in-progress action (e.g., while watching the movie, or driving to a location)."""
    ActiveNotRecruiting: NamedNode
    """Active, but not recruiting new participants."""
    AddAction: NamedNode
    """The act of editing by adding an object to a collection."""
    AdministrativeArea: NamedNode
    """A geographical region, typically under the jurisdiction of a particular government."""
    AdultEntertainment: NamedNode
    """An adult entertainment establishment."""
    AdultOrientedEnumeration: NamedNode
    """Enumeration of considerations that make a product relevant or potentially restricted for adults only."""
    AdvertiserContentArticle: NamedNode
    """An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content."""
    AerobicActivity: NamedNode
    """Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise."""
    AggregateOffer: NamedNode
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.\n\nNote: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined."""
    AggregateRating: NamedNode
    """The average rating based on multiple ratings or reviews."""
    AgreeAction: NamedNode
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants."""
    Airline: NamedNode
    """An organization that provides flights for passengers."""
    Airport: NamedNode
    """An airport."""
    AlbumRelease: NamedNode
    """AlbumRelease."""
    AlcoholConsideration: NamedNode
    """Item contains alcohol or promotes alcohol consumption."""
    AlgorithmicMediaDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    AlgorithmicallyEnhancedDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicallyEnhanced">algorithmically enhanced</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    AlignmentObject: NamedNode
    """An intangible item that describes an alignment between a learning resource and a node in an educational framework.

Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency."""
    AllWheelDriveConfiguration: NamedNode
    """All-wheel Drive is a transmission layout where the engine drives all four wheels."""
    AllergiesHealthAspect: NamedNode
    """Content about the allergy-related aspects of a health topic."""
    AllocateAction: NamedNode
    """The act of organizing tasks/objects/events by associating resources to it."""
    AmpStory: NamedNode
    """A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices."""
    AmusementPark: NamedNode
    """An amusement park."""
    AnaerobicActivity: NamedNode
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body."""
    AnalysisNewsArticle: NamedNode
    """An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting, incorporates the expertise of the author/producer, offering interpretations and conclusions."""
    AnatomicalStructure: NamedNode
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures."""
    AnatomicalSystem: NamedNode
    """An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can include circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems."""
    AndroidPlatform: NamedNode
    """Represents the broad notion of Android-based operating systems."""
    Anesthesia: NamedNode
    """A specific branch of medical science that pertains to study of anesthetics and their application."""
    AnimalShelter: NamedNode
    """Animal shelter."""
    Answer: NamedNode
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong."""
    Apartment: NamedNode
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>)."""
    ApartmentComplex: NamedNode
    """Residence type: Apartment complex."""
    Appearance: NamedNode
    """Appearance assessment with clinical examination."""
    AppendAction: NamedNode
    """The act of inserting at the end if an ordered collection."""
    ApplyAction: NamedNode
    """The act of registering to an organization/service without the guarantee to receive it.\n\nRelated actions:\n\n* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted."""
    ApprovedIndication: NamedNode
    """An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US."""
    Aquarium: NamedNode
    """Aquarium."""
    ArchiveComponent: NamedNode
    """An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections."""
    ArchiveOrganization: NamedNode
    """An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public."""
    ArriveAction: NamedNode
    """The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants."""
    ArtGallery: NamedNode
    """An art gallery."""
    Artery: NamedNode
    """A type of blood vessel that specifically carries blood away from the heart."""
    Article: NamedNode
    """An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.\n\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html)."""
    AskAction: NamedNode
    """The act of posing a question / favor to someone.\n\nRelated actions:\n\n* [[ReplyAction]]: Appears generally as a response to AskAction."""
    AskPublicNewsArticle: NamedNode
    """A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the public for input, insights, clarifications, anecdotes, documentation, etc., on an issue, for reporting purposes."""
    AssessAction: NamedNode
    """The act of forming one's opinion, reaction or sentiment."""
    AssignAction: NamedNode
    """The act of allocating an action/event/task to some destination (someone or something)."""
    Atlas: NamedNode
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject."""
    Attorney: NamedNode
    """Professional service: Attorney. \n\nThis type is deprecated - [[LegalService]] is more inclusive and less ambiguous."""
    Audience: NamedNode
    """Intended audience for an item, i.e. the group for whom the item was created."""
    AudioObject: NamedNode
    """An audio file."""
    AudioObjectSnapshot: NamedNode
    """A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity."""
    Audiobook: NamedNode
    """An audiobook."""
    AudiobookFormat: NamedNode
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties."""
    AuthoritativeLegalValue: NamedNode
    """Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications.) Something "Authoritative" is considered to be also [[OfficialLegalValue]]."""
    AuthorizeAction: NamedNode
    """The act of granting permission to an object."""
    AutoBodyShop: NamedNode
    """Auto body shop."""
    AutoDealer: NamedNode
    """An car dealership."""
    AutoPartsStore: NamedNode
    """An auto parts store."""
    AutoRental: NamedNode
    """A car rental business."""
    AutoRepair: NamedNode
    """Car repair business."""
    AutoWash: NamedNode
    """A car wash business."""
    AutomatedTeller: NamedNode
    """ATM/cash machine."""
    AutomotiveBusiness: NamedNode
    """Car repair, sales, or parts."""
    Ayurvedic: NamedNode
    """A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit."""
    BackOrder: NamedNode
    """Indicates that the item is available on back order."""
    BackgroundNewsArticle: NamedNode
    """A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective."""
    Bacteria: NamedNode
    """Pathogenic bacteria that cause bacterial infection."""
    Bakery: NamedNode
    """A bakery."""
    Balance: NamedNode
    """Physical activity that is engaged to help maintain posture and balance."""
    BankAccount: NamedNode
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest."""
    BankOrCreditUnion: NamedNode
    """Bank or credit union."""
    BarOrPub: NamedNode
    """A bar or pub."""
    Barcode: NamedNode
    """An image of a visual machine-readable code such as a barcode or QR code."""
    BasicIncome: NamedNode
    """BasicIncome: this is a benefit for basic income."""
    Beach: NamedNode
    """Beach."""
    BeautySalon: NamedNode
    """Beauty salon."""
    BedAndBreakfast: NamedNode
    """Bed and breakfast.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    BedDetails: NamedNode
    """An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development)."""
    BedType: NamedNode
    """A type of bed. This is used for indicating the bed or beds available in an accommodation."""
    BefriendAction: NamedNode
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\n\nRelated actions:\n\n* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal."""
    BenefitsHealthAspect: NamedNode
    """Content about the benefits and advantages of usage or utilization of topic."""
    BikeStore: NamedNode
    """A bike store."""
    BioChemEntity: NamedNode
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical."""
    Blog: NamedNode
    """A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a "weblog". Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially referred to by the same term."""
    BlogPosting: NamedNode
    """A blog post."""
    BloodTest: NamedNode
    """A medical test performed on a sample of a patient's blood."""
    BoardingPolicyType: NamedNode
    """A type of boarding policy used by an airline."""
    BoatReservation: NamedNode
    """A reservation for boat travel.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    BoatTerminal: NamedNode
    """A terminal for boats, ships, and other water vessels."""
    BoatTrip: NamedNode
    """A trip on a commercial ferry line."""
    BodyMeasurementArm: NamedNode
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts."""
    BodyMeasurementBust: NamedNode
    """Maximum girth of bust. Used, for example, to fit women's suits."""
    BodyMeasurementChest: NamedNode
    """Maximum girth of chest. Used, for example, to fit men's suits."""
    BodyMeasurementFoot: NamedNode
    """Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks."""
    BodyMeasurementHand: NamedNode
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves."""
    BodyMeasurementHead: NamedNode
    """Maximum girth of head above the ears. Used, for example, to fit hats."""
    BodyMeasurementHeight: NamedNode
    """Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets."""
    BodyMeasurementHips: NamedNode
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts."""
    BodyMeasurementInsideLeg: NamedNode
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants."""
    BodyMeasurementNeck: NamedNode
    """Girth of neck. Used, for example, to fit shirts."""
    BodyMeasurementTypeEnumeration: NamedNode
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes."""
    BodyMeasurementUnderbust: NamedNode
    """Girth of body just below the bust. Used, for example, to fit women's swimwear."""
    BodyMeasurementWaist: NamedNode
    """Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants."""
    BodyMeasurementWeight: NamedNode
    """Body weight. Used, for example, to measure pantyhose."""
    BodyOfWater: NamedNode
    """A body of water, such as a sea, ocean, or lake."""
    Bone: NamedNode
    """Rigid connective tissue that comprises up the skeletal structure of the human body."""
    Book: NamedNode
    """A book."""
    BookFormatType: NamedNode
    """The publication format of the book."""
    BookSeries: NamedNode
    """A series of books. Included books can be indicated with the hasPart property."""
    BookStore: NamedNode
    """A bookstore."""
    BookmarkAction: NamedNode
    """An agent bookmarks/flags/labels/tags/marks an object."""
    Boolean: NamedNode
    """Boolean: True or False."""
    BorrowAction: NamedNode
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.\n\nRelated actions:\n\n* [[LendAction]]: Reciprocal of BorrowAction."""
    BowlingAlley: NamedNode
    """A bowling alley."""
    BrainStructure: NamedNode
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity."""
    Brand: NamedNode
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar."""
    BreadcrumbList: NamedNode
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.\n\nThe [[position]] property is used to reconstruct the order of the items in a BreadcrumbList. The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]] (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.
      """
    Brewery: NamedNode
    """Brewery."""
    Bridge: NamedNode
    """A bridge."""
    BroadcastChannel: NamedNode
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup."""
    BroadcastEvent: NamedNode
    """An over the air or online broadcast event."""
    BroadcastFrequencySpecification: NamedNode
    """The frequency in MHz and the modulation used for a particular BroadcastService."""
    BroadcastRelease: NamedNode
    """BroadcastRelease."""
    BroadcastService: NamedNode
    """A delivery service through which content is provided via broadcast over the air or online."""
    BrokerageAccount: NamedNode
    """An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm."""
    BuddhistTemple: NamedNode
    """A Buddhist temple."""
    BusOrCoach: NamedNode
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury buses, usually in service for long distance travel."""
    BusReservation: NamedNode
    """A reservation for bus travel. \n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    BusStation: NamedNode
    """A bus station."""
    BusStop: NamedNode
    """A bus stop."""
    BusTrip: NamedNode
    """A trip on a commercial bus line."""
    BusinessAudience: NamedNode
    """A set of characteristics belonging to businesses, e.g. who compose an item's target audience."""
    BusinessEntityType: NamedNode
    """A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#Business\n* http://purl.org/goodrelations/v1#Enduser\n* http://purl.org/goodrelations/v1#PublicInstitution\n* http://purl.org/goodrelations/v1#Reseller
    """
    BusinessEvent: NamedNode
    """Event type: Business event."""
    BusinessFunction: NamedNode
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#ConstructionInstallation\n* http://purl.org/goodrelations/v1#Dispose\n* http://purl.org/goodrelations/v1#LeaseOut\n* http://purl.org/goodrelations/v1#Maintain\n* http://purl.org/goodrelations/v1#ProvideService\n* http://purl.org/goodrelations/v1#Repair\n* http://purl.org/goodrelations/v1#Sell\n* http://purl.org/goodrelations/v1#Buy
        """
    BusinessSupport: NamedNode
    """BusinessSupport: this is a benefit for supporting businesses."""
    BuyAction: NamedNode
    """The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction."""
    ByBankTransferInAdvance: NamedNode
    """Payment in advance by bank transfer, equivalent to <code>http://purl.org/goodrelations/v1#ByBankTransferInAdvance</code>."""
    ByInvoice: NamedNode
    """Payment by invoice, typically after the goods were delivered, equivalent to <code>http://purl.org/goodrelations/v1#ByInvoice</code>."""
    CDCPMDRecord: NamedNode
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
      definitions used as the source here.
      """
    CDFormat: NamedNode
    """CDFormat."""
    COD: NamedNode
    """Cash on Delivery (COD) payment, equivalent to <code>http://purl.org/goodrelations/v1#COD</code>."""
    CT: NamedNode
    """X-ray computed tomography imaging."""
    CableOrSatelliteService: NamedNode
    """A service which provides access to media programming like TV or radio. Access may be via cable or satellite."""
    CafeOrCoffeeShop: NamedNode
    """A cafe or coffee shop."""
    Campground: NamedNode
    """A camping site, campsite, or [[Campground]] is a place used for overnight stay in the outdoors, typically containing individual [[CampingPitch]] locations. \n\n
In British English a campsite is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites (source: Wikipedia, see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite)).\n\n

See also the dedicated [document on the use of schema.org for marking up hotels and other forms of accommodations](/docs/hotels.html).
"""
    CampingPitch: NamedNode
    """A [[CampingPitch]] is an individual place for overnight stay in the outdoors, typically being part of a larger camping site, or [[Campground]].\n\n
In British English a campsite, or campground, is an area, usually divided into a number of pitches, where people can camp overnight using tents or camper vans or caravans; this British English use of the word is synonymous with the American English expression campground. In American English the term campsite generally means an area where an individual, family, group, or military unit can pitch a tent or park a camper; a campground may contain many campsites.
(Source: Wikipedia, see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite).)\n\n
See also the dedicated [document on the use of schema.org for marking up hotels and other forms of accommodations](/docs/hotels.html).
"""
    Canal: NamedNode
    """A canal, like the Panama Canal."""
    CancelAction: NamedNode
    """The act of asserting that a future event/action is no longer going to happen.\n\nRelated actions:\n\n* [[ConfirmAction]]: The antonym of CancelAction."""
    Car: NamedNode
    """A car is a wheeled, self-powered motor vehicle used for transportation."""
    CarUsageType: NamedNode
    """A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi."""
    Cardiovascular: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature."""
    CardiovascularExam: NamedNode
    """Cardiovascular system assessment with clinical examination."""
    CaseSeries: NamedNode
    """A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection."""
    Cash: NamedNode
    """Payment using cash, on premises, equivalent to <code>http://purl.org/goodrelations/v1#Cash</code>."""
    Casino: NamedNode
    """A casino."""
    CassetteFormat: NamedNode
    """CassetteFormat."""
    CategoryCode: NamedNode
    """A Category Code."""
    CategoryCodeSet: NamedNode
    """A set of Category Code values."""
    CatholicChurch: NamedNode
    """A Catholic church."""
    CausesHealthAspect: NamedNode
    """Information about the causes and main actions that gave rise to the topic."""
    Cemetery: NamedNode
    """A graveyard."""
    Certification: NamedNode
    """A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary."""
    CertificationActive: NamedNode
    """Specifies that a certification is active."""
    CertificationInactive: NamedNode
    """Specifies that a certification is inactive (no longer in effect)."""
    CertificationStatusEnumeration: NamedNode
    """Enumerates the different statuses of a Certification (Active and Inactive)."""
    Chapter: NamedNode
    """One of the sections into which a book is divided. A chapter usually has a section number or a name."""
    CharitableIncorporatedOrganization: NamedNode
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK)."""
    CheckAction: NamedNode
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state."""
    CheckInAction: NamedNode
    """The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).\n\nRelated actions:\n\n* [[CheckOutAction]]: The antonym of CheckInAction.\n* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.\n* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence."""
    CheckInAdvance: NamedNode
    """Payment in advance by sending a check, equivalent to <code>http://purl.org/goodrelations/v1#CheckInAdvance</code>."""
    CheckOutAction: NamedNode
    """The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check-in) or place (e.g. hotel).\n\nRelated actions:\n\n* [[CheckInAction]]: The antonym of CheckOutAction.\n* [[DepartAction]]: Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.\n* [[CancelAction]]: Unlike CancelAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service."""
    CheckoutPage: NamedNode
    """Web page type: Checkout page."""
    ChemicalSubstance: NamedNode
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999))."""
    ChildCare: NamedNode
    """A Childcare center."""
    ChildrensEvent: NamedNode
    """Event type: Children's event."""
    Chiropractic: NamedNode
    """A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning."""
    ChooseAction: NamedNode
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options."""
    Church: NamedNode
    """A church."""
    City: NamedNode
    """A city or town."""
    CityHall: NamedNode
    """A city hall."""
    CivicStructure: NamedNode
    """A public structure, such as a town hall or concert hall."""
    Claim: NamedNode
    """A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized with the [[text]] property. Variations on well known claims can have their common identity indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]] description includes enough contextual information to minimize the risk of ambiguity or inclarity. In practice, many claims are better understood in the context in which they appear or the interpretations provided by claim reviews.

  Beyond [[ClaimReview]], the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]] or [[Question]] might be [[about]] some [[Claim]].

  At this time, Schema.org does not define any types of relationship between claims. This is a natural area for future exploration.
  """
    ClaimReview: NamedNode
    """A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed)."""
    Class: NamedNode
    """A class, also often called a 'Type'; equivalent to rdfs:Class."""
    CleaningFee: NamedNode
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental."""
    Clinician: NamedNode
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice."""
    Clip: NamedNode
    """A short TV or radio program or a segment/part of a program."""
    ClothingStore: NamedNode
    """A clothing store."""
    CoOp: NamedNode
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends."""
    Code: NamedNode
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates."""
    CohortStudy: NamedNode
    """Also known as a panel study. A cohort study is a form of longitudinal study used in medicine and social science. It is one type of study design and should be compared with a cross-sectional study.  A cohort is a group of people who share a common characteristic or experience within a defined period (e.g., are born, leave school, lose their job, are exposed to a drug or a vaccine, etc.). The comparison group may be the general population from which the cohort is drawn, or it may be another cohort of persons thought to have had little or no exposure to the substance under investigation, but otherwise similar. Alternatively, subgroups within the cohort may be compared with each other."""
    Collection: NamedNode
    """A collection of items, e.g. creative works or products."""
    CollectionPage: NamedNode
    """Web page type: Collection page."""
    CollegeOrUniversity: NamedNode
    """A college, university, or other third-level educational institution."""
    ComedyClub: NamedNode
    """A comedy club."""
    ComedyEvent: NamedNode
    """Event type: Comedy event."""
    ComicCoverArt: NamedNode
    """The artwork on the cover of a comic."""
    ComicIssue: NamedNode
    """Individual comic issues are serially published as
    	part of a larger series. For the sake of consistency, even one-shot issues
    	belong to a series comprised of a single issue. All comic issues can be
    	uniquely identified by: the combination of the name and volume number of the
    	series to which the issue belongs; the issue number; and the variant
    	description of the issue (if any)."""
    ComicSeries: NamedNode
    """A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer"."""
    ComicStory: NamedNode
    """The term "story" is any indivisible, re-printable
    	unit of a comic, including the interior stories, covers, and backmatter. Most
    	comics have at least two stories: a cover (ComicCoverArt) and an interior story."""
    Comment: NamedNode
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks."""
    CommentAction: NamedNode
    """The act of generating a comment about a subject."""
    CommentPermission: NamedNode
    """Permission to add comments to the document."""
    CommunicateAction: NamedNode
    """The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation."""
    CommunityHealth: NamedNode
    """A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas."""
    CompilationAlbum: NamedNode
    """CompilationAlbum."""
    CompleteDataFeed: NamedNode
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes content for every item currently in the feed.

This is the equivalent of Atom's element as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005), for example (and as defined for Atom), when using data from a feed that represents a collection of items that varies over time (e.g. "Top Twenty Records") there is no need to have newer entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed, old entries can be safely discarded when the feed is refreshed, since we can assume the feed has provided descriptions for all current items."""
    Completed: NamedNode
    """Completed."""
    CompletedActionStatus: NamedNode
    """An action that has already taken place."""
    CompositeCaptureDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeCapture">composite capture</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    CompositeSyntheticDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic">composite synthetic</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    CompositeWithTrainedAlgorithmicMediaDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia">composite with trained algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    CompoundPriceSpecification: NamedNode
    """A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning")."""
    ComputerLanguage: NamedNode
    """This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type."""
    ComputerStore: NamedNode
    """A computer store."""
    ConfirmAction: NamedNode
    """The act of notifying someone that a future event/action is going to happen as expected.\n\nRelated actions:\n\n* [[CancelAction]]: The antonym of ConfirmAction."""
    Consortium: NamedNode
    """A Consortium is a membership [[Organization]] whose members are typically Organizations."""
    ConstraintNode: NamedNode
    """The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a
    variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values."""
    ConsumeAction: NamedNode
    """The act of ingesting information/resources/food."""
    ContactPage: NamedNode
    """Web page type: Contact page."""
    ContactPoint: NamedNode
    """A contact point&#x2014;for example, a Customer Complaints department."""
    ContactPointOption: NamedNode
    """Enumerated options related to a ContactPoint."""
    ContagiousnessHealthAspect: NamedNode
    """Content about contagion mechanisms and contagiousness information over the topic."""
    Continent: NamedNode
    """One of the continents (for example, Europe or Africa)."""
    ControlAction: NamedNode
    """An agent controls a device or application."""
    ConvenienceStore: NamedNode
    """A convenience store."""
    Conversation: NamedNode
    """One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties."""
    CookAction: NamedNode
    """The act of producing/preparing food."""
    Corporation: NamedNode
    """Organization: A business corporation."""
    CorrectionComment: NamedNode
    """A [[comment]] that corrects [[CreativeWork]]."""
    Country: NamedNode
    """A country."""
    Course: NamedNode
    """A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners."""
    CourseInstance: NamedNode
    """An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students."""
    Courthouse: NamedNode
    """A courthouse."""
    CoverArt: NamedNode
    """The artwork on the outer surface of a CreativeWork."""
    CovidTestingFacility: NamedNode
    """A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus
      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other
      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information
      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.
      """
    CreateAction: NamedNode
    """The act of deliberately creating/producing/generating/building a result out of the agent."""
    CreativeWork: NamedNode
    """The most generic kind of creative work, including books, movies, photographs, software programs, etc."""
    CreativeWorkSeason: NamedNode
    """A media season, e.g. TV, radio, video game etc."""
    CreativeWorkSeries: NamedNode
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind. CreativeWorkSeries are usually organized into some order, often chronological. Unlike [[ItemList]] which is a general purpose data structure for lists of things, the emphasis with CreativeWorkSeries is on published materials (written e.g. books and periodicals, or media such as TV, radio and games).\n\nSpecific subtypes are available for describing [[TVSeries]], [[RadioSeries]], [[MovieSeries]], [[BookSeries]], [[Periodical]] and [[VideoGameSeries]]. In each case, the [[hasPart]] / [[isPartOf]] properties can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely just to organize these more specific and practical subtypes.\n\nIt is common for properties applicable to an item from the series to be usefully applied to the containing group. Schema.org attempts to anticipate some of these cases, but publishers should be free to apply properties of the series parts to the series as a whole wherever they seem appropriate.
    """
    CreditCard: NamedNode
    """A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#AmericanExpress\n* http://purl.org/goodrelations/v1#DinersClub\n* http://purl.org/goodrelations/v1#Discover\n* http://purl.org/goodrelations/v1#JCB\n* http://purl.org/goodrelations/v1#MasterCard\n* http://purl.org/goodrelations/v1#VISA
       """
    Crematorium: NamedNode
    """A crematorium."""
    CriticReview: NamedNode
    """A [[CriticReview]] is a more specialized form of Review written or published by a source that is recognized for its reviewing activities. These can include online columns, travel and food guides, TV and radio shows, blogs and other independent Web sites. [[CriticReview]]s are typically more in-depth and professionally written. For simpler, casually written user/visitor/viewer/customer reviews, it is more appropriate to use the [[UserReview]] type. Review aggregator sites such as Metacritic already separate out the site's user reviews from selected critic reviews that originate from third-party sources."""
    CrossSectional: NamedNode
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies."""
    CssSelectorType: NamedNode
    """Text representing a CSS selector."""
    CurrencyConversionService: NamedNode
    """A service to convert funds from one currency to another currency."""
    DDxElement: NamedNode
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it."""
    DJMixAlbum: NamedNode
    """DJMixAlbum."""
    DVDFormat: NamedNode
    """DVDFormat."""
    DamagedCondition: NamedNode
    """Indicates that the item is damaged."""
    DanceEvent: NamedNode
    """Event type: A social dance."""
    DanceGroup: NamedNode
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance."""
    DangerousGoodConsideration: NamedNode
    """The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf) defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more."""
    DataCatalog: NamedNode
    """A collection of datasets."""
    DataDownload: NamedNode
    """All or part of a [[Dataset]] in downloadable form. """
    DataDrivenMediaDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/dataDrivenMedia">data driven media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    DataFeed: NamedNode
    """A single feed providing structured information about one or more entities or topics."""
    DataFeedItem: NamedNode
    """A single item within a larger data feed."""
    DataType: NamedNode
    """The basic data types such as Integers, Strings, etc."""
    Dataset: NamedNode
    """A body of structured information describing some topic(s) of interest."""
    Date: NamedNode
    """A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)."""
    DateTime: NamedNode
    """A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601)."""
    DatedMoneySpecification: NamedNode
    """A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended."""
    DayOfWeek: NamedNode
    """The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.

Originally, URLs from [GoodRelations](http://purl.org/goodrelations/v1) were used (for [[Monday]], [[Tuesday]], [[Wednesday]], [[Thursday]], [[Friday]], [[Saturday]], [[Sunday]] plus a special entry for [[PublicHolidays]]); these have now been integrated directly into schema.org.
      """
    DaySpa: NamedNode
    """A day spa."""
    DeactivateAction: NamedNode
    """The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight)."""
    DecontextualizedContent: NamedNode
    """Content coded 'missing context' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'missing context': Presenting unaltered video in an inaccurate manner that misrepresents the footage. For example, using incorrect dates or locations, altering the transcript or sharing brief clips from a longer video to mislead viewers. (A video rated 'original' can also be missing context.)

For an [[ImageObject]] to be 'missing context': Presenting unaltered images in an inaccurate manner to misrepresent the image and mislead the viewer. For example, a common tactic is using an unaltered image but saying it came from a different time or place. (An image rated 'original' can also be missing context.)

For an [[ImageObject]] with embedded text to be 'missing context': An unaltered image presented in an inaccurate manner to misrepresent the image and mislead the viewer. For example, a common tactic is using an unaltered image but saying it came from a different time or place. (An 'original' image with inaccurate text would generally fall in this category.)

For an [[AudioObject]] to be 'missing context': Unaltered audio presented in an inaccurate manner that misrepresents it. For example, using incorrect dates or locations, or sharing brief clips from a longer recording to mislead viewers. (Audio rated “original” can also be missing context.)
"""
    DefenceEstablishment: NamedNode
    """A defence establishment, such as an army or navy base."""
    DefinedRegion: NamedNode
    """A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria. Properties are provided for defining a region by reference to sets of postal codes.

Examples: a delivery destination when shopping. Region where regional pricing is configured.

Requirement 1:
Country: US
States: "NY", "CA"

Requirement 2:
Country: US
PostalCode Set: { [94000-94585], [97000, 97999], [13000, 13599]}
{ [12345, 12345], [78945, 78945], }
Region = state, canton, prefecture, autonomous community...
"""
    DefinedTerm: NamedNode
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term."""
    DefinedTermSet: NamedNode
    """A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration."""
    DefinitiveLegalValue: NamedNode
    """Indicates a document for which the text is conclusively what the law says and is legally binding. (E.g. the digitally signed version of an Official Journal.)
  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]]."""
    DeleteAction: NamedNode
    """The act of editing a recipient by removing one of its objects."""
    DeliveryChargeSpecification: NamedNode
    """The price for the delivery of an offer using a particular delivery method."""
    DeliveryEvent: NamedNode
    """An event involving the delivery of an item."""
    DeliveryMethod: NamedNode
    """A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload\n* http://purl.org/goodrelations/v1#DeliveryModeFreight\n* http://purl.org/goodrelations/v1#DeliveryModeMail\n* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet\n* http://purl.org/goodrelations/v1#DeliveryModePickUp\n* http://purl.org/goodrelations/v1#DHL\n* http://purl.org/goodrelations/v1#FederalExpress\n* http://purl.org/goodrelations/v1#UPS
        """
    DeliveryTimeSettings: NamedNode
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]]."""
    Demand: NamedNode
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply."""
    DemoAlbum: NamedNode
    """DemoAlbum."""
    DemoGameAvailability: NamedNode
    """Indicates demo game availability, i.e. a somehow limited demonstration of the full game."""
    Dentist: NamedNode
    """A dentist."""
    Dentistry: NamedNode
    """A branch of medicine that is involved in the dental care."""
    DepartAction: NamedNode
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants."""
    DepartmentStore: NamedNode
    """A department store."""
    DepositAccount: NamedNode
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits."""
    Dermatologic: NamedNode
    """Something relating to or practicing dermatology."""
    Dermatology: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin."""
    DesktopWebPlatform: NamedNode
    """Represents the broad notion of 'desktop' browsers as a Web Platform."""
    DiabeticDiet: NamedNode
    """A diet appropriate for people with diabetes."""
    Diagnostic: NamedNode
    """A medical device used for diagnostic purposes."""
    DiagnosticLab: NamedNode
    """A medical laboratory that offers on-site or off-site diagnostic services."""
    DiagnosticProcedure: NamedNode
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes."""
    Diet: NamedNode
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related goal."""
    DietNutrition: NamedNode
    """Dietetics and nutrition as a medical specialty."""
    DietarySupplement: NamedNode
    """A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites."""
    DigitalArtDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalArt">digital art</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    DigitalAudioTapeFormat: NamedNode
    """DigitalAudioTapeFormat."""
    DigitalCaptureDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture">digital capture</a></a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    DigitalDocument: NamedNode
    """An electronic file or document."""
    DigitalDocumentPermission: NamedNode
    """A permission for a particular person or group to access a particular file."""
    DigitalDocumentPermissionType: NamedNode
    """A type of permission which can be granted for accessing a digital document."""
    DigitalFormat: NamedNode
    """DigitalFormat."""
    DigitalPlatformEnumeration: NamedNode
    """Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057). """
    DirectDebit: NamedNode
    """Payment in advance by direct debit from the bank, equivalent to <code>http://purl.org/goodrelations/v1#DirectDebit</code>."""
    DisabilitySupport: NamedNode
    """DisabilitySupport: this is a benefit for disability support."""
    DisagreeAction: NamedNode
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants."""
    Discontinued: NamedNode
    """Indicates that the item has been discontinued."""
    DiscoverAction: NamedNode
    """The act of discovering/finding an object."""
    DiscussionForumPosting: NamedNode
    """A posting to a discussion forum."""
    DislikeAction: NamedNode
    """The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants."""
    Distance: NamedNode
    """Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'."""
    DistanceFee: NamedNode
    """Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental."""
    Distillery: NamedNode
    """A distillery."""
    DonateAction: NamedNode
    """The act of providing goods, services, or money without compensation, often for philanthropic reasons."""
    DoseSchedule: NamedNode
    """A specific dosing schedule for a drug or supplement."""
    DoubleBlindedTrial: NamedNode
    """A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to."""
    DownloadAction: NamedNode
    """The act of downloading an object."""
    Downpayment: NamedNode
    """Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments."""
    DrawAction: NamedNode
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments."""
    Drawing: NamedNode
    """A picture or diagram made with a pencil, pen, or crayon rather than paint."""
    DrinkAction: NamedNode
    """The act of swallowing liquids."""
    DriveWheelConfigurationValue: NamedNode
    """A value indicating which roadwheels will receive torque."""
    DrivingSchoolVehicleUsage: NamedNode
    """Indicates the usage of the vehicle for driving school."""
    Drug: NamedNode
    """A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism. Here the term drug is used interchangeably with the term medicine although clinical knowledge makes a clear difference between them."""
    DrugClass: NamedNode
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc."""
    DrugCost: NamedNode
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup."""
    DrugCostCategory: NamedNode
    """Enumerated categories of medical drug costs."""
    DrugLegalStatus: NamedNode
    """The legal availability status of a medical drug."""
    DrugPregnancyCategory: NamedNode
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy."""
    DrugPrescriptionStatus: NamedNode
    """Indicates whether this drug is available by prescription or over-the-counter."""
    DrugStrength: NamedNode
    """A specific strength in which a medical drug is available in a specific country."""
    DryCleaningOrLaundry: NamedNode
    """A dry-cleaning business."""
    Duration: NamedNode
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601))."""
    EBook: NamedNode
    """Book format: Ebook."""
    EPRelease: NamedNode
    """EPRelease."""
    EUEnergyEfficiencyCategoryA: NamedNode
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryA1Plus: NamedNode
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryA2Plus: NamedNode
    """Represents EU Energy Efficiency Class A++ as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryA3Plus: NamedNode
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryB: NamedNode
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryC: NamedNode
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryD: NamedNode
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryE: NamedNode
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryF: NamedNode
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyCategoryG: NamedNode
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations."""
    EUEnergyEfficiencyEnumeration: NamedNode
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369."""
    Ear: NamedNode
    """Ear function assessment with clinical examination."""
    EatAction: NamedNode
    """The act of swallowing solid objects."""
    EditedOrCroppedContent: NamedNode
    """Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'edited or cropped content': The video has been edited or rearranged. This category applies to time edits, including editing multiple videos together to alter the story being told or editing out large portions from a video.

For an [[ImageObject]] to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.

For an [[ImageObject]] with embedded text to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.

For an [[AudioObject]] to be 'edited or cropped content': The audio has been edited or rearranged. This category applies to time edits, including editing multiple audio clips together to alter the story being told or editing out large portions from the recording.
"""
    EducationEvent: NamedNode
    """Event type: Education event."""
    EducationalAudience: NamedNode
    """An EducationalAudience."""
    EducationalOccupationalCredential: NamedNode
    """An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer."""
    EducationalOccupationalProgram: NamedNode
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree)."""
    EducationalOrganization: NamedNode
    """An educational organization."""
    EffectivenessHealthAspect: NamedNode
    """Content about the effectiveness-related aspects of a health topic."""
    Electrician: NamedNode
    """An electrician."""
    ElectronicsStore: NamedNode
    """An electronics store."""
    ElementarySchool: NamedNode
    """An elementary school."""
    EmailMessage: NamedNode
    """An email message."""
    Embassy: NamedNode
    """An embassy."""
    Emergency: NamedNode
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness."""
    EmergencyService: NamedNode
    """An emergency service, such as a fire station or ER."""
    EmployeeRole: NamedNode
    """A subclass of OrganizationRole used to describe employee relationships."""
    EmployerAggregateRating: NamedNode
    """An aggregate rating of an Organization related to its role as an employer."""
    EmployerReview: NamedNode
    """An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization."""
    EmploymentAgency: NamedNode
    """An employment agency."""
    Endocrine: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions."""
    EndorseAction: NamedNode
    """An agent approves/certifies/likes/supports/sanctions an object."""
    EndorsementRating: NamedNode
    """An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a
"Like" or "+1" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively by
some [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]].

An [[EndorsementRating]] may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive,
endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.
"""
    Energy: NamedNode
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'."""
    EnergyConsumptionDetails: NamedNode
    """EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US."""
    EnergyEfficiencyEnumeration: NamedNode
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards."""
    EnergyStarCertified: NamedNode
    """Represents EnergyStar certification."""
    EnergyStarEnergyEfficiencyEnumeration: NamedNode
    """Used to indicate whether a product is EnergyStar certified."""
    EngineSpecification: NamedNode
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities."""
    EnrollingByInvitation: NamedNode
    """Enrolling participants by invitation only."""
    EntertainmentBusiness: NamedNode
    """A business providing entertainment."""
    EntryPoint: NamedNode
    """An entry point, within some Web-based protocol."""
    Enumeration: NamedNode
    """Lists or enumerations—for example, a list of cuisines or music genres, etc."""
    Episode: NamedNode
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season."""
    Event: NamedNode
    """An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the [[offers]] property. Repeated events may be structured as separate Event objects."""
    EventAttendanceModeEnumeration: NamedNode
    """An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline."""
    EventCancelled: NamedNode
    """The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s)."""
    EventMovedOnline: NamedNode
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online."""
    EventPostponed: NamedNode
    """The event has been postponed and no new date has been set. The event's previousStartDate should be set."""
    EventRescheduled: NamedNode
    """The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)"""
    EventReservation: NamedNode
    """A reservation for an event like a concert, sporting event, or lecture.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    EventScheduled: NamedNode
    """The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default."""
    EventSeries: NamedNode
    """A series of [[Event]]s. Included events can relate with the series using the [[superEvent]] property.

An EventSeries is a collection of events that share some unifying characteristic. For example, "The Olympic Games" is a series, which
is repeated regularly. The "2012 London Olympics" can be presented both as an [[Event]] in the series "Olympic Games", and as an
[[EventSeries]] that included a number of sporting competitions as Events.

The nature of the association between the events in an [[EventSeries]] can vary, but typical examples could
include a thematic event series (e.g. topical meetups or classes), or a series of regular events that share a location, attendee group and/or organizers.

EventSeries has been defined as a kind of Event to make it easy for publishers to use it in an Event context without
worrying about which kinds of series are really event-like enough to call an Event. In general an EventSeries
may seem more Event-like when the period of time is compact and when aspects such as location are fixed, but
it may also sometimes prove useful to describe a longer-term series as an Event.
   """
    EventStatusType: NamedNode
    """EventStatusType is an enumeration type whose instances represent several states that an Event may be in."""
    EventVenue: NamedNode
    """An event venue."""
    EvidenceLevelA: NamedNode
    """Data derived from multiple randomized clinical trials or meta-analyses."""
    EvidenceLevelB: NamedNode
    """Data derived from a single randomized trial, or nonrandomized studies."""
    EvidenceLevelC: NamedNode
    """Only consensus opinion of experts, case studies, or standard-of-care."""
    ExampleMeasurementMethodEnum: NamedNode
    """An example [[MeasurementMethodEnum]] (to remove when real enums are added)."""
    ExchangeRateSpecification: NamedNode
    """A structured value representing exchange rate."""
    ExchangeRefund: NamedNode
    """Specifies that a refund can be done as an exchange for the same product."""
    ExerciseAction: NamedNode
    """The act of participating in exertive activity for the purposes of improving health and fitness."""
    ExerciseGym: NamedNode
    """A gym."""
    ExercisePlan: NamedNode
    """Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician."""
    ExhibitionEvent: NamedNode
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ..."""
    Eye: NamedNode
    """Eye or ophthalmological function assessment with clinical examination."""
    FAQPage: NamedNode
    """A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]])."""
    FDAcategoryA: NamedNode
    """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters)."""
    FDAcategoryB: NamedNode
    """A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women."""
    FDAcategoryC: NamedNode
    """A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks."""
    FDAcategoryD: NamedNode
    """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks."""
    FDAcategoryX: NamedNode
    """A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits."""
    FDAnotEvaluated: NamedNode
    """A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA."""
    FMRadioChannel: NamedNode
    """A radio channel that uses FM."""
    FailedActionStatus: NamedNode
    """An action that failed to complete. The action's error property and the HTTP return code contain more information about the failure."""
    FastFoodRestaurant: NamedNode
    """A fast-food restaurant."""
    Female: NamedNode
    """The female gender."""
    Festival: NamedNode
    """Event type: Festival."""
    FilmAction: NamedNode
    """The act of capturing sound and moving images on film, video, or digitally."""
    FinancialProduct: NamedNode
    """A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry."""
    FinancialService: NamedNode
    """Financial services business."""
    FindAction: NamedNode
    """The act of finding an object.\n\nRelated actions:\n\n* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily."""
    FireStation: NamedNode
    """A fire station. With firemen."""
    Flexibility: NamedNode
    """Physical activity that is engaged in to improve joint and muscle flexibility."""
    Flight: NamedNode
    """An airline flight."""
    FlightReservation: NamedNode
    """A reservation for air travel.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    Float: NamedNode
    """Data type: Floating number."""
    FloorPlan: NamedNode
    """A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]. """
    Florist: NamedNode
    """A florist."""
    FollowAction: NamedNode
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.\n\nRelated actions:\n\n* [[BefriendAction]]: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.\n* [[SubscribeAction]]: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.\n* [[RegisterAction]]: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.\n* [[JoinAction]]: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.\n* [[TrackAction]]: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don't follow it)."""
    FoodEstablishment: NamedNode
    """A food-related business."""
    FoodEstablishmentReservation: NamedNode
    """A reservation to dine at a food-related business.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations."""
    FoodEvent: NamedNode
    """Event type: Food event."""
    FoodService: NamedNode
    """A food service, like breakfast, lunch, or dinner."""
    FourWheelDriveConfiguration: NamedNode
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability."""
    FreeReturn: NamedNode
    """Specifies that product returns are free of charge for the customer."""
    Friday: NamedNode
    """The day of the week between Thursday and Saturday."""
    FrontWheelDriveConfiguration: NamedNode
    """Front-wheel drive is a transmission layout where the engine drives the front wheels."""
    FullGameAvailability: NamedNode
    """Indicates full game availability."""
    FullRefund: NamedNode
    """Specifies that a refund can be done in the full amount the customer paid for the product."""
    FundingAgency: NamedNode
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages
    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).
    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.
    
Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...
    """
    FundingScheme: NamedNode
    """A FundingScheme combines organizational, project and policy aspects of grant-based funding
    that sets guidelines, principles and mechanisms to support other kinds of projects and activities.
    Funding is typically organized via [[Grant]] funding. Examples of funding schemes: Swiss Priority Programmes (SPPs); EU Framework 7 (FP7); Horizon 2020; the NIH-R01 Grant Program; Wellcome institutional strategic support fund. For large scale public sector funding, the management and administration of grant awards is often handled by other, dedicated, organizations - [[FundingAgency]]s such as ERC, REA, ..."""
    Fungus: NamedNode
    """Pathogenic fungus."""
    FurnitureStore: NamedNode
    """A furniture store."""
    Game: NamedNode
    """The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting."""
    GameAvailabilityEnumeration: NamedNode
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. """
    GamePlayMode: NamedNode
    """Indicates whether this game is multi-player, co-op or single-player."""
    GameServer: NamedNode
    """Server that provides game interaction in a multiplayer game."""
    GameServerStatus: NamedNode
    """Status of a game server."""
    GardenStore: NamedNode
    """A garden store."""
    GasStation: NamedNode
    """A gas station."""
    Gastroenterologic: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system."""
    GatedResidenceCommunity: NamedNode
    """Residence type: Gated community."""
    GenderType: NamedNode
    """An enumeration of genders."""
    Gene: NamedNode
    """A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype)."""
    GeneralContractor: NamedNode
    """A general contractor."""
    GenericWebPlatform: NamedNode
    """Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and [[DesktopWebPlatform]], as an incomplete list. """
    Genetic: NamedNode
    """A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders."""
    Genitourinary: NamedNode
    """Genitourinary system function assessment with clinical examination."""
    GeoCircle: NamedNode
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape
          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.
          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.
       """
    GeoCoordinates: NamedNode
    """The geographic coordinates of a place or event."""
    GeoShape: NamedNode
    """The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points."""
    GeospatialGeometry: NamedNode
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices."""
    Geriatric: NamedNode
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged."""
    GettingAccessHealthAspect: NamedNode
    """Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines)."""
    GiveAction: NamedNode
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.\n\nRelated actions:\n\n* [[TakeAction]]: Reciprocal of GiveAction.\n* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you)."""
    GlutenFreeDiet: NamedNode
    """A diet exclusive of gluten."""
    GolfCourse: NamedNode
    """A golf course."""
    GovernmentBenefitsType: NamedNode
    """GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered."""
    GovernmentBuilding: NamedNode
    """A government building."""
    GovernmentOffice: NamedNode
    """A government office&#x2014;for example, an IRS or DMV office."""
    GovernmentOrganization: NamedNode
    """A governmental organization or agency."""
    GovernmentPermit: NamedNode
    """A permit issued by a government agency."""
    GovernmentService: NamedNode
    """A service provided by a government organization, e.g. food stamps, veterans benefits, etc."""
    Grant: NamedNode
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],
    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).

Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.

The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].
    """
    GraphicNovel: NamedNode
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances."""
    GroceryStore: NamedNode
    """A grocery store."""
    GroupBoardingPolicy: NamedNode
    """The airline boards by groups based on check-in time, priority, etc."""
    Guide: NamedNode
    """[[Guide]] is a page or article that recommends specific products or services, or aspects of a thing for a user to consider. A [[Guide]] may represent a Buying Guide and detail aspects of products or services for a user to consider. A [[Guide]] may represent a Product Guide and recommend specific products or services. A [[Guide]] may represent a Ranked List and recommend specific products or services with ranking."""
    Gynecologic: NamedNode
    """A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system."""
    HVACBusiness: NamedNode
    """A business that provides Heating, Ventilation and Air Conditioning services."""
    Hackathon: NamedNode
    """A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event."""
    HairSalon: NamedNode
    """A hair salon."""
    HalalDiet: NamedNode
    """A diet conforming to Islamic dietary practices."""
    Hardcover: NamedNode
    """Book format: Hardcover."""
    HardwareStore: NamedNode
    """A hardware store."""
    Head: NamedNode
    """Head assessment with clinical examination."""
    HealthAndBeautyBusiness: NamedNode
    """Health and beauty."""
    HealthAspectEnumeration: NamedNode
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]]."""
    HealthCare: NamedNode
    """HealthCare: this is a benefit for health care."""
    HealthClub: NamedNode
    """A health club."""
    HealthInsurancePlan: NamedNode
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs."""
    HealthPlanCostSharingSpecification: NamedNode
    """A description of costs to the patient under a given network or formulary."""
    HealthPlanFormulary: NamedNode
    """For a given health insurance plan, the specification for costs and coverage of prescription drugs."""
    HealthPlanNetwork: NamedNode
    """A US-style health insurance plan network."""
    HealthTopicContent: NamedNode
    """[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.
  """
    HealthcareConsideration: NamedNode
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device."""
    HearingImpairedSupported: NamedNode
    """Uses devices to support users with hearing impairments."""
    Hematologic: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs."""
    HighSchool: NamedNode
    """A high school."""
    HinduDiet: NamedNode
    """A diet conforming to Hindu dietary practices, in particular, beef-free."""
    HinduTemple: NamedNode
    """A Hindu temple."""
    HobbyShop: NamedNode
    """A store that sells materials useful or necessary for various hobbies."""
    HomeAndConstructionBusiness: NamedNode
    """A construction business.\n\nA HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\n\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]'(s)."""
    HomeGoodsStore: NamedNode
    """A home goods store."""
    Homeopathic: NamedNode
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people."""
    Hospital: NamedNode
    """A hospital."""
    Hostel: NamedNode
    """A hostel - cheap accommodation, often in shared dormitories.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    Hotel: NamedNode
    """A hotel is an establishment that provides lodging paid on a short-term basis (source: Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    HotelRoom: NamedNode
    """A hotel room is a single room in a hotel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    House: NamedNode
    """A house is a building or structure that has the ability to be occupied for habitation by humans or other creatures (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/House">http://en.wikipedia.org/wiki/House</a>)."""
    HousePainter: NamedNode
    """A house painting service."""
    HowItWorksHealthAspect: NamedNode
    """Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science."""
    HowOrWhereHealthAspect: NamedNode
    """Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed."""
    HowTo: NamedNode
    """Instructions that explain how to achieve a result by performing a sequence of steps."""
    HowToDirection: NamedNode
    """A direction indicating a single action to do in the instructions for how to achieve a result."""
    HowToItem: NamedNode
    """An item used as either a tool or supply when performing the instructions for how to achieve a result."""
    HowToSection: NamedNode
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe)."""
    HowToStep: NamedNode
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items."""
    HowToSupply: NamedNode
    """A supply consumed when performing the instructions for how to achieve a result."""
    HowToTip: NamedNode
    """An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author's preference, etc. It can explain what could be done, or what should not be done, but doesn't specify what should be done (see HowToDirection)."""
    HowToTool: NamedNode
    """A tool used (but not consumed) when performing instructions for how to achieve a result."""
    HyperToc: NamedNode
    """A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items."""
    HyperTocEntry: NamedNode
    """A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. The media object itself is indicated using [[associatedMedia]]. Each section of interest within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]] and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]] is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]]."""
    IOSPlatform: NamedNode
    """Represents the broad notion of iOS-based operating systems."""
    IPTCDigitalSourceEnumeration: NamedNode
    """<a href="https://www.iptc.org/">IPTC</a> "Digital Source" codes for use with the [[digitalSourceType]] property, providing information about the source for a digital media object. 
In general these codes are not declared here to be mutually exclusive, although some combinations would be contradictory if applied simultaneously, or might be considered mutually incompatible by upstream maintainers of the definitions. See the IPTC <a href="https://www.iptc.org/std/photometadata/documentation/userguide/">documentation</a> 
 for <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">detailed definitions</a> of all terms."""
    IceCreamShop: NamedNode
    """An ice cream shop."""
    IgnoreAction: NamedNode
    """The act of intentionally disregarding the object. An agent ignores an object."""
    ImageGallery: NamedNode
    """Web page type: Image gallery page."""
    ImageObject: NamedNode
    """An image file."""
    ImageObjectSnapshot: NamedNode
    """A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity."""
    ImagingTest: NamedNode
    """Any medical imaging modality typically used for diagnostic purposes."""
    InForce: NamedNode
    """Indicates that a legislation is in force."""
    InStock: NamedNode
    """Indicates that the item is in stock."""
    InStoreOnly: NamedNode
    """Indicates that the item is available only at physical locations."""
    InStorePrepay: NamedNode
    """Payment in advance in some form of shop or kiosk for goods purchased online."""
    IndividualPhysician: NamedNode
    """An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals use [[hospitalAffiliation]]. 
The [[practicesAt]] property can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc. where this physician practices."""
    IndividualProduct: NamedNode
    """A single, identifiable product instance (e.g. a laptop with a particular serial number)."""
    Infectious: NamedNode
    """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections."""
    InfectiousAgentClass: NamedNode
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type."""
    InfectiousDisease: NamedNode
    """An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease."""
    InformAction: NamedNode
    """The act of notifying someone of information pertinent to them, with no expectation of a response."""
    IngredientsHealthAspect: NamedNode
    """Content discussing ingredients-related aspects of a health topic."""
    InsertAction: NamedNode
    """The act of adding at a specific location in an ordered collection."""
    InstallAction: NamedNode
    """The act of installing an application."""
    Installment: NamedNode
    """Represents the installment pricing component of the total price for an offered product."""
    InsuranceAgency: NamedNode
    """An Insurance agency."""
    Intangible: NamedNode
    """A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc."""
    Integer: NamedNode
    """Data type: Integer."""
    InteractAction: NamedNode
    """The act of interacting with another person or organization."""
    InteractionCounter: NamedNode
    """A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction."""
    InternationalTrial: NamedNode
    """An international trial."""
    InternetCafe: NamedNode
    """An internet cafe."""
    InvestmentFund: NamedNode
    """A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets."""
    InvestmentOrDeposit: NamedNode
    """A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return."""
    InviteAction: NamedNode
    """The act of asking someone to attend an event. Reciprocal of RsvpAction."""
    Invoice: NamedNode
    """A statement of the money due for goods or services; a bill."""
    InvoicePrice: NamedNode
    """Represents the invoice price of an offered product."""
    ItemAvailability: NamedNode
    """A list of possible product availability options."""
    ItemList: NamedNode
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting."""
    ItemListOrderAscending: NamedNode
    """An ItemList ordered with lower values listed first."""
    ItemListOrderDescending: NamedNode
    """An ItemList ordered with higher values listed first."""
    ItemListOrderType: NamedNode
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized."""
    ItemListUnordered: NamedNode
    """An ItemList ordered with no explicit order."""
    ItemPage: NamedNode
    """A page devoted to a single item, such as a particular product or hotel."""
    JewelryStore: NamedNode
    """A jewelry store."""
    JobPosting: NamedNode
    """A listing that describes a job opening in a certain organization."""
    JoinAction: NamedNode
    """An agent joins an event/group with participants/friends at a location.\n\nRelated actions:\n\n* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.\n* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.\n* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates."""
    Joint: NamedNode
    """The anatomical location at which two or more bones make contact."""
    KeepProduct: NamedNode
    """Specifies that the consumer can keep the product, even when receiving a refund or store credit."""
    KosherDiet: NamedNode
    """A diet conforming to Jewish dietary practices."""
    LaboratoryScience: NamedNode
    """A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research."""
    LakeBodyOfWater: NamedNode
    """A lake (for example, Lake Pontrachain)."""
    Landform: NamedNode
    """A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins."""
    LandmarksOrHistoricalBuildings: NamedNode
    """An historical landmark or building."""
    Language: NamedNode
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) can be used via the [[alternateName]] property. The Language type previously also covered programming languages such as Scheme and Lisp, which are now best represented using [[ComputerLanguage]]."""
    LaserDiscFormat: NamedNode
    """LaserDiscFormat."""
    LearningResource: NamedNode
    """The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

[[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

[[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one."""
    LeaveAction: NamedNode
    """An agent leaves an event / group with participants/friends at a location.\n\nRelated actions:\n\n* [[JoinAction]]: The antonym of LeaveAction.\n* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service."""
    LeftHandDriving: NamedNode
    """The steering position is on the left side of the vehicle (viewed from the main direction of driving)."""
    LegalForceStatus: NamedNode
    """A list of possible statuses for the legal force of a legislation."""
    LegalService: NamedNode
    """A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.\n\nAs a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]'(s)."""
    LegalValueLevel: NamedNode
    """A list of possible levels for the legal validity of a legislation."""
    Legislation: NamedNode
    """A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article)."""
    LegislationObject: NamedNode
    """A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version."""
    LegislativeBuilding: NamedNode
    """A legislative building&#x2014;for example, the state capitol."""
    LeisureTimeActivity: NamedNode
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc."""
    LendAction: NamedNode
    """The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.\n\nRelated actions:\n\n* [[BorrowAction]]: Reciprocal of LendAction."""
    Library: NamedNode
    """A library."""
    LibrarySystem: NamedNode
    """A [[LibrarySystem]] is a collaborative system amongst several libraries."""
    LifestyleModification: NamedNode
    """A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition."""
    Ligament: NamedNode
    """A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints."""
    LikeAction: NamedNode
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants."""
    LimitedAvailability: NamedNode
    """Indicates that the item has limited availability."""
    LimitedByGuaranteeCharity: NamedNode
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK)."""
    LinkRole: NamedNode
    """A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds."""
    LiquorStore: NamedNode
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits."""
    ListItem: NamedNode
    """An list item, e.g. a step in a checklist or how-to description."""
    ListPrice: NamedNode
    """Represents the list price of an offered product."""
    ListenAction: NamedNode
    """The act of consuming audio content."""
    LiteraryEvent: NamedNode
    """Event type: Literary event."""
    LiveAlbum: NamedNode
    """LiveAlbum."""
    LiveBlogPosting: NamedNode
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage of an ongoing event through continuous updates."""
    LivingWithHealthAspect: NamedNode
    """Information about coping or life related to the topic."""
    LoanOrCredit: NamedNode
    """A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges."""
    LocalBusiness: NamedNode
    """A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc."""
    LocationFeatureSpecification: NamedNode
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality."""
    LockerDelivery: NamedNode
    """A DeliveryMethod in which an item is made available via locker."""
    Locksmith: NamedNode
    """A locksmith."""
    LodgingBusiness: NamedNode
    """A lodging business, such as a motel, hotel, or inn."""
    LodgingReservation: NamedNode
    """A reservation for lodging at a hotel, motel, inn, etc.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations."""
    Longitudinal: NamedNode
    """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases."""
    LoseAction: NamedNode
    """The act of being defeated in a competitive activity."""
    LowCalorieDiet: NamedNode
    """A diet focused on reduced calorie intake."""
    LowFatDiet: NamedNode
    """A diet focused on reduced fat and cholesterol intake."""
    LowLactoseDiet: NamedNode
    """A diet appropriate for people with lactose intolerance."""
    LowSaltDiet: NamedNode
    """A diet focused on reduced sodium intake."""
    Lung: NamedNode
    """Lung and respiratory system clinical examination."""
    LymphaticVessel: NamedNode
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart."""
    MRI: NamedNode
    """Magnetic resonance imaging."""
    MSRP: NamedNode
    """Represents the manufacturer suggested retail price ("MSRP") of an offered product."""
    MadeToOrder: NamedNode
    """Indicates that the item is made to order (custom made)."""
    Male: NamedNode
    """The male gender."""
    Manuscript: NamedNode
    """A book, document, or piece of music written by hand rather than typed or printed."""
    Map: NamedNode
    """A map."""
    MapCategoryType: NamedNode
    """An enumeration of several kinds of Map."""
    MarryAction: NamedNode
    """The act of marrying a person."""
    Mass: NamedNode
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'."""
    MathSolver: NamedNode
    """A math solver which is capable of solving a subset of mathematical problems."""
    MaximumDoseSchedule: NamedNode
    """The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity."""
    MayTreatHealthAspect: NamedNode
    """Related topics may be treated by a Topic."""
    MeasurementMethodEnum: NamedNode
    """Enumeration(s) for use with [[measurementMethod]]."""
    MeasurementTypeEnumeration: NamedNode
    """Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles."""
    MediaEnumeration: NamedNode
    """MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination."""
    MediaGallery: NamedNode
    """Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia."""
    MediaManipulationRatingEnumeration: NamedNode
    """ Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity of a media object (in the context of how it was published or shared). In general these codes are not mutually exclusive, although some combinations (such as 'original' versus 'transformed', 'edited' and 'staged') would be contradictory if applied in the same [[MediaReview]]. Note that the application of these codes is with regard to a piece of media shared or published in a particular context."""
    MediaObject: NamedNode
    """A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's)."""
    MediaReview: NamedNode
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.
    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is
    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working
    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized."""
    MediaReviewItem: NamedNode
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party."""
    MediaSubscription: NamedNode
    """A subscription which allows a user to access media including audio, video, books, etc."""
    MedicalAudience: NamedNode
    """Target audiences for medical web pages."""
    MedicalAudienceType: NamedNode
    """Target audiences types for medical web pages. Enumerated type."""
    MedicalBusiness: NamedNode
    """A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals."""
    MedicalCause: NamedNode
    """The causative agent(s) that are responsible for the pathophysiologic process that eventually results in a medical condition, symptom or sign. In this schema, unless otherwise specified this is meant to be the proximate cause of the medical condition, symptom or sign. The proximate cause is defined as the causative agent that most directly results in the medical condition, symptom or sign. For example, the HIV virus could be considered a cause of AIDS. Or in a diagnostic context, if a patient fell and sustained a hip fracture and two days later sustained a pulmonary embolism which eventuated in a cardiac arrest, the cause of the cardiac arrest (the proximate cause) would be the pulmonary embolism and not the fall. Medical causes can include cardiovascular, chemical, dermatologic, endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic, iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric, oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal, rheumatologic, toxic, traumatic, or urologic causes; medical conditions can be causes as well."""
    MedicalClinic: NamedNode
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well."""
    MedicalCode: NamedNode
    """A code for a medical entity."""
    MedicalCondition: NamedNode
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc."""
    MedicalConditionStage: NamedNode
    """A stage of a medical condition, such as 'Stage IIIa'."""
    MedicalContraindication: NamedNode
    """A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but these risks may be outweighed by other considerations or mitigated by other measures)."""
    MedicalDevice: NamedNode
    """Any object used in a medical capacity, such as to diagnose or treat a patient."""
    MedicalDevicePurpose: NamedNode
    """Categories of medical devices, organized by the purpose or intended use of the device."""
    MedicalEntity: NamedNode
    """The most generic type of entity related to health and the practice of medicine."""
    MedicalEnumeration: NamedNode
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice."""
    MedicalEvidenceLevel: NamedNode
    """Level of evidence for a medical guideline. Enumerated type."""
    MedicalGuideline: NamedNode
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity."""
    MedicalGuidelineContraindication: NamedNode
    """A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound."""
    MedicalGuidelineRecommendation: NamedNode
    """A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound."""
    MedicalImagingTechnique: NamedNode
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type."""
    MedicalIndication: NamedNode
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc."""
    MedicalIntangible: NamedNode
    """A utility class that serves as the umbrella for a number of 'intangible' things in the medical space."""
    MedicalObservationalStudy: NamedNode
    """An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment."""
    MedicalObservationalStudyDesign: NamedNode
    """Design models for observational medical studies. Enumerated type."""
    MedicalOrganization: NamedNode
    """A medical organization (physical or not), such as hospital, institution or clinic."""
    MedicalProcedure: NamedNode
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques."""
    MedicalProcedureType: NamedNode
    """An enumeration that describes different types of medical procedures."""
    MedicalResearcher: NamedNode
    """Medical researchers."""
    MedicalRiskCalculator: NamedNode
    """A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators."""
    MedicalRiskEstimator: NamedNode
    """Any rule set or interactive tool for estimating the risk of developing a complication or condition."""
    MedicalRiskFactor: NamedNode
    """A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication."""
    MedicalRiskScore: NamedNode
    """A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score."""
    MedicalScholarlyArticle: NamedNode
    """A scholarly article in the medical domain."""
    MedicalSign: NamedNode
    """Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination."""
    MedicalSignOrSymptom: NamedNode
    """Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective."""
    MedicalSpecialty: NamedNode
    """Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type."""
    MedicalStudy: NamedNode
    """A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID."""
    MedicalStudyStatus: NamedNode
    """The status of a medical study. Enumerated type."""
    MedicalSymptom: NamedNode
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue."""
    MedicalTest: NamedNode
    """Any medical test, typically performed for diagnostic purposes."""
    MedicalTestPanel: NamedNode
    """Any collection of tests commonly ordered together."""
    MedicalTherapy: NamedNode
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition."""
    MedicalTrial: NamedNode
    """A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups."""
    MedicalTrialDesign: NamedNode
    """Design models for medical trials. Enumerated type."""
    MedicalWebPage: NamedNode
    """A web page that provides medical information."""
    MedicineSystem: NamedNode
    """Systems of medical practice."""
    MeetingRoom: NamedNode
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Conference_hall">http://en.wikipedia.org/wiki/Conference_hall</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    MemberProgram: NamedNode
    """A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs may have multiple tiers, for example silver and gold members, each with different benefits."""
    MemberProgramTier: NamedNode
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold"."""
    MensClothingStore: NamedNode
    """A men's clothing store."""
    Menu: NamedNode
    """A structured representation of food or drink items available from a FoodEstablishment."""
    MenuItem: NamedNode
    """A food or drink item listed in a menu or menu section."""
    MenuSection: NamedNode
    """A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast', etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other classification made by the menu provider."""
    MerchantReturnEnumeration: NamedNode
    """Enumerates several kinds of product return policies."""
    MerchantReturnFiniteReturnWindow: NamedNode
    """Specifies that there is a finite window for product returns."""
    MerchantReturnNotPermitted: NamedNode
    """Specifies that product returns are not permitted."""
    MerchantReturnPolicy: NamedNode
    """A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]]."""
    MerchantReturnPolicySeasonalOverride: NamedNode
    """A seasonal override of a return policy, for example used for holidays."""
    MerchantReturnUnlimitedWindow: NamedNode
    """Specifies that there is an unlimited window for product returns."""
    MerchantReturnUnspecified: NamedNode
    """Specifies that a product return policy is not provided."""
    Message: NamedNode
    """A single message from a sender to one or more organizations or people."""
    MiddleSchool: NamedNode
    """A middle school (typically for children aged around 11-14, although this varies somewhat)."""
    Midwifery: NamedNode
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives."""
    MinimumAdvertisedPrice: NamedNode
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product."""
    MinorHumanEditsDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/minorHumanEdits">minor human edits</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    MisconceptionsHealthAspect: NamedNode
    """Content about common misconceptions and myths that are related to a topic."""
    MixedEventAttendanceMode: NamedNode
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes."""
    MixtapeAlbum: NamedNode
    """MixtapeAlbum."""
    MobileApplication: NamedNode
    """A software application designed specifically to work well on a mobile device such as a telephone."""
    MobilePhoneStore: NamedNode
    """A store that sells mobile phones and related accessories."""
    MobileWebPlatform: NamedNode
    """Represents the broad notion of 'mobile' browsers as a Web Platform."""
    MolecularEntity: NamedNode
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity."""
    Monday: NamedNode
    """The day of the week between Sunday and Tuesday."""
    MonetaryAmount: NamedNode
    """A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc."""
    MonetaryAmountDistribution: NamedNode
    """A statistical distribution of monetary amounts."""
    MonetaryGrant: NamedNode
    """A monetary grant."""
    MoneyTransfer: NamedNode
    """The act of transferring money from one place to another place. This may occur electronically or physically."""
    MortgageLoan: NamedNode
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)"""
    Mosque: NamedNode
    """A mosque."""
    Motel: NamedNode
    """A motel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    Motorcycle: NamedNode
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle."""
    MotorcycleDealer: NamedNode
    """A motorcycle dealer."""
    MotorcycleRepair: NamedNode
    """A motorcycle repair shop."""
    MotorizedBicycle: NamedNode
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling."""
    Mountain: NamedNode
    """A mountain, like Mount Whitney or Mount Everest."""
    MoveAction: NamedNode
    """The act of an agent relocating to a place.\n\nRelated actions:\n\n* [[TransferAction]]: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object."""
    Movie: NamedNode
    """A movie."""
    MovieClip: NamedNode
    """A short segment/part of a movie."""
    MovieRentalStore: NamedNode
    """A movie rental store."""
    MovieSeries: NamedNode
    """A series of movies. Included movies can be indicated with the hasPart property."""
    MovieTheater: NamedNode
    """A movie theater."""
    MovingCompany: NamedNode
    """A moving company."""
    MultiCenterTrial: NamedNode
    """A trial that takes place at multiple centers."""
    MultiPlayer: NamedNode
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously."""
    MulticellularParasite: NamedNode
    """Multicellular parasite that causes an infection."""
    Muscle: NamedNode
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement."""
    Musculoskeletal: NamedNode
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of muscles, ligaments and skeletal system."""
    MusculoskeletalExam: NamedNode
    """Musculoskeletal system clinical examination."""
    Museum: NamedNode
    """A museum."""
    MusicAlbum: NamedNode
    """A collection of music tracks."""
    MusicAlbumProductionType: NamedNode
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc."""
    MusicAlbumReleaseType: NamedNode
    """The kind of release which this album is: single, EP or album."""
    MusicComposition: NamedNode
    """A musical composition."""
    MusicEvent: NamedNode
    """Event type: Music event."""
    MusicGroup: NamedNode
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician."""
    MusicPlaylist: NamedNode
    """A collection of music tracks in playlist form."""
    MusicRecording: NamedNode
    """A music recording (track), usually a single song."""
    MusicRelease: NamedNode
    """A MusicRelease is a specific release of a music album."""
    MusicReleaseFormatType: NamedNode
    """Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.)."""
    MusicStore: NamedNode
    """A music store."""
    MusicVenue: NamedNode
    """A music venue."""
    MusicVideoObject: NamedNode
    """A music video file."""
    NGO: NamedNode
    """Organization: Non-governmental Organization."""
    NLNonprofitType: NamedNode
    """NLNonprofitType: Non-profit organization type originating from the Netherlands."""
    NailSalon: NamedNode
    """A nail salon."""
    NarcoticConsideration: NamedNode
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin."""
    Neck: NamedNode
    """Neck assessment with clinical examination."""
    NegativeFilmDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/negativeFilm">negative film</a></a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    Nerve: NamedNode
    """A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons."""
    Neuro: NamedNode
    """Neurological system clinical examination."""
    Neurologic: NamedNode
    """A specific branch of medical science that studies the nerves and nervous system and its respective disease states."""
    NewCondition: NamedNode
    """Indicates that the item is new."""
    NewsArticle: NamedNode
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

A more detailed overview of [schema.org News markup](/docs/news.html) is also available.
"""
    NewsMediaOrganization: NamedNode
    """A News/Media organization such as a newspaper or TV station."""
    Newspaper: NamedNode
    """A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily."""
    NightClub: NamedNode
    """A nightclub or discotheque."""
    NoninvasiveProcedure: NamedNode
    """A type of medical procedure that involves noninvasive techniques."""
    Nonprofit501a: NamedNode
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations."""
    Nonprofit501c1: NamedNode
    """Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations."""
    Nonprofit501c10: NamedNode
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations."""
    Nonprofit501c11: NamedNode
    """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations."""
    Nonprofit501c12: NamedNode
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies."""
    Nonprofit501c13: NamedNode
    """Nonprofit501c13: Non-profit type referring to Cemetery Companies."""
    Nonprofit501c14: NamedNode
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds."""
    Nonprofit501c15: NamedNode
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations."""
    Nonprofit501c16: NamedNode
    """Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance Crop Operations."""
    Nonprofit501c17: NamedNode
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts."""
    Nonprofit501c18: NamedNode
    """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959)."""
    Nonprofit501c19: NamedNode
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present Members of the Armed Forces."""
    Nonprofit501c2: NamedNode
    """Nonprofit501c2: Non-profit type referring to Title-holding Corporations for Exempt Organizations."""
    Nonprofit501c20: NamedNode
    """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations."""
    Nonprofit501c21: NamedNode
    """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts."""
    Nonprofit501c22: NamedNode
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds."""
    Nonprofit501c23: NamedNode
    """Nonprofit501c23: Non-profit type referring to Veterans Organizations."""
    Nonprofit501c24: NamedNode
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts."""
    Nonprofit501c25: NamedNode
    """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations or Trusts with Multiple Parents."""
    Nonprofit501c26: NamedNode
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing Health Coverage for High-Risk Individuals."""
    Nonprofit501c27: NamedNode
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation Reinsurance Organizations."""
    Nonprofit501c28: NamedNode
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts."""
    Nonprofit501c3: NamedNode
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, Fostering National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations."""
    Nonprofit501c4: NamedNode
    """Nonprofit501c4: Non-profit type referring to Civic Leagues, Social Welfare Organizations, and Local Associations of Employees."""
    Nonprofit501c5: NamedNode
    """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations."""
    Nonprofit501c6: NamedNode
    """Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce, Real Estate Boards."""
    Nonprofit501c7: NamedNode
    """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs."""
    Nonprofit501c8: NamedNode
    """Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and Associations."""
    Nonprofit501c9: NamedNode
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations."""
    Nonprofit501d: NamedNode
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations."""
    Nonprofit501e: NamedNode
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations."""
    Nonprofit501f: NamedNode
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations."""
    Nonprofit501k: NamedNode
    """Nonprofit501k: Non-profit type referring to Child Care Organizations."""
    Nonprofit501n: NamedNode
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools."""
    Nonprofit501q: NamedNode
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations."""
    Nonprofit527: NamedNode
    """Nonprofit527: Non-profit type referring to political organizations."""
    NonprofitANBI: NamedNode
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL)."""
    NonprofitSBBI: NamedNode
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL)."""
    NonprofitType: NamedNode
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be."""
    Nose: NamedNode
    """Nose function assessment with clinical examination."""
    NotInForce: NamedNode
    """Indicates that a legislation is currently not in force."""
    NotYetRecruiting: NamedNode
    """Not yet recruiting."""
    Notary: NamedNode
    """A notary."""
    NoteDigitalDocument: NamedNode
    """A file containing a note, primarily for the author."""
    Number: NamedNode
    """Data type: Number.\n\nUsage guidelines:\n\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    Nursing: NamedNode
    """A health profession of a person formally educated and trained in the care of the sick or infirm person."""
    NutritionInformation: NamedNode
    """Nutritional information about the recipe."""
    OTC: NamedNode
    """The character of a medical substance, typically a medicine, of being available over the counter or not."""
    Observation: NamedNode
    """Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].
    """
    Observational: NamedNode
    """An observational study design."""
    Obstetric: NamedNode
    """A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child."""
    Occupation: NamedNode
    """A profession, may involve prolonged training and/or a formal qualification."""
    OccupationalActivity: NamedNode
    """Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc."""
    OccupationalExperienceRequirements: NamedNode
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]]."""
    OccupationalTherapy: NamedNode
    """A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems."""
    OceanBodyOfWater: NamedNode
    """An ocean (for example, the Pacific)."""
    Offer: NamedNode
    """An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.\n\nNote: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.\n\nFor [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/)."""
    OfferCatalog: NamedNode
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider."""
    OfferForLease: NamedNode
    """An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose
  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  """
    OfferForPurchase: NamedNode
    """An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something, i.e. an [[Offer]] whose
  [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for
  background on the underlying concepts.
  """
    OfferItemCondition: NamedNode
    """A list of possible conditions for the item."""
    OfferShippingDetails: NamedNode
    """OfferShippingDetails represents information about shipping destinations.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

E.g. Cheaper and slower: $5 in 5-7 days
or Fast and expensive: $15 in 1-2 days."""
    OfficeEquipmentStore: NamedNode
    """An office equipment store."""
    OfficialLegalValue: NamedNode
    """All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of an EU directive published by the EU Office of Publications)."""
    OfflineEventAttendanceMode: NamedNode
    """OfflineEventAttendanceMode - an event that is primarily conducted offline. """
    OfflinePermanently: NamedNode
    """Game server status: OfflinePermanently. Server is offline and not available."""
    OfflineTemporarily: NamedNode
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon."""
    OnDemandEvent: NamedNode
    """A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand."""
    OnSitePickup: NamedNode
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office."""
    Oncologic: NamedNode
    """A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention."""
    OneTimePayments: NamedNode
    """OneTimePayments: this is a benefit for one-time payments for individuals."""
    Online: NamedNode
    """Game server status: Online. Server is available."""
    OnlineBusiness: NamedNode
    """A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc."""
    OnlineEventAttendanceMode: NamedNode
    """OnlineEventAttendanceMode - an event that is primarily conducted online. """
    OnlineFull: NamedNode
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached."""
    OnlineOnly: NamedNode
    """Indicates that the item is available only online."""
    OnlineStore: NamedNode
    """An eCommerce site."""
    OpenTrial: NamedNode
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient."""
    OpeningHoursSpecification: NamedNode
    """A structured value providing information about the opening hours of a place or a certain service inside a place.\n\n
The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.\n\nIf the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.
      """
    OpinionNewsArticle: NamedNode
    """An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions rather than journalistic reporting of news and events. For example, a [[NewsArticle]] consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of a news publication. """
    Optician: NamedNode
    """A store that sells reading glasses and similar devices for improving vision."""
    Optometric: NamedNode
    """The science or practice of testing visual acuity and prescribing corrective lenses."""
    Order: NamedNode
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer."""
    OrderAction: NamedNode
    """An agent orders an object/product/service to be delivered/sent."""
    OrderCancelled: NamedNode
    """OrderStatus representing cancellation of an order."""
    OrderDelivered: NamedNode
    """OrderStatus representing successful delivery of an order."""
    OrderInTransit: NamedNode
    """OrderStatus representing that an order is in transit."""
    OrderItem: NamedNode
    """An order item is a line of an order. It includes the quantity and shipping details of a bought offer."""
    OrderPaymentDue: NamedNode
    """OrderStatus representing that payment is due on an order."""
    OrderPickupAvailable: NamedNode
    """OrderStatus representing availability of an order for pickup."""
    OrderProblem: NamedNode
    """OrderStatus representing that there is a problem with the order."""
    OrderProcessing: NamedNode
    """OrderStatus representing that an order is being processed."""
    OrderReturned: NamedNode
    """OrderStatus representing that an order has been returned."""
    OrderStatus: NamedNode
    """Enumerated status values for Order."""
    Organization: NamedNode
    """An organization such as a school, NGO, corporation, club, etc."""
    OrganizationRole: NamedNode
    """A subclass of Role used to describe roles within organizations."""
    OrganizeAction: NamedNode
    """The act of manipulating/administering/supervising/controlling one or more objects."""
    OriginalMediaContent: NamedNode
    """Content coded 'as original media content' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'original': No evidence the footage has been misleadingly altered or manipulated, though it may contain false or misleading claims.

For an [[ImageObject]] to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.

For an [[ImageObject]] with embedded text to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.

For an [[AudioObject]] to be 'original': No evidence the audio has been misleadingly altered or manipulated, though it may contain false or misleading claims.
"""
    OriginalShippingFees: NamedNode
    """Specifies that the customer must pay the original shipping costs when returning a product."""
    Osteopathic: NamedNode
    """A system of medicine focused on promoting the body's innate ability to heal itself."""
    Otolaryngologic: NamedNode
    """A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states."""
    OutOfStock: NamedNode
    """Indicates that the item is out of stock."""
    OutletStore: NamedNode
    """An outlet store."""
    OverviewHealthAspect: NamedNode
    """Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction."""
    OwnershipInfo: NamedNode
    """A structured value providing information about when a certain organization or person owned a certain product."""
    PET: NamedNode
    """Positron emission tomography imaging."""
    PaidLeave: NamedNode
    """PaidLeave: this is a benefit for paid leave."""
    PaintAction: NamedNode
    """The act of producing a painting, typically with paint and canvas as instruments."""
    Painting: NamedNode
    """A painting."""
    PalliativeProcedure: NamedNode
    """A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition."""
    Paperback: NamedNode
    """Book format: Paperback."""
    ParcelDelivery: NamedNode
    """The delivery of a parcel either via the postal service or a commercial service."""
    ParcelService: NamedNode
    """A private parcel service as the delivery mode available for a certain offer.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#DHL\n* http://purl.org/goodrelations/v1#FederalExpress\n* http://purl.org/goodrelations/v1#UPS
      """
    ParentAudience: NamedNode
    """A set of characteristics describing parents, who can be interested in viewing some content."""
    ParentalSupport: NamedNode
    """ParentalSupport: this is a benefit for parental support."""
    Park: NamedNode
    """A park."""
    ParkingFacility: NamedNode
    """A parking lot or other parking facility."""
    ParkingMap: NamedNode
    """A parking map."""
    PartiallyInForce: NamedNode
    """Indicates that parts of the legislation are in force, and parts are not."""
    Pathology: NamedNode
    """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness."""
    PathologyTest: NamedNode
    """A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist."""
    Patient: NamedNode
    """A patient is any person recipient of health care services."""
    PatientExperienceHealthAspect: NamedNode
    """Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material."""
    PawnShop: NamedNode
    """A shop that will buy, or lend money against the security of, personal possessions."""
    PayAction: NamedNode
    """An agent pays a price to a participant."""
    PaymentAutomaticallyApplied: NamedNode
    """An automatic payment system is in place and will be used."""
    PaymentCard: NamedNode
    """A payment method using a credit, debit, store or other card to associate the payment with an account."""
    PaymentChargeSpecification: NamedNode
    """The costs of settling the payment using a particular payment method."""
    PaymentComplete: NamedNode
    """The payment has been received and processed."""
    PaymentDeclined: NamedNode
    """The payee received the payment, but it was declined for some reason."""
    PaymentDue: NamedNode
    """The payment is due, but still within an acceptable time to be received."""
    PaymentMethod: NamedNode
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction. The following legacy values should be accepted:
    \n\n* http://purl.org/goodrelations/v1#ByBankTransferInAdvance\n* http://purl.org/goodrelations/v1#ByInvoice\n* http://purl.org/goodrelations/v1#Cash\n* http://purl.org/goodrelations/v1#CheckInAdvance\n* http://purl.org/goodrelations/v1#COD\n* http://purl.org/goodrelations/v1#DirectDebit\n* http://purl.org/goodrelations/v1#GoogleCheckout\n* http://purl.org/goodrelations/v1#PayPal\n* http://purl.org/goodrelations/v1#PaySwarm\n\nStructured values are recommended for newer payment methods."""
    PaymentMethodType: NamedNode
    """The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod."""
    PaymentPastDue: NamedNode
    """The payment is due and considered late."""
    PaymentService: NamedNode
    """A Service to transfer funds from a person or organization to a beneficiary person or organization."""
    PaymentStatusType: NamedNode
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc."""
    Pediatric: NamedNode
    """A specific branch of medical science that specializes in the care of infants, children and adolescents."""
    PeopleAudience: NamedNode
    """A set of characteristics belonging to people, e.g. who compose an item's target audience."""
    PercutaneousProcedure: NamedNode
    """A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery."""
    PerformAction: NamedNode
    """The act of participating in performance arts."""
    PerformanceRole: NamedNode
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc."""
    PerformingArtsTheater: NamedNode
    """A theater or other performing art center."""
    PerformingGroup: NamedNode
    """A performance group, such as a band, an orchestra, or a circus."""
    Periodical: NamedNode
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.\n\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html)."""
    Permit: NamedNode
    """A permit issued by an organization, e.g. a parking pass."""
    Person: NamedNode
    """A person (alive, dead, undead, or fictional)."""
    PetStore: NamedNode
    """A pet store."""
    Pharmacy: NamedNode
    """A pharmacy or drugstore."""
    PharmacySpecialty: NamedNode
    """The practice or art and science of preparing and dispensing drugs and medicines."""
    PhoneCarrierPayment: NamedNode
    """Payment by billing via the phone carrier."""
    Photograph: NamedNode
    """A photograph."""
    PhotographAction: NamedNode
    """The act of capturing still images of objects using a camera."""
    PhysicalActivity: NamedNode
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan."""
    PhysicalActivityCategory: NamedNode
    """Categories of physical activity, organized by physiologic classification."""
    PhysicalExam: NamedNode
    """A type of physical examination of a patient performed by a physician. """
    PhysicalTherapy: NamedNode
    """A process of progressive physical care and rehabilitation aimed at improving a health condition."""
    Physician: NamedNode
    """An individual physician or a physician's office considered as a [[MedicalOrganization]]."""
    PhysiciansOffice: NamedNode
    """A doctor's office or clinic."""
    Physiotherapy: NamedNode
    """The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery."""
    Place: NamedNode
    """Entities that have a somewhat fixed, physical extension."""
    PlaceOfWorship: NamedNode
    """Place of worship, such as a church, synagogue, or mosque."""
    PlaceboControlledTrial: NamedNode
    """A placebo-controlled trial design."""
    PlanAction: NamedNode
    """The act of planning the execution of an event/task/action/reservation/plan to a future date."""
    PlasticSurgery: NamedNode
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means."""
    Play: NamedNode
    """A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]]."""
    PlayAction: NamedNode
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation, competition or exercise.\n\nRelated actions:\n\n* [[ListenAction]]: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.\n* [[WatchAction]]: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content."""
    PlayGameAction: NamedNode
    """The act of playing a video game."""
    Playground: NamedNode
    """A playground."""
    Plumber: NamedNode
    """A plumbing service."""
    PodcastEpisode: NamedNode
    """A single episode of a podcast series."""
    PodcastSeason: NamedNode
    """A single season of a podcast. Many podcasts do not break down into separate seasons. In that case, PodcastSeries should be used."""
    PodcastSeries: NamedNode
    """A podcast is an episodic series of digital audio or video files which a user can download and listen to."""
    Podiatric: NamedNode
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders."""
    PoliceStation: NamedNode
    """A police station."""
    PoliticalParty: NamedNode
    """Organization: Political Party."""
    Pond: NamedNode
    """A pond."""
    PositiveFilmDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/positiveFilm">positive film</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    PostOffice: NamedNode
    """A post office."""
    PostalAddress: NamedNode
    """The mailing address."""
    PostalCodeRangeSpecification: NamedNode
    """Indicates a range of postal codes, usually defined as the set of valid codes between [[postalCodeBegin]] and [[postalCodeEnd]], inclusively."""
    Poster: NamedNode
    """A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something."""
    PotentialActionStatus: NamedNode
    """A description of an action that is supported."""
    PreOrder: NamedNode
    """Indicates that the item is available for pre-order."""
    PreOrderAction: NamedNode
    """An agent orders a (not yet released) object/product/service to be delivered/sent."""
    PreSale: NamedNode
    """Indicates that the item is available for ordering and delivery before general availability."""
    PregnancyHealthAspect: NamedNode
    """Content discussing pregnancy-related aspects of a health topic."""
    PrependAction: NamedNode
    """The act of inserting at the beginning if an ordered collection."""
    Preschool: NamedNode
    """A preschool."""
    PrescriptionOnly: NamedNode
    """Available by prescription only."""
    PresentationDigitalDocument: NamedNode
    """A file containing slides or used for a presentation."""
    PreventionHealthAspect: NamedNode
    """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic."""
    PreventionIndication: NamedNode
    """An indication for preventing an underlying condition, symptom, etc."""
    PriceComponentTypeEnumeration: NamedNode
    """Enumerates different price components that together make up the total price for an offered product."""
    PriceSpecification: NamedNode
    """A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc."""
    PriceTypeEnumeration: NamedNode
    """Enumerates different price types, for example list price, invoice price, and sale price."""
    PrimaryCare: NamedNode
    """The medical care by a physician, or other health-care professional, who is the patient's first contact with the health-care system and who may recommend a specialist if necessary."""
    PrintDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/print">print</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    Prion: NamedNode
    """A prion is an infectious agent composed of protein in a misfolded form."""
    Product: NamedNode
    """Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online."""
    ProductCollection: NamedNode
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together e.g. in an [[Offer]]."""
    ProductGroup: NamedNode
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.

While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]]. """
    ProductModel: NamedNode
    """A datasheet or vendor specification of a product (in the sense of a prototypical description)."""
    ProductReturnEnumeration: NamedNode
    """ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy."""
    ProductReturnFiniteReturnWindow: NamedNode
    """ProductReturnFiniteReturnWindow: there is a finite window for product returns."""
    ProductReturnNotPermitted: NamedNode
    """ProductReturnNotPermitted: product returns are not permitted."""
    ProductReturnPolicy: NamedNode
    """A ProductReturnPolicy provides information about product return policies associated with an [[Organization]] or [[Product]]."""
    ProductReturnUnlimitedWindow: NamedNode
    """ProductReturnUnlimitedWindow: there is an unlimited window for product returns."""
    ProductReturnUnspecified: NamedNode
    """ProductReturnUnspecified: a product return policy is not specified here."""
    ProfessionalService: NamedNode
    """Original definition: "provider of professional services."\n\nThe general [[ProfessionalService]] type for local businesses was deprecated due to confusion with [[Service]]. For reference, the types that it included were: [[Dentist]],
        [[AccountingService]], [[Attorney]], [[Notary]], as well as types for several kinds of [[HomeAndConstructionBusiness]]: [[Electrician]], [[GeneralContractor]],
        [[HousePainter]], [[Locksmith]], [[Plumber]], [[RoofingContractor]]. [[LegalService]] was introduced as a more inclusive supertype of [[Attorney]]."""
    ProfilePage: NamedNode
    """Web page type: Profile page."""
    PrognosisHealthAspect: NamedNode
    """Typical progression and happenings of life course of the topic."""
    ProgramMembership: NamedNode
    """Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc."""
    Project: NamedNode
    """An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   """
    PronounceableText: NamedNode
    """Data type: PronounceableText."""
    Property: NamedNode
    """A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property."""
    PropertyValue: NamedNode
    """A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.\n\n Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.
    """
    PropertyValueSpecification: NamedNode
    """A Property value specification."""
    Protein: NamedNode
    """Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type :Protein. A protein can thus be a subclass of another protein, e.g. :Protein as a UniProt record can have multiple isoforms inside it which would also be :Protein. They can be imagined, synthetic, hypothetical or naturally occurring."""
    Protozoa: NamedNode
    """Single-celled organism that causes an infection."""
    Psychiatric: NamedNode
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies."""
    PsychologicalTreatment: NamedNode
    """A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs."""
    PublicHealth: NamedNode
    """Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine."""
    PublicHolidays: NamedNode
    """This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs."""
    PublicSwimmingPool: NamedNode
    """A public swimming pool."""
    PublicToilet: NamedNode
    """A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses."""
    PublicationEvent: NamedNode
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media."""
    PublicationIssue: NamedNode
    """A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.\n\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html)."""
    PublicationVolume: NamedNode
    """A part of a successively published publication such as a periodical or multi-volume work, often numbered. It may represent a time span, such as a year.\n\nSee also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html)."""
    Pulmonary: NamedNode
    """A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states."""
    QAPage: NamedNode
    """A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs)."""
    QualitativeValue: NamedNode
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'."""
    QuantitativeValue: NamedNode
    """ A point value or interval for product characteristics and other purposes."""
    QuantitativeValueDistribution: NamedNode
    """A statistical distribution of values."""
    Quantity: NamedNode
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'."""
    Question: NamedNode
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document."""
    Quiz: NamedNode
    """Quiz: A test of knowledge, skills and abilities."""
    Quotation: NamedNode
    """A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]]."""
    QuoteAction: NamedNode
    """An agent quotes/estimates/appraises an object/product/service with a price at a location/store."""
    RVPark: NamedNode
    """A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like."""
    RadiationTherapy: NamedNode
    """A process of care using radiation aimed at improving a health condition."""
    RadioBroadcastService: NamedNode
    """A delivery service through which radio content is provided via broadcast over the air or online."""
    RadioChannel: NamedNode
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup."""
    RadioClip: NamedNode
    """A short radio program or a segment/part of a radio program."""
    RadioEpisode: NamedNode
    """A radio episode which can be part of a series or season."""
    RadioSeason: NamedNode
    """Season dedicated to radio broadcast and associated online delivery."""
    RadioSeries: NamedNode
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery."""
    RadioStation: NamedNode
    """A radio station."""
    Radiography: NamedNode
    """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body."""
    RandomizedTrial: NamedNode
    """A randomized trial design."""
    Rating: NamedNode
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars."""
    ReactAction: NamedNode
    """The act of responding instinctively and emotionally to an object, expressing a sentiment."""
    ReadAction: NamedNode
    """The act of consuming written content."""
    ReadPermission: NamedNode
    """Permission to read or view the document."""
    RealEstateAgent: NamedNode
    """A real-estate agent."""
    RealEstateListing: NamedNode
    """A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).
  The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]].
  """
    RearWheelDriveConfiguration: NamedNode
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels."""
    ReceiveAction: NamedNode
    """The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.\n\nRelated actions:\n\n* [[SendAction]]: The reciprocal of ReceiveAction.\n* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine)."""
    Recipe: NamedNode
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used to add more detail."""
    Recommendation: NamedNode
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s."""
    RecommendedDoseSchedule: NamedNode
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity."""
    Recruiting: NamedNode
    """Recruiting participants."""
    RecyclingCenter: NamedNode
    """A recycling center."""
    ReducedRelevanceForChildrenConsideration: NamedNode
    """A general code for cases where relevance to children is reduced, e.g. adult education, mortgages, retirement-related products, etc."""
    RefundTypeEnumeration: NamedNode
    """Enumerates several kinds of product return refund types."""
    RefurbishedCondition: NamedNode
    """Indicates that the item is refurbished."""
    RegisterAction: NamedNode
    """The act of registering to be a user of a service, product or web page.\n\nRelated actions:\n\n* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering to be a user of a service, *not* a group/team of people.\n* [[FollowAction]]: Unlike FollowAction, RegisterAction doesn't imply that the agent is expecting to poll for updates from the object.\n* [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't imply that the agent is expecting updates from the object."""
    Registry: NamedNode
    """A registry-based study design."""
    RegularPrice: NamedNode
    """Represents the regular price (typically the previous advertised price before a sale) of an offered product. Often displayed as a strike-through price."""
    ReimbursementCap: NamedNode
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug."""
    RejectAction: NamedNode
    """The act of rejecting to/adopting an object.\n\nRelated actions:\n\n* [[AcceptAction]]: The antonym of RejectAction."""
    RelatedTopicsHealthAspect: NamedNode
    """Other prominent or relevant topics tied to the main topic."""
    RemixAlbum: NamedNode
    """RemixAlbum."""
    Renal: NamedNode
    """A specific branch of medical science that pertains to the study of the kidneys and its respective disease states."""
    RentAction: NamedNode
    """The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment."""
    RentalCarReservation: NamedNode
    """A reservation for a rental car.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations."""
    RentalVehicleUsage: NamedNode
    """Indicates the usage of the vehicle as a rental car."""
    RepaymentSpecification: NamedNode
    """A structured value representing repayment."""
    ReplaceAction: NamedNode
    """The act of editing a recipient by replacing an old object with a new object."""
    ReplyAction: NamedNode
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].\n\nRelated actions:\n\n* [[AskAction]]: Appears generally as an origin of a ReplyAction."""
    Report: NamedNode
    """A Report generated by governmental or non-governmental organization."""
    ReportageNewsArticle: NamedNode
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing
 news articles which are the result of journalistic news reporting conventions.

In practice many news publishers produce a wide variety of article types, many of which might be considered a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.

The [[ReportageNewsArticle]] type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the [[ReportageNewsArticle]] sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.

A [[ReportageNewsArticle]] which goes deeper into analysis can also be marked with an additional type of [[AnalysisNewsArticle]].
"""
    ReportedDoseSchedule: NamedNode
    """A patient-reported or observed dosing schedule for a drug or supplement."""
    ResearchOrganization: NamedNode
    """A Research Organization (e.g. scientific institute, research company)."""
    ResearchProject: NamedNode
    """A Research project."""
    Researcher: NamedNode
    """Researchers."""
    Reservation: NamedNode
    """Describes a reservation for travel, dining or an event. Some reservations require tickets. \n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use [[Offer]]."""
    ReservationCancelled: NamedNode
    """The status for a previously confirmed reservation that is now cancelled."""
    ReservationConfirmed: NamedNode
    """The status of a confirmed reservation."""
    ReservationHold: NamedNode
    """The status of a reservation on hold pending an update like credit card number or flight changes."""
    ReservationPackage: NamedNode
    """A group of multiple reservations with common values for all sub-reservations."""
    ReservationPending: NamedNode
    """The status of a reservation when a request has been sent, but not confirmed."""
    ReservationStatusType: NamedNode
    """Enumerated status values for Reservation."""
    ReserveAction: NamedNode
    """Reserving a concrete object.\n\nRelated actions:\n\n* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation."""
    Reserved: NamedNode
    """Indicates that the item is reserved and therefore not available."""
    Reservoir: NamedNode
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir."""
    Residence: NamedNode
    """The place where a person lives."""
    Resort: NamedNode
    """A resort is a place used for relaxation or recreation, attracting visitors for holidays or vacations. Resorts are places, towns or sometimes commercial establishments operated by a single company (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Resort">http://en.wikipedia.org/wiki/Resort</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    """
    RespiratoryTherapy: NamedNode
    """The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease)."""
    Restaurant: NamedNode
    """A restaurant."""
    RestockingFees: NamedNode
    """Specifies that the customer must pay a restocking fee when returning a product."""
    RestrictedDiet: NamedNode
    """A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. """
    ResultsAvailable: NamedNode
    """Results are available."""
    ResultsNotAvailable: NamedNode
    """Results are not available."""
    ResumeAction: NamedNode
    """The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer)."""
    Retail: NamedNode
    """The drug's cost represents the retail cost of the drug."""
    ReturnAction: NamedNode
    """The act of returning to the origin that which was previously received (concrete objects) or taken (ownership)."""
    ReturnAtKiosk: NamedNode
    """Specifies that product returns must be made at a kiosk."""
    ReturnByMail: NamedNode
    """Specifies that product returns must be done by mail."""
    ReturnFeesCustomerResponsibility: NamedNode
    """Specifies that product returns must be paid for, and are the responsibility of, the customer."""
    ReturnFeesEnumeration: NamedNode
    """Enumerates several kinds of policies for product return fees."""
    ReturnInStore: NamedNode
    """Specifies that product returns must be made in a store."""
    ReturnLabelCustomerResponsibility: NamedNode
    """Indicated that creating a return label is the responsibility of the customer."""
    ReturnLabelDownloadAndPrint: NamedNode
    """Indicated that a return label must be downloaded and printed by the customer."""
    ReturnLabelInBox: NamedNode
    """Specifies that a return label will be provided by the seller in the shipping box."""
    ReturnLabelSourceEnumeration: NamedNode
    """Enumerates several types of return labels for product returns."""
    ReturnMethodEnumeration: NamedNode
    """Enumerates several types of product return methods."""
    ReturnShippingFees: NamedNode
    """Specifies that the customer must pay the return shipping costs when returning a product."""
    Review: NamedNode
    """A review of an item - for example, of a restaurant, movie, or store."""
    ReviewAction: NamedNode
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review."""
    ReviewNewsArticle: NamedNode
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment of a service, product, performance, or artistic or literary work."""
    Rheumatologic: NamedNode
    """A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases."""
    RightHandDriving: NamedNode
    """The steering position is on the right side of the vehicle (viewed from the main direction of driving)."""
    RisksOrComplicationsHealthAspect: NamedNode
    """Information about the risk factors and possible complications that may follow a topic."""
    RiverBodyOfWater: NamedNode
    """A river (for example, the broad majestic Shannon)."""
    Role: NamedNode
    """Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.\n\nSee also [blog post](http://blog.schema.org/2014/06/introducing-role.html)."""
    RoofingContractor: NamedNode
    """A roofing contractor."""
    Room: NamedNode
    """A room is a distinguishable space within a structure, usually separated from other spaces by interior walls (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Room">http://en.wikipedia.org/wiki/Room</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    RsvpAction: NamedNode
    """The act of notifying an event organizer as to whether you expect to attend the event."""
    RsvpResponseMaybe: NamedNode
    """The invitee may or may not attend."""
    RsvpResponseNo: NamedNode
    """The invitee will not attend."""
    RsvpResponseType: NamedNode
    """RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request."""
    RsvpResponseYes: NamedNode
    """The invitee will attend."""
    SRP: NamedNode
    """Represents the suggested retail price ("SRP") of an offered product."""
    SafetyHealthAspect: NamedNode
    """Content about the safety-related aspects of a health topic."""
    SaleEvent: NamedNode
    """Event type: Sales event."""
    SalePrice: NamedNode
    """Represents a sale price (usually active for a limited period) of an offered product."""
    SatireOrParodyContent: NamedNode
    """Content coded 'satire or parody content' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'satire or parody content': A video that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[ImageObject]] to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[ImageObject]] with embedded text to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

For an [[AudioObject]] to be 'satire or parody content': Audio that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)
"""
    SatiricalArticle: NamedNode
    """An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire) in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized."""
    Saturday: NamedNode
    """The day of the week between Friday and Sunday."""
    Schedule: NamedNode
    """A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.
      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also
      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events."""
    ScheduleAction: NamedNode
    """Scheduling future actions, events, or tasks.\n\nRelated actions:\n\n* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation."""
    ScholarlyArticle: NamedNode
    """A scholarly article."""
    School: NamedNode
    """A school."""
    SchoolDistrict: NamedNode
    """A School District is an administrative area for the administration of schools."""
    ScreeningEvent: NamedNode
    """A screening of a movie or other video."""
    ScreeningHealthAspect: NamedNode
    """Content about how to screen or further filter a topic."""
    Sculpture: NamedNode
    """A piece of sculpture."""
    SeaBodyOfWater: NamedNode
    """A sea (for example, the Caspian sea)."""
    SearchAction: NamedNode
    """The act of searching for an object.\n\nRelated actions:\n\n* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily."""
    SearchRescueOrganization: NamedNode
    """A Search and Rescue organization of some kind."""
    SearchResultsPage: NamedNode
    """Web page type: Search results page."""
    Season: NamedNode
    """A media season, e.g. TV, radio, video game etc."""
    Seat: NamedNode
    """Used to describe a seat, such as a reserved seat in an event reservation."""
    SeatingMap: NamedNode
    """A seating map."""
    SeeDoctorHealthAspect: NamedNode
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation."""
    SeekToAction: NamedNode
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure."""
    SelfCareHealthAspect: NamedNode
    """Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself."""
    SelfStorage: NamedNode
    """A self-storage facility."""
    SellAction: NamedNode
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction."""
    SendAction: NamedNode
    """The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:\n\n* [[ReceiveAction]]: The reciprocal of SendAction.\n* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you)."""
    Series: NamedNode
    """A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]]."""
    Service: NamedNode
    """A service provided by an organization, e.g. delivery service, print services, etc."""
    ServiceChannel: NamedNode
    """A means for accessing a service, e.g. a government office location, web site, or phone number."""
    SexualContentConsideration: NamedNode
    """The item contains sexually oriented content such as nudity, suggestive or explicit material, or related online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual enhancement devices, sex toys."""
    ShareAction: NamedNode
    """The act of distributing content to people for their amusement or edification."""
    SheetMusic: NamedNode
    """Printed music, as opposed to performed or recorded music."""
    ShippingDeliveryTime: NamedNode
    """ShippingDeliveryTime provides various pieces of information about delivery times for shipping."""
    ShippingRateSettings: NamedNode
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]]."""
    ShoeStore: NamedNode
    """A shoe store."""
    ShoppingCenter: NamedNode
    """A shopping center or mall."""
    ShortStory: NamedNode
    """Short story or tale. A brief work of literature, usually written in narrative prose."""
    SideEffectsHealthAspect: NamedNode
    """Side effects that can be observed from the usage of the topic."""
    SingleBlindedTrial: NamedNode
    """A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not."""
    SingleCenterTrial: NamedNode
    """A trial that takes place at a single center."""
    SingleFamilyResidence: NamedNode
    """Residence type: Single-family home."""
    SinglePlayer: NamedNode
    """Play mode: SinglePlayer. Which is played by a lone player."""
    SingleRelease: NamedNode
    """SingleRelease."""
    SiteNavigationElement: NamedNode
    """A navigation element of the page."""
    SizeGroupEnumeration: NamedNode
    """Enumerates common size groups for various product categories."""
    SizeSpecification: NamedNode
    """Size related properties of a product, typically a size code ([[name]]) and optionally a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]]). In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]], and suggested body measurements ([[suggestedMeasurement]])."""
    SizeSystemEnumeration: NamedNode
    """Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws."""
    SizeSystemImperial: NamedNode
    """Imperial size system."""
    SizeSystemMetric: NamedNode
    """Metric size system."""
    SkiResort: NamedNode
    """A ski resort."""
    Skin: NamedNode
    """Skin assessment with clinical examination."""
    SocialEvent: NamedNode
    """Event type: Social event."""
    SocialMediaPosting: NamedNode
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc."""
    SoftwareApplication: NamedNode
    """A software application."""
    SoftwareSourceCode: NamedNode
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates."""
    SoldOut: NamedNode
    """Indicates that the item has sold out."""
    SolveMathAction: NamedNode
    """The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression."""
    SomeProducts: NamedNode
    """A placeholder for multiple similar products of the same kind."""
    SoundtrackAlbum: NamedNode
    """SoundtrackAlbum."""
    SpeakableSpecification: NamedNode
    """A SpeakableSpecification indicates (typically via [[xpath]] or [[cssSelector]]) sections of a document that are highlighted as particularly [[speakable]]. Instances of this type are expected to be used primarily as values of the [[speakable]] property."""
    SpecialAnnouncement: NamedNode
    """A SpecialAnnouncement combines a simple date-stamped textual information update
      with contextualized Web links and other structured data.  It represents an information update made by a
      locally-oriented organization, for example schools, pharmacies, healthcare providers,  community groups, police,
      local government.

For work in progress guidelines on Coronavirus-related markup see [this doc](https://docs.google.com/document/d/14ikaGCKxo50rRM7nvKSlbUpjyIk2WMQd3IkB1lItlrM/edit#).

The motivating scenario for SpecialAnnouncement is the [Coronavirus pandemic](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic), and the initial vocabulary is oriented to this urgent situation. Schema.org
expect to improve the markup iteratively as it is deployed and as feedback emerges from use. In addition to our
usual [Github entry](https://github.com/schemaorg/schemaorg/issues/2490), feedback comments can also be provided in [this document](https://docs.google.com/document/d/1fpdFFxk8s87CWwACs53SGkYv3aafSxz_DTtOQxMrBJQ/edit#).


While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like [CAP](https://en.wikipedia.org/wiki/Common_Alerting_Protocol), although there may be overlaps. The intent is to cover
the kinds of everyday practical information being posted to existing websites during an emergency situation.

Several kinds of information can be provided:

We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and
"url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known
URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20_coronavirus_pandemic" or "https://www.wikidata.org/wiki/Q81068910".

For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property's value. For an inline description, use a [[WebContent]] type, and provide the url as a property of that, alongside at least a simple "[[text]]" summary of the page. It is
unlikely that a single SpecialAnnouncement will need all of the possible properties simultaneously.

We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info, [[openingHours]], [[Event]], [[FAQPage]] etc. By linking to those pages from a [[SpecialAnnouncement]] you can help make it clearer that the events are related to the situation (e.g. Coronavirus) indicated by the [[category]] property of the [[SpecialAnnouncement]].

Many [[SpecialAnnouncement]]s will relate to particular regions and to identifiable local organizations. Use [[spatialCoverage]] for the region, and [[announcementLocation]] to indicate specific [[LocalBusiness]]es and [[CivicStructure]]s. If the announcement affects both a particular region and a specific location (for example, a library closure that serves an entire region), use both [[spatialCoverage]] and [[announcementLocation]].

The [[about]] property can be used to indicate entities that are the focus of the announcement. We now recommend using [[about]] only
for representing non-location entities (e.g. a [[Course]] or a [[RadioStation]]). For places, use [[announcementLocation]] and [[spatialCoverage]]. Consumers of this markup should be aware that the initial design encouraged the use of [[about]] for locations too.

The basic content of [[SpecialAnnouncement]] is similar to that of an [RSS](https://en.wikipedia.org/wiki/RSS) or [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)) feed. For publishers without such feeds, basic feed-like information can be shared by posting
[[SpecialAnnouncement]] updates in a page, e.g. using JSON-LD. For sites with Atom/RSS functionality, you can point to a feed
with the [[webFeed]] property. This can be a simple URL, or an inline [[DataFeed]] object, with [[encodingFormat]] providing
media type information, e.g. "application/rss+xml" or "application/atom+xml".
"""
    Specialty: NamedNode
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort."""
    SpeechPathology: NamedNode
    """The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition."""
    SpokenWordAlbum: NamedNode
    """SpokenWordAlbum."""
    SportingGoodsStore: NamedNode
    """A sporting goods store."""
    SportsActivityLocation: NamedNode
    """A sports location, such as a playing field."""
    SportsClub: NamedNode
    """A sports club."""
    SportsEvent: NamedNode
    """Event type: Sports event."""
    SportsOrganization: NamedNode
    """Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations."""
    SportsTeam: NamedNode
    """Organization: Sports team."""
    SpreadsheetDigitalDocument: NamedNode
    """A spreadsheet file."""
    StadiumOrArena: NamedNode
    """A stadium."""
    StagedContent: NamedNode
    """Content coded 'staged content' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'staged content': A video that has been created using actors or similarly contrived.

For an [[ImageObject]] to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.

For an [[ImageObject]] with embedded text to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.

For an [[AudioObject]] to be 'staged content': Audio that has been created using actors or similarly contrived.
"""
    StagesHealthAspect: NamedNode
    """Stages that can be observed from a topic."""
    State: NamedNode
    """A state or province of a country."""
    Statement: NamedNode
    """A statement about something, for example a fun or interesting fact. If known, the main entity this statement is about can be indicated using mainEntity. For more formal claims (e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property to capture the text of the statement."""
    StatisticalPopulation: NamedNode
    """A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.
The properties [[numConstraints]] and [[constraintProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statistical
population, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], where a [[populationType]] such as [[Person]] or [[Event]] can be indicated directly. In most cases it may be better to use [[StatisticalVariable]] instead of [[StatisticalPopulation]]."""
    StatisticalVariable: NamedNode
    """[[StatisticalVariable]] represents any type of statistical metric that can be measured at a place and time. The usage pattern for [[StatisticalVariable]] is typically expressed using [[Observation]] with an explicit [[populationType]], which is a type, typically drawn from Schema.org. Each [[StatisticalVariable]] is marked as a [[ConstraintNode]], meaning that some properties (those listed using [[constraintProperty]]) serve in this setting solely to define the statistical variable rather than literally describe a specific person, place or thing. For example, a [[StatisticalVariable]] Median_Height_Person_Female representing the median height of women, could be written as follows: the population type is [[Person]]; the measuredProperty [[height]]; the [[statType]] [[median]]; the [[gender]] [[Female]]. It is important to note that there are many kinds of scientific quantitative observation which are not fully, perfectly or unambiguously described following this pattern, or with solely Schema.org terminology. The approach taken here is designed to allow partial, incremental or minimal description of [[StatisticalVariable]]s, and the use of detailed sets of entity and property IDs from external repositories. The [[measurementMethod]], [[unitCode]] and [[unitText]] properties can also be used to clarify the specific nature and notation of an observed measurement. """
    StatusEnumeration: NamedNode
    """Lists or enumerations dealing with status types."""
    SteeringPositionValue: NamedNode
    """A value indicating a steering position."""
    Store: NamedNode
    """A retail good store."""
    StoreCreditRefund: NamedNode
    """Specifies that the customer receives a store credit as refund when returning a product."""
    StrengthTraining: NamedNode
    """Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training."""
    StructuredValue: NamedNode
    """Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing."""
    StudioAlbum: NamedNode
    """StudioAlbum."""
    StupidType: NamedNode
    """A StupidType for testing."""
    SubscribeAction: NamedNode
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates pushed to.\n\nRelated actions:\n\n* [[FollowAction]]: Unlike FollowAction, SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively pushed for updates.\n* [[RegisterAction]]: Unlike RegisterAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object.\n* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested in continuing receiving updates from the object."""
    Subscription: NamedNode
    """Represents the subscription pricing component of the total price for an offered product."""
    Substance: NamedNode
    """Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical."""
    SubwayStation: NamedNode
    """A subway station."""
    Suite: NamedNode
    """A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
"""
    Sunday: NamedNode
    """The day of the week between Saturday and Monday."""
    SuperficialAnatomy: NamedNode
    """Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure)."""
    Surgical: NamedNode
    """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means."""
    SurgicalProcedure: NamedNode
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes."""
    SuspendAction: NamedNode
    """The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer)."""
    Suspended: NamedNode
    """Suspended."""
    Syllabus: NamedNode
    """A syllabus that describes the material covered in a course, often with several such sections per [[Course]] so that a distinct [[timeRequired]] can be provided for that section of the [[Course]]."""
    SymptomsHealthAspect: NamedNode
    """Symptoms or related symptoms of a Topic."""
    Synagogue: NamedNode
    """A synagogue."""
    TVClip: NamedNode
    """A short TV program or a segment/part of a TV program."""
    TVEpisode: NamedNode
    """A TV episode which can be part of a series or season."""
    TVSeason: NamedNode
    """Season dedicated to TV broadcast and associated online delivery."""
    TVSeries: NamedNode
    """CreativeWorkSeries dedicated to TV broadcast and associated online delivery."""
    Table: NamedNode
    """A table on a Web page."""
    TakeAction: NamedNode
    """The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.\n\nRelated actions:\n\n* [[GiveAction]]: The reciprocal of TakeAction.\n* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred."""
    TattooParlor: NamedNode
    """A tattoo parlor."""
    Taxi: NamedNode
    """A taxi."""
    TaxiReservation: NamedNode
    """A reservation for a taxi.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    TaxiService: NamedNode
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled."""
    TaxiStand: NamedNode
    """A taxi stand."""
    TaxiVehicleUsage: NamedNode
    """Indicates the usage of the car as a taxi."""
    Taxon: NamedNode
    """A set of organisms asserted to represent a natural cohesive biological unit."""
    TechArticle: NamedNode
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc."""
    TelevisionChannel: NamedNode
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup."""
    TelevisionStation: NamedNode
    """A television station."""
    TennisComplex: NamedNode
    """A tennis complex."""
    Terminated: NamedNode
    """Terminated."""
    Text: NamedNode
    """Data type: Text."""
    TextDigitalDocument: NamedNode
    """A file composed primarily of text."""
    TextObject: NamedNode
    """A text file. The text can be unformatted or contain markup, html, etc."""
    TheaterEvent: NamedNode
    """Event type: Theater performance."""
    TheaterGroup: NamedNode
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre."""
    Therapeutic: NamedNode
    """A medical device used for therapeutic purposes."""
    TherapeuticProcedure: NamedNode
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition."""
    Thesis: NamedNode
    """A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification."""
    Thing: NamedNode
    """The most generic type of item."""
    Throat: NamedNode
    """Throat assessment with  clinical examination."""
    Thursday: NamedNode
    """The day of the week between Wednesday and Friday."""
    Ticket: NamedNode
    """Used to describe a ticket to an event, a flight, a bus ride, etc."""
    TieAction: NamedNode
    """The act of reaching a draw in a competitive activity."""
    TierBenefitEnumeration: NamedNode
    """An enumeration of possible benefits as part of a loyalty (members) program."""
    TierBenefitLoyaltyPoints: NamedNode
    """Benefit of the tier is earning of loyalty points."""
    TierBenefitLoyaltyPrice: NamedNode
    """Benefit of the tier is a members-only price."""
    TierBenefitLoyaltyReturns: NamedNode
    """Benefit of the tier is members-only returns, for example free unlimited returns."""
    TierBenefitLoyaltyShipping: NamedNode
    """Benefit of the tier is a members-only shipping price or speed (for example free shipping or 1-day shipping)."""
    Time: NamedNode
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for details](http://www.w3.org/TR/xmlschema-2/#time))."""
    TipAction: NamedNode
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered."""
    TireShop: NamedNode
    """A tire shop."""
    TobaccoNicotineConsideration: NamedNode
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs."""
    TollFree: NamedNode
    """The associated telephone number is toll free."""
    TouristAttraction: NamedNode
    """A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)"""
    TouristDestination: NamedNode
    """A tourist destination. In principle any [[Place]] can be a [[TouristDestination]] from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]] to add tourist relevant properties to any other [[Place]].  A [[TouristDestination]] is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s, often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines Destination (main destination of a tourism trip) as the place visited that is central to the decision to take the trip.
  (See examples below.)"""
    TouristInformationCenter: NamedNode
    """A tourist information center."""
    TouristTrip: NamedNode
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]]) often linked by a similar theme, geographic area, or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors.
  (See examples below.)"""
    Toxicologic: NamedNode
    """A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning."""
    ToyStore: NamedNode
    """A toy store."""
    TrackAction: NamedNode
    """An agent tracks an object for updates.\n\nRelated actions:\n\n* [[FollowAction]]: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.\n* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects."""
    TradeAction: NamedNode
    """The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment."""
    TraditionalChinese: NamedNode
    """A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions."""
    TrainReservation: NamedNode
    """A reservation for train travel.\n\nNote: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]]."""
    TrainStation: NamedNode
    """A train station."""
    TrainTrip: NamedNode
    """A trip on a commercial train line."""
    TrainedAlgorithmicMediaDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia">trained algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    TransferAction: NamedNode
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another."""
    TransformedContent: NamedNode
    """Content coded 'transformed content' in a [[MediaReview]], considered in the context of how it was published or shared.

For a [[VideoObject]] to be 'transformed content':  or all of the video has been manipulated to transform the footage itself. This category includes using tools like the Adobe Suite to change the speed of the video, add or remove visual elements or dub audio. Deepfakes are also a subset of transformation.

For an [[ImageObject]] to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.

For an [[ImageObject]] with embedded text to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.

For an [[AudioObject]] to be 'transformed content': Part or all of the audio has been manipulated to alter the words or sounds, or the audio has been synthetically generated, such as to create a sound-alike voice.
"""
    TransitMap: NamedNode
    """A transit map."""
    TravelAction: NamedNode
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants."""
    TravelAgency: NamedNode
    """A travel agency."""
    TreatmentIndication: NamedNode
    """An indication for treating an underlying condition, symptom, etc."""
    TreatmentsHealthAspect: NamedNode
    """Treatments or related therapies for a Topic."""
    Trip: NamedNode
    """A trip or journey. An itinerary of visits to one or more places."""
    TripleBlindedTrial: NamedNode
    """A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to."""
    Tuesday: NamedNode
    """The day of the week between Monday and Wednesday."""
    TypeAndQuantityNode: NamedNode
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer."""
    TypesHealthAspect: NamedNode
    """Categorization and other types related to a topic."""
    UKNonprofitType: NamedNode
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom."""
    UKTrust: NamedNode
    """UKTrust: Non-profit type referring to a UK trust."""
    URL: NamedNode
    """Data type: URL."""
    USNonprofitType: NamedNode
    """USNonprofitType: Non-profit organization type originating from the United States."""
    Ultrasound: NamedNode
    """Ultrasound imaging."""
    UnRegisterAction: NamedNode
    """The act of un-registering from a service.\n\nRelated actions:\n\n* [[RegisterAction]]: antonym of UnRegisterAction.\n* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people."""
    UnclassifiedAdultConsideration: NamedNode
    """The item is suitable only for adults, without indicating why. Due to widespread use of "adult" as a euphemism for "sexual", many such items are likely suited also for the SexualContentConsideration code."""
    UnemploymentSupport: NamedNode
    """UnemploymentSupport: this is a benefit for unemployment support."""
    UnincorporatedAssociationCharity: NamedNode
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK)."""
    UnitPriceSpecification: NamedNode
    """The price asked for a given offer by the respective organization or person."""
    UnofficialLegalValue: NamedNode
    """Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher)."""
    UpdateAction: NamedNode
    """The act of managing by changing/editing the state of the object."""
    Urologic: NamedNode
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system."""
    UsageOrScheduleHealthAspect: NamedNode
    """Content about how, when, frequency and dosage of a topic."""
    UseAction: NamedNode
    """The act of applying an object to its intended purpose."""
    UsedCondition: NamedNode
    """Indicates that the item is used."""
    UserBlocks: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserCheckins: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserComments: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserDownloads: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserInteraction: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserLikes: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserPageVisits: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserPlays: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserPlusOnes: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    UserReview: NamedNode
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]]."""
    UserTweets: NamedNode
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]]."""
    VacationRental: NamedNode
    """A kind of lodging business that focuses on renting single properties for limited time."""
    VeganDiet: NamedNode
    """A diet exclusive of all animal products."""
    VegetarianDiet: NamedNode
    """A diet exclusive of animal meat."""
    Vehicle: NamedNode
    """A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space."""
    Vein: NamedNode
    """A type of blood vessel that specifically carries blood to the heart."""
    VenueMap: NamedNode
    """A venue map (e.g. for malls, auditoriums, museums, etc.)."""
    Vessel: NamedNode
    """A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body."""
    VeterinaryCare: NamedNode
    """A vet's office."""
    VideoGallery: NamedNode
    """Web page type: Video gallery page."""
    VideoGame: NamedNode
    """A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device."""
    VideoGameClip: NamedNode
    """A short segment/part of a video game."""
    VideoGameSeries: NamedNode
    """A video game series."""
    VideoObject: NamedNode
    """A video file."""
    VideoObjectSnapshot: NamedNode
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity."""
    ViewAction: NamedNode
    """The act of consuming static visual content."""
    VinylFormat: NamedNode
    """VinylFormat."""
    ViolenceConsideration: NamedNode
    """Item shows or promotes violence."""
    VirtualLocation: NamedNode
    """An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world."""
    VirtualRecordingDigitalSource: NamedNode
    """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/virtualRecording">virtual recording</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary."""
    Virus: NamedNode
    """Pathogenic virus that causes viral infection."""
    VisualArtsEvent: NamedNode
    """Event type: Visual arts event."""
    VisualArtwork: NamedNode
    """A work of art that is primarily visual in character."""
    VitalSign: NamedNode
    """Vital signs are measures of various physiological functions in order to assess the most basic body functions."""
    Volcano: NamedNode
    """A volcano, like Fujisan."""
    VoteAction: NamedNode
    """The act of expressing a preference from a fixed/finite/structured set of choices/options."""
    WPAdBlock: NamedNode
    """An advertising section of the page."""
    WPFooter: NamedNode
    """The footer section of the page."""
    WPHeader: NamedNode
    """The header section of the page."""
    WPSideBar: NamedNode
    """A sidebar section of the page."""
    WantAction: NamedNode
    """The act of expressing a desire about the object. An agent wants an object."""
    WarrantyPromise: NamedNode
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product."""
    WarrantyScope: NamedNode
    """A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#Labor-BringIn\n* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn\n* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp
      """
    WatchAction: NamedNode
    """The act of consuming dynamic/moving visual content."""
    Waterfall: NamedNode
    """A waterfall, like Niagara."""
    WeaponConsideration: NamedNode
    """The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or other bombs, and spears."""
    WearAction: NamedNode
    """The act of dressing oneself in clothing."""
    WearableMeasurementBack: NamedNode
    """Measurement of the back section, for example of a jacket."""
    WearableMeasurementChestOrBust: NamedNode
    """Measurement of the chest/bust section, for example of a suit."""
    WearableMeasurementCollar: NamedNode
    """Measurement of the collar, for example of a shirt."""
    WearableMeasurementCup: NamedNode
    """Measurement of the cup, for example of a bra."""
    WearableMeasurementHeight: NamedNode
    """Measurement of the height, for example the heel height of a shoe."""
    WearableMeasurementHips: NamedNode
    """Measurement of the hip section, for example of a skirt."""
    WearableMeasurementInseam: NamedNode
    """Measurement of the inseam, for example of pants."""
    WearableMeasurementLength: NamedNode
    """Represents the length, for example of a dress."""
    WearableMeasurementOutsideLeg: NamedNode
    """Measurement of the outside leg, for example of pants."""
    WearableMeasurementSleeve: NamedNode
    """Measurement of the sleeve length, for example of a shirt."""
    WearableMeasurementTypeEnumeration: NamedNode
    """Enumerates common types of measurement for wearables products."""
    WearableMeasurementWaist: NamedNode
    """Measurement of the waist section, for example of pants."""
    WearableMeasurementWidth: NamedNode
    """Measurement of the width, for example of shoes."""
    WearableSizeGroupBig: NamedNode
    """Size group "Big" for wearables."""
    WearableSizeGroupBoys: NamedNode
    """Size group "Boys" for wearables."""
    WearableSizeGroupEnumeration: NamedNode
    """Enumerates common size groups (also known as "size types") for wearable products."""
    WearableSizeGroupExtraShort: NamedNode
    """Size group "Extra Short" for wearables."""
    WearableSizeGroupExtraTall: NamedNode
    """Size group "Extra Tall" for wearables."""
    WearableSizeGroupGirls: NamedNode
    """Size group "Girls" for wearables."""
    WearableSizeGroupHusky: NamedNode
    """Size group "Husky" (or "Stocky") for wearables."""
    WearableSizeGroupInfants: NamedNode
    """Size group "Infants" for wearables."""
    WearableSizeGroupJuniors: NamedNode
    """Size group "Juniors" for wearables."""
    WearableSizeGroupMaternity: NamedNode
    """Size group "Maternity" for wearables."""
    WearableSizeGroupMens: NamedNode
    """Size group "Mens" for wearables."""
    WearableSizeGroupMisses: NamedNode
    """Size group "Misses" (also known as "Missy") for wearables."""
    WearableSizeGroupPetite: NamedNode
    """Size group "Petite" for wearables."""
    WearableSizeGroupPlus: NamedNode
    """Size group "Plus" for wearables."""
    WearableSizeGroupRegular: NamedNode
    """Size group "Regular" for wearables."""
    WearableSizeGroupShort: NamedNode
    """Size group "Short" for wearables."""
    WearableSizeGroupTall: NamedNode
    """Size group "Tall" for wearables."""
    WearableSizeGroupWomens: NamedNode
    """Size group "Womens" for wearables."""
    WearableSizeSystemAU: NamedNode
    """Australian size system for wearables."""
    WearableSizeSystemBR: NamedNode
    """Brazilian size system for wearables."""
    WearableSizeSystemCN: NamedNode
    """Chinese size system for wearables."""
    WearableSizeSystemContinental: NamedNode
    """Continental size system for wearables."""
    WearableSizeSystemDE: NamedNode
    """German size system for wearables."""
    WearableSizeSystemEN13402: NamedNode
    """EN 13402 (joint European standard for size labelling of clothes)."""
    WearableSizeSystemEnumeration: NamedNode
    """Enumerates common size systems specific for wearable products."""
    WearableSizeSystemEurope: NamedNode
    """European size system for wearables."""
    WearableSizeSystemFR: NamedNode
    """French size system for wearables."""
    WearableSizeSystemGS1: NamedNode
    """GS1 (formerly NRF) size system for wearables."""
    WearableSizeSystemIT: NamedNode
    """Italian size system for wearables."""
    WearableSizeSystemJP: NamedNode
    """Japanese size system for wearables."""
    WearableSizeSystemMX: NamedNode
    """Mexican size system for wearables."""
    WearableSizeSystemUK: NamedNode
    """United Kingdom size system for wearables."""
    WearableSizeSystemUS: NamedNode
    """United States size system for wearables."""
    WebAPI: NamedNode
    """An application programming interface accessible over Web/Internet technologies."""
    WebApplication: NamedNode
    """Web applications."""
    WebContent: NamedNode
    """WebContent is a type representing all [[WebPage]], [[WebSite]] and [[WebPageElement]] content. It is sometimes the case that detailed distinctions between Web pages, sites and their parts are not always important or obvious. The  [[WebContent]] type makes it easier to describe Web-addressable content without requiring such distinctions to always be stated. (The intent is that the existing types [[WebPage]], [[WebSite]] and [[WebPageElement]] will eventually be declared as subtypes of [[WebContent]].)"""
    WebPage: NamedNode
    """A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page."""
    WebPageElement: NamedNode
    """A web page element, like a table or an image."""
    WebSite: NamedNode
    """A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs."""
    Wednesday: NamedNode
    """The day of the week between Tuesday and Thursday."""
    WesternConventional: NamedNode
    """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine."""
    Wholesale: NamedNode
    """The drug's cost represents the wholesale acquisition cost of the drug."""
    WholesaleStore: NamedNode
    """A wholesale store."""
    WinAction: NamedNode
    """The act of achieving victory in a competitive activity."""
    Winery: NamedNode
    """A winery."""
    Withdrawn: NamedNode
    """Withdrawn."""
    WorkBasedProgram: NamedNode
    """A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs."""
    WorkersUnion: NamedNode
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying."""
    WriteAction: NamedNode
    """The act of authoring written creative content."""
    WritePermission: NamedNode
    """Permission to write or edit the document."""
    XPathType: NamedNode
    """Text representing an XPath (typically but not necessarily version 1.0)."""
    XRay: NamedNode
    """X-ray imaging."""
    ZoneBoardingPolicy: NamedNode
    """The airline boards by zones of the plane."""
    Zoo: NamedNode
    """A zoo."""
    about: NamedNode
    """The subject matter of the content."""
    abridged: NamedNode
    """Indicates whether the book is an abridged edition."""
    abstract: NamedNode
    """An abstract is a short description that summarizes a [[CreativeWork]]."""
    accelerationTime: NamedNode
    """The time needed to accelerate the vehicle from a given start velocity to a given target velocity.\n\nTypical unit code(s): SEC for seconds\n\n* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds."""
    acceptedAnswer: NamedNode
    """The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author."""
    acceptedOffer: NamedNode
    """The offer(s) -- e.g., product, quantity and price combinations -- included in the order."""
    acceptedPaymentMethod: NamedNode
    """The payment method(s) that are accepted in general by an organization, or for some specific demand or offer."""
    acceptsReservations: NamedNode
    """Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```."""
    accessCode: NamedNode
    """Password, PIN, or access code needed for delivery (e.g. from a locker)."""
    accessMode: NamedNode
    """The human sensory perceptual system or cognitive faculty through which a person may process or perceive information. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary)."""
    accessModeSufficient: NamedNode
    """A list of single or combined accessModes that are sufficient to understand all the intellectual content of a resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary)."""
    accessibilityAPI: NamedNode
    """Indicates that the resource is compatible with the referenced accessibility API. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary)."""
    accessibilityControl: NamedNode
    """Identifies input methods that are sufficient to fully control the described resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary)."""
    accessibilityFeature: NamedNode
    """Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary)."""
    accessibilityHazard: NamedNode
    """A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary)."""
    accessibilitySummary: NamedNode
    """A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed"."""
    accommodationCategory: NamedNode
    """Category of an [[Accommodation]], following real estate conventions, e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields  for suggested values)."""
    accommodationFloorPlan: NamedNode
    """A floorplan of some [[Accommodation]]."""
    accountId: NamedNode
    """The identifier for the account the payment will be applied to."""
    accountMinimumInflow: NamedNode
    """A minimum amount that has to be paid in every month."""
    accountOverdraftLimit: NamedNode
    """An overdraft is an extension of credit from a lending institution when an account reaches zero. An overdraft allows the individual to continue withdrawing money even if the account has no funds in it. Basically the bank allows people to borrow a set amount of money."""
    accountablePerson: NamedNode
    """Specifies the Person that is legally accountable for the CreativeWork."""
    acquireLicensePage: NamedNode
    """Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item."""
    acquiredFrom: NamedNode
    """The organization or person from which the product was acquired."""
    acrissCode: NamedNode
    """The ACRISS Car Classification Code is a code used by many car rental companies, for classifying vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards."""
    actionAccessibilityRequirement: NamedNode
    """A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed."""
    actionApplication: NamedNode
    """An application that can complete the request."""
    actionOption: NamedNode
    """A sub property of object. The options subject to this action."""
    actionPlatform: NamedNode
    """The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication."""
    actionStatus: NamedNode
    """Indicates the current disposition of the Action."""
    actionableFeedbackPolicy: NamedNode
    """For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication."""
    activeIngredient: NamedNode
    """An active ingredient, typically chemical compounds and/or biologic substances."""
    activityDuration: NamedNode
    """Length of time to engage in the activity."""
    activityFrequency: NamedNode
    """How often one should engage in the activity."""
    actor: NamedNode
    """An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip."""
    actors: NamedNode
    """An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip."""
    addOn: NamedNode
    """An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge)."""
    additionalName: NamedNode
    """An additional name for a Person, can be used for a middle name."""
    additionalNumberOfGuests: NamedNode
    """If responding yes, the number of guests who will attend in addition to the invitee."""
    additionalProperty: NamedNode
    """A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\n\nNote: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
"""
    additionalType: NamedNode
    """An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the
    use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org <a href="https://schema.org/docs/styleguide.html">style guide</a>."""
    additionalVariable: NamedNode
    """Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc."""
    address: NamedNode
    """Physical address of the item."""
    addressCountry: NamedNode
    """The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1)."""
    addressLocality: NamedNode
    """The locality in which the street address is, and which is in the region. For example, Mountain View."""
    addressRegion: NamedNode
    """The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)."""
    administrationRoute: NamedNode
    """A route by which this drug may be administered, e.g. 'oral'."""
    advanceBookingRequirement: NamedNode
    """The amount of time that is required between accepting the offer and the actual usage of the resource or service."""
    adverseOutcome: NamedNode
    """A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead."""
    affectedBy: NamedNode
    """Drugs that affect the test's results."""
    affiliation: NamedNode
    """An organization that this person is affiliated with. For example, a school/university, a club, or a team."""
    afterMedia: NamedNode
    """A media object representing the circumstances after performing this direction."""
    agent: NamedNode
    """The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book."""
    agentInteractionStatistic: NamedNode
    """The number of completed interactions for this entity, in a particular role (the 'agent'), in a particular action (indicated in the statistic), and in a particular context (i.e. interactionService)."""
    aggregateRating: NamedNode
    """The overall rating, based on a collection of reviews or ratings, of the item."""
    aircraft: NamedNode
    """The kind of aircraft (e.g., "Boeing 747")."""
    album: NamedNode
    """A music album."""
    albumProductionType: NamedNode
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc."""
    albumRelease: NamedNode
    """A release of this album."""
    albumReleaseType: NamedNode
    """The kind of release which this album is: single, EP or album."""
    albums: NamedNode
    """A collection of music albums."""
    alcoholWarning: NamedNode
    """Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug."""
    algorithm: NamedNode
    """The algorithm or rules to follow to compute the score."""
    alignmentType: NamedNode
    """A category of alignment between the learning resource and the framework node. Recommended values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'."""
    alternateName: NamedNode
    """An alias for the item."""
    alternativeHeadline: NamedNode
    """A secondary title of the CreativeWork."""
    alternativeOf: NamedNode
    """Another gene which is a variation of this one."""
    alumni: NamedNode
    """Alumni of an organization."""
    alumniOf: NamedNode
    """An organization that the person is an alumni of."""
    amenityFeature: NamedNode
    """An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs."""
    amount: NamedNode
    """The amount of money."""
    amountOfThisGood: NamedNode
    """The quantity of the goods included in the offer."""
    announcementLocation: NamedNode
    """Indicates a specific [[CivicStructure]] or [[LocalBusiness]] associated with the SpecialAnnouncement. For example, a specific testing facility or business with special opening hours. For a larger geographic region like a quarantine of an entire region, use [[spatialCoverage]]."""
    annualPercentageRate: NamedNode
    """The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction."""
    answerCount: NamedNode
    """The number of answers this question has received."""
    answerExplanation: NamedNode
    """A step-by-step or full explanation about Answer. Can outline how this Answer was achieved or contain more broad clarification or statement about it. """
    antagonist: NamedNode
    """The muscle whose action counteracts the specified muscle."""
    appearance: NamedNode
    """Indicates an occurrence of a [[Claim]] in some [[CreativeWork]]."""
    applicableCountry: NamedNode
    """A country where a particular merchant return policy applies to, for example the two-letter ISO 3166-1 alpha-2 country code."""
    applicableLocation: NamedNode
    """The location in which the status applies."""
    applicantLocationRequirements: NamedNode
    """The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements."""
    application: NamedNode
    """An application that can complete the request."""
    applicationCategory: NamedNode
    """Type of software application, e.g. 'Game, Multimedia'."""
    applicationContact: NamedNode
    """Contact details for further information relevant to this job posting."""
    applicationDeadline: NamedNode
    """The date at which the program stops collecting applications for the next enrollment cycle."""
    applicationStartDate: NamedNode
    """The date at which the program begins collecting applications for the next enrollment cycle."""
    applicationSubCategory: NamedNode
    """Subcategory of the application, e.g. 'Arcade Game'."""
    applicationSuite: NamedNode
    """The name of the application suite to which the application belongs (e.g. Excel belongs to Office)."""
    appliesToDeliveryMethod: NamedNode
    """The delivery method(s) to which the delivery charge or payment charge specification applies."""
    appliesToPaymentMethod: NamedNode
    """The payment method(s) to which the payment charge specification applies."""
    archiveHeld: NamedNode
    """Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an [[ArchiveOrganization]]."""
    archivedAt: NamedNode
    """Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content."""
    area: NamedNode
    """The area within which users can expect to reach the broadcast service."""
    areaServed: NamedNode
    """The geographic area where a service or offered item is provided."""
    arrivalAirport: NamedNode
    """The airport where the flight terminates."""
    arrivalBoatTerminal: NamedNode
    """The terminal or port from which the boat arrives."""
    arrivalBusStop: NamedNode
    """The stop or station from which the bus arrives."""
    arrivalGate: NamedNode
    """Identifier of the flight's arrival gate."""
    arrivalPlatform: NamedNode
    """The platform where the train arrives."""
    arrivalStation: NamedNode
    """The station where the train trip ends."""
    arrivalTerminal: NamedNode
    """Identifier of the flight's arrival terminal."""
    arrivalTime: NamedNode
    """The expected arrival time."""
    artEdition: NamedNode
    """The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20")."""
    artMedium: NamedNode
    """The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)"""
    arterialBranch: NamedNode
    """The branches that comprise the arterial structure."""
    artform: NamedNode
    """e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc."""
    articleBody: NamedNode
    """The actual body of the article."""
    articleSection: NamedNode
    """Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc."""
    artist: NamedNode
    """The primary artist for a work
    	in a medium other than pencils or digital line art--for example, if the
    	primary artwork is done in watercolors or digital paints."""
    artworkSurface: NamedNode
    """The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc."""
    asin: NamedNode
    """An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).

Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.
ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too."""
    aspect: NamedNode
    """An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc."""
    assembly: NamedNode
    """Library file name, e.g., mscorlib.dll, system.web.dll."""
    assemblyVersion: NamedNode
    """Associated product/technology version. E.g., .NET Framework 4.5."""
    assesses: NamedNode
    """The item being described is intended to assess the competency or learning outcome defined by the referenced term."""
    associatedAnatomy: NamedNode
    """The anatomy of the underlying organ system or structures associated with this entity."""
    associatedArticle: NamedNode
    """A NewsArticle associated with the Media Object."""
    associatedClaimReview: NamedNode
    """An associated [[ClaimReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]]."""
    associatedDisease: NamedNode
    """Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or a URL. If you want to add an evidence supporting the association, please use PropertyValue."""
    associatedMedia: NamedNode
    """A media object that encodes this CreativeWork. This property is a synonym for encoding."""
    associatedMediaReview: NamedNode
    """An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]]."""
    associatedPathophysiology: NamedNode
    """If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system."""
    associatedReview: NamedNode
    """An associated [[Review]]."""
    athlete: NamedNode
    """A person that acts as performing member of a sports team; a player as opposed to a coach."""
    attendee: NamedNode
    """A person or organization attending the event."""
    attendees: NamedNode
    """A person attending the event."""
    audience: NamedNode
    """An intended audience, i.e. a group for whom something was created."""
    audienceType: NamedNode
    """The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.)."""
    audio: NamedNode
    """An embedded audio object."""
    auditDate: NamedNode
    """Date when a certification was last audited. See also  [gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate)."""
    authenticator: NamedNode
    """The Organization responsible for authenticating the user's subscription. For example, many media apps require a cable/satellite provider to authenticate your subscription before playing media."""
    author: NamedNode
    """The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably."""
    availability: NamedNode
    """The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc."""
    availabilityEnds: NamedNode
    """The end of the availability of the product or service included in the offer."""
    availabilityStarts: NamedNode
    """The beginning of the availability of the product or service included in the offer."""
    availableAtOrFrom: NamedNode
    """The place(s) from which the offer can be obtained (e.g. store locations)."""
    availableChannel: NamedNode
    """A means of accessing the service (e.g. a phone bank, a web site, a location, etc.)."""
    availableDeliveryMethod: NamedNode
    """The delivery method(s) available for this offer."""
    availableFrom: NamedNode
    """When the item is available for pickup from the store, locker, etc."""
    availableIn: NamedNode
    """The location in which the strength is available."""
    availableLanguage: NamedNode
    """A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]]."""
    availableOnDevice: NamedNode
    """Device required to run the application. Used in cases where a specific make/model is required to run the application."""
    availableService: NamedNode
    """A medical service available from this provider."""
    availableStrength: NamedNode
    """An available dosage strength for the drug."""
    availableTest: NamedNode
    """A diagnostic test or procedure offered by this lab."""
    availableThrough: NamedNode
    """After this date, the item will no longer be available for pickup."""
    award: NamedNode
    """An award won by or for this item."""
    awards: NamedNode
    """Awards won by or for this item."""
    awayTeam: NamedNode
    """The away team in a sports event."""
    backstory: NamedNode
    """For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc."""
    bankAccountType: NamedNode
    """The type of a bank account."""
    baseSalary: NamedNode
    """The base salary of the job or of an employee in an EmployeeRole."""
    bccRecipient: NamedNode
    """A sub property of recipient. The recipient blind copied on a message."""
    bed: NamedNode
    """The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.
      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property."""
    beforeMedia: NamedNode
    """A media object representing the circumstances before performing this direction."""
    beneficiaryBank: NamedNode
    """A bank or bank’s branch, financial institution or international financial institution operating the beneficiary’s bank account or releasing funds for the beneficiary."""
    benefits: NamedNode
    """Description of benefits associated with the job."""
    benefitsSummaryUrl: NamedNode
    """The URL that goes directly to the summary of benefits and coverage for the specific standard plan or plan variation."""
    bestRating: NamedNode
    """The highest value allowed in this rating system."""
    billingAddress: NamedNode
    """The billing address for the order."""
    billingDuration: NamedNode
    """Specifies for how long this price (or price component) will be billed. Can be used, for example, to model the contractual duration of a subscription or payment plan. Type can be either a Duration or a Number (in which case the unit of measurement, for example month, is specified by the unitCode property)."""
    billingIncrement: NamedNode
    """This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property."""
    billingPeriod: NamedNode
    """The time interval used to compute the invoice."""
    billingStart: NamedNode
    """Specifies after how much time this price (or price component) becomes valid and billing starts. Can be used, for example, to model a price increase after the first year of a subscription. The unit of measurement is specified by the unitCode property."""
    bioChemInteraction: NamedNode
    """A BioChemEntity that is known to interact with this item."""
    bioChemSimilarity: NamedNode
    """A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms."""
    biologicalRole: NamedNode
    """A role played by the BioChemEntity within a biological context."""
    biomechnicalClass: NamedNode
    """The biomechanical properties of the bone."""
    birthDate: NamedNode
    """Date of birth."""
    birthPlace: NamedNode
    """The place where the person was born."""
    bitrate: NamedNode
    """The bitrate of the media object."""
    blogPost: NamedNode
    """A posting that is part of this blog."""
    blogPosts: NamedNode
    """Indicates a post that is part of a [[Blog]]. Note that historically, what we term a "Blog" was once known as a "weblog", and that what we term a "BlogPosting" is now often colloquially referred to as a "blog"."""
    bloodSupply: NamedNode
    """The blood vessel that carries blood from the heart to the muscle."""
    boardingGroup: NamedNode
    """The airline-specific indicator of boarding order / preference."""
    boardingPolicy: NamedNode
    """The type of boarding policy used by the airline (e.g. zone-based or group-based)."""
    bodyLocation: NamedNode
    """Location in the body of the anatomical structure."""
    bodyType: NamedNode
    """Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.)."""
    bookEdition: NamedNode
    """The edition of the book."""
    bookFormat: NamedNode
    """The format of the book."""
    bookingAgent: NamedNode
    """'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent."""
    bookingTime: NamedNode
    """The date and time the reservation was booked."""
    borrower: NamedNode
    """A sub property of participant. The person that borrows the object being lent."""
    box: NamedNode
    """A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character."""
    branch: NamedNode
    """The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]]."""
    branchCode: NamedNode
    """A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs.\n\nFor example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.
      """
    branchOf: NamedNode
    """The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical) [[branch]]."""
    brand: NamedNode
    """The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person."""
    breadcrumb: NamedNode
    """A set of links that can help a user understand and navigate a website hierarchy."""
    breastfeedingWarning: NamedNode
    """Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding mothers."""
    broadcastAffiliateOf: NamedNode
    """The media network(s) whose content is broadcast on this station."""
    broadcastChannelId: NamedNode
    """The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number."""
    broadcastDisplayName: NamedNode
    """The name displayed in the channel guide. For many US affiliates, it is the network name."""
    broadcastFrequency: NamedNode
    """The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequencies of AM and FM radio channels, e.g. "87 FM"."""
    broadcastFrequencyValue: NamedNode
    """The frequency in MHz for a particular broadcast."""
    broadcastOfEvent: NamedNode
    """The event being broadcast such as a sporting event or awards ceremony."""
    broadcastServiceTier: NamedNode
    """The type of service required to have access to the channel (e.g. Standard or Premium)."""
    broadcastSignalModulation: NamedNode
    """The modulation (e.g. FM, AM, etc) used by a particular broadcast service."""
    broadcastSubChannel: NamedNode
    """The subchannel used for the broadcast."""
    broadcastTimezone: NamedNode
    """The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which the service bases its broadcasts."""
    broadcaster: NamedNode
    """The organization owning or operating the broadcast service."""
    broker: NamedNode
    """An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred."""
    browserRequirements: NamedNode
    """Specifies browser requirements in human-readable text. For example, 'requires HTML5 support'."""
    busName: NamedNode
    """The name of the bus (e.g. Bolt Express)."""
    busNumber: NamedNode
    """The unique identifier for the bus."""
    businessDays: NamedNode
    """Days of the week when the merchant typically operates, indicated via opening hours markup."""
    businessFunction: NamedNode
    """The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell."""
    buyer: NamedNode
    """A sub property of participant. The participant/person/organization that bought the object."""
    byArtist: NamedNode
    """The artist that performed this album or recording."""
    byDay: NamedNode
    """Defines the day(s) of the week on which a recurring [[Event]] takes place. May be specified using either [[DayOfWeek]], or alternatively [[Text]] conforming to iCal's syntax for byDay recurrence rules."""
    byMonth: NamedNode
    """Defines the month(s) of the year on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-12. January is 1."""
    byMonthDay: NamedNode
    """Defines the day(s) of the month on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-31."""
    byMonthWeek: NamedNode
    """Defines the week(s) of the month on which a recurring Event takes place. Specified as an Integer between 1-5. For clarity, byMonthWeek is best used in conjunction with byDay to indicate concepts like the first and third Mondays of a month."""
    callSign: NamedNode
    """A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles."""
    calories: NamedNode
    """The number of calories."""
    candidate: NamedNode
    """A sub property of object. The candidate subject of this action."""
    caption: NamedNode
    """The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]]."""
    carbohydrateContent: NamedNode
    """The number of grams of carbohydrates."""
    cargoVolume: NamedNode
    """The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.\n\nTypical unit code(s): LTR for liters, FTQ for cubic foot/feet\n\nNote: You can use [[minValue]] and [[maxValue]] to indicate ranges."""
    carrier: NamedNode
    """'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights."""
    carrierRequirements: NamedNode
    """Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network)."""
    cashBack: NamedNode
    """A cardholder benefit that pays the cardholder a small percentage of their net expenditures."""
    catalog: NamedNode
    """A data catalog which contains this dataset."""
    catalogNumber: NamedNode
    """The catalog number for the release."""
    category: NamedNode
    """A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy."""
    causeOf: NamedNode
    """The condition, complication, symptom, sign, etc. caused."""
    ccRecipient: NamedNode
    """A sub property of recipient. The recipient copied on a message."""
    certificationIdentification: NamedNode
    """Identifier of a certification instance (as registered with an independent certification body). Typically this identifier can be used to consult and verify the certification instance. See also [gs1:certificationIdentification](https://www.gs1.org/voc/certificationIdentification)."""
    certificationRating: NamedNode
    """Rating of a certification instance (as defined by an independent certification body). Typically this rating can be used to rate the level to which the requirements of the certification instance are fulfilled. See also [gs1:certificationValue](https://www.gs1.org/voc/certificationValue)."""
    certificationStatus: NamedNode
    """Indicates the current status of a certification: active or inactive. See also  [gs1:certificationStatus](https://www.gs1.org/voc/certificationStatus)."""
    character: NamedNode
    """Fictional person connected with a creative work."""
    characterAttribute: NamedNode
    """A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage)."""
    characterName: NamedNode
    """The name of a character played in some acting or performing role, i.e. in a PerformanceRole."""
    cheatCode: NamedNode
    """Cheat codes to the game."""
    checkinTime: NamedNode
    """The earliest someone may check into a lodging establishment."""
    checkoutPageURLTemplate: NamedNode
    """A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here."""
    checkoutTime: NamedNode
    """The latest someone may check out of a lodging establishment."""
    chemicalComposition: NamedNode
    """The chemical composition describes the identity and relative ratio of the chemical elements that make up the substance."""
    chemicalRole: NamedNode
    """A role played by the BioChemEntity within a chemical context."""
    childMaxAge: NamedNode
    """Maximal age of the child."""
    childMinAge: NamedNode
    """Minimal age of the child."""
    childTaxon: NamedNode
    """Closest child taxa of the taxon in question."""
    children: NamedNode
    """A child of the person."""
    cholesterolContent: NamedNode
    """The number of milligrams of cholesterol."""
    circle: NamedNode
    """A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters."""
    citation: NamedNode
    """A citation or reference to another creative work, such as another publication, web page, scholarly article, etc."""
    claimInterpreter: NamedNode
    """For a [[Claim]] interpreted from [[MediaObject]] content, the [[interpretedAsClaim]] property can be used to indicate a claim contained, implied or refined from the content of a [[MediaObject]]."""
    claimReviewed: NamedNode
    """A short summary of the specific claims reviewed in a ClaimReview."""
    clincalPharmacology: NamedNode
    """Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD)."""
    clinicalPharmacology: NamedNode
    """Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD)."""
    clipNumber: NamedNode
    """Position of the clip within an ordered group of clips."""
    closes: NamedNode
    """The closing hour of the place or service on the given day(s) of the week."""
    coach: NamedNode
    """A person that acts in a coaching role for a sports team."""
    code: NamedNode
    """A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc."""
    codeRepository: NamedNode
    """Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex)."""
    codeSampleType: NamedNode
    """What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template."""
    codeValue: NamedNode
    """A short textual code that uniquely identifies the value."""
    codingSystem: NamedNode
    """The coding system, e.g. 'ICD-10'."""
    colleague: NamedNode
    """A colleague of the person."""
    colleagues: NamedNode
    """A colleague of the person."""
    collection: NamedNode
    """A sub property of object. The collection target of the action."""
    collectionSize: NamedNode
    """The number of items in the [[Collection]]."""
    color: NamedNode
    """The color of the product."""
    colorSwatch: NamedNode
    """A color swatch image, visualizing the color of a [[Product]]. Should match the textual description specified in the [[color]] property. This can be a URL or a fully described ImageObject."""
    colorist: NamedNode
    """The individual who adds color to inked drawings."""
    comment: NamedNode
    """Comments, typically from users."""
    commentCount: NamedNode
    """The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere."""
    commentText: NamedNode
    """The text of the UserComment."""
    commentTime: NamedNode
    """The time at which the UserComment was made."""
    competencyRequired: NamedNode
    """Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource."""
    competitor: NamedNode
    """A competitor in a sports event."""
    composer: NamedNode
    """The person or organization who wrote a composition, or who is the composer of a work performed at some event."""
    comprisedOf: NamedNode
    """Specifying something physically contained by something else. Typically used here for the underlying anatomical structures, such as organs, that comprise the anatomical system."""
    conditionsOfAccess: NamedNode
    """Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]. This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.\n\nFor example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ". """
    confirmationNumber: NamedNode
    """A number that confirms the given order or payment has been received."""
    connectedTo: NamedNode
    """Other anatomical structures to which this structure is connected."""
    constraintProperty: NamedNode
    """Indicates a property used as a constraint. For example, in the definition of a [[StatisticalVariable]]. The value is a property, either from within Schema.org or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org. """
    contactOption: NamedNode
    """An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)."""
    contactPoint: NamedNode
    """A contact point for a person or organization."""
    contactPoints: NamedNode
    """A contact point for a person or organization."""
    contactType: NamedNode
    """A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point."""
    contactlessPayment: NamedNode
    """A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology."""
    containedIn: NamedNode
    """The basic containment relation between a place and one that contains it."""
    containedInPlace: NamedNode
    """The basic containment relation between a place and one that contains it."""
    containsPlace: NamedNode
    """The basic containment relation between a place and another that it contains."""
    containsSeason: NamedNode
    """A season that is part of the media series."""
    contentLocation: NamedNode
    """The location depicted or described in the content. For example, the location in a photograph or painting."""
    contentRating: NamedNode
    """Official rating of a piece of content&#x2014;for example, 'MPAA PG-13'."""
    contentReferenceTime: NamedNode
    """The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event."""
    contentSize: NamedNode
    """File size in (mega/kilo)bytes."""
    contentType: NamedNode
    """The supported content type(s) for an EntryPoint response."""
    contentUrl: NamedNode
    """Actual bytes of the media object, for example the image file or video file."""
    contraindication: NamedNode
    """A contraindication for this therapy."""
    contributor: NamedNode
    """A secondary contributor to the CreativeWork or Event."""
    cookTime: NamedNode
    """The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)."""
    cookingMethod: NamedNode
    """The method of cooking, such as Frying, Steaming, ..."""
    copyrightHolder: NamedNode
    """The party holding the legal copyright to the CreativeWork."""
    copyrightNotice: NamedNode
    """Text of a notice appropriate for describing the copyright aspects of this Creative Work, ideally indicating the owner of the copyright for the Work."""
    copyrightYear: NamedNode
    """The year during which the claimed copyright for the CreativeWork was first asserted."""
    correction: NamedNode
    """Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]], textually or in another document."""
    correctionsPolicy: NamedNode
    """For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors."""
    costCategory: NamedNode
    """The category of cost, such as wholesale, retail, reimbursement cap, etc."""
    costCurrency: NamedNode
    """The currency (in 3-letter) of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217. """
    costOrigin: NamedNode
    """Additional details to capture the origin of the cost data. For example, 'Medicare Part B'."""
    costPerUnit: NamedNode
    """The cost per unit of the drug."""
    countriesNotSupported: NamedNode
    """Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code."""
    countriesSupported: NamedNode
    """Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code."""
    countryOfAssembly: NamedNode
    """The place where the product was assembled."""
    countryOfLastProcessing: NamedNode
    """The place where the item (typically [[Product]]) was last processed and tested before importation."""
    countryOfOrigin: NamedNode
    """The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here."""
    course: NamedNode
    """A sub property of location. The course where this action was taken."""
    courseCode: NamedNode
    """The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001)."""
    courseMode: NamedNode
    """The medium or means of delivery of the course instance or the mode of study, either as a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or as a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous)."""
    coursePrerequisites: NamedNode
    """Requirements for taking the Course. May be completion of another [[Course]] or a textual description like "permission of instructor". Requirements may be a pre-requisite competency, referenced using [[AlignmentObject]]."""
    courseSchedule: NamedNode
    """Represents the length and pace of a course, expressed as a [[Schedule]]."""
    courseWorkload: NamedNode
    """The amount of work expected of students taking the course, often provided as a figure per week or per month, and may be broken down by type. For example, "2 hours of lectures, 1 hour of lab work and 3 hours of independent study per week"."""
    coverageEndTime: NamedNode
    """The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes."""
    coverageStartTime: NamedNode
    """The time when the live blog will begin covering the Event. Note that coverage may begin before the Event's start time. The LiveBlogPosting may also be created before coverage begins."""
    creativeWorkStatus: NamedNode
    """The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle."""
    creator: NamedNode
    """The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork."""
    credentialCategory: NamedNode
    """The category or type of credential being described, for example "degree”, “certificate”, “badge”, or more specific term."""
    creditText: NamedNode
    """Text that can be used to credit person(s) and/or organization(s) associated with a published Creative Work."""
    creditedTo: NamedNode
    """The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga."""
    cssSelector: NamedNode
    """A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element"."""
    currenciesAccepted: NamedNode
    """The currency accepted.\n\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR"."""
    currency: NamedNode
    """The currency in which the monetary amount is expressed.\n\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR"."""
    currentExchangeRate: NamedNode
    """The current price of a currency."""
    customer: NamedNode
    """Party placing the order or paying the invoice."""
    customerRemorseReturnFees: NamedNode
    """The type of return fees if the product is returned due to customer remorse."""
    customerRemorseReturnLabelSource: NamedNode
    """The method (from an enumeration) by which the customer obtains a return shipping label for a product returned due to customer remorse."""
    customerRemorseReturnShippingFeesAmount: NamedNode
    """The amount of shipping costs if a product is returned due to customer remorse. Applicable when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]]."""
    cutoffTime: NamedNode
    """Order cutoff time allows merchants to describe the time after which they will no longer process orders received on that day. For orders processed after cutoff time, one day gets added to the delivery time estimate. This property is expected to be most typically used via the [[ShippingRateSettings]] publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC)."""
    cvdCollectionDate: NamedNode
    """collectiondate - Date for which patient counts are reported."""
    cvdFacilityCounty: NamedNode
    """Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]] to identify the facility. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry."""
    cvdFacilityId: NamedNode
    """Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]] to indicate the county. To provide other details, [[healthcareReportingData]] can be used on a [[Hospital]] entry."""
    cvdNumBeds: NamedNode
    """numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed, and overflow (surge) beds used for inpatients."""
    cvdNumBedsOcc: NamedNode
    """numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds that are occupied."""
    cvdNumC19Died: NamedNode
    """numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital, ED, or any overflow location."""
    cvdNumC19HOPats: NamedNode
    """numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location with onset of suspected or confirmed COVID-19 14 or more days after hospitalization."""
    cvdNumC19HospPats: NamedNode
    """numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care location who have suspected or confirmed COVID-19."""
    cvdNumC19MechVentPats: NamedNode
    """numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical ventilator."""
    cvdNumC19OFMechVentPats: NamedNode
    """numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical ventilator."""
    cvdNumC19OverflowPats: NamedNode
    """numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19 who are in the ED or any overflow location awaiting an inpatient bed."""
    cvdNumICUBeds: NamedNode
    """numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds."""
    cvdNumICUBedsOcc: NamedNode
    """numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are occupied."""
    cvdNumTotBeds: NamedNode
    """numtotbeds - ALL HOSPITAL BEDS: Total number of all inpatient and outpatient beds, including all staffed, ICU, licensed, and overflow (surge) beds used for inpatients or outpatients."""
    cvdNumVent: NamedNode
    """numvent - MECHANICAL VENTILATORS: Total number of ventilators available."""
    cvdNumVentUse: NamedNode
    """numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use."""
    dataFeedElement: NamedNode
    """An item within a data feed. Data feeds may have many elements."""
    dataset: NamedNode
    """A dataset contained in this catalog."""
    datasetTimeInterval: NamedNode
    """The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format)."""
    dateCreated: NamedNode
    """The date on which the CreativeWork was created or the item was added to a DataFeed."""
    dateDeleted: NamedNode
    """The datetime the item was removed from the DataFeed."""
    dateIssued: NamedNode
    """The date the ticket was issued."""
    dateModified: NamedNode
    """The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed."""
    datePosted: NamedNode
    """Publication date of an online listing."""
    datePublished: NamedNode
    """Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued."""
    dateRead: NamedNode
    """The date/time at which the message has been read by the recipient if a single recipient exists."""
    dateReceived: NamedNode
    """The date/time the message was received if a single recipient exists."""
    dateSent: NamedNode
    """The date/time at which the message was sent."""
    dateVehicleFirstRegistered: NamedNode
    """The date of the first registration of the vehicle with the respective public authorities."""
    dateline: NamedNode
    """A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included in news articles that describes where and when the story was written or filed though the date is often omitted. Sometimes only a placename is provided.

Structured representations of dateline-related information can also be expressed more explicitly using [[locationCreated]] (which represents where a work was created, e.g. where a news report was written).  For location depicted or described in the content, use [[contentLocation]].

Dateline summaries are oriented more towards human readers than towards automated processing, and can vary substantially. Some examples: "BEIRUT, Lebanon, June 2.", "Paris, France", "December 19, 2017 11:43AM Reporting from Washington", "Beijing/Moscow", "QUEZON CITY, Philippines".
      """
    dayOfWeek: NamedNode
    """The day of the week for which these opening hours are valid."""
    deathDate: NamedNode
    """Date of death."""
    deathPlace: NamedNode
    """The place where the person died."""
    defaultValue: NamedNode
    """The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values."""
    deliveryAddress: NamedNode
    """Destination address."""
    deliveryLeadTime: NamedNode
    """The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup."""
    deliveryMethod: NamedNode
    """A sub property of instrument. The method of delivery."""
    deliveryStatus: NamedNode
    """New entry added as the package passes through each leg of its journey (from shipment to final delivery)."""
    deliveryTime: NamedNode
    """The total delay between the receipt of the order and the goods reaching the final customer."""
    department: NamedNode
    """A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe."""
    departureAirport: NamedNode
    """The airport where the flight originates."""
    departureBoatTerminal: NamedNode
    """The terminal or port from which the boat departs."""
    departureBusStop: NamedNode
    """The stop or station from which the bus departs."""
    departureGate: NamedNode
    """Identifier of the flight's departure gate."""
    departurePlatform: NamedNode
    """The platform from which the train departs."""
    departureStation: NamedNode
    """The station from which the train departs."""
    departureTerminal: NamedNode
    """Identifier of the flight's departure terminal."""
    departureTime: NamedNode
    """The expected departure time."""
    dependencies: NamedNode
    """Prerequisites needed to fulfill steps in article."""
    depth: NamedNode
    """The depth of the item."""
    description: NamedNode
    """A description of the item."""
    device: NamedNode
    """Device required to run the application. Used in cases where a specific make/model is required to run the application."""
    diagnosis: NamedNode
    """One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process."""
    diagram: NamedNode
    """An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures."""
    diet: NamedNode
    """A sub property of instrument. The diet used in this action."""
    dietFeatures: NamedNode
    """Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body's approved dietary guidelines."""
    differentialDiagnosis: NamedNode
    """One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient."""
    digitalSourceType: NamedNode
    """Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some [[CreativeWork]]."""
    directApply: NamedNode
    """Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct application for the job, via the posting website. A job posting is considered to have directApply of [[True]] if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of [[False]] is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied."""
    director: NamedNode
    """A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip."""
    directors: NamedNode
    """A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip."""
    disambiguatingDescription: NamedNode
    """A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation."""
    discount: NamedNode
    """Any discount applied (to an Order)."""
    discountCode: NamedNode
    """Code used to redeem a discount."""
    discountCurrency: NamedNode
    """The currency of the discount.\n\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR"."""
    discusses: NamedNode
    """Specifies the CreativeWork associated with the UserComment."""
    discussionUrl: NamedNode
    """A link to the page containing the comments of the CreativeWork."""
    diseasePreventionInfo: NamedNode
    """Information about disease prevention."""
    diseaseSpreadStatistics: NamedNode
    """Statistical information about the spread of a disease, either as [[WebContent]], or
  described directly as a [[Dataset]], or the specific [[Observation]]s in the dataset. When a [[WebContent]] URL is
  provided, the page indicated might also contain more such markup."""
    dissolutionDate: NamedNode
    """The date that this organization was dissolved."""
    distance: NamedNode
    """The distance travelled, e.g. exercising or travelling."""
    distinguishingSign: NamedNode
    """One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis."""
    distribution: NamedNode
    """A downloadable form of this dataset, at a specific location, in a specific format. This property can be repeated if different variations are available. There is no expectation that different downloadable distributions must contain exactly equivalent information (see also [DCAT](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution) on this point). Different distributions might include or exclude different subsets of the entire dataset, for example."""
    diversityPolicy: NamedNode
    """Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data."""
    diversityStaffingReport: NamedNode
    """For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported."""
    documentation: NamedNode
    """Further documentation describing the Web API in more detail."""
    doesNotShip: NamedNode
    """Indicates when shipping to a particular [[shippingDestination]] is not available."""
    domainIncludes: NamedNode
    """Relates a property to a class that is (one of) the type(s) the property is expected to be used on."""
    domiciledMortgage: NamedNode
    """Whether borrower is a resident of the jurisdiction where the property is located."""
    doorTime: NamedNode
    """The time admission will commence."""
    dosageForm: NamedNode
    """A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'."""
    doseSchedule: NamedNode
    """A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used."""
    doseUnit: NamedNode
    """The unit of the dose, e.g. 'mg'."""
    doseValue: NamedNode
    """The value of the dose, e.g. 500."""
    downPayment: NamedNode
    """a type of payment made in cash during the onset of the purchase of an expensive good/service. The payment typically represents only a percentage of the full purchase price."""
    downloadUrl: NamedNode
    """If the file can be downloaded, URL to download the binary."""
    downvoteCount: NamedNode
    """The number of downvotes this question, answer or comment has received from the community."""
    drainsTo: NamedNode
    """The vasculature that the vein drains into."""
    driveWheelConfiguration: NamedNode
    """The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain."""
    dropoffLocation: NamedNode
    """Where a rental car can be dropped off."""
    dropoffTime: NamedNode
    """When a rental car can be dropped off."""
    drug: NamedNode
    """Specifying a drug or medicine used in a medication procedure."""
    drugClass: NamedNode
    """The class of drug this belongs to (e.g., statins)."""
    drugUnit: NamedNode
    """The unit in which the drug is measured, e.g. '5 mg tablet'."""
    duns: NamedNode
    """The Dun & Bradstreet DUNS number for identifying an organization or business person."""
    duplicateTherapy: NamedNode
    """A therapy that duplicates or overlaps this one."""
    duration: NamedNode
    """The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)."""
    durationOfWarranty: NamedNode
    """The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days."""
    duringMedia: NamedNode
    """A media object representing the circumstances while performing this direction."""
    earlyPrepaymentPenalty: NamedNode
    """The amount to be paid as a penalty in the event of early payment of the loan."""
    editEIDR: NamedNode
    """An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing a specific edit / edition for a work of film or television.

For example, the motion picture known as "Ghostbusters" whose [[titleEIDR]] is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".

Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
"""
    editor: NamedNode
    """Specifies the Person who edited the CreativeWork."""
    eduQuestionType: NamedNode
    """For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard"."""
    educationRequirements: NamedNode
    """Educational background needed for the position or Occupation."""
    educationalAlignment: NamedNode
    """An alignment to an established educational framework.

This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency."""
    educationalCredentialAwarded: NamedNode
    """A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program."""
    educationalFramework: NamedNode
    """The framework to which the resource being described is aligned."""
    educationalLevel: NamedNode
    """The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators."""
    educationalProgramMode: NamedNode
    """Similar to courseMode, the medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous )."""
    educationalRole: NamedNode
    """An educationalRole of an EducationalAudience."""
    educationalUse: NamedNode
    """The purpose of a work in the context of education; for example, 'assignment', 'group work'."""
    elevation: NamedNode
    """The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT_OF_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters."""
    eligibilityToWorkRequirement: NamedNode
    """The legal requirements such as citizenship, visa and other documentation required for an applicant to this job."""
    eligibleCustomerType: NamedNode
    """The type(s) of customers for which the given offer is valid."""
    eligibleDuration: NamedNode
    """The duration for which the given offer is valid."""
    eligibleQuantity: NamedNode
    """The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity."""
    eligibleRegion: NamedNode
    """The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\n\nSee also [[ineligibleRegion]].
    """
    eligibleTransactionVolume: NamedNode
    """The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount."""
    email: NamedNode
    """Email address."""
    embedUrl: NamedNode
    """A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag."""
    embeddedTextCaption: NamedNode
    """Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'."""
    emissionsCO2: NamedNode
    """The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km"."""
    employee: NamedNode
    """Someone working for this organization."""
    employees: NamedNode
    """People working for this organization."""
    employerOverview: NamedNode
    """A description of the employer, career opportunities and work environment for this position."""
    employmentType: NamedNode
    """Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship)."""
    employmentUnit: NamedNode
    """Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed."""
    encodesBioChemEntity: NamedNode
    """Another BioChemEntity encoded by this one. """
    encodesCreativeWork: NamedNode
    """The CreativeWork encoded by this media object."""
    encoding: NamedNode
    """A media object that encodes this CreativeWork. This property is a synonym for associatedMedia."""
    encodingFormat: NamedNode
    """Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.

In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry."""
    encodingType: NamedNode
    """The supported encoding type(s) for an EntryPoint request."""
    encodings: NamedNode
    """A media object that encodes this CreativeWork."""
    endDate: NamedNode
    """The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601))."""
    endOffset: NamedNode
    """The end time of the clip expressed as the number of seconds from the beginning of the work."""
    endTime: NamedNode
    """The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.\n\nNote that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."""
    endorsee: NamedNode
    """A sub property of participant. The person/organization being supported."""
    endorsers: NamedNode
    """People or organizations that endorse the plan."""
    energyEfficiencyScaleMax: NamedNode
    """Specifies the most energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++."""
    energyEfficiencyScaleMin: NamedNode
    """Specifies the least energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++."""
    engineDisplacement: NamedNode
    """The volume swept by all of the pistons inside the cylinders of an internal combustion engine in a single movement. \n\nTypical unit code(s): CMQ for cubic centimeter, LTR for liters, INQ for cubic inches\n* Note 1: You can link to information about how the given value has been determined using the [[valueReference]] property.\n* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges."""
    enginePower: NamedNode
    """The power of the vehicle's engine.
    Typical unit code(s): KWT for kilowatt, BHP for brake horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W)\n\n* Note 1: There are many different ways of measuring an engine's power. For an overview, see  [http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes).\n* Note 2: You can link to information about how the given value has been determined using the [[valueReference]] property.\n* Note 3: You can use [[minValue]] and [[maxValue]] to indicate ranges."""
    engineType: NamedNode
    """The type of engine or engines powering the vehicle."""
    entertainmentBusiness: NamedNode
    """A sub property of location. The entertainment business where the action occurred."""
    epidemiology: NamedNode
    """The characteristics of associated patients, such as age, gender, race etc."""
    episode: NamedNode
    """An episode of a TV, radio or game media within a series or season."""
    episodeNumber: NamedNode
    """Position of the episode within an ordered group of episodes."""
    episodes: NamedNode
    """An episode of a TV/radio series or season."""
    equal: NamedNode
    """This ordering relation for qualitative values indicates that the subject is equal to the object."""
    error: NamedNode
    """For failed actions, more information on the cause of the failure."""
    estimatedCost: NamedNode
    """The estimated cost of the supply or supplies consumed when performing instructions."""
    estimatedFlightDuration: NamedNode
    """The estimated time the flight will take."""
    estimatedSalary: NamedNode
    """An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value."""
    estimatesRiskOf: NamedNode
    """The condition, complication, or symptom whose risk is being estimated."""
    ethicsPolicy: NamedNode
    """Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization."""
    event: NamedNode
    """Upcoming or past event associated with this place, organization, or action."""
    eventAttendanceMode: NamedNode
    """The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix."""
    eventSchedule: NamedNode
    """Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable to share a schedule for a series of
      repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly
      gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An [[Event]] that
      is associated with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]] properties. These are instead defined within the associated
      [[Schedule]], this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months
      or seasons."""
    eventStatus: NamedNode
    """An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled."""
    events: NamedNode
    """Upcoming or past events associated with this place or organization."""
    evidenceLevel: NamedNode
    """Strength of evidence of the data used to formulate the guideline (enumerated)."""
    evidenceOrigin: NamedNode
    """Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc."""
    exampleOfWork: NamedNode
    """A creative work that this work is an example/instance/realization/derivation of."""
    exceptDate: NamedNode
    """Defines a [[Date]] or [[DateTime]] during which a scheduled [[Event]] will not take place. The property allows exceptions to
      a [[Schedule]] to be specified. If an exception is specified as a [[DateTime]] then only the event that would have started at that specific date and time
      should be excluded from the schedule. If an exception is specified as a [[Date]] then any event that is scheduled for that 24 hour period should be
      excluded from the schedule. This allows a whole day to be excluded from the schedule without having to itemise every scheduled event."""
    exchangeRateSpread: NamedNode
    """The difference between the price at which a broker or other intermediary buys and sells foreign currency."""
    executableLibraryName: NamedNode
    """Library file name, e.g., mscorlib.dll, system.web.dll."""
    exerciseCourse: NamedNode
    """A sub property of location. The course where this action was taken."""
    exercisePlan: NamedNode
    """A sub property of instrument. The exercise plan used on this action."""
    exerciseRelatedDiet: NamedNode
    """A sub property of instrument. The diet used in this action."""
    exerciseType: NamedNode
    """Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc."""
    exifData: NamedNode
    """exif data for this object."""
    expectedArrivalFrom: NamedNode
    """The earliest date the package may arrive."""
    expectedArrivalUntil: NamedNode
    """The latest date the package may arrive."""
    expectedPrognosis: NamedNode
    """The likely outcome in either the short term or long term of the medical condition."""
    expectsAcceptanceOf: NamedNode
    """An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."""
    experienceInPlaceOfEducation: NamedNode
    """Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]]) in place of its formal educational qualifications (as indicated by [[educationRequirements]]). If true, indicates that satisfying one of these requirements is sufficient."""
    experienceRequirements: NamedNode
    """Description of skills and experience needed for the position or Occupation."""
    expertConsiderations: NamedNode
    """Medical expert advice related to the plan."""
    expires: NamedNode
    """Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a [[Certification]] the validity has expired."""
    expressedIn: NamedNode
    """Tissue, organ, biological sample, etc in which activity of this gene has been observed experimentally. For example brain, digestive system."""
    familyName: NamedNode
    """Family name. In the U.S., the last name of a Person."""
    fatContent: NamedNode
    """The number of grams of fat."""
    faxNumber: NamedNode
    """The fax number."""
    featureList: NamedNode
    """Features or modules provided by this application (and possibly required by other applications)."""
    feesAndCommissionsSpecification: NamedNode
    """Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization."""
    fiberContent: NamedNode
    """The number of grams of fiber."""
    fileFormat: NamedNode
    """Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)) of the content, e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry."""
    fileSize: NamedNode
    """Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed."""
    financialAidEligible: NamedNode
    """A financial aid type or program which students may use to pay for tuition or fees associated with the program."""
    firstAppearance: NamedNode
    """Indicates the first known occurrence of a [[Claim]] in some [[CreativeWork]]."""
    firstPerformance: NamedNode
    """The date and place the work was first performed."""
    flightDistance: NamedNode
    """The distance of the flight."""
    flightNumber: NamedNode
    """The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'."""
    floorLevel: NamedNode
    """The floor level for an [[Accommodation]] in a multi-storey building. Since counting
  systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible."""
    floorLimit: NamedNode
    """A floor limit is the amount of money above which credit card transactions must be authorized."""
    floorSize: NamedNode
    """The size of the accommodation, e.g. in square meter or squarefoot.
Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard."""
    followee: NamedNode
    """A sub property of object. The person or organization being followed."""
    follows: NamedNode
    """The most generic uni-directional social relation."""
    followup: NamedNode
    """Typical or recommended followup care after the procedure is performed."""
    foodEstablishment: NamedNode
    """A sub property of location. The specific food establishment where the action occurred."""
    foodEvent: NamedNode
    """A sub property of location. The specific food event where the action occurred."""
    foodWarning: NamedNode
    """Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug."""
    founder: NamedNode
    """A person or organization who founded this organization."""
    founders: NamedNode
    """A person who founded this organization."""
    foundingDate: NamedNode
    """The date that this organization was founded."""
    foundingLocation: NamedNode
    """The place where the Organization was founded."""
    free: NamedNode
    """A flag to signal that the item, event, or place is accessible for free."""
    freeShippingThreshold: NamedNode
    """A monetary value above (or at) which the shipping rate becomes free. Intended to be used via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]]."""
    frequency: NamedNode
    """How often the dose is taken, e.g. 'daily'."""
    fromLocation: NamedNode
    """A sub property of location. The original location of the object or the agent before the action."""
    fuelCapacity: NamedNode
    """The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.\n\nTypical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles)."""
    fuelConsumption: NamedNode
    """The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).\n\n* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.\n* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\n* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value."""
    fuelEfficiency: NamedNode
    """The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).\n\n* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.\n* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\n* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value."""
    fuelType: NamedNode
    """The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle."""
    functionalClass: NamedNode
    """The degree of mobility the joint allows."""
    fundedItem: NamedNode
    """Indicates something directly or indirectly funded or sponsored through a [[Grant]]. See also [[ownershipFundingInfo]]."""
    funder: NamedNode
    """A person or organization that supports (sponsors) something through some kind of financial contribution."""
    funding: NamedNode
    """A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]]."""
    game: NamedNode
    """Video game which is played on this server."""
    gameAvailabilityType: NamedNode
    """Indicates the availability type of the game content associated with this action, such as whether it is a full version or a demo."""
    gameEdition: NamedNode
    """The edition of a video game."""
    gameItem: NamedNode
    """An item is an object within the game world that can be collected by a player or, occasionally, a non-player character."""
    gameLocation: NamedNode
    """Real or fictional location of the game (or part of game)."""
    gamePlatform: NamedNode
    """The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>."""
    gameServer: NamedNode
    """The server on which  it is possible to play the game."""
    gameTip: NamedNode
    """Links to tips, tactics, etc."""
    gender: NamedNode
    """Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed"."""
    genre: NamedNode
    """Genre of the creative work, broadcast channel or group."""
    geo: NamedNode
    """The geo coordinates of the place."""
    geoContains: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoCoveredBy: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoCovers: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoCrosses: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoDisjoint: NamedNode
    """Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)"""
    geoEquals: NamedNode
    """Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship)."""
    geoIntersects: NamedNode
    """Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoMidpoint: NamedNode
    """Indicates the GeoCoordinates at the centre of a GeoShape, e.g. GeoCircle."""
    geoOverlaps: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geoRadius: NamedNode
    """Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation)."""
    geoTouches: NamedNode
    """Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)"""
    geoWithin: NamedNode
    """Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."""
    geographicArea: NamedNode
    """The geographic area associated with the audience."""
    gettingTestedInfo: NamedNode
    """Information about getting tested (for a [[MedicalCondition]]), e.g. in the context of a pandemic."""
    givenName: NamedNode
    """Given name. In the U.S., the first name of a Person."""
    globalLocationNumber: NamedNode
    """The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations."""
    governmentBenefitsInfo: NamedNode
    """governmentBenefitsInfo provides information about government benefits associated with a SpecialAnnouncement."""
    gracePeriod: NamedNode
    """The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred."""
    grantee: NamedNode
    """The person, organization, contact point, or audience that has been granted this permission."""
    greater: NamedNode
    """This ordering relation for qualitative values indicates that the subject is greater than the object."""
    greaterOrEqual: NamedNode
    """This ordering relation for qualitative values indicates that the subject is greater than or equal to the object."""
    gtin: NamedNode
    """A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.

A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.

The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.).
Digital Links should be populated into the [[hasGS1DigitalLink]] attribute.

Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details."""
    gtin12: NamedNode
    """The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details."""
    gtin13: NamedNode
    """The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details."""
    gtin14: NamedNode
    """The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details."""
    gtin8: NamedNode
    """The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details."""
    guideline: NamedNode
    """A medical guideline related to this entity."""
    guidelineDate: NamedNode
    """Date on which this guideline's recommendation was made."""
    guidelineSubject: NamedNode
    """The medical conditions, treatments, etc. that are the subject of the guideline."""
    handlingTime: NamedNode
    """The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup. Typical properties: minValue, maxValue, unitCode (d for DAY).  This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates."""
    hasAdultConsideration: NamedNode
    """Used to tag an item to be intended or suitable for consumption or use by adults only."""
    hasBioChemEntityPart: NamedNode
    """Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part. """
    hasBioPolymerSequence: NamedNode
    """A symbolic representation of a BioChemEntity. For example, a nucleotide sequence of a Gene or an amino acid sequence of a Protein."""
    hasBroadcastChannel: NamedNode
    """A broadcast channel of a broadcast service."""
    hasCategoryCode: NamedNode
    """A Category code contained in this code set."""
    hasCertification: NamedNode
    """Certification information about a product, organization, service, place, or person."""
    hasCourse: NamedNode
    """A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program."""
    hasCourseInstance: NamedNode
    """An offering of the course at a specific time and place or through specific media or mode of study or to a specific section of students."""
    hasCredential: NamedNode
    """A credential awarded to the Person or Organization."""
    hasDefinedTerm: NamedNode
    """A Defined Term contained in this term set."""
    hasDeliveryMethod: NamedNode
    """Method used for delivery or shipping."""
    hasDigitalDocumentPermission: NamedNode
    """A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public"."""
    hasDriveThroughService: NamedNode
    """Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users."""
    hasEnergyConsumptionDetails: NamedNode
    """Defines the energy efficiency Category (also known as "class" or "rating") for a product according to an international energy efficiency standard."""
    hasEnergyEfficiencyCategory: NamedNode
    """Defines the energy efficiency Category (which could be either a rating out of range of values or a yes/no certification) for a product according to an international energy efficiency standard."""
    hasGS1DigitalLink: NamedNode
    """The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>)  should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly."""
    hasHealthAspect: NamedNode
    """Indicates the aspect or aspects specifically addressed in some [[HealthTopicContent]]. For example, that the content is an overview, or that it talks about treatment, self-care, treatments or their side-effects."""
    hasMap: NamedNode
    """A URL to a map of the place."""
    hasMeasurement: NamedNode
    """A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings."""
    hasMemberProgram: NamedNode
    """MemberProgram offered by an Organization, for example an eCommerce merchant or an airline."""
    hasMenu: NamedNode
    """Either the actual menu as a structured representation, as text, or a URL of the menu."""
    hasMenuItem: NamedNode
    """A food or drink item contained in a menu or menu section."""
    hasMenuSection: NamedNode
    """A subgrouping of the menu (by dishes, course, serving time period, etc.)."""
    hasMerchantReturnPolicy: NamedNode
    """Specifies a MerchantReturnPolicy that may be applicable."""
    hasMolecularFunction: NamedNode
    """Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence."""
    hasOccupation: NamedNode
    """The Person's occupation. For past professions, use Role for expressing dates."""
    hasOfferCatalog: NamedNode
    """Indicates an OfferCatalog listing for this Organization, Person, or Service."""
    hasPOS: NamedNode
    """Points-of-Sales operated by the organization or person."""
    hasPart: NamedNode
    """Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense)."""
    hasProductReturnPolicy: NamedNode
    """Indicates a ProductReturnPolicy that may be applicable."""
    hasRepresentation: NamedNode
    """A common representation such as a protein sequence or chemical structure for this entity. For images use schema.org/image."""
    hasTierBenefit: NamedNode
    """A member benefit for a particular tier of a loyalty program."""
    hasTierRequirement: NamedNode
    """A requirement for a user to join a membership tier, for example: a CreditCard if the tier requires sign up for a credit card, A UnitPriceSpecification if the user is required to pay a (periodic) fee, or a MonetaryAmount if the user needs to spend a minimum amount to join the tier. If a tier is free to join then this property does not need to be specified."""
    hasTiers: NamedNode
    """The tiers of a member program."""
    hasVariant: NamedNode
    """Indicates a [[Product]] that is a member of this [[ProductGroup]] (or [[ProductModel]])."""
    headline: NamedNode
    """Headline of the article."""
    healthCondition: NamedNode
    """Specifying the health condition(s) of a patient, medical study, or other target audience."""
    healthPlanCoinsuranceOption: NamedNode
    """Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed set?"""
    healthPlanCoinsuranceRate: NamedNode
    """The rate of coinsurance expressed as a number between 0.0 and 1.0."""
    healthPlanCopay: NamedNode
    """The copay amount."""
    healthPlanCopayOption: NamedNode
    """Whether the copay is before or after deductible, etc. TODO: Is this a closed set?"""
    healthPlanCostSharing: NamedNode
    """The costs to the patient for services under this network or formulary."""
    healthPlanDrugOption: NamedNode
    """TODO."""
    healthPlanDrugTier: NamedNode
    """The tier(s) of drugs offered by this formulary or insurance plan."""
    healthPlanId: NamedNode
    """The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across different markets.)"""
    healthPlanMarketingUrl: NamedNode
    """The URL that goes directly to the plan brochure for the specific standard plan or plan variation."""
    healthPlanNetworkId: NamedNode
    """Name or unique ID of network. (Networks are often reused across different insurance plans.)"""
    healthPlanNetworkTier: NamedNode
    """The tier(s) for this network."""
    healthPlanPharmacyCategory: NamedNode
    """The category or type of pharmacy associated with this cost sharing."""
    healthcareReportingData: NamedNode
    """Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of [[Dataset]]."""
    height: NamedNode
    """The height of the item."""
    highPrice: NamedNode
    """The highest price of all offers available.\n\nUsage guidelines:\n\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    hiringOrganization: NamedNode
    """Organization or Person offering the job position."""
    holdingArchive: NamedNode
    """[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]]."""
    homeLocation: NamedNode
    """A contact location for a person's residence."""
    homeTeam: NamedNode
    """The home team in a sports event."""
    honorificPrefix: NamedNode
    """An honorific prefix preceding a Person's name such as Dr/Mrs/Mr."""
    honorificSuffix: NamedNode
    """An honorific suffix following a Person's name such as M.D./PhD/MSCSW."""
    hospitalAffiliation: NamedNode
    """A hospital with which the physician or office is affiliated."""
    hostingOrganization: NamedNode
    """The Organization (airline, travelers' club, retailer, etc.) the membership is made with or which offers the  MemberProgram."""
    hoursAvailable: NamedNode
    """The hours during which this service or contact is available."""
    howPerformed: NamedNode
    """How the procedure is performed."""
    httpMethod: NamedNode
    """An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP."""
    iataCode: NamedNode
    """IATA identifier for an airline or airport."""
    icaoCode: NamedNode
    """ICAO identifier for an airport."""
    identifier: NamedNode
    """The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
        """
    identifyingExam: NamedNode
    """A physical examination that can identify this sign."""
    identifyingTest: NamedNode
    """A diagnostic test that can identify this sign."""
    illustrator: NamedNode
    """The illustrator of the book."""
    image: NamedNode
    """An image of the item. This can be a [[URL]] or a fully described [[ImageObject]]."""
    imagingTechnique: NamedNode
    """Imaging technique used."""
    inAlbum: NamedNode
    """The album to which this recording belongs."""
    inBroadcastLineup: NamedNode
    """The CableOrSatelliteService offering the channel."""
    inChI: NamedNode
    """Non-proprietary identifier for molecular entity that can be used in printed and electronic data sources thus enabling easier linking of diverse data compilations."""
    inChIKey: NamedNode
    """InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm)."""
    inCodeSet: NamedNode
    """A [[CategoryCodeSet]] that contains this category code."""
    inDefinedTermSet: NamedNode
    """A [[DefinedTermSet]] that contains this term."""
    inLanguage: NamedNode
    """The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]]."""
    inPlaylist: NamedNode
    """The playlist to which this recording belongs."""
    inProductGroupWithID: NamedNode
    """Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]]. """
    inStoreReturnsOffered: NamedNode
    """Are in-store returns offered? (For more advanced return methods use the [[returnMethod]] property.)"""
    inSupportOf: NamedNode
    """Qualification, candidature, degree, application that Thesis supports."""
    incentiveCompensation: NamedNode
    """Description of bonus and commission compensation aspects of the job."""
    incentives: NamedNode
    """Description of bonus and commission compensation aspects of the job."""
    includedComposition: NamedNode
    """Smaller compositions included in this work (e.g. a movement in a symphony)."""
    includedDataCatalog: NamedNode
    """A data catalog which contains this dataset (this property was previously 'catalog', preferred name is now 'includedInDataCatalog')."""
    includedInDataCatalog: NamedNode
    """A data catalog which contains this dataset."""
    includedInHealthInsurancePlan: NamedNode
    """The insurance plans that cover this drug."""
    includedRiskFactor: NamedNode
    """A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition."""
    includesAttraction: NamedNode
    """Attraction located at destination."""
    includesHealthPlanFormulary: NamedNode
    """Formularies covered by this plan."""
    includesHealthPlanNetwork: NamedNode
    """Networks covered by this plan."""
    includesObject: NamedNode
    """This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]]."""
    increasesRiskOf: NamedNode
    """The condition, complication, etc. influenced by this factor."""
    industry: NamedNode
    """The industry associated with the job position."""
    ineligibleRegion: NamedNode
    """The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\n\nSee also [[eligibleRegion]].
      """
    infectiousAgent: NamedNode
    """The actual infectious agent, such as a specific bacterium."""
    infectiousAgentClass: NamedNode
    """The class of infectious agent (bacteria, prion, etc.) that causes the disease."""
    ingredients: NamedNode
    """A single ingredient used in the recipe, e.g. sugar, flour or garlic."""
    inker: NamedNode
    """The individual who traces over the pencil drawings in ink after pencils are complete."""
    insertion: NamedNode
    """The place of attachment of a muscle, or what the muscle moves."""
    installUrl: NamedNode
    """URL at which the app may be installed, if different from the URL of the item."""
    instructor: NamedNode
    """A person assigned to instruct or provide instructional assistance for the [[CourseInstance]]."""
    instrument: NamedNode
    """The object that helped the agent perform the action. E.g. John wrote a book with *a pen*."""
    intensity: NamedNode
    """Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement."""
    interactingDrug: NamedNode
    """Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications."""
    interactionCount: NamedNode
    """This property is deprecated, alongside the UserInteraction types on which it depended."""
    interactionService: NamedNode
    """The WebSite or SoftwareApplication where the interactions took place."""
    interactionStatistic: NamedNode
    """The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used."""
    interactionType: NamedNode
    """The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]. For down votes use [[DislikeAction]]. Otherwise, use the most specific Action."""
    interactivityType: NamedNode
    """The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'."""
    interestRate: NamedNode
    """The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate."""
    interpretedAsClaim: NamedNode
    """Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]]."""
    inventoryLevel: NamedNode
    """The current approximate inventory level for the item or items."""
    inverseOf: NamedNode
    """Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the 'alumni' and 'alumniOf' properties are inverseOf each other. Some properties don't have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used."""
    isAcceptingNewPatients: NamedNode
    """Whether the provider is accepting new patients."""
    isAccessibleForFree: NamedNode
    """A flag to signal that the item, event, or place is accessible for free."""
    isAccessoryOrSparePartFor: NamedNode
    """A pointer to another product (or multiple products) for which this product is an accessory or spare part."""
    isAvailableGenerically: NamedNode
    """True if the drug is available in a generic form (regardless of name)."""
    isBasedOn: NamedNode
    """A resource from which this work is derived or from which it is a modification or adaptation."""
    isBasedOnUrl: NamedNode
    """A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html."""
    isConsumableFor: NamedNode
    """A pointer to another product (or multiple products) for which this product is a consumable."""
    isEncodedByBioChemEntity: NamedNode
    """Another BioChemEntity encoding by this one."""
    isFamilyFriendly: NamedNode
    """Indicates whether this content is family friendly."""
    isGift: NamedNode
    """Indicates whether the offer was accepted as a gift for someone other than the buyer."""
    isInvolvedInBiologicalProcess: NamedNode
    """Biological process this BioChemEntity is involved in; please use PropertyValue if you want to include any evidence."""
    isLiveBroadcast: NamedNode
    """True if the broadcast is of a live event."""
    isLocatedInSubcellularLocation: NamedNode
    """Subcellular location where this BioChemEntity is located; please use PropertyValue if you want to include any evidence."""
    isPartOf: NamedNode
    """Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of."""
    isPartOfBioChemEntity: NamedNode
    """Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity. """
    isPlanForApartment: NamedNode
    """Indicates some accommodation that this floor plan describes."""
    isProprietary: NamedNode
    """True if this item's name is a proprietary/brand name (vs. generic name)."""
    isRelatedTo: NamedNode
    """A pointer to another, somehow related product (or multiple products)."""
    isResizable: NamedNode
    """Whether the 3DModel allows resizing. For example, room layout applications often do not allow 3DModel elements to be resized to reflect reality."""
    isSimilarTo: NamedNode
    """A pointer to another, functionally similar product (or multiple products)."""
    isTierOf: NamedNode
    """The member program this tier is a part of."""
    isUnlabelledFallback: NamedNode
    """This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings."""
    isVariantOf: NamedNode
    """Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group."""
    isbn: NamedNode
    """The ISBN of the book."""
    isicV4: NamedNode
    """The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place."""
    iso6523Code: NamedNode
    """An organization identifier as defined in [ISO 6523(-1)](https://en.wikipedia.org/wiki/ISO/IEC_6523). The identifier should be in the `XXXX:YYYYYY:ZZZ` or `XXXX:YYYYYY`format. Where `XXXX` is a 4 digit _ICD_ (International Code Designator), `YYYYYY` is an _OID_ (Organization Identifier) with all formatting characters (dots, dashes, spaces) removed with a maximal length of 35 characters, and `ZZZ` is an optional OPI (Organization Part Identifier) with a maximum length of 35 characters. The various components (ICD, OID, OPI) are joined with a colon character (ASCII `0x3a`). Note that many existing organization identifiers defined as attributes like [leiCode](https://schema.org/leiCode) (`0199`), [duns](https://schema.org/duns) (`0060`) or [GLN](https://schema.org/globalLocationNumber) (`0088`) can be expressed using ISO-6523. If possible, ISO-6523 codes should be preferred to populating [vatID](https://schema.org/vatID) or [taxID](https://schema.org/taxID), as ISO identifiers are less ambiguous."""
    isrcCode: NamedNode
    """The International Standard Recording Code for the recording."""
    issn: NamedNode
    """The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication."""
    issueNumber: NamedNode
    """Identifies the issue of publication; for example, "iii" or "2"."""
    issuedBy: NamedNode
    """The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]]."""
    issuedThrough: NamedNode
    """The service through which the permit was granted."""
    iswcCode: NamedNode
    """The International Standard Musical Work Code for the composition."""
    item: NamedNode
    """An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')."""
    itemCondition: NamedNode
    """A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns."""
    itemDefectReturnFees: NamedNode
    """The type of return fees for returns of defect products."""
    itemDefectReturnLabelSource: NamedNode
    """The method (from an enumeration) by which the customer obtains a return shipping label for a defect product."""
    itemDefectReturnShippingFeesAmount: NamedNode
    """Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]] equals [[ReturnShippingFees]]."""
    itemListElement: NamedNode
    """For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.\n\nText values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.\n\nNote: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases."""
    itemListOrder: NamedNode
    """Type of ordering (e.g. Ascending, Descending, Unordered)."""
    itemLocation: NamedNode
    """Current location of the item."""
    itemOffered: NamedNode
    """An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer."""
    itemReviewed: NamedNode
    """The item that is being reviewed/rated."""
    itemShipped: NamedNode
    """Item(s) being shipped."""
    itinerary: NamedNode
    """Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples)."""
    iupacName: NamedNode
    """Systematic method of naming chemical compounds as recommended by the International Union of Pure and Applied Chemistry (IUPAC)."""
    jobBenefits: NamedNode
    """Description of benefits associated with the job."""
    jobImmediateStart: NamedNode
    """An indicator as to whether a position is available for an immediate start."""
    jobLocation: NamedNode
    """A (typically single) geographic location associated with the job position."""
    jobLocationType: NamedNode
    """A description of the job location (e.g. TELECOMMUTE for telecommute jobs)."""
    jobStartDate: NamedNode
    """The date on which a successful applicant for this job would be expected to start work. Choose a specific date in the future or use the jobImmediateStart property to indicate the position is to be filled as soon as possible."""
    jobTitle: NamedNode
    """The job title of the person (for example, Financial Manager)."""
    jurisdiction: NamedNode
    """Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based."""
    keywords: NamedNode
    """Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property."""
    knownVehicleDamages: NamedNode
    """A textual description of known damages, both repaired and unrepaired."""
    knows: NamedNode
    """The most generic bi-directional social/work relation."""
    knowsAbout: NamedNode
    """Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions."""
    knowsLanguage: NamedNode
    """Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47)."""
    labelDetails: NamedNode
    """Link to the drug's label details."""
    landlord: NamedNode
    """A sub property of participant. The owner of the real estate property."""
    language: NamedNode
    """A sub property of instrument. The language used on this action."""
    lastReviewed: NamedNode
    """Date on which the content on this web page was last reviewed for accuracy and/or completeness."""
    latitude: NamedNode
    """The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."""
    layoutImage: NamedNode
    """A schematic image showing the floorplan layout."""
    learningResourceType: NamedNode
    """The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'."""
    leaseLength: NamedNode
    """Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property."""
    legalName: NamedNode
    """The official name of the organization, e.g. the registered company name."""
    legalStatus: NamedNode
    """The drug or supplement's legal status, including any controlled substance schedules that apply."""
    legislationApplies: NamedNode
    """Indicates that this legislation (or part of a legislation) somehow transfers another legislation in a different legislative context. This is an informative link, and it has no legal value. For legally-binding links of transposition, use the <a href="/legislationTransposes">legislationTransposes</a> property. For example an informative consolidated law of a European Union's member state "applies" the consolidated version of the European Directive implemented in it."""
    legislationChanges: NamedNode
    """Another legislation that this legislation changes. This encompasses the notions of amendment, replacement, correction, repeal, or other types of change. This may be a direct change (textual or non-textual amendment) or a consequential or indirect change. The property is to be used to express the existence of a change relationship between two acts rather than the existence of a consolidated version of the text that shows the result of the change. For consolidation relationships, use the <a href="/legislationConsolidates">legislationConsolidates</a> property."""
    legislationConsolidates: NamedNode
    """Indicates another legislation taken into account in this consolidated legislation (which is usually the product of an editorial process that revises the legislation). This property should be used multiple times to refer to both the original version or the previous consolidated version, and to the legislations making the change."""
    legislationDate: NamedNode
    """The date of adoption or signature of the legislation. This is the date at which the text is officially aknowledged to be a legislation, even though it might not even be published or in force."""
    legislationDateVersion: NamedNode
    """The point-in-time at which the provided description of the legislation is valid (e.g.: when looking at the law on the 2016-04-07 (= dateVersion), I get the consolidation of 2015-04-12 of the "National Insurance Contributions Act 2015")"""
    legislationIdentifier: NamedNode
    """An identifier for the legislation. This can be either a string-based identifier, like the CELEX at EU level or the NOR in France, or a web-based, URL/URI identifier, like an ELI (European Legislation Identifier) or an URN-Lex."""
    legislationJurisdiction: NamedNode
    """The jurisdiction from which the legislation originates."""
    legislationLegalForce: NamedNode
    """Whether the legislation is currently in force, not in force, or partially in force."""
    legislationLegalValue: NamedNode
    """The legal value of this legislation file. The same legislation can be written in multiple files with different legal values. Typically a digitally signed PDF have a "stronger" legal value than the HTML file of the same act."""
    legislationPassedBy: NamedNode
    """The person or organization that originally passed or made the law: typically parliament (for primary legislation) or government (for secondary legislation). This indicates the "legal author" of the law, as opposed to its physical author."""
    legislationResponsible: NamedNode
    """An individual or organization that has some kind of responsibility for the legislation. Typically the ministry who is/was in charge of elaborating the legislation, or the adressee for potential questions about the legislation once it is published."""
    legislationTransposes: NamedNode
    """Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typically, some legislations of European Union's member states or regions transpose European Directives. This indicates a legally binding link between the 2 legislations."""
    legislationType: NamedNode
    """The type of the legislation. Examples of values are "law", "act", "directive", "decree", "regulation", "statutory instrument", "loi organique", "règlement grand-ducal", etc., depending on the country."""
    leiCode: NamedNode
    """An organization identifier that uniquely identifies a legal entity as defined in ISO 17442."""
    lender: NamedNode
    """A sub property of participant. The person that lends the object being borrowed."""
    lesser: NamedNode
    """This ordering relation for qualitative values indicates that the subject is lesser than the object."""
    lesserOrEqual: NamedNode
    """This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object."""
    letterer: NamedNode
    """The individual who adds lettering, including speech balloons and sound effects, to artwork."""
    license: NamedNode
    """A license document that applies to this content, typically indicated by URL."""
    line: NamedNode
    """A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space."""
    linkRelationship: NamedNode
    """Indicates the relationship type of a Web link. """
    liveBlogUpdate: NamedNode
    """An update to the LiveBlog."""
    loanMortgageMandateAmount: NamedNode
    """Amount of mortgage mandate that can be converted into a proper mortgage at a later stage."""
    loanPaymentAmount: NamedNode
    """The amount of money to pay in a single payment."""
    loanPaymentFrequency: NamedNode
    """Frequency of payments due, i.e. number of months between payments. This is defined as a frequency, i.e. the reciprocal of a period of time."""
    loanRepaymentForm: NamedNode
    """A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment."""
    loanTerm: NamedNode
    """The duration of the loan or credit agreement."""
    loanType: NamedNode
    """The type of a loan or credit."""
    location: NamedNode
    """The location of, for example, where an event is happening, where an organization is located, or where an action takes place."""
    locationCreated: NamedNode
    """The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork."""
    lodgingUnitDescription: NamedNode
    """A full description of the lodging unit."""
    lodgingUnitType: NamedNode
    """Textual description of the unit type (including suite vs. room, size of bed, etc.)."""
    logo: NamedNode
    """An associated logo."""
    longitude: NamedNode
    """The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."""
    loser: NamedNode
    """A sub property of participant. The loser of the action."""
    lowPrice: NamedNode
    """The lowest price of all offers available.\n\nUsage guidelines:\n\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    lyricist: NamedNode
    """The person who wrote the words."""
    lyrics: NamedNode
    """The words in the song."""
    mainContentOfPage: NamedNode
    """Indicates if this web page element is the main subject of the page."""
    mainEntity: NamedNode
    """Indicates the primary entity described in some page or other CreativeWork."""
    mainEntityOfPage: NamedNode
    """Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details."""
    maintainer: NamedNode
    """A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other [[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When [[maintainer]] is applied to a specific version of something e.g. a particular version or packaging of a [[Dataset]], it is always  possible that the upstream source has a different maintainer. The [[isBasedOn]] property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.
      """
    makesOffer: NamedNode
    """A pointer to products or services offered by the organization or person."""
    manufacturer: NamedNode
    """The manufacturer of the product."""
    map: NamedNode
    """A URL to a map of the place."""
    mapType: NamedNode
    """Indicates the kind of Map, from the MapCategoryType Enumeration."""
    maps: NamedNode
    """A URL to a map of the place."""
    marginOfError: NamedNode
    """A [[marginOfError]] for an [[Observation]]."""
    masthead: NamedNode
    """For a [[NewsMediaOrganization]], a link to the masthead page or a page listing top editorial management."""
    material: NamedNode
    """A material that something is made from, e.g. leather, wool, cotton, paper."""
    materialExtent: NamedNode
    """The quantity of the materials being described or an expression of the physical space they occupy."""
    mathExpression: NamedNode
    """A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable, simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or math as you would write with a keyboard."""
    maxPrice: NamedNode
    """The highest price if the price is a range."""
    maxValue: NamedNode
    """The upper value of some characteristic or property."""
    maximumAttendeeCapacity: NamedNode
    """The total number of individuals that may attend an event or venue."""
    maximumEnrollment: NamedNode
    """The maximum number of students who may be enrolled in the program."""
    maximumIntake: NamedNode
    """Recommended intake of this supplement for a given population as defined by a specific recommending authority."""
    maximumPhysicalAttendeeCapacity: NamedNode
    """The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]). """
    maximumVirtualAttendeeCapacity: NamedNode
    """The maximum virtual attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]). """
    mealService: NamedNode
    """Description of the meals that will be provided or available for purchase."""
    measuredProperty: NamedNode
    """The measuredProperty of an [[Observation]], typically via its [[StatisticalVariable]]. There are various kinds of applicable [[Property]]: a schema.org property, a property from other RDF-compatible systems, e.g. W3C RDF Data Cube, Data Commons, Wikidata, or schema.org extensions such as [GS1's](https://www.gs1.org/voc/?show=properties)."""
    measurementDenominator: NamedNode
    """Identifies the denominator variable when an observation represents a ratio or percentage."""
    measurementMethod: NamedNode
    """A subproperty of [[measurementTechnique]] that can be used for specifying specific methods, in particular via [[MeasurementMethodEnum]]."""
    measurementQualifier: NamedNode
    """Provides additional qualification to an observation. For example, a GDP observation measures the Nominal value."""
    measurementTechnique: NamedNode
    """A technique, method or technology used in an [[Observation]], [[StatisticalVariable]] or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]]; for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each [[variableMeasured]] will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [[variableMeasured]] called [[measuredProperty]] is applicable.
    
The [[measurementTechnique]] property helps when extra clarification is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. 

For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". 

If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]]. The value can also be from an enumeration, organized as a [[MeasurementMetholdEnumeration]]."""
    mechanismOfAction: NamedNode
    """The specific biochemical interaction through which this drug or supplement produces its pharmacological effect."""
    mediaAuthenticityCategory: NamedNode
    """Indicates a MediaManipulationRatingEnumeration classification of a media object (in the context of how it was published or shared)."""
    mediaItemAppearance: NamedNode
    """In the context of a [[MediaReview]], indicates specific media item(s) that are grouped using a [[MediaReviewItem]]."""
    median: NamedNode
    """The median value."""
    medicalAudience: NamedNode
    """Medical audience for page."""
    medicalSpecialty: NamedNode
    """A medical specialty of the provider."""
    medicineSystem: NamedNode
    """The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc."""
    meetsEmissionStandard: NamedNode
    """Indicates that the vehicle meets the respective emission standard."""
    member: NamedNode
    """A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals."""
    memberOf: NamedNode
    """An Organization (or ProgramMembership) to which this Person or Organization belongs."""
    members: NamedNode
    """A member of this organization."""
    membershipNumber: NamedNode
    """A unique identifier for the membership."""
    membershipPointsEarned: NamedNode
    """The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)"""
    memoryRequirements: NamedNode
    """Minimum memory requirements."""
    mentions: NamedNode
    """Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept."""
    menu: NamedNode
    """Either the actual menu as a structured representation, as text, or a URL of the menu."""
    menuAddOn: NamedNode
    """Additional menu item(s) such as a side dish of salad or side order of fries that can be added to this menu item. Additionally it can be a menu section containing allowed add-on menu items for this menu item."""
    merchant: NamedNode
    """'merchant' is an out-dated term for 'seller'."""
    merchantReturnDays: NamedNode
    """Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]]."""
    merchantReturnLink: NamedNode
    """Specifies a Web page or service by URL, for product returns."""
    messageAttachment: NamedNode
    """A CreativeWork attached to the message."""
    mileageFromOdometer: NamedNode
    """The total distance travelled by the particular vehicle since its initial production, as read from its odometer.\n\nTypical unit code(s): KMT for kilometers, SMI for statute miles."""
    minPrice: NamedNode
    """The lowest price if the price is a range."""
    minValue: NamedNode
    """The lower value of some characteristic or property."""
    minimumPaymentDue: NamedNode
    """The minimum payment required at this time."""
    missionCoveragePrioritiesPolicy: NamedNode
    """For a [[NewsMediaOrganization]], a statement on coverage priorities, including any public agenda or stance on issues."""
    mobileUrl: NamedNode
    """The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.

To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
    """
    model: NamedNode
    """The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties."""
    modelDate: NamedNode
    """The release date of a vehicle model (often used to differentiate versions of the same make and model)."""
    modifiedTime: NamedNode
    """The date and time the reservation was modified."""
    molecularFormula: NamedNode
    """The empirical formula is the simplest whole number ratio of all the atoms in a molecule."""
    molecularWeight: NamedNode
    """This is the molecular weight of the entity being described, not of the parent. Units should be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;."""
    monoisotopicMolecularWeight: NamedNode
    """The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound, ground-state, rest mass of the principal (most abundant) isotope for each element instead of the isotopic average mass. Please include the units in the form '&lt;Number&gt; &lt;unit&gt;', for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;."""
    monthlyMinimumRepaymentAmount: NamedNode
    """The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month."""
    monthsOfExperience: NamedNode
    """Indicates the minimal number of months of experience required for a position."""
    mpn: NamedNode
    """The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers."""
    multipleValues: NamedNode
    """Whether multiple values are allowed for the property.  Default is false."""
    muscleAction: NamedNode
    """The movement the muscle generates."""
    musicArrangement: NamedNode
    """An arrangement derived from the composition."""
    musicBy: NamedNode
    """The composer of the soundtrack."""
    musicCompositionForm: NamedNode
    """The type of composition (e.g. overture, sonata, symphony, etc.)."""
    musicGroupMember: NamedNode
    """A member of a music group&#x2014;for example, John, Paul, George, or Ringo."""
    musicReleaseFormat: NamedNode
    """Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.)."""
    musicalKey: NamedNode
    """The key, mode, or scale this composition uses."""
    naics: NamedNode
    """The North American Industry Classification System (NAICS) code for a particular organization or business person."""
    name: NamedNode
    """The name of the item."""
    namedPosition: NamedNode
    """A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named 'Quarterback'."""
    nationality: NamedNode
    """Nationality of the person."""
    naturalProgression: NamedNode
    """The expected progression of the condition if it is not treated and allowed to progress naturally."""
    negativeNotes: NamedNode
    """Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry 

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions 
tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list)."""
    nerve: NamedNode
    """The underlying innervation associated with the muscle."""
    nerveMotor: NamedNode
    """The neurological pathway extension that involves muscle control."""
    netWorth: NamedNode
    """The total financial value of the person as calculated by subtracting assets from liabilities."""
    newsUpdatesAndGuidelines: NamedNode
    """Indicates a page with news updates and guidelines. This could often be (but is not required to be) the main page containing [[SpecialAnnouncement]] markup on a site."""
    nextItem: NamedNode
    """A link to the ListItem that follows the current one."""
    noBylinesPolicy: NamedNode
    """For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement explaining when authors of articles are not named in bylines."""
    nonEqual: NamedNode
    """This ordering relation for qualitative values indicates that the subject is not equal to the object."""
    nonProprietaryName: NamedNode
    """The generic name of this drug or supplement."""
    nonprofitStatus: NamedNode
    """nonprofitStatus indicates the legal status of a non-profit organization in its primary place of business."""
    normalRange: NamedNode
    """Range of acceptable values for a typical patient, when applicable."""
    nsn: NamedNode
    """Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number) (nsn) of a [[Product]]. """
    numAdults: NamedNode
    """The number of adults staying in the unit."""
    numChildren: NamedNode
    """The number of children staying in the unit."""
    numConstraints: NamedNode
    """Indicates the number of constraints property values defined for a particular [[ConstraintNode]] such as [[StatisticalVariable]]. This helps applications understand if they have access to a sufficiently complete description of a [[StatisticalVariable]] or other construct that is defined using properties on template-style nodes."""
    numTracks: NamedNode
    """The number of tracks in this album or playlist."""
    numberOfAccommodationUnits: NamedNode
    """Indicates the total (available plus unavailable) number of accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]]."""
    numberOfAirbags: NamedNode
    """The number or type of airbags in the vehicle."""
    numberOfAvailableAccommodationUnits: NamedNode
    """Indicates the number of available accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAccommodationUnits]]."""
    numberOfAxles: NamedNode
    """The number of axles.\n\nTypical unit code(s): C62."""
    numberOfBathroomsTotal: NamedNode
    """The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]]."""
    numberOfBedrooms: NamedNode
    """The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]]."""
    numberOfBeds: NamedNode
    """The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment."""
    numberOfCredits: NamedNode
    """The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram."""
    numberOfDoors: NamedNode
    """The number of doors.\n\nTypical unit code(s): C62."""
    numberOfEmployees: NamedNode
    """The number of employees in an organization, e.g. business."""
    numberOfEpisodes: NamedNode
    """The number of episodes in this season or series."""
    numberOfForwardGears: NamedNode
    """The total number of forward gears available for the transmission system of the vehicle.\n\nTypical unit code(s): C62."""
    numberOfFullBathrooms: NamedNode
    """Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field)."""
    numberOfItems: NamedNode
    """The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list."""
    numberOfLoanPayments: NamedNode
    """The number of payments contractually required at origination to repay the loan. For monthly paying loans this is the number of months from the contractual first payment date to the maturity date."""
    numberOfPages: NamedNode
    """The number of pages in the book."""
    numberOfPartialBathrooms: NamedNode
    """Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field). """
    numberOfPlayers: NamedNode
    """Indicate how many people can play this game (minimum, maximum, or range)."""
    numberOfPreviousOwners: NamedNode
    """The number of owners of the vehicle, including the current one.\n\nTypical unit code(s): C62."""
    numberOfRooms: NamedNode
    """The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.
Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue."""
    numberOfSeasons: NamedNode
    """The number of seasons in this series."""
    numberedPosition: NamedNode
    """A number associated with a role in an organization, for example, the number on an athlete's jersey."""
    nutrition: NamedNode
    """Nutrition information about the recipe or menu item."""
    object: NamedNode
    """The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*."""
    observationAbout: NamedNode
    """The [[observationAbout]] property identifies an entity, often a [[Place]], associated with an [[Observation]]."""
    observationDate: NamedNode
    """The observationDate of an [[Observation]]."""
    observationPeriod: NamedNode
    """The length of time an Observation took place over. The format follows `P[0-9]*[Y|M|D|h|m|s]`. For example, P1Y is Period 1 Year, P3M is Period 3 Months, P3h is Period 3 hours."""
    occupancy: NamedNode
    """The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).
Typical unit code(s): C62 for person."""
    occupationLocation: NamedNode
    """ The region/country for which this occupational description is appropriate. Note that educational requirements and qualifications can vary between jurisdictions."""
    occupationalCategory: NamedNode
    """A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\n
Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC."""
    occupationalCredentialAwarded: NamedNode
    """A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program."""
    offerCount: NamedNode
    """The number of offers for the product."""
    offeredBy: NamedNode
    """A pointer to the organization or person making the offer."""
    offers: NamedNode
    """An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      """
    offersPrescriptionByMail: NamedNode
    """Whether prescriptions can be delivered by mail."""
    openingHours: NamedNode
    """The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.\n\n* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.\n* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. \n* Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.\n* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>."""
    openingHoursSpecification: NamedNode
    """The opening hours of a certain place."""
    opens: NamedNode
    """The opening hour of the place or service on the given day(s) of the week."""
    operatingSystem: NamedNode
    """Operating systems supported (Windows 7, OS X 10.6, Android 1.6)."""
    opponent: NamedNode
    """A sub property of participant. The opponent on this action."""
    option: NamedNode
    """A sub property of object. The options subject to this action."""
    orderDate: NamedNode
    """Date order was placed."""
    orderDelivery: NamedNode
    """The delivery of the parcel related to this order or order item."""
    orderItemNumber: NamedNode
    """The identifier of the order item."""
    orderItemStatus: NamedNode
    """The current status of the order item."""
    orderNumber: NamedNode
    """The identifier of the transaction."""
    orderQuantity: NamedNode
    """The number of the item ordered. If the property is not set, assume the quantity is one."""
    orderStatus: NamedNode
    """The current status of the order."""
    orderedItem: NamedNode
    """The item ordered."""
    organizer: NamedNode
    """An organizer of an Event."""
    originAddress: NamedNode
    """Shipper's address."""
    originalMediaContextDescription: NamedNode
    """Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]], background information that can contribute to better interpretation of the [[MediaObject]]."""
    originalMediaLink: NamedNode
    """Link to the page containing an original version of the content, or directly to an online copy of the original [[MediaObject]] content, e.g. video file."""
    originatesFrom: NamedNode
    """The vasculature the lymphatic structure originates, or afferents, from."""
    overdosage: NamedNode
    """Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response."""
    ownedFrom: NamedNode
    """The date and time of obtaining the product."""
    ownedThrough: NamedNode
    """The date and time of giving up ownership on the product."""
    ownershipFundingInfo: NamedNode
    """For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable."""
    owns: NamedNode
    """Products owned by the organization or person."""
    pageEnd: NamedNode
    """The page on which the work ends; for example "138" or "xvi"."""
    pageStart: NamedNode
    """The page on which the work starts; for example "135" or "xiii"."""
    pagination: NamedNode
    """Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49"."""
    parent: NamedNode
    """A parent of this person."""
    parentItem: NamedNode
    """The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it."""
    parentOrganization: NamedNode
    """The larger organization that this organization is a [[subOrganization]] of, if any."""
    parentService: NamedNode
    """A broadcast service to which the broadcast service may belong to such as regional variations of a national channel."""
    parentTaxon: NamedNode
    """Closest parent taxon of the taxon in question."""
    parents: NamedNode
    """A parents of the person."""
    partOfEpisode: NamedNode
    """The episode to which this clip belongs."""
    partOfInvoice: NamedNode
    """The order is being paid as part of the referenced Invoice."""
    partOfOrder: NamedNode
    """The overall order the items in this delivery were included in."""
    partOfSeason: NamedNode
    """The season to which this episode belongs."""
    partOfSeries: NamedNode
    """The series to which this episode or season belongs."""
    partOfSystem: NamedNode
    """The anatomical or organ system that this structure is part of."""
    partOfTVSeries: NamedNode
    """The TV series to which this episode or season belongs."""
    partOfTrip: NamedNode
    """Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip."""
    participant: NamedNode
    """Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*."""
    partySize: NamedNode
    """Number of people the reservation should accommodate."""
    passengerPriorityStatus: NamedNode
    """The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority)."""
    passengerSequenceNumber: NamedNode
    """The passenger's sequence number as assigned by the airline."""
    pathophysiology: NamedNode
    """Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition."""
    pattern: NamedNode
    """A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported."""
    payload: NamedNode
    """The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.\n\nTypical unit code(s): KGM for kilogram, LBR for pound\n\n* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]\n* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\n* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\n* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges."""
    paymentAccepted: NamedNode
    """Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc."""
    paymentDue: NamedNode
    """The date that payment is due."""
    paymentDueDate: NamedNode
    """The date that payment is due."""
    paymentMethod: NamedNode
    """The name of the credit card or other method of payment for the order."""
    paymentMethodId: NamedNode
    """An identifier for the method of payment used (e.g. the last 4 digits of the credit card)."""
    paymentMethodType: NamedNode
    """The type of a payment method."""
    paymentStatus: NamedNode
    """The status of payment; whether the invoice has been paid or not."""
    paymentUrl: NamedNode
    """The URL for sending a payment."""
    penciler: NamedNode
    """The individual who draws the primary narrative artwork."""
    percentile10: NamedNode
    """The 10th percentile value."""
    percentile25: NamedNode
    """The 25th percentile value."""
    percentile75: NamedNode
    """The 75th percentile value."""
    percentile90: NamedNode
    """The 90th percentile value."""
    performTime: NamedNode
    """The length of time it takes to perform instructions or a direction (not including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)."""
    performer: NamedNode
    """A performer at the event&#x2014;for example, a presenter, musician, musical group or actor."""
    performerIn: NamedNode
    """Event that this person is a performer or participant in."""
    performers: NamedNode
    """The main performer or performers of the event&#x2014;for example, a presenter, musician, or actor."""
    permissionType: NamedNode
    """The type of permission granted the person, organization, or audience."""
    permissions: NamedNode
    """Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi)."""
    permitAudience: NamedNode
    """The target audience for this permit."""
    permittedUsage: NamedNode
    """Indications regarding the permitted usage of the accommodation."""
    petsAllowed: NamedNode
    """Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value."""
    phoneticText: NamedNode
    """Representation of a text [[textValue]] using the specified [[speechToTextMarkup]]. For example the city name of Houston in IPA: /ˈhjuːstən/."""
    photo: NamedNode
    """A photograph of this place."""
    photos: NamedNode
    """Photographs of this place."""
    physicalRequirement: NamedNode
    """A description of the types of physical activity associated with the job. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term."""
    physiologicalBenefits: NamedNode
    """Specific physiologic benefits associated to the plan."""
    pickupLocation: NamedNode
    """Where a taxi will pick up a passenger or a rental car can be picked up."""
    pickupTime: NamedNode
    """When a taxi will pick up a passenger or a rental car can be picked up."""
    playMode: NamedNode
    """Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time."""
    playerType: NamedNode
    """Player type required&#x2014;for example, Flash or Silverlight."""
    playersOnline: NamedNode
    """Number of players on the server."""
    polygon: NamedNode
    """A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical."""
    populationType: NamedNode
    """Indicates the populationType common to all members of a [[StatisticalPopulation]] or all cases within the scope of a [[StatisticalVariable]]."""
    position: NamedNode
    """The position of an item in a series or sequence of items."""
    positiveNotes: NamedNode
    """Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list)."""
    possibleComplication: NamedNode
    """A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc."""
    possibleTreatment: NamedNode
    """A possible treatment to address this condition, sign or symptom."""
    postOfficeBoxNumber: NamedNode
    """The post office box number for PO box addresses."""
    postOp: NamedNode
    """A description of the postoperative procedures, care, and/or followups for this device."""
    postalCode: NamedNode
    """The postal code. For example, 94043."""
    postalCodeBegin: NamedNode
    """First postal code in a range (included)."""
    postalCodeEnd: NamedNode
    """Last postal code in the range (included). Needs to be after [[postalCodeBegin]]."""
    postalCodePrefix: NamedNode
    """A defined range of postal codes indicated by a common textual prefix. Used for non-numeric systems such as UK."""
    postalCodeRange: NamedNode
    """A defined range of postal codes."""
    potentialAction: NamedNode
    """Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role."""
    potentialUse: NamedNode
    """Intended use of the BioChemEntity by humans."""
    practicesAt: NamedNode
    """A [[MedicalOrganization]] where the [[IndividualPhysician]] practices."""
    preOp: NamedNode
    """A description of the workup, testing, and other preparations required before implanting this device."""
    predecessorOf: NamedNode
    """A pointer from a previous, often discontinued variant of the product to its newer variant."""
    pregnancyCategory: NamedNode
    """Pregnancy category of this drug."""
    pregnancyWarning: NamedNode
    """Any precaution, guidance, contraindication, etc. related to this drug's use during pregnancy."""
    prepTime: NamedNode
    """The length of time it takes to prepare the items to be used in instructions or a direction, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)."""
    preparation: NamedNode
    """Typical preparation that a patient must undergo before having the procedure performed."""
    prescribingInfo: NamedNode
    """Link to prescribing information for the drug."""
    prescriptionStatus: NamedNode
    """Indicates the status of drug prescription, e.g. local catalogs classifications or whether the drug is available by prescription or over-the-counter, etc."""
    previousItem: NamedNode
    """A link to the ListItem that precedes the current one."""
    previousStartDate: NamedNode
    """Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated."""
    price: NamedNode
    """The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.\n\nUsage guidelines:\n\n* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.\n* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
      """
    priceComponent: NamedNode
    """This property links to all [[UnitPriceSpecification]] nodes that apply in parallel for the [[CompoundPriceSpecification]] node."""
    priceComponentType: NamedNode
    """Identifies a price component (for example, a line item on an invoice), part of the total price for an offer."""
    priceCurrency: NamedNode
    """The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\n\nUse standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR"."""
    priceRange: NamedNode
    """The price range of the business, for example ```$$$```."""
    priceSpecification: NamedNode
    """One or more detailed price specifications, indicating the unit price and delivery or payment charges."""
    priceType: NamedNode
    """Defines the type of a price specified for an offered product, for example a list price, a (temporary) sale price or a manufacturer suggested retail price. If multiple prices are specified for an offer the [[priceType]] property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or as a free form text string for price types that are not already predefined in PriceTypeEnumeration."""
    priceValidUntil: NamedNode
    """The date after which the price is no longer available."""
    primaryImageOfPage: NamedNode
    """Indicates the main image on the page."""
    primaryPrevention: NamedNode
    """A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination."""
    printColumn: NamedNode
    """The number of the column in which the NewsArticle appears in the print edition."""
    printEdition: NamedNode
    """The edition of the print product in which the NewsArticle appears."""
    printPage: NamedNode
    """If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18)."""
    printSection: NamedNode
    """If this NewsArticle appears in print, this field indicates the print section in which the article appeared."""
    procedure: NamedNode
    """A description of the procedure involved in setting up, using, and/or installing the device."""
    procedureType: NamedNode
    """The type of procedure, for example Surgical, Noninvasive, or Percutaneous."""
    processingTime: NamedNode
    """Estimated processing time for the service using this channel."""
    processorRequirements: NamedNode
    """Processor architecture required to run the application (e.g. IA64)."""
    producer: NamedNode
    """The person or organization who produced the work (e.g. music album, movie, TV/radio series etc.)."""
    produces: NamedNode
    """The tangible thing generated by the service, e.g. a passport, permit, etc."""
    productGroupID: NamedNode
    """Indicates a textual identifier for a ProductGroup."""
    productID: NamedNode
    """The product identifier, such as ISBN. For example: ``` meta itemprop="productID" content="isbn:123-456-789" ```."""
    productReturnDays: NamedNode
    """The productReturnDays property indicates the number of days (from purchase) within which relevant product return policy is applicable."""
    productReturnLink: NamedNode
    """Indicates a Web page or service by URL, for product return."""
    productSupported: NamedNode
    """The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones")."""
    productionCompany: NamedNode
    """The production company or studio responsible for the item, e.g. series, video game, episode etc."""
    productionDate: NamedNode
    """The date of production of the item, e.g. vehicle."""
    proficiencyLevel: NamedNode
    """Proficiency needed for this content; expected values: 'Beginner', 'Expert'."""
    program: NamedNode
    """The [MemberProgram](https://schema.org/MemberProgram) associated with a [ProgramMembership](https://schema.org/ProgramMembership)."""
    programMembershipUsed: NamedNode
    """Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation."""
    programName: NamedNode
    """The program providing the membership. It is preferable to use [:program](https://schema.org/program) instead."""
    programPrerequisites: NamedNode
    """Prerequisites for enrolling in the program."""
    programType: NamedNode
    """The type of educational or occupational program. For example, classroom, internship, alternance, etc."""
    programmingLanguage: NamedNode
    """The computer programming language."""
    programmingModel: NamedNode
    """Indicates whether API is managed or unmanaged."""
    propertyID: NamedNode
    """A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be
(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific ID of the property), or (3)
a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).
Standards bodies should promote a standard prefix for the identifiers of properties from their standards."""
    proprietaryName: NamedNode
    """Proprietary name given to the diet plan, typically by its originator or creator."""
    proteinContent: NamedNode
    """The number of grams of protein."""
    provider: NamedNode
    """The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller."""
    providerMobility: NamedNode
    """Indicates the mobility of a provided service (e.g. 'static', 'dynamic')."""
    providesBroadcastService: NamedNode
    """The BroadcastService offered on this channel."""
    providesService: NamedNode
    """The service provided by this channel."""
    publicAccess: NamedNode
    """A flag to signal that the [[Place]] is open to public visitors.  If this property is omitted there is no assumed default boolean value."""
    publicTransportClosuresInfo: NamedNode
    """Information about public transport closures."""
    publication: NamedNode
    """A publication event associated with the item."""
    publicationType: NamedNode
    """The type of the medical article, taken from the US NLM MeSH publication type catalog. See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html)."""
    publishedBy: NamedNode
    """An agent associated with the publication event."""
    publishedOn: NamedNode
    """A broadcast service associated with the publication event."""
    publisher: NamedNode
    """The publisher of the creative work."""
    publisherImprint: NamedNode
    """The publishing division which published the comic."""
    publishingPrinciples: NamedNode
    """The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].

While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
"""
    purchaseDate: NamedNode
    """The date the item, e.g. vehicle, was purchased by the current owner."""
    qualifications: NamedNode
    """Specific qualifications required for this role or Occupation."""
    quarantineGuidelines: NamedNode
    """Guidelines about quarantine rules, e.g. in the context of a pandemic."""
    query: NamedNode
    """A sub property of instrument. The query used on this action."""
    quest: NamedNode
    """The task that a player-controlled character, or group of characters may complete in order to gain a reward."""
    question: NamedNode
    """A sub property of object. A question."""
    rangeIncludes: NamedNode
    """Relates a property to a class that constitutes (one of) the expected type(s) for values of the property."""
    ratingCount: NamedNode
    """The count of total number of ratings."""
    ratingExplanation: NamedNode
    """A short explanation (e.g. one to two sentences) providing background context and other information that led to the conclusion expressed in the rating. This is particularly applicable to ratings associated with "fact check" markup using [[ClaimReview]]."""
    ratingValue: NamedNode
    """The rating for the content.\n\nUsage guidelines:\n\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    readBy: NamedNode
    """A person who reads (performs) the audiobook."""
    readonlyValue: NamedNode
    """Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form."""
    realEstateAgent: NamedNode
    """A sub property of participant. The real estate agent involved in the action."""
    recipe: NamedNode
    """A sub property of instrument. The recipe/instructions used to perform the action."""
    recipeCategory: NamedNode
    """The category of the recipe—for example, appetizer, entree, etc."""
    recipeCuisine: NamedNode
    """The cuisine of the recipe (for example, French or Ethiopian)."""
    recipeIngredient: NamedNode
    """A single ingredient used in the recipe, e.g. sugar, flour or garlic."""
    recipeInstructions: NamedNode
    """A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered list with HowToStep and/or HowToSection items."""
    recipeYield: NamedNode
    """The quantity produced by the recipe (for example, number of people served, number of servings, etc)."""
    recipient: NamedNode
    """A sub property of participant. The participant who is at the receiving end of the action."""
    recognizedBy: NamedNode
    """An organization that acknowledges the validity, value or utility of a credential. Note: recognition may include a process of quality assurance or accreditation."""
    recognizingAuthority: NamedNode
    """If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine."""
    recommendationStrength: NamedNode
    """Strength of the guideline's recommendation (e.g. 'class I')."""
    recommendedIntake: NamedNode
    """Recommended intake of this supplement for a given population as defined by a specific recommending authority."""
    recordLabel: NamedNode
    """The label that issued the release."""
    recordedAs: NamedNode
    """An audio recording of the work."""
    recordedAt: NamedNode
    """The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event."""
    recordedIn: NamedNode
    """The CreativeWork that captured all or part of this Event."""
    recordingOf: NamedNode
    """The composition this track is a recording of."""
    recourseLoan: NamedNode
    """The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money."""
    referenceQuantity: NamedNode
    """The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity. This property is a replacement for unitOfMeasurement for the advanced cases where the price does not relate to a standard unit."""
    referencesOrder: NamedNode
    """The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice."""
    refundType: NamedNode
    """A refund type, from an enumerated list."""
    regionDrained: NamedNode
    """The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ."""
    regionsAllowed: NamedNode
    """The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166)."""
    relatedAnatomy: NamedNode
    """Anatomical systems or structures that relate to the superficial anatomy."""
    relatedCondition: NamedNode
    """A medical condition associated with this anatomy."""
    relatedDrug: NamedNode
    """Any other drug related to this one, for example commonly-prescribed alternatives."""
    relatedLink: NamedNode
    """A link related to this web page, for example to other related web pages."""
    relatedStructure: NamedNode
    """Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system."""
    relatedTherapy: NamedNode
    """A medical therapy related to this anatomy."""
    relatedTo: NamedNode
    """The most generic familial relation."""
    releaseDate: NamedNode
    """The release date of a product or product model. This can be used to distinguish the exact variant of a product."""
    releaseNotes: NamedNode
    """Description of what changed in this version."""
    releaseOf: NamedNode
    """The album this is a release of."""
    releasedEvent: NamedNode
    """The place and time the release was issued, expressed as a PublicationEvent."""
    relevantOccupation: NamedNode
    """The Occupation for the JobPosting."""
    relevantSpecialty: NamedNode
    """If applicable, a medical specialty in which this entity is relevant."""
    remainingAttendeeCapacity: NamedNode
    """The number of attendee places for an event that remain unallocated."""
    renegotiableLoan: NamedNode
    """Whether the terms for payment of interest can be renegotiated during the life of the loan."""
    repeatCount: NamedNode
    """Defines the number of times a recurring [[Event]] will take place."""
    repeatFrequency: NamedNode
    """Defines the frequency at which [[Event]]s will occur according to a schedule [[Schedule]]. The intervals between
      events should be defined as a [[Duration]] of time."""
    repetitions: NamedNode
    """Number of times one should repeat the activity."""
    replacee: NamedNode
    """A sub property of object. The object that is being replaced."""
    replacer: NamedNode
    """A sub property of object. The object that replaces."""
    replyToUrl: NamedNode
    """The URL at which a reply may be posted to the specified UserComment."""
    reportNumber: NamedNode
    """The number or other unique designator assigned to a Report by the publishing organization."""
    representativeOfPage: NamedNode
    """Indicates whether this image is representative of the content of the page."""
    requiredCollateral: NamedNode
    """Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)"""
    requiredGender: NamedNode
    """Audiences defined by a person's gender."""
    requiredMaxAge: NamedNode
    """Audiences defined by a person's maximum age."""
    requiredMinAge: NamedNode
    """Audiences defined by a person's minimum age."""
    requiredQuantity: NamedNode
    """The required quantity of the item(s)."""
    requirements: NamedNode
    """Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime)."""
    requiresSubscription: NamedNode
    """Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no')."""
    reservationFor: NamedNode
    """The thing -- flight, event, restaurant, etc. being reserved."""
    reservationId: NamedNode
    """A unique identifier for the reservation."""
    reservationStatus: NamedNode
    """The current status of the reservation."""
    reservedTicket: NamedNode
    """A ticket associated with the reservation."""
    responsibilities: NamedNode
    """Responsibilities associated with this role or Occupation."""
    restPeriods: NamedNode
    """How often one should break from the activity."""
    restockingFee: NamedNode
    """Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer."""
    result: NamedNode
    """The result produced in the action. E.g. John wrote *a book*."""
    resultComment: NamedNode
    """A sub property of result. The Comment created or sent as a result of this action."""
    resultReview: NamedNode
    """A sub property of result. The review that resulted in the performing of the action."""
    returnFees: NamedNode
    """The type of return fees for purchased products (for any return reason)."""
    returnLabelSource: NamedNode
    """The method (from an enumeration) by which the customer obtains a return shipping label for a product returned for any reason."""
    returnMethod: NamedNode
    """The type of return method offered, specified from an enumeration."""
    returnPolicyCategory: NamedNode
    """Specifies an applicable return policy (from an enumeration)."""
    returnPolicyCountry: NamedNode
    """The country where the product has to be sent to for returns, for example "Ireland" using the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this can be different from the country where the product was originally shipped from or sent to."""
    returnPolicySeasonalOverride: NamedNode
    """Seasonal override of a return policy."""
    returnShippingFeesAmount: NamedNode
    """Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]]."""
    review: NamedNode
    """A review of the item."""
    reviewAspect: NamedNode
    """This Review or Rating is relevant to this part or facet of the itemReviewed."""
    reviewBody: NamedNode
    """The actual body of the review."""
    reviewCount: NamedNode
    """The count of total number of reviews."""
    reviewRating: NamedNode
    """The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]] property applies to the review itself, as a creative work."""
    reviewedBy: NamedNode
    """People or organizations that have reviewed the content on this web page for accuracy and/or completeness."""
    reviews: NamedNode
    """Review of the item."""
    riskFactor: NamedNode
    """A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition."""
    risks: NamedNode
    """Specific physiologic risks associated to the diet plan."""
    roleName: NamedNode
    """A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'."""
    roofLoad: NamedNode
    """The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.\n\nTypical unit code(s): KGM for kilogram, LBR for pound\n\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]]\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges."""
    rsvpResponse: NamedNode
    """The response (yes, no, maybe) to the RSVP."""
    runsTo: NamedNode
    """The vasculature the lymphatic structure runs, or efferents, to."""
    runtime: NamedNode
    """Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0)."""
    runtimePlatform: NamedNode
    """Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0)."""
    rxcui: NamedNode
    """The RxCUI drug identifier from RXNORM."""
    safetyConsideration: NamedNode
    """Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement."""
    salaryCurrency: NamedNode
    """The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee."""
    salaryUponCompletion: NamedNode
    """The expected salary upon completing the training."""
    sameAs: NamedNode
    """URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website."""
    sampleType: NamedNode
    """What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template."""
    saturatedFatContent: NamedNode
    """The number of grams of saturated fat."""
    scheduleTimezone: NamedNode
    """Indicates the timezone for which the time(s) indicated in the [[Schedule]] are given. The value provided should be among those listed in the IANA Time Zone Database."""
    scheduledPaymentDate: NamedNode
    """The date the invoice is scheduled to be paid."""
    scheduledTime: NamedNode
    """The time the object is scheduled to."""
    schemaVersion: NamedNode
    """Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to
    indicate the use of a specific schema.org release, e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```. There may be situations in which other schemas might usefully be referenced this way, e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/``` but this has not been carefully explored in the community."""
    schoolClosuresInfo: NamedNode
    """Information about school closures."""
    screenCount: NamedNode
    """The number of screens in the movie theater."""
    screenshot: NamedNode
    """A link to a screenshot image of the app."""
    sdDatePublished: NamedNode
    """Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]]."""
    sdLicense: NamedNode
    """A license document that applies to this structured data, typically indicated by URL."""
    sdPublisher: NamedNode
    """Indicates the party responsible for generating and publishing the current structured data markup, typically in cases where the structured data is derived automatically from existing published content but published on a different site. For example, student projects and open data initiatives often re-publish existing content with more explicitly structured metadata. The
[[sdPublisher]] property helps make such practices more explicit."""
    season: NamedNode
    """A season in a media series."""
    seasonNumber: NamedNode
    """Position of the season within an ordered group of seasons."""
    seasons: NamedNode
    """A season in a media series."""
    seatNumber: NamedNode
    """The location of the reserved seat (e.g., 27)."""
    seatRow: NamedNode
    """The row location of the reserved seat (e.g., B)."""
    seatSection: NamedNode
    """The section location of the reserved seat (e.g. Orchestra)."""
    seatingCapacity: NamedNode
    """The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.\n\nTypical unit code(s): C62 for persons."""
    seatingType: NamedNode
    """The type/class of the seat."""
    secondaryPrevention: NamedNode
    """A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition."""
    securityClearanceRequirement: NamedNode
    """A description of any security clearance requirements of the job."""
    securityScreening: NamedNode
    """The type of security screening the passenger is subject to."""
    seeks: NamedNode
    """A pointer to products or services sought by the organization or person (demand)."""
    seller: NamedNode
    """An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider."""
    sender: NamedNode
    """A sub property of participant. The participant who is at the sending end of the action."""
    sensoryRequirement: NamedNode
    """A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term."""
    sensoryUnit: NamedNode
    """The neurological pathway extension that inputs and sends information to the brain or spinal cord."""
    serialNumber: NamedNode
    """The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer."""
    seriousAdverseOutcome: NamedNode
    """A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition."""
    serverStatus: NamedNode
    """Status of a game server."""
    servesCuisine: NamedNode
    """The cuisine of the restaurant."""
    serviceArea: NamedNode
    """The geographic area where the service is provided."""
    serviceAudience: NamedNode
    """The audience eligible for this service."""
    serviceLocation: NamedNode
    """The location (e.g. civic structure, local business, etc.) where a person can go to access the service."""
    serviceOperator: NamedNode
    """The operating organization, if different from the provider.  This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor."""
    serviceOutput: NamedNode
    """The tangible thing generated by the service, e.g. a passport, permit, etc."""
    servicePhone: NamedNode
    """The phone number to use to access the service."""
    servicePostalAddress: NamedNode
    """The address for accessing the service by mail."""
    serviceSmsNumber: NamedNode
    """The number to access the service by text message."""
    serviceType: NamedNode
    """The type of service being offered, e.g. veterans' benefits, emergency relief, etc."""
    serviceUrl: NamedNode
    """The website to access the service."""
    servingSize: NamedNode
    """The serving size, in terms of the number of volume or mass."""
    sha256: NamedNode
    """The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'."""
    sharedContent: NamedNode
    """A CreativeWork such as an image, video, or audio clip shared as part of this posting."""
    shippingDestination: NamedNode
    """indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges."""
    shippingDetails: NamedNode
    """Indicates information about the shipping policies and options associated with an [[Offer]]."""
    shippingLabel: NamedNode
    """Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference)."""
    shippingOrigin: NamedNode
    """Indicates the origin of a shipment, i.e. where it should be coming from."""
    shippingRate: NamedNode
    """The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate."""
    shippingSettingsLink: NamedNode
    """Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]] details."""
    sibling: NamedNode
    """A sibling of the person."""
    siblings: NamedNode
    """A sibling of the person."""
    signDetected: NamedNode
    """A sign detected by the test."""
    signOrSymptom: NamedNode
    """A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition."""
    significance: NamedNode
    """The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment."""
    significantLink: NamedNode
    """One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most."""
    significantLinks: NamedNode
    """The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most."""
    size: NamedNode
    """A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable. """
    sizeGroup: NamedNode
    """The size group (also known as "size type") for a product's size. Size groups are common in the fashion industry to define size segments and suggested audiences for wearable products. Multiple values can be combined, for example "men's big and tall", "petite maternity" or "regular"."""
    sizeSystem: NamedNode
    """The size system used to identify a product's size. Typically either a standard (for example, "GS1" or "ISO-EN13402"), country code (for example "US" or "JP"), or a measuring system (for example "Metric" or "Imperial")."""
    skills: NamedNode
    """A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is desired or required to fulfill this role or to work in this occupation."""
    sku: NamedNode
    """The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers."""
    slogan: NamedNode
    """A slogan or motto associated with the item."""
    smiles: NamedNode
    """A specification in form of a line notation for describing the structure of chemical species using short ASCII strings.  Double bond stereochemistry \\ indicators may need to be escaped in the string in formats where the backslash is an escape character."""
    smokingAllowed: NamedNode
    """Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room."""
    sodiumContent: NamedNode
    """The number of milligrams of sodium."""
    softwareAddOn: NamedNode
    """Additional content for a software application."""
    softwareHelp: NamedNode
    """Software application help."""
    softwareRequirements: NamedNode
    """Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime)."""
    softwareVersion: NamedNode
    """Version of the software instance."""
    sourceOrganization: NamedNode
    """The Organization on whose behalf the creator was working."""
    sourcedFrom: NamedNode
    """The neurological pathway that originates the neurons."""
    spatial: NamedNode
    """The "spatial" property can be used in cases when more specific properties
(e.g. [[locationCreated]], [[spatialCoverage]], [[contentLocation]]) are not known to be appropriate."""
    spatialCoverage: NamedNode
    """The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of
      contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates
      areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York."""
    speakable: NamedNode
    """Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.

The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:

1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.

2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.

3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.


For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this
we define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
         """
    specialCommitments: NamedNode
    """Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc."""
    specialOpeningHoursSpecification: NamedNode
    """The special opening hours of a certain place.\n\nUse this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].
      """
    specialty: NamedNode
    """One of the domain specialities to which this web page's content applies."""
    speechToTextMarkup: NamedNode
    """Form of markup used. eg. [SSML](https://www.w3.org/TR/speech-synthesis11) or [IPA](https://www.wikidata.org/wiki/Property:P898)."""
    speed: NamedNode
    """The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable under regular conditions.\n\nTypical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot\n\n*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.\n* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property."""
    spokenByCharacter: NamedNode
    """The (e.g. fictional) character, Person or Organization to whom the quotation is attributed within the containing CreativeWork."""
    sponsor: NamedNode
    """A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event."""
    sport: NamedNode
    """A type of sport (e.g. Baseball)."""
    sportsActivityLocation: NamedNode
    """A sub property of location. The sports activity location where this action occurred."""
    sportsEvent: NamedNode
    """A sub property of location. The sports event where this action occurred."""
    sportsTeam: NamedNode
    """A sub property of participant. The sports team that participated on this action."""
    spouse: NamedNode
    """The person's spouse."""
    stage: NamedNode
    """The stage of the condition, if applicable."""
    stageAsNumber: NamedNode
    """The stage represented as a number, e.g. 3."""
    starRating: NamedNode
    """An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars)."""
    startDate: NamedNode
    """The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601))."""
    startOffset: NamedNode
    """The start time of the clip expressed as the number of seconds from the beginning of the work."""
    startTime: NamedNode
    """The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.\n\nNote that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."""
    statType: NamedNode
    """Indicates the kind of statistic represented by a [[StatisticalVariable]], e.g. mean, count etc. The value of statType is a property, either from within Schema.org (e.g. [[median]], [[marginOfError]], [[maxValue]], [[minValue]]) or from other compatible (e.g. RDF) systems such as DataCommons.org or Wikidata.org. """
    status: NamedNode
    """The status of the study (enumerated)."""
    steeringPosition: NamedNode
    """The position of the steering wheel or similar device (mostly for cars)."""
    step: NamedNode
    """A single step item (as HowToStep, text, document, video, etc.) or a HowToSection."""
    stepValue: NamedNode
    """The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification."""
    steps: NamedNode
    """A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally misnamed 'steps'; 'step' is preferred)."""
    storageRequirements: NamedNode
    """Storage requirements (free space required)."""
    streetAddress: NamedNode
    """The street address. For example, 1600 Amphitheatre Pkwy."""
    strengthUnit: NamedNode
    """The units of an active ingredient's strength, e.g. mg."""
    strengthValue: NamedNode
    """The value of an active ingredient's strength, e.g. 325."""
    structuralClass: NamedNode
    """The name given to how bone physically connects to each other."""
    study: NamedNode
    """A medical study or trial related to this entity."""
    studyDesign: NamedNode
    """Specifics about the observational study design (enumerated)."""
    studyLocation: NamedNode
    """The location in which the study is taking/took place."""
    studySubject: NamedNode
    """A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study."""
    stupidProperty: NamedNode
    """This is a StupidProperty! - for testing only."""
    subEvent: NamedNode
    """An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference."""
    subEvents: NamedNode
    """Events that are a part of this event. For example, a conference event includes many presentations, each subEvents of the conference."""
    subOrganization: NamedNode
    """A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property."""
    subReservation: NamedNode
    """The individual reservations included in the package. Typically a repeated property."""
    subStageSuffix: NamedNode
    """The substage, e.g. 'a' for Stage IIIa."""
    subStructure: NamedNode
    """Component (sub-)structure(s) that comprise this anatomical structure."""
    subTest: NamedNode
    """A component test of the panel."""
    subTrip: NamedNode
    """Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip."""
    subjectOf: NamedNode
    """A CreativeWork or Event about this Thing."""
    subtitleLanguage: NamedNode
    """Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47)."""
    successorOf: NamedNode
    """A pointer from a newer variant of a product  to its previous, often discontinued predecessor."""
    sugarContent: NamedNode
    """The number of grams of sugar."""
    suggestedAge: NamedNode
    """The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers."""
    suggestedAnswer: NamedNode
    """An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site."""
    suggestedGender: NamedNode
    """The suggested gender of the intended person or audience, for example "male", "female", or "unisex"."""
    suggestedMaxAge: NamedNode
    """Maximum recommended age in years for the audience or user."""
    suggestedMeasurement: NamedNode
    """A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products."""
    suggestedMinAge: NamedNode
    """Minimum recommended age in years for the audience or user."""
    suitableForDiet: NamedNode
    """Indicates a dietary restriction or guideline for which this recipe or menu item is suitable, e.g. diabetic, halal etc."""
    superEvent: NamedNode
    """An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent."""
    supersededBy: NamedNode
    """Relates a term (i.e. a property, class or enumeration) to one that supersedes it."""
    supply: NamedNode
    """A sub-property of instrument. A supply consumed when performing instructions or a direction."""
    supplyTo: NamedNode
    """The area to which the artery supplies blood."""
    supportingData: NamedNode
    """Supporting data for a SoftwareApplication."""
    surface: NamedNode
    """A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc."""
    syllabusSections: NamedNode
    """Indicates (typically several) Syllabus entities that lay out what each section of the overall course will cover."""
    target: NamedNode
    """Indicates a target EntryPoint, or url, for an Action."""
    targetCollection: NamedNode
    """A sub property of object. The collection target of the action."""
    targetDescription: NamedNode
    """The description of a node in an established educational framework."""
    targetName: NamedNode
    """The name of a node in an established educational framework."""
    targetPlatform: NamedNode
    """Type of app development: phone, Metro style, desktop, XBox, etc."""
    targetPopulation: NamedNode
    """Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'."""
    targetProduct: NamedNode
    """Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used."""
    targetUrl: NamedNode
    """The URL of a node in an established educational framework."""
    taxID: NamedNode
    """The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain."""
    taxonRank: NamedNode
    """The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary – typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs."""
    taxonomicRange: NamedNode
    """The taxonomic grouping of the organism that expresses, encodes, or in some way related to the BioChemEntity."""
    teaches: NamedNode
    """The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term."""
    telephone: NamedNode
    """The telephone number."""
    temporal: NamedNode
    """The "temporal" property can be used in cases where more specific properties
(e.g. [[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]]) are not known to be appropriate."""
    temporalCoverage: NamedNode
    """The temporalCoverage of a CreativeWork indicates the period that the content applies to, i.e. that it describes, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In
      the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL.
      Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".

Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated."""
    termCode: NamedNode
    """A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]."""
    termDuration: NamedNode
    """The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term."""
    termsOfService: NamedNode
    """Human-readable terms of service documentation."""
    termsPerYear: NamedNode
    """The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2."""
    text: NamedNode
    """The textual content of this CreativeWork."""
    textValue: NamedNode
    """Text value being annotated."""
    thumbnail: NamedNode
    """Thumbnail image for an image or video."""
    thumbnailUrl: NamedNode
    """A thumbnail image relevant to the Thing."""
    tickerSymbol: NamedNode
    """The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we recommend using the controlled vocabulary of Market Identifier Codes (MIC) specified in ISO 15022."""
    ticketNumber: NamedNode
    """The unique identifier for the ticket."""
    ticketToken: NamedNode
    """Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance."""
    ticketedSeat: NamedNode
    """The seat associated with the ticket."""
    timeOfDay: NamedNode
    """The time of day the program normally runs. For example, "evenings"."""
    timeRequired: NamedNode
    """Approximate or typical time it usually takes to work with or through the content of this work for the typical or target audience."""
    timeToComplete: NamedNode
    """The expected length of time to complete the program if attending full-time."""
    tissueSample: NamedNode
    """The type of tissue sample required for the test."""
    title: NamedNode
    """The title of the job."""
    titleEIDR: NamedNode
    """An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television.

For example, the motion picture known as "Ghostbusters" has a titleEIDR of  "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]].

Since schema.org types like [[Movie]], [[TVEpisode]], [[TVSeason]], and [[TVSeries]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
"""
    toLocation: NamedNode
    """A sub property of location. The final location of the object or the agent after the action."""
    toRecipient: NamedNode
    """A sub property of recipient. The recipient who was directly sent the message."""
    tocContinuation: NamedNode
    """A [[HyperTocEntry]] can have a [[tocContinuation]] indicated, which is another [[HyperTocEntry]] that would be the default next item to play or render."""
    tocEntry: NamedNode
    """Indicates a [[HyperTocEntry]] in a [[HyperToc]]."""
    tongueWeight: NamedNode
    """The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR).\n\nTypical unit code(s): KGM for kilogram, LBR for pound\n\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges."""
    tool: NamedNode
    """A sub property of instrument. An object used (but not consumed) when performing instructions or a direction."""
    torque: NamedNode
    """The torque (turning force) of the vehicle's engine.\n\nTypical unit code(s): NU for newton metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch\n\n* Note 1: You can link to information about how the given value has been determined (e.g. reference RPM) using the [[valueReference]] property.\n* Note 2: You can use [[minValue]] and [[maxValue]] to indicate ranges."""
    totalHistoricalEnrollment: NamedNode
    """The total number of students that have enrolled in the history of the course."""
    totalJobOpenings: NamedNode
    """The number of positions open for this job posting. Use a positive integer. Do not use if the number of positions is unclear or not known."""
    totalPaymentDue: NamedNode
    """The total amount due."""
    totalPrice: NamedNode
    """The total price for the reservation or ticket, including applicable taxes, shipping, etc.\n\nUsage guidelines:\n\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    totalTime: NamedNode
    """The total time required to perform instructions or a direction (including time to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)."""
    tourBookingPage: NamedNode
    """A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate."""
    touristType: NamedNode
    """Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular country, etc. """
    track: NamedNode
    """A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording."""
    trackingNumber: NamedNode
    """Shipper tracking number."""
    trackingUrl: NamedNode
    """Tracking url for the parcel delivery."""
    tracks: NamedNode
    """A music recording (track)&#x2014;usually a single song."""
    trailer: NamedNode
    """The trailer of a movie or TV/radio series, season, episode, etc."""
    trailerWeight: NamedNode
    """The permitted weight of a trailer attached to the vehicle.\n\nTypical unit code(s): KGM for kilogram, LBR for pound\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges."""
    trainName: NamedNode
    """The name of the train (e.g. The Orient Express)."""
    trainNumber: NamedNode
    """The unique identifier for the train."""
    trainingSalary: NamedNode
    """The estimated salary earned while in the program."""
    transFatContent: NamedNode
    """The number of grams of trans fat."""
    transcript: NamedNode
    """If this MediaObject is an AudioObject or VideoObject, the transcript of that object."""
    transitTime: NamedNode
    """The typical delay the order has been sent for delivery and the goods reach the final customer. Typical properties: minValue, maxValue, unitCode (d for DAY)."""
    transitTimeLabel: NamedNode
    """Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference)."""
    translationOfWork: NamedNode
    """The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the Origin of Species”."""
    translator: NamedNode
    """Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event."""
    transmissionMethod: NamedNode
    """How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc."""
    travelBans: NamedNode
    """Information about travel bans, e.g. in the context of a pandemic."""
    trialDesign: NamedNode
    """Specifics about the trial design (enumerated)."""
    tributary: NamedNode
    """The anatomical or organ system that the vein flows into; a larger structure that the vein connects to."""
    tripOrigin: NamedNode
    """The location of origin of the trip, prior to any destination(s)."""
    typeOfBed: NamedNode
    """The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity indicated by quantity."""
    typeOfGood: NamedNode
    """The product that this structured value is referring to."""
    typicalAgeRange: NamedNode
    """The typical expected age range, e.g. '7-9', '11-'."""
    typicalCreditsPerTerm: NamedNode
    """The number of credits or units a full-time student would be expected to take in 1 term however 'term' is defined by the institution."""
    typicalTest: NamedNode
    """A medical test typically performed given this condition."""
    underName: NamedNode
    """The person or organization the reservation or ticket is for."""
    unitCode: NamedNode
    """The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon."""
    unitText: NamedNode
    """A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>."""
    unnamedSourcesPolicy: NamedNode
    """For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required."""
    unsaturatedFatContent: NamedNode
    """The number of grams of unsaturated fat."""
    uploadDate: NamedNode
    """Date (including time if available) when this media object was uploaded to this site."""
    upvoteCount: NamedNode
    """The number of upvotes this question, answer or comment has received from the community."""
    url: NamedNode
    """URL of the item."""
    urlTemplate: NamedNode
    """An url template (RFC6570) that will be used to construct the target of the execution of the action."""
    usNPI: NamedNode
    """A <a href="https://en.wikipedia.org/wiki/National_Provider_Identifier">National Provider Identifier</a> (NPI) 
    is a unique 10-digit identification number issued to health care providers in the United States by the Centers for Medicare and Medicaid Services."""
    usageInfo: NamedNode
    """The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]. This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.

This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses."""
    usedToDiagnose: NamedNode
    """A condition the test is used to diagnose."""
    userInteractionCount: NamedNode
    """The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."""
    usesDevice: NamedNode
    """Device used to perform the test."""
    usesHealthPlanIdStandard: NamedNode
    """The standard for interpreting the Plan ID. The preferred is "HIOS". See the Centers for Medicare & Medicaid Services for more details."""
    utterances: NamedNode
    """Text of an utterances (spoken words, lyrics etc.) that occurs at a certain section of a media object, represented as a [[HyperTocEntry]]."""
    validFor: NamedNode
    """The duration of validity of a permit or similar thing."""
    validForMemberTier: NamedNode
    """The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for."""
    validFrom: NamedNode
    """The date when the item becomes valid."""
    validIn: NamedNode
    """The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]]. """
    validThrough: NamedNode
    """The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours."""
    validUntil: NamedNode
    """The date when the item is no longer valid."""
    value: NamedNode
    """The value of a [[QuantitativeValue]] (including [[Observation]]) or property value node.\n\n* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.\n* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.\n* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\n* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator."""
    valueAddedTaxIncluded: NamedNode
    """Specifies whether the applicable value-added tax (VAT) is included in the price specification or not."""
    valueMaxLength: NamedNode
    """Specifies the allowed range for number of characters in a literal value."""
    valueMinLength: NamedNode
    """Specifies the minimum allowed range for number of characters in a literal value."""
    valueName: NamedNode
    """Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name."""
    valuePattern: NamedNode
    """Specifies a regular expression for testing literal values according to the HTML spec."""
    valueReference: NamedNode
    """A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement."""
    valueRequired: NamedNode
    """Whether the property must be filled in to complete the action.  Default is false."""
    variableMeasured: NamedNode
    """The variableMeasured property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue, or more explicitly as a [[StatisticalVariable]]."""
    variablesMeasured: NamedNode
    """Originally named [[variablesMeasured]], the [[variableMeasured]] property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue."""
    variantCover: NamedNode
    """A description of the variant cover
    	for the issue, if the issue is a variant printing. For example, "Bryan Hitch
    	Variant Cover" or "2nd Printing Variant"."""
    variesBy: NamedNode
    """Indicates the property or properties by which the variants in a [[ProductGroup]] vary, e.g. their size, color etc. Schema.org properties can be referenced by their short name e.g. "color"; terms defined elsewhere can be referenced with their URIs."""
    vatID: NamedNode
    """The Value-added Tax ID of the organization or person."""
    vehicleConfiguration: NamedNode
    """A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'."""
    vehicleEngine: NamedNode
    """Information about the engine or engines of the vehicle."""
    vehicleIdentificationNumber: NamedNode
    """The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles."""
    vehicleInteriorColor: NamedNode
    """The color or color combination of the interior of the vehicle."""
    vehicleInteriorType: NamedNode
    """The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience."""
    vehicleModelDate: NamedNode
    """The release date of a vehicle model (often used to differentiate versions of the same make and model)."""
    vehicleSeatingCapacity: NamedNode
    """The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.\n\nTypical unit code(s): C62 for persons."""
    vehicleSpecialUsage: NamedNode
    """Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale."""
    vehicleTransmission: NamedNode
    """The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars)."""
    vendor: NamedNode
    """'vendor' is an earlier term for 'seller'."""
    verificationFactCheckingPolicy: NamedNode
    """Disclosure about verification and fact-checking processes for a [[NewsMediaOrganization]] or other fact-checking [[Organization]]."""
    version: NamedNode
    """The version of the CreativeWork embodied by a specified resource."""
    video: NamedNode
    """An embedded video object."""
    videoFormat: NamedNode
    """The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.)."""
    videoFrameSize: NamedNode
    """The frame size of the video."""
    videoQuality: NamedNode
    """The quality of the video."""
    volumeNumber: NamedNode
    """Identifies the volume of publication or multi-part work; for example, "iii" or "2"."""
    warning: NamedNode
    """Any FDA or other warnings about the drug (text or URL)."""
    warranty: NamedNode
    """The warranty promise(s) included in the offer."""
    warrantyPromise: NamedNode
    """The warranty promise(s) included in the offer."""
    warrantyScope: NamedNode
    """The scope of the warranty promise."""
    webCheckinTime: NamedNode
    """The time when a passenger can check into the flight online."""
    webFeed: NamedNode
    """The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped updates. This is usually RSS or Atom."""
    weight: NamedNode
    """The weight of the product or person."""
    weightTotal: NamedNode
    """The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.\n\nTypical unit code(s): KGM for kilogram, LBR for pound\n\n* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\n* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\n* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges."""
    wheelbase: NamedNode
    """The distance between the centers of the front and rear wheels.\n\nTypical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet."""
    width: NamedNode
    """The width of the item."""
    winner: NamedNode
    """A sub property of participant. The winner of the action."""
    wordCount: NamedNode
    """The number of words in the text of the Article."""
    workExample: NamedNode
    """Example/instance/realization/derivation of the concept of this creative work. E.g. the paperback edition, first edition, or e-book."""
    workFeatured: NamedNode
    """A work featured in some event, e.g. exhibited in an ExhibitionEvent.
       Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent)."""
    workHours: NamedNode
    """The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm)."""
    workLocation: NamedNode
    """A contact location for a person's place of work."""
    workPerformed: NamedNode
    """A work performed in some event, for example a play performed in a TheaterEvent."""
    workPresented: NamedNode
    """The movie presented during this event."""
    workTranslation: NamedNode
    """A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation “Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese  translation Tây du ký bình khảo."""
    workload: NamedNode
    """Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure."""
    worksFor: NamedNode
    """Organizations that the person works for."""
    worstRating: NamedNode
    """The lowest value allowed in this rating system."""
    xpath: NamedNode
    """An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element"."""
    yearBuilt: NamedNode
    """The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field). """
    yearlyRevenue: NamedNode
    """The size of the business in annual revenue."""
    yearsInOperation: NamedNode
    """The age of the business."""
