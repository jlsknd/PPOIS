Museum Management System
========================

AccessControl 2 4 →
Account 5 6 → Transaction
Administrator 5 4 →
Analytics 3 5 → Visitor
Artifact 7 6 →
ArtifactCatalog 2 5 → Artifact
AudioGuide 5 4 → Visitor
BankCard 5 6 → Payment, PaymentProcessor, Wallet
Building 4 3 → Room
Cafe 5 4 → MenuItem, Visitor
Camera 4 4 →
ClimateControl 3 4 → Room
Collection 4 5 → Artifact, Curator
Curator 4 4 → Artifact, Exhibit, Exhibition
Department 4 5 → Employee
Donation 5 2 →
Employee 6 5 → Department
Event 5 4 → Sponsor, Visitor
Exhibit 7 7 → Artifact
Exhibition 5 4 → Exhibit, Sponsor
Feedback 5 2 → Visitor
GiftShop 3 3 → Payment, Product
Guide 4 4 → Tour, VisitorGroup
Membership 6 5 → Visitor
MenuItem 4 3 →
Museum 7 7 → Exhibit, Visitor
Newsletter 4 3 →
Notification 5 3 →
Parking 4 3 →
Payment 6 5 → PaymentProcessor, Receipt, TicketOffice, Workshop
PaymentProcessor 2 4 → BankCard, Payment
Product 4 3 →
Receipt 4 3 → Payment
Report 4 3 →
Reservation 5 3 → Visitor
Room 6 3 → ClimateControl
Schedule 3 4 → Employee
SecurityGuard 4 4 →
SecuritySystem 4 6 → Camera
Sponsor 4 3 → Event, Exhibit
Statistics 1 4 →
StorageRoom 4 4 → Artifact
Survey 3 3 →
Ticket 7 5 → Visitor
TicketOffice 4 5 → Museum, Payment, Ticket, Visitor
Tour 6 4 → Guide, Visitor
Transaction 5 3 → Account
Visitor 6 5 → Exhibit, Ticket
VisitorGroup 4 5 → Guide, Visitor
Wallet 4 5 → BankCard
Workshop 5 3 → Payment, Visitor

Exceptions (13):
----------------

ArtifactDamageError 0 1 →
ArtifactNotFoundError 1 1 →
CapacityExceededError 0 1 →
ExhibitClosedError 0 1 →
InsufficientFundsError 1 1 →
InvalidDateError 1 1 →
InvalidPasswordError 0 1 →
MembershipExpiredError 1 1 →
MuseumException 1 1 →
PaymentProcessingError 1 1 →
SecurityViolationError 0 1 →
TicketValidationError 0 1 →
UnauthorizedAccessError 1 1 →

Итоги
-----
Классы: 51
Поля: 227
Поведения: 211
Ассоциации: 34
Исключения: 13

