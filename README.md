# Project API requests

## front end
```
I need to request for 4 objects resources(items), shipments, processes, and orders
```

## resources
```
resources involve being able to add, update, and delete resource types
each resource type will have an amount attached there won't be two of a single resource type
```

## shipments
```
shipments involve being able to add, update, and delete shipments
shipments involve incoming resources types with certian amounts along with the ability to see completed shipments
```

## processes
```
processes involve being able to add, update, and delete processes
each process should be built in with an certian items per second
I will do calculations to determine estimated time depending on the amount wanted for creation
```

## orders
```
orders involve being able to add, update, and delete orders
orders involve outgoing resources types with certian amounts along with the ability to see completed orders
```

# Endpoints

```
GET /products - list candies/inventory
POST /products - add new Wonka candies
PUT /products/{id} - update stock levels
DELETE /products/{id} - remove bad products
POST /transactions - record stock movements
```
