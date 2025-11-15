Museum Management System
========================

AccessControl 2 5 →
Account 5 7 → Transaction
Administrator 5 5 →
Analytics 3 6 → Visitor
Artifact 7 7 →
ArtifactCatalog 2 6 → Artifact
AudioGuide 5 5 → Visitor
BankCard 5 7 → Payment, PaymentProcessor, Wallet
Building 4 4 → Room
Cafe 5 5 → MenuItem, Visitor
Camera 4 5 →
ClimateControl 3 5 → Room
Collection 4 6 → Artifact, Curator
Curator 4 5 → Artifact, Exhibit, Exhibition
Department 4 6 → Employee
Donation 5 3 →
Employee 6 6 → Department
Event 5 5 → Sponsor, Visitor
Exhibit 7 8 → Artifact
Exhibition 5 5 → Exhibit, Sponsor
Feedback 5 3 → Visitor
GiftShop 3 4 → Payment, Product
Guide 4 5 → Tour, VisitorGroup
Membership 6 6 → Visitor
MenuItem 4 4 →
Museum 7 8 → Exhibit, Visitor
Newsletter 4 4 →
Notification 5 4 →
Parking 4 4 →
Payment 6 6 → PaymentProcessor, Receipt, TicketOffice, Workshop
PaymentProcessor 2 5 → BankCard, Payment
Product 4 4 →
Receipt 4 4 → Payment
Report 4 4 →
Reservation 5 4 → Visitor
Room 6 4 → ClimateControl
Schedule 3 5 → Employee
SecurityGuard 4 5 →
SecuritySystem 4 7 → Camera
Sponsor 4 4 → Event, Exhibit
Statistics 1 5 →
StorageRoom 4 5 → Artifact
Survey 3 4 →
Ticket 7 6 → Visitor
TicketOffice 4 6 → Museum, Payment, Ticket, Visitor
Tour 6 5 → Guide, Visitor
Transaction 5 4 → Account
Visitor 6 6 → Exhibit, Ticket
VisitorGroup 4 6 → Guide, Visitor
Wallet 4 6 → BankCard
Workshop 5 4 → Payment, Visitor

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
Поведения: 262
Ассоциации: 60
Исключения: 13

