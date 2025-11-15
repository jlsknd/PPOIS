Logistics and Transport Management System
==========================================

AccessControl 2 4 →
Account 6 3 → Transaction
Analytics 2 4 →
BankCard 7 5 → Payment
Camera 4 3 →
Cargo 10 5 →
Container 9 4 →
CustomerFeedback 3 2 →
CustomerSupport 2 3 →
CustomsService 2 3 → Shipment
Dashboard 1 3 →
Delivery 10 6 → Shipment, Vehicle, Driver, Route
Department 6 5 → Employee, Manager
Dispatcher 3 3 → Route
Driver 7 4 → Vehicle
Employee 10 4 → Department
ExpressDelivery 3 2 →
Fleet 4 5 → Vehicle
FreightService 4 3 → Shipment
GPSTracker 4 4 →
InsuranceService 2 2 → Shipment
Inventory 2 5 →
Invoice 10 4 → Payment
KPI 1 3 →
LoadingDock 5 5 → Vehicle
LoadingSchedule 2 5 →
LogisticsCenter 9 7 → Warehouse, LoadingDock
MaintenanceSchedule 1 3 →
Manager 4 3 → Employee
Notification 5 3 →
PackagingService 1 2 →
Payment 7 4 → PaymentProcessor
PaymentProcessor 1 3 → Payment, BankCard
PerformanceMetrics 1 4 →
Receipt 4 2 → Payment
Report 4 3 →
Route 8 4 → Delivery
SecuritySystem 4 5 → Camera
Shipment 14 7 →
StorageZone 6 4 →
SubscriptionService 4 3 →
Survey 3 2 →
TrackingSystem 1 5 →
Transaction 6 2 → Account
Truck 4 2 →
Van 2 0 →
Vehicle 14 8 →
Warehouse 9 6 → StorageZone, Inventory
WarehouseService 2 3 →
WarehouseWorker 5 3 → Warehouse

Exceptions (13):
----------------

DeliveryDelayedError 0 1
DocumentMissingError 0 1
InsufficientCapacityError 0 1
InsufficientFundsError 0 1
InvalidDateError 0 1
InvalidPasswordError 0 1
InvalidRouteError 0 1
LogisticsException 1 1
OverweightError 0 1
PaymentProcessingError 0 1
ShipmentNotFoundError 0 1
UnauthorizedAccessError 0 1
VehicleUnavailableError 0 1

Итоги
-----
Классы: 50
Поля: 242
Поведения: 187
Ассоциации: 30
Исключения: 13
