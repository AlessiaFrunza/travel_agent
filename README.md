# Travel Agent
*Full-stack travel planning web-app - currently in development*

## Architecture & Design Choices

## Database Schema
- Used a `Trip_Destination` junction table instead of array columns to keep the schema normalised and support efficient querying across destinations
- `Booking` is modelled separately from `Trip` to allow a trip to have multiple bookings without duplicating trip data
- `Daily_Itinerary` has a composite primary key made from the foreign key from `Trip` combined with the day number of the trip

## Branching Strategy

This project follows the following branching strategy:
- `main` is the primary branch that represents the production-ready code
- `dev` is the integration branch for all feature development
- `feat/*` are short lived branches created for developing specific features
- `bugfix/*` are also short lived branches created for fixes in preparing releases

![Git flow that this project follows (image created  by author)](./graphics/git_flow.png)

