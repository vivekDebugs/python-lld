# Design a Food Delivery App

## Requirements:
- Support multiple restaurants, each with their own menu
- Users can search for restaurants/dishes and place orders
- Real-time order tracking for users
- Assign a delivery partner to an order based on proximity
- Support for different payment methods
- Calculate total cost including taxes, delivery fees, and discounts
- Rating and review system for restaurants and delivery partners

## Design
### Entities
- Restaurant
- MenuItem
- User
- DeliveryAgent
- Order

**MenuItem**
- name: str
- price: Float
- isAvailable: Boolean

**Restaurant**
- name: str
- menuItems: Dict[str, MenuItem]

**RestaurantService**
- createRestaurant(): Restaurant
- createMenuItem(): MenuItem

**User**
- name: str
- phone: str
- notify(): None

**OrderItem**
- item: Item
- quantity: Integer

**OrderStatus(Enum)**
- PLACED
- ON_THE_WAY
- DELIVERED

**Order**
- restaurant: Restaurant
- orderItems: List[OrderItem]
- user: User
- deliveryAgent: DeliveryAgent
- status: OrderStatus
- orderTotal: Float
- deliveryCharges: Float

**OrderService**
- placeOrder(): Order // creates order and calls assignDeliveryAgent()
- assignDeliveryAgent(): DeliveryAgent // assigns a delivery agent using strategy pattern and notifies the agent
- pickOrder(): None // changes the order status and notifies the user
- deliverOrder(): None // changes the order status and frees the delivery agent

**DeliveryAgentStatus(Enum)**
- AVAILABLE
- BOOKED
- OFFLINE

**DeliveryAgent**
- name: str
- phone: str
- status: DeliveryAgentStatus
- notify(): None

**FoodDeliverySystem**
- orderService: OrderService
- restaurantService: RestaurantService
- createUser(): User
- createDeliveryAgent(): DeliveryAgent
- createRestaurant(): Restaurant
- createMenuItem(): MenuItem
- placeOrder(): Order
- pickOrder(): None
- deliverOrder(): None
